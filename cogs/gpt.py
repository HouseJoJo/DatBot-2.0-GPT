import discord
from discord.ext import commands
from discord.commands import Option
import os
import openai
import random

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

    @discord.slash_command(description = "Have GPT-3 explain a topic/random topic to you 'in simple terms'")
    async def gptexplain(self, ctx, topic: Option(str, "Enter a topic", required = False, default = '')):
        if (topic == ''):
            topics = ['Numerical Analysis', 'Calculus', 'Linear Algebra', 'Physics 1', 'Physics 2', 'Python', 'Internet of Things',
                      'Data Science', 'Artificial Intelligence', 'Astrology', 'Neuroscience', 'Meteorology']
            topic = random.choice(topics)
            message = f"Explain one fun fact about a college level {topic} course content like I'm five."
        else:
            message = f"Explain {topic} to me like I'm five, simplify any unnecessary details."
        await ctx.defer()
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt=message,
            temperature = 0.5,
            max_tokens = 325,
            top_p=1
        )
        outMessage = f"**Topic:** {topic} {response['choices'][0]['text']}"
        await ctx.respond(outMessage)

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member): #REQUIRES INTENT: MEMBERS
        await ctx.defer()
        message = f"Write a witty or clever welcome message for Discord user {member.name}"
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = message,
            temperature = 0.9,
            max_tokens = 300,
            top_p=1
        )
        await member.send(response['choices'][0]['text'])

def setup(bot):
    bot.add_cog(GPT(bot))

