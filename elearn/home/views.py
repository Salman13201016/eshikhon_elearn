from django.shortcuts import render

from elearn.models import Categories
from course.models import courses

def index(req):
    data = Categories.objects.all()
    cat = {'all_cat':data}
    return render(req,'user/home.html',cat)

def product_list(req,id):
    course_obj = courses.objects.filter(cat_id_id=id)
    # data = Categories.objects.all()
    course_obj1 = {'all_course':course_obj}
    return render(req,'user/product_list.html',course_obj1)

# Create your views here.
