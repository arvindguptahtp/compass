"""

"""
import pytest

from network_search.affiliates.models import Affiliate
from network_search.affiliates.models import EndOfYear
from network_search.affiliates.models import SchoolEOYData
from network_search.affiliates.models import AffiliateEOYData


def affiliate_factory(**kwargs):
    defaults = dict(
        name="Base Affiliate",
        state="VA",
        cis_id=8,
        official_name="Base Affiliate",
        address_street="100 Main St",
        address_city="Anywhere",
        address_state="VA",
        address_postcode="22202",
    )
    defaults.update(kwargs)
    return Affiliate.affiliates.create(**defaults)


def school_data_factory(affiliate, year, **kwargs):
    defaults = dict(
        students_female_american_indian=0,
        students_female_asian=0,
        students_female_black=0,
        students_female_hispanic=0,
        students_female_white=0,
        students_female_two_or_more_races=0,
        students_female_other=0,
        students_female_unknown=0,
        students_male_american_indian=0,
        students_male_asian=0,
        students_male_black=0,
        students_male_hispanic=0,
        students_male_white=0,
        students_male_two_or_more_races=0,
        students_male_other=0,
        students_male_unknown=0,
        students_unknown_race_gender=0,
    )
    defaults.update(kwargs)
    affiliate_data, _ = AffiliateEOYData.objects.get_or_create(affiliate=affiliate, year=year)
    defaults.update({'affiliate_data': affiliate_data})
    school_data = SchoolEOYData.objects.create(**defaults)
    return school_data


@pytest.fixture
def current_eoy():
    yield EndOfYear.objects.create(year_ends=2017, is_active=True)


@pytest.fixture
def past_eoy():
    yield EndOfYear.objects.create(year_ends=2016, is_active=False)