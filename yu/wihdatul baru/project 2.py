# Impor modul
import requests
import pandas as pd

# Mengubah deskripsi cuaca menjadi bahasa Indonesia
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds': 'berawan sebagian',
    'broken clouds': 'berawan',
    'overcast clouds': 'mendung',
    'moderate rain': 'hujan sedang',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',
    'rain': 'hujan',
    'thunderstorm': 'badai petir',
    'snow': 'salju',
    'mist': 'kabut'
}

# Fungsi untuk mengambil data cuaca
def ambil_data_cuaca(kota, api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

# Fungsi untuk menganalisis cuaca
def analisis_cuaca(data):
    if data is None:
        return None

    forecast_list = data.get('list', [])
    dates = []
    temperatures = []
    humidities = []
    weather_descriptions = []

    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]
        dates.append(date)
        temperatures.append(item['main']['temp'])
        humidities.append(item['main']['humidity'])
        desc = item['weather'][0]['description']
        weather_descriptions.append(deskripsi_cuaca_id.get(desc, desc))

    df = pd.DataFrame({
        'Tanggal': dates,
        'Suhu (K)': temperatures,
        'Kelembapan (%)': humidities,
        'Deskripsi Cuaca': weather_descriptions
    })

    df['Suhu (C)'] = df['Suhu (K)'] - 273.15
    df = df.drop(columns=['Suhu (K)'])

    df_daily = df.groupby('Tanggal').agg({
        'Suhu (C)': 'mean',
        'Kelembapan (%)': 'mean',
        'Deskripsi Cuaca': lambda x: x.mode()[0]
    }).reset_index()

    df_daily.index = df_daily.index + 1
    return df_daily

# Fungsi utama
def main():
    kota = input('Masukkan Nama Kota: ')
    api_key = '8565d5c18ade527e24b912d42e28d6f6'

    data = ambil_data_cuaca(kota, api_key)
    df = analisis_cuaca(data)

    if df is not None:
        print(df.head())

if __name__ == '_main_':
    main()