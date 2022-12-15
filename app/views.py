from django.shortcuts import render
from . models import Products 
from django.views import View


# Create your views here.
def home(request):
    return render(request, "app/home.html")
class CategoryView(View):
    def get(self, request, val):
        products= Products.objects.filter(category=val)
        return render(request, 'app/category.html', locals())