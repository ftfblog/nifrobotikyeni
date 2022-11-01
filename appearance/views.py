from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactform
from .models import slider,menu,feature,icon,banner,information_gallery,experience,get_more_with_us,footer
from setting.models import site
from django.urls import reverse

def index(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("thanks"))          
    else:
        form = contactform(request.POST)
    context = {
        "site_adı": site.objects.values_list("sitename").first(),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "site":site.objects.order_by("order").first(),
        "menu":menu.objects.all(),
        "sliders":slider.objects.filter(slider_status ="Published").order_by("slider_order"),
        "feature":feature.objects.filter(feature_status = "Published").order_by("feature_order").first(),
        "icons":icon.objects.all(),
        "banner":banner.objects.filter(banner_status="Published").order_by("banner_order").first(),
        "title_and_description":information_gallery.objects.filter(status="Published",title_and_description_activate=True).order_by("order").first(),
        "gallery":information_gallery.objects.filter(status="Published",).order_by("order"),
        "experience":experience.objects.filter(status="Published",).order_by("order"),
        "getmorewithus":get_more_with_us.objects.filter(status="Published",).order_by("order").first(),
        "form": form,
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order")

    }
    return render(request,"theme/index.html",context=context)

def thanks(request):
    return render(request,"theme/thanks.html",)
