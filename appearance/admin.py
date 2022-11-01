from django.contrib import admin

from .forms import contactform
from .models import (get_more_with_us, menu, slider,
                     feature,icon,banner,image_for_information,
                     information_gallery,experience,contactform,footer)
from mptt.admin import DraggableMPTTAdmin
from adminsortable2.admin import SortableAdminMixin


class menuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "menu_name"
    list_display = ('tree_actions', 'indented_title',"menu_name","menu_status","menu_activate")
    list_display_links = ('indented_title',)
    prepopulated_fields = {"menu_url":("menu_name",)}
    

class slideradmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["slider_order","resim","slider_name","slider_title","slider_button_url"]
    list_display_links = ["slider_name"]  # 'position' is the name of the model field which holds the position of an element
    readonly_fields = ('resim',)
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('slider_name', 'slider_image'),
            }),
            ("Slider Başlık Bölümü",{
            "fields":("slider_title",
                      "slider_title_activate",),
                    }),
            ("Slider Açıklama Bölümü:",{
            "fields":("slider_description",
                      "slider_description_activate",),
                    }),         
            ("Slider Buton Bölümü",{
            "fields":(           
                       "slider_button_title",
                       "slider_button_url",
                       "slider_button_activate",),
                    }),

            ("Slider Statüsü",{
            "fields":("slider_status",),
                        })
        )
    

class featureadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["feature_order","feature_name","feature_status",]
    list_display_links = ["feature_name"]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('feature_name', 'feature_image'),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Birinci Feature Bölümü:",{
            "fields":("feature_first_title",
                       "feature_first_button_title",
                       "feature_first_button_url"),
                    }),
            ("İkinci Feature Bölümü:",{
            "fields":("feature_second_icons",
                       "feature_second_title",
                       "feature_second_url",
                       "feature_second_description"),
                    }),         
            ("Üçüncü Feature Bölümü",{
            "fields":(           
                       "feature_third_icons",
                       "feature_third_title",
                       "feature_third_url",
                       "feature_third_description"),
                    }),

            ("Dördüncü Feature Bölümü:",{
            "fields":("feature_fourth_icons",
                       "feature_fourth_title",
                       "feature_fourth_url",
                       "feature_fourth_description",),
                        }),
            ("Feature Statüsü",{
            "fields":("feature_status",),
                        }),
        )

       
    # def has_add_permission(self,request):
    #     return False
    #def has_change_permission(self,request,obj=None):
    #     return False
    # def has_delete_permission(self,request,obj=None):
    #     return False
    # def has_view_permission(self,request,object=None):
    #     return False


class iconadmin(admin.ModelAdmin):
    admin.site.disable_action("delete_selected")            
    list_display = ["resim","icon_name",]
    list_display_links = ["icon_name"]

class banneradmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["banner_order","banner_name","banner_title","banner_status",]
    list_display_links = ["banner_name"]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('banner_name', 'banner_image'),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Banner Başlığı",{
            "fields":("banner_title",
                       "banner_title_activate",),
                    }),
            ("Banner Açıklaması",{
            "fields":("banner_description",
                       "banner_description_activate",),
                    }),         
            ("Banner Birinci Buton",{
            "fields":(           
                       "banner_button_title",
                       "banner_button_url",
                       "banner_button_activate",),
                    }),

            ("Banner İkinci Buton",{
            "fields":("banner_button2_title",
                       "banner_button2_url",
                       "banner_button2_activate",),
                        }),
            ("Banner Statüsü",{
            "fields":("banner_status",)
                        }),
        )
    
    
    
# class information_gallery_inlines(admin.StackedInline):
#     model = image_for_information
#     extra = 0
#     fields = ("image_for_information_foregeinkey",)
#     show_change_link = False
    
class image_for_information_admin(admin.ModelAdmin):
    list_display = ["resim","image_for_information_name","image_for_information_title",]
    list_display_links = ["image_for_information_name"]
    readonly_fields = ('resim',)
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('image_for_information_name', 'image_for_information_image'),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Resim Başlığı",{
            "fields":("image_for_information_title",
                       "image_for_information_title_url",),
                    }),
            ("Resim Açıklaması",{
            "fields":("image_for_information_description",
                       ),
                    }),         
        )


