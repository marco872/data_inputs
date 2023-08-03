from django.db import models
from django.contrib.auth.models import AbstractUser






# Create your models here.
class LoftRentals(models.Model):
    STATUS_CHOICES = (
        ('occupied', 'Occupied'),
        ('free', 'Free'),
    )

    rent_value_euro = models.DecimalField(max_digits=10, decimal_places=2)
    present_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    rental_period_from = models.DateField(null=True, blank=True)
    rental_period_to = models.DateField(null=True, blank=True)
    loft_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Loft Rental - Loft Number: {self.loft_number}, Status: {self.present_status}, Rent: {self.rent_value_euro} Euro"




class TemporaryStandRental(models.Model):
    STATUS_CHOICES = (
        ('occupied', 'Occupied'),
        ('free', 'Free'),
    )

    rent_day_value_yi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Rent Value in Euro for Yi Number")
    present_status_yi = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Present Status for Yi Number")
    rental_period_from_yi = models.DateField(null=True, blank=True, verbose_name="Rental Period From for Yi Number")
    rental_period_to_yi = models.DateField(null=True, blank=True, verbose_name="Rental Period To for Yi Number")

    rent_day_value_yang = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Rent Value in Euro for Yang Number")
    present_status_yang = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Present Status for Yang Number")
    rental_period_from_yang = models.DateField(null=True, blank=True, verbose_name="Rental Period From for Yang Number")
    rental_period_to_yang = models.DateField(null=True, blank=True, verbose_name="Rental Period To for Yang Number")

    temporary_stand_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Temporary Stand Rental - Stand Number: {self.temporary_stand_number}, Yi Status: {self.present_status_yi}, Yang Status: {self.present_status_yang}"



class CoMinimizing(models.Model):
    item_image = models.ImageField(upload_to='cominimizing/', null=True, blank=True)
    item_name = models.CharField(max_length=100)
    item_number = models.PositiveIntegerField()
    item_shelf_number_in_storage = models.CharField(max_length=50)

    def __str__(self):
        return f"Co-Minimizing Item - {self.item_name}, Item Number: {self.item_number}, Shelf Number: {self.item_shelf_number_in_storage}"




class MaintenanceAndHousekeeping(models.Model):
    ITEM_CHOICES = (
        ('kitchen_plumbing', 'Kitchen Plumbing'),
        ('bathroom_plumbing', 'Bathroom Plumbing'),
        ('panelling_system', 'Panelling System'),
        ('video_system', 'Video System'),
        ('audio_system', 'Audio System'),
        ('ventilation_system', 'Ventilation System'),
        ('bed_system', 'Bed System'),
        ('ventilation_system', 'Ventilation System'),
        ('others', 'Others'),
    )

    loft_number = models.PositiveIntegerField()
    item_to_be_repaired = models.CharField(max_length=50, choices=ITEM_CHOICES)

    def __str__(self):
        return f"Maintenance and Housekeeping - Loft Number: {self.loft_number}, Item to be Repaired: {self.item_to_be_repaired}"



class ConnectedAppliance(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LoftFeature(models.Model):
    LOFT_FEATURE_CHOICES = (
        ('lighting', 'Lighting'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('ventilation_ac', 'Ventilation/AC'),
        ('bed_up_down', 'Bed Up and Down'),
        ('panel1_open_close_fold', 'Panel 1 - Open/Close/Fold'),
        ('panel2_open_close_fold', 'Panel 2 - Open/Close/Fold'),
        ('entrance_door_security', 'Entrance Door Security'),
        ('silent_sound_system', 'Silent Sound System'),
    )

    feature = models.CharField(max_length=30, choices=LOFT_FEATURE_CHOICES)
    connected_appliance = models.ForeignKey(ConnectedAppliance, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Loft Feature - {self.feature} (Connected Appliance: {self.connected_appliance})"




# ... (other model classes)

class UserProfile(models.Model):
    # Define your user profile fields here
    pass

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    # For example, you can add first_name, last_name, and email
    pass



