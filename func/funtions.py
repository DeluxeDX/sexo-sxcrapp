import re

def FindCards(text):
    try:
        card_info = re.search(r'(\d{15,16})+?[^0-9]+?(\d{1,2})[\D]*?(\d{2,4})[^0-9]+?(\d{3,4})', text)
        cc, mes, ano, cvv = card_info.groups()
        cc = cc.replace("-", "").replace(" ", "")
        return f'{cc}|{mes}|{ano}|{cvv}'
    except:...