# 🤖 AI Mention Bot

A feature-rich Telegram mention/tagging bot built with Pyrogram.

## Features

- `/tagall`, `/hitag`, `/entag`, `/gmtag`, `/gntag`, `/jtag`, `/vctag`
- `/all` or `@all` — Tag all members (supports custom message)
- `/admin` or `@admin` — Tag admins only (supports custom message)
- `/stop`, `/pause`, `/resume` — Control tagging (admins only)
- `/broadcast` — Broadcast to all users & groups (owner only)
- `/stats` — Bot statistics (owner only)

## Deploy on Heroku

### Step 1 — Fork & Clone
```
git clone https://github.com/yourusername/AIMentionBot
cd AIMentionBot
```

### Step 2 — Create Heroku App
```
heroku create your-app-name
```

### Step 3 — Set Config Vars
```
heroku config:set API_ID=12345678
heroku config:set API_HASH=your_api_hash
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set MONGO_URI=your_mongodb_uri
heroku config:set OWNER_ID=your_telegram_id
```

### Step 4 — Deploy
```
git push heroku main
```

### Step 5 — Start Worker Dyno
```
heroku ps:scale worker=1
```

## Config Vars

| Variable | Description |
|----------|-------------|
| `API_ID` | From my.telegram.org |
| `API_HASH` | From my.telegram.org |
| `BOT_TOKEN` | From @BotFather |
| `MONGO_URI` | MongoDB Atlas connection string |
| `OWNER_ID` | Your Telegram user ID |

## Local Run

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill .env with your values
python -m AIMentionBot
```
