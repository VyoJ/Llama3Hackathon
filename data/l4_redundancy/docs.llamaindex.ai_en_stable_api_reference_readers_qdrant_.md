Title: Qdrant - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/

Markdown Content:
Qdrant - LlamaIndex


QdrantReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/#llama_index.readers.qdrant.QdrantReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Qdrant reader.

Retrieve documents from existing Qdrant collections.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `location` | `Optional[str]` | 
If `:memory:` - use in-memory Qdrant instance. If `str` - use it as a `url` parameter. If `None` - use default values for `host` and `port`.



 | `None` |
| `url` | `Optional[str]` | 

either host or str of "Optional\[scheme\], host, Optional\[port\], Optional\[prefix\]". Default: `None`



 | `None` |
| `port` | `Optional[int]` | 

Port of the REST API interface. Default: 6333



 | `6333` |
| `grpc_port` | `int` | 

Port of the gRPC interface. Default: 6334



 | `6334` |
| `prefer_grpc` | `bool` | 

If `true` - use gPRC interface whenever possible in custom methods.



 | `False` |
| `https` | `Optional[bool]` | 

If `true` - use HTTPS(SSL) protocol. Default: `false`



 | `None` |
| `api_key` | `Optional[str]` | 

API key for authentication in Qdrant Cloud. Default: `None`



 | `None` |
| `prefix` | `Optional[str]` | 

If not `None` - add `prefix` to the REST URL path. Example: `service/v1` will result in `http://localhost:6333/service/v1/{qdrant-endpoint}` for REST API. Default: `None`



 | `None` |
| `timeout` | `Optional[float]` | 

Timeout for REST and gRPC API requests. Default: 5.0 seconds for REST and unlimited for gRPC



 | `None` |
| `host` | `Optional[str]` | 

Host name of Qdrant service. If url and host are None, set to 'localhost'. Default: `None`



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-qdrant/llama_index/readers/qdrant/base.py`

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
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QdrantReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Qdrant reader.</span>

<span class="sd">    Retrieve documents from existing Qdrant collections.</span>

<span class="sd">    Args:</span>
<span class="sd">        location:</span>
<span class="sd">            If `:memory:` - use in-memory Qdrant instance.</span>
<span class="sd">            If `str` - use it as a `url` parameter.</span>
<span class="sd">            If `None` - use default values for `host` and `port`.</span>
<span class="sd">        url:</span>
<span class="sd">            either host or str of</span>
<span class="sd">            "Optional[scheme], host, Optional[port], Optional[prefix]".</span>
<span class="sd">            Default: `None`</span>
<span class="sd">        port: Port of the REST API interface. Default: 6333</span>
<span class="sd">        grpc_port: Port of the gRPC interface. Default: 6334</span>
<span class="sd">        prefer_grpc: If `true` - use gPRC interface whenever possible in custom methods.</span>
<span class="sd">        https: If `true` - use HTTPS(SSL) protocol. Default: `false`</span>
<span class="sd">        api_key: API key for authentication in Qdrant Cloud. Default: `None`</span>
<span class="sd">        prefix:</span>
<span class="sd">            If not `None` - add `prefix` to the REST URL path.</span>
<span class="sd">            Example: `service/v1` will result in</span>
<span class="sd">            `http://localhost:6333/service/v1/{qdrant-endpoint}` for REST API.</span>
<span class="sd">            Default: `None`</span>
<span class="sd">        timeout:</span>
<span class="sd">            Timeout for REST and gRPC API requests.</span>
<span class="sd">            Default: 5.0 seconds for REST and unlimited for gRPC</span>
<span class="sd">        host: Host name of Qdrant service. If url and host are None, set to 'localhost'.</span>
<span class="sd">            Default: `None`</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">location</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">6333</span><span class="p">,</span>
        <span class="n">grpc_port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">6334</span><span class="p">,</span>
        <span class="n">prefer_grpc</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">https</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"`qdrant-client` package not found, please run `pip install qdrant-client`"</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">qdrant_client</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">qdrant_client</span><span class="o">.</span><span class="n">QdrantClient</span><span class="p">(</span>
            <span class="n">location</span><span class="o">=</span><span class="n">location</span><span class="p">,</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="n">grpc_port</span><span class="o">=</span><span class="n">grpc_port</span><span class="p">,</span>
            <span class="n">prefer_grpc</span><span class="o">=</span><span class="n">prefer_grpc</span><span class="p">,</span>
            <span class="n">https</span><span class="o">=</span><span class="n">https</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="n">prefix</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="n">path</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
        <span class="n">should_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">must_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">must_not_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">rang_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Qdrant.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_name (str): Name of the Qdrant collection.</span>
