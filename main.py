import discord
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

load_dotenv()
bot = discord.Bot()
cogs_list = [
    'general',
    'gpt'
]
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")

@bot.slash_command(name = "hello", description = "Test command, lets say hello.")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN'))