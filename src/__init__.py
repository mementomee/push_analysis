# config/__init__.py
"""
Конфігураційні модулі для push-аналізу
"""

from .database_config import DatabaseManager
from .constants import (
    PUSH_START_DATE, 
    PUSH_END_DATE,
    CONVERSION_START_DATE,
    CONVERSION_END_DATE,
    ANDROID_TYPE,
    PUSH_EVENT_TYPE,
    TARGET_APPS,
    TIER_1_COUNTRIES,
    TIER_2_COUNTRIES, 
    TIER_3_COUNTRIES,
    get_country_tier
)

__all__ = [
    'DatabaseManager', 
    'PUSH_START_DATE', 
    'PUSH_END_DATE',
    'CONVERSION_START_DATE',
    'CONVERSION_END_DATE',
    'ANDROID_TYPE',
    'PUSH_EVENT_TYPE',
    'TARGET_APPS',
    'TIER_1_COUNTRIES',
    'TIER_2_COUNTRIES', 
    'TIER_3_COUNTRIES',
    'get_country_tier'
]

# src/__init__.py
"""
Основні модулі для аналізу push-сповіщень
"""

# Імпортуємо тільки після того, як всі файли створені
try:
    from .database import PushDatabase
    from .data_loader import DataLoader
    from .analyzer import PushAnalyzer
    from .visualizer import PushVisualizer
    
    __all__ = [
        'PushDatabase',
        'DataLoader', 
        'PushAnalyzer',
        'PushVisualizer'
    ]
    
    def get_analysis_suite(cache_enabled=True):
        """
        Повертає готовий набір інструментів для аналізу
        
        Returns:
            tuple: (loader, analyzer, visualizer)
        """
        loader = DataLoader(cache_enabled=cache_enabled)
        analyzer = PushAnalyzer()
        visualizer = PushVisualizer()
        
        return loader, analyzer, visualizer

except ImportError as e:
    print(f"Увага: Деякі модулі не завантажені: {e}")
    __all__ = []

__version__ = "1.0.0"
__author__ = "Push Analysis Team"