# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.

# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in
# this project, and the INSTALLED_ADDONS section in requirements.in.

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.

    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.

import os

import aldryn_addons.settings
from django_storage_url import dsn_configured_storage_class

aldryn_addons.settings.load(locals())

# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.

INSTALLED_APPS.extend([
    # Extend the INSTALLED_APPS setting by listing additional applications here
    'livereload',
    'django_extensions',
    "users.apps.UsersConfig",
    "pages.apps.PagesConfig",
    "apartments.apps.ApartmentsConfig",
])

MIDDLEWARE.extend([
    'livereload.middleware.LiveReloadScript',
])

# To see the settings that have been applied, use the Django diffsettings
# management command.
# See https://docs.divio.com/en/latest/how-to/configure-settings.html#list

AUTH_USER_MODEL = "users.User"

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join('/data/media/')

# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = 'isotachglobal.settings.DefaultStorageClass'
