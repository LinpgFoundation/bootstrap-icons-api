from os import path as PATH
from typing import Final

# the path of the dir that stores all the icon images
_PATH: Final[str] = PATH.join(PATH.dirname(__file__), "icons")


# get the path of image for given icon
def get_icon_path(name: str) -> str:
    return PATH.join(_PATH, f"{name}.svg")
