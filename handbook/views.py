from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from companies.models import Companies

from .forms import AddMasterForm, AddWorkerForm, HouseForm, StreetForm

from .models import City, House, Master, Status_application, Street, Type_application, Usernames, View_application, Worker




def handbook(request):
    context = {
        "title": "Справочник",
    }
    return render(request, 'handbook/handbook.html', context)





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
    content = Worker.objects.all()
    context = {
        "title": "Исполнители",
        "content": content,
    }
    return render(request, 'handbook/executor.html', context)

def executor_add(request):
    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        
        if form.is_valid():
            company = Companies.objects.filter(created_by=request.user)[0]
            executor = form.save(commit=False)
            executor.user = request.user
            executor.company = company
            executor.save()
            
            messages.success(request, 'Исполнитель успешно добавлен.')
            
            return HttpResponseRedirect(reverse('handbook:executor'))
    else:
        form = AddWorkerForm()
            
    return render(request, 'handbook/worker_add.html', {
        'form': form})

def master(request):
    content = Master.objects.all()
    context = {
        "title": "Мастера",
        "content": content,
        
        
    }
    return render(request, 'handbook/master.html', context)

def master_add(request):
    if request.method == 'POST':
        form = AddMasterForm(request.POST)
        
        if form.is_valid():
            company = Companies.objects.filter(created_by=request.user)[0]
            workers = Worker.objects.filter(user=request.user)[0]
            master = form.save(commit=False)
            master.user = request.user
            master.company = company
            master.workers = workers
            master.save()
            
            messages.success(request, 'Мастер успешно добавлен.')
            
            return HttpResponseRedirect(reverse('handbook:add_master'))
    else:
        form = AddWorkerForm()
            
    return render(request, 'handbook/master_add.html', {
        'form': form})
    
            



def username(request):
    content = Usernames.objects.all()
    context = {
        "title": "Пользователи",
        "content": content,
    }
    return render(request, 'handbook/username.html', context)


