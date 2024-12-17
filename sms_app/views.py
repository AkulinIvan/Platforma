from wsgiref import headers
import requests
import json
from .models import SmsTable


def send_sms_via_tele2():
    messages = SmsTable.find().where(status=None).and_where(client_type=['master', 'worker', 'dezh_worker']).all()
    # messages = SmsTable.objects.filter(result__isnull=True)  # Получаем неотправленные сообщения
    for message in messages:
        if message.sms_code is not None:
            addr = f"http://newbsms.tele2.ru/api/send?operation=status&login=http_X1ChNPg3&password=SeuQ457c&id={message.sms_code}"
            response = requests.get(addr)
            out = response.text
            
            message.status = out
            message.save(False)
            if out == 'delivered':
                application_sms_status = 'Доставлено'
            elif out == 'billed':
                application_sms_status = 'Передано на сервер'
            elif out == 'sending':
                application_sms_status = 'Отправлено адресату'
            else:
                application_sms_status = 'Ошибка отправки'
    
        
        response = requests.post("https://example.api.tele2.com/send-sms", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result_data = response.json()
            result = SmsResult(message=message, status_code=response.status_code, response_text=result_data)
            result.save()
        else:
            print(f"Error sending SMS: {response.content}")
            
            
            # import requests

# from list_of_request.models import Articles
# from sms_app.models import SmsTable

# def action_check_sms():
#     models = SmsTable.find().where(status=None).and_where(client_type=['master', 'worker', 'dezh_worker']).all()
#     for model in models:
#         if model.sms_code is not None:
#             addr = f"http://newbsms.tele2.ru/api/send?operation=status&login=http_X1ChNPg3&password=SeuQ457c&id={model.sms_code}"
#             response = requests.get(addr)
#             out = response.text
            
#             model.status = out
#             model.save(False)
#             if out == 'delivered':
#                 application_sms_status = 'Доставлено'
#             elif out == 'billed':
#                 application_sms_status = 'Передано на сервер'
#             elif out == 'sending':
#                 application_sms_status = 'Отправлено адресату'
#             else:
#                 application_sms_status = 'Ошибка отправки'

#             application = Articles.find_one({'nomer': model.application_nomer})
#             if model.client_type == 'master':
#                 application.sms_master = application_sms_status
#             elif model.client_type == 'worker':
#                 application.sms_worker = application_sms_status
#             elif model.client_type == 'dezh_worker':
#                 application.sms_dezh_worker = application_sms_status
#             application.save(False)

#     models = SmsTable.find().where(status=['billed', 'sending']).and_where(client_type=['master', 'worker', 'dezh_worker']).all()
#     for model in models:
#         addr = f"http://newbsms.tele2.ru/api/send?operation=status&login=http_X1ChNPg3&password=SeuQ457c&id={model.sms_code}"
#         response = requests.get(addr)
#         out = response.text
        
#         model.status = out
#         model.save(False)
#         if out == 'delivered':
#             application_sms_status = 'Доставлено'
#         elif out == 'billed':
#             application_sms_status = 'Передано на сервер'
#         elif out == 'sending':
#             application_sms_status = 'Отправлено адресату'
#         else:
#             application_sms_status = 'Ошибка отправки'

#         application = Articles.find_one({'nomer': model.application_nomer})
#         if model.client_type == 'master':
#             application.sms_master = application_sms_status
#         elif model.client_type == 'worker':
#             application.sms_worker = application_sms_status
#         elif model.client_type == 'dezh_worker':
#             application.sms_dezh_worker = application_sms_status
#         application.save(False)

#     models = SmsTable.find(status=['expired', 'undeliverable', 'rejected', 'accepted', 'unknown']).and_where(try=1).all()
#     for model in models:
#         model.try += 1
#         model.status = None
#         model.sms_code = None
#         model.save(False)
