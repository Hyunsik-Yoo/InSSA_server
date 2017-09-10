from django.db import models


class MyScore(models.Model):
    score = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return str(self.score)
