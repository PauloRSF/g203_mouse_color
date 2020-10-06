import sys
import time
import struct
import argparse
import usb.core
import usb.util

tag = 'g203_mouse_color.py:'

def hid_set_report(payload):
    dev.ctrl_transfer(0x21, 0x9, 0x210, 0x1, payload)

def send_mouse_data(dev, color, mode, osc_period):
    payload = b'\x11\xff\x0e\x3d\x00' + mode + color + osc_period + b'\x00' * 9
    hid_set_report(payload)

parser = argparse.ArgumentParser(
    prog='g203_mouse_color.py',
    description='Set the lighting mode and color of the Logitech G203 mouse.'
)
parser.add_argument(
    '--mode',
    type=str,
    default='fixed',
    choices=['fixed', 'oscillate'],
    help='set the lighting mode'
)
parser.add_argument(
    '--osc-period',
    type=int,
    default=2000,
    metavar='VALUE',
    help='set the oscillating period in "oscillate" mode (0-65535)'
)
parser.add_argument(
    'color',
    type=str,
    metavar='COLOR',
    help='the desired color RGB hex code (Ex.: F0B1C3)'
)
args = parser.parse_args()

mode_map = {
    'fixed': b'\x01',
    'oscillate': b'\x03',
}

# Logitech's G203 ID -> 046D:C084
dev = usb.core.find(idVendor=0x046D, idProduct=0xC084)

if not dev:
    print(f'{tag} Device not found. Are you sure it is plugged in?')
    sys.exit(1)

if not dev.is_kernel_driver_active(1):
    dev.attach_kernel_driver(1)

if dev.is_kernel_driver_active(1):
    reattach = True
    dev.detach_kernel_driver(1)

try:
    color = bytes.fromhex(args.color)
except:
    print(f'{tag} Invalid hex color code.')
    sys.exit(2)

send_mouse_data(
    dev=dev,
    color=color,
    mode=mode_map[args.mode],
    osc_period=struct.pack('>H', args.osc_period)
)
