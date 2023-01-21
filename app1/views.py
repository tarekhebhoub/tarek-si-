from django.shortcuts import render

# Create your views here.
def create_client(request):
    return render(request,"client.html")