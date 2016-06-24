from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from blogpost.models import BlogPost
from blogpost.forms import BlogPostForm


def homepage(request):

    # if request is post,
    if request.POST:
        # create a form instance and populate it with data from the request:
        form = BlogPostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BlogPostForm()

    blog_list = BlogPost.objects.all()
    data = {
        'data_blog': blog_list,
        'form': form
    }
    data.update(csrf(request))

    return render_to_response('index.html', data)
