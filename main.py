import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print("We have logged in a s {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Welcome, young padawan.")

client.run("TOKEN")
