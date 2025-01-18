from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Banner, ContactMessage, Bio, FAQ, Map

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('title', 'description', 'background_image')
    search_fields = ('title',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):  # TranslationAdmin deyil, adi ModelAdmin istifadə olunur
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
@admin.register(Bio)
class BioAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('name', 'position', 'email', 'telephone')
    search_fields = ('name', 'position', 'email')

@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
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
    search_fields = ('title',)
class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'map_src')  
    search_fields = ('map_src',)  
    list_filter = ('map_src',)  

admin.site.register(Map, MapAdmin)


