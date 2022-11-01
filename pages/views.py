from django.shortcuts import render
from .models import projectpage, teampage,sponsorpage,page
from setting.models import site
from appearance.models import menu,footer
from django.shortcuts import get_object_or_404
from appearance.forms import contactform
from django.urls import reverse
from django.http import HttpResponseRedirect

def bos(request):
    return False

def index(request):
    context = dict()
    context = {
        "team":teampage.objects.filter(status="Published",).order_by("order"),
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
    }
    return render(request,template_name="theme/page/team.html",context=context)

def sponsorview(request):
    context = dict()
    context = {
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
        "sponsor":sponsorpage.objects.filter(status="Published",).order_by("order"),

    }
    return render(request,template_name="theme/page/sponsor.html",context=context)

def projectpageview(request):
    context = dict()
    context = {
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
        "projects":projectpage.objects.filter(status="Published",).order_by("order"),
    }
    return render(request,template_name="theme/page/projects.html",context=context)


def projectdetailview(request,slug):
    context = {
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
        "projects":projectpage.objects.filter(status="Published",).order_by("order"),
        "projectdetail":get_object_or_404(projectpage,status="Published",slug=slug),
    }
    return render(request,template_name="theme/page/projectdetail.html",context=context)


def pageview(request,slug):
    context = {
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
        "page":page.objects.filter(status="Published",),
        "pagedetail":get_object_or_404(page,status="Published",slug=slug),
    }
    return render(request,template_name="theme/page/pagedetail.html",context=context)


def iletisimpageview(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("thanks"))          
    else:
        form = contactform(request.POST)
    context = dict()
    context = {
        "site_footer":site.objects.order_by("order").first(),
        "footer":footer.objects.filter(menu_status="Published",).order_by("order"),
        "site_favicon": "media/"+site.objects.values_list("site_favicon")[0][0],
        "menu":menu.objects.all(),
        "form": form,
    }
    return render(request,template_name="theme/page/contact-form.html",context=context)
def thanks(request):
    return render(request,"theme/thanks.html",)