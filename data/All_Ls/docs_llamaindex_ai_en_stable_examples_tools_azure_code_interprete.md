Title: Azure Code Interpreter Tool Spec

URL Source: https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/

Markdown Content:
Azure Code Interpreter Tool Spec - LlamaIndex


This example walks through configuring and using the Azure Code Interpreter tool spec (powered by Azure Dynamic Sessions).

In \[ \]:

Copied!

%pip install llama\-index
%pip install llama\-index\-llms\-azure
%pip install llama\-index\-tools\-azure\-code\-interpreter

%pip install llama-index %pip install llama-index-llms-azure %pip install llama-index-tools-azure-code-interpreter

In \[ \]:

Copied!

\# Setup Azure OpenAI Agent
from llama\_index.llms.azure\_openai import AzureOpenAI

api\_key \= "your-azure-openai-api-key"
azure\_endpoint \= "your-azure-openai-endpoint"
api\_version \= "azure-api-version"

\# Setup Azure OpenAI Agent from llama\_index.llms.azure\_openai import AzureOpenAI api\_key = "your-azure-openai-api-key" azure\_endpoint = "your-azure-openai-endpoint" api\_version = "azure-api-version"

In \[ \]:

Copied!

\# Import the AzureCodeInterpreterToolSpec from llama\_index
from llama\_index.tools.azure\_code\_interpreter import (
    AzureCodeInterpreterToolSpec,
)

\# Import the ReActAgent
from llama\_index.core.agent import ReActAgent

\# Create the AzureCodeInterpreterToolSpec with the pool\_managment\_endpoint set to your session management endpoint
\# It is optional to set the local\_save\_path, but it is recommended to set it to a path where the tool can automatically save any intermediate data generated from Python code's output.
azure\_code\_interpreter\_spec \= AzureCodeInterpreterToolSpec(
    pool\_managment\_endpoint\="your-pool-management-endpoint",
    local\_save\_path\="local-file-path-to-save-intermediate-data",
)

llm \= AzureOpenAI(
    model\="gpt-35-turbo",
    deployment\_name\="gpt-35-deploy",
    api\_key\=api\_key,
    azure\_endpoint\=azure\_endpoint,
    api\_version\=api\_version,
)

\# Create the ReActAgent and inject the tools defined in the AzureDynamicSessionsToolSpec
agent \= ReActAgent.from\_tools(
    azure\_code\_interpreter\_spec.to\_tool\_list(), llm\=llm, verbose\=True
)

\# Import the AzureCodeInterpreterToolSpec from llama\_index from llama\_index.tools.azure\_code\_interpreter import ( AzureCodeInterpreterToolSpec, ) # Import the ReActAgent from llama\_index.core.agent import ReActAgent # Create the AzureCodeInterpreterToolSpec with the pool\_managment\_endpoint set to your session management endpoint # It is optional to set the local\_save\_path, but it is recommended to set it to a path where the tool can automatically save any intermediate data generated from Python code's output. azure\_code\_interpreter\_spec = AzureCodeInterpreterToolSpec( pool\_managment\_endpoint="your-pool-management-endpoint", local\_save\_path="local-file-path-to-save-intermediate-data", ) llm = AzureOpenAI( model="gpt-35-turbo", deployment\_name="gpt-35-deploy", api\_key=api\_key, azure\_endpoint=azure\_endpoint, api\_version=api\_version, ) # Create the ReActAgent and inject the tools defined in the AzureDynamicSessionsToolSpec agent = ReActAgent.from\_tools( azure\_code\_interpreter\_spec.to\_tool\_list(), llm=llm, verbose=True )

In \[ \]:

Copied!

\# You can use the code interpreter directly without the LLM agent.
print(azure\_code\_interpreter\_spec.code\_interpreter("1+1"))

\# You can use the code interpreter directly without the LLM agent. print(azure\_code\_interpreter\_spec.code\_interpreter("1+1"))

{'$id': '1', 'status': 'Success', 'stdout': '', 'stderr': '', 'result': 2, 'executionTimeInMilliseconds': 11}

In \[ \]:

Copied!

\# Test the agent with simple answers that could leverage Python codes
print(agent.chat("Tell me the current time in Seattle."))

\# Test the agent with simple answers that could leverage Python codes print(agent.chat("Tell me the current time in Seattle."))

Thought: To provide the current time in Seattle, I need to calculate it based on the current UTC time and adjust for Seattle's time zone, which is Pacific Daylight Time (PDT) during daylight saving time and Pacific Standard Time (PST) outside of daylight saving time. PDT is UTC-7, and PST is UTC-8. I can use the code interpreter tool to get the current UTC time and adjust it accordingly.
Action: code\_interpreter
Action Input: {'python\_code': "from datetime import datetime, timedelta; import pytz; utc\_now = datetime.now(pytz.utc); seattle\_time = utc\_now.astimezone(pytz.timezone('America/Los\_Angeles')); seattle\_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')"}
Observation: {'$id': '1', 'status': 'Success', 'stdout': '', 'stderr': '', 'result': '2024-05-04 13:54:09 PDT-0700', 'executionTimeInMilliseconds': 120}
Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: The current time in Seattle is 2024-05-04 13:54:09 PDT.
The current time in Seattle is 2024-05-04 13:54:09 PDT.

