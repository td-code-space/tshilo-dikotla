"""
Django settings for tshilo_dikotla project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

from django.core.management.color import color_style


style = color_style()

APP_NAME = 'tshilo_dikotla'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ETC_DIR = '/etc'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'td.bhp.org.bw:8000'

# KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mt2-_fw#9p*yx4vps(j&-*5*a(t(jpos&24xd&)4+s4!lu*w^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['td-test.bhp.org.bw', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'simple_history',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_action_item.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_form_validators.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_lab_dashboard.apps.AppConfig',
    'edc_label.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'td_visit_schedule.apps.AppConfig',
    'td_dashboard.apps.AppConfig',
    'td_infant.apps.AppConfig',
    'td_infant_validators.apps.AppConfig',
    'td_maternal.apps.AppConfig',
    'td_reference.apps.AppConfig',
    'td_maternal_validators.apps.AppConfig',
    'td_metadata_rules.apps.AppConfig',
    'tshilo_dikotla.apps.EdcTimepointAppConfig',
    'tshilo_dikotla.apps.EdcAppointmentAppConfig',
    'tshilo_dikotla.apps.EdcMetadataAppConfig',
    'tshilo_dikotla.apps.EdcBaseAppConfig',
    'tshilo_dikotla.apps.EdcProtocolAppConfig',
    'tshilo_dikotla.apps.EdcVisitTrackingAppConfig',
    'tshilo_dikotla.apps.AppConfig',
    'tshilo_dikotla.apps.EdcFacilityAppConfig',
    'tshilo_dikotla.apps.EdcIdentifierAppConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_lab_dashboard.middleware.DashboardMiddleware'
]

ROOT_URLCONF = 'tshilo_dikotla.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tshilo_dikotla.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'test' in sys.argv and 'mysql' not in DATABASES.get('default').get('ENGINE'):
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        "edc_call_manager": None,
        "edc_appointment": None,
        "edc_call_manager": None,
        "edc_consent": None,
        "edc_death_report": None,
        "edc_export": None,
        "edc_identifier": None,
        "edc_lab": None,
        "edc_metadata": None,
        "edc_rule_groups": None,
        "edc_registration": None,
        "edc_sync_files": None,
        "edc_sync": None,
        "td_maternal": None}

if 'test' in sys.argv:
    PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_STUDY_SITE = '40'
REVIEWER_SITE_ID = 41


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'tshilo_dikotla', 'static')

# dashboards
DASHBOARD_URL_NAMES = {
    'maternal_subject_models_url': 'maternal_subject_models_url',
    'subject_listboard_url': 'td_dashboard:subject_listboard_url',
    'screening_listboard_url': 'td_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'td_dashboard:subject_dashboard_url',
    'infant_listboard_url': 'td_dashboard:infant_listboard_url',
    'infant_subject_dashboard_url': 'td_dashboard:infant_subject_dashboard_url',
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'tshilo_dikotla/base.html',
    'dashboard_base_template': 'tshilo_dikotla/base.html',
    'screening_listboard_template': 'td_dashboard/subject_screening/listboard.html',
    'subject_listboard_template': 'td_dashboard/maternal_subject/listboard.html',
    'subject_dashboard_template': 'td_dashboard/maternal_subject/dashboard.html',
    'infant_listboard_template': 'td_dashboard/infant_subject/listboard.html',
    'infant_subject_dashboard_template': 'td_dashboard/infant_subject/dashboard.html',
}

REST_FRAMEWORK = {
    'PAGE_SIZE': 1,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination',
    )
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

# edc_facility
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''
