Title: Load and search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/

Markdown Content:
Load and search - LlamaIndex


Ad-hoc data loader tool.

Tool that wraps any data loader, and is able to load data on-demand.

LoadAndSearchToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/#llama_index.core.tools.tool_spec.load_and_search.base.LoadAndSearchToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Load and Search Tool.

This tool can be used with other tools that load large amounts of information. Compared to OndemandLoaderTool this returns two tools, one to retrieve data to an index and another to allow the Agent to search the retrieved data with a natural language query string.

Source code in `llama-index-core/llama_index/core/tools/tool_spec/load_and_search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 19</span>
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
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LoadAndSearchToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Load and Search Tool.</span>

<span class="sd">    This tool can be used with other tools that load large amounts of</span>
<span class="sd">    information. Compared to OndemandLoaderTool this returns two tools,</span>
<span class="sd">    one to retrieve data to an index and another to allow the Agent to search</span>
<span class="sd">    the retrieved data with a natural language query string.</span>

<span class="sd">    """</span>

    <span class="n">loader_prompt</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        Use this tool to load data from the following function. It must then be read from</span>
<span class="s2">        the corresponding read_</span><span class="si">{}</span><span class="s2"> function.</span>

<span class="s2">        </span><span class="si">{}</span>
<span class="s2">    """</span>

    <span class="c1"># TODO, more general read prompt, not always natural language?</span>
    <span class="n">reader_prompt</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        Once data has been loaded from </span><span class="si">{}</span><span class="s2"> it can then be read using a natural</span>
<span class="s2">        language query from this function.</span>

<span class="s2">        You are required to pass the natural language query argument when calling this endpoint</span>

<span class="s2">        Args:</span>
<span class="s2">            query (str): The natural language query used to retreieve information from the index</span>
<span class="s2">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tool</span><span class="p">:</span> <span class="n">FunctionTool</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">],</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">ToolMetadata</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span> <span class="o">=</span> <span class="n">index_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tool</span> <span class="o">=</span> <span class="n">tool</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Tool name cannot be None"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"read_</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tool_list</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">FunctionTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">fn</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                <span class="n">description</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">loader_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">description</span>
                <span class="p">),</span>
                <span class="n">fn_schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">fn_schema</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">FunctionTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">fn</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="sa">f</span><span class="s2">"read_</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">),</span>
                <span class="n">description</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reader_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">),</span>
                <span class="n">fn_schema</span><span class="o">=</span><span class="n">create_schema_from_function</span><span class="p">(</span><span class="s2">"ReadData"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">),</span>
            <span class="p">),</span>
        <span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tool</span><span class="p">:</span> <span class="n">FunctionTool</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LoadAndSearchToolSpec"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From defaults."""</span>
        <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
        <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">name</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span>
        <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">description</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span>
        <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">fn_schema</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">tool</span><span class="o">=</span><span class="n">tool</span><span class="p">,</span>
            <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
            <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_tool_list</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">spec_functions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">func_to_metadata_mapping</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">ToolMetadata</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">FunctionTool</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tool_list</span>

    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="c1"># Call the wrapped tool and save the result in the index</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tool</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">raw_output</span>

        <span class="c1"># convert to Document if necessary</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">Document</span><span class="p">):</span>
                    <span class="n">docs</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">doc</span><span class="p">))</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">docs</span><span class="p">)]</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="n">Document</span><span class="p">):</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">docs</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">docs</span><span class="p">))]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="s2">"Content loaded! You can now search the information using read_</span><span class="si">{}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="c1"># Query the index for the result</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="s2">"Error: No content has been loaded into the index. "</span>
                <span class="sa">f</span><span class="s2">"You must call </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> first"</span>
            <span class="p">)</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/#llama_index.core.tools.tool_spec.load_and_search.base.LoadAndSearchToolSpec.from_defaults "Permanent link")

```
from_defaults(tool: [FunctionTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool "llama_index.core.tools.function_tool.FunctionTool"), index_cls: Optional[Type[[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]] = None, index_kwargs: Optional[Dict] = None, name: Optional[str] = None, description: Optional[str] = None, fn_schema: Optional[Type[BaseModel]] = None) -> [LoadAndSearchToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/#llama_index.core.tools.tool_spec.load_and_search.base.LoadAndSearchToolSpec "llama_index.core.tools.tool_spec.load_and_search.base.LoadAndSearchToolSpec")
```

From defaults.

Source code in `llama-index-core/llama_index/core/tools/tool_spec/load_and_search/base.py`

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
<span class="normal">114</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tool</span><span class="p">:</span> <span class="n">FunctionTool</span><span class="p">,</span>
    <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LoadAndSearchToolSpec"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From defaults."""</span>
    <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
    <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span>
    <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">description</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span>
    <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">fn_schema</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">tool</span><span class="o">=</span><span class="n">tool</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Jina](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/)[Next Metaphor](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/)
