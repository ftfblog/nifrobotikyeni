from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from phone_field import PhoneField


STATUS = (
        ('Published', 'Yayınla'),
        ('Draft', 'Taslak'),
    )

Phoneoremail = (
    ("Phone","Telefon",),
    ("Email","Mail"),
    ("Both","İkiside Olabilir")
)

class menu(MPTTModel):
    ust_menu = TreeForeignKey("self",related_name="children", on_delete=models.CASCADE,null=True,blank=True,verbose_name="üst kategori",db_constraint=False)
    menu_name = models.CharField(("Menü Adı"), max_length=100)
    menu_url = models.SlugField(("Menü Url"), max_length=300,primary_key=True,unique=True,blank=True)
    menu_status = models.CharField(verbose_name="Menü Statüsü",max_length=100, choices=STATUS)
    menu_activate = models.BooleanField(default=False,verbose_name="Menü Çizgisi")
    
    def __str__(self):
        return self.menu_name
    class MPTTMeta:
        order_insertion_by = ['menu_name']
        parent_attr = 'ust_menu'
    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.menu_name]                  # post.  use __unicode__ in place of
        k = self.ust_menu
        while k is not None:
            full_path.append(k.menu_name)
            k = k.ust_menu
        return ' / '.join(full_path[::-1])
    class Meta:
        verbose_name_plural='1) Menü'
        verbose_name = "Menü"

class slider(models.Model):
    slider_name = models.CharField(max_length=200,primary_key=True,verbose_name="Slider Adı")
    slider_image = models.ImageField(("slider resmi"), upload_to="media/images/site/slider")
    slider_title = models.CharField(max_length=100,verbose_name="Slider Başlık")
    slider_title_activate = models.BooleanField(default=True,verbose_name="Slider Adının Aktiflik Durumu")
    slider_description = models.TextField(verbose_name="Slider Açıklaması")
    slider_description_activate = models.BooleanField(default=True,verbose_name="Slider Açıklaması Aktiflik Durumu")
    slider_button_title = models.CharField(max_length=50,verbose_name="Slider Buton Başlık")
    slider_button_url = models.SlugField(verbose_name="Slider Buton Url Adresi")
    slider_button_activate = models.BooleanField(default=True,verbose_name="Slider Buton Aktiflik Durumu")
    slider_order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="sıra")  
    slider_status = models.CharField(max_length=100,choices=STATUS,verbose_name="Slider Statüsü")
    def __str__(self):
        return self.slider_name
    def delete(self, *args, **kwargs):
        self.slider_image.delete()
        super(slider, self).delete(*args, **kwargs)
    def resim(self):
        if self.slider_image:
            return mark_safe(f"<img src={self.slider_image.url} width=100 height=100></img>")
        return mark_safe(f"<h3>{self.slider_name} adlı slider resime sahip değil</h3>")
    class Meta:
        ordering = ('slider_order',)
        verbose_name_plural='2) Slider'
        verbose_name = "Slider"
class icon(models.Model):
    icon_name = models.CharField(max_length=100,verbose_name="İcon Adı")
    icon_image = models.ImageField(("icon image"), upload_to="media/images/site/icons/",blank=True,null=True)
    icon_image_url = models.URLField(("icon resim url adresi"),blank=True,null=True)
    
    def __str__(self):
        self.icon_image
        return self.icon_name
    def clean(self):
        if not (self.icon_image or self.icon_image_url):
            raise ValidationError("Lütfen en az bir image bölümünü giriniz.")
    def delete(self, *args, **kwargs):
        self.icon_image.delete()
        super(icon, self).delete(*args, **kwargs)
    def resim(self):
        if self.icon_image:
            return mark_safe(f"<img src={self.icon_image.url} width=64 height=64></img>")
        if self.icon_image_url:
            return mark_safe(f"<img src={self.icon_image_url} width=64 height=64></img>")
        return mark_safe(f"<h3>{self.icon_name} adlı yazı resime sahip değil</h3>")
    class Meta:
        verbose_name_plural='3) İcon'
        verbose_name = "İcon"
