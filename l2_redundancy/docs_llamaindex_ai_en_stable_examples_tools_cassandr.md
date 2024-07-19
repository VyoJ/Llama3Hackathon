Title: Cassandra Database Tools - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/

Markdown Content:
Cassandra Database Tools - LlamaIndex


Apache Cassandra® is a widely used database for storing transactional application data. The introduction of functions and tooling in Large Language Models has opened up some exciting use cases for existing data in Generative AI applications. The Cassandra Database toolkit enables AI engineers to efficiently integrate Agents with Cassandra data, offering the following features:

*   Fast data access through optimized queries. Most queries should run in single-digit ms or less.
*   Schema introspection to enhance LLM reasoning capabilities
*   Compatibility with various Cassandra deployments, including Apache Cassandra®, DataStax Enterprise™, and DataStax Astra™
*   Currently, the toolkit is limited to SELECT queries and schema introspection operations. (Safety first)

Quick Start[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#quick-start)
------------------------------------------------------------------------------------------

*   Install the cassio library
*   Set environment variables for the Cassandra database you are connecting to
*   Initialize CassandraDatabase
*   Pass the tools to your agent with spec.to\_tool\_list()
*   Sit back and watch it do all your work for you

Theory of Operation[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#theory-of-operation)
----------------------------------------------------------------------------------------------------------

Cassandra Query Language (CQL) is the primary _human-centric_ way of interacting with a Cassandra database. While offering some flexibility when generating queries, it requires knowledge of Cassandra data modeling best practices. LLM function calling gives an agent the ability to reason and then choose a tool to satisfy the request. Agents using LLMs should reason using Cassandra-specific logic when choosing the appropriate tool or chain of tools. This reduces the randomness introduced when LLMs are forced to provide a top-down solution. Do you want an LLM to have complete unfettered access to your database? Yeah. Probably not. To accomplish this, we provide a prompt for use when constructing questions for the agent:

You are an Apache Cassandra expert query analysis bot with the following features 
and rules:
 \- You will take a question from the end user about finding specific 
   data in the database.
 \- You will examine the schema of the database and create a query path. 
 \- You will provide the user with the correct query to find the data they are looking 
   for, showing the steps provided by the query path.
 \- You will use best practices for querying Apache Cassandra using partition keys 
   and clustering columns.
 \- Avoid using ALLOW FILTERING in the query.
 \- The goal is to find a query path, so it may take querying other tables to get 
   to the final answer. 

The following is an example of a query path in JSON format:

 {
  "query\_paths": \[
    {
      "description": "Direct query to users table using email",
      "steps": \[
        {
          "table": "user\_credentials",
          "query": 
             "SELECT userid FROM user\_credentials WHERE email = 'example@example.com';"
        },
        {
          "table": "users",
          "query": "SELECT \* FROM users WHERE userid = ?;"
        }
      \]
    }
  \]
}

Tools Provided[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#tools-provided)
------------------------------------------------------------------------------------------------

### `cassandra_db_schema`[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#cassandra_db_schema)

Gathers all schema information for the connected database or a specific schema. Critical for the agent when determining actions.

### `cassandra_db_select_table_data`[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#cassandra_db_select_table_data)

Selects data from a specific keyspace and table. The agent can pass paramaters for a predicate and limits on the number of returned records.

### `cassandra_db_query`[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#cassandra_db_query)

Experimental alternative to `cassandra_db_select_table_data` which takes a query string completely formed by the agent instead of parameters. _Warning_: This can lead to unusual queries that may not be as performant(or even work). This may be removed in future releases. If it does something cool, we want to know about that too. You never know!

Enviroment Setup[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#enviroment-setup)
----------------------------------------------------------------------------------------------------

Install the following Python modules:

pip install ipykernel python-dotenv cassio llama-index llama-index-agent-openai llama-index-llms-openai llama-index-tools-cassandra

### .env file[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#env-file)

Connection is via `cassio` using `auto=True` parameter, and the notebook uses OpenAI. You should create a `.env` file accordingly.

For Cassandra, set:

CASSANDRA\_CONTACT\_POINTS
CASSANDRA\_USERNAME
CASSANDRA\_PASSWORD
CASSANDRA\_KEYSPACE

For Astra, set:

ASTRA\_DB\_APPLICATION\_TOKEN
ASTRA\_DB\_DATABASE\_ID
ASTRA\_DB\_KEYSPACE

For example:

\# Connection to Astra:
ASTRA\_DB\_DATABASE\_ID\=a1b2c3d4-...
ASTRA\_DB\_APPLICATION\_TOKEN\=AstraCS:...
ASTRA\_DB\_KEYSPACE\=notebooks

\# Also set 
OPENAI\_API\_KEY\=sk-....

(You may also modify the below code to directly connect with `cassio`.)

In \[ \]:

Copied!

from dotenv import load\_dotenv

load\_dotenv(override\=True)

from dotenv import load\_dotenv load\_dotenv(override=True)

In \[ \]:

Copied!

\# Import necessary libraries
import os

import cassio

from llama\_index.tools.cassandra.base import CassandraDatabaseToolSpec
from llama\_index.tools.cassandra.cassandra\_database\_wrapper import (
    CassandraDatabase,
)

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.llms.openai import OpenAI

\# Import necessary libraries import os import cassio from llama\_index.tools.cassandra.base import CassandraDatabaseToolSpec from llama\_index.tools.cassandra.cassandra\_database\_wrapper import ( CassandraDatabase, ) from llama\_index.agent.openai import OpenAIAgent from llama\_index.llms.openai import OpenAI

Connect to a Cassandra Database[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#connect-to-a-cassandra-database)
----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

cassio.init(auto\=True)

session \= cassio.config.resolve\_session()
if not session:
    raise Exception(
        "Check environment configuration or manually configure cassio connection parameters"
    )

cassio.init(auto=True) session = cassio.config.resolve\_session() if not session: raise Exception( "Check environment configuration or manually configure cassio connection parameters" )

In \[ \]:

Copied!

\# Test data prep

session \= cassio.config.resolve\_session()

session.execute("""DROP KEYSPACE IF EXISTS llamaindex\_agent\_test; """)

session.execute(
    """
CREATE KEYSPACE if not exists llamaindex\_agent\_test 
WITH replication = {'class': 'SimpleStrategy', 'replication\_factor': 1};
"""
)

session.execute(
    """
    CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.user\_credentials (
    user\_email text PRIMARY KEY,
    user\_id UUID,
    password TEXT
);
"""
)

session.execute(
    """
    CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT
);"""
)

session.execute(
    """
    CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.user\_videos ( 
    user\_id UUID,
    video\_id UUID,
    title TEXT,
    description TEXT,
    PRIMARY KEY (user\_id, video\_id)
);
"""
)

user\_id \= "522b1fe2-2e36-4cef-a667-cd4237d08b89"
video\_id \= "27066014-bad7-9f58-5a30-f63fe03718f6"

session.execute(
    f"""
    INSERT INTO llamaindex\_agent\_test.user\_credentials (user\_id, user\_email) 
    VALUES ({user\_id}, 'patrick@datastax.com');
"""
)

session.execute(
    f"""
    INSERT INTO llamaindex\_agent\_test.users (id, name, email) 
    VALUES ({user\_id}, 'Patrick McFadin', 'patrick@datastax.com');
"""
)

session.execute(
    f"""
    INSERT INTO llamaindex\_agent\_test.user\_videos (user\_id, video\_id, title)
    VALUES ({user\_id}, {video\_id}, 'Use Langflow to Build an LLM Application in 5 Minutes');
"""
)

session.set\_keyspace("llamaindex\_agent\_test")

\# Test data prep session = cassio.config.resolve\_session() session.execute("""DROP KEYSPACE IF EXISTS llamaindex\_agent\_test; """) session.execute( """ CREATE KEYSPACE if not exists llamaindex\_agent\_test WITH replication = {'class': 'SimpleStrategy', 'replication\_factor': 1}; """ ) session.execute( """ CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.user\_credentials ( user\_email text PRIMARY KEY, user\_id UUID, password TEXT ); """ ) session.execute( """ CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.users ( id UUID PRIMARY KEY, name TEXT, email TEXT );""" ) session.execute( """ CREATE TABLE IF NOT EXISTS llamaindex\_agent\_test.user\_videos ( user\_id UUID, video\_id UUID, title TEXT, description TEXT, PRIMARY KEY (user\_id, video\_id) ); """ ) user\_id = "522b1fe2-2e36-4cef-a667-cd4237d08b89" video\_id = "27066014-bad7-9f58-5a30-f63fe03718f6" session.execute( f""" INSERT INTO llamaindex\_agent\_test.user\_credentials (user\_id, user\_email) VALUES ({user\_id}, 'patrick@datastax.com'); """ ) session.execute( f""" INSERT INTO llamaindex\_agent\_test.users (id, name, email) VALUES ({user\_id}, 'Patrick McFadin', 'patrick@datastax.com'); """ ) session.execute( f""" INSERT INTO llamaindex\_agent\_test.user\_videos (user\_id, video\_id, title) VALUES ({user\_id}, {video\_id}, 'Use Langflow to Build an LLM Application in 5 Minutes'); """ ) session.set\_keyspace("llamaindex\_agent\_test")

In \[ \]:

Copied!

\# Create a CassandraDatabaseToolSpec object
db \= CassandraDatabase()

spec \= CassandraDatabaseToolSpec(db\=db)

tools \= spec.to\_tool\_list()
for tool in tools:
    print(tool.metadata.name)
    print(tool.metadata.description)
    print(tool.metadata.fn\_schema)

\# Create a CassandraDatabaseToolSpec object db = CassandraDatabase() spec = CassandraDatabaseToolSpec(db=db) tools = spec.to\_tool\_list() for tool in tools: print(tool.metadata.name) print(tool.metadata.description) print(tool.metadata.fn\_schema)

cassandra\_db\_schema
cassandra\_db\_schema(keyspace: str) -> List\[llama\_index.core.schema.Document\]
Input to this tool is a keyspace name, output is a table description
            of Apache Cassandra tables.
            If the query is not correct, an error message will be returned.
            If an error is returned, report back to the user that the keyspace
            doesn't exist and stop.

        Args:
            keyspace (str): The name of the keyspace for which to return the schema.

        Returns:
            List\[Document\]: A list of Document objects, each containing a table description.
        
<class 'pydantic.main.cassandra\_db\_schema'>
cassandra\_db\_select\_table\_data
cassandra\_db\_select\_table\_data(keyspace: str, table: str, predicate: str, limit: int) -> List\[llama\_index.core.schema.Document\]
Tool for getting data from a table in an Apache Cassandra database.
            Use the WHERE clause to specify the predicate for the query that uses the
            primary key. A blank predicate will return all rows. Avoid this if possible.
            Use the limit to specify the number of rows to return. A blank limit will
            return all rows.

        Args:
            keyspace (str): The name of the keyspace containing the table.
            table (str): The name of the table for which to return data.
            predicate (str): The predicate for the query that uses the primary key.
            limit (int): The maximum number of rows to return.

        Returns:
            List\[Document\]: A list of Document objects, each containing a row of data.
        
<class 'pydantic.main.cassandra\_db\_select\_table\_data'>

In \[ \]:

Copied!

\# Choose the LLM that will drive the agent
\# Only certain models support this
llm \= OpenAI(model\="gpt-4-1106-preview")

\# Create the Agent with our tools. Verbose will echo the agent's actions
agent \= OpenAIAgent.from\_tools(tools, llm\=llm, verbose\=True)

\# Choose the LLM that will drive the agent # Only certain models support this llm = OpenAI(model="gpt-4-1106-preview") # Create the Agent with our tools. Verbose will echo the agent's actions agent = OpenAIAgent.from\_tools(tools, llm=llm, verbose=True)

### Invoking the agent with tools[¶](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/#invoking-the-agent-with-tools)

We've created an agent that uses an LLM for reasoning and communication with a tool list for actions, Now we can simply ask questions of the agent and watch it utilize the tools we've given it.

In \[ \]:

Copied!

\# Ask our new agent a series of questions. What how the agent uses tools to get the answers.
agent.chat("What tables are in the keyspace llamaindex\_agent\_test?")
agent.chat("What is the userid for patrick@datastax.com ?")
agent.chat("What videos did user patrick@datastax.com upload?")

\# Ask our new agent a series of questions. What how the agent uses tools to get the answers. agent.chat("What tables are in the keyspace llamaindex\_agent\_test?") agent.chat("What is the userid for patrick@datastax.com ?") agent.chat("What videos did user patrick@datastax.com upload?")

Added user message to memory: What tables are in the keyspace llamaindex\_agent\_test?

Calling function: cassandra\_db\_schema with args: {"keyspace":"llamaindex\_agent\_test"}
Got output: \[Document(id\_='4b6011e6-62e6-4db2-9198-046534b7c8dd', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Table Name: user\_credentials\\n- Keyspace: llamaindex\_agent\_test\\n- Columns\\n  - password (text)\\n  - user\_email (text)\\n  - user\_id (uuid)\\n- Partition Keys: (user\_email)\\n- Clustering Keys: \\n\\nTable Name: user\_videos\\n- Keyspace: llamaindex\_agent\_test\\n- Columns\\n  - description (text)\\n  - title (text)\\n  - user\_id (uuid)\\n  - video\_id (uuid)\\n- Partition Keys: (user\_id)\\n- Clustering Keys: (video\_id asc)\\n\\n\\nTable Name: users\\n- Keyspace: llamaindex\_agent\_test\\n- Columns\\n  - email (text)\\n  - id (uuid)\\n  - name (text)\\n- Partition Keys: (id)\\n- Clustering Keys: \\n\\n', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]
 Calling Function 

Added user message to memory: What videos did user patrick@datastax.com upload?

Calling function: cassandra\_db\_select\_table\_data with args: {"keyspace":"llamaindex\_agent\_test","table":"user\_videos","predicate":"user\_id = 522b1fe2-2e36-4cef-a667-cd4237d08b89","limit":10}
Got output: \[Document(id\_='e3ecfba1-e8e1-4ce3-b321-3f51e12077a1', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Row(user\_id=UUID('522b1fe2-2e36-4cef-a667-cd4237d08b89'), video\_id=UUID('27066014-bad7-9f58-5a30-f63fe03718f6'), description=None, title='Use Langflow to Build an LLM Application in 5 Minutes')", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]


Out\[ \]:

AgentChatResponse(response='The user \`patrick@datastax.com\` uploaded the following video in the \`llamaindex\_agent\_test\` keyspace:\\n\\n- Title: "Use Langflow to Build an LLM Application in 5 Minutes"\\n- Video ID: \`27066014-bad7-9f58-5a30-f63fe03718f6\`\\n- Description: Not provided', sources=\[ToolOutput(content='\[Document(id\_=\\'e3ecfba1-e8e1-4ce3-b321-3f51e12077a1\\', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Row(user\_id=UUID(\\'522b1fe2-2e36-4cef-a667-cd4237d08b89\\'), video\_id=UUID(\\'27066014-bad7-9f58-5a30-f63fe03718f6\\'), description=None, title=\\'Use Langflow to Build an LLM Application in 5 Minutes\\')", start\_char\_idx=None, end\_char\_idx=None, text\_template=\\'{metadata\_str}\\\\n\\\\n{content}\\', metadata\_template=\\'{key}: {value}\\', metadata\_seperator=\\'\\\\n\\')\]', tool\_name='cassandra\_db\_select\_table\_data', raw\_input={'args': (), 'kwargs': {'keyspace': 'llamaindex\_agent\_test', 'table': 'user\_videos', 'predicate': 'user\_id = 522b1fe2-2e36-4cef-a667-cd4237d08b89', 'limit': 10}}, raw\_output=\[Document(id\_='e3ecfba1-e8e1-4ce3-b321-3f51e12077a1', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Row(user\_id=UUID('522b1fe2-2e36-4cef-a667-cd4237d08b89'), video\_id=UUID('27066014-bad7-9f58-5a30-f63fe03718f6'), description=None, title='Use Langflow to Build an LLM Application in 5 Minutes')", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\], is\_error=False)\], source\_nodes=\[\], is\_dummy\_stream=False)

Back to top

[Previous Azure Code Interpreter Tool Spec](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)[Next Evaluation Query Engine Tool](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/)
