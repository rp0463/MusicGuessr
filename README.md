# MusicGussr
guess song discord bot - link with last.fm / spotify / apple music

# Setup

- Get Tokens for Discord / Spotify here:
Discord: https://discord.com/developers/applications
Spotify: https://developer.spotify.com/dashboard

- Install ngrok for dev testing on localhost
ngrok: https://ngrok.com/downloads/linux

- Set up .env as follows:

DISCORD_TOKEN=YOURTOKEN
SPOTIFY_CLIENT_ID=CLIENTID
SPOTIFY_CLIENT_SECRET=CLIENTSECRET
SPOTIFY_REDIRECT_URI=https://4230-99-125-127-215.ngrok-free.app/callback <- example
BASE_URL=https://4230-99-125-127-215.ngrok-free.app <- example

^^ Bottom 2 URLS are coming from ngrok

- Run ngrok on port 8888 with 'ngrok http 8888'
- Set the callback link to the ngrok link on spotify dev page
- Run auth_server.py
- Run bot.py


# Notes
I am using ngrok to test since spotify needs an "https" to sync account to spotify app
