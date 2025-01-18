from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('title', 'breadcrumb_title', 'breadcrumb_home')
    search_fields = ('title', 'description')

@admin.register(ServiceIcon)
class ServiceIconAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Counter)
class CounterAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('label', 'number', 'suffix', 'description')
    search_fields = ('label', 'description')

@admin.register(VideoPopup)
class VideoPopupAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('title', 'image', 'video_file')
    search_fields = ('title',)

@admin.register(Offering)
class OfferingAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("information_text", "email", "phone")
    fields = ("information_text", "address", "phone", "email", "facebook_link", "instagram_link", "whatsapp_link")


