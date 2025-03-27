from django.contrib import admin

from lesson_8.models import GameModel, GamerLibraryModel, GamerModel

admin.site.register(GameModel)
admin.site.register(GamerLibraryModel)
admin.site.register(GamerModel)
