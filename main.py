from time import time
import telebot
from decouple import config
from datetime import datetime
from pydub import AudioSegment
import pyttsx3
from io import BytesIO
from pydub.utils import which
import pytz

AudioSegment.converter = which("ffmpeg")

API_KEY = config("TOKEN_TELEGRAM")

bot = telebot.TeleBot(API_KEY)


def semana_encerrada(date):
    print('Server date: ', datetime.fromtimestamp(date))

    msg_date = datetime.fromtimestamp(date, pytz.timezone('America/Sao_Paulo'))
    print('Message date: ', msg_date)

    num = msg_date.weekday()

    sem = ("uma Segunda-feira", "uma Terça-feira", "uma Quarta-feira",
           "uma Quinta-feira", "uma Sexta-feira", "um Sábado", "um Domingo")

    def getPeriod(h):
        if h == 0:
            return ''
        if h <= 3:
            return ' da madrugada'
        if h < 12:
            return ' da manhã'
        if h < 19:
            return ' da tarde'
        return ' da noite'

    def getHour(h):
        if h == '00':
            return 'meia-noite'
        if h == '01' or h == '13':
            return 'Uma hora'
        return f"{msg_date.strftime('%I')} horas".lstrip("0")

    current_time = msg_date.strftime(
        f"{getHour(msg_date.strftime('%H'))}{getPeriod(int(msg_date.strftime('%H')))} de {sem[num]}")

    return current_time


def get_audio(date):
    tts = pyttsx3.init('espeak')

    # if (voices[1].name == 'Microsoft Maria Desktop - Portuguese(Brazil)'):
    #     tts.setProperty('voice', voices[1].id)
    # else:
    # tts.setProperty('voice', 'brazil')

    # tts.save_to_file(semana_encerrada(date), './assets/horas.mp3')
    print(date)
    tts.say('hello')
    tts.runAndWait()

    # sao = AudioSegment.from_file("./assets/sao.mp3")
    # horas = AudioSegment.from_file("./assets/horas.mp3")
    # encerrada = AudioSegment.from_file("./assets/encerrada.mp3")

    # semana = sao + horas + encerrada
    # mp3IO = BytesIO()
    # semana.export(mp3IO, format="mp3")
    # return mp3IO.getvalue()


@bot.message_handler(commands=["encerrada"])
def responder(msg):
    # To send an Audio File
    bot.send_audio(msg.chat.id, get_audio(msg.date),
                   performer='@a_semana_bot', title='São que horas?')

    # To send a Message File
    # bot.reply_to(
    #     msg, f"São {semana_encerrada(msg.date)}, Ahh... Semana praticamente encerrada!")


bot.polling()
