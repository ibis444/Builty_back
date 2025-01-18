from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import ContactForm

def contact(request):
    banner = Banner.objects.first() 
    map_info = Map.objects.first() 
    faqs = FAQ.objects.all()
    bio = Bio.objects.first()  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Mesajınız uğurla göndərildi! 😊")
            return redirect('contact:contact')  
        else:
            messages.error(request, "Xəta baş verdi. Təkrar cəhd edin.")

    else:
        form = ContactForm() 
    context = {
        'map_info': map_info,
        'faqs': faqs,
        'bio': bio,
        'banner': banner,
        'form': form,
    }
    return render(request, 'contact.html', context)
