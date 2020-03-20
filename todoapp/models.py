from django.db import models
from django.conf import settings


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    text = models.CharField(max_length=128, null=False, help_text="This field is required.",)
    added_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
