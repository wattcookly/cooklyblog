from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from blogpost.models import BlogPost
from blogpost.forms import BlogPostForm

# Create your views here.
import logging
logger = logging.getLogger(__name__)


def homepage(request):

    if request.POST:
        # create a form instance and populate it with data from the request:
        form = BlogPostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            logger.info(form.cleaned_data)
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
    logger.info('hehehehe')

    return render_to_response('index.html', data)
