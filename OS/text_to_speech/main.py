import os
import subprocess
import time


import requests

root_path = os.path.dirname(__file__)
target_path = "./audio"


def synthesize(text):
    token = "t1.9euelZrMlIqbnpXJj5yVlciQnM6Lie3rnpWais-QkJ7OlZOcic6Llpaenprl8_cjEQZj-e9QAAUS_t3z92M_A2P571AABRL-.gOBX76B6Hs3jPwMekiARb_XmSTSc58AkCSFjGF4MbiQfvK60DR5qaFC-S3lU2EPdnMnZf3rUahrAvIhw6YF3CQ"
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {'Authorization': 'Bearer ' + token, }

    data = {
        'folderId': 'b1gtf3dqupicap0o7l1v',
        'text': text,
        'lang': 'ru-RU',
        'voice': 'jane',  # oksana
        'emotion': 'good',
        'speed': '1.0',
        'format': 'lpcm',
        'sampleRateHertz': 48000,
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (
                resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


def write_file(text):

    filename = str(int(time.time()))
    with open(target_path + filename + ".raw", "wb") as f:
        for audio_content in synthesize(text):
            f.write(audio_content)

    time.sleep(2)

    return filename


def convert(filename):
    cmd = " ".join([
        root_path + "\sox\sox.exe",
        "-r 48000 -b 16 -e signed-integer -c 1",
        target_path + filename + ".raw",
        target_path + filename + ".wav",
    ])

    subprocess.Popen(cmd, stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT, universal_newlines=True)


def read_text():
    with open("text.txt", "r", encoding="UTF-8") as f:
        text = f.read()

    return text


convert(write_file(read_text()))
