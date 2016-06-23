from django.shortcuts import render_to_response
from blogpost.models import BlogPost

# Create your views here.


def homepage(request):
    blog_list = BlogPost.objects.all()
    data = {
        'data1': 'hello',
        'data2': 'its me',
        'data_blog': blog_list,
    }
    return render_to_response('index.html', data)
