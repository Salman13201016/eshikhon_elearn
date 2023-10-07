from django.shortcuts import render

from elearn.models import Categories
from course.models import courses
from itertools import zip_longest

def index(req):
    data = Categories.objects.all()
    cat = {'all_cat':data}
    return render(req,'user/home.html',cat)

def product_list(req,id):
    course_obj = courses.objects.filter(cat_id_id=id)
    discount_fee_list = []
    for i in course_obj:
        print(i)
        print("helo",i.fee)
        print("heellwdadasd",i.discount)
        discount_fee = i.fee - ((i.fee*i.discount)/100)
        discount_fee_list.append(discount_fee)
    # data = Categories.objects.all()
    zipped_data = zip_longest(course_obj, discount_fee_list)

    course_obj1 = {'all_course':zipped_data}
    return render(req,'user/product_list.html',course_obj1)

# Create your views here.
def details(req,id):
    course_obj = courses.objects.get(id=id)
    discount_fee = course_obj.fee - ((course_obj.fee*course_obj.discount)/100)
    course_obj1 = {'all_course':course_obj,"discount":discount_fee}
   
    return render(req,'user/detail.html',course_obj1)