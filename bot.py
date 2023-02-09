import discord
import responses


async def send_message(message, user_message, is_public):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_public else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA3MzMyMTIyMjQyODk2Njk1Mg.GLIJqF.2CqFiFzWQNZh4S_LAXGZln63j3cvg_CeK5LpzI'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '/':
            user_message = user_message[1:]
            await send_message(message, user_message, is_public=True)

    client.run(TOKEN)