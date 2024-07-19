Title: Router - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/

Markdown Content:
Router - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Selector component.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/router.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
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
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SelectorComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Selector component."""</span>

    <span class="n">selector</span><span class="p">:</span> <span class="n">BaseSelector</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Selector"</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="k">if</span> <span class="s2">"choices"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'choices'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"choices"</span><span class="p">],</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input choices must be a list"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">choice</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"choices"</span><span class="p">]):</span>
            <span class="c1"># make stringable</span>
            <span class="nb">input</span><span class="p">[</span><span class="s2">"choices"</span><span class="p">][</span><span class="n">idx</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="n">choice</span><span class="p">)</span>

        <span class="c1"># make sure `query` is stringable</span>
        <span class="k">if</span> <span class="s2">"query"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'query'"</span><span class="p">)</span>
        <span class="nb">input</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"query"</span><span class="p">])</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s2">"choices"</span><span class="p">],</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query"</span><span class="p">])</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"output"</span><span class="p">:</span> <span class="n">output</span><span class="o">.</span><span class="n">selections</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="c1"># NOTE: no native async for postprocessor</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"choices"</span><span class="p">,</span> <span class="s2">"query"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"output"</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.SelectorComponent.input_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.SelectorComponent.output_keys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.SelectorComponent.set_callback_manager "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/router.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
<span class="normal">29</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Router Component.

Routes queries to different query components based on a selector.

Assumes a single query component is selected.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/router.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 70</span>
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
<span class="normal">198</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RouterComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Router Component.</span>

<span class="sd">    Routes queries to different query components based on a selector.</span>

<span class="sd">    Assumes a single query component is selected.</span>

<span class="sd">    """</span>

    <span class="n">selector</span><span class="p">:</span> <span class="n">BaseSelector</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Selector"</span><span class="p">)</span>
    <span class="n">choices</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Choices (must correspond to components)"</span>
    <span class="p">)</span>
    <span class="n">components</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">QueryComponent</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Components (must correspond to choices)"</span>
    <span class="p">)</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Verbose"</span><span class="p">)</span>

    <span class="n">_query_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">selector</span><span class="p">:</span> <span class="n">BaseSelector</span><span class="p">,</span>
        <span class="n">choices</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">components</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">QUERY_COMPONENT_TYPE</span><span class="p">],</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init."""</span>
        <span class="n">new_components</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">query_keys</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="n">components</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">component</span><span class="p">,</span> <span class="n">ChainableMixin</span><span class="p">):</span>
                <span class="n">new_component</span> <span class="o">=</span> <span class="n">component</span><span class="o">.</span><span class="n">as_query_component</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">new_component</span> <span class="o">=</span> <span class="n">component</span>

            <span class="c1"># validate component has one input key</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">new_component</span><span class="o">.</span><span class="n">free_req_input_keys</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Expected one required input key"</span><span class="p">)</span>
            <span class="n">query_keys</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">new_component</span><span class="o">.</span><span class="n">free_req_input_keys</span><span class="p">)))</span>
            <span class="n">new_components</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_component</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_query_keys</span> <span class="o">=</span> <span class="n">query_keys</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">selector</span><span class="o">=</span><span class="n">selector</span><span class="p">,</span>
            <span class="n">choices</span><span class="o">=</span><span class="n">choices</span><span class="p">,</span>
            <span class="n">components</span><span class="o">=</span><span class="n">new_components</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="p">:</span>
            <span class="n">component</span><span class="o">.</span><span class="n">set_callback_manager</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># make sure `query` is stringable</span>
        <span class="k">if</span> <span class="s2">"query"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">input</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Input must have key 'query'"</span><span class="p">)</span>
        <span class="nb">input</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]</span> <span class="o">=</span> <span class="n">validate_and_convert_stringable</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="s2">"query"</span><span class="p">])</span>

        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="c1"># for the output selection, run the corresponding component, aggregate into list</span>
        <span class="n">sel_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">choices</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query"</span><span class="p">])</span>
        <span class="c1"># assume one selection</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sel_output</span><span class="o">.</span><span class="n">selections</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Expected one selection"</span><span class="p">)</span>
        <span class="n">component</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="p">[</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Selecting component </span><span class="si">{</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sel_output</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="c1"># run component</span>
        <span class="c1"># run with input_keys of component</span>
        <span class="k">return</span> <span class="n">component</span><span class="o">.</span><span class="n">run_component</span><span class="p">(</span>
            <span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_keys</span><span class="p">[</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="p">]:</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]}</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="c1"># for the output selection, run the corresponding component, aggregate into list</span>
        <span class="n">sel_output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">selector</span><span class="o">.</span><span class="n">aselect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">choices</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query"</span><span class="p">])</span>
        <span class="c1"># assume one selection</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sel_output</span><span class="o">.</span><span class="n">selections</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Expected one selection"</span><span class="p">)</span>
        <span class="n">component</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="p">[</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="p">]</span>
        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Selecting component </span><span class="si">{</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="si">}</span><span class="s2">: "</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sel_output</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">."</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="n">log_str</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="c1"># run component</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">component</span><span class="o">.</span><span class="n">arun_component</span><span class="p">(</span>
            <span class="o">**</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_keys</span><span class="p">[</span><span class="n">sel_output</span><span class="o">.</span><span class="n">ind</span><span class="p">]:</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]}</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="s2">"query"</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># not used</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span><span class="nb">set</span><span class="p">())</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">sub_query_components</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"QueryComponent"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get sub query components.</span>

<span class="sd">        Certain query components may have sub query components, e.g. a</span>
<span class="sd">        query pipeline will have sub query components, and so will</span>
<span class="sd">        an IfElseComponent.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.RouterComponent.input_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.RouterComponent.output_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

sub\_query\_components `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.RouterComponent.sub_query_components "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
sub_query_components: List[[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")]
```

Get sub query components.

Certain query components may have sub query components, e.g. a query pipeline will have sub query components, and so will an IfElseComponent.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.RouterComponent.set_callback_manager "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/router.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="p">:</span>
        <span class="n">component</span><span class="o">.</span><span class="n">set_callback_manager</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

validate\_component\_outputs [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/#llama_index.core.query_pipeline.components.router.RouterComponent.validate_component_outputs "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
validate_component_outputs(input: Dict[str, Any]) -> Dict[str, Any]
```

Validate component inputs during run\_component.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/router.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Validate component inputs during run_component."""</span>
    <span class="k">return</span> <span class="nb">input</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/retriever/)[Next Synthesizer](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/)
