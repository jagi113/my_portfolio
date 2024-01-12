from django.shortcuts import render

def mybio(request):
    return render(request, 'my_bio.html')

def contact(request):
    return render(request, 'contact.html')