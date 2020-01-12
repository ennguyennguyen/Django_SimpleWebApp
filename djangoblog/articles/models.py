from django.db import models

# [NGUYEN] 1. mode represent a class in Django

# [NGUYEN] 2. when you complete a model, need to migrate the model to a database tables

# [NGUYEN] 3. need to migrate all defaults models of Django first by running "python manage.py migrate" in cmd

# [NGUYEN] 4. After we have migrated all defaults models of Django, need to create a migrate file for our own models by running "python manage.py makemigrations"
#               ==> Django will create a migration file in "migrations" folder. Name e.g: 0001_initial.py
#               ==> Then run the command "python manage.py migrate" again to migrate new migrations

# [NGUYEN] 5: IN GENERAL, whenever you have some changes to model, need to run the below commands again to migrate the models:
#               5.1) python manage.py makemigrations
#               5.2) python manage.py migrate

# Create your models here.
class Article(models.Model): # [NGUYEN] models.Model is the parent class that Article inherits from
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    # [NGUYEN] create a function to print out the article title in database (this is a BUILT IN FUNCTION)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...' # take the first 50 characters of the body