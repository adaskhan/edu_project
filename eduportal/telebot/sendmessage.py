import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    setting = TeleSettings.objects.get(pk=1)
    token = str(setting.tg_token)
    chat_id = str(setting.tg_chat)
    text = str(setting.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    a = text.find('{')
    b = text.find('}')
    c = text.rfind('{')
    d = text.rfind('}')

    part_1 = text[:a]
    part_2 = text[b+1:c]
    part_3 = text[d:-1]

    text_slice = part_1 + tg_name + part_2 + part_3 + tg_phone

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slice
    })
