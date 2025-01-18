from django.shortcuts import render
from .models import *


def services (request):
    service_data = Services.objects.first() 
    footer_data = Footer.objects.first()
    services = ServiceIcon.objects.all()
    offerings = Offering.objects.all()
    counters = Counter.objects.all()
    features = VideoPopup.objects.all()
    context = {
        'service': service_data,
        'services': services,
        'features': features,
        'footer': footer_data,
        'offerings': offerings,
        'counters': counters,
    }
    return render(request, 'services.html', context)