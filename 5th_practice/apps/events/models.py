from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=50)
    num_pizzazip = models.IntegerField()
    created = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.country, self.num_pizzazip)

class Pizzazip(models.Model):
    location = models.ForeignKey(Location)
    rating = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.location)
