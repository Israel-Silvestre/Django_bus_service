from django.db import models
import uuid

class Bus(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    null=False,
    blank=True)
  description = models.CharField(
    max_length=200,
    null=False,
    blank=False)
  number_of_seats = models.IntegerField(
    null=False,
    blank=False,
    default=50)
  departure_date = models.DateField(
    null=False,
    blank=False
  )
  return_date = models.DateField(
    null=False,
    blank=False
  )
