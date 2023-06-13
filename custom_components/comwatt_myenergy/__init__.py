"""Support for Comwatt devices connected to a Comwatt Gen4 Box."""
import asyncio

from .const import DATA_COORDINATOR, DOMAIN

PLATFORMS = ["sensor"]

DATA_LISTENER = "listener"


async def async_setup(hass, config):
    """Set up the Comwatt My Energy component."""
    # hass.data[DOMAIN] = {DATA_COORDINATOR: {}, DATA_LISTENER: {}}
    return True
