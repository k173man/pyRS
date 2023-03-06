from pydataset import data
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd
import seaborn as sns



# data_df = data()
# data_df.to_excel('data/data.xlsx')

cars93 = data('Cars93')
col_names = np.asarray([
    'mfgr', 'model', 'type', 'min_price', 'price', 'max_price', 'mpg_city', 
    'mpg_highway', 'airbags', 'drivetrain', 'cylinders', 'engine_size', 
    'horsepower', 'rpm', 'rev_per_mile', 'man_trans_avail', 'fuel_tank_capacity', 
    'passengers', 'length', 'wheelbase', 'width', 'turn_circle', 'rear_seat_room', 
    'luggage_room', 'weight', 'origin', 'make'
    ])
cars93.columns = col_names

origin_cnt = cars93.groupby('origin').size()
plt.pie(origin_cnt, labels = origin_cnt.index, autopct='%.1f')
plt.show()