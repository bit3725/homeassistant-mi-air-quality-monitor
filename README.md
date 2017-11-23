# homeassistant-mi-air-quality-monitor
XiaoMi Air Quality Monitor(PM2.5 sensor) component for Home Assistant.

![Screenshot](https://raw.githubusercontent.com/bit3725/homeassistant-mi-air-quality-monitor/master/images/screenshot.jpg)

## Installation
1. Copy *custom_components/sensor/mi_air_quality_moitor.py* to **.homeassistant/custom_components/sensor**.
2. Get the IP of your sensor.
3. Follow [Retrieving the Access Token](https://home-assistant.io/components/vacuum.xiaomi_miio/#retrieving-the-access-token) guide to get the token of your sensor

## Configuration
```yaml
sensor:
  - platform: mi_air_quality_monitor
    host: YOUR_SENSOR_IP
    token: YOUR_SENSOR_TOKEN
    name: YOUT_SENSOR_NAME
```
