import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
import spotipy

# Load environment variables
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BASE_URL = os.getenv("BASE_URL")  # e.g., https://your-subdomain.loca.lt
TOKEN_FILE = "user_tokens.json"

# Discord setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Helper to load a user's Spotify token
def load_user_token(discord_id):
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE) as f:
        data = json.load(f)
    return data.get(str(discord_id), None)

# Helper to create a Spotipy client from stored token
def get_spotify_client(token_info):
    return spotipy.Spotify(auth=token_info["access_token"])

# Command: link Spotify account
@bot.command()
async def linkspotify(ctx):
    auth_url = f"{BASE_URL}/login?discord_id={ctx.author.id}"
    await ctx.send(f"🎵 Click here to link your Spotify account: {auth_url}")

# Command: start the guessing game
@bot.command()
async def startgame(ctx):
    token_info = load_user_token(ctx.author.id)
    if not token_info:
        await ctx.send("😢 You haven't linked your Spotify yet. Use `!linkspotify` first.")
        return

    sp = get_spotify_client(token_info)
    try:
        top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
        if not top_tracks["items"]:
            await ctx.send("😢 Could not fetch top tracks. Please play more on Spotify and try again.")
            return

        # Find first track with preview_url available
        track = None
        for t in top_tracks["items"]:
            if t["preview_url"]:
                track = t
                break
        
        if track:
            name = track["name"]
            artist = track["artists"][0]["name"]
            preview_url = track["preview_url"]
            await ctx.send(f"🎵 Playing preview of **{name}** by **{artist}**... Guess the song!")
            await ctx.send(preview_url)
        else:
            await ctx.send("😢 None of your top tracks have a preview available.")

    except Exception as e:
        print(e)
        await ctx.send("😢 Something went wrong trying to fetch your top tracks.")



#run bot
bot.run(DISCORD_TOKEN)

