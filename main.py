import discord
import random
import os
from discord.ext import commands

TOKEN = 'ODY5ODE2MjIxNDkzNzU1OTM1.YQDtew.Fp9euV4UNDGJbbRRFRRl-EEV9xI'

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '?', intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity = discord.Game('May is gay!'))
    print('Bot is online!')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)