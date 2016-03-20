from django.shortcuts import render
from .forms import SignUpForm, ContactForm


def home(request):
    title = "My little {}" .format(request.user)
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        'form': form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'Initial full_name'
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank You"
        }
    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        full_name = form.cleaned_data['full_name']

    context = {
        'form': form,
    }
    return render(request, 'forms.html', context)