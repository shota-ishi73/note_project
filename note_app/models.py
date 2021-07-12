from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.
class Note(models.Model):
  user_id = models.ForeignKey(
    User, on_delete=models.RESTRICT
  )
  title = models.CharField('タイトル',max_length=200)
  text = models.TextField('本文')
  category = models.CharField('分類',max_length=200)
  create_at = models.DateTimeField(default=timezone.now)
  update_at = models.DateTimeField(default=timezone.now)