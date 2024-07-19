Title: Chatgpt plugin - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/

Markdown Content:
Chatgpt plugin - LlamaIndex


ChatGPTRetrievalPluginClient [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/#llama_index.vector_stores.chatgpt_plugin.ChatGPTRetrievalPluginClient "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

ChatGPT Retrieval Plugin Client.

In this client, we make use of the endpoints defined by ChatGPT.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `endpoint_url` | `str` | 
URL of the ChatGPT Retrieval Plugin.



 | _required_ |
| `bearer_token` | `Optional[str]` | 

Bearer token for the ChatGPT Retrieval Plugin.



 | `None` |
| `retries` | `Optional[Retry]` | 

Retry object for the ChatGPT Retrieval Plugin.



 | `None` |
| `batch_size` | `int` | 

Batch size for the ChatGPT Retrieval Plugin.



 | `100` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chatgpt-plugin/llama_index/vector_stores/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 58</span>
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
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatGPTRetrievalPluginClient</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ChatGPT Retrieval Plugin Client.</span>

<span class="sd">    In this client, we make use of the endpoints defined by ChatGPT.</span>

<span class="sd">    Args:</span>
<span class="sd">        endpoint_url (str): URL of the ChatGPT Retrieval Plugin.</span>
<span class="sd">        bearer_token (Optional[str]): Bearer token for the ChatGPT Retrieval Plugin.</span>
<span class="sd">        retries (Optional[Retry]): Retry object for the ChatGPT Retrieval Plugin.</span>
<span class="sd">        batch_size (int): Batch size for the ChatGPT Retrieval Plugin.</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">is_embedding_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">_endpoint_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_bearer_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_retries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Retry</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_s</span><span class="p">:</span> <span class="n">requests</span><span class="o">.</span><span class="n">Session</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">endpoint_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bearer_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Retry</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span> <span class="o">=</span> <span class="n">endpoint_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span> <span class="o">=</span> <span class="n">bearer_token</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"BEARER_TOKEN"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retries</span> <span class="o">=</span> <span class="n">retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span> <span class="o">=</span> <span class="n">batch_size</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">mount</span><span class="p">(</span><span class="s2">"http://"</span><span class="p">,</span> <span class="n">HTTPAdapter</span><span class="p">(</span><span class="n">max_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_retries</span><span class="p">))</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ChatGPTRetrievalPluginClient"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index."""</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>

        <span class="n">docs_to_upload</span> <span class="o">=</span> <span class="n">convert_docs_to_json</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">iterable_docs</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_upload</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span><span class="p">),</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">desc</span><span class="o">=</span><span class="s2">"Uploading documents"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">iterable_docs</span><span class="p">:</span>
            <span class="n">i_end</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_upload</span><span class="p">))</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/upsert"</span><span class="p">,</span>
                <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
                <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"documents"</span><span class="p">:</span> <span class="n">docs_to_upload</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i_end</span><span class="p">]},</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/delete"</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Metadata filters not implemented for ChatGPT Plugin yet."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str must be provided"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
        <span class="c1"># TODO: add metadata filter</span>
        <span class="n">queries</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="s2">"top_k"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">}]</span>
        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/query"</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"queries"</span><span class="p">:</span> <span class="n">queries</span><span class="p">}</span>
        <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">query_result</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">query_result</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
                <span class="n">result_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
                <span class="n">result_txt</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
                <span class="n">result_score</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span>
                <span class="n">result_ref_doc_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">]</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">result_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">result_txt</span><span class="p">,</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="p">{</span>
                        <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">:</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span>
                            <span class="n">node_id</span><span class="o">=</span><span class="n">result_ref_doc_id</span>
                        <span class="p">)</span>
                    <span class="p">},</span>
                <span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result_score</span><span class="p">)</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result_id</span><span class="p">)</span>

            <span class="c1"># NOTE: there should only be one query</span>
            <span class="k">break</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/#llama_index.vector_stores.chatgpt_plugin.ChatGPTRetrievalPluginClient.client "Permanent link")

```
client: None
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/#llama_index.vector_stores.chatgpt_plugin.ChatGPTRetrievalPluginClient.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chatgpt-plugin/llama_index/vector_stores/chatgpt_plugin/base.py`

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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index."""</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>

    <span class="n">docs_to_upload</span> <span class="o">=</span> <span class="n">convert_docs_to_json</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
    <span class="n">iterable_docs</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
        <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_upload</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span><span class="p">),</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">desc</span><span class="o">=</span><span class="s2">"Uploading documents"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">iterable_docs</span><span class="p">:</span>
        <span class="n">i_end</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">docs_to_upload</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/upsert"</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"documents"</span><span class="p">:</span> <span class="n">docs_to_upload</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i_end</span><span class="p">]},</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/#llama_index.vector_stores.chatgpt_plugin.ChatGPTRetrievalPluginClient.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chatgpt-plugin/llama_index/vector_stores/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">131</span>
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
<span class="normal">144</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/delete"</span><span class="p">,</span>
        <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
        <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="p">[</span><span class="n">ref_doc_id</span><span class="p">]},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/#llama_index.vector_stores.chatgpt_plugin.ChatGPTRetrievalPluginClient.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Get nodes for response.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chatgpt-plugin/llama_index/vector_stores/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
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
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get nodes for response."""</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Metadata filters not implemented for ChatGPT Plugin yet."</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str must be provided"</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
    <span class="c1"># TODO: add metadata filter</span>
    <span class="n">queries</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="s2">"top_k"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">}]</span>
    <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/query"</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"queries"</span><span class="p">:</span> <span class="n">queries</span><span class="p">}</span>
    <span class="p">)</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">query_result</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"results"</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">query_result</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="n">result_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
            <span class="n">result_txt</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
            <span class="n">result_score</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span>
            <span class="n">result_ref_doc_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">]</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">result_id</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result_txt</span><span class="p">,</span>
                <span class="n">relationships</span><span class="o">=</span><span class="p">{</span>
                    <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">:</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span>
                        <span class="n">node_id</span><span class="o">=</span><span class="n">result_ref_doc_id</span>
                    <span class="p">)</span>
                <span class="p">},</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result_score</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result_id</span><span class="p">)</span>

        <span class="c1"># NOTE: there should only be one query</span>
        <span class="k">break</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/cassandra/)[Next Chroma](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/)
