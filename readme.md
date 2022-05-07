## Pibooth Facemap Plugin

This plugin filters captured images utilising the private rest api of the mobile app facemap.

### Installation

Add the plugin to your Pibooth config:

    plugins = "/Users/your_user/projects/facemap/pibooth_facemap.py"

Update `TOKEN` in `facemap.py`.

### Notes

- Token is only valid for some hours and needs to be acquired by yourself.
- Images are not resized before sending them of to the api - you probably want to do this if you are using huge dslr images that could piss of facemap.
- The plugin uses the private property `PictureFactory._images` which could brake easily.