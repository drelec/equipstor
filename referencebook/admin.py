from django.contrib import admin

from .models import PrinterModel
from .models import PrinterType
from .models import ColorType
from .models import Vendor
from .models import MaxPaperSize
from .models import Cartridge
from .models import Connectivity

# Register your models here.


class ModelList(admin.ModelAdmin):
    list_display = ('model_name', 'product_number', 'cartridges_list', 'print_type', 'max_monthly_load',
                    'max_paper_size', 'duplex_mode')
    list_editable = ('product_number', 'print_type', 'max_monthly_load', 'max_paper_size', 'duplex_mode')


class CartridgeList(admin.ModelAdmin):
    list_display = ('cartridge_name', 'color_type', 'max_number_prints', 'package', 'printers_list')
    list_editable = ('color_type', 'max_number_prints', 'package')

admin.site.register(PrinterModel, ModelList)
admin.site.register(PrinterType)
admin.site.register(ColorType)
admin.site.register(Vendor)
admin.site.register(MaxPaperSize)
admin.site.register(Cartridge, CartridgeList)
admin.site.register(Connectivity)
