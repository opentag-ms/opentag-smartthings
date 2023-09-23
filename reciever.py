import asyncio
from bleak import BleakClient, BleakScanner
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"
SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"


async def find_device(name: str):
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == name:
            print()
            print(f"Name: {device.name}")
            print(f"Address: {device.address}")
            print(f"Details: {device.details}")
            print(f"Metadata: {device.metadata}")
            print(f"RSSI: {device.rssi}")
            return device.address

mac_address = asyncio.run(find_device("OpenSchlüsselbund"))


async def run(address):
    async with BleakClient(address) as client:
        while True:
            value = await client.read_gatt_char(CHARACTERISTIC_UUID)
            print(value.decode())

asyncio.run(run(mac_address))  # Replace with your ESP32's MAC address
