import time
import asyncio
from tesla_fleet_api import TeslaBluetooth

async def main():
    vin = "LRWYGCFJ7MC076154"
    tesla_bluetooth = TeslaBluetooth()
    private_key = await tesla_bluetooth.get_private_key()
    vehicle = tesla_bluetooth.vehicles.create(vin)
    device = await vehicle.find_vehicle()
    print(f"Vehicle data for VIN: {vehicle.vin}")
    for i in range(100):
        data = await vehicle.vehicle_data(["charge_state", "drive_state"])
        print(data)
        time.sleep(0.5)

asyncio.run(main())
