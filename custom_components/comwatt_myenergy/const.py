"""Constants for Comwatt My Energy."""
from datetime import timedelta

# Tools
DEBUG_FLAG = False

# Domain name
DOMAIN = "comwatt_myenergy"

# Config flow
DATA_COORDINATOR = "coordinator"

# Conf comwatt_site_code
CONF_COMWATT_SITE_CODE = "comwatt_site_code"

# Device name
DEVICE_CONF_URL = "https://energy.comwatt.com/#/login"

# Attribution
ATTRIBUTION = "Data provided by Comwatt"

# Scan interval (avoid synchronisation to lower request per seconds on server)
LOGIN_STAT_SCAN_INTERVAL = timedelta(hours=1, minutes=30, seconds=13)

# Max error theshold
MAX_SERVER_ERROR_THRESHOLD = 5
