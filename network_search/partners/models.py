from django.db import models
from django.contrib.postgres.fields import ArrayField

from network_search.core.models import Link
from network_search.core.models import BaseResource
from network_search.core.models import ResourceQueryset


class PartnerQueryset(ResourceQueryset):
    def search(self, **kwargs):
        qs = super().search(**kwargs)

        grades = kwargs.pop('grade', [])
        genders = kwargs.pop('gender', [])
        needs = kwargs.pop('need', [])
        reach = kwargs.pop('reach', [])
        service_tiers = kwargs.pop('service_tiers', [])
        setting = kwargs.pop('setting', [])
        services = kwargs.pop('services', [])
        evidence = kwargs.pop('evidence', [])
        cost_free = kwargs.pop('free_of_cost', None)
        use_in_network = kwargs.pop('use_in_network', None)

        if grades:
            qs = qs.filter(grade__overlap=grades)
        if genders:
            qs = qs.filter(gender__overlap=genders)
        if needs:
            qs = qs.filter(student_need__overlap=needs)
        if reach:
            qs = qs.filter(organizational_reach__overlap=reach)
        if service_tiers:
            qs = qs.filter(tiers_of_service__overlap=service_tiers)
        if setting:
            qs = qs.filter(setting__overlap=setting)
        if services:
            qs = qs.filter(service_categories__overlap=services)
        if evidence:
            qs = qs.filter(tiers_of_evidence__overlap=evidence)

        if cost_free is not None:
            qs = qs.filter(is_cost_free=cost_free)

        if use_in_network is True:
            qs = qs.exclude(network_use=None)
        elif use_in_network is False:
            qs = qs.filter(network_use=None)

        return qs.distinct('name')


class Partner(BaseResource):
    """
    Represents a partner organization
    """

    url_name = "partner_detail"
    search_content_fields = ['name', 'mission', 'overview']

    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    contact_email = models.EmailField()

    website = models.URLField()

    mission = models.TextField(blank=True)
    overview = models.TextField(blank=True)

    grade = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    gender = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    organizational_reach = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    student_need = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    tiers_of_service = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    setting = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    service_categories = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )
    tiers_of_evidence = ArrayField(
        models.CharField(max_length=100, blank=True),
        blank=True,
        null=True,
    )

    is_cost_free = models.BooleanField(blank=True, default=False)
    cost_description = models.CharField(max_length=200, blank=True, null=True)

    is_core_partner = models.BooleanField(blank=True, default=False)  # is this based on link from Program???

    network_use = models.ManyToManyField('affiliates.Affiliate', related_name='partner_profiles', blank=True)
    featured_network = models.ManyToManyField('affiliates.Affiliate', related_name='featured_partners', blank=True)

    partners = PartnerQueryset.as_manager()
    objects = partners

    def evidence_base(self):
        """Returns either the last evidence choice or ''
        """
        try:
            return self.tiers_of_evidence[-1]
        except (IndexError, TypeError):
            return ''


class WebinarLink(Link):
    partner = models.ForeignKey('Partner', related_name='webinars')


class PresentationsLink(Link):
    partner = models.ForeignKey('Partner', related_name='presentations')
