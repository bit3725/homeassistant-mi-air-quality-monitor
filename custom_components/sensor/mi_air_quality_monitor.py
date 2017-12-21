"""Support for Xiaomi air quality monitor."""
import logging

from homeassistant.const import (CONF_NAME, CONF_HOST, CONF_TOKEN, )
from homeassistant.helpers.entity import Entity
from homeassistant.exceptions import PlatformNotReady

_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['python-miio>=0.3.2']

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Perform the setup for Xiaomi air quality monitor."""
    from miio import AirQualityMonitor, DeviceException

    host = config.get(CONF_HOST)
    name = config.get(CONF_NAME)
    token = config.get(CONF_TOKEN)

    _LOGGER.info("Initializing Xiaomi air quality monitor with host %s (token %s...)", host, token[:5])

    devices = []
    try:
        airQualityMonitor = AirQualityMonitor(host, token)
        airQualityMonitorSensor = XiaomiAirQualityMonitorSensor(airQualityMonitor, name)
        devices.append(airQualityMonitorSensor)
    except DeviceException:
        raise PlatformNotReady

    add_devices(devices)

class XiaomiAirQualityMonitorSensor(Entity):
    """Representation of a XiaomiAirQualityMonitorSensor."""

    def __init__(self, airQualityMonitor, name):
        """Initialize the XiaomiAirQualityMonitorSensor."""
        self._state = None
        self._name = name
        self._airQualityMonitor = airQualityMonitor
        self.parse_data()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:cloud'

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return 'AQI'

    @property
    def device_state_attributes(self):
        """Return the state attributes of the last update."""
        attrs = {}
        attrs['Battery'] = '{}%'.format(self._airQualityMonitor.status().battery)
        attrs['USB Power'] = 'On' if self._airQualityMonitor.status().usb_power else 'Off'

        return attrs

    def parse_data(self):
        try:
            self._state = self._airQualityMonitor.status().aqi
        except DeviceException:
            _LOGGER.exception('Fail to get aqi from Xiaomi Air Quality Monitor')
            raise PlatformNotReady

    def update(self):
        """Get the latest data and updates the states."""
        self.parse_data()
