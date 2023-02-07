import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def info(self, ctx):
        await ctx.send("")

def setup(bot):
    bot.add_cog(General(bot))
    