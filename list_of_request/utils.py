from .models import Articles


def get_user_application(request):
    if request.user.is_authenticated:
        return Articles.objects.filter(user=request.user).select_related('fio')
    
    # if not request.session.session_key:
    #     request.session.create()
    # return Articles.objects.filter(session_key=request.session.session_key)




# from .models import Articles


# menu = [{'title': "Заявки", 'url_name': 'applications'},
#         {'title': "Новая заявка", 'url_name': 'create_application'},
#         {'title': "Детали заявки", 'url_name': 'application'},
# ]

# class DataMixin:
#     def get_application_context(self, **kwargs):
#         context = kwargs
#         apps = Articles.objects.all()
#         context['menu'] = menu
#         context['apps'] = apps
#         if 'app_selected' not in context:
#             context['app_selected'] = 0
#         return context