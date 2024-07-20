Title: Singlestore - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/

Markdown Content:
Singlestore - LlamaIndex


SingleStoreReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/#llama_index.readers.singlestore.SingleStoreReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

SingleStore reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `scheme` | `str` | 
Database Scheme.



 | _required_ |
| `host` | `str` | 

Database Host.



 | _required_ |
| `port` | `str` | 

Database Port.



 | _required_ |
| `user` | `str` | 

Database User.



 | _required_ |
| `password` | `str` | 

Database Password.



 | _required_ |
| `dbname` | `str` | 

Database Name.



 | _required_ |
| `table_name` | `str` | 

Table Name.



 | _required_ |
| `content_field` | `str` | 

Content Field.



 | `'text'` |
| `vector_field` | `str` | 

Vector Field.



 | `'embedding'` |

Source code in `llama-index-integrations/readers/llama-index-readers-singlestore/llama_index/readers/singlestore/base.py`

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
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SingleStoreReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SingleStore reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        scheme (str): Database Scheme.</span>
<span class="sd">        host (str): Database Host.</span>
<span class="sd">        port (str): Database Port.</span>
<span class="sd">        user (str): Database User.</span>
<span class="sd">        password (str): Database Password.</span>
<span class="sd">        dbname (str): Database Name.</span>
<span class="sd">        table_name (str): Table Name.</span>
<span class="sd">        content_field (str): Content Field.</span>
<span class="sd">        vector_field (str): Vector Field.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">scheme</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">dbname</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">content_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">vector_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embedding"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">scheme</span> <span class="o">=</span> <span class="n">scheme</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">host</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">port</span> <span class="o">=</span> <span class="n">port</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">user</span> <span class="o">=</span> <span class="n">user</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">password</span> <span class="o">=</span> <span class="n">password</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dbname</span> <span class="o">=</span> <span class="n">dbname</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">table_name</span> <span class="o">=</span> <span class="n">table_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">content_field</span> <span class="o">=</span> <span class="n">content_field</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span> <span class="o">=</span> <span class="n">vector_field</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pymysql</span>

            <span class="n">pymysql</span><span class="o">.</span><span class="n">install_as_MySQLdb</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">pass</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">DatabaseReader</span> <span class="o">=</span> <span class="n">DatabaseReader</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">DatabaseReader</span><span class="p">(</span>
            <span class="n">scheme</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">scheme</span><span class="p">,</span>
            <span class="n">host</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="p">,</span>
            <span class="n">user</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">user</span><span class="p">,</span>
            <span class="n">password</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">password</span><span class="p">,</span>
            <span class="n">dbname</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">dbname</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">search_embedding</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from SingleStore.</span>

<span class="sd">        Args:</span>
<span class="sd">            search_embedding (str): The embedding to search.</span>
<span class="sd">            top_k (int): Number of results to return.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">query</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        SELECT </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content_field</span><span class="si">}</span><span class="s2">, DOT_PRODUCT_F64(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span><span class="si">}</span><span class="s2">, JSON_ARRAY_PACK_F64(</span><span class="se">\'</span><span class="si">{</span><span class="n">search_embedding</span><span class="si">}</span><span class="se">\'</span><span class="s2">)) AS score</span>
<span class="s2">        FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span>
<span class="s2">        ORDER BY score</span>
<span class="s2">        DESC LIMIT </span><span class="si">{</span><span class="n">top_k</span><span class="si">}</span>
<span class="s2">        """</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/#llama_index.readers.singlestore.SingleStoreReader.load_data "Permanent link")

```
load_data(search_embedding: str, top_k: int = 5) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from SingleStore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `search_embedding` | `str` | 
The embedding to search.



 | _required_ |
| `top_k` | `int` | 

Number of results to return.



 | `5` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-singlestore/llama_index/readers/singlestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">65</span>
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
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">search_embedding</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from SingleStore.</span>

<span class="sd">    Args:</span>
<span class="sd">        search_embedding (str): The embedding to search.</span>
<span class="sd">        top_k (int): Number of results to return.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">query</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">    SELECT </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">content_field</span><span class="si">}</span><span class="s2">, DOT_PRODUCT_F64(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_field</span><span class="si">}</span><span class="s2">, JSON_ARRAY_PACK_F64(</span><span class="se">\'</span><span class="si">{</span><span class="n">search_embedding</span><span class="si">}</span><span class="se">\'</span><span class="s2">)) AS score</span>
<span class="s2">    FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">table_name</span><span class="si">}</span>
<span class="s2">    ORDER BY score</span>
<span class="s2">    DESC LIMIT </span><span class="si">{</span><span class="n">top_k</span><span class="si">}</span>
<span class="s2">    """</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple directory reader](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/)[Next Slack](https://docs.llamaindex.ai/en/stable/api_reference/readers/slack/)
