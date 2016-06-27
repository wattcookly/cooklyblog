from django.shortcuts import render_to_response

# Create your views here.


def activity_select_page(request):

    return render_to_response('activity_select.html')
