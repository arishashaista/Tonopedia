from django.shortcuts import render
from .models import Product

def show_main(request):
    model = Product.objects.all()
    context = {
        'npm' : '2306123456',
        'name': 'Arisha Shaista Aurelya',
        'class': 'PBP C',
        'product_name': 'Soffell',
        'price': 27000,
        'description': 'Soffell adalah penangkal nyamuk yang memiliki wangi lembut dan tidak membuat kulit kering',
    }

    return render(request, "main.html", context)