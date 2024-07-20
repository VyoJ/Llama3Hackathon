Title: Hologres - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/

Markdown Content:
Hologres - LlamaIndex


HologresVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/#llama_index.vector_stores.hologres.HologresVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Hologres Vector Store.

Hologres is a one-stop real-time data warehouse, which can support high performance OLAP analysis and high QPS online services. Hologres supports vector processing and allows you to use vector data to show the characteristics of unstructured data. https://www.alibabacloud.com/help/en/hologres/user-guide/introduction-to-vector-processing

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-hologres/llama_index/vector_stores/hologres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 21</span>
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
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HologresVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hologres Vector Store.</span>

<span class="sd">    Hologres is a one-stop real-time data warehouse, which can support high performance OLAP analysis and high QPS online services.</span>
<span class="sd">    Hologres supports vector processing and allows you to use vector data</span>
<span class="sd">    to show the characteristics of unstructured data.</span>
<span class="sd">    https://www.alibabacloud.com/help/en/hologres/user-guide/introduction-to-vector-processing</span>

<span class="sd">    """</span>

    <span class="c1"># Hologres storage instance</span>
    <span class="n">_storage</span><span class="p">:</span> <span class="n">HologresVector</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="c1"># Hologres vector db stores the document node's text as string.</span>
    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">hologres_storage</span><span class="p">:</span> <span class="n">HologresVector</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Construct from a Hologres storage instance.</span>
<span class="sd">        You can use from_connection_string instead.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage</span> <span class="o">=</span> <span class="n">hologres_storage</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"document"</span><span class="p">:</span> <span class="s2">"text"</span><span class="p">},</span>
        <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1536</span><span class="p">,</span>
        <span class="n">pre_delete_table</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HologresVectorStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create Hologres Vector Store from connection string.</span>

<span class="sd">        Args:</span>
<span class="sd">            connection_string: connection string of hologres database</span>
<span class="sd">            table_name: table name to persist data</span>
<span class="sd">            table_schema: table column schemam</span>
<span class="sd">            embedding_dimension: dimension size of embedding vector</span>
<span class="sd">            pre_delete_table: whether to erase data from table on creation</span>
<span class="sd">        """</span>
        <span class="n">hologres_storage</span> <span class="o">=</span> <span class="n">HologresVector</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="p">,</span>
            <span class="n">ndims</span><span class="o">=</span><span class="n">embedding_dimension</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">table_schema</span><span class="o">=</span><span class="n">table_schema</span><span class="p">,</span>
            <span class="n">pre_delete_table</span><span class="o">=</span><span class="n">pre_delete_table</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">hologres_storage</span><span class="o">=</span><span class="n">hologres_storage</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_param</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">table_schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"document"</span><span class="p">:</span> <span class="s2">"text"</span><span class="p">},</span>
        <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1536</span><span class="p">,</span>
        <span class="n">pre_delete_table</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HologresVectorStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Create Hologres Vector Store from database configurations.</span>

<span class="sd">        Args:</span>
<span class="sd">            host: host</span>
<span class="sd">            port: port number</span>
<span class="sd">            user: hologres user</span>
<span class="sd">            password: hologres password</span>
<span class="sd">            database: hologres database</span>
<span class="sd">            table_name: hologres table name</span>
<span class="sd">            table_schema: table column schemam</span>
<span class="sd">            embedding_dimension: dimension size of embedding vector</span>
<span class="sd">            pre_delete_table: whether to erase data from table on creation</span>
<span class="sd">        """</span>
        <span class="n">connection_string</span> <span class="o">=</span> <span class="n">HologresVector</span><span class="o">.</span><span class="n">connection_string_from_db_params</span><span class="p">(</span>
            <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">database</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">password</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="o">=</span><span class="n">connection_string</span><span class="p">,</span>
            <span class="n">table_name</span><span class="o">=</span><span class="n">table_name</span><span class="p">,</span>
            <span class="n">embedding_dimension</span><span class="o">=</span><span class="n">embedding_dimension</span><span class="p">,</span>
            <span class="n">table_schema</span><span class="o">=</span><span class="n">table_schema</span><span class="p">,</span>
            <span class="n">pre_delete_table</span><span class="o">=</span><span class="n">pre_delete_table</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"HologresVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to hologres index.</span>

<span class="sd">        Embedding data will be saved to `vector` column and text will be saved to `document` column.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>
<span class="sd">        """</span>
        <span class="n">embeddings</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">schema_data_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">meta_data_list</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">text_embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
            <span class="n">embeddings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text_embedding</span><span class="p">)</span>
            <span class="n">node_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">meta_data_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
            <span class="n">schema_data_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">{</span><span class="s2">"document"</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)}</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_storage</span><span class="o">.</span><span class="n">upsert_vectors</span><span class="p">(</span>
            <span class="n">embeddings</span><span class="p">,</span> <span class="n">node_ids</span><span class="p">,</span> <span class="n">meta_data_list</span><span class="p">,</span> <span class="n">schema_data_list</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">node_ids</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_embedding (List[float]): query embedding</span>
<span class="sd">            similarity_top_k (int): top k most similar nodes</span>

<span class="sd">        """</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
        <span class="n">top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

        <span class="n">query_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">k</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span>
            <span class="n">select_columns</span><span class="o">=</span><span class="p">[</span><span class="s2">"document"</span><span class="p">,</span> <span class="s2">"vector"</span><span class="p">],</span>
            <span class="n">metadata_filters</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># if empty, then return an empty response</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_results</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">similarities</span><span class="o">=</span><span class="p">[],</span> <span class="n">ids</span><span class="o">=</span><span class="p">[])</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">query_results</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"document"</span><span class="p">],</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"vector"</span><span class="p">],</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">])</span>
        <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="n">result</span><span class="p">[</span><span class="s2">"distance"</span><span class="p">]))</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/#llama_index.vector_stores.hologres.HologresVectorStore.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-hologres/llama_index/vector_stores/hologres/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_storage</span><span class="o">.</span><span class="n">delete_vectors</span><span class="p">(</span><span class="n">metadata_filters</span><span class="o">=</span><span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Google](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/)
