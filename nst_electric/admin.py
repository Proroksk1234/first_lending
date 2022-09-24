from .models import Review, DraftService, CleanService, LegalService, Navigate

from django.contrib import admin
# Register your models here.

class Base:
    list_per_page = 10
    search_fields = ['service']


@admin.register(Review)
class Review(admin.ModelAdmin):
    pass


@admin.register(DraftService)
class DraftService(Base, admin.ModelAdmin):

    pass


@admin.register(CleanService)
class CleanService(Base, admin.ModelAdmin):
    pass


@admin.register(LegalService)
class LegalService(Base, admin.ModelAdmin):
    pass


@admin.register(Navigate)
class Navigate(admin.ModelAdmin):
    pass