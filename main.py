import discord

token = "MTI4MDE0Nzc2MDkzNDI4OTQ3OQ.GdXOFe.jcOVYvz61SnQ74WIhhBhqX7g9yCjB_IPVThXd8"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "LOL" in message.content:
        await message.channel.send("Ne smijes reći LOL")
        await message.author.kick(reason="Rekao je LOL")  # Ispravljen kick

    if message.content == "ping":
        await message.channel.send("pong")

    if message.content.startswith("!poll"):
        question = message.content[len("!poll"):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction("👍")
            await poll_message.add_reaction("👎")
    else:
        await message.channel. send ("Nisi napisao pitanje")


client.run(token)

# Ova linija će se ispisati čim se program pokrene
print("test")


