from typing import Tuple

from django.core.validators import RegexValidator, URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from . import REGEX_VALIDATOR_MSG
from .manager import UrlManager


class Url(TimeStampedModel):
    '''
    Url model

    shortcode -> str pk 
    url -> str 
    redirect_count -> int:  amount of redirect calls
    last_redirect -> datetime: last redirect timestamp

    created -> datetime
    modified -> datetime
    '''

    shortcode = models.CharField(
        _('shorcode'),
        primary_key=True,
        max_length=6,
        help_text=_('url shortname'),
        validators=[
            RegexValidator(
                regex=r'^[a-z0-9_]{6}',
                message=_(REGEX_VALIDATOR_MSG),
                code='invalid shortcode',
            ),
        ],
    )
    url = models.CharField(
        _('url'),
        max_length=256,
        validators=[URLValidator()]
    )
    _redirect_count = models.IntegerField(
        default=0, 
        help_text=_('Number of times shortcode has been retreived'))
    last_redirect = MonitorField(monitor='redirect_count')

    objects = UrlManager()

    @property
    def redirect_count(self) -> int:
        return self._redirect_count

    def increment_redirect_count(self) -> None:
        """
        increment redirect count by one.
        :return :type Url
        """
        self._redirect_count+=1
        self.save()

    class Meta:
        ordering: Tuple[str] = ('created', 'modified')

    def __str__(self) -> str:
        return self.url
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({self.__str__()!r})>'
 