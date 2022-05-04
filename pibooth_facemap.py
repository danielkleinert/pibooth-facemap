import io

import PIL.Image
import pibooth
from pibooth.utils import LOGGER
from facemap import age_image

__version__ = "1.0.0"

@pibooth.hookimpl
def pibooth_setup_picture_factory(cfg, opt_index, factory):
    try:
        LOGGER.info("aging images")
        factory._images = tuple(map(apply_filter, factory._images))
        LOGGER.info("done aging images")
    except Exception:
        LOGGER.error("error aging image:")
        raise


def apply_filter(pil_image: PIL.Image) -> PIL.Image:
    with io.BytesIO() as jpg_image:
        pil_image.save(jpg_image)
        jpg_image.name = "capture.jpg"
        jpg_image.seek(0)
        return PIL.Image.open(age_image(jpg_image))
