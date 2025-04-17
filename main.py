import asyncio
from tesla_fleet_api import TeslaBluetooth, BluetoothVehicleData

async def main():
    tesla_bluetooth = TeslaBluetooth()
    device = await tesla_bluetooth.find_vehicle()
    private_key = tesla_bluetooth.get_private_key("path/to/private_key.pem")
    vehicle = tesla_bluetooth.vehicles.create("<vin>")
    data = await vehicle.vehicle_data([BluetoothVehicleData.CHARGE_STATE, BluetoothVehicleData.CLIMATE_STATE])
    print(f"Vehicle data for VIN: {vehicle.vin}")
    print(data)

asyncio.run(main())
