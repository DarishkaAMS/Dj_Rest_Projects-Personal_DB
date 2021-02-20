from django.db import models
from django.contrib.auth import get_user_model

Customer = get_user_model()


class Champagne(models.Model):
    brand = models.CharField(verbose_name='Brand', db_index=True, unique=True, max_length=25)
    color = models.CharField(verbose_name='Color', max_length=25)
    size = models.CharField(verbose_name='Size', max_length=25)
    CHAMP_TYPES = {
        (1, 'Brut'),
        (2, 'Extra Dry'),
        (3, 'Dry'),
        (4, 'Demi-Sec'),
        (5, 'Doux'),
    }
    champ_type = models.IntegerField(verbose_name='Champagne Type', choices=CHAMP_TYPES)
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.CASCADE)