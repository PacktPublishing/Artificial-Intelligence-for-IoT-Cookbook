from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import (
  BotFrameworkAdapter,
  BotFrameworkAdapterSettings,
  ConversationState,
  UserState,
  MemoryStorage
  )
import asyncio
from luisbot import LuisBot

app = Flask(__name__)

loop = asyncio.get_event_loop()
botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)
memstore = MemoryStorage()
constate = ConversationState(memstore)
userstate = UserState(memstore)
botdialog = LuisBot(constate,userstate)


@app.route("/api/messages",methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        body = request.json
    else:
        return Response(status = 415)

    activity = Activity().deserialize(request.json)

    auth_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")

    async def call_fun(turncontext):
        await botdialog.on_turn(turncontext)

    task = loop.create_task(botadapter.process_activity(activity,"",call_fun))
    loop.run_until_complete(task)



if __name__ == '__main__':
    app.run('localhost',3978)
