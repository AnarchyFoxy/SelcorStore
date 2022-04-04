from django.db import models
from django.urls import reverse

# Models for shop
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    #category - foregin key for Category relation one to many
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #product name
    name = models.CharField(max_length=200, db_index=True)
    #slug for product, to create sophisticated url adress
    slug = models.SlugField(max_length=200, db_index=True)
    #product image
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    #product description
    description = models.TextField(blank=True)
    #product price - decimal type
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #produc availability
    available = models.BooleanField(default=True)
    #product creation
    created = models.DateTimeField(auto_now_add=True)
    #Product upgrade
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
