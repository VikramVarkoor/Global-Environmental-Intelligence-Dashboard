# Global Environmental Intelligence Dashboard

A cloud-integrated diagnostic tool that interfaces with **RESTful API** endpoints to monitor urban air quality and environmental health in real-time. This project demonstrates proficiency in asynchronous web services, JSON data parsing, and high-level data visualization.

## Overview
As urban environments face increasing pollution challenges, real-time monitoring is critical for public health. This dashboard:
1. **Connects** to the OpenWeatherMap Global API.
2. **Parses** complex JSON payloads containing multi-spectral gas concentrations.
3. **Visualizes** pollutant data (CO, NO2, O3, PM2.5, PM10) into actionable analytics.

---

## Technical Stack
* **Language:** Python 3.13
* **Protocol:** REST API (HTTP GET requests)
* **Libraries:** * `Requests`: For handling cloud server handshakes and data retrieval.
    * `Matplotlib`: For generating high-fidelity analytical bar charts.
* **Data Format:** JSON (JavaScript Object Notation).

---

## Analytics Breakdown
The dashboard monitors key **Air Quality Index (AQI)** components:
* **Carbon Monoxide (CO):** Indicator of vehicle emissions and combustion.
* **Ozone (O3):** Ground-level pollutant affecting respiratory health.
* **Particulate Matter (PM2.5 & PM10):** Fine particles critical for urban air quality assessment.



---

## Demonstration

<img width="1512" height="982" alt="Screenshot 2025-12-23 at 3 11 03 PM" src="https://github.com/user-attachments/assets/ffec33dc-ccd3-4862-9acd-2fd6efa3e427" />

---

## Installation & Setup
1. **API Key:** Sign up for a free key at [OpenWeatherMap](https://openweathermap.org/api).
2. **Dependencies:**
   ```bash
   pip install requests matplotlib
