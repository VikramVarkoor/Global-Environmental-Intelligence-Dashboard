import requests
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
API_KEY = "b64a867b29bb25c25610b33dcf092f14"  # Paste your key here
CITY = "Dubai"  # You can change this to any city


def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=25.2&lon=55.2&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['list'][0]['components']
    elif response.status_code == 401:
        print("⚠️ Error: API Key is still activating. Please wait 30 mins.")
        return None
    else:
        print(f"⚠️ Error: Server returned status {response.status_code}")
        return None


def update_dashboard():
    data = get_weather_data()

    # Check if data was actually returned
    if data is None:
        print("📊 Dashboard Standby: Waiting for API activation...")
        return

    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    # Custom colors for different gases
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#BA55D3', '#FF6347']

    plt.bar(labels, values, color=colors)
    plt.title(f"Real-Time Air Quality Analytics: {CITY}", fontsize=14, fontweight='bold')
    plt.ylabel("Concentration (μg/m³)")
    plt.xlabel("Pollutant Type")
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # Add a watermark/status box
    plt.text(0.5, 0.95, "Source: OpenWeatherMap Global API",
             transform=plt.gca().transAxes, ha='center',
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    plt.tight_layout()
    plt.show()


print(f"Accessing Global Environmental Data for {CITY}...")
update_dashboard()