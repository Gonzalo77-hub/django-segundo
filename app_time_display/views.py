from django.shortcuts import render, HttpResponse

from time import gmtime, strftime,localtime
    
def index(request):
    context = {
        "time": strftime("%H:%M %p", localtime()),
        "time2": strftime("%b %d, %Y", localtime()),
    }
    return render(request,'index.html', context)