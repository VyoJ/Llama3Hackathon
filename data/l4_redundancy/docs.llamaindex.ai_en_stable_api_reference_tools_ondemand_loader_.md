Title: Ondemand loader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/

Markdown Content:
Ondemand loader - LlamaIndex


Ad-hoc data loader tool.

Tool that wraps any data loader, and is able to load data on-demand.

OnDemandLoaderTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")`

On-demand data loader tool.

Loads data with by calling the provided loader function, stores in index, and queries for relevant data with a natural language query string.

Source code in `llama-index-core/llama_index/core/tools/ondemand_loader_tool.py`

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
<span class="normal">168</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OnDemandLoaderTool</span><span class="p">(</span><span class="n">AsyncBaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""On-demand data loader tool.</span>

<span class="sd">    Loads data with by calling the provided loader function,</span>
<span class="sd">    stores in index, and queries for relevant data with a</span>
<span class="sd">    natural language query string.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">loader</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]],</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">],</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">ToolMetadata</span><span class="p">,</span>
        <span class="n">use_query_str_in_loader</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">query_str_kwargs_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"query_str"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_loader</span> <span class="o">=</span> <span class="n">loader</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span> <span class="o">=</span> <span class="n">index_cls</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_query_str_in_loader</span> <span class="o">=</span> <span class="n">use_query_str_in_loader</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_str_kwargs_key</span> <span class="o">=</span> <span class="n">query_str_kwargs_key</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">reader</span><span class="p">:</span> <span class="n">BaseReader</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_query_str_in_loader</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">query_str_kwargs_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"query_str"</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OnDemandLoaderTool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From defaults."""</span>
        <span class="c1"># NOTE: fn_schema should be specified if you want to use as langchain Tool</span>

        <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
        <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Tool to load data from </span><span class="si">{</span><span class="n">reader</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">create_schema_from_function</span><span class="p">(</span>
                <span class="n">name</span> <span class="ow">or</span> <span class="s2">"LoadData"</span><span class="p">,</span>
                <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">,</span>
                <span class="p">[(</span><span class="n">query_str_kwargs_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">)],</span>
            <span class="p">)</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">loader</span><span class="o">=</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">,</span>
            <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
            <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
            <span class="n">use_query_str_in_loader</span><span class="o">=</span><span class="n">use_query_str_in_loader</span><span class="p">,</span>
            <span class="n">query_str_kwargs_key</span><span class="o">=</span><span class="n">query_str_kwargs_key</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tool</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tool</span><span class="p">:</span> <span class="n">FunctionTool</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_query_str_in_loader</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">query_str_kwargs_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"query_str"</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">return_direct</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OnDemandLoaderTool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From defaults."""</span>
        <span class="c1"># NOTE: fn_schema should be specified if you want to use as langchain Tool</span>

        <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
        <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Tool to load data from </span><span class="si">{</span><span class="n">tool</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">create_schema_from_function</span><span class="p">(</span>
                <span class="n">name</span> <span class="ow">or</span> <span class="s2">"LoadData"</span><span class="p">,</span> <span class="n">tool</span><span class="o">.</span><span class="n">_fn</span><span class="p">,</span> <span class="p">[(</span><span class="n">query_str_kwargs_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">)]</span>
            <span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
            <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">,</span>
            <span class="n">return_direct</span><span class="o">=</span><span class="n">return_direct</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">loader</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">_fn</span><span class="p">,</span>
            <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
            <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
            <span class="n">use_query_str_in_loader</span><span class="o">=</span><span class="n">use_query_str_in_loader</span><span class="p">,</span>
            <span class="n">query_str_kwargs_key</span><span class="o">=</span><span class="n">query_str_kwargs_key</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_parse_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_str_kwargs_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Missing query_str in kwargs with parameter name: "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_str_kwargs_key</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_query_str_in_loader</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_str_kwargs_key</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_str_kwargs_key</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loader</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">query_str</span><span class="p">,</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Call."""</span>
        <span class="n">query_str</span><span class="p">,</span> <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_args</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
        <span class="c1"># TODO: add query kwargs</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async Call."""</span>
        <span class="n">query_str</span><span class="p">,</span> <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_args</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
        <span class="c1"># TODO: add query kwargs</span>
        <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool.from_defaults "Permanent link")

```
from_defaults(reader: [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader"), index_cls: Optional[Type[[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]] = None, index_kwargs: Optional[Dict] = None, use_query_str_in_loader: bool = False, query_str_kwargs_key: str = 'query_str', name: Optional[str] = None, description: Optional[str] = None, fn_schema: Optional[Type[BaseModel]] = None) -> [OnDemandLoaderTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool "llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool")
```

From defaults.

Source code in `llama-index-core/llama_index/core/tools/ondemand_loader_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
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
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">reader</span><span class="p">:</span> <span class="n">BaseReader</span><span class="p">,</span>
    <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">use_query_str_in_loader</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">query_str_kwargs_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"query_str"</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OnDemandLoaderTool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From defaults."""</span>
    <span class="c1"># NOTE: fn_schema should be specified if you want to use as langchain Tool</span>

    <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
    <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Tool to load data from </span><span class="si">{</span><span class="n">reader</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">"</span>
    <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">create_schema_from_function</span><span class="p">(</span>
            <span class="n">name</span> <span class="ow">or</span> <span class="s2">"LoadData"</span><span class="p">,</span>
            <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">,</span>
            <span class="p">[(</span><span class="n">query_str_kwargs_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">)],</span>
        <span class="p">)</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">loader</span><span class="o">=</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
        <span class="n">use_query_str_in_loader</span><span class="o">=</span><span class="n">use_query_str_in_loader</span><span class="p">,</span>
        <span class="n">query_str_kwargs_key</span><span class="o">=</span><span class="n">query_str_kwargs_key</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_tool `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool.from_tool "Permanent link")

