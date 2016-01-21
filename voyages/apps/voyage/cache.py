from django.utils.translation import ugettext as _
import threading
from models import *

class CachedGeo:
    """
    Caches a geographical place (could be a port, region, or broad region)
    """
    def __init__(self, pk, name, lat, lng, show, parent):
        self.pk = pk
        self.name = name
        self.lat = lat
        self.lng = lng
        self.show = show
        self.parent = parent

    @classmethod
    def get_hierarchy(cls, pk):
        """
        Fetches a tuple (port, region, broad_region) given the primary key of a port.
        """
        port = VoyageCache.ports.get(pk)
        if port is None:
            return None
        region = VoyageCache.regions.get(port.parent)
        if region is None:
            return None
        broad_region = VoyageCache.broad_regions.get(region.parent)
        return port, region, broad_region

class CachedVoyage:
    """
    Cache the most basic information of a voyage for map generation and aggregation
    """
    def __init__(self, pk, id, emb_pk, dis_pk, ship_nat_pk, ship_name, ship_ton, date_voyage_began, embarked, disembarked):
        self.pk = pk
        self.voyage_id = id
        self.emb_pk = emb_pk
        self.dis_pk = dis_pk
        self.ship_nat_pk = ship_nat_pk
        self.ship_name = ship_name
        self.ship_ton = ship_ton
        self.year = VoyageDates.get_date_year(date_voyage_began)
        self.embarked = embarked
        self.disembarked = disembarked

class VoyageCache:
    """
    Caches all geo locations and all voyages in the db loading only the minimum
    amount of fields required.
    """
    voyages = {}
    ports = {}
    regions = {}
    broad_regions = {}
    nations = {}

    _loaded = False
    _lock = threading.Lock()

    @classmethod
    def load(cls, force_reload=False):
        with cls._lock:
            if not force_reload and cls._loaded:
                return
            cls._loaded = False
            cls.ports = {x[0]: CachedGeo(x[0], x[1], x[2], x[3], x[4], x[5])
                         for x in Place.objects.values_list('pk',
                                                            'place',
                                                            'latitude',
                                                            'longitude',
                                                            'show_on_main_map',
                                                            'region_id').iterator()}
            cls.regions = {x[0]: CachedGeo(x[0], x[1], x[2], x[3], x[4], x[5])
                           for x in Region.objects.values_list('pk',
                                                               'region',
                                                               'latitude',
                                                               'longitude',
                                                               'show_on_main_map',
                                                               'broad_region_id').iterator()}
            cls.broad_regions = {x[0]: CachedGeo(x[0], x[1], x[2], x[3], x[4], None)
                                 for x in BroadRegion.objects.values_list('pk',
                                                                          'broad_region',
                                                                          'latitude',
                                                                          'longitude',
                                                                          'show_on_map').iterator()}
            cls.nations = {x[0]: _(x[1])
                           for x in Nationality.objects.values_list('pk', 'label').iterator()}
            cls.voyages = {x[0]: CachedVoyage(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9])
                           for x in Voyage.objects.values_list('pk',
                                                               'voyage_id',
                                                               'voyage_itinerary__imp_principal_place_of_slave_purchase_id',
                                                               'voyage_itinerary__imp_principal_port_slave_dis_id',
                                                               'voyage_ship__imputed_nationality_id',
                                                               'voyage_ship__ship_name',
                                                               'voyage_ship__tonnage',
                                                               'voyage_dates__voyage_began',
                                                               'voyage_slaves_numbers__imp_total_num_slaves_embarked',
                                                               'voyage_slaves_numbers__imp_total_num_slaves_disembarked'
                                                               ).iterator()}
            cls._loaded = True