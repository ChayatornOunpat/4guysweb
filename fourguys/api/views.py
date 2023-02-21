from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
	return HttpResponse('main') 


def initialize(response):
	return render(response, 'api/index.html')