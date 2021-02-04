import asyncio
from six.moves import input
from azure.iot.device.aio import IoTHubDeviceClient


async def main():
    device_client = IoTHubDeviceClient.create_from_connection_string("HostName=YOURAZUREACCOUNT.azure-devices.net;DeviceId=Pi_Envirnoment;SharedAccessKey=YOURSHAREDACCESSKEY")

    await device_client.connect()

    async def twin_patch_listener(device_client):
        while True:
            patch = await device_client.receive_twin_desired_properties_patch()  # blocking call
            print("the data in the desired properties patch was: {}".format(patch))

    def quit_listener():
        while True:
            selection = input("Press Q to quit\n")
            if selection == "Q" or selection == "q":
                print("Quitting...")
                break

    asyncio.create_task(twin_patch_listener(device_client))

    loop = asyncio.get_running_loop()
    user_finished = loop.run_in_executor(None, quit_listener)

    await user_finished

    await device_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
