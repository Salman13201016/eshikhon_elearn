from django.shortcuts import render,HttpResponse
from elearn.models import Categories

# Create your views here.

def index(request):
    all_cats = Categories.objects.all().order_by('-id')
    data = {'data':all_cats}
    return render(request,'admin/course_admin.html',data)
