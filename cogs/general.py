import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Provides information of bot, history, and creator")
    async def info(self, ctx):
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

    @discord.slash_command(description = "Find bot latency. Might play ping pong with you if you're lucky.")
    async def ping(self, ctx):
        latency = round(self.bot.latency, 3)
        await ctx.respond(f"Pong. Latency is {latency} seconds.")

def setup(bot):
    bot.add_cog(General(bot))
    