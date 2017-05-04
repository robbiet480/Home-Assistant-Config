"""
Provides a sensor that exposes room sensors from Hello Sense.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/sensor.sense/
"""
import logging
import requests
from datetime import timedelta

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_NAME, TEMP_CELSIUS, CONF_RESOURCES)
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = 'Sense'

DEFAULT_RESOURCES = ['temperature', 'humidity', 'light', 'sound',
                     'particulates']

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)

CONF_ACCESS_TOKEN = 'access_token'

SENSOR_TYPES = {
    'temperature': ['Room temperature', TEMP_CELSIUS, 'mdi:temperature'],
    'humidity': ['Room humidity', '%', 'mdi:water-percent'],
    'light': ['Room light', 'lux', 'mdi:flashlight'],
    'sound': ['Room sound', 'dB', 'mdi:speaker'],
    'particulates': ['Room particulates', 'µg/m³', 'mdi:broom'],
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ACCESS_TOKEN): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_RESOURCES, default=DEFAULT_RESOURCES):
        vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Sense sensors."""
    name = config.get(CONF_NAME)
    access_token = config.get(CONF_ACCESS_TOKEN)

    data = PySenseData(access_token)

    if data.status is None:
        _LOGGER.error("Sense Sensor has no data, unable to setup")
        return False

    _LOGGER.debug('Sense Sensors Available: %s', data.status)

    entities = []

    for resource in config[CONF_RESOURCES]:
        sensor_type = resource.lower()

        if sensor_type in data.status:
            entities.append(SenseSensor(name, data, sensor_type))
        else:
            _LOGGER.warning(
                "Sensor type: %s does not appear in the Sense status "
                "output, cannot add", sensor_type)

    data.update(no_throttle=True)

    add_entities(entities)


class SenseSensor(Entity):
    """Representation of a sensor entity for Sense status values."""

    def __init__(self, name, data, sensor_type):
        """Initialize the sensor."""
        self._data = data
        self.type = sensor_type
        self._name = "{} {}".format(name, SENSOR_TYPES[sensor_type][0])
        self._unit = SENSOR_TYPES[sensor_type][1]
        self.update()

    @property
    def name(self):
        """Return the name of the Sense sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return SENSOR_TYPES[self.type][2]

    @property
    def state(self):
        """Return entity state from Sense."""
        return self._state['value']

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit

    @property
    def device_state_attributes(self):
        """Return the sensor attributes."""
        allowed_keys = ['ideal_conditions', 'condition', 'message']
        return {i: self._state[i].replace('**', '') for i in self._state
                if i in allowed_keys}

    def update(self):
        """Get the latest status and use it to update our sensor state."""
        if self._data.status is None:
            self._state = None
            return

        if self.type not in self._data.status:
            self._state = None
        else:
            self._state = self._data.status[self.type]


class PySenseData(object):
    """Stores the data retrieved from Sense.

    For each entity to use, acts as the single point responsible for fetching
    updates from the server.
    """

    def __init__(self, access_token):
        """Initialize the data oject."""
        self._access_token = access_token
        self._status = None

    @property
    def status(self):
        """Get latest update if throttle allows. Return status."""
        self.update()
        return self._status

    def _get_status(self):
        """Get the room status from Sense."""
        response = requests.get(
            "https://api.hello.is/v1/room/current?temp_unit=f", timeout=10,
            headers={"Authorization": "Bearer {}".format(self._access_token)})
        if response.status_code == 401:
            raise RuntimeError("Invalid access token")
        elif response.status_code != 200:
            _LOGGER.error("Invalid HTTP response: %s", response.status_code)
            return
        return response.json()

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self, **kwargs):
        """Fetch the latest status from Sense."""
        self._status = self._get_status()

