from django.shortcuts import render, redirect
from .models import short_url
from .forms import UrlForm
from .shortner import shortner

# Create your views here.

def Home(request, token):
    long_url = short_url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, "short/make.html", {'form':form, 'a':a})