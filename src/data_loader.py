import os
import sys
# Додаємо кореневу директорію проекту до sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import pandas as pd
from config.database_config import DatabaseManager
from config.constants import *

class DataLoader:
    """Клас для завантаження даних з баз"""
    
    def __init__(self):
        self.db = DatabaseManager()
    
    def load_push_data(self) -> pd.DataFrame:
        """Завантажити дані про push-и"""
        query = f"""
        SELECT 
            toString(d.gadid) as gadid,
            d.tag as ab_group,
            d.country_name as country,
            COUNT(*) as push_count,
            MIN(e.created_at) as first_push,
            MAX(e.created_at) as last_push
        FROM event e
        JOIN device d ON e.device_id = d.id
        WHERE e.event_type = {PUSH_EVENT_TYPE}
          AND e.type = {ANDROID_TYPE}
          AND d.gadid IS NOT NULL
          AND d.tag IS NOT NULL
          AND toDate(e.created_at) >= '{PUSH_START_DATE}'
          AND toDate(e.created_at) <= '{PUSH_END_DATE}'
        GROUP BY gadid, ab_group, country
        ORDER BY push_count DESC
        """
        
        client = self.db.connect_statistic()
        return self.db.query_to_df(client, query)
    
    def load_conversion_data(self, campaign_ids: list = None) -> pd.DataFrame:
        """Завантажити дані про конверсії"""
        where_campaign = ""
        if campaign_ids:
            ids_filter = ','.join(map(str, campaign_ids))
            where_campaign = f"AND campaign_id IN ({ids_filter})"
        
        query = f"""
        SELECT 
            sub_id_14 as gadid,
            SUM(is_sale) as total_deposits,
            SUM(is_lead) as total_registrations,
            MIN(datetime) as first_conversion,
            MAX(datetime) as last_conversion,
            COUNT(*) as conversion_events
        FROM keitaro_clicks
        WHERE sub_id_14 IS NOT NULL 
          AND sub_id_14 != ''
          AND date_key >= '{CONVERSION_START_DATE}'
          AND date_key <= '{CONVERSION_END_DATE}'
          {where_campaign}
          AND (is_sale > 0 OR is_lead > 0)
        GROUP BY gadid
        """
        
        client = self.db.connect_keitaro()
        return self.db.query_to_df(client, query)
    
    def find_campaign_groups(self) -> list:
        """Знайти групи кампаній"""
        query = """
        SELECT id, name, alias, state
        FROM keitaro_campaigns
        WHERE name IS NOT NULL 
        ORDER BY name
        LIMIT 100
        """
        
        client = self.db.connect_keitaro()
        df = self.db.query_to_df(client, query)
        
        found_ids = []
        for app in TARGET_APPS:
            mask = (
                df['name'].str.contains(app, case=False, na=False) |
                df['alias'].str.contains(app, case=False, na=False)
            )
            found_ids.extend(df[mask]['id'].tolist())
        
        return list(set(found_ids))