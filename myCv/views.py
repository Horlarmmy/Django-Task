from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse('My CV')
	return render(request, 'index.html')

