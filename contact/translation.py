from modeltranslation.translator import translator ,register, TranslationOptions
from .models import *


# Banner Model Translation
@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # title və description sahələri üçün az, en, ru yaradılacaq

# Bio Model Translation
@register(Bio)
class BioTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'address')  # name, position və address üçün az, en, ru yaradılacaq

# FAQ Model Translation
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # title və description üçün az, en, ru yaradılacaq
