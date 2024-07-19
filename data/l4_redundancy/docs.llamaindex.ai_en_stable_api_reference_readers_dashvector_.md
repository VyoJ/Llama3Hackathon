Title: Dashvector - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/

Markdown Content:
Dashvector - LlamaIndex


DashVectorReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/#llama_index.readers.dashvector.DashVectorReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

DashVector reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_key` | `str` | 
DashVector API key.



 | _required_ |
| `endpoint` | `str` | 

DashVector cluster endpoint.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-dashvector/llama_index/readers/dashvector/base.py`

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
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DashVectorReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DashVector reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key (str): DashVector API key.</span>
<span class="sd">        endpoint (str): DashVector cluster endpoint.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">dashvector</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`dashvector` package not found, please run `pip install dashvector`"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">dashvector</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">endpoint</span><span class="o">=</span><span class="n">endpoint</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">id_to_text_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">separate_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="nb">filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_vector</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from DashVector.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_name (str): Name of the collection.</span>
<span class="sd">            id_to_text_map (Dict[str, str]): A map from ID's to text.</span>
<span class="sd">            separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">                documents per retrieved entry. Defaults to True.</span>
<span class="sd">            vector (List[float]): Query vector.</span>
<span class="sd">            top_k (int): Number of results to return.</span>
<span class="sd">            filter (Optional[str]): doc fields filter conditions that meet the SQL</span>
<span class="sd">                where clause specification.</span>
<span class="sd">            include_vector (bool): Whether to include the embedding in the response.</span>
<span class="sd">                Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">collection</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Failed to get collection: </span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2">,"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">collection</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="n">resp</span> <span class="o">=</span> <span class="n">collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">vector</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span>
            <span class="n">topk</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
            <span class="n">include_vector</span><span class="o">=</span><span class="n">include_vector</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">resp</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to query document,"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">resp</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">resp</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">doc</span><span class="o">.</span><span class="n">id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">id_to_text_map</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"ID not found in id_to_text_map."</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">id_to_text_map</span><span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">vector</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">embedding</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">))</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/)[Next Database](https://docs.llamaindex.ai/en/stable/api_reference/readers/database/)
