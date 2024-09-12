from datetime import date

from django.db import models


class ShoppingItem(models.Model):
    created_at = models.DateField(
        default=date.today
    )  # hier kann nur ein datum abgespeichert werden
    name = models.CharField(max_length=200)  # damit wird ein textfeld generiert!
    done = models.BooleanField(default=False)  # kann nur booleans speichern
