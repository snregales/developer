from django.db.models import Manager, QuerySet

from .utils import generate_shortcode


class UrlQuerySet(models.QuerySet):
    def create(self, *args, **kwargs):
        kwargs.setdefault('shortcode', generate_shortcode())
        return super(UrlQuerySet, self).create(*args, **kwargs)


class UrlManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        """
        Retreive costum QuerySet class (UrlQuerySet).

        :return :type QuerySet
        """
        return UrlQuerySet(self.model, using=self._db)
