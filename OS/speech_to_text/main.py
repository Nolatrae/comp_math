import os
import subprocess
import time
# from creds import token, folder_id

import requests

root_path = os.path.dirname(__file__)
target_path = "D:\\comp_math\\OS\\speech_to_text\\"

"""

https://cloud.yandex.ru/docs/speechkit/tts/request#wav
https://cloud.yandex.ru/docs/speechkit/tts/request
https://cloud.yandex.ru/docs/speechkit/api-ref/grpc/tts_service
"""


def synthesize(text):
    token = "t1.9euelZrNko2Jnpqaz5WQnZaZnY-Ynu3rnpWais-QkJ7OlZOcic6Llpaenprl8_c6dxpj-e9UWnwc_t3z93olGGP571RafBz-.pqW2PCGpQjSTaDPDwz2q51s3XkpVnPt5h5Nahs6ugDEf21ITLUaN7BaFAoe33eQ0KknSn-FK4zLzJQTUdPxBBA"
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
