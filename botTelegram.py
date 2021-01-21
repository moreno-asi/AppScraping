import requests

#Funcion para enviar mensaje al Bot creado
def telegram_bot_sendtext(bot_message):
    
    bot_token = 'XXXXXXXXXXXXXXXXXXXXXXX'#Token del Bot creado
    bot_chatID = 'XXXXXXXXXX'#ID del chat creado
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

