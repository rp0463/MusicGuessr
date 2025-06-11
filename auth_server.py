# auth_server.py

from flask import Flask, redirect, request
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

load_dotenv()
app = Flask(__name__)

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-top-read"
)

# Memory + disk cache for tokens
TOKEN_FILE = "user_tokens.json"
if not os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, 'w') as f:
        json.dump({}, f)

def save_token(discord_id, token_info):
    with open(TOKEN_FILE, 'r+') as f:
        data = json.load(f)
        data[str(discord_id)] = token_info
        f.seek(0)
        json.dump(data, f, indent=2)

@app.route("/login")
def login():
    discord_id = request.args.get("discord_id")
    auth_url = sp_oauth.get_authorize_url(state=discord_id)
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")  # this is the Discord user ID
    token_info = sp_oauth.get_access_token(code, as_dict=True)
    save_token(state, token_info)
    return f"✅ Spotify linked! You can return to Discord and start the game."

if __name__ == "__main__":
    app.run(port=8888)

