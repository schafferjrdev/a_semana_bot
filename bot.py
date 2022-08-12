from decouple import config
from pyrogram import Client, filters
from datetime import datetime

TOKEN_TELEGRAM = config("TOKEN_TELEGRAM")
API_HASH = config("API_HASH")
API_ID = config("API_ID")

app = Client('a_semana_bot', api_hash=API_HASH,
             api_id=API_ID, bot_token=TOKEN_TELEGRAM)


@app.on_message(filters.command('encerrada'))
async def hello(client, message):
    print(message)
    print(client)
    d = datetime.fromisoformat(str(message.date))
    print(message.date)
    print(d.weekday())
    print(d.strftime('%H'))
    await message.reply(f"Sua hora é: {message.date}")


app.run()
