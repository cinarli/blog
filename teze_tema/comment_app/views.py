from django.shortcuts import render

# Create your views here.
def comment_list(request):
    return render(request,'comment.html',{})