from django.db import models


class Product_category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sub_Product_category1(models.Model):
    name = models.CharField(max_length=255)
    product_category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sub_Product_category2(models.Model):
    name = models.CharField(max_length=255)
    sub_product_category1 = models.ForeignKey(Sub_Product_category1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sub_Product_category3(models.Model):
    name = models.CharField(max_length=255)
    sub_product_category2 = models.ForeignKey(Sub_Product_category2, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product_inventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quantity


class Discount(models.Model):
    name = models.CharField(max_length=255)
    discount_percent = models.IntegerField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    sku = models.CharField(max_length=20)
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    sub_category1 = models.ForeignKey(Sub_Product_category1, on_delete=models.CASCADE)
    sub_category2 = models.ForeignKey(Sub_Product_category2, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Product_inventory, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Payment_details(models.Model):
    order = models.IntegerField()
    amount = models.FloatField()
    provider = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order


class User_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    telephone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.user


class User_payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    account_no = models.IntegerField()
    expiry = models.DateField()

    def __str__(self):
        return f"{self.user} {self.payment_type} {self.provider} {self.account_no}"



class Order_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    payment = models.ForeignKey(Payment_details, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Order_items(models.Model):
    order = models.ForeignKey(Order_details, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order


class Shopping_session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Cart_item(models.Model):
    session = models.ForeignKey(Shopping_session, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session


