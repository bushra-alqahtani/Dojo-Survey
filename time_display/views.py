from multiprocessing import context
from django.shortcuts import redirect, render

from time import gmtime, strftime



def index(request):
    return render(request,'index.html')


    
def show(request):
    name=request.POST["name1"] # to avoid the error just write request.post.get("name")
    location=request.POST["location"]
    language=request.POST["language"]
    comment=request.POST["comment"]

    context = {
    	"name" :name,
    	"location" :location,
        "language" :language,
    	"comment" :comment
    }
    return render(request,"result.html",context)









