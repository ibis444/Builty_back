from modeltranslation.translator import translator, TranslationOptions
from .models import *

# Services Model Translation
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'breadcrumb_title', 'breadcrumb_home')

translator.register(Services, ServicesTranslationOptions)

# ServiceIcon Model Translation
class ServiceIconTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(ServiceIcon, ServiceIconTranslationOptions)

# Counter Model Translation
class CounterTranslationOptions(TranslationOptions):
    fields = ('label', 'description')

translator.register(Counter, CounterTranslationOptions)

# VideoPopup Model Translation
class VideoPopupTranslationOptions(TranslationOptions):
    fields = ('title',)  # Only title is necessary for translation

translator.register(VideoPopup, VideoPopupTranslationOptions)

# Offering Model Translation
class OfferingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Offering, OfferingTranslationOptions)

class FooterTranslationOptions(TranslationOptions):
    fields = ('information_text', 'address', 'phone', 'email') 

translator.register(Footer, FooterTranslationOptions)
