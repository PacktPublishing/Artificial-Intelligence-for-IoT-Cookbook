import time
import os
import sys
import asyncio
from six.moves import input
import threading
from azure.iot.device.aio import IoTHubModuleClient
from azure.iot.device import Message
import uuid


def MLCode():
    # You bispoke ML code here
    return True

async def main():
    try:
        module_client = IoTHubModuleClient.create_from_edge_environment()
        await module_client.connect()
        async def send_d2c_message(module_client):
            while True:
                msg = Message("test machine learning ")
                msg.message_id = uuid.uuid4()
                msg.custom_properties["MachineLearningBasedAlert"] = MLCode()

                await module_client.send_message_to_output(msg, "output1")

        # define behavior for halting the application
        def stdin_listener():
            while True:
                try:
                    selection = input("Press Q to quit\n")
                    if selection == "Q" or selection == "q":
                        print("Quitting...")
                        break
                except:
                    time.sleep(10)

        # Schedule task for C2D Listener
        listeners = asyncio.gather(send_d2c_message(module_client))

        print ( "The sample is now waiting for messages. ")

        # Run the stdin listener in the event loop
        loop = asyncio.get_event_loop()
        user_finished = loop.run_in_executor(None, stdin_listener)

        # Wait for user to indicate they are done listening for messages
        await user_finished

        # Cancel listening
        listeners.cancel()

        # Finally, disconnect
        await module_client.disconnect()

    except Exception as e:
        print ( "Unexpected error %s " % e )
        raise

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