<span class="sd">            query_vector (List[float]): Query vector.</span>
<span class="sd">            should_search_mapping (Optional[Dict[str, str]]): Mapping from field name</span>
<span class="sd">                to query string.</span>
<span class="sd">            must_search_mapping (Optional[Dict[str, str]]): Mapping from field name</span>
<span class="sd">                to query string.</span>
<span class="sd">            must_not_search_mapping (Optional[Dict[str, str]]): Mapping from field</span>
<span class="sd">                name to query string.</span>
<span class="sd">            rang_search_mapping (Optional[Dict[str, Dict[str, float]]]): Mapping from</span>
<span class="sd">                field name to range query.</span>
<span class="sd">            limit (int): Number of results to return.</span>

<span class="sd">        Example:</span>
<span class="sd">            reader = QdrantReader()</span>
<span class="sd">            reader.load_data(</span>
<span class="sd">                 collection_name="test_collection",</span>
<span class="sd">                 query_vector=[0.1, 0.2, 0.3],</span>
<span class="sd">                 should_search_mapping={"text_field": "text"},</span>
<span class="sd">                 must_search_mapping={"text_field": "text"},</span>
<span class="sd">                 must_not_search_mapping={"text_field": "text"},</span>
<span class="sd">                 # gte, lte, gt, lt supported</span>
<span class="sd">                 rang_search_mapping={"text_field": {"gte": 0.1, "lte": 0.2}},</span>
<span class="sd">                 limit=10</span>
<span class="sd">            )</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">qdrant_client.http.models</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">FieldCondition</span><span class="p">,</span>
            <span class="n">Filter</span><span class="p">,</span>
            <span class="n">MatchText</span><span class="p">,</span>
            <span class="n">MatchValue</span><span class="p">,</span>
            <span class="n">Range</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">qdrant_client.http.models.models</span> <span class="kn">import</span> <span class="n">Payload</span>

        <span class="n">should_search_mapping</span> <span class="o">=</span> <span class="n">should_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">must_search_mapping</span> <span class="o">=</span> <span class="n">must_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">must_not_search_mapping</span> <span class="o">=</span> <span class="n">must_not_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">rang_search_mapping</span> <span class="o">=</span> <span class="n">rang_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="n">should_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchText</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">should_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">should_search_mapping</span>
        <span class="p">]</span>
        <span class="n">must_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">must_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">must_search_mapping</span>
        <span class="p">]</span>
        <span class="n">must_not_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">must_not_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">must_not_search_mapping</span>
        <span class="p">]</span>
        <span class="n">rang_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">FieldCondition</span><span class="p">(</span>
                <span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span>
                <span class="nb">range</span><span class="o">=</span><span class="n">Range</span><span class="p">(</span>
                    <span class="n">gte</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gte"</span><span class="p">),</span>
                    <span class="n">lte</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lte"</span><span class="p">),</span>
                    <span class="n">gt</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gt"</span><span class="p">),</span>
                    <span class="n">lt</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lt"</span><span class="p">),</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">rang_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">rang_search_mapping</span>
        <span class="p">]</span>
        <span class="n">should_search_conditions</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">rang_search_conditions</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">query_vector</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
            <span class="n">query_filter</span><span class="o">=</span><span class="n">Filter</span><span class="p">(</span>
                <span class="n">must</span><span class="o">=</span><span class="n">must_search_conditions</span><span class="p">,</span>
                <span class="n">must_not</span><span class="o">=</span><span class="n">must_not_search_conditions</span><span class="p">,</span>
                <span class="n">should</span><span class="o">=</span><span class="n">should_search_conditions</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">with_vectors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">with_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">payload</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Payload</span><span class="p">,</span> <span class="n">point</span><span class="o">.</span><span class="n">payload</span><span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">vector</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">point</span><span class="o">.</span><span class="n">vector</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Could not cast vector to List[float]."</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">),</span>
                <span class="n">text</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text"</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/#llama_index.readers.qdrant.QdrantReader.load_data "Permanent link")

```
load_data(collection_name: str, query_vector: List[float], should_search_mapping: Optional[Dict[str, str]] = None, must_search_mapping: Optional[Dict[str, str]] = None, must_not_search_mapping: Optional[Dict[str, str]] = None, rang_search_mapping: Optional[Dict[str, Dict[str, float]]] = None, limit: int = 10) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Qdrant.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the Qdrant collection.



 | _required_ |
| `query_vector` | `List[float]` | 

Query vector.



 | _required_ |
| `should_search_mapping` | `Optional[Dict[str, str]]` | 

Mapping from field name to query string.



 | `None` |
| `must_search_mapping` | `Optional[Dict[str, str]]` | 

Mapping from field name to query string.



 | `None` |
| `must_not_search_mapping` | `Optional[Dict[str, str]]` | 

Mapping from field name to query string.



 | `None` |
| `rang_search_mapping` | `Optional[Dict[str, Dict[str, float]]]` | 

Mapping from field name to range query.



 | `None` |
| `limit` | `int` | 

Number of results to return.



 | `10` |

Examplereader = QdrantReader() reader.load\_data( collection\_name="test\_collection", query\_vector=\[0.1, 0.2, 0.3\], should\_search\_mapping={"text\_field": "text"}, must\_search\_mapping={"text\_field": "text"}, must\_not\_search\_mapping={"text\_field": "text"}, # gte, lte, gt, lt supported rang\_search\_mapping={"text\_field": {"gte": 0.1, "lte": 0.2}}, limit=10 )

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-qdrant/llama_index/readers/qdrant/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 77</span>
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
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
    <span class="n">should_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">must_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">must_not_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">rang_search_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Qdrant.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): Name of the Qdrant collection.</span>
<span class="sd">        query_vector (List[float]): Query vector.</span>
<span class="sd">        should_search_mapping (Optional[Dict[str, str]]): Mapping from field name</span>
<span class="sd">            to query string.</span>
<span class="sd">        must_search_mapping (Optional[Dict[str, str]]): Mapping from field name</span>
<span class="sd">            to query string.</span>
<span class="sd">        must_not_search_mapping (Optional[Dict[str, str]]): Mapping from field</span>
<span class="sd">            name to query string.</span>
<span class="sd">        rang_search_mapping (Optional[Dict[str, Dict[str, float]]]): Mapping from</span>
<span class="sd">            field name to range query.</span>
<span class="sd">        limit (int): Number of results to return.</span>

<span class="sd">    Example:</span>
<span class="sd">        reader = QdrantReader()</span>
<span class="sd">        reader.load_data(</span>
<span class="sd">             collection_name="test_collection",</span>
<span class="sd">             query_vector=[0.1, 0.2, 0.3],</span>
<span class="sd">             should_search_mapping={"text_field": "text"},</span>
<span class="sd">             must_search_mapping={"text_field": "text"},</span>
<span class="sd">             must_not_search_mapping={"text_field": "text"},</span>
<span class="sd">             # gte, lte, gt, lt supported</span>
<span class="sd">             rang_search_mapping={"text_field": {"gte": 0.1, "lte": 0.2}},</span>
<span class="sd">             limit=10</span>
<span class="sd">        )</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">qdrant_client.http.models</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">FieldCondition</span><span class="p">,</span>
        <span class="n">Filter</span><span class="p">,</span>
        <span class="n">MatchText</span><span class="p">,</span>
        <span class="n">MatchValue</span><span class="p">,</span>
        <span class="n">Range</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="kn">from</span> <span class="nn">qdrant_client.http.models.models</span> <span class="kn">import</span> <span class="n">Payload</span>

    <span class="n">should_search_mapping</span> <span class="o">=</span> <span class="n">should_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">must_search_mapping</span> <span class="o">=</span> <span class="n">must_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">must_not_search_mapping</span> <span class="o">=</span> <span class="n">must_not_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">rang_search_mapping</span> <span class="o">=</span> <span class="n">rang_search_mapping</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="n">should_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchText</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">should_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">should_search_mapping</span>
    <span class="p">]</span>
    <span class="n">must_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">must_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">must_search_mapping</span>
    <span class="p">]</span>
    <span class="n">must_not_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">FieldCondition</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="n">MatchValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">value</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">must_not_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">must_not_search_mapping</span>
    <span class="p">]</span>
    <span class="n">rang_search_conditions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">FieldCondition</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span>
            <span class="nb">range</span><span class="o">=</span><span class="n">Range</span><span class="p">(</span>
                <span class="n">gte</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gte"</span><span class="p">),</span>
                <span class="n">lte</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lte"</span><span class="p">),</span>
                <span class="n">gt</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gt"</span><span class="p">),</span>
                <span class="n">lt</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"lt"</span><span class="p">),</span>
            <span class="p">),</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">rang_search_mapping</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">rang_search_mapping</span>
    <span class="p">]</span>
    <span class="n">should_search_conditions</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">rang_search_conditions</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
        <span class="n">query_vector</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
        <span class="n">query_filter</span><span class="o">=</span><span class="n">Filter</span><span class="p">(</span>
            <span class="n">must</span><span class="o">=</span><span class="n">must_search_conditions</span><span class="p">,</span>
            <span class="n">must_not</span><span class="o">=</span><span class="n">must_not_search_conditions</span><span class="p">,</span>
            <span class="n">should</span><span class="o">=</span><span class="n">should_search_conditions</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">with_vectors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">with_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Payload</span><span class="p">,</span> <span class="n">point</span><span class="o">.</span><span class="n">payload</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">vector</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">point</span><span class="o">.</span><span class="n">vector</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Could not cast vector to List[float]."</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
        <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">),</span>
            <span class="n">text</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text"</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">),</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">vector</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Psychic](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/)[Next Rayyan](https://docs.llamaindex.ai/en/stable/api_reference/readers/rayyan/)
