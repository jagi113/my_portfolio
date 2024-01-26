from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def mybio(request):
    return render(request, 'my_bio.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"Message from Portfolio website from {name}"
            message = f"Sender's Name: {name}\nSender's Email: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                message,
                email,
                [settings.EMAIL_ADDRESS],
                fail_silently=False,
            )

            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})