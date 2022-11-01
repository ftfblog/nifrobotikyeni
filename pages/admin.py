from django.contrib import admin
from .models import teampage,sponsorpage,projectpage,page
from adminsortable2.admin import SortableAdminMixin


class teampageadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","Name","status"]
    list_display_links = ["Name"]
    list_editable = ["status"]



class sponsorpageadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","name","status"]
    list_display_links = ["name"]
    list_editable = ["status"]


class projectpageadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","title","status"]
    list_display_links = ["title"]
    list_editable = ["status"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('title',),
            }),
            ("Diğer ayarlar",{
            "fields":("image",
                       "slug",
                       "description",
                       "içerik"),
                    }),
            ("Statü Bölümü",{
            "fields":("status",
                      ),
                    }),
            
        )
    
    

class pageadmin(admin.ModelAdmin):
    list_display = ["title","status"]
    list_display_links = ["title"]
    list_editable = ["status"]
    
admin.site.register(sponsorpage,sponsorpageadmin)
admin.site.register(teampage,teampageadmin)
admin.site.register(projectpage,projectpageadmin)
admin.site.register(page,pageadmin)


