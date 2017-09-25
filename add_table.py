
from __future__ import unicode_literals

from django.db import models


class FrmItem(models.Model):
    id = models.IntegerField()
    placement = models.CharField(db_column='Placement', max_length=50, blank=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True)
    logo = models.CharField(db_column='Logo', max_length=50, blank=True)
    line1 = models.CharField(db_column='Line1', max_length=50, blank=True)
    line2 = models.CharField(db_column='Line2', max_length=50, blank=True)
    line3 = models.CharField(db_column='Line3', max_length=50, blank=True)
    line4 = models.CharField(db_column='Line4', max_length=50, blank=True)
    line5 = models.CharField(db_column='Line5', max_length=50, blank=True)
    paver = models.CharField(db_column='Paver', max_length=50, blank=True)
    row = models.CharField(db_column='Row', max_length=50, blank=True)
    col = models.CharField(db_column='Col', max_length=50, blank=True)
    paypal_id = models.CharField(db_column='PayPal_ID', max_length=50, blank=True)
    purchaser = models.CharField(db_column='Purchaser', max_length=50, blank=True)
    email = models.CharField(db_column='Email', max_length=50, blank=True)
    install_date = models.DateTimeField(db_column='Install_Date', blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fmitem'
