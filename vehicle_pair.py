import asyncio
from tesla_fleet_api import TeslaBluetooth

async def main():
    vin = "LRWYGCFJ7MC076154"
    tesla_bluetooth = TeslaBluetooth()
    private_key = await tesla_bluetooth.get_private_key()
    vehicle = tesla_bluetooth.vehicles.create(vin)
    device = await vehicle.find_vehicle()
    await vehicle.pair()
    print(f"Paired with VehicleBluetooth instance for VIN: {vehicle.vin}")

asyncio.run(main())
