from datetime import datetime, timedelta

# ЧАСОВІ ПЕРІОДИ
PUSH_START_DATE = '2025-05-22'
PUSH_END_DATE = '2025-05-29' 
CONVERSION_START_DATE = '2025-05-22'
CONVERSION_END_DATE = '2025-06-07'  # +9 днів для конверсій

# ФІЛЬТРИ
ANDROID_TYPE = 1
PUSH_EVENT_TYPE = 7  # SendPush
TARGET_APPS = ['Michelangelo', 'Leonardo', 'Raphael', 'Splinter']

# GEO CLASSIFICATION
TIER_1_COUNTRIES = [
    'US', 'UK', 'CA', 'AU', 'DE', 'FR', 'NL', 
    'SE', 'NO', 'DK', 'CH', 'AT', 'BE', 'FI'
]

TIER_2_COUNTRIES = [
    'ES', 'IT', 'PL', 'BR', 'MX', 'AR', 'CL', 
    'CZ', 'HU', 'SK', 'HR', 'SI', 'EE', 'LV', 'LT'
]

TIER_3_COUNTRIES = [
    'IN', 'ID', 'TH', 'VN', 'PH', 'MY', 'BD', 
    'PK', 'UA', 'RU', 'TR', 'EG', 'ZA', 'NG'
]

def get_country_tier(country: str) -> str:
    """Визначити tier країни"""
    if country in TIER_1_COUNTRIES:
        return 'Tier 1'
    elif country in TIER_2_COUNTRIES:
        return 'Tier 2'
    elif country in TIER_3_COUNTRIES:
        return 'Tier 3'
    else:
        return 'Other'
