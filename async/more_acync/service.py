
from typing import Protocol
import uuid
from message import Message, MessageType
import asyncio 

def generate_id():
    return str(uuid.uuid4())

class Device(Protocol):
    
    async def connect(self)->None:
        ...

    async def disconnect(self)->None:
        ...

    async def send_message(self,message_type:MessageType,data:str)->None:
        ...

class IOTService:

    def __init__(self) -> None:
        self.devices :dict[str,Device] = {}

    async def register_device(self,device:Device):
        await device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    def unregister_device(self,device_id:str):
        self.devices.pop(device_id)

    def get_device(self,device_id:str):
        return self.devices.get(device_id)
    
    async def run_program(self,program:list[Message]):
        print("=======RUNNING PROGRAM=========")
        for msg in program:
            await self.send_message(msg)
        print("=======END OF PROGRAM=========")

    async def send_message(self,msg:Message):

        await self.devices.get(msg.device_id).send_message(msg.msg_type,msg.data)