from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from companies.forms import CompanyForm


from .models import Companies

def company(request):
    content = Companies.published.filter(is_active=1)
    context = {
        "title": "Управляющие компании",
        "content": content,
    }
    return render(request, 'companies/companies.html', context)

# class AddCompany(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
#     form_class =CompanyForm
#     template_name = 'companies/create_company.html'
#     title_page = 'Добавление компании'
    
#     def form_valid(self, form):
#         w = form.save(commit=False)
#         w.

def create_company(request):
    error = ''
    if request.method=="POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.created_by = request.user
            
            new_app.save()
            return HttpResponseRedirect(reverse('companies:company'))
        else:
            error = 'Форма была не верной'
    
    form = CompanyForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'handbook/create_company.html', data)
