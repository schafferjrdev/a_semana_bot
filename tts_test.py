import pyttsx3
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which
import pytz
import tzlocal

AudioSegment.converter = which("ffmpeg")


def semana_encerrada():
    now = datetime.now()

    num = datetime.today().weekday()

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
        return f"{now.strftime('%I')} horas".lstrip("0")

    current_time = now.strftime(
        f"{getHour(now.strftime('%H'))}{getPeriod(int(now.strftime('%H')))} de {sem[num]}")

    return current_time


def get_audio():
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    if (voices[1].name == 'Microsoft Maria Desktop - Portuguese(Brazil)'):
        tts.setProperty('voice', voices[1].id)
    else:
        tts.setProperty('voice', 'brazil')

    tts.save_to_file(semana_encerrada(), './assets/horas.mp3')
    tts.runAndWait()

# get_audio()


sao = AudioSegment.from_file("./assets/sao.mp3")
horas = AudioSegment.from_file("./assets/horas.mp3")
encerrada = AudioSegment.from_file("./assets/encerrada.mp3")
silence = AudioSegment.silent(duration=300)

semana = sao + horas + encerrada

# semana.export("./assets/semana.mp3", format="mp3")


# from io import BytesIO
# seg=AudioSegment.from_file("./assets/horas.mp3")

# mp3IO=BytesIO()
# seg.export(mp3IO, format="mp3")
# mp3IO.getvalue()


print('locale', tzlocal.get_localzone())
print('Request date from: ', datetime.utcfromtimestamp(1660326375))
