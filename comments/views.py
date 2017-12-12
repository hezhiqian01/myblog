from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from users.models import User
from .models import Comment
from blog.models import Blog
# Create your views here.


def post_comment(request, post_pk):
    print(post_pk)
    blog = get_object_or_404(Blog, pk=post_pk)
    user = get_object_or_404(User, pk=request.user.id)
    print("i am here")
    if request.method == 'POST':
        print("i ma here")
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = user
            comment.save()
            return redirect('/')
        else:
            comments = Comment.objects.filter(blog=blog)
            context = {'blog':blog,
                       'form':form,
                       'comments':comments
                       }
        return render(request, 'blog/detail.html/' + str(post_pk) , context=context)



