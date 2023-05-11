from django.db import models

class Raspisanie(models.Model):
    title = models.CharField('Название', max_length=50)
    time = models.DateTimeField('Время', )
    zaniatia = models.TextField('Занятия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
