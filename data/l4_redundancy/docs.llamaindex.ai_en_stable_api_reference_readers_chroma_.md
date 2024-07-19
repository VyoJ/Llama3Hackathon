Title: Chroma - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/

Markdown Content:
Chroma - LlamaIndex


ChromaReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/#llama_index.readers.chroma.ChromaReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Chroma reader.

Retrieve documents from existing persisted Chroma collections.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the persisted collection.



 | _required_ |
| `persist_directory` | `Optional[str]` | 

Directory where the collection is persisted.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-chroma/llama_index/readers/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  9</span>
<span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChromaReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chroma reader.</span>

<span class="sd">    Retrieve documents from existing persisted Chroma collections.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name: Name of the persisted collection.</span>
<span class="sd">        persist_directory: Directory where the collection is persisted.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">persist_directory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chroma_api_impl</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"rest"</span><span class="p">,</span>
        <span class="n">chroma_db_impl</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"localhost"</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">8000</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"`chromadb` package not found, please run `pip install chromadb`"</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">chromadb</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">collection_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Please provide a collection name."</span><span class="p">)</span>
        <span class="c1"># from chromadb.config import Settings</span>

        <span class="k">if</span> <span class="n">persist_directory</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="o">.</span><span class="n">PersistentClient</span><span class="p">(</span>
                <span class="n">path</span><span class="o">=</span><span class="n">persist_directory</span> <span class="k">if</span> <span class="n">persist_directory</span> <span class="k">else</span> <span class="s2">"./chroma"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span><span class="n">host</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">port</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="o">.</span><span class="n">HttpClient</span><span class="p">(</span>
                <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
                <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">create_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create documents from the results.</span>

<span class="sd">        Args:</span>
<span class="sd">            results: Results from the query.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of documents.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="p">):</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">where_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load data from the collection.</span>

<span class="sd">        Args:</span>
<span class="sd">            limit: Number of results to return.</span>
<span class="sd">            where: Filter results by metadata. {"metadata_field": "is_equal_to_this"}</span>
<span class="sd">            where_document: Filter results by document. {"$contains":"search_string"}</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of documents.</span>
<span class="sd">        """</span>
        <span class="n">where</span> <span class="o">=</span> <span class="n">where</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">where_document</span> <span class="o">=</span> <span class="n">where_document</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">query_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
                <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
                <span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">query</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query</span> <span class="o">=</span> <span class="n">query</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span> <span class="k">else</span> <span class="p">[</span><span class="n">query</span><span class="p">]</span>
            <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
                <span class="n">query_texts</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
                <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
                <span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Please provide either query embedding or query."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/#llama_index.readers.chroma.ChromaReader.create_documents "Permanent link")

```
create_documents(results: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Create documents from the results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `results` | `Any` | 
Results from the query.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-chroma/llama_index/readers/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
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
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Create documents from the results.</span>

<span class="sd">    Args:</span>
<span class="sd">        results: Results from the query.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of documents.</span>
<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
        <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
    <span class="p">):</span>
        <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/#llama_index.readers.chroma.ChromaReader.load_data "Permanent link")

```
load_data(query_embedding: Optional[List[float]] = None, limit: int = 10, where: Optional[dict] = None, where_document: Optional[dict] = None, query: Optional[Union[str, List[str]]] = None) -> Any
```

Load data from the collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `limit` | `int` | 
Number of results to return.



 | `10` |
| `where` | `Optional[dict]` | 

Filter results by metadata. {"metadata\_field": "is\_equal\_to\_this"}



 | `None` |
| `where_document` | `Optional[dict]` | 

Filter results by document. {"$contains":"search\_string"}



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `Any` | 
List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-chroma/llama_index/readers/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">where_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load data from the collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        limit: Number of results to return.</span>
<span class="sd">        where: Filter results by metadata. {"metadata_field": "is_equal_to_this"}</span>
<span class="sd">        where_document: Filter results by document. {"$contains":"search_string"}</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of documents.</span>
<span class="sd">    """</span>
    <span class="n">where</span> <span class="o">=</span> <span class="n">where</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">where_document</span> <span class="o">=</span> <span class="n">where_document</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">query_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
            <span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">query</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span> <span class="k">else</span> <span class="p">[</span><span class="n">query</span><span class="p">]</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">query_texts</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
            <span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Please provide either query embedding or query."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/)[Next Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/)
