Title: Graphdb cypher - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/

Markdown Content:
Graphdb cypher - LlamaIndex


GraphDBCypherReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/#llama_index.readers.graphdb_cypher.GraphDBCypherReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Graph database Cypher reader.

Combines all Cypher query results into the Document type used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `uri` | `str` | 
Graph Database URI



 | _required_ |
| `username` | `str` | 

Username



 | _required_ |
| `password` | `str` | 

Password



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-graphdb-cypher/llama_index/readers/graphdb_cypher/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
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
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GraphDBCypherReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Graph database Cypher reader.</span>

<span class="sd">    Combines all Cypher query results into the Document type used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        uri (str): Graph Database URI</span>
<span class="sd">        username (str): Username</span>
<span class="sd">        password (str): Password</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">database</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">neo4j</span> <span class="kn">import</span> <span class="n">GraphDatabase</span><span class="p">,</span> <span class="n">basic_auth</span>

        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`neo4j` package not found, please run `pip install neo4j`"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">uri</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">uri</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`uri` must be provided."</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span>
                <span class="n">uri</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="n">basic_auth</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">database</span> <span class="o">=</span> <span class="n">database</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">parameters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run the Cypher with optional parameters and turn results into documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): Graph Cypher query string.</span>
<span class="sd">            parameters (Optional[Dict]): optional query parameters.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">parameters</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">parameters</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">records</span><span class="p">,</span> <span class="n">summary</span><span class="p">,</span> <span class="n">keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute_query</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">parameters</span><span class="p">,</span> <span class="n">database_</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">database</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">entry</span><span class="o">.</span><span class="n">data</span><span class="p">()))</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">records</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/#llama_index.readers.graphdb_cypher.GraphDBCypherReader.load_data "Permanent link")

```
load_data(query: str, parameters: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Run the Cypher with optional parameters and turn results into documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
Graph Cypher query string.



 | _required_ |
| `parameters` | `Optional[Dict]` | 

optional query parameters.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-graphdb-cypher/llama_index/readers/graphdb_cypher/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">parameters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run the Cypher with optional parameters and turn results into documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): Graph Cypher query string.</span>
<span class="sd">        parameters (Optional[Dict]): optional query parameters.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">parameters</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="n">records</span><span class="p">,</span> <span class="n">summary</span><span class="p">,</span> <span class="n">keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute_query</span><span class="p">(</span>
        <span class="n">query</span><span class="p">,</span> <span class="n">parameters</span><span class="p">,</span> <span class="n">database_</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">database</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">entry</span><span class="o">.</span><span class="n">data</span><span class="p">()))</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">records</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Gpt repo](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/)[Next Graphql](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/)
