from django.db import models
from django.utils import timezone
# from django.core.urlresolvers import reverse
# Create your models here.

# Fund Raising Memorial Item
class FMItem(models.Model):
    # id = models.IntegerField()
    PLACEMENT_CHOICES = (
        ('N/A', 'N/A'), ('WWI', 'WWI'), ('WWII', 'WWII'), ('Korea', 'Korea'), ('Vietnam', 'Vietnam'),
        ('Gulf War', 'Gulf War'), ('Iraq', 'Iraq'), ('Afghanistan', 'Afghanistan'),
        ('Purple Heart', 'Purple Heart'), ('Women in Service', 'Women in Service'), ('POW/MIA', 'POW/MIA')
    )
    placement = models.CharField(db_column='Placement', max_length=50,
                                 choices=PLACEMENT_CHOICES, default='N/A')
    name = models.CharField(db_column='Name', max_length=50, blank=True)
    LOGO_CHOICES = (
        ('None', 'None'), ('Army', 'Army'), ('Marine Corp', 'Marine Corp'), ('Navy', 'Navy'),
        ('Air Force', 'Air Force'), ('Coast Guard', 'Coast Guard')
    )
    logo = models.CharField(db_column='Logo', max_length=50,
                            choices=LOGO_CHOICES, default='None')
    line1 = models.CharField(db_column='Line1', max_length=50, blank=True)
    line2 = models.CharField(db_column='Line2', max_length=50, blank=True)
    line3 = models.CharField(db_column='Line3', max_length=50, blank=True)
    line4 = models.CharField(db_column='Line4', max_length=50, blank=True)
    line5 = models.CharField(db_column='Line5', max_length=50, blank=True)
    type = models.CharField(db_column='Type', max_length=50, blank=True)
    row = models.CharField(db_column='Row', max_length=50, blank=True)
    col = models.CharField(db_column='Col', max_length=50, blank=True)
    paypal_id = models.CharField(db_column='PayPal_ID', max_length=50, blank=True)
    purchaser = models.CharField(db_column='Purchaser', max_length=50, blank=True)
    email = models.CharField(db_column='Email', max_length=50, blank=True)
    install_date = models.DateTimeField(db_column='Install_Date', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     managed = False
    #     db_table = 'fmitem'
