from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.forms import BlogPostForm
from .models import *

# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})
@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "blog/add_blog.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "blog/add_blog.html", {'form':form})
