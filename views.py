from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect, render, Http404
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from blog.views import index as blog_index

def index(request, template_name='blog/index.html'):
    """
    The site homepage.
    """
    return blog_index(request)
#    return render_to_response(template_name,
#        dict(
#            test=1,
#        ),
#        context_instance=RequestContext(request))