class feature(models.Model):
    feature_name = models.CharField(max_length=100,verbose_name="Feature Adı")
    feature_image = models.ImageField(("Resim"), upload_to="media/images/site/features/",help_text="En uygun 415x592 boyutudur.")
    
    feature_first_title = models.CharField(max_length=100,verbose_name="Başlık")
    feature_first_button_title = models.CharField(max_length=100,verbose_name="Buton Başlık")
    feature_first_button_url = models.SlugField(verbose_name="Buton url")
    
    feature_second_icons = models.ForeignKey("appearance.icon",default="project",related_name="feature_second_icons", verbose_name=("İcon Seç"), on_delete=models.PROTECT,db_constraint=False)
    feature_second_title = models.CharField(max_length=100,verbose_name="Başlık")
    feature_second_url = models.SlugField(verbose_name="Url Adresi")
    feature_second_description = models.TextField(verbose_name="Açıklama")
    
    feature_third_icons = models.ForeignKey("appearance.icon",related_name="feature_third_icons", verbose_name=("İcon Seç"), on_delete=models.PROTECT,db_constraint=False)
    feature_third_title = models.CharField(max_length=100,verbose_name="Başlık")
    feature_third_url = models.SlugField(verbose_name="Url Adresi")
    feature_third_description = models.TextField(verbose_name="Açıklama")
    
    feature_fourth_icons = models.ForeignKey("appearance.icon",related_name="feature_fourth_icons", verbose_name=("dördüncü icon"), on_delete=models.PROTECT,db_constraint=False)
    feature_fourth_title = models.CharField(max_length=100,null=True,blank=True,verbose_name="Başlık")
    feature_fourth_url = models.SlugField(verbose_name="Url Adresi")
    feature_fourth_description = models.TextField(verbose_name="Açıklama")
    
    feature_order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    feature_status = models.CharField(max_length=100,choices=STATUS,default="Published",verbose_name="Feaure Statüsü")
    
    def __str__(self):
        return self.feature_name
    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        super(feature, self).delete(*args, **kwargs)
    class Meta:
        verbose_name='Feature'
        verbose_name_plural='4) Feature'
        ordering = ('feature_order',)
