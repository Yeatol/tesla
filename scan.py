import asyncio
from bleak import BleakScanner
from tesla_fleet_api import TeslaBluetooth

async def main():
    scanner = BleakScanner()
    devices = await scanner.discover()
    for device in devices:
        if TeslaBluetooth().valid_name(device.name):
            print(f"Found Tesla vehicle: {device.name}")

asyncio.run(main())
