import requests

def send_sms():
    response = requests.get("https://target.t2.ru/api/v2/send_message?operation=send&login=a328d5627d&password=58ac02e411&msisdn=79874353230&shortcode=ADPlatforma&text=test"
    )
    print (response.text)
