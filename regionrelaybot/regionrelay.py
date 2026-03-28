import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("Error: DISCORD_TOKEN is missing.")
    exit()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MAX_POKEMON_ID = 1025
ATTEMPTS_PER_TURN = 10
MIN_PLAYERS = 2
MAX_PLAYERS = 4

REGION_RANGES = {
    "Johto": range(152, 252),
    "Kalos": range(650, 722),
    "Alola": range(722, 810),
    "Galar": range(810, 906),
}

VALID_PATTERNS = [
    ["Johto", "Kalos", "Alola"],
    ["Alola", "Kalos", "Johto"],
    ["Kalos", "Alola", "Galar"],
    ["Galar", "Alola", "Kalos"]
]

def draw_pokemon():
    poke_id = random.randint(1, MAX_POKEMON_ID)
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
    return poke_id, sprite_url


def get_region(poke_id):
    for region, rng in REGION_RANGES.items():
        if poke_id in rng:
            return region
    return None


def check_sequence(regions):
    for pattern in VALID_PATTERNS:
        idx = 0
        for r in regions:
            if r == pattern[idx]:
                idx += 1
                if idx == len(pattern):
                    return True, pattern
    return False, None


async def play_turn(ctx, player):
    seen = []

    for attempt in range(ATTEMPTS_PER_TURN):
        poke_id, sprite = draw_pokemon()
        region = get_region(poke_id)

        if region:
            seen.append(region)

        embed = discord.Embed(
            title=f"🎲 {player.display_name} drew Pokémon #{poke_id}",
            description=f"Region: {region if region else 'Unknown'}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=sprite)

        await ctx.send(embed=embed)

        success, pattern = check_sequence(seen)
        if success:
            return True, seen, pattern

    return False, seen, None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="relaygame")
async def relaygame(ctx):
    players = [m for m in ctx.message.mentions]

    if not (MIN_PLAYERS <= len(players) <= MAX_PLAYERS):
        return await ctx.send(f"Mention {MIN_PLAYERS}-{MAX_PLAYERS} players.")

    standings = []
    active_players = players.copy()

    await ctx.send(f"Game starting with: {', '.join(p.mention for p in players)}")

    round_num = 1

    while len(active_players) > 1:
        await ctx.send(f"\n--- Round {round_num} ---")

        winners = []

        for player in active_players:
            await ctx.send(f"🎮 {player.mention}'s turn...")
            success, seen, pattern = await play_turn(ctx, player)

            seq = " -> ".join(seen) if seen else "None"

            if success:
                await ctx.send(f"🏆 {player.mention} matched {pattern}!\nSequence: {seq}")
                winners.append(player)
            else:
                await ctx.send(f"❌ {player.mention} failed. Sequence: {seq}")

        if winners:
            first_winner = winners[0]
            standings.append(first_winner)
            await ctx.send(f"🥇 {first_winner.mention} takes this position!")

            active_players.remove(first_winner)
        else:
            await ctx.send("No one succeeded this round. Retrying...")

        round_num += 1

    standings.append(active_players[0])

    result = "\n🏁 Final Standings:\n"
    medals = ["🥇", "🥈", "🥉", "🏅"]

    for i, player in enumerate(standings):
        medal = medals[i] if i < len(medals) else ""
        result += f"{medal} {player.mention}\n"

    await ctx.send(result)

bot.run(TOKEN)
