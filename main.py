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

@bot.slash_command(name = "info", description = "Get info about when the bot was created.")
async def info(ctx):
    embed = discord.Embed(
        title = "DatBot 2.0",
        description="A silly bot with great capabilities.",
        color=discord.Colour.green(),
    )
    file = discord.File('./imgs/avatar.jpg', filename = 'avatar.jpg')
    embed.set_thumbnail(url="attachment://avatar.jpg")
    embed.set_footer(text="Written by HouseJoJo #4651")
    embed.add_field(name = "History:",value = "First created on April 15, 2017", inline=False)
    embed.add_field(name = "",value = "First ran on Jul 15, 2020 using Java", inline=False)
    embed.add_field(name = "",value = "First developed using python on Feb 6th, 2023", inline=False)

    await ctx.respond(file= file, embed=embed)

bot.run(os.getenv('TOKEN'))