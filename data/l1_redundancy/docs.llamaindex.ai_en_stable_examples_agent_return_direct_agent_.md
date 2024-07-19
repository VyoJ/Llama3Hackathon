Title: Controlling Agent Reasoning Loop with Return Direct Tools

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/

Markdown Content:
Controlling Agent Reasoning Loop with Return Direct Tools - LlamaIndex


All tools have an option for `return_direct` -- if this is set to `True`, and the associated tool is called (without any other tools being called), the agent reasoning loop is ended and the tool output is returned directly.

This can be useful for speeding up response times when you know the tool output is good enough, to avoid the agent re-writing the response, and for ending the reasoning loop.

This notebook walks through a notebook where an agent needs to gather information from a user in order to make a restaurant booking.

In \[ \]:

Copied!

!pip install llama\-index\-core llama\-index\-llms\-anthropic

!pip install llama-index-core llama-index-llms-anthropic

In \[ \]:

Copied!

import os

os.environ\["ANTHROPIC\_API\_KEY"\] \= "sk-ant-..."

import os os.environ\["ANTHROPIC\_API\_KEY"\] = "sk-ant-..."

Tools setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/#tools-setup)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from typing import Optional

from llama\_index.core.tools import FunctionTool
from llama\_index.core.bridge.pydantic import BaseModel

\# we will store booking under random IDs
bookings \= {}

\# we will represent and track the state of a booking as a Pydantic model
class Booking(BaseModel):
    name: Optional\[str\] \= None
    email: Optional\[str\] \= None
    phone: Optional\[str\] \= None
    date: Optional\[str\] \= None
    time: Optional\[str\] \= None

def get\_booking\_state(user\_id: str) \-> str:
    """Get the current state of a booking for a given booking ID."""
    try:
        return str(bookings\[user\_id\].dict())
    except:
        return f"Booking ID {user\_id} not found"

def update\_booking(user\_id: str, property: str, value: str) \-> str:
    """Update a property of a booking for a given booking ID. Only enter details that are explicitly provided."""
    booking \= bookings\[user\_id\]
    setattr(booking, property, value)
    return f"Booking ID {user\_id} updated with {property} = {value}"

def create\_booking(user\_id: str) \-> str:
    """Create a new booking and return the booking ID."""
    bookings\[user\_id\] \= Booking()
    return "Booking created, but not yet confirmed. Please provide your name, email, phone, date, and time."

def confirm\_booking(user\_id: str) \-> str:
    """Confirm a booking for a given booking ID."""
    booking \= bookings\[user\_id\]

    if booking.name is None:
        raise ValueError("Please provide your name.")

    if booking.email is None:
        raise ValueError("Please provide your email.")

    if booking.phone is None:
        raise ValueError("Please provide your phone number.")

    if booking.date is None:
        raise ValueError("Please provide the date of your booking.")

    if booking.time is None:
        raise ValueError("Please provide the time of your booking.")

    return f"Booking ID {user\_id} confirmed!"

\# create tools for each function
get\_booking\_state\_tool \= FunctionTool.from\_defaults(fn\=get\_booking\_state)
update\_booking\_tool \= FunctionTool.from\_defaults(fn\=update\_booking)
create\_booking\_tool \= FunctionTool.from\_defaults(
    fn\=create\_booking, return\_direct\=True
)
confirm\_booking\_tool \= FunctionTool.from\_defaults(
    fn\=confirm\_booking, return\_direct\=True
)

from typing import Optional from llama\_index.core.tools import FunctionTool from llama\_index.core.bridge.pydantic import BaseModel # we will store booking under random IDs bookings = {} # we will represent and track the state of a booking as a Pydantic model class Booking(BaseModel): name: Optional\[str\] = None email: Optional\[str\] = None phone: Optional\[str\] = None date: Optional\[str\] = None time: Optional\[str\] = None def get\_booking\_state(user\_id: str) -> str: """Get the current state of a booking for a given booking ID.""" try: return str(bookings\[user\_id\].dict()) except: return f"Booking ID {user\_id} not found" def update\_booking(user\_id: str, property: str, value: str) -> str: """Update a property of a booking for a given booking ID. Only enter details that are explicitly provided.""" booking = bookings\[user\_id\] setattr(booking, property, value) return f"Booking ID {user\_id} updated with {property} = {value}" def create\_booking(user\_id: str) -> str: """Create a new booking and return the booking ID.""" bookings\[user\_id\] = Booking() return "Booking created, but not yet confirmed. Please provide your name, email, phone, date, and time." def confirm\_booking(user\_id: str) -> str: """Confirm a booking for a given booking ID.""" booking = bookings\[user\_id\] if booking.name is None: raise ValueError("Please provide your name.") if booking.email is None: raise ValueError("Please provide your email.") if booking.phone is None: raise ValueError("Please provide your phone number.") if booking.date is None: raise ValueError("Please provide the date of your booking.") if booking.time is None: raise ValueError("Please provide the time of your booking.") return f"Booking ID {user\_id} confirmed!" # create tools for each function get\_booking\_state\_tool = FunctionTool.from\_defaults(fn=get\_booking\_state) update\_booking\_tool = FunctionTool.from\_defaults(fn=update\_booking) create\_booking\_tool = FunctionTool.from\_defaults( fn=create\_booking, return\_direct=True ) confirm\_booking\_tool = FunctionTool.from\_defaults( fn=confirm\_booking, return\_direct=True )

