from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import template
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig, SingleTableView
from sqlalchemy import table
from companies.forms import CompanyForm
from django.views.generic.detail import DetailView
import django_tables2 as tables

from .models import Companies, CompanyTable
register = template.Library()



class CompanyDetail(DetailView):
    model = Companies
    template_name = 'companies/show_company.html'
    pk_url_kwarg = 'company_id'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Companies.objects.filter(created_by=self.request.user)
        else:
            return Companies.objects.none() 
# @login_required    
# def company(request):
#     content = Companies.published.filter(created_by=request.user)
#     context = {
#         "title": "Управляющие компании",
#         "content": content,
#     }
#     return render(request, 'companies/companies.html', context)
# class SomeTable(tables.Table):

#     class Meta:
#         model= Companies
#         attrs = {"class": "paleblue"}
        
# class SomeTableView(SingleTableView):  # <-- check for SingleTableView
#     model = Companies
#     template_name = 'companies/companies.html'
#     table_class = SomeTable
    
@login_required
def company(request):
    table = CompanyTable(Companies.published.filter(created_by=request.user))
    RequestConfig(request).configure(table)
    return render(request, 'companies/companies.html', {'table': table})
    

# class AddCompany(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
#     form_class =CompanyForm
#     template_name = 'companies/create_company.html'
#     title_page = 'Добавление компании'
    
#     def form_valid(self, form):
#         w = form.save(commit=False)
#         w.
@login_required 
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
    
    return render(request, 'companies/create_company.html', data)
