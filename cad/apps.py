from django.apps import AppConfig


class CadConfig(AppConfig):
    name = 'cad'

    from django.contrib import admin
    from .models import Supplier
    from .models import Client
    admin.site.register(Supplier)
    admin.site.register(Client)
