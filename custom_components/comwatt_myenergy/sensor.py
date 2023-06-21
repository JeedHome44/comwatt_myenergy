"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import POWER_WATT
from homeassistant.const import POWER_KILO_WATT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

SENSOR_TYPES = {
    'current': ['Current', 'A'],
    'power': ['Power', 'W'],
    'voltage': ['Voltage', 'V'],
}

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurer les capteurs de Comwatt My Energy."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    sensors = []

    for sensor_type in SENSOR_TYPES:
        name = SENSOR_TYPES[sensor_type][0]
        unit = SENSOR_TYPES[sensor_type][1]
        sensors.append(ComwattMyEnergySensor(data, sensor_type, name, unit))

    async_add_entities(sensors)

class ComwattMyEnergySensor(Entity):
    """Capteur pour la box Comwatt My Energy."""

    def __init__(self, data, sensor_type, name, unit):
        """Initialiser le capteur."""
        self._data = data
        self._sensor_type = sensor_type
        self._name = name
        self._unit = unit
        self._state = None

    @property
    def name(self):
        """Nom du capteur."""
        return f"Comwatt My Energy {self._name}"

    @property
    def unique_id(self):
        """ID unique du capteur."""
        return f"comwatt_myenergy_{self._sensor_type}"

    @property
    def unit_of_measurement(self):
        """Unité de mesure du capteur."""
        return self._unit

    @property
    def state(self):
        """Valeur du capteur."""
        return self._state

    async def async_update(self):
        """Mettre à jour la valeur du capteur."""
        # Utilisez les fonctions ou les API nécessaires pour récupérer les données de la box Comwatt Gen4
        # et mettez à jour self._state avec la valeur appropriée
        self._state = 42  # Exemple de valeur statique pour illustrer