In \[ \]:

Copied!

\# Upload a sample temperature file of a day in Redmond Washington and ask a question about it
res \= azure\_code\_interpreter\_spec.upload\_file(
    local\_file\_path\="./TemperatureData.csv"
)
if len(res) != 0:
    print(
        agent.chat("Find the highest temperature in the file that I uploaded.")
    )

\# Upload a sample temperature file of a day in Redmond Washington and ask a question about it res = azure\_code\_interpreter\_spec.upload\_file( local\_file\_path="./TemperatureData.csv" ) if len(res) != 0: print( agent.chat("Find the highest temperature in the file that I uploaded.") )

Thought: I need to use the list\_files tool to get the metadata for the uploaded file, and then use python to read the file and find the highest temperature.
Action: list\_files
Action Input: {}
Observation: \[RemoteFileMetadata(filename='TemperatureData.csv', size\_in\_bytes=514, file\_full\_path='/mnt/data/TemperatureData.csv')\]
Thought: I have the metadata for the file. I need to use python to read the file and find the highest temperature.
Action: code\_interpreter
Action Input: {'python\_code': "import csv\\n\\nwith open('/mnt/data/TemperatureData.csv', 'r') as f:\\n    reader = csv.reader(f)\\n    next(reader)\\n    highest\_temp = float('-inf')\\n    for row in reader:\\n        temp = float(row\[1\])\\n        if temp > highest\_temp:\\n            highest\_temp = temp\\nprint(highest\_temp)"}
Observation: {'$id': '1', 'status': 'Success', 'stdout': '12.4\\n', 'stderr': '', 'result': '', 'executionTimeInMilliseconds': 26}
Thought: I have the highest temperature. I can answer the question.
Answer: The highest temperature in the file is 12.4 degrees.
The highest temperature in the file is 12.4 degrees.

In \[ \]:

Copied!

\# Ask the LLM to draw a diagram based on the uploaded file.
\# Because the local\_save\_path is set, the diagram data will be automatically saved to the local\_save\_path.
print(
    agent.chat(
        "Use the temperature data that I uploaded, create a temperature curve."
    )
)

\# Ask the LLM to draw a diagram based on the uploaded file. # Because the local\_save\_path is set, the diagram data will be automatically saved to the local\_save\_path. print( agent.chat( "Use the temperature data that I uploaded, create a temperature curve." ) )

Thought: To proceed, I need to list the files in the session pool to identify the uploaded file containing the temperature data.
Action: list\_files
Action Input: {}
Observation: \[RemoteFileMetadata(filename='TemperatureData.csv', size\_in\_bytes=514, file\_full\_path='/mnt/data/TemperatureData.csv')\]
Thought: The file containing the temperature data is identified as 'TemperatureData.csv'. I need to read this file to extract the temperature data for plotting the temperature curve.
Action: code\_interpreter
Action Input: {'python\_code': "import pandas as pd\\n\\ndf = pd.read\_csv('/mnt/data/TemperatureData.csv')\\nprint(df.head())"}
Observation: {'$id': '1', 'status': 'Success', 'stdout': '             Time  Temperature\\n0  4/11/2024 0:00          6.5\\n1  4/11/2024 1:00          5.2\\n2  4/11/2024 2:00          4.8\\n3  4/11/2024 3:00          5.1\\n4  4/11/2024 4:00          5.7\\n', 'stderr': '', 'result': '', 'executionTimeInMilliseconds': 2103}
Thought: The data has been successfully loaded and previewed, showing columns for Time and Temperature. I will now proceed to plot the temperature curve using this data.
Action: code\_interpreter
Action Input: {'python\_code': "import pandas as pd\\nimport matplotlib.pyplot as plt\\n\\ndf = pd.read\_csv('/mnt/data/TemperatureData.csv')\\n\\nplt.figure(figsize=(10, 6))\\nplt.plot(pd.to\_datetime(df\['Time'\]), df\['Temperature'\], marker='o', linestyle='-', color='b')\\nplt.title('Temperature Curve')\\nplt.xlabel('Time')\\nplt.ylabel('Temperature (°C)')\\nplt.xticks(rotation=45)\\nplt.tight\_layout()\\nplt.savefig('/mnt/data/TemperatureCurve.png')\\nprint('/mnt/data/TemperatureCurve.png')"}
Observation: {'$id': '1', 'status': 'Success', 'stdout': '/mnt/data/TemperatureCurve.png\\n', 'stderr': '', 'result': {'type': 'image', 'format': 'png', 'saved\_to\_local\_path': True}, 'executionTimeInMilliseconds': 3810}
Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: The temperature curve has been successfully created and saved. You can view and download the image from \[here\](sandbox:/mnt/data/TemperatureCurve.png).
The temperature curve has been successfully created and saved. You can view and download the image from \[here\](sandbox:/mnt/data/TemperatureCurve.png).

