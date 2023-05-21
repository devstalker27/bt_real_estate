from django.contrib import admin

from .models import Realtor
# Register your models here.
class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name', 'email')
    list_editable = ('is_mvp',)
    list_filter = ('hire_date',)


admin.site.register(Realtor, RealtorsAdmin)