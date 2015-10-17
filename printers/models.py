from django.db import models
from referencebook.models import PrinterModel

# Create your models here.


class Printer(models.Model):
    model_name = models.ForeignKey(PrinterModel)
    page_counter = models.IntegerField(default=0, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    description = models.CharField(default='', blank=True, max_length=250)
    barcode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        pm = PrinterModel.objects.get(id=self.model_name.id)
        return pm.model_name
