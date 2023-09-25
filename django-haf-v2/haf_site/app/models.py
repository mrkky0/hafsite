from django.db import models
# from django.utils.translation import gettext as _

Category_name = (
    ("All", "all"),
    ("Other Category 1", "other-category-1"),
    ("Other Category 2", "other-category-2"),
    ("Other Category 3", "other-category-3"),
    ("Other Category 4", "other-category-4"),
    ("Other Category 5", "other-category-5"),
    ("Other Category 6", "other-category-6"),
)


class Products(models.Model):
    product_name = models.CharField(('Product name'), max_length=40, db_index=True)
    product_id = models.IntegerField(('Product ID'), db_index=True )
    product_des1 = models.CharField(('Product Descriptions 1'), max_length=40, db_index=True,null=True)
    
    product_category = models.CharField(max_length=30,choices=Category_name,default='All')
    default_tag = models.CharField(max_length=10,default='all_tag',editable=False)
     
    product_url = models.URLField(null=True,max_length=200,db_index=True,blank=True,default="https://i.hizliresim.com/b70cygu.jpg")
    

    
    
    created_time = models.DateTimeField(verbose_name=('creation On'), db_index=True)
    updated_time = models.DateTimeField(verbose_name=('modified On'), auto_now=True)
     

        
        

    def __str__(self):
        return self.product_name  # Kullanıcının ismini temsil eder


    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('Product')
        
        
class Category(models.Model):
    product_category = models.CharField(max_length=30,choices=Category_name,default='All')
 

    def __str__(self):
        return self.product_category  # Kullanıcının ismini temsil eder


    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('Category')