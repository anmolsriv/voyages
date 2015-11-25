from django.db import models


class ExportArea(models.Model):
    """
    Class represents Export area entity.
    """

    name = models.CharField(max_length=200, verbose_name="Export area name")
    order_num = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    show_at_zoom = models.IntegerField()
    show_on_map = models.BooleanField()

    def __unicode__(self):
        return self.name


class ExportRegion(models.Model):
    """
    Class represents Export region entity.
    """

    name = models.CharField(max_length=200, verbose_name="Export region name")
    order_num = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    show_at_zoom = models.IntegerField()
    show_on_map = models.BooleanField()
    export_area = models.ForeignKey(ExportArea)

    def __unicode__(self):
        return self.name


class ImportArea(models.Model):
    """
    Class represents Import area entity.
    """

    name = models.CharField(max_length=200, verbose_name="Import area name")
    order_num = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    show_at_zoom = models.IntegerField()
    show_on_map = models.BooleanField()

    def __unicode__(self):
        return self.name


class ImportRegion(models.Model):
    """
    Class represents Import region entity.
    """

    name = models.CharField(max_length=200, verbose_name="Import region name")
    order_num = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    show_at_zoom = models.IntegerField()
    show_on_map = models.BooleanField()
    import_area = models.ForeignKey(ImportArea)

    def __unicode__(self):
        return self.name


class Nation(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    order_num = models.IntegerField()

    def __unicode__(self):
        return self.name


class Estimate(models.Model):
    """
    Class represents Estimate entity
    """

    nation = models.ForeignKey(Nation)
    year = models.IntegerField()
    embarkation_region = models.ForeignKey(ExportRegion, null=True, blank=True)
    disembarkation_region = models.ForeignKey(ImportRegion, null=True, blank=True)
    embarked_slaves = models.FloatField(null=True, blank=True)
    disembarked_slaves = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


class EstimateManager(models.Manager):
    _all = {}
    _has_loaded = False
    import threading

    _lock = threading.Lock()

    @classmethod
    def cache(cls):
        with cls._lock:
            if not cls._has_loaded:
                cls._has_loaded = True
                cls._all = {v.pk: v for v in Estimate.objects.all()}
        return cls._all

    # Ensure that we load some related members thus
    # avoiding hitting the DB multiple times.
    def get_query_set(self):
        return super(EstimateManager, self).get_query_set().select_related(
            'embarkation_region__export_area',
            'disembarkation_region__import_area')
