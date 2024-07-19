Title: Pgvecto rs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/

Markdown Content:
Pgvecto rs - LlamaIndex


PGVectoRsStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/#llama_index.vector_stores.pgvecto_rs.PGVectoRsStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

PGVectoRs Vector Store.

**Examples:**

`pip install llama-index-vector-stores-pgvecto-rs`

```
from llama_index.vector_stores.pgvecto_rs import PGVectoRsStore

# Setup PGVectoRs client
from pgvecto_rs.sdk import PGVectoRs
import os

URL = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}".format(
    port=os.getenv("DB_PORT", "5432"),
    host=os.getenv("DB_HOST", "localhost"),
    username=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASS", "mysecretpassword"),
    db_name=os.getenv("DB_NAME", "postgres"),
)

client = PGVectoRs(
    db_url=URL,
    collection_name="example",
    dimension=1536,  # Using OpenAI’s text-embedding-ada-002
)

# Initialize PGVectoRsStore
vector_store = PGVectoRsStore(client=client)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-pgvecto-rs/llama_index/vector_stores/pgvecto_rs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 25</span>
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
<span class="normal">115</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PGVectoRsStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PGVectoRs Vector Store.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-pgvecto-rs`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.pgvecto_rs import PGVectoRsStore</span>

<span class="sd">        # Setup PGVectoRs client</span>
<span class="sd">        from pgvecto_rs.sdk import PGVectoRs</span>
<span class="sd">        import os</span>

<span class="sd">        URL = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}".format(</span>
<span class="sd">            port=os.getenv("DB_PORT", "5432"),</span>
<span class="sd">            host=os.getenv("DB_HOST", "localhost"),</span>
<span class="sd">            username=os.getenv("DB_USER", "postgres"),</span>
<span class="sd">            password=os.getenv("DB_PASS", "mysecretpassword"),</span>
<span class="sd">            db_name=os.getenv("DB_NAME", "postgres"),</span>
<span class="sd">        )</span>

<span class="sd">        client = PGVectoRs(</span>
<span class="sd">            db_url=URL,</span>
<span class="sd">            collection_name="example",</span>
<span class="sd">            dimension=1536,  # Using OpenAI’s text-embedding-ada-002</span>
<span class="sd">        )</span>

<span class="sd">        # Initialize PGVectoRsStore</span>
<span class="sd">        vector_store = PGVectoRsStore(client=client)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_client</span><span class="p">:</span> <span class="s2">"PGVectoRs"</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="s2">"PGVectoRs"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">:</span> <span class="n">PGVectoRs</span> <span class="o">=</span> <span class="n">client</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PGVectoRsStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">records</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">Record</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                <span class="n">meta</span><span class="o">=</span><span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
        <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">records</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">meta_contains</span><span class="p">({</span><span class="s2">"ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">}))</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">(</span>
                <span class="n">meta_contains</span><span class="p">(</span>
                    <span class="p">{</span><span class="n">pair</span><span class="o">.</span><span class="n">key</span><span class="p">:</span> <span class="n">pair</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">pair</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">legacy_filters</span><span class="p">()}</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
                <span class="k">else</span> <span class="kc">None</span>
            <span class="p">),</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">meta</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">record</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">record</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">results</span>
        <span class="p">]</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">similarities</span><span class="o">=</span><span class="p">[</span><span class="n">score</span> <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">results</span><span class="p">],</span>
            <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">id</span><span class="p">)</span> <span class="k">for</span> <span class="n">record</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">results</span><span class="p">],</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/)[Next Pinecone](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/)
