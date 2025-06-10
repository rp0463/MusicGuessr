""" Sample code for main.py """

# Importing discord.py to interact with Discord's API
import discord

# Importing os module for environment variable access
import os

# Importing load_dotenv to load .env file
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the token from the .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Enable message content intent so the bot can read messages
intents = discord.Intents.default()
intents.message_content = True

# Create the bot client with specified intents
bot = discord.Client(intents=intents)

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    print(f"MomentoMori is in {guild_count} guilds.")

# Event listener for incoming messages
@bot.event
async def on_message(message):
    # Prevent bot from responding to its own messages
    if message.author == bot.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("hey GFG user")
    elif message.content.lower() == "you":
        await message.channel.send("i am also good")

# Run the bot
bot.run(DISCORD_TOKEN)
