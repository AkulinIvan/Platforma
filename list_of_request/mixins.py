from django.template.loader import render_to_string
from django.urls import reverse
from .models import Articles
from .utils import get_user_application

class ApplicationMixin():
    def get_application(self, request, product=None, cart_id=None):
        if request.user.is_authenticated:
            query_kwargs={"user": request.user}
        else:
            query_kwargs={"session_key": request.session.session_key}    
        # if product:
        #     query_kwargs[""] = product

        # if application_id:
        #     query_kwargs["id"] = application_id
            
        return Articles.objects.filter(**query_kwargs).first()
    
    # def render_application(self, request):
    #     user_application = get_user_application(request)
    #     context = {"application": user_application}
        
    #     referer = request.META.get("HTTP_REFERER")
    #     if reverse('list_of_request:create_application') in referer:
    #         context["order"] = True
            
    #     return render_to_string(
    #         "carts/includes/included_cart.html", context, request=request
    #     )