from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('homepage/home.html',
        dict(
            test=1,
        ),
        context_instance=RequestContext(request))