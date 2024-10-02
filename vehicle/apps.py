from django.apps import AppConfig

'''
class VehicleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicle'
'''

class DemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicle'

class VehicleConfig(AppConfig):
    name = 'vehicle'
