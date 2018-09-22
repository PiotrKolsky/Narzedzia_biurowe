
import pandas as pd
import os
#os.chdir('/home/sas/Zasoby/Python/Robocze/GitHub')

# Wczytanie adresów restauracji
tables = pd.read_html("http://www.e-warszawa.com/restauracje/spis.php")
tables_cut = tables[1:77]
df =pd.DataFrame(columns=['Nazwa', 'Adres', 'Specjalnosc'])
for i in range(len(tables_cut)):
    df.loc[i]=[tables_cut[i][0][0], tables_cut[i][1][0], tables_cut[i][2][0]]

# ręczna korekta nazw ulic
df['Adres'][df[df['Adres'] == 'ul. Agrykoli 1']['Adres'].index[0]] = 'Agrykola 1'
df['Adres'][df[df['Adres'] == 'pl. Teatralny 1']['Adres'].index[0]] = 'Teatralny 1'
df['Adres'][df[df['Adres'] == 'ul. E. Plater 28']['Adres'].index[0]] = 'Plater 28'

# Dołączenie współrzędnych GPS
from geopy.geocoders import Nominatim

geolocator = Nominatim()
df['Lat'] = 'NA' ; df['Lng'] = 'NA'
for i in range(len(df)):
    #print(i)
    location = geolocator.geocode(str(df.iloc[i,1]).strip('ul. ') + ' Warszawa Poland')
    try:
        df['Lat'][i] = location.latitude
        df['Lng'][i] = location.longitude
    except:
        pass

# Wykonanie mapy
import folium

m = folium.Map(location=[52.23, 21], zoom_start=13)
for i in range(0, len(df)):
    folium.Marker([df.iloc[i]['Lat'], df.iloc[i]['Lng']],
    popup = df.iloc[i]['Nazwa'] + str(df.iloc[i]['Adres']) + df.iloc[i]['Specjalnosc'],
    icon = folium.Icon(color='cadetblue', icon=None)).add_to(m)
m.save('Restauracje.html')
##########################
