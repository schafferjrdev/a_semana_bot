import telebot
from datetime import datetime

API_KEY = "5517245515:AAE8wpqQO5NErueC_L5jYmK3v6aHHcQJWzY"

bot = telebot.TeleBot(API_KEY)

def semana_encerrada():
    now = datetime.now()

    num = datetime.today().weekday()

    sem = ("uma Segunda-feira", "uma Terça-feira", "uma Quarta-feira", "uma Quinta-feira", "uma Sexta-feira", "um Sábado-feira", "um Domingo-feira")

    def getPeriod(h):
        if h <= 3: 
            return 'madrugada'
        if h < 12:
            return 'manhã'
        if h < 18:
            return 'tarde'
        return 'noite'

    current_time = now.strftime(f"São %I horas da {getPeriod(int(now.strftime('%H')))} de {sem[num]}, não é? Semana praticamente encerrada!").replace('0','')

    return current_time


@bot.message_handler(commands=["encerrada"])
def responder(msg):
    bot.reply_to(msg, semana_encerrada())

bot.polling()
