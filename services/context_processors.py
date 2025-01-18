from .models import Footer

def footer_info(request):
    try:
        footer = Footer.objects.first()
        return {'footer': footer}
    except Footer.DoesNotExist:
        return {'footer': None}
