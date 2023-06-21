"""Support for Comwatt devices connected to a Comwatt Gen4 Box."""
import asyncio

from .const import DATA_COORDINATOR, DOMAIN

DATA_LISTENER = "listener"
DOMAIN = "comwatt_myenergy"

async def async_setup(hass, config):
    """Set up the Comwatt My Energy component."""
    # hass.data[DOMAIN] = {DATA_COORDINATOR: {}, DATA_LISTENER: {}}
    return True