In \[ \]:

Copied!

\# Ask the LLM to perform modifications on the sample temperature file
print(
    agent.chat(
        "Rearrange the temperature data in a descending order and save it back to the original csv file."
    )
)

\# Ask the LLM to perform modifications on the sample temperature file print( agent.chat( "Rearrange the temperature data in a descending order and save it back to the original csv file." ) )

Thought: To proceed, I need to first list the files in the session pool to identify the uploaded temperature data file.
Action: list\_files
Action Input: {}
Observation: \[RemoteFileMetadata(filename='TemperatureCurve.png', size\_in\_bytes=35512, file\_full\_path='/mnt/data/TemperatureCurve.png'), RemoteFileMetadata(filename='TemperatureData.csv', size\_in\_bytes=514, file\_full\_path='/mnt/data/TemperatureData.csv')\]
Thought: The temperature data file is identified as 'TemperatureData.csv'. I need to read its contents, rearrange the temperature data in descending order, and then save the changes back to the original CSV file.
Action: code\_interpreter
Action Input: {'python\_code': "import pandas as pd\\n\\ndf = pd.read\_csv('/mnt/data/TemperatureData.csv')\\ndf\_sorted = df.sort\_values(by='Temperature', ascending=False)\\ndf\_sorted.to\_csv('/mnt/data/TemperatureData.csv', index=False)\\n'filename': 'TemperatureData.csv'"}
Observation: {'$id': '1', 'status': 'Failure', 'stdout': '', 'stderr': "illegal target for annotation (3407605186.py, line 6)  Cell In\[2363\], line 6\\n    'filename': 'TemperatureData.csv'\\n    ^\\nSyntaxError: illegal target for annotation\\n\\n", 'result': None, 'executionTimeInMilliseconds': 9}
Thought: There was a syntax error in the Python code due to an incorrect line. I need to correct the code and execute it again to sort the temperature data and save it back to the CSV file.
Action: code\_interpreter
Action Input: {'python\_code': "import pandas as pd\\n\\ndf = pd.read\_csv('/mnt/data/TemperatureData.csv')\\ndf\_sorted = df.sort\_values(by='Temperature', ascending=False)\\ndf\_sorted.to\_csv('/mnt/data/TemperatureData.csv', index=False)"}
Observation: {'$id': '1', 'status': 'Success', 'stdout': '', 'stderr': '', 'result': '', 'executionTimeInMilliseconds': 91}
Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: The temperature data has been successfully rearranged in descending order and saved back to the original CSV file, 'TemperatureData.csv'.
The temperature data has been successfully rearranged in descending order and saved back to the original CSV file, 'TemperatureData.csv'.

In \[ \]:

Copied!

\# Download the modified file
azure\_code\_interpreter\_spec.download\_file\_to\_local(
    remote\_file\_path\="TemperatureData.csv",
    local\_file\_path\="/.../SortedTemperatureData.csv",
)

\# Download the modified file azure\_code\_interpreter\_spec.download\_file\_to\_local( remote\_file\_path="TemperatureData.csv", local\_file\_path="/.../SortedTemperatureData.csv", )

In \[ \]:

Copied!

\# For comparison, print the first 10 lines of the original file
with open("/.../TemperatureData.csv", "r") as f:
    for i in range(10):
        print(f.readline().strip())

\# For comparison, print the first 10 lines of the original file with open("/.../TemperatureData.csv", "r") as f: for i in range(10): print(f.readline().strip())

Time,Temperature
4/11/2024 0:00,6.5
4/11/2024 1:00,5.2
4/11/2024 2:00,4.8
4/11/2024 3:00,5.1
4/11/2024 4:00,5.7
4/11/2024 5:00,5.1
4/11/2024 6:00,4.5
4/11/2024 7:00,5.5
4/11/2024 8:00,5.3

In \[ \]:

Copied!

\# For comparison, print the first 10 lines of the sorted file downloaded from session pool
with open("/.../SortedTemperatureData.csv", "r") as f:
    for i in range(10):
        print(f.readline().strip())

\# For comparison, print the first 10 lines of the sorted file downloaded from session pool with open("/.../SortedTemperatureData.csv", "r") as f: for i in range(10): print(f.readline().strip())

Time,Temperature
4/11/2024 20:00,12.4
4/11/2024 19:00,12.3
4/11/2024 17:00,12.3
4/11/2024 18:00,12.1
4/11/2024 16:00,11.7
4/11/2024 15:00,11.3
4/11/2024 21:00,10.9
4/11/2024 22:00,10.0
4/11/2024 23:00,9.4

Back to top

[Previous OnDemandLoaderTool Tutorial](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/)[Next Cassandra Database Tools](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/)
