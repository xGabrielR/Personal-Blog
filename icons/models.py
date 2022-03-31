from django.db import models

class Icon(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Ícones'

    def __str__(self):
        return self.name
