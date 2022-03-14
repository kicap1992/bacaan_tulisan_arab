from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import tb_bacaan

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    bacaans = tb_bacaan.objects.filter(Q(kategori__icontains=q))
    context = {'bacaans':bacaans}
    return render(request,'base/home.html',context)

def bacaan(request,pk):
    check = tb_bacaan.objects.filter(id=pk).exists()
    if check == False:
        return redirect('home')
    
    bacaannya = tb_bacaan.objects.get(id=pk)
    print(bacaannya.id)
    if(bacaannya.id != 1 and bacaannya.id != 2):
        style = "width:30%; height: 30%;"
    else:
        style = ''
        

        
    context = {'bacaan':bacaannya, 'style': str(style)}
    return render(request,'base/bacaan.html',context)
