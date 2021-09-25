from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from core import models


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'phone_number',
        'outlets_list'
    ]
    search_fields = [
        'id',
        'name',
        'phone_number'
    ]

    def outlets_list(self, worker: models.Worker):
        outlet_links = []
        for outlet in worker.outlets.all():
            outlet_links.append(f"<a href='{reverse('admin:core_outlet_change', args=[outlet.id])}'>{outlet.name}</a>")
        return format_html('<br/>'.join(outlet_links))

    outlets_list.short_description = "Outlets"


@admin.register(models.Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'worker',
        'visits_count'
    ]
    search_fields = [
        'id',
        'name'
    ]
    list_filter = [
        'worker'
    ]
    autocomplete_fields = [
        'worker',
    ]

    def visits_count(self, outlet: models.Outlet):
        return outlet.visits.count()

    visits_count.short_description = "Visits count"


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'worker',
        'outlet',
        'coordinates',
        'date'
    ]
    list_filter = [
        'outlet__worker',
        'outlet',
    ]

    def worker(self, visit: models.Visit):
        return visit.outlet.worker.first_name

    worker.short_description = "Worker"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