class banner(models.Model):
    banner_name = models.CharField(max_length=200,verbose_name="Banner Adı")
    banner_image = models.ImageField(("Banner resmi"), upload_to="media/images/site/banner",help_text="1770x550 boyutunda resim önerilmektedir.")
    
    banner_title = models.CharField(max_length=100,null=True,blank=True,verbose_name="Banner Başlığı")
    banner_title_activate = models.BooleanField(default=True,verbose_name="Banner Başlığı Aktiflik Durumu")
    
    banner_description = models.TextField(null=True,blank=True,verbose_name="Banner Açıklaması")
    banner_description_activate = models.BooleanField(default=True,verbose_name="Banner Açıklaması Aktiflik Durumu")
    
    banner_button_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Banner Buton Başlığı")
    banner_button_url = models.SlugField(null=True,blank=True,verbose_name="Banner Buton Url Adresi")
    banner_button_activate = models.BooleanField(default=True,verbose_name="Banner Buton Başlığı Aktiflik Durumu")
    
    banner_button2_title = models.CharField(max_length=50,null=True,blank=True,verbose_name="Banner Buton Başlığı")
    banner_button2_url = models.SlugField(null=True,blank=True,verbose_name="Banner Buton Url Adresi")
    banner_button2_activate = models.BooleanField(default=True,verbose_name="Banner Buton Başlığı Aktiflik Durumu")
    
    banner_order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    banner_status = models.CharField(max_length=100,choices=STATUS,verbose_name="Banner Statüsü")
    def __str__(self):
        return self.banner_title
    def delete(self, *args, **kwargs):
        self.banner_image.delete()
        super(banner, self).delete(*args, **kwargs)
    def clean(self):
        liste = {}
        if not (self.banner_button_title and self.banner_button_url and self.banner_button_activate):
            if None == self.banner_button_title and None == self.banner_button_url and False != self.banner_button_activate:
                liste['banner_button_url'] = ValidationError("Eğera bu bölüm aktifse buton url dolu olmalı.")
                liste['banner_button_title'] = ValidationError("Eğer bu bölüm aktifse button title dolu olmalı.")
            elif (None == self.banner_button_url and True == self.banner_button_activate):
                liste['banner_button_url'] = ValidationError("Eğer bu bölüm aktifse button url dolu olmalı.")
            elif None == (self.banner_button_title) and False != self.banner_button_activate:
                liste['banner_button_title'] = ValidationError("Eğer bu bölüm aktifse button title dolu olmalı.")    
        
        if not (self.banner_button2_title and self.banner_button2_url and self.banner_button2_activate):
            if None == (self.banner_button2_title or self.banner_button2_url) and self.banner_button2_activate:
                liste['banner_button2_url'] = ValidationError("Eğer bu bölüm aktifse buton url dolu olmalı.")
                liste['banner_button2_title'] = ValidationError("Eğer bu bölüm aktifse button title dolu olmalı.")
            elif (self.banner_button2_title and self.banner_button2_activate):
                liste['banner_button2_url'] = ValidationError("Eğer bu bölüm aktifse button url dolu olmalı.")
            else:
                if (self.banner_button2_url and self.banner_button2_activate):
                    liste['banner_button2_title'] = ValidationError("Eğer bu bölüm aktifse button title dolu olmalı.")
        if liste:
            raise ValidationError(liste)
    class Meta:
        verbose_name_plural='5) Banner'
        verbose_name = "Banner"
        ordering = ('banner_order',)
    

class information_gallery(models.Model):
    name =  models.CharField(verbose_name="Galeri Adı",max_length=200,help_text="admin sayfasında sizin göreceğiniz isim",)
    title =  RichTextField(verbose_name="Galeri Başlığı",max_length=200,help_text="admin sayfasında sizin göreceğiniz isim",config_name="Başlık",null=True,blank=True)
    description =  RichTextField(max_length=100,verbose_name="Galeri Açıklaması",null=True,blank=True)
    title_and_description_activate = models.BooleanField(default=True,verbose_name="Galeri Başlık Ve Açıklamanın aktiflik Durumu")
    menu_name = models.CharField(max_length=200,verbose_name="Galeri Menü Adı")
    menu_activate = models.BooleanField(default=False,verbose_name="Galeri Menu aktiflik Durumu")
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Gallery Statüsü")
    foregeinkey = models.ManyToManyField("image_for_information", verbose_name="Resim Seçimi",blank=False)

    def __str__(self):
        return self.name
    def clean(self):
        if self.title_and_description_activate == True:            
            if 0 == len(self.title) and 0 == len(self.description):
                raise ValidationError({"title":"Eğer bu bölüm aktifse başlık dolu olmalı.","description":"Eğer bu bölüm aktifse açıklama dolu olmalı. "})
            elif 0 == len(self.title):
                raise ValidationError({"title":"Eğer bu bölüm aktifse başlık dolu olmalı."})
            elif 0 == len(self.description):
                raise ValidationError({"description":"Eğer bu bölüm aktifse açıklama dolu olmalı."})

            
    class Meta:
        ordering = ('order',)
        verbose_name='Galeri Bilgisi'
        verbose_name_plural='6) Galeri Bilgisi'

