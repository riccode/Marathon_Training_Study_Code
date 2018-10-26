import pandas as pd
import logging
log = logging.getLogger(__name__)

def clean_garmin_fit_data(filename):
    data = pd.read_csv(filename, encoding="utf-8")
    data = data.fillna(0)
    col_order = ['record.timestamp[s]', 'record.position_lat[semicircles]',
     'record.position_long[semicircles]', 'record.distance[m]',
     'record.altitude[m]', 'record.speed[m/s]', 'record.unknown',
     'record.heart_rate[bpm]', 'record.cadence[rpm]',
     'record.fractional_cadence[rpm]']
    data_to_write= data[col_order]

    data_to_write.to_csv(filename, sep=',', index=False)
    log.info('Written clean data')
