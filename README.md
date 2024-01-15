<div align="center">
  <h3>⏫ Discord Tools - Level Up Selfbot ⏫</h3>
 </div>
<h3 align="center">Automatically sends random message</h3>
<h4 align="center">⭐ Don't forget to leave a star! ⭐</h4>

## Requirement
* Python3

## Feature
* Custom text ID & EN
* Custom delay time
* You can choose remove message after send or not
* Multiple Account
* Push notification to your telegram bot

## Configuration
set Configuration settings in (https://github.com/0xtbug/discord-tools/blob/main/config.json) `config.json`
   ```
    "accounts": [
      {
        "id": "your_discord_id",
        "token": "your_discord_token"
      },
      {
        "id": "your_discord_id",
        "token": "your_discord_token"
      }
      // unlimited how many accounts you want
    ],
   ```

## Windows:
1. Open install.bat
2. Open start.bat
3. In channel write `!lp <amount of messages>`

## Linux:
~~~
pkg install python3
~~~

~~~
pip install -r requirements.txt 
~~~

~~~
python3 main.py
~~~

## Showcase:

<img width="450" alt="nyoevUc4x0" src="https://github.com/0xtbug/discord-tools/assets/54710482/90eae473-e143-4ebc-9b68-6f1fa5e39abd">

# Telegram bot (Optional)
<img width="685" alt="Telegram_fU3zVJALFb" src="https://github.com/0xtbug/discord-tools/assets/54710482/80288a55-6456-4215-9cf3-8e2d4d765a19">

set your bot configuration in (https://github.com/0xtbug/discord-tools/blob/main/config.json) `config.json`

```
  "telegram": {
    "token": "your_telegram_bot_token",
    "chat_id": "your_telegram_chat_id"
  },
  "is_telegram_bot": true // make sure to change this
```


`WARN: Using a selfbot is against TOS, It's not my fault if you get a ban when someone reports you`

### # Source
Original source: https://github.com/yudhasaputra/discord-bot
