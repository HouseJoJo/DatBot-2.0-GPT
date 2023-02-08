import discord
from discord.ext import commands
import os
import openai
import asyncio

openai.api_key = os.getenv("OPENAI_KEY")

class GPT(commands.Cog):

    def __ini__(self, bot):
        self.bot = bot
    
    @discord.slash_command(description = "Ask the bot any prompt to be processed by GPT3.0")
    async def askgpt(self, ctx, *, message):
        await ctx.defer()
        asyncio.sleep(1)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            temperature = 0.3,
            max_tokens = 150,
            top_p=1
        )
        print("OUTPUT="+response['choices'][0]['text'])
        await ctx.respond(response['choices'][0]['text'])

def setup(bot):
    bot.add_cog(GPT(bot))

