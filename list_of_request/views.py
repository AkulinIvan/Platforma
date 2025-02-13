from django.views import View
from django.core.paginator import Paginator
from django_tables2 import LazyPaginator, RequestConfig, SingleTableView

from companies.models import Companies
from .mixins import ApplicationMixin
from handbook.models import House
from .filters import ArticlesFilter
from django_filters.views import FilterView
from rest_framework import generics
from django.db.models import F

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin

from .permissions import  IsOwnerOrReadOnly

from list_of_request.serializers import ArticlesSerializer

from .models import ApplicationTable, Articles
from .forms import ArticlesForm
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q

import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

# class ArticlesViewSet(viewsets.ModelViewSet):
#     #queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer  

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
        
#         if not pk:
#             return Articles.objects.all()[:3]
        
#         return Articles.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def company(self, request, pk=None):
#         company = Company.objects.get(pk=pk)
#         return Response({'company': company.name})


# class ArticlesAPIList(generics.ListCreateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer
#     permission_classes = (IsAuthenticated,  )
    
    

# class ArticlesAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer
#     permission_classes = (IsAuthenticated,  )
    
# class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer
#     permission_classes = (IsOwnerOrReadOnly,  )




# class ApplicationList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'list_of_request/list_of_applications.html'

#     def get(self, request):
#         content = Articles.objects.all().order_by('-id')
#         return Response({'applications': content})

@login_required
def new_applications_list(request):
    page = request.GET.get('page', 1)
    applications = Articles.objects.filter(user=request.user).filter(Q(status='NEW')).order_by('-id')
    paginator = Paginator(applications, 4)
    current_page = paginator.page(int(page))
    context = {
        "title": "Список новых заявок",
        "content": current_page,
        
    }
    return render(request, 'list_of_request/new_applications.html', context)


@login_required  
def list_applications(request):
    
    table = ApplicationTable(Articles.objects.filter(user=request.user).order_by('-id'))
    # RequestConfig(request, paginate={"per_page": 25}).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    # paginator = Paginator(table, 4)
    # current_page = paginator.page(int(page))
    context = {
        "title": "Список заявок",
        "table": table,
    }
    return render(request, 'list_of_request/list_of_applications.html', context)

