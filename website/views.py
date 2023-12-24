from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context={'title':'django developer'}
    return render (request ,'website/index.html',context)
