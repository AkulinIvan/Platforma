from django.views import View
from .mixins import ApplicationMixin
from handbook.models import House, Worker
from .filters import ArticlesFilter
from django_filters.views import FilterView
from rest_framework import generics
from django.db.models import F

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import redirect, render


from .permissions import  IsOwnerOrReadOnly

from list_of_request.serializers import ArticlesSerializer

from .models import  Articles
from .forms import ArticlesForm
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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


class ArticlesAPIList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticated,  )
    
    

class ArticlesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticated,  )
    
class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,  )




# class ApplicationList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'list_of_request/list_of_applications.html'

#     def get(self, request):
#         content = Articles.objects.all().order_by('-id')
#         return Response({'applications': content})
class ApplicationList(ListView):
    model = Articles
    context_object_name = 'applications_list'
    template_name = 'list_of_request/list_of_applications.html'
    paginate_by = 3
    allow_empty = True
    context_object_name = 'content'
    

    
    def get_queryset(self):
        return Articles.objects.all().order_by('-id')
        
    
class ApplicationSearchList(FilterView):
    model = Articles
    context_object_name = 'applications_list'
    template_name = 'list_of_request/search_application.html'
    filterset_class = ArticlesFilter
    paginate_by = 3
    allow_empty = True
    
    def get_queryset(self):
        return Articles.objects.all().order_by('-id')
    



class ApplicationDetail(DetailView):
    model = Articles
    template_name = 'list_of_request/application_detail.html'
    pk_url_kwarg = 'application_id'
    
    
    

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
            
def archive(request, year):
    if year > 2024:
        return redirect('main')
    return HttpResponse(f"<h1>Архив заявок по годам</h1><p>{year}</p>")    
        
def create_application(request):
    if request.method=="POST":
        form = ArticlesForm(request.POST, request.FILES)
        
        # worker = Worker.objects.filter(address=F('articles__house')).values_list('worker', flat=True)#сделать двойную проверку по адресу и типу заявки, прежде чем выбирать worker
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
            




