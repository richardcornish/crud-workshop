from django.db import models
from django.urls import reverse


class Poll(models.Model):
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("poll_detail", kwargs={
            "pk": str(self.pk),
        })
