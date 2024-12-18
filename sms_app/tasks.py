

# from sms_app.views import send_sms_via_tele2


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
#                 application_sms_status = 'Р”РѕСЃС‚Р°РІР»РµРЅРѕ'
#             elif out == 'billed':
#                 application_sms_status = 'РџРµСЂРµРґР°РЅРѕ РЅР° СЃРµСЂРІРµСЂ'
#             elif out == 'sending':
#                 application_sms_status = 'РћС‚РїСЂР°РІР»РµРЅРѕ Р°РґСЂРµСЃР°С‚Сѓ'
#             else:
#                 application_sms_status = 'РћС€РёР±РєР° РѕС‚РїСЂР°РІРєРё'

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
#             application_sms_status = 'Р”РѕСЃС‚Р°РІР»РµРЅРѕ'
#         elif out == 'billed':
#             application_sms_status = 'РџРµСЂРµРґР°РЅРѕ РЅР° СЃРµСЂРІРµСЂ'
#         elif out == 'sending':
#             application_sms_status = 'РћС‚РїСЂР°РІР»РµРЅРѕ Р°РґСЂРµСЃР°С‚Сѓ'
#         else:
#             application_sms_status = 'РћС€РёР±РєР° РѕС‚РїСЂР°РІРєРё'

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
#     # РћС‚РїСЂР°РІРєР° SMS РёСЃРїРѕР»РЅРёС‚РµР»СЋ
#     client = Client('AC8b5e8bd3263a2d5566f2fd67e34fe5b4', '7e866c03e65eab8f058cfc8e0a185e9c')
#     executor_phone = articles.phone_worker
#     message = f"РќРѕРІР°СЏ Р·Р°СЏРІРєР°: РђРґСЂРµСЃ: {articles.street, articles.house, articles.flat}, РўРµР»РµС„РѕРЅ: {articles.phone}, РўРµРєСЃС‚: {articles.text}"
#     client.messages.create(body=message, from_='+12164388146', to=executor_phone)

#     # Р�РЅС„РѕСЂРјРёСЂРѕРІР°С‚СЊ Р¶РёС‚РµР»СЏ Рѕ РЅР°Р·РЅР°С‡РµРЅРёРё РёСЃРїРѕР»РЅРёС‚РµР»СЏ
#     resident_message = f"Р’Р°С€Сѓ Р·Р°СЏРІРєСѓ РЅР°Р·РЅР°С‡РёР»Рё РёСЃРїРѕР»РЅРёС‚РµР»СЋ: {articles.executor.name}"
#     client.messages.create(body=resident_message, from_='+12164388146', to=articles.phone)
    
    
# # def send_sms():
    
# #         # Р СџР С•Р В»РЎС“РЎвЂЎР В°Р ВµР С� Р С—Р С•РЎРѓР В»Р ВµР Т‘Р Р…Р ВµР Вµ РЎРѓР С•Р С•Р В±РЎвЂ°Р ВµР Р…Р С‘Р Вµ
# #         message = SMS_Message.objects.last()
        
# #         if not message:
# #             return JsonResponse({'status': 'error', 'message': 'No messages found.'})

# #         # Р СњР В°РЎРѓРЎвЂљРЎР‚Р С•Р в„–Р С”Р С‘ API
# #         api_url = "https://smsc.ru/sys/send.php?login=ADPlatforma&psw=J4h-ziU-eN4-fp3&phones=89535855757&mes=РЎвЂљР ВµР С”РЎРѓРЎвЂљ2"  # Р СџРЎР‚Р С‘Р С�Р ВµРЎР‚ URL, РЎС“РЎвЂљР С•РЎвЂЎР Р…Р С‘РЎвЂљР Вµ Р С—Р С• Р Т‘Р С•Р С”РЎС“Р С�Р ВµР Р…РЎвЂљР В°РЎвЂ Р С‘Р С‘
        
# #         # api_url = "http://newbsms.tele2.ru/api/send?operation=status&login=e3ae02e7bd&password=d590356ddd&id=&phones=89874353230&mes=РЎвЂљР ВµРЎРѓРЎвЂљ"
        
# #         # Р С›РЎвЂљР С—РЎР‚Р В°Р Р†Р В»РЎРЏР ВµР С� Р РЋР СљР РЋ
# #         response = requests.get(f"{api_url}")
# #         return response
# # send_sms()
'''