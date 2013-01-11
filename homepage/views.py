from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST
from django_shared.http import JsonResponse

from homepage.forms import EmailForm
from homepage.models import CAMPAIGNS, MEDIUM, SOURCE


def index(request):
    """
    Shows the homepage.
    """
    return render_to_response('homepage/home.html',
        {
            'buddy_form': EmailForm(initial={
                'campaign': CAMPAIGNS.BUDDY,
                'medium': MEDIUM.FORM,
                'source': SOURCE.DIRECT}),
            'vet24seven_form': EmailForm(initial={
                'campaign': CAMPAIGNS.NONE,
                'medium': MEDIUM.FORM,
                'source': SOURCE.DIRECT}),
        },
        context_instance=RequestContext(request))


@require_POST
def email(request):
    """
    Adds a new email record.
    """
    form = EmailForm(request.POST)
    success = form.is_valid()

    if success:
        form.save()

    return JsonResponse(success=success)