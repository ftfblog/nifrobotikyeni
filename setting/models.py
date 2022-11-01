from django.db import models
from phone_field import PhoneField
from django.core.exceptions import ValidationError

class site(models.Model):
    sitename = models.CharField(verbose_name="site adı",max_length=256)
    siteslogan = models.CharField(verbose_name="site sloganı",max_length=256)
    site_favicon = models.ImageField(("favicon"), upload_to="media/images/site/favicon/")
    site_logo = models.ImageField(("Logo"), upload_to="media/images/site/logo/")

    site_email = models.EmailField(verbose_name="email adresi",null=True,blank=True)
    site_phone = PhoneField(verbose_name="telefon numarası",null=True,blank=True)
    site_adres = models.CharField(verbose_name="Okul Adresi",max_length=400,null=True,blank=True)
    site_adres_url = models.URLField(verbose_name="Okul Adresi Url",null=True,blank=True)
    
    facebook_url = models.URLField(verbose_name="facebook Url",null=True,blank=True)
    twitter_url = models.URLField(verbose_name="twitter Url",null=True,blank=True)
    instgram_url = models.URLField(verbose_name="instgram adresi",null=True,blank=True)

    copyright = models.CharField(verbose_name="copyright",max_length=400,null=True,blank=True)

    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    class Meta:
        ordering = ('order',)
    def __str__(self):
        return "site ayarları"
    def delete(self, *args, **kwargs):
        self.site_favicon.delete()
        self.site_logo.delete()
        super(site, self).delete(*args, **kwargs)
    def clean(self):
        liste = {}
        if self.site_adres == None:
            if self.site_adres_url !=None:
                print(self.site_adres_url)
                liste['site_adres_url'] = ValidationError('"Buton Url" dolu ise "Buton Adı" dolu olmalı.') 
        else:
            pass
        if liste:
            raise ValidationError(liste)