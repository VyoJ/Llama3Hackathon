Title: Agent search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/

Markdown Content:
Agent search - LlamaIndex


AgentSearchReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/#llama_index.readers.agent_search.AgentSearchReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

AgentSearch reader.

Source code in `llama-index-integrations/readers/llama-index-readers-agent-search/llama_index/readers/agent_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
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
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentSearchReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentSearch reader."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_base</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"`agent-search` package not found, please run `pip install agent-search`"</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">agent_search</span>  <span class="c1"># noqa: F401</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="kn">from</span> <span class="nn">agent_search</span> <span class="kn">import</span> <span class="n">SciPhi</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">SciPhi</span><span class="p">(</span><span class="n">api_base</span><span class="o">=</span><span class="n">api_base</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">search_provider</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"bing"</span><span class="p">,</span>
        <span class="n">llm_model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"SciPhi/Sensei-7B-V1"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from AgentSearch, hosted by SciPhi.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_name (str): Name of the Milvus collection.</span>
<span class="sd">            query_vector (List[float]): Query vector.</span>
<span class="sd">            limit (int): Number of results to return.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">rag_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get_search_rag_response</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">search_provider</span><span class="o">=</span><span class="n">search_provider</span><span class="p">,</span> <span class="n">llm_model</span><span class="o">=</span><span class="n">llm_model</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">rag_response</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"response"</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">rag_response</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/#llama_index.readers.agent_search.AgentSearchReader.load_data "Permanent link")

```
load_data(query: str, search_provider: str = 'bing', llm_model: str = 'SciPhi/Sensei-7B-V1') -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from AgentSearch, hosted by SciPhi.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the Milvus collection.



 | _required_ |
| `query_vector` | `List[float]` | 

Query vector.



 | _required_ |
| `limit` | `int` | 

Number of results to return.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-agent-search/llama_index/readers/agent_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
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
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">search_provider</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"bing"</span><span class="p">,</span>
    <span class="n">llm_model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"SciPhi/Sensei-7B-V1"</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load data from AgentSearch, hosted by SciPhi.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): Name of the Milvus collection.</span>
<span class="sd">        query_vector (List[float]): Query vector.</span>
<span class="sd">        limit (int): Number of results to return.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">rag_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get_search_rag_response</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">search_provider</span><span class="o">=</span><span class="n">search_provider</span><span class="p">,</span> <span class="n">llm_model</span><span class="o">=</span><span class="n">llm_model</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">rag_response</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"response"</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">rag_response</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openai](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/)[Next Airbyte cdk](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_cdk/)
