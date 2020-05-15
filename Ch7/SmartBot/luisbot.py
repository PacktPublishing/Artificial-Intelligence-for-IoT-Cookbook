from botbuilder.ai.luis import LuisApplication,LuisPredictionOptions,LuisRecognizer
from botbuilder.core import(
ConversationState
, UserState
, TurnContext
, ActivityHandler
, RecognizerResult
, MessageFactory
)
from enum import Enum

class EnumOrder(Enum):    
    ENTREE=1
    SIDE=2
    DRINK=3
    DONE=4


class Order:
    def __init__(self):
        self.entree = ""
        self.drink=""
        self.side=""

    @property
    def Entree(self):
        return self.entre
    @Entree.setter
    def Entree(self,entree:str):
        self.entree = entree

    @property
    def Drink(self):
        return self.drink
    @Drink.setter
    def Drink(self,drink:str):
        self.drink = drink

    @property
    def Side(self):
        return self.side
    @Side.setter
    def Side(self,side:str):
        self.side = side


class ConState:
    def __init__(self):
        self.orderstatus = EnumOrder.ENTREE
    @property
    def CurrentPos(self):
        return self.orderstatus
    @CurrentPos.setter
    def EnumOrder(self,current:EnumOrder):
        self.orderstatus = current

class LuisBot(ActivityHandler):
    def __init__(self,constate:ConversationState,userstate:UserState):
        luis_app = LuisApplication("APP ID","primary starter key","https://westus.api.cognitive.microsoft.com/")
        luis_option = LuisPredictionOptions(include_all_intents=True,include_instance_data=True)
        self.LuisReg = LuisRecognizer(luis_app,luis_option,True)
        self.constate = constate
        self.userstate = userstate

        self.conprop = self.constate.create_property("constate")
        self.userprop = self.userstate.create_property("userstate")
 
    async def on_turn(self,turn_context:TurnContext):
        await super().on_turn(turn_context)
        await self.constate.save_changes(turn_context)
        await self.userstate.save_changes(turn_context)
        
    
    async def on_message_activity(self,turn_context:TurnContext):
        conmode = await self.conprop.get(turn_context,ConState)
        ordermode = await self.userprop.get(turn_context,Order)
        luis_result = await self.LuisReg.recognize(turn_context)
        intent = LuisRecognizer.top_intent(luis_result)
        await turn_context.send_activity(f"Top Intent : {intent}")
        retult = luis_result.properties["luisResult"]
        item = ''
        if len(retult.entities) != 0:
            await turn_context.send_activity(f" Luis Result {retult.entities[0]}")
            item = retult.entities[0].entity
        if(conmode.orderstatus == EnumOrder.ENTREE):
            await turn_context.send_activity("Please enter a main Entree")
            conmode.orderstatus = EnumOrder.SIDE
        elif(conmode.orderstatus == EnumOrder.SIDE):
            ordermode.entree = item
            await turn_context.send_activity("Please enter a side dish")
            conmode.orderstatus = EnumOrder.DRINK
        elif(conmode.orderstatus == EnumOrder.DRINK):
            await turn_context.send_activity("Please a drink")
            ordermode.side = item
            conmode.orderstatus = EnumOrder.DONE
        elif(conmode.orderstatus == EnumOrder.DONE):
            ordermode.drink = item
            info = ordermode.entree + " " + ordermode.side + "  " + ordermode.drink
            await turn_context.send_activity(info)
            conmode.orderstatus = EnumOrder.ENTREE
