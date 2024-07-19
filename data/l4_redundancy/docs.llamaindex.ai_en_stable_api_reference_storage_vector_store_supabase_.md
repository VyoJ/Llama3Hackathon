Title: Supabase - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/

Markdown Content:
Supabase - LlamaIndex


SupabaseVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Supbabase Vector.

In this vector store, embeddings are stored in Postgres table using pgvector.

During query time, the index uses pgvector/Supabase to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `postgres_connection_string` | `str` | 
postgres connection string



 | _required_ |
| `collection_name` | `str` | 

name of the collection to store the embeddings in



 | _required_ |
| `dimension` | `int` | 

dimension of the embeddings. Defaults to 1536.



 | `DEFAULT_EMBEDDING_DIM` |

**Examples:**

`pip install llama-index-vector-stores-supabase`

```
from llama_index.vector_stores.supabase import SupabaseVectorStore

# Set up SupabaseVectorStore
vector_store = SupabaseVectorStore(
    postgres_connection_string="postgresql://<user>:<password>@<host>:<port>/<db_name>",
    collection_name="base_demo",
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-supabase/llama_index/vector_stores/supabase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 27</span>
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
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SupabaseVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Supbabase Vector.</span>

<span class="sd">    In this vector store, embeddings are stored in Postgres table using pgvector.</span>

<span class="sd">    During query time, the index uses pgvector/Supabase to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        postgres_connection_string (str):</span>
<span class="sd">            postgres connection string</span>
<span class="sd">        collection_name (str):</span>
<span class="sd">            name of the collection to store the embeddings in</span>
<span class="sd">        dimension (int, optional):</span>
<span class="sd">            dimension of the embeddings. Defaults to 1536.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-supabase`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.supabase import SupabaseVectorStore</span>

<span class="sd">        # Set up SupabaseVectorStore</span>
<span class="sd">        vector_store = SupabaseVectorStore(</span>
<span class="sd">            postgres_connection_string="postgresql://&lt;user&gt;:&lt;password&gt;@&lt;host&gt;:&lt;port&gt;/&lt;db_name&gt;",</span>
<span class="sd">            collection_name="base_demo",</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Collection</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">postgres_connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_EMBEDDING_DIM</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">vecs</span><span class="o">.</span><span class="n">create_client</span><span class="p">(</span><span class="n">postgres_connection_string</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">CollectionNotFound</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Collection </span><span class="si">{</span><span class="n">collection_name</span><span class="si">}</span><span class="s2"> does not exist, "</span>
                <span class="sa">f</span><span class="s2">"try creating one with dimension=</span><span class="si">{</span><span class="n">dimension</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">create_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span> <span class="n">dimension</span><span class="o">=</span><span class="n">dimension</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Close the client when the object is deleted."""</span>
        <span class="k">try</span><span class="p">:</span>  <span class="c1"># try-catch in case the attribute is not present</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
            <span class="k">pass</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">_to_vecs_filters</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filters</span><span class="p">:</span> <span class="n">MetadataFilters</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert llama filters to vecs filters. $eq is the only supported operator."""</span>
        <span class="n">vecs_filter</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="n">filter_cond</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"$</span><span class="si">{</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>

        <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">filters</span><span class="o">.</span><span class="n">legacy_filters</span><span class="p">():</span>
            <span class="n">sub_filter</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">sub_filter</span><span class="p">[</span><span class="n">f</span><span class="o">.</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"$eq"</span><span class="p">:</span> <span class="n">f</span><span class="o">.</span><span class="n">value</span><span class="p">}</span>
            <span class="n">vecs_filter</span><span class="p">[</span><span class="n">filter_cond</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sub_filter</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">vecs_filter</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="c1"># NOTE: keep text in metadata dict since there's no special field in</span>
            <span class="c1">#       Supabase Vector.</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>

            <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span> <span class="n">metadata_dict</span><span class="p">))</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">get_by_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get row ids by doc id.</span>

<span class="sd">        Args:</span>
<span class="sd">            doc_id (str): document id</span>
<span class="sd">        """</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$eq"</span><span class="p">:</span> <span class="n">doc_id</span><span class="p">}}</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">data</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
            <span class="n">include_value</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># NOTE: list of row ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete doc.</span>

<span class="sd">        Args:</span>
<span class="sd">            :param ref_doc_id (str): document id</span>

<span class="sd">        """</span>
        <span class="n">row_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_by_id</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">row_ids</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">row_ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (List[float]): query embedding</span>

<span class="sd">        """</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_vecs_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">data</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
            <span class="n">include_value</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">id_</span><span class="p">,</span> <span class="n">distance</span><span class="p">,</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
<span class="w">            </span><span class="sd">"""shape of the result is [(vector, distance, metadata)]"""</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                    <span class="n">metadata</span>
                <span class="p">)</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mf">1.0</span> <span class="o">-</span> <span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="n">distance</span><span class="p">))</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">id_</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore.client "Permanent link")

```
client: None
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-supabase/llama_index/vector_stores/supabase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="c1"># NOTE: keep text in metadata dict since there's no special field in</span>
        <span class="c1">#       Supabase Vector.</span>
        <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
        <span class="p">)</span>

        <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span> <span class="n">metadata_dict</span><span class="p">))</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span><span class="n">records</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### get\_by\_id [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore.get_by_id "Permanent link")

```
get_by_id(doc_id: str, **kwargs: Any) -> list
```

Get row ids by doc id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `doc_id` | `str` | 
document id



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-supabase/llama_index/vector_stores/supabase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
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
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_by_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get row ids by doc id.</span>

<span class="sd">    Args:</span>
<span class="sd">        doc_id (str): document id</span>
<span class="sd">    """</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$eq"</span><span class="p">:</span> <span class="n">doc_id</span><span class="p">}}</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="n">data</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
        <span class="n">include_value</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete doc.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  |  | 
param ref\_doc\_id (str): document id



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-supabase/llama_index/vector_stores/supabase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete doc.</span>

<span class="sd">    Args:</span>
<span class="sd">        :param ref_doc_id (str): document id</span>

<span class="sd">    """</span>
    <span class="n">row_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_by_id</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">row_ids</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">row_ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/#llama_index.vector_stores.supabase.SupabaseVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `List[float]` | 
query embedding



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-supabase/llama_index/vector_stores/supabase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (List[float]): query embedding</span>

<span class="sd">    """</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_vecs_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="n">data</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
        <span class="n">include_value</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">id_</span><span class="p">,</span> <span class="n">distance</span><span class="p">,</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""shape of the result is [(vector, distance, metadata)]"""</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
            <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                <span class="n">metadata</span>
            <span class="p">)</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mf">1.0</span> <span class="o">-</span> <span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="n">distance</span><span class="p">))</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">id_</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Singlestoredb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/)[Next Tair](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tair/)
