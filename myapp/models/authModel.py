from django.db import models

ROLE_CHOICES = [
    ('user', 'User'),
    ('admin', 'Admin'),
    ('staff', 'Staff'),
]

class AuthModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, blank=False)
    full_name = models.TextField(blank=False) 
    password = models.TextField(blank=False) 
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='user') 

    class Meta:
        db_table = 'app_user'
    def __str__(self):
        return f"User(email={self.email}, full_name={self.full_name}, role={self.role})"
    
    def toDTO(self):
        return {
            'email': self.email,
            'fullName': self.full_name,
            'role': self.role,
        }