A user has walked in! Let's help them make a booking[¶](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/#a-user-has-walked-in-lets-help-them-make-a-booking)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic
from llama\_index.core.llms import ChatMessage
from llama\_index.core.agent import FunctionCallingAgentWorker

llm \= Anthropic(model\="claude-3-sonnet-20240229", temperature\=0.1)

user \= "user123"
prefix\_messages \= \[
    ChatMessage(
        role\="system",
        content\=(
            f"You are now connected to the booking system and helping {user} with making a booking. "
            "Only enter details that the user has explicitly provided. "
            "Do not make up any details."
        ),
    )
\]

worker \= FunctionCallingAgentWorker(
    tools\=\[
        get\_booking\_state\_tool,
        update\_booking\_tool,
        create\_booking\_tool,
        confirm\_booking\_tool,
    \],
    llm\=llm,
    prefix\_messages\=prefix\_messages,
    max\_function\_calls\=10,
    allow\_parallel\_tool\_calls\=False,
    verbose\=True,
)

agent \= worker.as\_agent()

from llama\_index.llms.anthropic import Anthropic from llama\_index.core.llms import ChatMessage from llama\_index.core.agent import FunctionCallingAgentWorker llm = Anthropic(model="claude-3-sonnet-20240229", temperature=0.1) user = "user123" prefix\_messages = \[ ChatMessage( role="system", content=( f"You are now connected to the booking system and helping {user} with making a booking. " "Only enter details that the user has explicitly provided. " "Do not make up any details." ), ) \] worker = FunctionCallingAgentWorker( tools=\[ get\_booking\_state\_tool, update\_booking\_tool, create\_booking\_tool, confirm\_booking\_tool, \], llm=llm, prefix\_messages=prefix\_messages, max\_function\_calls=10, allow\_parallel\_tool\_calls=False, verbose=True, ) agent = worker.as\_agent()

In \[ \]:

Copied!

response \= agent.chat("Hello! I would like to make a booking, around 5pm?")

response = agent.chat("Hello! I would like to make a booking, around 5pm?")

Added user message to memory: Hello! I would like to make a booking, around 5pm?

Okay, let's create a new booking for you. To do that, I'll invoke the create\_booking tool with your user ID:

Calling function: create\_booking with args: {"user\_id": "user123"}

Booking created, but not yet confirmed. Please provide your name, email, phone, date, and time.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Booking created, but not yet confirmed. Please provide your name, email, phone, date, and time.

Perfect, we can see the function output was retruned directly, with no modification or final LLM call!

In \[ \]:

Copied!

response \= agent.chat("Sure! My name is Logan, and my email is test@gmail.com")

response = agent.chat("Sure! My name is Logan, and my email is test@gmail.com")

Added user message to memory: Sure! My name is Logan, and my email is test@gmail.com

Got it, thanks for providing your name and email. Let me update the booking with those details:

Calling function: update\_booking with args: {"user\_id": "user123", "property": "name", "value": "Logan"}

Booking ID user123 updated with name = Logan

Calling function: update\_booking with args: {"user\_id": "user123", "property": "email", "value": "test@gmail.com"}

Booking ID user123 updated with email = test@gmail.com

I still need your phone number, date, and preferred time for the booking. Please provide those details.

In \[ \]:

Copied!

print(str(response))

print(str(response))

assistant: I still need your phone number, date, and preferred time for the booking. Please provide those details.

In \[ \]:

Copied!

response \= agent.chat(
    "Right! My phone number is 1234567890, the date of the booking is April 5, at 5pm."
)

response = agent.chat( "Right! My phone number is 1234567890, the date of the booking is April 5, at 5pm." )

Added user message to memory: Right! My phone number is 1234567890, the date of the booking is April 5, at 5pm.

Great, thank you for providing the remaining details. Let me update the booking:

Calling function: update\_booking with args: {"user\_id": "user123", "property": "phone", "value": "1234567890"}

Booking ID user123 updated with phone = 1234567890

Calling function: update\_booking with args: {"user\_id": "user123", "property": "date", "value": "2023-04-05"}

Booking ID user123 updated with date = 2023-04-05

Calling function: update\_booking with args: {"user\_id": "user123", "property": "time", "value": "17:00"}

Booking ID user123 updated with time = 17:00

Your booking for April 5th at 5pm is now created with all the provided details. To confirm it, I'll invoke:

Calling function: confirm\_booking with args: {"user\_id": "user123"}

Booking ID user123 confirmed!

In \[ \]:

Copied!

print(str(response))

print(str(response))

Booking ID user123 confirmed!

In \[ \]:

Copied!

print(bookings\["user123"\])

print(bookings\["user123"\])

name='Logan' email='test@gmail.com' phone='1234567890' date='2023-04-05' time='17:00'

Back to top

[Previous ReAct Agent with Query Engine (RAG) Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)[Next Structured Planning Agent](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)

Hi, how can I help you?

🦙
