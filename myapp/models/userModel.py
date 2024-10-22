from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto increment
    email = models.EmailField(max_length=254, blank=False, default='')
    name = models.CharField(max_length=100, blank=False, default='')

    class Meta:
        db_table = 'user' 
