from django.db import models
from django.db.models import *

from voyages.apps.voyage.models import Place, Voyage, VoyageSources


class NamedModelAbstractBase(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()

    class Meta:
        abstract = True


class EnslaverInfoAbstractBase(models.Model):
    id = models.IntegerField(primary_key=True)
    principal_alias = models.CharField()
    is_corporate_entity = models.BooleanField()

    # Personal info.
    birth_year = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_day = models.IntegerField(null=True)
    birth_place = models.CharField(null=True)

    death_year = models.IntegerField(null=True)
    death_month = models.IntegerField(null=True)
    death_day = models.IntegerField(null=True)
    death_place = models.CharField(null=True)

    father_name = models.CharField(null=True)
    father_occupation = models.CharField(null=True)
    mother_name = models.CharField(null=True)

    first_spouse_name = models.CharField(null=True)
    first_marriage_date = models.CharField(null=True)
    second_spouse_name = models.CharField(null=True)
    second_marriage_date = models.CharField(null=True)

    probate_date = models.CharField(null=True)
    will_value_pounds = models.CharField(null=True)
    will_value_dollars = models.CharField(null=True)
    will_court = models.CharField(null=True)

    class Meta:
        abstract = True


class ModernCountry(NamedModelAbstractBase):
    longitude = models.DecimalField("Longitude of Country",
                                    max_digits=10, decimal_places=7,
                                    null=False)
    latitude = models.DecimalField("Latitude of Country",
                                   max_digits=10, decimal_places=7,
                                   null=False)


class RegisterCountry(NamedModelAbstractBase):
    pass


class LanguageGroup(NamedModelAbstractBase):
    longitude = models.DecimalField("Longitude of point",
                                    max_digits=10, decimal_places=7,
                                    null=False)
    latitude = models.DecimalField("Latitude of point",
                                   max_digits=10, decimal_places=7,
                                   null=False)
    modern_country = models.ForeignKey(ModernCountry, null=False, related_name='language_groups')


class AltLanguageGroupName(NamedModelAbstractBase):
    language_group = models.ForeignKey(LanguageGroup, null=False, related_name='alt_names')


class Ethnicity(NamedModelAbstractBase):
    language_group = models.ForeignKey(LanguageGroup, null=False, related_name='ethnicities')


class AltEthnicityName(NamedModelAbstractBase):
    ethnicity = models.ForeignKey(Ethnicity, null=False, related_name='alt_names')


class Gender(NamedModelAbstractBase):
    pass


class EnslavedFate(NamedModelAbstractBase):
    pass


class EnslavedStatus(NamedModelAbstractBase):
    pass


class EnslavedName(NamedModelAbstractBase):
    language = models.CharField(null=False, blank=False)
    recordings_count = models.IntegerField()

    class Meta:
        unique_together = ('name', 'language')


class EnslavedVoyageStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField()


class EnslavedAlias(models.Model):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(null=False)


# TODO: this model will replace resources.AfricanName
class EnslavedIdentity(models.Model):
    """
    Enslaved person.
    """
    id = models.IntegerField(primary_key=True)
    african_name = models.CharField(blank=True)
    modern_african_name = models.CharField(blank=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    language_group = models.ForeignKey(LanguageGroup, null=True, on_delete=models.CASCADE)
    register_country = models.ForeignKey(RegisterCountry, null=True, on_delete=models.CASCADE)
    stature = models.DecimalField()
    last_location = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    enslaved_status = models.ForeignKey(EnslavedStatus, null=True, on_delete=models.CASCADE)
    enslaved_fate = models.ForeignKey(EnslavedFate, null=True, on_delete=models.CASCADE)
    voyage = models.ManyToManyField(Voyage, through='EnslavedVoyageConnection', null=False)
    alias = models.ForeignKey(EnslavedAlias, null=True)
    sources = models.ManyToManyField \
        (VoyageSources, through='EnslavedSourceConnection', related_name='+')
    related_enslaver = models.ManyToManyField('EnslaverIdentity', null=True,
                                              through='EnslaverEnslaverEnslavementConnection')
    last_known_year = models.IntegerField()
    last_known_month = models.IntegerField()
    last_known_date = models.IntegerField()


class EnslavedVoyageConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.ForeignKey(EnslavedVoyageStatus, null=True)
    voyage = models.ForeignKey(Voyage, null=False)
    enslaved = models.ForeignKey('EnslavedIdentity', null=False)


class EnslavedSourceConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    enslaved = models.ForeignKey(EnslavedIdentity, on_delete=models.CASCADE,
                                 related_name='sources_conn')
    # Sources are shared with Voyages.
    source = models.ForeignKey(VoyageSources, on_delete=models.CASCADE,
                               related_name='+', null=False)
    source_order = models.IntegerField()
    text_ref = models.CharField(null=False, blank=True)


class StanfordKin(NamedModelAbstractBase):
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    kin_url = models.CharField()


class EnslavementRelation(NamedModelAbstractBase):
    pass


class Enslavement(models.Model):
    id = models.IntegerField(primary_key=True)
    relation = models.ForeignKey(EnslavementRelation, on_delete=models.CASCADE, null=False)
    relation_start_year = models.IntegerField()
    relation_start_month = models.IntegerField()
    relation_start_date = models.IntegerField()
    relation_end_year = models.IntegerField()
    relation_end_month = models.IntegerField()
    relation_end_date = models.IntegerField()
    enslavement_place = models.ManyToManyField('Place', through='EnslavementPlaceConnection',
                                               null=True)
    sources = models.ManyToManyField \
        (VoyageSources, through='EnslavementSourceConnection', related_name='+')

    
class EnslavementPlaceConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    enslavement = models.ForeignKey('Enslavement', on_delete=models.CASCADE, null=False)
    enslavement_place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True)


class EnslaverIdentity(EnslaverInfoAbstractBase):
    alias = models.ForeignKey('EnslaverAlias', on_delete=models.CASCADE, null=True)
    stanford_kin = models.ManyToManyField('StanfordKin', through='EnslaverStanfordKinConnection',
                                          null=True)
    voyage = models.ManyToManyField('Voyage', through='EnslaverVoyageConnection', null=True)
    sources = models.ManyToManyField \
        (VoyageSources, through='EnslaverIdentitySourceConnection', related_name='+')
    related_enslaver = models.ManyToManyField('EnslaverIdentity', null=True,
                                              through='EnslaverEnslaverEnslavementConnection')
    related_enslaved = models.ManyToManyField('EnslavedIdentity', null=True,
                                              through='EnslavedEnslaverEnslavementConnection')

    class Meta:
        verbose_name = 'Enslaver unique identity and personal info'


class EnslaverStanfordKinConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    enslaver = models.ForeignKey('EnslaverIdentity', on_delete=models.CASCADE)
    stanford_kin = models.ForeignKey('StanfordKin', on_delete=models.CASCADE)


class EnslaverAlias(models.Model):
    """
        An alias represents a name appearing in a record that is mapped to
        a consolidated identity. The same individual may appear in multiple
        records under different names (aliases).
        """
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(null=False)
    enslaver = models.ForeignKey('EnslaverIdentity', on_delete=CASCADE, null=False)

    class Meta:
        verbose_name = 'Enslaver alias'


class EnslaverVoyageConnection(models.Model):
    """
    Associates an enslaver with a voyage at some particular role.
    """

    class Role:
        CAPTAIN = 1
        OWNER = 2
        BUYER = 3
        SELLER = 4
        INSURER = 5
        INVESTOR = 6
        SUPPLIER = 7

    id = models.IntegerField(primary_key=True)
    enslaver = models.ForeignKey('EnslaverIdentity', null=False, on_delete=models.CASCADE)
    voyage = models.ForeignKey('voyage.Voyage', null=False, on_delete=models.CASCADE)
    role = models.IntegerField(null=False)
    # There might be multiple persons with the same role for the same voyage
    # and they can be ordered (ranked) using the following field.
    order = models.IntegerField(null=True)
    # NOTE: we will have to substitute VoyageShipOwner and VoyageCaptain
    # models/tables by this entity.


class EnslaverIdentitySourceConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    identity = models.ForeignKey('EnslaverIdentity', on_delete=models.CASCADE)
    # Sources are shared with Voyages.
    source = models.ForeignKey('VoyageSources', related_name="+", null=False,
                               on_delete=models.CASCADE)
    source_order = models.IntegerField()
    text_ref = models.CharField(null=False, blank=True)


class EnslavedEnslaverEnslavementConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    enslaver = models.ForeignKey('EnslaverIdentity', null=False, on_delete=models.CASCADE)
    enslaved = models.ForeignKey('EnslavedIdentity', null=False, on_delete=models.CASCADE)
    enslavement = models.ForeignKey('Enslavement', null=False, on_delete=models.CASCADE)


class EnslaverEnslaverEnslavementConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    first_enslaver = models.ForeignKey('EnslaverIdentity', related_name="first_enslaver", on_delete=models.CASCADE)
    second_enslaver = models.ForeignKey('EnslaverIdentity', related_name="second_enslaver", on_delete=models.CASCADE)
    enslavement = models.ForeignKey('Enslavement', null=False, on_delete=models.CASCADE)


class EnslavementSourceConnection(models.Model):
    id = models.IntegerField(primary_key=True)
    enslavement = models.ForeignKey(Enslavement, on_delete=models.CASCADE)
    source = models.ForeignKey(VoyageSources, related_name="+", null=False)
    source_order = models.IntegerField()
    text_ref = models.CharField(null=False, blank=True)