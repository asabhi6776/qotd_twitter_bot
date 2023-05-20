import tweepy
import requests
import json
import discord
import os
from dotenv import load_dotenv
from discord import Webhook
# from discord.ext import commands
import aiohttp
import json
import asyncio

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
consumer_key = os.getenv('YOUR_CONSUMER_KEY')
consumer_secret = os.getenv('YOUR_CONSUMER_SECRET')
access_token = os.getenv('YOUR_ACCESS_TOKEN') 
access_token_secret = os.getenv('YOUR_ACCESS_TOKEN_SECRET')

# Discord webhook URL for sending notifications
discord_webhook_url = os.getenv('YOUR_DISCORD_WEBHOOK_URL')

# Fetch a random quote from an API
def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = json.loads(response.text)
        quote = data["content"]
        author = data["author"]
        return f'"{quote}" - {author}'
    return None

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get a quote
quote = get_quote()

# Post the quote on Twitter
if quote:
    try:
        api.update_status(quote)
        print("Quote posted successfully!")
    except tweepy.TweepError as e:
        print("Failed to tweet:", e)
        # Send a notification on Discord
        async def send_discord_notification():
            async with aiohttp.ClientSession() as session:
                async with session.post(discord_webhook_url, json={"content": f"Failed to tweet: {e}"}) as response:
                    if response.status == 200:
                        print("Discord notification sent successfully!")
                    else:
                        print("Failed to send Discord notification:", response.status)
        asyncio.run(send_discord_notification())
else:
    print("Failed to fetch a quote.")
    # Send a notification on Discord
    async def send_discord_notification():
        async with aiohttp.ClientSession() as session:
            async with session.post(discord_webhook_url, json={"content": "Failed to fetch a quote."}) as response:
                if response.status == 200:
                    print("Discord notification sent successfully!")
                else:
                    print("Failed to send Discord notification:", response.status)
    asyncio.run(send_discord_notification())