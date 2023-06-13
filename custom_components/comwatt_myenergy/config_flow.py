"""Define a config flow manager for Comwatt My Energy."""
import logging

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

# component library
from .const import (
    CONF_ATOME_SITE_CODE,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

COMWATT_MYENERGY_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
    }
)

