from django.http import HttpResponse
from django.shortcuts import render
def task(request):
    c=''
    try:
        
         if request.method=="POST":
          n1=eval(request.POST.get("num1"))
          n2=eval(request.POST.get("num2"))
          ope=(request.POST.get("ope"))
          if ope=="+":
           c=n1+n2
          elif ope=="-":
            c=n1-n2
          elif ope=="*":
           c=n1*n2
          elif ope=="/":
           c=n1/n2
    except:
     c="invalid operation"
    return render(request,"task.html",{'c':c})
 
  
 