class image_for_information(models.Model):
    image_for_information_name = models.CharField(max_length=200,verbose_name="Resim Adı",null=False,blank=False)
    image_for_information_image = models.ImageField(("gallery information resmi"), upload_to="media/images/site/image_for_information/",help_text="420x350 boyutunda resim önerilmektedir.",null=False,blank=False)
    image_for_information_title = models.CharField(max_length=200,verbose_name="Resim Başlığı",null=False,blank=False)
    image_for_information_title_url = models.SlugField(max_length=500,verbose_name="Resim Başlığının Url Adresi",null=False,blank=False)
    image_for_information_description = RichTextField(max_length = 200,verbose_name="Resim Açıklaması")

    def __str__(self):
        return self.image_for_information_name
    def resim(self):
        if self.image_for_information_image:
            return mark_safe(f"<img src={self.image_for_information_image.url} width=100 height=100></img>")
        return mark_safe(f"<h3>{self.image_for_information_name} adlı yazı resime sahip değil</h3>")
    def delete(self, *args, **kwargs):
        self.image_for_information_image.delete()
        super(image_for_information, self).delete(*args, **kwargs)
    class Meta:
        verbose_name='Resim'
        verbose_name_plural='9) Resim'

class experience(models.Model):
    name =  models.CharField(verbose_name="Experience Adı",max_length=200,help_text="Admin sayfasında sizin göreceğiniz isim",)
    effect_number = models.PositiveSmallIntegerField()
    title =  models.CharField(verbose_name="Experience Başlığı",max_length=200)
    
    description =  RichTextField(max_length=300,verbose_name="Açıklama")
    button_name = models.CharField(max_length=200,verbose_name="Buton Adı")
    button_url = models.SlugField(verbose_name="Buton Url")

    first_information_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    first_information_number = models.PositiveSmallIntegerField()
    first_information_description = models.CharField(max_length=30,null=True,blank=True)
    
    second_information_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    second_information_number = models.PositiveSmallIntegerField()
    second_information_description = models.CharField(max_length=30,null=True,blank=True)
    
    third_information_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    third_information_number = models.PositiveSmallIntegerField()
    third_information_description = models.CharField(max_length=30,null=True,blank=True)
    
    fourth_information_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    fourth_information_number = models.PositiveSmallIntegerField()
    fourth_information_description = models.CharField(max_length=30,null=True,blank=True)
    
    foregeinkey = models.ManyToManyField("image_for_information", verbose_name="Resim Seçimi",blank=False)
    
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Gallery Statüsü")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('order',)
        verbose_name='Experience'
        verbose_name_plural='7) Experience'
        
        
        

