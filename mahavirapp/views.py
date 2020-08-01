from django.shortcuts import render

# Create your views here.

def baseView(request):
	return render(request,'mahavirapp/base1.html')