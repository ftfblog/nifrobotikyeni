from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
STATUS = (
        ('Published', 'Yayınla'),
        ('Draft', 'Taslak'),
    )


class teampage(models.Model):
    Name = models.CharField(max_length = 200,verbose_name = "Adınız")
    image = models.ImageField(("Takım Arkadaşının Resmi"), upload_to="media/images/site/team/",help_text="420x424 boyutunda resim önerilmektedir.",null=True,blank=True)
    description = models.CharField(max_length = 200,verbose_name = "Görevi")
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Gallery Statüsü")

    def __str__(self):
        return self.Name
    class Meta:
        ordering = ('order',)
        verbose_name='team'
        verbose_name_plural='team'
        
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(teampage, self).delete(*args, **kwargs)
        
        

class sponsorpage(models.Model):
    name = models.CharField(max_length = 200,verbose_name = "Adınız")
    image = models.ImageField(("Sponsor Resmi"), upload_to="media/images/site/sponsor/",help_text="420x424 boyutunda resim önerilmektedir.",null=True,blank=True)
    description = RichTextField(max_length = 200,verbose_name = "Görevi")
    
    url_name = models.CharField(verbose_name="Sponsor Url Adı",null=True,blank=True,max_length=200)
    url_adres = models.URLField(verbose_name="Sponsor Url adresi",null=True,blank=True)
    
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Gallery Statüsü")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('order',)
        verbose_name='sponsor'
        verbose_name_plural='sponsor'
    def clean(self):
        liste = {}
        if self.url_name == None:
            if self.url_adres !=None:
                liste['url_adres'] = ValidationError('"Url" dolu ise "Ad" dolu olmalı.')
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(teampage, self).delete(*args, **kwargs)
        
        

class projectpage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/images/site/project/")
    description = RichTextField()
    içerik = RichTextUploadingField(config_name="all",)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=True)
    order = models.IntegerField(editable=True,default=1,blank=False,null=False,verbose_name="Sıra")  
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Statüsü")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering = ('order',)
        verbose_name='Projeler'
        verbose_name_plural='Projeler'
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(projectpage, self).delete(*args, **kwargs)
        
        
        
      
class page(models.Model):
    title = models.CharField(max_length=400)
    içerik = RichTextUploadingField(config_name="all",)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=True)
    status = models.CharField(max_length=100,choices=STATUS,verbose_name="Statüsü")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name='Sayfalar'
        verbose_name_plural='Sayfalar'

        
        
        
      