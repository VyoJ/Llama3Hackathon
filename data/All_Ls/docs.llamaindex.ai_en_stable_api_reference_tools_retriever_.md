Title: Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/

Markdown Content:
Retriever - LlamaIndex


Retriever tool.

RetrieverTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/#llama_index.core.tools.retriever_tool.RetrieverTool "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")`

Retriever tool.

A tool making use of a retriever.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 
A retriever.



 | _required_ |
| `metadata` | `[ToolMetadata](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata "llama_index.core.tools.types.ToolMetadata")` | 

The associated metadata of the query engine.



 | _required_ |
| `node_postprocessors` | `Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]]` | 

A list of node postprocessors.



 | `None` |

Source code in `llama-index-core/llama_index/core/tools/retriever_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrieverTool</span><span class="p">(</span><span class="n">AsyncBaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retriever tool.</span>

<span class="sd">    A tool making use of a retriever.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (BaseRetriever): A retriever.</span>
<span class="sd">        metadata (ToolMetadata): The associated metadata of the query engine.</span>
<span class="sd">        node_postprocessors (Optional[List[BaseNodePostprocessor]]): A list of</span>
<span class="sd">            node postprocessors.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">ToolMetadata</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RetrieverTool"</span><span class="p">:</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">DEFAULT_NAME</span>
        <span class="n">description</span> <span class="o">=</span> <span class="n">description</span> <span class="ow">or</span> <span class="n">DEFAULT_DESCRIPTION</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span>

    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="n">args</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">+=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">])</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">if</span> <span class="n">kwargs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">!s}</span><span class="s2"> is </span><span class="si">{</span><span class="n">v</span><span class="si">!s}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">query_str</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot call query engine without inputs"</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">content</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_node_postprocessors</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="n">query_str</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">node_copy</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">node_copy</span><span class="o">.</span><span class="n">text_template</span> <span class="o">=</span> <span class="s2">"</span><span class="si">{metadata_str}</span><span class="se">\n</span><span class="si">{content}</span><span class="s2">"</span>
            <span class="n">node_copy</span><span class="o">.</span><span class="n">metadata_template</span> <span class="o">=</span> <span class="s2">"</span><span class="si">{key}</span><span class="s2"> = </span><span class="si">{value}</span><span class="s2">"</span>
            <span class="n">content</span> <span class="o">+=</span> <span class="n">node_copy</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"input"</span><span class="p">:</span> <span class="nb">input</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">docs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_langchain_tool</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LlamaIndexTool"</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"`as_langchain_tool` not implemented here."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_apply_node_postprocessors</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Requests](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/)[Next Salesforce](https://docs.llamaindex.ai/en/stable/api_reference/tools/salesforce/)
