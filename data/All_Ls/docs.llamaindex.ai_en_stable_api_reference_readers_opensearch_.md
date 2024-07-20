Title: Opensearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/

Markdown Content:
Opensearch - LlamaIndex


OpensearchReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/#llama_index.readers.opensearch.OpensearchReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Read documents from an Opensearch index.

These documents can then be used in a downstream Llama Index data structure.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `endpoint` | `str` | 
URL (http/https) of cluster without port



 | _required_ |
| `index` | `str` | 

Name of the index (required)



 | _required_ |
| `basic_auth` | `set` | 

basic authentication username password



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-opensearch/llama_index/readers/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpensearchReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Read documents from an Opensearch index.</span>

<span class="sd">    These documents can then be used in a downstream Llama Index data structure.</span>

<span class="sd">    Args:</span>
<span class="sd">        endpoint (str): URL (http/https) of cluster without port</span>
<span class="sd">        index (str): Name of the index (required)</span>
<span class="sd">        basic_auth (set): basic authentication username password</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">basic_auth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">set</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="kn">from</span> <span class="nn">opensearchpy</span> <span class="kn">import</span> <span class="n">OpenSearch</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_opster_client</span> <span class="o">=</span> <span class="n">OpenSearch</span><span class="p">(</span>
            <span class="n">hosts</span><span class="o">=</span><span class="p">[{</span><span class="s2">"host"</span><span class="p">:</span> <span class="n">host</span><span class="p">,</span> <span class="s2">"port"</span><span class="p">:</span> <span class="n">port</span><span class="p">}],</span>
            <span class="n">http_compress</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>  <span class="c1"># enables gzip compression for request bodies</span>
            <span class="n">http_auth</span><span class="o">=</span><span class="n">basic_auth</span><span class="p">,</span>
            <span class="n">use_ssl</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">verify_certs</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">ssl_assert_hostname</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">ssl_show_warn</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embedding_field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Read data from the Opensearch index.</span>

<span class="sd">        Args:</span>
<span class="sd">            field (str): Field in the document to retrieve text from</span>
<span class="sd">            query (Optional[dict]): Opensearch JSON query DSL object.</span>
<span class="sd">                For example:</span>
<span class="sd">                { "query" : {"match": {"message": {"query": "this is a test"}}}}</span>
<span class="sd">            embedding_field (Optional[str]): If there are embeddings stored in</span>
<span class="sd">                this index, this field can be used</span>
<span class="sd">                to set the embedding field on the returned Document list.</span>


<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_opster_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">][</span><span class="s2">"hits"</span><span class="p">]:</span>
            <span class="n">value</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">][</span><span class="n">field</span><span class="p">]</span>
            <span class="n">_</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">field</span><span class="p">)</span>
            <span class="n">embedding</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">embedding_field</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">],</span> <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/#llama_index.readers.opensearch.OpensearchReader.load_data "Permanent link")

```
load_data(field: str, query: Optional[dict] = None, embedding_field: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Read data from the Opensearch index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `field` | `str` | 
Field in the document to retrieve text from



 | _required_ |
| `query` | `Optional[dict]` | 

Opensearch JSON query DSL object. For example: { "query" : {"match": {"message": {"query": "this is a test"}}}}



 | `None` |
| `embedding_field` | `Optional[str]` | 

If there are embeddings stored in this index, this field can be used to set the embedding field on the returned Document list.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-opensearch/llama_index/readers/opensearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
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
    <span class="n">field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">embedding_field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Read data from the Opensearch index.</span>

<span class="sd">    Args:</span>
<span class="sd">        field (str): Field in the document to retrieve text from</span>
<span class="sd">        query (Optional[dict]): Opensearch JSON query DSL object.</span>
<span class="sd">            For example:</span>
<span class="sd">            { "query" : {"match": {"message": {"query": "this is a test"}}}}</span>
<span class="sd">        embedding_field (Optional[str]): If there are embeddings stored in</span>
<span class="sd">            this index, this field can be used</span>
<span class="sd">            to set the embedding field on the returned Document list.</span>


<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_opster_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">)</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">][</span><span class="s2">"hits"</span><span class="p">]:</span>
        <span class="n">value</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">][</span><span class="n">field</span><span class="p">]</span>
        <span class="n">_</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">field</span><span class="p">)</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">embedding_field</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">hit</span><span class="p">[</span><span class="s2">"_source"</span><span class="p">],</span> <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Opendal](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/)[Next Pandas ai](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/)
