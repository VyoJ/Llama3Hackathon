Title: Mongodb atlas bm25 retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/

Markdown Content:
Mongodb atlas bm25 retriever - LlamaIndex


MongoDBAtlasBM25Retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/#llama_index.retrievers.mongodb_atlas_bm25_retriever.MongoDBAtlasBM25Retriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-mongodb-atlas-bm25-retriever/llama_index/retrievers/mongodb_atlas_bm25_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
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
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MongoDBAtlasBM25Retriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">mongodb_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_db"</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_collection"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            mongodb_client: A MongoDB client.</span>
<span class="sd">            db_name: A MongoDB database name.</span>
<span class="sd">            collection_name: A MongoDB collection name.</span>
<span class="sd">            index_name: A MongoDB Atlas Vector Search index name.</span>
<span class="sd">            text_key: A MongoDB field that will contain the text for each document.</span>
<span class="sd">            metadata_key: A MongoDB field that will contain</span>
<span class="sd">        """</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="s2">"`pymongo` package not found, please run `pip install pymongo`"</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">importlib.metadata</span> <span class="kn">import</span> <span class="n">version</span>
            <span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span>
            <span class="kn">from</span> <span class="nn">pymongo.driver_info</span> <span class="kn">import</span> <span class="n">DriverInfo</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">mongodb_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">MongoClient</span><span class="p">,</span> <span class="n">mongodb_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"MONGO_URI"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify MONGO_URI via env variable "</span>
                    <span class="s2">"if not directly passing in client."</span>
                <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">(</span>
                <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"MONGO_URI"</span><span class="p">],</span>
                <span class="n">driver</span><span class="o">=</span><span class="n">DriverInfo</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">"llama-index"</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="n">version</span><span class="p">(</span><span class="s2">"llama-index"</span><span class="p">)),</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span><span class="p">[</span><span class="n">db_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="p">[</span><span class="n">collection_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="o">=</span> <span class="n">index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="o">=</span> <span class="n">text_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">=</span> <span class="n">metadata_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve nodes given query."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>

        <span class="n">pipeline</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">"$search"</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                    <span class="s2">"text"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span> <span class="s2">"path"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">},</span>
                <span class="p">}</span>
            <span class="p">},</span>
            <span class="p">{</span><span class="s2">"$addFields"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"score"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$meta"</span><span class="p">:</span> <span class="s2">"searchScore"</span><span class="p">}}},</span>
            <span class="p">{</span><span class="s2">"$sort"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"score"</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}},</span>
            <span class="p">{</span><span class="s2">"$limit"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span><span class="p">},</span>
        <span class="p">]</span>

        <span class="n">results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">aggregate</span><span class="p">(</span><span class="n">pipeline</span><span class="p">))</span>

        <span class="n">retrieve_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span><span class="p">]:</span>
            <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s2">"_id"</span><span class="p">:</span> <span class="n">result</span><span class="p">[</span><span class="s2">"_id"</span><span class="p">]})</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">doc</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">]</span>
            <span class="n">node_content</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span>
                <span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"_node_content"</span><span class="p">,</span> <span class="s2">"</span><span class="si">{}</span><span class="s2">"</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">)</span>
            <span class="n">node</span> <span class="o">=</span> <span class="kc">None</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">doc</span><span class="p">[</span><span class="s2">"text"</span><span class="p">])</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">,</span> <span class="p">{}),</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_content</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start_char_idx"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_content</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end_char_idx"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">node_content</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="p">)</span>

            <span class="n">node_with_score</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>
            <span class="n">retrieve_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_with_score</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retrieve_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/)[Next Pathway](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/)
