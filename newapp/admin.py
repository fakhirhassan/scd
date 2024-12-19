# newapp/admin.py

from django.contrib import admin
from .models import Team
admin.site.register(Team)

# newapp/admin.py
from .models import Game
admin.site.register(Game)
