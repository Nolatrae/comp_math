import json
import requests

URL = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
TOKEN = " t1.9euelZrMlIqbnpXJj5yVlciQnM6Lie3rnpWais-QkJ7OlZOcic6Llpaenprl8_cjEQZj-e9QAAUS_t3z92M_A2P571AABRL-.gOBX76B6Hs3jPwMekiARb_XmSTSc58AkCSFjGF4MbiQfvK60DR5qaFC-S3lU2EPdnMnZf3rUahrAvIhw6YF3CQ"
ID_FOLDER = "b1gtf3dqupicap0o7l1v"

with open("zamal-golod.ogg", "rb") as f:
    music = f.read()

headers = {'Authorization': f'Bearer {TOKEN}'}

params = {
    'lang': 'ru-RU',
    'folderId': ID_FOLDER,
    'sampleRateHertz': 48000,
}

req = requests.post(URL, params=params, headers=headers, data=music)
dec_req = req.content.decode('UTF-8')
text = json.loads(dec_req)

print(text)
