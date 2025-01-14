import django_filters
from django_filters import DateFilter
from .models import *



class ArticlesFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="create_time", lookup_expr='gte')
    end_date = DateFilter(field_name="create_time", lookup_expr='lte')
    class Meta:
        model = Articles
        fields = ('create_time', 'street', 'house', 'flat', 'text', 'phone', 'fio', 'view', 'type', 'status',
                    'povtornaya', 'company', 'master', 'worker', 'dezh_worker', 'user')
        exclude = ['user', 'create_time']


    
    

