from pathlib import Path

from kospet_watchface_studio.explorer import WatchfacePackage

package = WatchfacePackage.open(Path("DM.zip"))

print(package.name)

print(package.assets)

print(package.app_json)

print(package.app_js)