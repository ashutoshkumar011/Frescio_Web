from django.shortcuts import render

# Create your views here.

def sellcrops(request):
    return render( request, 'ecommerce/sell.html')