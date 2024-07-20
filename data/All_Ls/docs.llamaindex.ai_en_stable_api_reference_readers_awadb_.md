Title: Awadb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/

Markdown Content:
Awadb - LlamaIndex


AwadbReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/#llama_index.readers.awadb.AwadbReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Awadb reader.

Retrieves documents through an existing awadb client. These documents can then be used in a downstream LlamaIndex data structure.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `client` | `client` | 
An awadb client.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-awadb/llama_index/readers/awadb/base.py`

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
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AwadbReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Awadb reader.</span>

<span class="sd">    Retrieves documents through an existing awadb client.</span>
<span class="sd">    These documents can then be used in a downstream LlamaIndex data structure.</span>

<span class="sd">    Args:</span>
<span class="sd">        client (awadb.client): An awadb client.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="s2">"`awadb` package not found, please run `pip install awadb`"</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">awadb_client</span> <span class="o">=</span> <span class="n">client</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span>
        <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="n">separate_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Faiss.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (np.ndarray): A 2D numpy array of query vectors.</span>
<span class="sd">            k (int): Number of nearest neighbors to retrieve. Defaults to 4.</span>
<span class="sd">            separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">                documents. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">awadb_client</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span>
            <span class="n">k</span><span class="p">,</span>
            <span class="n">text_in_page_content</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">meta_filter</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">not_include_fields</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">item_detail</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"ResultItems"</span><span class="p">]:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">item_detail</span><span class="p">[</span><span class="s2">"embedding_text"</span><span class="p">]))</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
            <span class="c1"># join all documents into one</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/#llama_index.readers.awadb.AwadbReader.load_data "Permanent link")

```
load_data(query: ndarray, k: int = 4, separate_documents: bool = True) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Faiss.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `ndarray` | 
A 2D numpy array of query vectors.



 | _required_ |
| `k` | `int` | 

Number of nearest neighbors to retrieve. Defaults to 4.



 | `4` |
| `separate_documents` | `Optional[bool]` | 

Whether to return separate documents. Defaults to True.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-awadb/llama_index/readers/awadb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span>
    <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
    <span class="n">separate_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Faiss.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (np.ndarray): A 2D numpy array of query vectors.</span>
<span class="sd">        k (int): Number of nearest neighbors to retrieve. Defaults to 4.</span>
<span class="sd">        separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">            documents. Defaults to True.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">awadb_client</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
        <span class="n">query</span><span class="p">,</span>
        <span class="n">k</span><span class="p">,</span>
        <span class="n">text_in_page_content</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">meta_filter</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">not_include_fields</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">item_detail</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"ResultItems"</span><span class="p">]:</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">item_detail</span><span class="p">[</span><span class="s2">"embedding_text"</span><span class="p">]))</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
        <span class="c1"># join all documents into one</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Athena](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/)[Next Azcognitive search](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/)
