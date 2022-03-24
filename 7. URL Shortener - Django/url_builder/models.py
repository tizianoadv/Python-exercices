from django.db import models

class TinyURL(models.Model):
    initUrl = models.URLField(max_length=200, null=False, unique=True)
    shortcutCode = models.CharField(max_length=6, unique=True)
    date = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date of creation of the shorcut")
    username = models.CharField(max_length=20)
    numberAccess = models.IntegerField(default=0)

    def __str__(self):
        return self.initUrl + " to " + self.shortcutCode + " (" + self.numberAccess + " access)"