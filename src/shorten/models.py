from typing import Tuple

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

# Create your models here.
class Url(TimeStampedModel):
    url = models.CharField(primary_key=True, max_length=256)
    shortcode = models.CharField(unique=True, max_length=6)
    redirect_count = models.IntegerField(default=0)
    last_redirect = MonitorField(monitor='redirect_count')

    objects = models.Manager()

    class Meta:
        ordering: Tuple[str] = ('created', 'modified')

    def __str__(self) -> str:
        return self.url
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.__str__()!r})>'
 