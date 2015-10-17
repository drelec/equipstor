from django.db import models

# Create your models here.


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    vendor_site = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.vendor_name


class PrinterType(models.Model):
    print_type = models.CharField(max_length=20)

    def __str__(self):
        return self.print_type


class ColorType(models.Model):
    color_type = models.CharField(max_length=20, verbose_name='color')

    def __str__(self):
        return self.color_type


class Cartridge(models.Model):
    cartridge_name = models.CharField(max_length=20)
    color_type = models.ForeignKey(ColorType, verbose_name='color')
    max_number_prints = models.IntegerField(default=0)
    package = models.IntegerField(default=1)
    barcode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.cartridge_name

    def printers_list(self):
        return ', '.join([printer.model_name for printer in Cartridge.objects.get(id=self.id).printermodel_set.all()])


class Connectivity(models.Model):
    type_connectivity = models.CharField(max_length=10)

    def __str__(self):
        return self.type_connectivity


class MaxPaperSize(models.Model):
    max_paper_size = models.CharField(max_length=10)

    def __str__(self):
        return self.max_paper_size


class PrinterModel(models.Model):
    vendor_name = models.ForeignKey(Vendor)
    model_name = models.CharField(max_length=50)
    product_number = models.CharField(max_length=20)
    print_type = models.ForeignKey(PrinterType, verbose_name='Type of print')
    model_site = models.CharField(max_length=200, blank=True)
    driver_url = models.CharField(max_length=250, blank=True)
    max_print_resolution_dpi = models.IntegerField(default=0)
    memory_size = models.IntegerField(default=0)
    max_monthly_load = models.IntegerField(default=0)
    cartridges = models.ManyToManyField(Cartridge, blank=True)
    duplex_mode = models.BooleanField()
    print_speed_ppm = models.IntegerField(default=0)
    connectivity = models.ManyToManyField(Connectivity)
    max_paper_size = models.ForeignKey(MaxPaperSize)

    def __str__(self):
        return self.model_name

    def cartridges_list(self):
        return ', '.join([cartridge.cartridge_name for cartridge in self.cartridges.all()])
    cartridges_list.short_description = 'cartridges'
    cartridges_list.allow_tags = True
