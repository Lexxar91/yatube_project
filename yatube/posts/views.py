from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello Universal')

def groups_posts(request, pk):
    return HttpResponse(f'Groups posts {pk}')