class get_more_with_us(models.Model):
    name =  models.CharField(verbose_name="Bilgi Adı",max_length=200,help_text="admin sayfasında sizin göreceğiniz isim",)
    title =  models.CharField(verbose_name="Bilgi Başlığı",max_length=200)

    first_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    first_title = models.CharField(max_length=20,verbose_name="Bilgi Başlık")
    first_description = RichTextField(max_length=300,null=True,blank=True)
    first_button_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    first_button_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    first_button2_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    first_button2_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    
    second_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    second_title = models.CharField(max_length=20,verbose_name="Bilgi Başlık")
    second_description = RichTextField(max_length=300,null=True,blank=True)
    second_button_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    second_button_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    second_button2_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    second_button2_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    
    
    third_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    third_title = models.CharField(max_length=20,verbose_name="Bilgi Başlık")
    third_description = RichTextField(max_length=300,null=True,blank=True)
    third_button_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    third_button_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    third_button2_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    third_button2_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    
    
    fourth_name = models.CharField(max_length=200,verbose_name="Bilgi Adı")
    fourth_title = models.CharField(max_length=20,verbose_name="Bilgi Başlık")
    fourth_description = RichTextField(max_length=300,null=True,blank=True)
    fourth_button_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    fourth_button_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)
    fourth_button2_name = models.CharField(max_length=200,verbose_name="Buton Adı",null=True,blank=True)
    fourth_button2_url = models.SlugField(verbose_name="Buton Url",null=True,blank=True)   
    
    image = models.ForeignKey("appearance.image_for_information",related_name="image1", verbose_name=("Resim 1"),help_text="313x580 boyutunda resim önerilmektedir.", on_delete=models.PROTECT,db_constraint=False)
    image_2 = models.ForeignKey("appearance.image_for_information",related_name="image2", verbose_name=("Resim 2"),help_text="313x580 boyutunda resim önerilmektedir.", on_delete=models.PROTECT,db_constraint=False)
    image_3 = models.ForeignKey("appearance.image_for_information",related_name="image3", verbose_name=("Resim 3"),help_text="313x580 boyutunda resim önerilmektedir.", on_delete=models.PROTECT,db_constraint=False)
    image_4 = models.ForeignKey("appearance.image_for_information",related_name="image4", verbose_name=("Resim 4"),help_text="313x580 boyutunda resim önerilmektedir.", on_delete=models.PROTECT,db_constraint=False)

    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Gallery Statüsü")

    def __str__(self):
        return self.name
    def clean(self):
        liste = {}
        if not (self.first_button_name or self.first_button_url):
            pass
        elif not (self.first_button_name):
            liste['first_button_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.') 
        elif not (self.first_button_url):
            liste['first_button_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')

        if not (self.first_button2_name or self.first_button2_url):
            pass
        elif not (self.first_button2_name):
            liste['first_button2_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.')
        elif not (self.first_button2_url):
            liste['first_button2_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')


        if not (self.second_button_name or self.second_button_url):
            pass
        elif not (self.second_button_name):
            liste['second_button_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.') 
        elif not (self.second_button_url):
            liste['second_button_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')

        if not (self.second_button2_name or self.second_button2_url):
            pass
        elif not (self.second_button2_name):
            liste['second_button2_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.')
        elif not (self.second_button2_url):
            liste['second_button2_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')


        if not (self.third_button_name or self.third_button_url):
            pass
        elif not (self.third_button_name):
            liste['third_button_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.') 
        elif not (self.third_button_url):
            liste['third_button_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')

        if not (self.third_button2_name or self.third_button2_url):
            pass
        elif not (self.third_button2_name):
            liste['third_button2_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.')
        elif not (self.third_button2_url):
            liste['third_button2_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')


        if not (self.fourth_button_name or self.fourth_button_url):
            pass
        elif not (self.fourth_button_name):
            liste['fourth_button_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.') 
        elif not (self.fourth_button_url):
            liste['fourth_button_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')

        if not (self.fourth_button2_name or self.fourth_button2_url):
            pass
        elif not (self.fourth_button2_name):
            liste['fourth_button2_name'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.')
        elif not (self.fourth_button2_url):
            liste['fourth_button2_url'] = ValidationError('"Buton Adı" dolu ise "Buton Url" dolu olmalı.')

        
        if liste:
            raise ValidationError(liste)
    
    
    class Meta:
        ordering = ('order',)
        verbose_name='Bilgi'
        verbose_name_plural='8) Bilgi'
        
        



class contactform(models.Model):
    first_name = models.CharField(max_length = 200,verbose_name = "Adınız")
    last_name = models.CharField(max_length = 200,verbose_name = "Soyadınız")
    email = models.EmailField(verbose_name = "Email Adresi")
    phone = PhoneField(verbose_name="Telefon numarası",null=True,blank=True,)
    Company = models.CharField(verbose_name = "Şirket",blank=True,null=True,max_length=300)
    emailorphone = models.CharField(max_length=100,choices=Phoneoremail,verbose_name="İletişim Yolu",)
    message = models.CharField(max_length = 5000,verbose_name = "Mesajınız")
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural='Contact'
        verbose_name = "Contact"


class footer(models.Model):
    menu_name = models.CharField(("Menü Adı"), max_length=200)
    menu_url = models.SlugField(("Menü Url"), max_length=300,unique=True)
    menu_kare = models.BooleanField(("Menü kare Koyma Adı"),default=False)

    menu_status = models.CharField(verbose_name="Menü Statüsü",max_length=100, choices=STATUS)
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  

    def __str__(self):
        return self.menu_name
    class Meta:
        ordering = ('order',)
        verbose_name='footer'
        verbose_name_plural='Footer'
        
        
        
