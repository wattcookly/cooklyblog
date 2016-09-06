from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from reportlab.pdfgen import canvas
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

    response = render_to_response('index.html', data)

    return response


def generate_pdf(res):
    res['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    pdf_file = canvas.Canvas(res)
    pdf_file.drawString(100, 100, "Hello world.")
    pdf_file.showPage()
    pdf_file.save()
