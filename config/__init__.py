# config/__init__.py
"""
Конфігураційні модулі для push-аналізу
"""

from .database_config import DatabaseManager
from .constants import *

__all__ = [
    'DatabaseManager', 
    'PUSH_START_DATE', 
    'PUSH_END_DATE',
    'TARGET_APPS',
    'get_country_tier'
]

# src/__init__.py
"""
Основні модулі для аналізу push-сповіщень
"""

from .database import PushDatabase
from .data_loader import DataLoader
from .analyzer import PushAnalyzer
from .visualizer import PushVisualizer

__version__ = "1.0.0"
__author__ = "Push Analysis Team"

__all__ = [
    'PushDatabase',
    'DataLoader', 
    'PushAnalyzer',
    'PushVisualizer'
]

# Швидкий імпорт для зручності
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

# Головний __init__.py (кореневий)
"""
Push Analysis Project - Аналіз впливу push-сповіщень на депозити Android-користувачів

Це пакет для аналізу ефективності push-сповіщень в мобільних застосунках.
Включає інструменти для завантаження даних, A/B тестування, 
географічного аналізу та візуалізації результатів.

Основні компоненти:
- config: Налаштування баз даних та константи
- src: Основна логіка аналізу
- notebooks: Jupyter notebooks для інтерактивного аналізу

Швидкий старт:
    from src import get_analysis_suite
    loader, analyzer, visualizer = get_analysis_suite()
"""

__version__ = "1.0.0"
__title__ = "Push Analysis"
__description__ = "Аналіз впливу push-сповіщень на поведінку користувачів"
__author__ = "Analysis Team"

# Основні експорти
from src import (
    PushDatabase,
    DataLoader,
    PushAnalyzer, 
    PushVisualizer,
    get_analysis_suite
)

from config import (
    DatabaseManager,
    PUSH_START_DATE,
    PUSH_END_DATE,
    TARGET_APPS,
    get_country_tier
)

# Зручні функції для швидкого старту
def quick_start(cache_enabled=True):
    """
    Швидкий старт аналізу з базовими налаштуваннями
    
    Args:
        cache_enabled: Використовувати кеш
        
    Returns:
        dict: Словник з готовими компонентами
    """
    return {
        'loader': DataLoader(cache_enabled=cache_enabled),
        'analyzer': PushAnalyzer(),
        'visualizer': PushVisualizer(),
        'database': PushDatabase(cache_enabled=cache_enabled)
    }

def test_setup():
    """
    Тестування налаштувань проекту
    
    Returns:
        bool: Чи готова система до роботи
    """
    try:
        from config.database_config import DatabaseManager
        db = DatabaseManager()
        db.test_connections()
        return True
    except Exception as e:
        print(f"Помилка налаштування: {e}")
        return False

__all__ = [
    # Класи
    'PushDatabase',
    'DataLoader',
    'PushAnalyzer', 
    'PushVisualizer',
    'DatabaseManager',
    
    # Константи
    'PUSH_START_DATE',
    'PUSH_END_DATE', 
    'TARGET_APPS',
    
    # Функції
    'get_analysis_suite',
    'get_country_tier',
    'quick_start',
    'test_setup'
]