class information_gallery_admin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","name","menu_name","status"]
    list_display_links = ["name"]
    list_editable = ["status"]
    # inlines = [information_gallery_inlines,]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('name',),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Galeri Başlık ve Açıklama Bilgisi",{
            "fields":("title",
                       "description",
                       "title_and_description_activate",),
                    }),
            ("Galeri Menü Bilgisi",{
            "fields":("menu_name",
                       "menu_activate",),
                    }),
            ("Galeri Statüsü",{
            "fields":("status",
                      "foregeinkey"),
                    }),
        )
    
class experienceadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","name","title","status"]
    list_display_links = ["name"]
    list_editable = ["status"]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('name',"effect_number","title","description",),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Buton Ayarları",{
            "fields":("button_name",
                       "button_url",),
                    }),
            ("Birinci Bilgi Bölümü",{
            "fields":("first_information_name","first_information_number",
                       "first_information_description"),
                    }),
            ("İkinci Bilgi Bölümü",{
            "fields":("second_information_name","second_information_number",
                       "second_information_description"),
                    }),
            ("Üçüncü Bilgi Bölümü",{
            "fields":("third_information_name","third_information_number",
                       "third_information_description"),
                    }),
            ("Dördüncü Bilgi Bölümü",{
            "fields":("fourth_information_name","fourth_information_number",
                       "fourth_information_description"),
                    }),
            ("Resim Bölümü",{
            "fields":("foregeinkey",
                      ),
                    }),
            ("Statü Bölümü",{
            "fields":("status",
                      ),
                    }),
            
        )
    
    
class getmorewithusadmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","name","title","status"]
    list_display_links = ["name"]
    list_editable = ["status"]
    # inlines = [information_gallery_inlines,]
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        if hasattr(formfield, "widget"):
            formfield.widget.can_add_related = True
            formfield.widget.can_delete_related = False
            formfield.widget.can_change_related = True
        else:
            pass  # this relation doesn't have an admin page to add/delete/change

        return formfield

    
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('name',"title",),
            "description":"Genel özellik bilgilerini giriniz.",
            }),
            ("Birinci Bilgi Bölümü",{
            "fields":("first_name",
                      "first_title",
                       "first_description",
                       "first_button_name",
                       "first_button_url",
                       "first_button2_name",
                       "first_button2_url"),
                    }),
            ("İkinci Bilgi Bölümü",{
            "fields":("second_name",
                      "second_title",
                      "second_description",
                       "second_button_name",
                       "second_button_url",
                       "second_button2_name",
                       "second_button2_url"),
                    }),
            ("Üçüncü Bilgi Bölümü",{
            "fields":("third_name",
                      "third_title",
                       "third_description",
                       "third_button_name",
                       "third_button_url",
                       "third_button2_name",
                       "third_button2_url"),
                    }),
            ("Dördüncü Bilgi Bölümü",{
            "fields":("fourth_name",
                      "fourth_title",
                       "fourth_description",
                       "fourth_button_name",
                       "fourth_button_url",
                       "fourth_button2_name",
                       "fourth_button2_url"),
                    }),
            ("Resim Bölümü",{
            "fields":("image",
                      "image_2",
                      "image_3",
                      "image_4"
                      ),
                    }),
            ("Statü Bölümü",{
            "fields":("status",
                      ),
                    }),
            
        )


class footeradmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ["order","menu_name","menu_url","menu_status"]
    list_display_links = ["menu_name"]
    list_editable = ["menu_status"]
    fieldsets = (
        ("Genel Özellikler:", {
            'fields': ('menu_name',"menu_url","menu_kare","menu_status"),
            }),
        )
    
    
admin.site.register(slider, slideradmin)
admin.site.register(menu,menuAdmin)
admin.site.register(feature,featureadmin)
admin.site.register(icon,iconadmin)
admin.site.register(banner,banneradmin)
admin.site.register(image_for_information,image_for_information_admin)
admin.site.register(information_gallery,information_gallery_admin)
admin.site.register(experience,experienceadmin)
admin.site.register(get_more_with_us,getmorewithusadmin)
admin.site.register(contactform)
admin.site.register(footer,footeradmin)



