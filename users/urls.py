from django.urls import path
from .views import LoginFormView, RegistrationFormView, \
    LogoutFormView, UserProfileTemplateView, UserProfileFormView, UserVerifyView, \
    UserPasswordRecoveryFormView, UserSetPasswordFormView, MenuSectionsAdd, my_profile, \
    change_username

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegistrationFormView.as_view(), name='register'),
    path('profile/', UserProfileFormView.as_view(), name='myprofile'),
    
    path('change-username/', change_username, name='change-username'),
    path('my_profile/', my_profile, name='my_profile'),
    path('user_menu/', MenuSectionsAdd.as_view()),
    path('<int:id>/', UserProfileTemplateView.as_view(), name='profile'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('verify/<str:username>/<str:activation_key>/',
        UserVerifyView.as_view(), name='verify'),
    path('password-recovery/', UserPasswordRecoveryFormView.as_view(),
        name='password-recovery'),
    path('password-recovery-link/<str:email>/<str:password_recovery_key>/',
        UserSetPasswordFormView.as_view(), name='password-recovery-link'),
]
