Title: Dynamodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/

Markdown Content:
Dynamodb - LlamaIndex


DynamoDBVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

DynamoDB Vector Store.

In this vector store, embeddings are stored within dynamodb table. This class was implemented with reference to SimpleVectorStore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dynamodb_kvstore` | `[DynamoDBKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore "llama_index.storage.kvstore.dynamodb.DynamoDBKVStore")` | 
data store



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-dynamodb`

```
from llama_index.vector_stores.dynamodb import DynamoDBVectorStore

vector_store = DynamoDBVectorStore.from_table_name(table_name="my_table")
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-dynamodb/llama_index/vector_stores/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 33</span>
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
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DynamoDBVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DynamoDB Vector Store.</span>

<span class="sd">    In this vector store, embeddings are stored within dynamodb table.</span>
<span class="sd">    This class was implemented with reference to SimpleVectorStore.</span>

<span class="sd">    Args:</span>
<span class="sd">        dynamodb_kvstore (DynamoDBKVStore): data store</span>
<span class="sd">        namespace (Optional[str]): namespace</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-dynamodb`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.dynamodb import DynamoDBVectorStore</span>

<span class="sd">        vector_store = DynamoDBVectorStore.from_table_name(table_name="my_table")</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">_kvstore</span><span class="p">:</span> <span class="n">DynamoDBKVStore</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection_embedding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection_text_id_to_doc_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_key_value</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">dynamodb_kvstore</span><span class="p">:</span> <span class="n">DynamoDBKVStore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span> <span class="o">=</span> <span class="n">dynamodb_kvstore</span>
        <span class="n">namespace</span> <span class="o">=</span> <span class="n">namespace</span> <span class="ow">or</span> <span class="n">DEFAULT_NAMESPACE</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection_embedding</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">namespace</span><span class="si">}</span><span class="s2">/embedding"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection_text_id_to_doc_id</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">namespace</span><span class="si">}</span><span class="s2">/text_id_to_doc_id"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span> <span class="o">=</span> <span class="s2">"value"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBVectorStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load from DynamoDB table name."""</span>
        <span class="n">dynamodb_kvstore</span> <span class="o">=</span> <span class="n">DynamoDBKVStore</span><span class="o">.</span><span class="n">from_table_name</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dynamodb_kvstore</span><span class="o">=</span><span class="n">dynamodb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"DynamoDBVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get embedding."""</span>
        <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">text_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_embedding</span><span class="p">)</span>
        <span class="n">item</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span> <span class="n">item</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">key</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                <span class="n">val</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()},</span>
                <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_embedding</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">key</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                <span class="n">val</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">},</span>
                <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_text_id_to_doc_id</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">response</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="n">text_ids_to_delete</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">text_id</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_text_id_to_doc_id</span>
        <span class="p">)</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="n">top_similarities</span><span class="p">,</span> <span class="n">top_ids</span> <span class="o">=</span> <span class="n">get_top_k_embeddings</span><span class="p">(</span>
                <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
                <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">embedding_ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query mode: </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">similarities</span><span class="o">=</span><span class="n">top_similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore.client "Permanent link")

```
client: None
```

Get client.

### from\_table\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore.from_table_name "Permanent link")

```
from_table_name(table_name: str, namespace: str | None = None) -> [DynamoDBVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore "llama_index.vector_stores.dynamodb.base.DynamoDBVectorStore")
```

Load from DynamoDB table name.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-dynamodb/llama_index/vector_stores/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBVectorStore</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load from DynamoDB table name."""</span>
    <span class="n">dynamodb_kvstore</span> <span class="o">=</span> <span class="n">DynamoDBKVStore</span><span class="o">.</span><span class="n">from_table_name</span><span class="p">(</span><span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dynamodb_kvstore</span><span class="o">=</span><span class="n">dynamodb_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore.get "Permanent link")

```
get(text_id: str) -> List[float]
```

Get embedding.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-dynamodb/llama_index/vector_stores/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get embedding."""</span>
    <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">text_id</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_embedding</span><span class="p">)</span>
    <span class="n">item</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]],</span> <span class="n">item</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-dynamodb/llama_index/vector_stores/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 95</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index."""</span>
    <span class="n">response</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="n">val</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()},</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_embedding</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="n">val</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_value</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">},</span>
            <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_text_id_to_doc_id</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/#llama_index.vector_stores.dynamodb.DynamoDBVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document to delete.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-dynamodb/llama_index/vector_stores/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="n">text_ids_to_delete</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">text_id</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span>
        <span class="n">collection</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_text_id_to_doc_id</span>
    <span class="p">)</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="n">top_similarities</span><span class="p">,</span> <span class="n">top_ids</span> <span class="o">=</span> <span class="n">get_top_k_embeddings</span><span class="p">(</span>
            <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">embedding_ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid query mode: </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">similarities</span><span class="o">=</span><span class="n">top_similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Duckdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/duckdb/)[Next Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/elasticsearch/)