```
from_tool(tool: [FunctionTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool "llama_index.core.tools.function_tool.FunctionTool"), index_cls: Optional[Type[[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]] = None, index_kwargs: Optional[Dict] = None, use_query_str_in_loader: bool = False, query_str_kwargs_key: str = 'query_str', name: Optional[str] = None, description: Optional[str] = None, return_direct: bool = False, fn_schema: Optional[Type[BaseModel]] = None) -> [OnDemandLoaderTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool "llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool")
```

From defaults.

Source code in `llama-index-core/llama_index/core/tools/ondemand_loader_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 86</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tool</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tool</span><span class="p">:</span> <span class="n">FunctionTool</span><span class="p">,</span>
    <span class="n">index_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">use_query_str_in_loader</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">query_str_kwargs_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"query_str"</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">return_direct</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OnDemandLoaderTool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From defaults."""</span>
    <span class="c1"># NOTE: fn_schema should be specified if you want to use as langchain Tool</span>

    <span class="n">index_cls</span> <span class="o">=</span> <span class="n">index_cls</span> <span class="ow">or</span> <span class="n">VectorStoreIndex</span>
    <span class="n">index_kwargs</span> <span class="o">=</span> <span class="n">index_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">description</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">description</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Tool to load data from </span><span class="si">{</span><span class="n">tool</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">"</span>
    <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">create_schema_from_function</span><span class="p">(</span>
            <span class="n">name</span> <span class="ow">or</span> <span class="s2">"LoadData"</span><span class="p">,</span> <span class="n">tool</span><span class="o">.</span><span class="n">_fn</span><span class="p">,</span> <span class="p">[(</span><span class="n">query_str_kwargs_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">)]</span>
        <span class="p">)</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
        <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">,</span>
        <span class="n">return_direct</span><span class="o">=</span><span class="n">return_direct</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">loader</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">_fn</span><span class="p">,</span>
        <span class="n">index_cls</span><span class="o">=</span><span class="n">index_cls</span><span class="p">,</span>
        <span class="n">index_kwargs</span><span class="o">=</span><span class="n">index_kwargs</span><span class="p">,</span>
        <span class="n">use_query_str_in_loader</span><span class="o">=</span><span class="n">use_query_str_in_loader</span><span class="p">,</span>
        <span class="n">query_str_kwargs_key</span><span class="o">=</span><span class="n">query_str_kwargs_key</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### call [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool.call "Permanent link")

```
call(*args: Any, **kwargs: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

Call.

Source code in `llama-index-core/llama_index/core/tools/ondemand_loader_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Call."""</span>
    <span class="n">query_str</span><span class="p">,</span> <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_args</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
    <span class="c1"># TODO: add query kwargs</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
        <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### acall `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/#llama_index.core.tools.ondemand_loader_tool.OnDemandLoaderTool.acall "Permanent link")

```
acall(*args: Any, **kwargs: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

Async Call.

Source code in `llama-index-core/llama_index/core/tools/ondemand_loader_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">155</span>
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
<span class="normal">168</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async Call."""</span>
    <span class="n">query_str</span><span class="p">,</span> <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_args</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_cls</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_kwargs</span><span class="p">)</span>
    <span class="c1"># TODO: add query kwargs</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
    <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
        <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
        <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Notion](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/)[Next Openai](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/)
