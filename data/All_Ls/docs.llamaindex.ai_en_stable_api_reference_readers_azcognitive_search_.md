Title: Azcognitive search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/

Markdown Content:
Azcognitive search - LlamaIndex


AzCognitiveSearchReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/#llama_index.readers.azcognitive_search.AzCognitiveSearchReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any Azure Cognitive Search index reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_name` | `str` | 
the name of azure cognitive search service.



 | _required_ |
| `search_key` | `str` | 

provide azure search access key directly.



 | _required_ |
| `index` | `str` | 

index name



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-azcognitive-search/llama_index/readers/azcognitive_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzCognitiveSearchReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any Azure Cognitive Search index reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_name (str): the name of azure cognitive search service.</span>
<span class="sd">        search_key (str): provide azure search access key directly.</span>
<span class="sd">        index (str): index name</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">searck_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Azure cognitive search service using the search key."""</span>
        <span class="kn">import</span> <span class="nn">logging</span>

        <span class="n">logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s2">"azure.core.pipeline.policies.http_logging_policy"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">WARNING</span><span class="p">)</span>

        <span class="n">azure_credential</span> <span class="o">=</span> <span class="n">AzureKeyCredential</span><span class="p">(</span><span class="n">searck_key</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">search_client</span> <span class="o">=</span> <span class="n">SearchClient</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="o">=</span><span class="sa">f</span><span class="s2">"https://</span><span class="si">{</span><span class="n">service_name</span><span class="si">}</span><span class="s2">.search.windows.net"</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index</span><span class="p">,</span>
            <span class="n">credential</span><span class="o">=</span><span class="n">azure_credential</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">content_field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Read data from azure cognitive search index.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): search term in Azure Search index</span>
<span class="sd">            content_field (str): field name of the document content.</span>
<span class="sd">            filter (str): Filter expression. For example : 'sourcepage eq</span>
<span class="sd">                'employee_handbook-3.pdf' and sourcefile eq 'employee_handbook.pdf''</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="n">search_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="n">content_field</span><span class="p">],</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span> <span class="s2">"score"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"@search.score"</span><span class="p">]},</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search_result</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/#llama_index.readers.azcognitive_search.AzCognitiveSearchReader.load_data "Permanent link")

```
load_data(query: str, content_field: str, filter: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Read data from azure cognitive search index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
search term in Azure Search index



 | _required_ |
| `content_field` | `str` | 

field name of the document content.



 | _required_ |
| `filter` | `str` | 

Filter expression. For example : 'sourcepage eq 'employee\_handbook-3.pdf' and sourcefile eq 'employee\_handbook.pdf''



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azcognitive-search/llama_index/readers/azcognitive_search/base.py`

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
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">content_field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Read data from azure cognitive search index.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): search term in Azure Search index</span>
<span class="sd">        content_field (str): field name of the document content.</span>
<span class="sd">        filter (str): Filter expression. For example : 'sourcepage eq</span>
<span class="sd">            'employee_handbook-3.pdf' and sourcefile eq 'employee_handbook.pdf''</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="n">search_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="n">content_field</span><span class="p">],</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span> <span class="s2">"score"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"@search.score"</span><span class="p">]},</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search_result</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Awadb](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/)[Next Azstorage blob](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/)
