from django.shortcuts import render

from blog.models import Blog

# Create your views here.


def home(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog/pages/home.html', context={"blogs": blog},)
