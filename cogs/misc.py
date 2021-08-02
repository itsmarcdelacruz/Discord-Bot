import discord
from discord.ext import commands
import random

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):
            responses = ['It is certain',
                 'Without a doubt',
                 'You may rely on it',
                 'Yes definitely',
                 'It is decidedly so',
                 'As I see it, yes',
                 'Most likely',
                 'Yes',
                 'Outlook good',
                 'Signs point to yes',
                 'Reply hazy try again',
                 'Better not tell you now',
                 'Ask again later',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'Outlook not so good',
                 'My sources say no',
                 'Very doubtful',
                 'My reply is no']
            randomAnswer = random.choice(responses)
            await ctx.send(f'Questions: {question}\nAnswer: {randomAnswer}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {self.client.latency * 1000}ms')

    @commands.command()
    async def createInvite(self, ctx):
        inviteLink = await ctx.channel.create_invite()
        await ctx.send(f"Here is the instant invite link to your server: {inviteLink}")

def setup(client):
    client.add_cog(Misc(client))