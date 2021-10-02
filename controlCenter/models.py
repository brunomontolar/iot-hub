from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator

class Devices(models.Model):
    device = models.CharField(max_length=30)
    startup_date = models.DateTimeField()
    heartbeat = models.DateTimeField(auto_now_add=True)

class Actions(models.Model):
    INPUT_TYPES = (
        ('S', 'Switch'),
        ('B', 'Button'),
        ('R', 'Range'),
    )
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    input_name = models.CharField(max_length=30)
    input_value = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(255)])
    input_type = models.CharField(max_length=1, choices=INPUT_TYPES)
# Create your models here.
    def __str__(self):
        return "%s %s" % (self.device, self.input_name)