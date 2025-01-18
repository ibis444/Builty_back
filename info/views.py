from django.shortcuts import render
from .models import *

from django.shortcuts import render
from .models import *


def home(request):
    sliders = Slider.objects.all()
    services = HomeService.objects.all()
    counters = Counter.objects.all()
    features = CoreFeature.objects.all().order_by('num')
    video = CoreFeatureVideo.objects.first()
    about_info = About.objects.first()
    section_info = CoreFeatureSection.objects.first()
    renovation_info = RenovationInfo.objects.first()

    return render(request, 'index.html', {
        'sliders': sliders,
        'services': services,
        'about_info': about_info,
        'counters': counters,
        'features': features,
        'video': video,
        'section_info': section_info,
        'renovation_info': renovation_info,
    })


def about(request):
    about_data = AboutUs.objects.first() 
    counters = Counter.objects.all()
    data = HowItWorks.objects.first()
    renovation_info = RenovationInfo.objects.first()
    about_section = AboutSection.objects.first() 
    context = {
        'about': about_data ,
        'counters': counters,
        'data': data, 
        'renovation_info': renovation_info,
        'about_section': about_section, 
    }
    return render(request, 'about.html', context)