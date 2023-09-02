from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .models import Categories
def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    cat_name = request.POST.get('cat_name')
    if cat_name:
        if len(cat_name)<4:
            messages.success(request, 'the cat name field length minimum 3')
            
        elif Categories.objects.filter(name=cat_name).exists():
            messages.success(request, 'This value already exists.')
        else:

            cat_obj = Categories()
            cat_obj.name = cat_name

            cat_obj.save()
            messages.success(request, 'Category Inserted successfully')    
    else:
        messages.success(request, 'The field can not be empty')
       

    # cat_obj = Categories()
    # cat_obj.name = cat_name

    # cat_obj.save()
    # messages.success(request, 'Category Inserted successfully')
    return redirect('catadmin')

    