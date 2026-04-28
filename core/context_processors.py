from .models import PageHeader

def header_images(request):
    # This creates a dictionary where you can access headers by page name
    # e.g., {{ headers.about.image.url }}
    headers = {h.page: h for h in PageHeader.objects.all()}
    return {'headers': headers}