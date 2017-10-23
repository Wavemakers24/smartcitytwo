from django.contrib import admin
from website.models import UserProfile
from website.models import NewUser
from website.models import Post

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(NewUser)
admin.site.register(Post)