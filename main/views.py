from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'title': 'АДС - Главная',
        'content': 'Кто снег набросал тот его и убирает!'
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context={
        'title': 'АДС - О нас',
        'content': 'Информация о нас',
        'text_on_page': 'Текст о том, почему наша аварийно-диспетчерская служба классная и как мы молниеносно приходим на помощь Вашим абонентам'
        
    }
    return render(request, 'main/about.html', context)

