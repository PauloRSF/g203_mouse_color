# g203_mouse_color

A simple CLI to change the color on Logitech's G203 gaming mouse

## Why?

Because i don't like having to install Logitech's G Hub just to switch my goddamn mouse colors

## Requirements

You only need to install PyUSB: `pip install pyusb`

## Usage

```
usage: g203_mouse_color.py [-h] [--mode {fixed,oscillate}] [--osc-period VALUE] COLOR

Set the lighting mode and color of the Logitech G203 mouse.

positional arguments:
  COLOR                     the desired color RGB hex code (Ex.: F0B1C3)

optional arguments:
  -h, --help                show this help message and exit
  --mode {fixed,oscillate}  set the lighting mode
  --osc-period VALUE        set the oscillating period in "oscillate" mode (0-65535)

```
