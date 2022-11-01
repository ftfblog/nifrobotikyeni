from django.contrib import admin
from .models import site
from adminsortable2.admin import SortableAdminMixin

class siteadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","sitename",]
    list_display_links = ["sitename"]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('sitename',"siteslogan","site_favicon","site_logo"),
            }),
            ("Site İletişim Bilgileri",{
            "fields":("site_email",
                       "site_phone",
                       "site_adres",
                       "site_adres_url",
                       ),
                    }),
            
        ("Sosyal Medya Adresleri:", {
            'fields': ('facebook_url',"twitter_url","instgram_url"),
            }),
        ("copyright", {
            'fields': ("copyright",),
            }),
        )
admin.site.register(site,siteadmin)


