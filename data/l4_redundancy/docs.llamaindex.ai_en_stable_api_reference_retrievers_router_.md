Title: Router - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/

Markdown Content:
Router - LlamaIndex


RouterRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/#llama_index.core.retrievers.RouterRetriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Router retriever.

Selects one (or multiple) out of several candidate retrievers to execute a query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `selector` | `BaseSelector` | 
A selector that chooses one out of many options based on each candidate's metadata and query.



 | _required_ |
| `retriever_tools` | `Sequence[[RetrieverTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/#llama_index.core.tools.retriever_tool.RetrieverTool "llama_index.core.tools.retriever_tool.RetrieverTool")]` | 

A sequence of candidate retrievers. They must be wrapped as tools to expose metadata to the selector.



 | _required_ |

Source code in `llama-index-core/llama_index/core/retrievers/router_retriever.py`

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
<span class="normal">151</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RouterRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Router retriever.</span>

<span class="sd">    Selects one (or multiple) out of several candidate retrievers to execute a query.</span>

<span class="sd">    Args:</span>
<span class="sd">        selector (BaseSelector): A selector that chooses one out of many options based</span>
<span class="sd">            on each candidate's metadata and query.</span>
<span class="sd">        retriever_tools (Sequence[RetrieverTool]): A sequence of candidate</span>
<span class="sd">            retrievers. They must be wrapped as tools to expose metadata to</span>
<span class="sd">            the selector.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">BaseSelector</span><span class="p">,</span>
        <span class="n">retriever_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">RetrieverTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span> <span class="o">=</span> <span class="n">selector</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseRetriever</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">retriever</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">retriever_tools</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">retriever_tools</span><span class="p">]</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">),</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">objects</span><span class="o">=</span><span class="n">objects</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="c1"># NOTE: don't include tools for now</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"selector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">retriever_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">RetrieverTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSelector</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">select_multi</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RouterRetriever"</span><span class="p">:</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="n">selector</span> <span class="o">=</span> <span class="n">selector</span> <span class="ow">or</span> <span class="n">get_selector_from_llm</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">is_multi</span><span class="o">=</span><span class="n">select_multi</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">selector</span><span class="p">,</span>
            <span class="n">retriever_tools</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">retrieved_results</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">engine_ind</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">):</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Selecting retriever </span><span class="si">{</span><span class="n">engine_ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reasons</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s2">."</span>
                    <span class="p">)</span>
                    <span class="n">selected_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span><span class="p">[</span><span class="n">engine_ind</span><span class="p">]</span>
                    <span class="n">cur_results</span> <span class="o">=</span> <span class="n">selected_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                    <span class="n">retrieved_results</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">cur_results</span><span class="p">})</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">selected_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Selecting retriever </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Failed to select retriever"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

                <span class="n">cur_results</span> <span class="o">=</span> <span class="n">selected_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">retrieved_results</span> <span class="o">=</span> <span class="p">{</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">cur_results</span><span class="p">}</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">retrieved_results</span><span class="o">.</span><span class="n">values</span><span class="p">()})</span>

        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">retrieved_results</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_selector</span><span class="o">.</span><span class="n">aselect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">retrieved_results</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">engine_ind</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">inds</span><span class="p">):</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Selecting retriever </span><span class="si">{</span><span class="n">engine_ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reasons</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s2">."</span>
                    <span class="p">)</span>
                    <span class="n">selected_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span><span class="p">[</span><span class="n">engine_ind</span><span class="p">]</span>
                    <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">selected_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">))</span>

                <span class="n">results_of_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
                <span class="n">cur_results</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">item</span> <span class="k">for</span> <span class="n">sublist</span> <span class="ow">in</span> <span class="n">results_of_results</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">sublist</span>
                <span class="p">]</span>
                <span class="n">retrieved_results</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">cur_results</span><span class="p">})</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">selected_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrievers</span><span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Selecting retriever </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Failed to select retriever"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

                <span class="n">cur_results</span> <span class="o">=</span> <span class="k">await</span> <span class="n">selected_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
                <span class="n">retrieved_results</span> <span class="o">=</span> <span class="p">{</span><span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">cur_results</span><span class="p">}</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">retrieved_results</span><span class="o">.</span><span class="n">values</span><span class="p">()})</span>

        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">retrieved_results</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Recursive](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/)[Next Sql](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/)
