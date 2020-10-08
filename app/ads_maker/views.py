from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import SiteMap, Site
from .forms import NewSiteForm


def ads_maker(request):
    context = {}

    sites = Site.objects.all().order_by('-updated_at')[:10]
    context['sites'] = {site.pk: site for site in sites}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewSiteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_site = Site()
            new_site.url = form.cleaned_data['url']
            new_site.check_status()
            new_site.save()


            # redirect to a new URL:
            return HttpResponseRedirect('/ads_maker/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewSiteForm()



    context['form'] = form

    return render(request, 'ads_maker.html', {'context': context})
