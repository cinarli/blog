from django.shortcuts import render

# Create your views here.
def author_list(request):
    return render(request,'author.html',{})