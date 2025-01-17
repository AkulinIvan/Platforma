from django.urls import path
from userprofile import views


app_name = 'userprofile'

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path("update_roles/", views.update_roles, name="update_roles"),
    # path("editorial_staff_view/", views.editorial_staff_view, name="editorial_staff"),
]