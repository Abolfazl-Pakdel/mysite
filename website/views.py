from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
# def http_test(request):
#   return HttpResponse('<h1>this is a test</h1>')

# def json_test(request):
#   return JsonResponse({'name':'Abolfazl'})
def index_view(request):
  return render(request,'index.html')

def about_view(request):
  return render(request, 'about.html')

def contact_view(request):
  return render(request, 'contact.html')