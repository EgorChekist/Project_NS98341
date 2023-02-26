from django.db import models
from django.contrib.auth.models import User


class TODO(models.Model):
    text = models.TextField("Задачи")
    priority = models.PositiveIntegerField("Приоритет")
    stick = models.BooleanField("КНОПКА", default=False)
    check_table = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["-priority"]
