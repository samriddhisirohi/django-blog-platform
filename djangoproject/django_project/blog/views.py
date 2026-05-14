from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.




def home(request):
     context= {
          'posts': Post.objects.all()  
           
            # this is the context dictionary that we will pass to the template. 
                            # It contains the data that we want to display on the home page. 
                            # In this case, we are passing the list of posts to the template.
     }
     return render(request, 'blog/home.html',context)


def about(request):
     return render(request, 'blog/about.html',{'title': 'About'}) 
