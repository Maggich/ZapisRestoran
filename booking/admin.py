from django.contrib import admin
from .models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "x", "y")
    search_fields = ("number",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "table", "data", "time", "created")
    list_filter = ("data", "table")