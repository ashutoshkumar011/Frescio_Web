from django.http.response import HttpResponse
from django.shortcuts import render
import csv

from user.models import crop
# Create your views here.

def sellcrops(request):
    if request.user.is_authenticated:
        if request.POST:
            name = request.POST.get('name')
            if name == "add_new_crop":
                crop_name = request.POST['crop_name']
                price = request.POST['price']
                quantity = request.POST['quantity']
                photo = request.FILES['photo']
                new_crop = crop( user=request.user, crop_name = crop_name, price=price, quantity=quantity, photo=photo)
                new_crop.save()
                print(new_crop)
        context = {}
        # context['crop'] = {'sdf','asd','lol'}
        data=[]
        # data = pd.read_csv("fertilizer.csv")
        with open('home/fertilizer.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row[1])
        data.sort()
        context['crop'] = data

        crops_added = crop.objects.filter(user=request.user)
        
        return render( request, 'ecommerce/sell.html', {'crop':data, 'crops_added': crops_added} )
    else:
        return HttpResponse("sorry")
