from django.db import models

class Aftosalon(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.context} - {self.created_ed} - {self.updated_ed} - {self.is_bool}"

class Car(models.Model):
    modeli = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    ot_kuchi = models.IntegerField()
    narxi = models.IntegerField()
    chiqarilgan_yili = models.IntegerField()

    def __str__(self):
        return f"{self.modeli} - {self.context} - {self.ot_kuchi} ot kuchi - {self.narxi} so‘m - {self.chiqarilgan_yili}"
