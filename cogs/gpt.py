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
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message + " summarize details to provide answer within a paragraph.",
            temperature = 0.3,
            max_tokens = 250,
            top_p=1
        )
        outMessage = f"**Prompt:** {message} {response['choices'][0]['text']}"
        await ctx.respond(outMessage)

    @discord.slash_command(description = "Provide a prompt that will be asked to a 'creative' version of GPT-3")
    async def askcreativegpt(self, ctx, *, message):
        await ctx.defer()
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt="Be creative, " + message,
            temperature = 0.9,
            max_tokens = 400,
            top_p=1
        )
        outMessage = f"**Prompt:** {message} {response['choices'][0]['text']}"
        await ctx.respond(outMessage)

def setup(bot):
    bot.add_cog(GPT(bot))

