from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    
    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, please log in.')
        del(request.session['register_form_data'])
        
    return redirect('authors:register')