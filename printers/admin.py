from django.contrib import admin
from printers.models import Printer

# Register your models here.


class PrintersList(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'page_counter', 'description')
    list_filter = ['id', 'create_date','model_name','description']
    search_fields = ['model_name']


admin.site.register(Printer, PrintersList)
