import pandas as pd
from isochrones.cluster import StarCatalog

df = pd.read_csv('../../data/k2_input_isochrones.csv', index_col='id')
df['parallax'] *= 1000
df['parallax_unc'] *= 1000
bands = ['g', 'r', 'J', 'H', 'K', 'Bp', 'Rp']  #, 'B', 'V']
k2cat = StarCatalog(df, props=['parallax'], bands=bands)
k2cat.write_ini(root='../../results/isochrones')
