from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


def request_form_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('request_form')
    else:
        form = RequestForm()

    return render(request, 'callback/request.html', {'form': form})
