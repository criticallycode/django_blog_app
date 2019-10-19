from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# the models file controls the model used for the SQL database

# every class is its own table in the database
# while every attribute of the class will be its own field in the table

class Post(models.Model):
    # models.charfield specifies the field takes character inputs
    title = models.CharField(max_length=120)
    # a textfield is unrestricted text
    content = models.TextField()
    # the function is not being called now, called when created, so don't execute with paren
    date_posted = models.DateTimeField(default=timezone.now)
    # foreign key is a key that references the value of attribute at a different row in another table
    # or same table
    # the models.foreignkey takes the other table as the parameter
    # on delete controls logic for handling how the posts should be addressed if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title

    # when using class create view, django needs to know how to find absolute url
    # create this method
    def get_absolute_url(self):
        # url's primary key value is the primary kry of that specific post
        return reverse('post-detail', kwargs={'pk': self.pk})