import discord
import random
import os
from discord.ext import commands

TOKEN = 'ODY5ODE2MjIxNDkzNzU1OTM1.YQDtew.Fp9euV4UNDGJbbRRFRRl-EEV9xI'

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '?', intents = intents)

@client.event
async def on_ready():
    print('Bot is online!')

#@client.event
#async def on_member_join(member):
    #print(f'{member} has joined a server!')

#@client.event
#async def on_member_remove(member):
    #print(f'{member} has left a server.')

#@client.command()
#async def ping(ctx):
    #await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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
    await ctx.send(f'Questions: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason =None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kicked. \nReason: {reason}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason =None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned. \nReason: {reason}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'User {member} has been unbanned.')
            return

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