def table_view(request):
    table = ApplicationTable(Articles.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response(f"table.{export_format}")

    return render(request, 'list_of_request/list_of_applications.html', {
        "table": table
    })

class TableView(ExportMixin, tables.SingleTableView):
    table_class = ApplicationTable
    model = Articles
    export_formats = ['csv',]
    template_name = "list_of_request/list_of_applications.html"

@login_required
def complete_applications(request):
    page = request.GET.get('page', 1)
    complete_applications = Articles.objects.filter(user=request.user).filter(Q(status='COMPLETED')).order_by('-id')
    paginator = Paginator(complete_applications, 4)
    current_page = paginator.page(int(page))
    context = {
        "title": "Список выполненных заявок",
        "content": current_page,
    }
    return render(request, 'list_of_request/complete_applications.html', context)

@login_required
def assigned_applications(request):
    page = request.GET.get('page', 1)
    assigned_applications = Articles.objects.filter(user=request.user).filter(Q(status='ASSIGNED')).order_by('-id')
    paginator = Paginator(assigned_applications, 4)
    current_page = paginator.page(int(page))
    context = {
        "title": "Список назначенных заявок",
        "content": current_page,
    }
    return render(request, 'list_of_request/assigned_applications.html', context)

@login_required
def application_detail(request, pk):
    application = Articles.objects.filter(user=request.user, converted_to_complete=False).order_by('-id').get(pk=pk)
    context = {
        "title": "Детали заявки",
        "content": application,
    }
    return render(request, 'list_of_request/application_detail.html', context)

# @login_required  
# def list_applications(request):
    
#     table = ApplicationTable(Articles.objects.filter(user=request.user).order_by('-id'))
#     RequestConfig(request, paginate={"per_page": 25}).configure(table)
    
#     # paginator = Paginator(table, 4)
#     # current_page = paginator.page(int(page))
#     context = {
#         "title": "Список заявок",
#         "table": table,
#     }
#     return render(request, 'list_of_request/list_of_applications.html', context)

class ApplicationSearchList(FilterView):
    model = Articles
    context_object_name = 'applications_list'
    template_name = 'list_of_request/search_application.html'
    filterset_class = ArticlesFilter
    paginate_by = 3
    allow_empty = True
    
    def get_queryset(self):
        return Articles.objects.filter(user=self.request.user).order_by('-id')
    
# class ApplicationCompleteDetail(DetailView):
#     model = Articles
#     template_name = 'list_of_request/application_detail.html'
#     # pk_url_kwarg = 'application_id'
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             return Application_complete.objects.filter(user=self.request.user)
#         else:
#             return Application_complete.objects.none() 

class ApplicationDetail(DetailView):
    model = Articles
    template_name = 'list_of_request/application_detail.html'
    # pk_url_kwarg = 'application_id'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Articles.objects.filter(user=self.request.user, converted_to_complete=False)
        else:
            return Articles.objects.none() 

class ApplicationAssignDetail(DetailView):
    model = Articles
    template_name = 'list_of_request/application_assign_detail.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Articles.objects.filter(user=self.request.user, status="Назначена")
        else:
            return Articles.objects.none()
            
class ApplicationCompleteDetail(DetailView):
    model = Articles
    template_name = 'list_of_request/application_complete_detail.html'
    # pk_url_kwarg = 'application_id'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Articles.objects.filter(user=self.request.user, converted_to_complete=True)
        else:
            return Articles.objects.none()

@login_required
def convert_to_complete_application(request, pk):
    application = get_object_or_404(Articles, converted_to_complete=False, user=request.user, pk=pk)
    application.converted_to_complete=True
    application.save()
    return redirect('list_of_request:complete_applications')

@login_required    
def application_delete(request, pk):
    application = get_object_or_404(Articles, user=request.user, pk=pk)
    application.delete()
    
    messages.success(request, 'Заявка была удалена')
    
    return redirect('list_of_request:applications')

@login_required    
def application_edit(request, pk):
    application = get_object_or_404(Articles, user=request.user, pk=pk)
    if request.method=="POST":
        form = ArticlesForm(request.POST, request.FILES, instance=application)
        
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.user = request.user
            new_app.save()
            messages.success(request, 'Заявка успешно изменена')
            return HttpResponseRedirect(reverse('list_of_request:applications'))
        
    else: form = ArticlesForm(instance=application)
    
    data = {
        'form': form
    }
    
    return render(request, 'list_of_request/edit_application.html', data)
    
    
    



def create_application(request):
    if request.method=="POST":
        form = ArticlesForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_app = form.save(commit=False)
            new_app.user = request.user
            new_app.save()
            messages.success(request, 'Заявка успешно добавлена')
            return HttpResponseRedirect(reverse('list_of_request:applications'))
        
        
    else: form = ArticlesForm()
    
    data = {
        'form': form
    }
    
    return render(request, 'list_of_request/create_application.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
            
def archive(request, year):
    if year > 2024:
        return redirect('main')
    return HttpResponse(f"<h1>Архив заявок по годам</h1><p>{year}</p>")   

# class ApplicationAPIView(APIView):
#     def get(self, request):
#         A = Articles.objects.all().order_by('-id')
#         return Response({'fio': ArticlesSerializer(A, many=True).data})
    
#     def post(self, request):
#         serializer = ArticlesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Articles.objects.get(pk=pk)
#         except:
#             return Response({"Ошибка": "Объект не найден"})

#         serializer = ArticlesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Метод 'DELETE' не разрешен"})
#         obj = get_object_or_404(Articles, pk=pk)
    
#         if request.method == 'DELETE':
#         # Удаляем запись
#                 obj.delete()
        
        
        # return Response({"post": "delete post " + str(pk)})
            




