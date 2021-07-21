from haystack import indexes
from unidecode import unidecode

from voyages.apps.past.models import Enslaved
from voyages.apps.voyage.globals import search_mangle_methods, no_mangle
from voyages.apps.voyage.search_indexes import TranslatedTextField, get_year


class EnslavedIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Index method for class Enslaved.
    """
    text = indexes.CharField(document=True, use_template=True)

    var_enslaved_id = indexes.IntegerField(null=True, indexed=True, model_attr='enslaved_id')

    var_documented_name = indexes.CharField(null=True, model_attr='documented_name')
    var_name_first = indexes.CharField(null=True, model_attr='name_first')
    var_name_second = indexes.CharField(null=True, model_attr='name_second')
    var_name_third = indexes.CharField(null=True, model_attr='name_third')

    var_modern_name_first = indexes.CharField(null=True, model_attr='modern_name_first')
    var_modern_name_second = indexes.CharField(null=True, model_attr='modern_name_second')
    var_modern_name_third = indexes.CharField(null=True, model_attr='modern_name_third')

    var_editor_modern_names_certainty = indexes.CharField(null=True,
                                                     model_attr='editor_modern_names_certainty')

    var_age = indexes.IntegerField(null=True, model_attr='age')
    var_is_adult = indexes.BooleanField(null=True, model_attr='is_adult')
    var_gender = indexes.IntegerField(null=True, model_attr='gender')
    var_height = indexes.FloatField(null=True, model_attr='height')

    # Sources
    var_sources = indexes.MultiValueField(indexed=True, stored=True, null=True)
    var_sources_plaintext = indexes.CharField(null=True, faceted=True, indexed=True)
    var_sources_plaintext_search = indexes.NgramField(null=True, faceted=False, indexed=True)

    #ethnicity
    var_ethnicity_name = indexes.CharField(null=True, indexed=True, model_attr='ethnicity__name')
    var_ethnicity_language_group_name = indexes.CharField(null=True,
                                                          model_attr='ethnicity__language_group__name')
    var_ethnicity_language_group_latitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='ethnicity__language_group__latitude')
    var_ethnicity_language_group_longitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='ethnicity__language_group__longitude')
    var_ethnicity_language_group_modern_country_name = indexes.CharField(null=True, indexed=True,
                                                          model_attr='ethnicity__language_group__modern_country__name')
    var_ethnicity_language_group_modern_country_latitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='ethnicity__language_group__modern_country__latitude')
    var_ethnicity_language_group_modern_country_longitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='ethnicity__language_group__modern_country__longitude')

    #language_group
    var_language_group_name = indexes.CharField(null=True,
                                                          model_attr='language_group__name')
    var_language_group_latitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='language_group__latitude')
    var_language_group_longitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='language_group__longitude')
    var_language_group_modern_country_name = indexes.CharField(null=True, indexed=True,
                                                          model_attr='language_group__modern_country__name')
    var_language_group_modern_country_latitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='language_group__modern_country__latitude')
    var_language_group_modern_country_longitude = indexes.DecimalField(null=True, indexed=True,
                                                          model_attr='language_group__modern_country__longitude')

    #register_country
    var_register_country_name = indexes.CharField(null=True, indexed=True,
                                                          model_attr='register_country__name')

    #post_disembark_location
    var_post_disembark_location_place = indexes.CharField(null=True, indexed=True,
                                                          model_attr='post_disembark_location__place')
    var_post_disembark_location_region = indexes.CharField(null=True, indexed=True,
                                                          model_attr='post_disembark_location__region')
    var_post_disembark_location_idnum = indexes.CharField(null=True, indexed=True,
                                                          model_attr='post_disembark_location__value')
    var_post_disembark_location_longitude = indexes.CharField(null=True, indexed=True,
                                                          model_attr='post_disembark_location__longitude')
    var_post_disembark_location_latitude = indexes.CharField(null=True, indexed=True,
                                                          model_attr='post_disembark_location__latitude')

    #voyage
    var_voyage_ship_name = indexes.NgramField(null=True, model_attr='voyage__voyage_ship__ship_name')

    var_voyage_ship_name_plaintext = indexes.CharField( null=True, faceted=True, indexed=True,
                                                        model_attr='voyage__voyage_ship__ship_name' )
    var_voyage_imp_port_voyage_begin = indexes.CharField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_port_voyage_begin__place')
    var_voyage_imp_port_voyage_begin_lang_en = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_port_voyage_begin__place')
    var_voyage_imp_port_voyage_begin_lang_pt = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_port_voyage_begin__place')
    var_voyage_imp_port_voyage_begin_lang_es = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_port_voyage_begin__place')
    var_voyage_imp_principal_port_slave_dis = indexes.CharField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_principal_port_slave_dis__place')
    var_voyage_imp_principal_port_slave_dis_lang_en = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_principal_port_slave_dis__place')
    var_voyage_imp_principal_port_slave_dis_lang_pt = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_principal_port_slave_dis__place')
    var_voyage_imp_principal_port_slave_dis_lang_es = TranslatedTextField( null=True,
                                                        model_attr='voyage__voyage_itinerary__imp_principal_port_slave_dis__place')
    var_voyage_imp_arrival_at_port_of_dis = indexes.IntegerField(null=True, faceted=True)
    var_voyage_dataset = indexes.IntegerField(null=False, stored=True, indexed=True, model_attr='voyage__dataset')

    def get_model(self):
        return Enslaved

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    # Voyage sources
    def prepare_var_sources(self, obj):
        return [
            conn.text_ref + "<"
            ">" + ("" if conn.source is None else conn.source.full_ref)
            for conn in obj.sources.all()
        ]

    def prepare_var_sources_plaintext(self, obj):
        return ", ".join(self.prepare_var_sources(obj))

    def prepare_var_sources_plaintext_search(self, obj):
        mangle_method = search_mangle_methods.get('var_sources', no_mangle)
        return mangle_method(
            unidecode(self.prepare_var_sources_plaintext(obj)))

    # Voyage dates
    def prepare_var_imp_arrival_at_port_of_dis(self, obj):
        try:
            return get_year(obj.voyage.voyage_dates.imp_arrival_at_port_of_dis)
        except (AttributeError, TypeError):
            return None