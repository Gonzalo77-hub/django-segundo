from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string



def index(request):
    palabra = get_random_string(length=14)
    context = {"word": palabra}
    
    if 'cont' in request.session:
        request.session['cont'] += 1 
    else:
        request.session['cont'] = 1

    return render(request,'index2.html',context)

def reset(request):
    request.session['cont'] = 0

    return redirect("/word")




