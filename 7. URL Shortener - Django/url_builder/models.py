from django.db import models
import string

class TinyURL(models.Model):
    url = models.URLField(max_length=200, null=False)
    shortcutCode = models.CharField(max_length=6, null=False, unique=True)
    date = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date of creation of the shorcut")
    username = models.CharField(max_length=20)
    numberAccess = models.IntegerField(default=1)

    def __str__(self):
        return "URL - FROM: " + str(self.url) + " TO: http://127.0.0.1:8000/" + str(self.shortcutCode) + " - (" + str(self.numberAccess) + " access)"