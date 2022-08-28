from landing_page.settings import MAIN_PAGE_URL
from .models import CompanySettings, SocialMedia, HeaderContent

def company_settings(request):
    company = CompanySettings.objects.first()

    kwargs = {
        'main_page_url': MAIN_PAGE_URL,
        'company_logo': company.logo.url,
    }

    social_medias = SocialMedia.objects.filter(active=True).all()

    for social_media in social_medias:
        kwargs.update({
            social_media.unique_description: (
                social_media.url,
                social_media.logo.url,
                social_media.logo_bg_white.url)
        })

    return kwargs
