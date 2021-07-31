import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        print(f'{member} has joined the server!')
        if channel is not None:
            await channel.send('Welcome {0.mention}!' .format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        print(f'{member} has left the server!')
        if channel is not None:
            await channel.send('Goodbye {0.mention}!' .format(member))

def setup(client):
    client.add_cog(Greetings(client))