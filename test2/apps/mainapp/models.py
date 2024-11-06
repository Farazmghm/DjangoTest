from django.db import models
from django.utils import timezone

class Faraz(models.Model):
   
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    age=models.IntegerField(default=20)
    is_active=models.BooleanField(default=True)
    email=models.EmailField(default=False)
    register=models.DateTimeField(default=timezone.now)
    image_name=models.CharField(max_length=200,default='nophoto.jpg',null=True,blank=True)
    
   

    def __str__(self):
       return f"{self.name}\t{self.family}\t{self.age}\t{self.email}"
   
   
class Company(models.Model):
    member_id=models.IntegerField(primary_key=True)
    cheif=models.CharField(max_length=100,default='faraz')
    member=models.CharField(max_length=100)
    product=models.CharField(max_length=200)
   
    



    
    
    
class Product_company(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=200)
    production_date=models.DateField(max_length=100,null=True)
    produst_price=models.CharField(max_length=100)
    PRODUCT_STATUS=[
        
                ('sales', 'Sales'),
                 ('normal', 'Normal')
                  ]
      

    status=models.CharField(max_length=100,choices=PRODUCT_STATUS)
    company=models.ForeignKey(Company,null=True,on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, related_name="product_companies")
    
    
class Emplyee(models.Model):
    employee_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=200,null=True)
    number=models.IntegerField()
    is_active=models.BooleanField()
    slug=models.SlugField(max_length=100)
    company=models.ForeignKey(Company,null=True,on_delete=models.CASCADE)
    emplyee=models.ManyToManyField(Company, related_name="employee_companies")
    
    
    
class Post(models.Model):
     name=models.CharField(max_length=100)
     family=models.CharField(max_length=100)
     age=models.IntegerField()
     is_active=models.BooleanField()
     
     def __str__(self):
         return f"{self.name}\t\t\{self.family}\t\t{self.age}"
     