# Anime-Generator-Bot
**A Heroku Deployable Telegram Bot Which Can Generate Random Images**

# Config Vars :
```
TOKEN = Enter Your Bot Token From @BotFather
API_ID = Your API_ID from https://my.telegram.org/apps
API_HASH = Your API_HASH from https://my.telegram.org/apps
```
# Deploy Method :
## Heroku :

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Prime-Hritu/Anime-Generator-Bot)

## Termux :
```
apt update && apt upgrade
pkg update && pkg upgrade
pkg install python
pkg install git
git clone https://github.com/Prime-Hritu/Anime-Generator-Bot
cd Anime-Generator-Bot
pip install -r requirements.txt
```
**Now Fill The Requirements In** ```bot.py```

**To Run / Start The Bot**

```python bot.py```
