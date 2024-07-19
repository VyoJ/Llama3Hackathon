Title: Zep - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/

Markdown Content:
Zep - LlamaIndex


ZepReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/#llama_index.readers.zep.ZepReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Zep document vector store reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_url` | `str` | 
Zep API URL



 | _required_ |
| `api_key` | `str` | 

Zep API key, optional



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-zep/llama_index/readers/zep/base.py`

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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ZepReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Zep document vector store reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_url (str): Zep API URL</span>
<span class="sd">        api_key (str): Zep API key, optional</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="kn">from</span> <span class="nn">zep_python</span> <span class="kn">import</span> <span class="n">ZepClient</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_api_url</span> <span class="o">=</span> <span class="n">api_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">ZepClient</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">api_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">separate_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_values</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Zep.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_name (str): Name of the Zep collection.</span>
<span class="sd">            query (Optional[str]): Query string. Required if vector is None.</span>
<span class="sd">            vector (Optional[List[float]]): Query vector. Required if query is None.</span>
<span class="sd">            metadata (Optional[Dict[str, Any]]): Metadata to filter on.</span>
<span class="sd">            top_k (Optional[int]): Number of results to return. Defaults to 5.</span>
<span class="sd">            separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">                documents per retrieved entry. Defaults to True.</span>
<span class="sd">            include_values (Optional[bool]): Whether to include the embedding in</span>
<span class="sd">                the response. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">vector</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Either query or vector must be specified."</span><span class="p">)</span>

        <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span>
        <span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">embedding</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">include_values</span>
                <span class="k">else</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">response</span>
        <span class="p">]</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/#llama_index.readers.zep.ZepReader.load_data "Permanent link")

```
load_data(collection_name: str, query: Optional[str] = None, vector: Optional[List[float]] = None, metadata: Optional[Dict[str, Any]] = None, top_k: Optional[int] = 5, separate_documents: Optional[bool] = True, include_values: Optional[bool] = True) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Zep.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the Zep collection.



 | _required_ |
| `query` | `Optional[str]` | 

Query string. Required if vector is None.



 | `None` |
| `vector` | `Optional[List[float]]` | 

Query vector. Required if query is None.



 | `None` |
| `metadata` | `Optional[Dict[str, Any]]` | 

Metadata to filter on.



 | `None` |
| `top_k` | `Optional[int]` | 

Number of results to return. Defaults to 5.



 | `5` |
| `separate_documents` | `Optional[bool]` | 

Whether to return separate documents per retrieved entry. Defaults to True.



 | `True` |
| `include_values` | `Optional[bool]` | 

Whether to include the embedding in the response. Defaults to True.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-zep/llama_index/readers/zep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
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
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">separate_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_values</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Zep.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): Name of the Zep collection.</span>
<span class="sd">        query (Optional[str]): Query string. Required if vector is None.</span>
<span class="sd">        vector (Optional[List[float]]): Query vector. Required if query is None.</span>
<span class="sd">        metadata (Optional[Dict[str, Any]]): Metadata to filter on.</span>
<span class="sd">        top_k (Optional[int]): Number of results to return. Defaults to 5.</span>
<span class="sd">        separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">            documents per retrieved entry. Defaults to True.</span>
<span class="sd">        include_values (Optional[bool]): Whether to include the embedding in</span>
<span class="sd">            the response. Defaults to True.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">vector</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Either query or vector must be specified."</span><span class="p">)</span>

    <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span>
    <span class="p">)</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">embedding</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">include_values</span>
            <span class="k">else</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">response</span>
    <span class="p">]</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Zendesk](https://docs.llamaindex.ai/en/stable/api_reference/readers/zendesk/)[Next Zulip](https://docs.llamaindex.ai/en/stable/api_reference/readers/zulip/)
