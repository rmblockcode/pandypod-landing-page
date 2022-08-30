from email.header import Header
import requests 
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import HeaderContent, MainPageSectionContent
from products.models import Product
from .forms import SubscriptionForm

# Create your views here.
def index(request):
    header_content = HeaderContent.objects.first()
    section_contents = MainPageSectionContent.objects.filter(active=True).all()
    products = Product.objects.filter(active=True)
    form = SubscriptionForm()

    context = {
        'header_title': header_content.title,
        'header_body': header_content.body,
        'image': header_content.image,
        'section_contents': section_contents,
        'products': products,
        'visit_us_url': settings.VISIT_US_BTN,
        'form': form
    }

    # e = Extractor.from_yaml_file('utils/selector.yml')

    # r = requests.get('https://www.amazon.com/Tea-Infuser-Bamboo-Tumbler-Insulated/product-reviews/B091GG9CC7/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')

    # data = e.extract(r.text)

    return render(request, 'main_page/index.html', context)


def subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'Data saved successfully!'
            }, status=201)
        else:
            errors = ''
            for _, value in form.errors.items():
                errors += value[0] + '. '
            return JsonResponse({'error': errors}, status=400)

    return JsonResponse({
            'error': 'An error has ocured. Try again later!'
        }, status=400)