from django.contrib import admin

from learning_logs.models import Topic, Entry
from pizzeria.models import Pizza, Topping

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizza)
admin.site.register(Topping)
