from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    # class Meta:
    #     verbose_name_plural = 'entries'

    def __str__(self):
        length = len(self.name)
        return self.name if length < 50 else self.name[:50] + '...'
