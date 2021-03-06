from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

from network_search.affiliates import forms
from network_search.affiliates import models


@admin.register(models.ExcelUpload)
class AffiliateUploadAdmin(admin.ModelAdmin):
    list_display = ['year', 'status', 'created', 'data_file']
    actions = ['copy_import']

    def copy_import(self, request, queryset):
        try:
            original = queryset.get()
        except (MultipleObjectsReturned, ObjectDoesNotExist):
            messages.error(request, "Select 1 and only 1 upload to copy")
            return

        original.copy()
        messages.success(request, "Starting new data import.")

    copy_import.short_description = "Duplicate and rerun an import"


@admin.register(models.Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    form = forms.AffiliateAdminForm
    list_display = ('name', 'state')
    search_fields = ('name', 'state')

    def get_queryset(self, request):
        return super().get_queryset(request).active()


@admin.register(models.EndOfYear)
class EndOfYearAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']


@admin.register(models.AffiliateEOYData)
class AffiliateEOYAdmin(admin.ModelAdmin):
    list_display = ('affiliate', 'year')
    search_fields = ('affiliate__name',)
    raw_id_fields = ['affiliate']

    fieldsets = (
        (None, {
            'fields': ['affiliate', 'year'],
        }),
        ('Basic info', {
            'fields': [
                'districts', 'executive_director_name', 'executive_director_email',
                'program_lead_name', 'program_lead_email',
            ],
        }),
        ('Staffing', {
            'fields': [
                'staff_fulltime_affiliate', 'staff_parttime_affiliate', 'staff_fulltime_non_affiliate',
                'staff_parttime_non_affiliate', 'staff_fulltime_americorps', 'staff_parttime_americorps',
            ],
        }),
        ('Funding', {
            'fields': [
                'funding_public_federal', 'funding_public_state', 'funding_public_city',
                'funding_public_school_district', 'funding_private_corporate', 'funding_private_foundation',
                'funding_private_board', 'funding_private_individual', 'funding_private_events',
                'funding_private_cis_national', 'funding_private_cis_state_office', 'funding_private_npo',
                'funding_private_other',
            ],
        })
    )


@admin.register(models.SchoolEOYData)
class SchoolEOYAdmin(admin.ModelAdmin):
    # list_display = ('name', 'affiliate', 'year')
    search_fields = ['name', 'affiliate_data__affiliate__name']
    raw_id_fields = ['affiliate_data']
    form = forms.SchoolAdminForm
    fieldsets = (
        (None, {
            'fields': ['affiliate_data'],
        }),
        ('School', {
            'fields': ['name', 'site_type', 'location', 'location_model', 'students_case_managed', 'students_total',
                       'partners'],
        }),
        ('Students race and gender', {
            'fields': [
                'students_female_american_indian', 'students_female_asian', 'students_female_black',
                'students_female_hispanic', 'students_female_white', 'students_female_two_or_more_races',
                'students_female_other', 'students_female_unknown', 'students_male_american_indian',
                'students_male_asian', 'students_male_black', 'students_male_hispanic',
                'students_male_white', 'students_male_two_or_more_races', 'students_male_other',
                'students_male_unknown', 'students_unknown_race_gender',
            ],
        }),
        ('Student performance', {
            'fields': [
                'students_k_11_promoted', 'students_k_11_retained', 'students_k_11_dropped_out',
                'students_k_11_transferred', 'students_k_11_ged',
                'students_k_11_expelled', 'students_k_11_incarcerated', 'students_k_11_deceased',
                'students_k_11_other', 'students_k_11_unknown',
                'students_grade_12_graduated', 'students_grade_12_retained', 'students_grade_12_dropped_out',
                'students_grade_12_transferred',
                'students_grade_12_ged',
                'students_grade_12_expelled',
                'students_grade_12_incarcerated',
                'students_grade_12_deceased',
                'students_grade_12_other', 'students_grade_12_unknown'
            ],
        }),
        ('Students served', {
            'fields': [
                'students_served_frpl', 'students_served_ell', 'students_served_foster',
                'students_served_homeless', 'students_served_lgbt', 'students_served_pregnant_parenting',
                'students_served_special_education', 'students_served_substance_abuse',
                'students_served_adjudicated_youth', 'students_served_child_of_military',
                'students_served_gang', 'students_served_incarcerated_parent'
            ],
        }),
        ('Students by grade', {
            'description': "1 or 0 for whether the affiliate serves students in this grade",
            'fields': [
                'students_grade_prek',
                'students_grade_k',
                'students_grade_1',
                'students_grade_2',
                'students_grade_3',
                'students_grade_4',
                'students_grade_5',
                'students_grade_6',
                'students_grade_7',
                'students_grade_8',
                'students_grade_9',
                'students_grade_10',
                'students_grade_11',
                'students_grade_12',
            ],
        }),
        ('Services', {
            'fields': [
                'service_academic_assistance', 'service_basic_needs',
                'service_behavior_intervention', 'service_college_career_prep',
                'service_comm_service', 'service_enrichment',
                'service_family_engagement', 'service_life_skills',
                'service_physical_fitness_health', 'service_prof_mental_health',
            ],
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
