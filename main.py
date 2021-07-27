import discord
import random

TOKEN = 'Nzc0MDM4NDEyMjg1MzEzMDk1.X6R9cg.rXDgU5bsxlWsqTjBm_D7l6bRlu8'

client = discord.Client()

@client.event
async def on_ready();
    print('We have logged in as {0.user]'.format(client))

client.run(TOKEN)