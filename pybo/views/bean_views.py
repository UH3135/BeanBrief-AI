from django.shortcuts import render
from ..models.bean import Beans

def bean_list(request):
    beans = Beans.objects.all().order_by('-rating')
    return render(request, 'pybo/bean_list.html', {'beans': beans})

def bean_detail(request, bean_id):
    bean = Beans.objects.get(id=bean_id)
    return render(request, 'pybo/bean_detail.html', {'bean': bean}) 