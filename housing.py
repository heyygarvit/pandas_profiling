import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_csv('HousingData.csv')

profile = ProfileReport(df)
profile.to_file(output_file="housingData.html")



