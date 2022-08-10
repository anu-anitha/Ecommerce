from django.db import models

# from django.contrib.auth.models import AbstractUser
# # Create your models here.
# class User(AbstractUser):
# 	uesrname=None
# 	email=models.EmailField(max_length=50,unique=True)
# 	USERNAME_FIELD='email'


status_choice=(
			('process','In Process'),
			('shipped','shipped'),
			('delivery','delivery')	)





class Category(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    # user = models.ForeignKey(
    #     CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    orderstatus=models.CharField(choices=status_choice,default='process',max_length=150)

    product_names = models.ForeignKey(Product,on_delete=models.CASCADE,max_length=500)
    total_products = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class OrderItem(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    # def __str__(self):
    #     return f"{self.quantity} of {self.item.}" 

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

RATING=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)
class ProductReview(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.IntegerField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.review_rating

        



















