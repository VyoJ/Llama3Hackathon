Title: Graphql - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/

Markdown Content:
Graphql - LlamaIndex


GraphQLToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/#llama_index.tools.graphql.GraphQLToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Requests Tool.

Source code in `llama-index-integrations/tools/llama-index-tools-graphql/llama_index/tools/graphql/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GraphQLToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Requests Tool."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"graphql_request"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="n">headers</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span>

    <span class="k">def</span> <span class="nf">graphql_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">variables</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">operation_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sa">r</span><span class="sd">"""</span>
<span class="sd">        Use this tool to make a GraphQL query against the server.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The GraphQL query to execute</span>
<span class="sd">            variables (str): The variable values for the query</span>
<span class="sd">            operation_name (str): The name for the query</span>

<span class="sd">        example input:</span>
<span class="sd">            "query":"query Ships {\n  ships {\n    id\n    model\n    name\n    type\n    status\n  }\n}",</span>
<span class="sd">            "variables":{},</span>
<span class="sd">            "operation_name":"Ships"</span>

<span class="sd">        """</span>
        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
                <span class="s2">"variables"</span><span class="p">:</span> <span class="n">variables</span><span class="p">,</span>
                <span class="s2">"operationName"</span><span class="p">:</span> <span class="n">operation_name</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">text</span>
</code></pre></div></td></tr></tbody></table>

### graphql\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/#llama_index.tools.graphql.GraphQLToolSpec.graphql_request "Permanent link")

```
graphql_request(query: str, variables: str, operation_name: str)
```

Use this tool to make a GraphQL query against the server.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The GraphQL query to execute



 | _required_ |
| `variables` | `str` | 

The variable values for the query



 | _required_ |
| `operation_name` | `str` | 

The name for the query



 | _required_ |

example input"query":"query Ships {\\n ships {\\n id\\n model\\n name\\n type\\n status\\n }\\n}", "variables":{}, "operation\_name":"Ships"

Source code in `llama-index-integrations/tools/llama-index-tools-graphql/llama_index/tools/graphql/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">graphql_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">variables</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">operation_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""</span>
<span class="sd">    Use this tool to make a GraphQL query against the server.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The GraphQL query to execute</span>
<span class="sd">        variables (str): The variable values for the query</span>
<span class="sd">        operation_name (str): The name for the query</span>

<span class="sd">    example input:</span>
<span class="sd">        "query":"query Ships {\n  ships {\n    id\n    model\n    name\n    type\n    status\n  }\n}",</span>
<span class="sd">        "variables":{},</span>
<span class="sd">        "operation_name":"Ships"</span>

<span class="sd">    """</span>
    <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
        <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
        <span class="n">json</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
            <span class="s2">"variables"</span><span class="p">:</span> <span class="n">variables</span><span class="p">,</span>
            <span class="s2">"operationName"</span><span class="p">:</span> <span class="n">operation_name</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">text</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Google](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/tools/)
