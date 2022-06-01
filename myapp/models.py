from django.db import models

# Create your models here.
class Person(models.Model):
    personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    carid = models.IntegerField(db_column='CarID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    empAuth_objects=models.Manager()
    class Meta:
        managed = False
        db_table = 'person'








class Cars(models.Model):
    carid = models.IntegerField(db_column='CarID', primary_key=True)  # Field name made lowercase.
    model = models.CharField(max_length=20, blank=True, null=True)
    manufacturer = models.CharField(max_length=20, blank=True, null=True)
    model_year = models.CharField(max_length=20, blank=True, null=True)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)
    engine_size = models.IntegerField(blank=True, null=True)
    body_type = models.CharField(max_length=20, blank=True, null=True)
    transmission = models.CharField(max_length=20, blank=True, null=True)
    car_img=models.ImageField(null=False,upload_to="images/")
    mileage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    
    class Meta:
        managed = False
        db_table = 'cars'