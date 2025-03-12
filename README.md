```markdown
# Anime-Generator-Bot

**A Telegram Bot to Generate Random Anime Images**

This project is maintained by [@Prime_Hritu](https://t.me/Prime_Hritu).  
Join our [Developer Channel](https://t.me/Private_Bots) for updates, support, and discussions.

## Config Vars

Set the following environment variables for your bot:

```
TOKEN    = Your Bot Token from @BotFather
API_ID   = Your Telegram API ID from https://my.telegram.org/apps
API_HASH = Your Telegram API Hash from https://my.telegram.org/apps
OWNER    = Your Telegram user id from @userinfobot
PORT     = Port number for the bot (default: 8080)
NSFW     = Set "True" to enable NSFW content, "False" otherwise (default: False)
```

## Deployment Methods

### Ubuntu Deployment

Follow these steps to deploy on an Ubuntu system:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Prime-Hritu/Anime-Generator-Bot
cd Anime-Generator-Bot
pip3 install -r requirements.txt
```

Now, fill in the required configurations in `bot.py`.

To run the bot, execute:

```bash
python3 bot.py
```

### Heroku Deployment

Deploy on Heroku using the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Prime-Hritu/Anime-Generator-Bot)

---

**Developer:** [@Prime_Hritu](https://t.me/Prime_Hritu)  
**Developer Channel:** [Private Bots](https://t.me/Private_Bots)
```