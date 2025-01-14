import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from list_of_request.models import Articles
from rest_framework.parsers import JSONParser

# class ArticlesModel:
#     def __init__(self, fio, phone, text):
#         self.fio = fio
#         self.phone = phone
#         self.text = text
        
        
class ArticlesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Articles
        #fields = ("__all__")
        fields = ('create_time', 'street', 'house', 'flat', 'text', 'phone', 'fio', 'job_date',  'view', 'type',  'status',
                    'nomer', 'povtornaya', 'company', 'master', 'worker', 'dezh_worker', 'comment', 'end_date', 'call_record', 'voice_record', 
                    'user', 'record_status', 'new_sms', 'sms_master', 'sms_about_worker', 'sms_worker', 'sms_complete', 'sms_dezh_worker', 
                    'materials', 'files')
    
    
# def encode():
#     model = Articles('Иванов', 'text: Иванов', 'phone: 89874353230')
#     model_sr = ArticlesSerializers(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
    
# def decode():
#     stream = io.BytesIO(b'{"fio":"\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2","phone":"text: \xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2","text":"phone: 89874353230"}')        
#     data = JSONParser().parse(stream)
#     serializers = ArticlesSerializers(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
