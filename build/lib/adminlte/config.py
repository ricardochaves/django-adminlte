from django.conf import settings
from django.contrib.admin import ModelAdmin


def default_config():
    return {
        
        # configurable
        'ADMIN_NAME': 'Admin LTE',
        'HEADER_DATE_FORMAT': 'l, jS F Y',
        'HEADER_TIME_FORMAT': 'H:i',

        # menu
        'SEARCH_URL': '/admin/auth/user/',

        # misc
        'LIST_PER_PAGE': 20
    }
    
def get_config(param=None):
    config_key = 'SUIT_CONFIG'
    if hasattr(settings, config_key):
        config = getattr(settings, config_key, {})
    else:
        config = default_config()
    if param:
        value = config.get(param)
        if value is None:
            value = default_config().get(param)
        return value
    return config

# Set global list_per_page
ModelAdmin.list_per_page = get_config('LIST_PER_PAGE')