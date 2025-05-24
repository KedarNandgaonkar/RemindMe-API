from django.db import models

# Create your models here.
class Reminder(models.Model):
    Remind_Type_choice=[
        ('email','Email'),
        ('sms','SMS'),
    ]
    date=models.DateField()
    time=models.TimeField()
    message=models.TextField()
    remind_type=models.CharField(max_length=10,choices=Remind_Type_choice)
    