from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to='category',blank=True,null=True)
    parent=models.ForeignKey('self',related_name='childrem',on_delete=models.CASCADE,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering =['-created']
        verbose_name_plural='Categories'


class Product(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    preview_des=models.CharField(max_length=250,verbose_name='short Descriptions')
    description=models.TextField(max_length=1000,verbose_name='Descriptions')
    image=models.ImageField(upload_to='product/',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    old_price=models.DecimalField(max_digits=10,decimal_places=2, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    class Meta:
        ordering=['-created']
