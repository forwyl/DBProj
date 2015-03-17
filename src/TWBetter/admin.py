from django.contrib import admin
from TWBetter.models import UserProfile, Producer, GFood, Favorite, Comment

# Register your models here.
admin.site.register(Producer)
admin.site.register(GFood)
admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(Comment)