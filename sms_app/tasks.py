from sms_app.views import send_sms_via_tele2


# @app.task
# def schedule_send_sms():
#     send_sms_via_tele2()





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

'''
# from twilio.rest import Client
# from list_of_request.models import Articles

# def inform_executor(articles=Articles):
#     # Отправка SMS исполнителю
#     client = Client('AC8b5e8bd3263a2d5566f2fd67e34fe5b4', '7e866c03e65eab8f058cfc8e0a185e9c')
#     executor_phone = articles.phone_worker
#     message = f"Новая заявка: Адрес: {articles.street, articles.house, articles.flat}, Телефон: {articles.phone}, Текст: {articles.text}"
#     client.messages.create(body=message, from_='+12164388146', to=executor_phone)

#     # Информировать жителя о назначении исполнителя
#     resident_message = f"Вашу заявку назначили исполнителю: {articles.executor.name}"
#     client.messages.create(body=resident_message, from_='+12164388146', to=articles.phone)
    
    
# # def send_sms():
    
# #         # РџРѕР»СѓС‡Р°РµРј РїРѕСЃР»РµРґРЅРµРµ СЃРѕРѕР±С‰РµРЅРёРµ
# #         message = SMS_Message.objects.last()
        
# #         if not message:
# #             return JsonResponse({'status': 'error', 'message': 'No messages found.'})

# #         # РќР°СЃС‚СЂРѕР№РєРё API
# #         api_url = "https://smsc.ru/sys/send.php?login=ADPlatforma&psw=J4h-ziU-eN4-fp3&phones=89535855757&mes=С‚РµРєСЃС‚2"  # РџСЂРёРјРµСЂ URL, СѓС‚РѕС‡РЅРёС‚Рµ РїРѕ РґРѕРєСѓРјРµРЅС‚Р°С†РёРё
        
# #         # api_url = "http://newbsms.tele2.ru/api/send?operation=status&login=e3ae02e7bd&password=d590356ddd&id=&phones=89874353230&mes=С‚РµСЃС‚"
        
# #         # РћС‚РїСЂР°РІР»СЏРµРј РЎРњРЎ
# #         response = requests.get(f"{api_url}")
# #         return response
# # send_sms()
'''