from django.contrib import admin

# [NGUYEN] 1. Need to create a super user first by using the command "python manage.py createsuperuser" -> fill in username and pass (at least 8 characters)

# [NGUYEN] 2. After create a super user, need to register the app (e.g articles) to admin

from .models import Article # .models means "import "models" file from the same directory (.)"

# Register your models here.
admin.site.register(Article)
