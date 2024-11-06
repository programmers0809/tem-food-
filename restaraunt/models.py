from django.db import models
from django.utils import timezone


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nomi')
    image = models.ImageField(upload_to='fast-food/images', verbose_name='Ikonkasi')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Kategoriyalar'
        managed = True
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalaar'
        
        

class ProductsModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='Mahsulot nomi')
    # slug = models.SlugField(unique=True, blank=True)
    body = models.TextField(verbose_name="Mahsulot haqida ma'lumot")
    category = models.ForeignKey(CategoryModel, verbose_name='Kategoriyasi', on_delete=models.CASCADE)
    
    UZ = "so'm"
    RU = '₽'
    ENG = '$'

    the_price = (
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="so'm")
    price = models.IntegerField()
    image = models.ImageField(verbose_name='Rasmi')
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='Nashr qilingan vaqt')
    manager = models.Manager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Produktlar'
        verbose_name_plural = 'Produktlar'
        managed = True



class OpeningHours(models.Model):
    day_of_week = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.day_of_week}: {self.opening_time} - {self.closing_time}"

    class Meta:
        verbose_name = "Opening Hour"
        verbose_name_plural = "Opening Hours"
    
