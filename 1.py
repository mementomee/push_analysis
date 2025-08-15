#!/usr/bin/env python3
"""
Швидкий тест системи push-аналізу
Запуск: python quick_test.py
"""

def test_basic_imports():
    """Базовий тест імпортів"""
    print("🔍 Тестування базових імпортів...")
    
    try:
        # Тестуємо config
        from config.database_config import DatabaseManager
        print("   ✅ DatabaseManager імпортовано")
        
        from config.constants import PUSH_START_DATE, TARGET_APPS
        print("   ✅ Константи імпортовано")
        
        # Тестуємо src
        from src.database import PushDatabase  
        print("   ✅ PushDatabase імпортовано")
        
        from src.data_loader import DataLoader
        print("   ✅ DataLoader імпортовано")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Помилка: {e}")
        return False

def test_objects_creation():
    """Тест створення об'єктів"""
    print("\n🏗️ Тестування створення об'єктів...")
    
    try:
        from src.database import PushDatabase
        from src.data_loader import DataLoader
        
        # Створюємо об'єкти без підключення до БД
        db = PushDatabase(cache_enabled=False)
        loader = DataLoader(cache_enabled=False)
        
        print("   ✅ Об'єкти створено успішно")
        return True
        
    except Exception as e:
        print(f"   ❌ Помилка створення об'єктів: {e}")
        return False

def test_constants():
    """Тест роботи констант"""
    print("\n📋 Тестування констант...")
    
    try:
        from config.constants import (
            PUSH_START_DATE, 
            TARGET_APPS, 
            get_country_tier,
            TIER_1_COUNTRIES
        )
        
        print(f"   📅 Дати: {PUSH_START_DATE}")
        print(f"   📱 Застосунки: {TARGET_APPS}")
        print(f"   🌍 Tier 1: {TIER_1_COUNTRIES[:3]}...")
        
        # Тестуємо функцію tier
        tier = get_country_tier('US')
        print(f"   🌎 US -> {tier}")
        
        print("   ✅ Константи працюють")
        return True
        
    except Exception as e:
        print(f"   ❌ Помилка констант: {e}")
        return False

def main():
    """Головна функція"""
    print("🚀 Швидкий тест системи push-аналізу")
    print("=" * 45)
    
    tests = [
        test_basic_imports,
        test_objects_creation, 
        test_constants
    ]
    
    results = [test() for test in tests]
    passed = sum(results)
    total = len(results)
    
    print("\n" + "=" * 45)
    print(f"📊 Результат: {passed}/{total} тестів пройдено")
    
    if passed == total:
        print("🎉 Базова система працює!")
        print("\n🚀 Тепер можеш:")
        print("   1. python test_system.py - повний тест")
        print("   2. jupyter notebook - запуск notebook")
        print("   3. Перейти до аналізу даних")
    else:
        print("⚠️ Є проблеми з налаштуванням")
        print("🔧 Перевір структуру файлів проекту")

if __name__ == "__main__":
    main()