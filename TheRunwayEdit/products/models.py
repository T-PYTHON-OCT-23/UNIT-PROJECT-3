from django.db import models

class Product(models.Model):
    quantities=models.TextChoices('quantities',['1','2','3','4','5'])
    sizes=models.TextChoices('sizes',['XS','S','M','L','XL','XXL'])
    categories=models.TextChoices('categories',['Abayas','Dresses','Hoodies&Sweatshirts','Jackets&Coats','Jeans','Tshirts&Vests'])
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.CharField(max_length=200,choices=quantities.choices,default=1)
    brand=models.CharField(max_length=200)
    category=models.CharField(max_length=200,choices=categories.choices)
    size=models.CharField(max_length=200,choices=sizes.choices,blank=True)
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return f'{self.name}'




# Create your models here.
