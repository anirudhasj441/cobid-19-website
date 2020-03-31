from django.db import models
from django.utils import timezone
# Create your models here.

class Updates(models.Model):
  active = models.CharField(max_length=30,null=True,blank=True)
  recover = models.CharField(max_length=30,null=True,blank=True)
  death = models.CharField(max_length=30,null=True,blank=True)
  def __str__(self):
    return str(self.pk)
  class Meta:
    verbose_name_plural = 'Updates'

class Sypmtoms(models.Model):
  sym = models.CharField(max_length=30)
  img = models.ImageField(upload_to='app/images',null=True)
  def __str__(self):
    return str(self.pk)
  class Meta:
    verbose_name_plural = 'Sypmtoms'
    verbose_name = 'Symptom'



class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField()
    contact = models.CharField(max_length=30,null=True)
    message = models.TextField(max_length=3000,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Messages"
        verbose_name = "Message"