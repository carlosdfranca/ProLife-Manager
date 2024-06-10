from django.db import models
from django.contrib.auth.models import User

important_choices = [
    (1, "Urgente"),
    (2, "Alta"),
    (3, "Média"),
    (4, "Baixa")
]

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    date_completed = models.DateField(null=True, blank=True)
    important = models.IntegerField(choices=important_choices, null=True, blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title