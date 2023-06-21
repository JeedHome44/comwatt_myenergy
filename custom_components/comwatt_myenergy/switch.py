"""Interrupteurs pour l'intégration de la box Comwatt My Energy et des prises connectées Wi-Fi."""

from homeassistant.helpers.entity import ToggleEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurer les interrupteurs de Comwatt My Energy et des prises connectées Wi-Fi."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    switches = []

    # Interrupteur pour le ballon d'eau chaude
    switches.append(ComwattGen4WaterHeaterSwitch(data))

    # Interrupteurs pour les prises connectées Wi-Fi
    for outlet in data['outlets']:
        switches.append(WifiOutletSwitch(data, outlet))

    async_add_entities(switches)

class ComwattMyEnergyWaterHeaterSwitch(ToggleEntity):
    """Interrupteur pour le ballon d'eau chaude de Comwatt My Energy."""

    def __init__(self, data):
        """Initialiser l'interrupteur."""
        self._data = data
        self._state = False

    @property
    def name(self):
        """Nom de l'interrupteur."""
        return "Ballon d'eau chaude"

    @property
    def is_on(self):
        """Vérifier si l'interrupteur est allumé."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Allumer le ballon d'eau chaude."""
        # Code pour allumer le ballon d'eau chaude via la box Comwatt Gen4
        self._state = True

    async def async_turn_off(self, **kwargs):
        """Éteindre le ballon d'eau chaude."""
        # Code pour éteindre le ballon d'eau chaude via la box Comwatt Gen4
        self._state = False

class WifiOutletSwitch(ToggleEntity):
    """Interrupteur pour une prise connectée Wi-Fi."""

    def __init__(self, data, outlet):
        """Initialiser l'interrupteur."""
        self._data = data
        self._outlet = outlet
        self._state = False

    @property
    def name(self):
        """Nom de l'interrupteur."""
        return f"Prise {self._outlet}"

    @property
    def is_on(self):
        """Vérifier si l'interrupteur est allumé."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Allumer la prise connectée Wi-Fi."""
        # Code pour allumer la prise connectée Wi-Fi spécifiée
        self._state = True

    async def async_turn_off(self, **kwargs):
        """Éteindre la prise connectée Wi-Fi."""
        # Code pour éteindre la prise connectée Wi-Fi spécifiée
        self._state = False
