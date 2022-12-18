import json
import requests

URL = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
TOKEN = "t1.9euelZrKysfPk5yRlozJmMmJjsuZk-3rnpWais-QkJ7OlZOcic6Llpaenprl8_cIUyVj-e8pcBk1_N3z90gBI2P57ylwGTX8.wJ0IJmXJKTbutP8aSjhT36vHZWT6csFnNj_LWl3Lxc7wEyc4HoKg7tGF25UxboKVUHLsPhnEamaGdIrwrUrVDw"
ID_FOLDER = "b1gtf3dqupicap0o7l1v"

with open("zamal-golod.ogg", "rb") as f:
    music = f.read()

headers = {'Authorization': f'Bearer {TOKEN}'}

params = {
    'lang': 'ru-RU',
    'folderId': ID_FOLDER,
    'sampleRateHertz': 48000,
}

response = requests.post(URL, params=params, headers=headers, data=music)
decode_resp = response.content.decode('UTF-8')
text = json.loads(decode_resp)

print(text)
