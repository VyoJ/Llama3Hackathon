Title: Graphql - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/

Markdown Content:
Graphql - LlamaIndex


GraphQLReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/#llama_index.readers.graphql.GraphQLReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

GraphQL reader.

Combines all GraphQL results into the Document used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `uri` | `str` | 
GraphQL uri.



 | `None` |
| `headers` | `Optional[Dict]` | 

Optional http headers.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-graphql/llama_index/readers/graphql/base.py`

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
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GraphQLReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GraphQL reader.</span>

<span class="sd">    Combines all GraphQL results into the Document used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        uri (str): GraphQL uri.</span>
<span class="sd">        headers (Optional[Dict]): Optional http headers.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">gql</span> <span class="kn">import</span> <span class="n">Client</span>
            <span class="kn">from</span> <span class="nn">gql.transport.requests</span> <span class="kn">import</span> <span class="n">RequestsHTTPTransport</span>

        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"`gql` package not found, please run `pip install gql`"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">uri</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">uri</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`uri` must be provided."</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">headers</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">headers</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">transport</span> <span class="o">=</span> <span class="n">RequestsHTTPTransport</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">uri</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">transport</span><span class="o">=</span><span class="n">transport</span><span class="p">,</span> <span class="n">fetch_schema_from_transport</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">variables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run query with optional variables and turn results into documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): GraphQL query string.</span>
<span class="sd">            variables (Optional[Dict]): optional query parameters.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">gql</span> <span class="kn">import</span> <span class="n">gql</span>

        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"`gql` package not found, please run `pip install gql`"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">variables</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">variables</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">gql</span><span class="p">(</span><span class="n">query</span><span class="p">),</span> <span class="n">variable_values</span><span class="o">=</span><span class="n">variables</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
            <span class="n">entry</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">v</span><span class="p">))</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">entry</span><span class="p">)))</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/#llama_index.readers.graphql.GraphQLReader.load_data "Permanent link")

```
load_data(query: str, variables: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Run query with optional variables and turn results into documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
GraphQL query string.



 | _required_ |
| `variables` | `Optional[Dict]` | 

optional query parameters.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-graphql/llama_index/readers/graphql/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">41</span>
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
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">variables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run query with optional variables and turn results into documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): GraphQL query string.</span>
<span class="sd">        variables (Optional[Dict]): optional query parameters.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">gql</span> <span class="kn">import</span> <span class="n">gql</span>

    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"`gql` package not found, please run `pip install gql`"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">variables</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">variables</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">gql</span><span class="p">(</span><span class="n">query</span><span class="p">),</span> <span class="n">variable_values</span><span class="o">=</span><span class="n">variables</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
        <span class="n">entry</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">v</span><span class="p">))</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">yaml</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">entry</span><span class="p">)))</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Graphdb cypher](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/)[Next Guru](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/)
