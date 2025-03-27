from django.contrib import admin

from lesson_5.models import Flower, Bouquet, Client

admin.site.register(Bouquet)
admin.site.register(Client)
admin.site.register(Flower)
