Title: Vertexai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/

Markdown Content:
Vertexai - LlamaIndex


VertexAIIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

Vertex AI Index.

The Vertex AI RAG index implements a managed index that uses Vertex AI as the backend. Vertex AI performs a lot of the functions in traditional indexes in the backend: - breaks down a document into chunks (nodes) - Creates the embedding for each chunk (node) - Performs the search for the top k most similar nodes to a query - Optionally can perform summarization of the top k nodes

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `show_progress` | `bool` | 
Whether to show tqdm progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 44</span>
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
<span class="normal">192</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VertexAIIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vertex AI Index.</span>

<span class="sd">    The Vertex AI RAG index implements a managed index that uses Vertex AI as the backend.</span>
<span class="sd">    Vertex AI performs a lot of the functions in traditional indexes in the backend:</span>
<span class="sd">    - breaks down a document into chunks (nodes)</span>
<span class="sd">    - Creates the embedding for each chunk (node)</span>
<span class="sd">    - Performs the search for the top k most similar nodes to a query</span>
<span class="sd">    - Optionally can perform summarization of the top k nodes</span>

<span class="sd">    Args:</span>
<span class="sd">        show_progress (bool): Whether to show tqdm progress bars. Defaults to False.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">location</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">corpus_display_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">corpus_description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the Vertex AI API."""</span>
        <span class="k">if</span> <span class="n">corpus_id</span> <span class="ow">and</span> <span class="p">(</span><span class="n">corpus_display_name</span> <span class="ow">or</span> <span class="n">corpus_description</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify both corpus_id and corpus_display_name or corpus_description"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">project_id</span> <span class="o">=</span> <span class="n">project_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">location</span> <span class="o">=</span> <span class="n">location</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span> <span class="o">=</span> <span class="n">get_user_agent</span><span class="p">(</span><span class="s2">"vertexai-rag"</span><span class="p">)</span>

        <span class="n">vertexai</span><span class="o">.</span><span class="n">init</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">location</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="c1"># If a corpus is not specified, create a new one.</span>
            <span class="k">if</span> <span class="n">corpus_id</span><span class="p">:</span>
                <span class="c1"># Make sure corpus exists</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span> <span class="o">=</span> <span class="n">rag</span><span class="o">.</span><span class="n">get_corpus</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">)</span><span class="o">.</span><span class="n">name</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span> <span class="o">=</span> <span class="n">rag</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span>
                    <span class="n">display_name</span><span class="o">=</span><span class="n">corpus_display_name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">corpus_description</span>
                <span class="p">)</span><span class="o">.</span><span class="n">name</span>

    <span class="k">def</span> <span class="nf">import_files</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">uris</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chunk_overlap</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImportRagFilesResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Import Google Cloud Storage or Google Drive files into the index."""</span>
        <span class="c1"># Convert https://storage.googleapis.com URLs to gs:// format</span>
        <span class="n">uris</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^https://storage\.googleapis\.com/"</span><span class="p">,</span> <span class="s2">"gs://"</span><span class="p">,</span> <span class="n">uri</span><span class="p">)</span> <span class="k">for</span> <span class="n">uri</span> <span class="ow">in</span> <span class="n">uris</span>
        <span class="p">]</span>

        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">rag</span><span class="o">.</span><span class="n">import_files</span><span class="p">(</span>
                <span class="n">corpus</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
                <span class="n">uris</span><span class="o">=</span><span class="n">uris</span><span class="p">,</span>
                <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
                <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
                <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">insert_file</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Insert a local file into the index."""</span>
        <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
            <span class="n">display_name</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"display_name"</span><span class="p">)</span>
            <span class="n">description</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="n">rag_file</span> <span class="o">=</span> <span class="n">rag</span><span class="o">.</span><span class="n">upload_file</span><span class="p">(</span>
                <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
                <span class="n">path</span><span class="o">=</span><span class="n">file_path</span><span class="p">,</span>
                <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span><span class="p">,</span>
                <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
                <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">rag_file</span><span class="o">.</span><span class="n">name</span> <span class="k">if</span> <span class="n">rag_file</span> <span class="k">else</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">list_files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""List all files in the index."""</span>
        <span class="n">files</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">rag</span><span class="o">.</span><span class="n">list_files</span><span class="p">(</span><span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">):</span>
                <span class="n">files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">files</span>

    <span class="k">def</span> <span class="nf">delete_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete file from the index."""</span>
        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="n">rag</span><span class="o">.</span><span class="n">delete_file</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">file_name</span><span class="p">,</span> <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a Retriever for this managed index."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vertexai.retriever</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">VertexAIRetriever</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"similarity_top_k"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">vector_distance_threshold</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"vector_distance_threshold"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VertexAIRetriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
            <span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">vector_distance_threshold</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Insert a set of documents (each a node)."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Node insertion is not supported."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a document and it's nodes by using ref_doc_id."""</span>
        <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
                <span class="n">rag</span><span class="o">.</span><span class="n">delete_file</span><span class="p">(</span>
                    <span class="n">name</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span>
                    <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
                <span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update a document and it's corresponding nodes."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Document update is not supported."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### import\_files [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.import_files "Permanent link")

```
import_files(uris: Sequence[str], chunk_size: Optional[int] = None, chunk_overlap: Optional[int] = None, timeout: Optional[int] = None, **kwargs: Any) -> ImportRagFilesResponse
```

Import Google Cloud Storage or Google Drive files into the index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">113</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">import_files</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">uris</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">chunk_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chunk_overlap</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImportRagFilesResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Import Google Cloud Storage or Google Drive files into the index."""</span>
    <span class="c1"># Convert https://storage.googleapis.com URLs to gs:// format</span>
    <span class="n">uris</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^https://storage\.googleapis\.com/"</span><span class="p">,</span> <span class="s2">"gs://"</span><span class="p">,</span> <span class="n">uri</span><span class="p">)</span> <span class="k">for</span> <span class="n">uri</span> <span class="ow">in</span> <span class="n">uris</span>
    <span class="p">]</span>

    <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">rag</span><span class="o">.</span><span class="n">import_files</span><span class="p">(</span>
            <span class="n">corpus</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
            <span class="n">uris</span><span class="o">=</span><span class="n">uris</span><span class="p">,</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">,</span>
            <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">chunk_overlap</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### insert\_file [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.insert_file "Permanent link")

```
insert_file(file_path: str, metadata: Optional[dict] = None, **insert_kwargs: Any) -> Optional[str]
```

Insert a local file into the index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">115</span>
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
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">insert_file</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Insert a local file into the index."""</span>
    <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
        <span class="n">display_name</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"display_name"</span><span class="p">)</span>
        <span class="n">description</span> <span class="o">=</span> <span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
        <span class="n">rag_file</span> <span class="o">=</span> <span class="n">rag</span><span class="o">.</span><span class="n">upload_file</span><span class="p">(</span>
            <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="n">file_path</span><span class="p">,</span>
            <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
            <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">rag_file</span><span class="o">.</span><span class="n">name</span> <span class="k">if</span> <span class="n">rag_file</span> <span class="k">else</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### list\_files [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.list_files "Permanent link")

```
list_files() -> Sequence[str]
```

List all files in the index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""List all files in the index."""</span>
    <span class="n">files</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">rag</span><span class="o">.</span><span class="n">list_files</span><span class="p">(</span><span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">):</span>
            <span class="n">files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">files</span>
</code></pre></div></td></tr></tbody></table>

### delete\_file [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.delete_file "Permanent link")

```
delete_file(file_name: str) -> None
```

Delete file from the index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete file from the index."""</span>
    <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
        <span class="n">rag</span><span class="o">.</span><span class="n">delete_file</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">file_name</span><span class="p">,</span> <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.as_retriever "Permanent link")

```
as_retriever(**kwargs: Any) -> [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Return a Retriever for this managed index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">158</span>
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
<span class="normal">173</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a Retriever for this managed index."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.indices.managed.vertexai.retriever</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">VertexAIRetriever</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">similarity_top_k</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"similarity_top_k"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="n">vector_distance_threshold</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"vector_distance_threshold"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VertexAIRetriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">vector_distance_threshold</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Delete a document and it's nodes by using ref\_doc\_id.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a document and it's nodes by using ref_doc_id."""</span>
    <span class="k">if</span> <span class="n">delete_from_docstore</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">telemetry</span><span class="o">.</span><span class="n">tool_context_manager</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_user_agent</span><span class="p">):</span>
            <span class="n">rag</span><span class="o">.</span><span class="n">delete_file</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span>
                <span class="n">corpus_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_name</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/#llama_index.indices.managed.vertexai.VertexAIIndex.update_ref_doc "Permanent link")

```
update_ref_doc(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **update_kwargs: Any) -> None
```

Update a document and it's corresponding nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-vertexai/llama_index/indices/managed/vertexai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update a document and it's corresponding nodes."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Document update is not supported."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vector](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/)[Next Zilliz](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/)
