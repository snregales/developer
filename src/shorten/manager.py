from django.db.models import Manager, QuerySet

from .utils import generate_shortcode


class UrlQuerySet(QuerySet):
    def create(self, **kwargs) -> 'Url':
        kwargs.setdefault('shortcode', generate_shortcode())
        return super(UrlQuerySet, self).create(**kwargs)


class UrlManager(Manager):
    def get_queryset(self) -> QuerySet:
        """
        Retreive costum QuerySet class (UrlQuerySet).

        :return :type QuerySet
        """
        return UrlQuerySet(self.model, using=self._db)
