import discord
from dotenv import load_dotenv
import os

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")

@bot.slash_command(name = "hello", description = "Test command, lets say hello.")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN'))