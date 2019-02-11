from django.db import models

# Create your models here.

class Item(models.Model):
    
    Record_ID = models.IntegerField()
    Record_Type = models.CharField(max_length=200, blank=False)
    Campaign_ID = models.IntegerField()
    Campaign = models.CharField(max_length=200, blank=False)
    Budget = models.DecimalField(max_digits=30, decimal_places=2)
    Portofolio_ID = models.IntegerField()
    Campaign_Start_Date = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return 'Record_ID: {0} Record_Type: {1}'.format(self.Record_ID, self.Record_Type)

class HSC(Item):
    pass

class PPC(Item):
    pass

class Bidopt(Item):
    pass


# class Desktops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Laptops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Mobiles(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
