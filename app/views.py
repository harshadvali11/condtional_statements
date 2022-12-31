from django.shortcuts import render

# Create your views here.

def operations(request):
    #a=int(input('enter'))
    d={'a':66123,'b':225,'c':2388}
    return render(request,'operations.html',d)