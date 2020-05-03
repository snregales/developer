from typing import Tuple

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from .manager import UrlManager
# from .utils import validate_shortcode


class Url(TimeStampedModel):
    url = models.CharField(
        _('url'),
        primary_key=True, 
        max_length=256
    )
    shortcode = models.CharField(
        _('shorcode'),
        unique=True,
        max_length=6,
        help_text=_('url shortname'),
        validators=[
            RegexValidator(
                regex=r'^[a-z0-9_]{6}',
                message=_('shortcode must be lowercase alpha numeric charater; underscore is allowed.'),
                code='invalid shortcode',
            ),
        ],
    )
    _redirect_count = models.IntegerField(
        default=0, 
        help_text=_('Number of times shortcode has been retreived'))
    last_redirect = MonitorField(monitor='redirect_count')

    objects = UrlManager()

    @property
    def redirect_count(self) -> int:
        return self._redirect_count

    def increment_redirect_count(self) -> 'Url':
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
 