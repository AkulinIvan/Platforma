from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
from .models import Userprofile

from .forms import LoginUserForm



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            return redirect('userprofile:login')
    else:
        form = UserCreationForm(request.POST)
        
    return render(request, 'userprofile/signup.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('list_of_request:applications'))
    else:
        form = LoginUserForm()
    return render(request, 'userprofile/login.html', {'form': form})
            

        
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('userprofile:login'))
            

# @login_required
# def editorial_staff_view(request):
#     if request.userprofile.is_admin:
#         users = Userprofile.objects.all().order_by('last_name')
#         all_groups = Group.objects.all()

#         special_permissions = SpecialPermissions.objects.all().select_related('admin')
#         admins = special_permissions.values_list('admin_id', flat=True)

#         template_name = 'userprofile/staff.html'

#         return render(request, template_name, {'users': users,
#                                             'special_permissions': special_permissions,
#                                             'admins': admins,
#                                             'all_groups': all_groups})
#     else:
#         return redirect(request.META['HTTP_REFERER'])

# @login_required
# def update_roles(request):
#     if not request.userprofile.is_admin or not request.method == 'POST':
#         return JsonResponse({'error': 'Invalid request'}, status=400)

#     user_id = request.POST.get('userId')
#     is_dispatcher = request.POST.get('isEmployee') == 'true'
#     is_admin = request.POST.get('isAdmin') == 'true'
#     user = Userprofile.objects.get(id=user_id)
#     message = f'Уважаемый {user.first_name}! \n'
#     was_admin = user.is_admin

#     if is_dispatcher and is_admin:
#         user.is_dispatcher = True
#         user.is_admin = True
#         message += "Вам дано право Администратора портала."
#         subject = "Дано право Администратора портала"
#     elif is_dispatcher:
#         user.is_dispatcher = True
#         user.is_admin = False
#         if was_admin:
#             message += "Вы лишены права Администратора портала."
#             subject = "Лишение права Администратора портала"
#         else:
#             message += "Вам дано право Сотрудника редакции."
#             subject = "Дано право Сотрудника редакции"
#     else:
#         user.is_dispatcher = False
#         user.is_admin = False
#         message += "Вы лишены права Сотрудника редакции"
#         subject = "Лишение права Сотрудника редакции."

#     message += '\n\nРедакция портала "Дерево знаний" '
#     user.save()

#     # send_email(user.email, subject, False, message)

#     return JsonResponse({'message': 'Roles updated successfully'})            
        
        