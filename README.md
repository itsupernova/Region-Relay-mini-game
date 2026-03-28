# 🎮 Pokémon Region Relay Discord Bot

A fast-paced, luck-based Discord game where players race to complete region sequences using randomly drawn Pokémon.

No economy. No grinding. Just pure chaos and clutch RNG.

---

## 🚀 Features

* 🎯 Multiplayer game (2–4 players)
* 🎲 Random Pokémon draws (with sprites!)
* 🌍 Region-based sequence matching
* 🏆 Automatic ranking system (1st → last)
* 🔁 Round-based elimination gameplay
* 🎨 Clean embed-based visuals

---

## 🧠 How the Game Works

1. Players start the game using:

   ```
   !relaygame @player1 @player2 ...
   ```

2. Each player gets up to **10 Pokémon draws per turn**

3. The bot checks if the player completes **any of these sequences (in order):**

   * Johto → Kalos → Alola
   * Alola → Kalos → Johto
   * Kalos → Alola → Galar
   * Galar → Alola → Kalos

4. ✅ If a player completes a sequence:

   * They secure the **next rank (🥇 first, then 🥈, etc.)**
   * They are removed from the game

5. ❌ If no one succeeds:

   * A new round starts with remaining players

6. 🔚 Game ends when only one player remains

---

## 🖼️ Pokémon Draw System

Each draw shows:

* Pokémon ID
* Region
* Sprite image (via PokéAPI)

Example:

> 🎲 Player drew Pokémon #158
> 🌍 Region: Johto
> 🖼️ (Sprite displayed)

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/region-relay-bot.git
cd region-relay-bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create a `.env` file

```
DISCORD_TOKEN=your_bot_token_here
```

### 4. Run the bot

```
python main_bot_file.py
```

---

## 🧩 Requirements

* Python 3.8+
* discord.py
* python-dotenv

---

## 🔐 Bot Permissions

Make sure your bot has:

* Read Messages
* Send Messages
* Embed Links
* Read Message History

---

## 📌 Notes

* Only mentioned users are included in the game
* Region detection is based on Pokémon ID ranges
* Sequences do **not** need to be consecutive draws, only in order

---

## 🌟 Future Ideas

* Leaderboards 📊
* Cooldown system ⏱️
* Animated draw reveals 🎥
* Web dashboard integration 🌐

---

## 🧑‍💻 Author

Built by Nova
Fueled by Pokémon, probability, and a bit of chaos ⚡

---

## 📜 License

This project is open-source and free to use.
