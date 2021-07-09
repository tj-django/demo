import django
from django.db import models
from django.utils.translation import gettext_lazy as _


class TestModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500)
    dob = models.DateTimeField(blank=True, null=True)
    age = models.PositiveIntegerField(default=500)

    if django.VERSION < (2, 1):
        active = models.NullBooleanField()
    else:
        active = models.BooleanField(null=True)
        
    

    class Meta:
        verbose_name = _("test model")
        verbose_name_plural = _("test models")

    def __str__(self):
        return str(_(self.name))

    __repr__ = __str__
