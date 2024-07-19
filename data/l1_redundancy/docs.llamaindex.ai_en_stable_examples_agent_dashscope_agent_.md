Title: DashScope Agent Tutorial - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/

Markdown Content:
DashScope Agent Tutorial - LlamaIndex


In this notebook tutorial, we will show you how to call the agent application built in the ModelStudio Platform. You can create an agent application in ModelStudio platform by referring to document: [Create application in ModelStudio.](https://help.aliyun.com/document_detail/2586405.html?spm=a2c4g.2400264.0.0.7c2e1ff58BeD83) If you open this Notebook on colab, you will probably need to install LlamaIndex 🦙 first and then install the following integration.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-dashscope

%pip install llama-index-agent-dashscope

Note: Please note that you have to get <app\_id> and <api\_key> first and then initialize an agent. For how to get , please refer to guide: [How to get API-KEY in ModelStudio](https://help.aliyun.com/document_detail/2712195.html?spm=a2c4g.2400264.0.0.7c2e1ff5tp740E).

There are two ways you can set api-key when initializing a dashscope agent.

In \[ \]:

Copied!

\# Set API key by environment variables
%env DASHSCOPE\_API\_KEY\=your\_api\_key

\# set API key by parameters
\# agent = DashScopeAgent(api\_key="your\_api\_key", app\_id="your\_app\_id")

\# Set API key by environment variables %env DASHSCOPE\_API\_KEY=your\_api\_key # set API key by parameters # agent = DashScopeAgent(api\_key="your\_api\_key", app\_id="your\_app\_id")

Simple Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/#simple-chat)
------------------------------------------------------------------------------------------------

Let's start with a simple chat by using dashscope agent.

In \[ \]:

Copied!

from llama\_index.agent.dashscope import DashScopeAgent

agent \= DashScopeAgent(
    app\_id\="your\_app\_id",  \# The id of app that you created
    chat\_session\=True,  \# Enable chat session which will auto save and pass chat                               history to LLM.
    verbose\=False,  \# If need to print more details
)

resp \= agent.chat("I want to travel to Seattle.")
print(resp.response)

from llama\_index.agent.dashscope import DashScopeAgent agent = DashScopeAgent( app\_id="your\_app\_id", # The id of app that you created chat\_session=True, # Enable chat session which will auto save and pass chat history to LLM. verbose=False, # If need to print more details ) resp = agent.chat("I want to travel to Seattle.") print(resp.response)

Great choice! Seattle is a fantastic city known for its stunning natural beauty, vibrant culture, and technology scene. Here are some key points to consider when planning your trip to Seattle:

1. \*\*Best Time to Visit\*\*: The best time to visit Seattle is from June to September when the weather is at its warmest and driest. Keep in mind that Seattle is famous for its rain, so packing a waterproof jacket is always a good idea.

2. \*\*Attractions\*\*: Don't miss out on these iconic Seattle attractions:
   - \*\*Space Needle\*\*: Take an elevator ride up for panoramic views of the city.
   - \*\*Pike Place Market\*\*: Watch the famous fish toss and explore local artisan crafts and fresh produce.
   - \*\*Seattle Center\*\*: Home to the Space Needle, Chihuly Garden and Glass, and several museums.
   - \*\*Museum of Pop Culture (MoPOP)\*\*: A must-visit for music and pop culture enthusiasts.
   - \*\*Pioneer Square\*\*: The historic heart of Seattle with underground tours and charming architecture.
   - \*\*Chihuly Garden and Glass\*\*: A stunning display of glass art by Dale Chihuly.

3. \*\*Transportation\*\*: Seattle has a good public transportation system including buses, light rail, and streetcars. Consider getting an ORCA card for easy access to public transit. Ride-sharing services like Uber and Lyft are also widely available.

4. \*\*Accommodation\*\*: Seattle offers a range of accommodations from budget-friendly hostels to luxury hotels. Popular areas to stay include Downtown, Capitol Hill, and Belltown for their proximity to attractions and nightlife.

5. \*\*Food and Drink\*\*: Seattle is famous for its coffee culture, seafood, and international cuisine. Be sure to try some fresh seafood at Pike Place Market, grab a cup of coffee from the original Starbucks, and explore the diverse food scene in neighborhoods like Capitol Hill and International District.

6. \*\*Outdoor Activities\*\*: Seattle is surrounded by natural beauty. Take a ferry to Bainbridge Island, hike in Mount Rainier National Park, or explore the lush forests of Olympic National Park.

7. \*\*Safety Tips\*\*: Like any big city, be aware of your surroundings, especially in crowded tourist areas. Keep valuables secure and use common sense when traveling at night.

Remember to check the latest COVID-19 related travel restrictions and guidelines before planning your trip. Enjoy your adventure in Seattle!

In \[ \]:

Copied!

resp \= agent.chat("Are there any tourist attractions there?")
print(resp.response)

resp = agent.chat("Are there any tourist attractions there?") print(resp.response)

Absolutely! Seattle is filled with tourist attractions that cater to a wide variety of interests. Here are just a few highlights:

1. \*\*Space Needle\*\*: This 605-foot tower offers breathtaking views of the city, Mount Rainier, Elliott Bay, and the surrounding islands. It's an iconic symbol of Seattle.

2. \*\*Pike Place Market\*\*: One of the oldest continuously operated public farmers' markets in the U.S., famous for its flying fish, local crafts, and vibrant atmosphere.

3. \*\*Chihuly Garden and Glass\*\*: A stunning exhibit showcasing the glass artwork of Dale Chihuly, with indoor galleries and an outdoor garden integrated with his colorful, large-scale sculptures.

4. \*\*Museum of Pop Culture (MoPOP)\*\*: A museum dedicated to contemporary popular culture, featuring exhibits on music, science fiction, and pop culture artifacts.

5. \*\*Seattle Aquarium\*\*: Located on Pier 59, it offers a chance to get up close with marine life from the Puget Sound and beyond.

6. \*\*Seattle Great Wheel\*\*: A giant Ferris wheel on Pier 57, providing a unique perspective of the city skyline and waterfront.

7. \*\*Seattle Art Museum (SAM)\*\*: Houses a diverse collection of global art, including modern and ethnic works, as well as rotating exhibitions.

8. \*\*Woodland Park Zoo\*\*: Known for its naturalistic habitats and conservation efforts, this zoo is home to over 1,000 animals from around the world.

9. \*\*Seattle Waterfront\*\*: A lively area with restaurants, shops, and attractions like the Seattle Aquarium and the Great Wheel, offering picturesque views of Elliott Bay.

10. \*\*International District/Chinatown\*\*: Rich in cultural heritage, this neighborhood offers a variety of Asian cuisines, shops, and historical landmarks.

These are just a few examples; Seattle also boasts numerous parks, gardens, and outdoor spaces like Kerry Park, Discovery Park, and the Hiram M. Chittenden Locks, as well as a thriving arts and cultural scene with theaters, galleries, and live music venues.

If you want to start with new conversation, you can reset and then call chat function.

In \[ \]:

Copied!

\# reset agent
agent.reset()

resp \= agent.chat("Are there any tourist attractions there?")
print(resp.response)

\# reset agent agent.reset() resp = agent.chat("Are there any tourist attractions there?") print(resp.response)

To provide a relevant answer, I would need to know which location you are referring to. Please specify the place you are interested in, and I can then share information about tourist attractions there.

Streaming Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/#streaming-chat)
------------------------------------------------------------------------------------------------------

DashScope agent can also return response as a generator for chat, so you can stream every delta step.

In \[ \]:

Copied!

agent.reset()

response \= agent.stream\_chat("What is the area of Seattle?")
for resp in response.chat\_stream:
    print(resp.message.content)

agent.reset() response = agent.stream\_chat("What is the area of Seattle?") for resp in response.chat\_stream: print(resp.message.content)

The
The area
The area of
The area of Seattle, Washington, is
The area of Seattle, Washington, is approximately 142.5 square
The area of Seattle, Washington, is approximately 142.5 square miles (369 square kilometers).
The area of Seattle, Washington, is approximately 142.5 square miles (369 square kilometers). This includes both land and water areas within
The area of Seattle, Washington, is approximately 142.5 square miles (369 square kilometers). This includes both land and water areas within the city limits.

Workspace[¶](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/#workspace)
--------------------------------------------------------------------------------------------

Sometimes, you have to pass workspace id when you created an agent application in non-default workspace. For how to use workspace, please refer to doc: [How to use different workspaces in ModelStudio.](https://help.aliyun.com/document_detail/2587495.html?spm=a2c4g.2712191.0.i29#c5222ec081sbo)

In \[ \]:

Copied!

agent \= DashScopeAgent(
    app\_id\="your\_app\_id",  \# The id of app that you created
    chat\_session\=True,  \# Enable chat session which will auto save and pass chat                               history to LLM.
    workspace\="your\_workspace\_id",  \# Workspace id that the agent application belongs to.
    verbose\=False,  \# If need to print more details
)

resp \= agent.chat("The radius is 9.3 meters, what is the area of the circle?")
print(resp.response)

agent = DashScopeAgent( app\_id="your\_app\_id", # The id of app that you created chat\_session=True, # Enable chat session which will auto save and pass chat history to LLM. workspace="your\_workspace\_id", # Workspace id that the agent application belongs to. verbose=False, # If need to print more details ) resp = agent.chat("The radius is 9.3 meters, what is the area of the circle?") print(resp.response)

To find the area of a circle when you know the radius (r), you can use the formula:

\\\[ \\text{Area} = \\pi r^2 \\\]

Given that the radius \\( r = 9.3 \\) meters, substituting this value into the formula gives:

\\\[ \\text{Area} = \\pi (9.3)^2 \\\]
\\\[ \\text{Area} = \\pi \\times 86.49 \\\]
\\\[ \\text{Area} \\approx 270.17 \\text{ square meters} \\\]

Therefore, the area of the circle with a radius of 9.3 meters is approximately 270.17 square meters.

Back to top

[Previous Building a Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)[Next Introspective Agents: Performing Tasks With Reflection](https://docs.llamaindex.ai/en/stable/examples/agent/introspective_agent_toxicity_reduction/)

Hi, how can I help you?

🦙
