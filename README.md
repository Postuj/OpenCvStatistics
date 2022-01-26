# OpenCv pen detector

## Project setup

To setup your project complete the following steps

## ROI setup

To set up ROIs run this script and select where you want your ROIs to be (ROIs are places when your pen will be detected). You don't need those pink cards, they were there only for me to see where I've placed ROIs xD.
```
python ./settings/roi_setter.py
```
## Mask setup

Next you have to setup color mask, for that run this script and adjust tracebars (value_min and value_max are enough in most cases) so that regions what you've picked for your ROIs are pitch black while the pen is white.
```
python ./settings/color_picker.py
```

## Run project
After running main script switch to photos app and you'll be able to controll left and right arrows with your pen.

```
python ./index.py
```