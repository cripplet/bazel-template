import pkgutil

for importer, modname, ispkg in pkgutil.walk_packages(path=None, onerror=lambda x: None):
    print(modname)

import requests

print(dir(requests))
