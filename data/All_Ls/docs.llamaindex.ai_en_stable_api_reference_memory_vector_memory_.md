Title: Vector memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/

Markdown Content:
Vector memory - LlamaIndex


Vector memory.

Memory backed by a vector database.

VectorMemory [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")`

Memory backed by a vector index.

NOTE: This class requires the `delete_nodes` method to be implemented by the vector store underlying the vector index. At time of writing (May 2024), Chroma, Qdrant and SimpleVectorStore all support delete\_nodes.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">193</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorMemory</span><span class="p">(</span><span class="n">BaseMemory</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Memory backed by a vector index.</span>

<span class="sd">    NOTE: This class requires the `delete_nodes` method to be implemented</span>
<span class="sd">    by the vector store underlying the vector index. At time of writing (May 2024),</span>
<span class="sd">    Chroma, Qdrant and SimpleVectorStore all support delete_nodes.</span>
<span class="sd">    """</span>

    <span class="n">vector_index</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">retriever_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="c1"># Whether to combine a user message with all subsequent messages</span>
    <span class="c1"># until the next user message into a single message</span>
    <span class="c1"># This is on by default, ensuring that we always fetch contiguous blocks of user/response pairs.</span>
    <span class="c1"># Turning this off may lead to errors in the function calling API of the LLM.</span>
    <span class="c1"># If this is on, then any message that's not a user message will be combined with the last user message</span>
    <span class="c1"># in the vector store.</span>
    <span class="n">batch_by_user_message</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">cur_batch_textnode</span><span class="p">:</span> <span class="n">TextNode</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">_get_starter_node_for_new_batch</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The super node for the current active user-message batch."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"vector_index"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_vector_index</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate vector index."""</span>
        <span class="c1"># NOTE: we can't import VectorStoreIndex directly due to circular imports,</span>
        <span class="c1"># which is why the type is Any</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.vector_store</span> <span class="kn">import</span> <span class="n">VectorStoreIndex</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">VectorStoreIndex</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Expected 'vector_index' to be an instance of VectorStoreIndex, got </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">value</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"VectorMemory"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">VectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retriever_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"VectorMemory"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create vector memory.</span>

<span class="sd">        Args:</span>
<span class="sd">            vector_store (Optional[VectorStore]): vector store (note: delete_nodes must</span>
<span class="sd">                be implemented. At time of writing (May 2024), Chroma, Qdrant and</span>
<span class="sd">                SimpleVectorStore all support delete_nodes.</span>
<span class="sd">            embed_model (Optional[EmbedType]): embedding model</span>
<span class="sd">            index_kwargs (Optional[Dict]): kwargs for initializing the index</span>
<span class="sd">            retriever_kwargs (Optional[Dict]): kwargs for initializing the retriever</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.indices.vector_store</span> <span class="kn">import</span> <span class="n">VectorStoreIndex</span>

        <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">retriever_kwargs</span> <span class="o">=</span> <span class="n">retriever_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="n">vector_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># initialize a blank in-memory vector store</span>
            <span class="c1"># NOTE: can't easily do that from `from_vector_store` at the moment.</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
                <span class="p">[],</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">index_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_vector_store</span><span class="p">(</span>
                <span class="n">vector_store</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">index_kwargs</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">vector_index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">retriever_kwargs</span><span class="o">=</span><span class="n">retriever_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">initial_token_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="k">if</span> <span class="nb">input</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="c1"># retrieve from index</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">retriever_kwargs</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="nb">input</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>

        <span class="c1"># retrieve underlying messages</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">sub_dict</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
            <span class="k">for</span> <span class="n">sub_dict</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sub_dicts"</span><span class="p">]</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all chat history."""</span>
        <span class="c1"># TODO: while we could implement get_all, would be hacky through metadata filtering</span>
        <span class="c1"># since vector stores don't easily support get()</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Vector memory does not support get_all method, can only retrieve based on input."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_commit_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">override_last</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Commit new node to vector store."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o">+=</span> <span class="n">sub_dict</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">""</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o">+=</span> <span class="s2">" "</span> <span class="o">+</span> <span class="p">(</span><span class="n">sub_dict</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sub_dicts"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sub_dict</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_commit_node</span><span class="p">(</span><span class="n">override_last</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### validate\_vector\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.validate_vector_index "Permanent link")

```
validate_vector_index(value: Any) -> Any
```

Validate vector index.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">71</span>
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
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"vector_index"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_vector_index</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate vector index."""</span>
    <span class="c1"># NOTE: we can't import VectorStoreIndex directly due to circular imports,</span>
    <span class="c1"># which is why the type is Any</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.indices.vector_store</span> <span class="kn">import</span> <span class="n">VectorStoreIndex</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">VectorStoreIndex</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Expected 'vector_index' to be an instance of VectorStoreIndex, got </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">value</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"VectorMemory"</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.from_defaults "Permanent link")

```
from_defaults(vector_store: Optional[[VectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore "llama_index.core.vector_stores.types.VectorStore")] = None, embed_model: Optional[EmbedType] = None, index_kwargs: Optional[Dict] = None, retriever_kwargs: Optional[Dict] = None) -> [VectorMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory "llama_index.core.memory.vector_memory.VectorMemory")
```

Create vector memory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `vector_store` | `Optional[[VectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore "llama_index.core.vector_stores.types.VectorStore")]` | 
vector store (note: delete\_nodes must be implemented. At time of writing (May 2024), Chroma, Qdrant and SimpleVectorStore all support delete\_nodes.



 | `None` |
| `embed_model` | `Optional[EmbedType]` | 

embedding model



 | `None` |
| `index_kwargs` | `Optional[Dict]` | 

kwargs for initializing the index



 | `None` |
| `retriever_kwargs` | `Optional[Dict]` | 

kwargs for initializing the retriever



 | `None` |

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 89</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">VectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EmbedType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">retriever_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"VectorMemory"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create vector memory.</span>

<span class="sd">    Args:</span>
<span class="sd">        vector_store (Optional[VectorStore]): vector store (note: delete_nodes must</span>
<span class="sd">            be implemented. At time of writing (May 2024), Chroma, Qdrant and</span>
<span class="sd">            SimpleVectorStore all support delete_nodes.</span>
<span class="sd">        embed_model (Optional[EmbedType]): embedding model</span>
<span class="sd">        index_kwargs (Optional[Dict]): kwargs for initializing the index</span>
<span class="sd">        retriever_kwargs (Optional[Dict]): kwargs for initializing the retriever</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.indices.vector_store</span> <span class="kn">import</span> <span class="n">VectorStoreIndex</span>

    <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="n">retriever_kwargs</span> <span class="o">=</span> <span class="n">retriever_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="k">if</span> <span class="n">vector_store</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># initialize a blank in-memory vector store</span>
        <span class="c1"># NOTE: can't easily do that from `from_vector_store` at the moment.</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="p">[],</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">index_kwargs</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_vector_store</span><span class="p">(</span>
            <span class="n">vector_store</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">index_kwargs</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">vector_index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">retriever_kwargs</span><span class="o">=</span><span class="n">retriever_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.get "Permanent link")

```
get(input: Optional[str] = None, initial_token_count: int = 0, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">125</span>
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
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">initial_token_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get chat history."""</span>
    <span class="k">if</span> <span class="nb">input</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="c1"># retrieve from index</span>
    <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">retriever_kwargs</span><span class="p">)</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="n">retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="nb">input</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>

    <span class="c1"># retrieve underlying messages</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">sub_dict</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
        <span class="k">for</span> <span class="n">sub_dict</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sub_dicts"</span><span class="p">]</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.get_all "Permanent link")

```
get_all() -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get all chat history.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all chat history."""</span>
    <span class="c1"># TODO: while we could implement get_all, would be hacky through metadata filtering</span>
    <span class="c1"># since vector stores don't easily support get()</span>
    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
        <span class="s2">"Vector memory does not support get_all method, can only retrieve based on input."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.put "Permanent link")

```
put(message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")) -> None
```

Put chat history.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">167</span>
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
<span class="normal">183</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put chat history."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_by_user_message</span> <span class="ow">or</span> <span class="n">message</span><span class="o">.</span><span class="n">role</span> <span class="ow">in</span> <span class="p">[</span>
        <span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span>
        <span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span>
    <span class="p">]:</span>
        <span class="c1"># if not batching by user message, commit to vector store immediately after adding</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span> <span class="o">=</span> <span class="n">_get_starter_node_for_new_batch</span><span class="p">()</span>

    <span class="c1"># update current batch textnode</span>
    <span class="n">sub_dict</span> <span class="o">=</span> <span class="n">_stringify_chat_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o">==</span> <span class="s2">""</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o">+=</span> <span class="n">sub_dict</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">""</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">text</span> <span class="o">+=</span> <span class="s2">" "</span> <span class="o">+</span> <span class="p">(</span><span class="n">sub_dict</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">cur_batch_textnode</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sub_dicts"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sub_dict</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_commit_node</span><span class="p">(</span><span class="n">override_last</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.set "Permanent link")

```
set(messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]) -> None
```

Set chat history.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### reset [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/#llama_index.core.memory.vector_memory.VectorMemory.reset "Permanent link")

```
reset() -> None
```

Reset chat history.

Source code in `llama-index-core/llama_index/core/memory/vector_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">vector_store</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple composable memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/)[Next Entity](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/)
