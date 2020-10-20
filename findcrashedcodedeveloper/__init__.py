"""Find developer responsible for crashed code

See https://github.com/karambir252/findthedeveloper/ for more information
"""
import importlib_resources as _resources
try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser


__version__ = "0.1.0"

# Read Github URL from config file
_cfg = _ConfigParser()
with _resources.path("findcrashedcodedeveloper", "config.cfg") as _path:
    _cfg.read(str(_path))
GITHUB_API_SERVER_URL = _cfg.get("github", "api_server_url")
SENTRY_URL = _cfg.get("sentry", "url")
