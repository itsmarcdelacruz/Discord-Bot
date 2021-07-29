import discord

TOKEN = 'ODY5ODE2MjIxNDkzNzU1OTM1.YQDtew.Fp9euV4UNDGJbbRRFRRl-EEV9xI'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(TOKEN)