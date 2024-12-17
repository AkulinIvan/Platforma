from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CompanyForm, HouseForm, StreetForm

from .models import Company, City, House, Status_application, Street, Type_application, Usernames, View_application




def handbook(request):
    context = {
        "title": "Справочник",
    }
    return render(request, 'handbook/handbook.html', context)

def company(request):
    content = Company.objects.all()
    context = {
        "title": "Управляющие компании",
        "content": content,
    }
    return render(request, 'handbook/company.html', context)

def create_company(request):
    error = ''
    if request.method=="POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.created_by = request.user
            
            new_app.save()
            return HttpResponseRedirect(reverse('handbook:company'))
        else:
            error = 'Форма была не верной'
    
    form = CompanyForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'handbook/create_company.html', data)



def city(request):
    content = City.objects.all()
    context = {
        "title": "Города",
        "content": content,
    }
    return render(request, 'handbook/city.html', context)




def street(request):
    content = Street.objects.all()
    context = {
        "title": "Улицы",
        "content": content,
    }
    return render(request, 'handbook/street.html', context)

def create_street(request):
    error = ''
    if request.method=="POST":
        form = StreetForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.created_by = request.user
            
            new_app.save()
            return HttpResponseRedirect(reverse('handbook:street'))
        else:
            error = 'Форма была не верной'
    
    form = StreetForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'handbook/create_street.html', data)


def house(request):
    content = House.objects.all()
    context = {
        "title": "Дома",
        "content": content,
    }
    return render(request, 'handbook/house.html', context)

def create_house(request):
    error = ''
    if request.method=="POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.created_by = request.user
            
            new_app.save()
            return HttpResponseRedirect(reverse('handbook:house'))
        else:
            error = 'Форма была не верной'
    
    form = HouseForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'handbook/create_house.html', data)




def type_application(request):
    content = Type_application.objects.all()
    context = {
        "title": "Тип заявки",
        "content": content,
    }
    return render(request, 'handbook/type_application.html', context)




def view_application(request):
    content = View_application.objects.all()
    context = {
        "title": "Вид заявки",
        "content": content,
    }
    return render(request, 'handbook/view_application.html', context)




def status_application(request):
    content = Status_application.objects.all()
    context = {
        "title": "Статус заявки",
        "content": content,
    }
    return render(request, 'handbook/status_application.html', context)




def executor(request):
    content = Usernames.objects.all()
    context = {
        "title": "Исполнители",
        "content": content,
    }
    return render(request, 'handbook/executor.html', context)




def username(request):
    content = Usernames.objects.all()
    context = {
        "title": "Пользователи",
        "content": content,
    }
    return render(request, 'handbook/username.html', context)


