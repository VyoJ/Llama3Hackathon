Title: Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/

Markdown Content:
Retriever - LlamaIndex


RetrieverQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/#llama_index.core.query_engine.RetrieverQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Retriever query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 
A retriever object.



 | _required_ |
| `response_synthesizer` | `Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")]` | 

A BaseSynthesizer object.



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/retriever_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 30</span>
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
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrieverQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Retriever query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (BaseRetriever): A retriever object.</span>
<span class="sd">        response_synthesizer (Optional[BaseSynthesizer]): A BaseSynthesizer</span>
<span class="sd">            object.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">retriever</span><span class="o">.</span><span class="n">get_service_context</span><span class="p">()),</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">retriever</span><span class="o">.</span><span class="n">get_service_context</span><span class="p">()</span>
            <span class="p">),</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"response_synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_args</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># response synthesizer args</span>
        <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">summary_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">simple_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RetrieverQueryEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a RetrieverQueryEngine object.".</span>

<span class="sd">        Args:</span>
<span class="sd">            retriever (BaseRetriever): A retriever object.</span>
<span class="sd">            service_context (Optional[ServiceContext]): A ServiceContext object.</span>
<span class="sd">            node_postprocessors (Optional[List[BaseNodePostprocessor]]): A list of</span>
<span class="sd">                node postprocessors.</span>
<span class="sd">            verbose (bool): Whether to print out debug info.</span>
<span class="sd">            response_mode (ResponseMode): A ResponseMode object.</span>
<span class="sd">            text_qa_template (Optional[BasePromptTemplate]): A BasePromptTemplate</span>
<span class="sd">                object.</span>
<span class="sd">            refine_template (Optional[BasePromptTemplate]): A BasePromptTemplate object.</span>
<span class="sd">            simple_template (Optional[BasePromptTemplate]): A BasePromptTemplate object.</span>

<span class="sd">            use_async (bool): Whether to use async.</span>
<span class="sd">            streaming (bool): Whether to use streaming.</span>
<span class="sd">            optimizer (Optional[BaseTokenUsageOptimizer]): A BaseTokenUsageOptimizer</span>
<span class="sd">                object.</span>

<span class="sd">        """</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
            <span class="n">refine_template</span><span class="o">=</span><span class="n">refine_template</span><span class="p">,</span>
            <span class="n">summary_template</span><span class="o">=</span><span class="n">summary_template</span><span class="p">,</span>
            <span class="n">simple_template</span><span class="o">=</span><span class="n">simple_template</span><span class="p">,</span>
            <span class="n">response_mode</span><span class="o">=</span><span class="n">response_mode</span><span class="p">,</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_apply_node_postprocessors</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">postprocess_nodes</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_node_postprocessors</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_apply_node_postprocessors</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">query_bundle</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">with_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RetrieverQueryEngine"</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="p">(</span>
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">response_synthesizer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">node_postprocessors</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">asynthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">additional_source_nodes</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the retriever object."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span>
</code></pre></div></td></tr></tbody></table>

### retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/#llama_index.core.query_engine.RetrieverQueryEngine.retriever "Permanent link")

```
retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Get the retriever object.

### from\_args `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/#llama_index.core.query_engine.RetrieverQueryEngine.from_args "Permanent link")

```
from_args(retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever"), llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, response_synthesizer: Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")] = None, node_postprocessors: Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]] = None, response_mode: [ResponseMode](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "llama_index.core.response_synthesizers.ResponseMode") = ResponseMode.COMPACT, text_qa_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, refine_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, summary_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, simple_template: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")] = None, output_cls: Optional[BaseModel] = None, use_async: bool = False, streaming: bool = False, service_context: Optional[ServiceContext] = None, **kwargs: Any) -> [RetrieverQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/#llama_index.core.query_engine.RetrieverQueryEngine "llama_index.core.query_engine.retriever_query_engine.RetrieverQueryEngine")
```

Initialize a RetrieverQueryEngine object.".

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 
A retriever object.



 | _required_ |
| `service_context` | `Optional[ServiceContext]` | 

A ServiceContext object.



 | `None` |
| `node_postprocessors` | `Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]]` | 

A list of node postprocessors.



 | `None` |
| `verbose` | `bool` | 

Whether to print out debug info.



 | _required_ |
| `response_mode` | `[ResponseMode](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode "llama_index.core.response_synthesizers.ResponseMode")` | 

A ResponseMode object.



 | `[COMPACT](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.type.ResponseMode.COMPACT "llama_index.core.response_synthesizers.ResponseMode.COMPACT")` |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A BasePromptTemplate object.



 | `None` |
| `refine_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A BasePromptTemplate object.



 | `None` |
| `simple_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

A BasePromptTemplate object.



 | `None` |
| `use_async` | `bool` | 

Whether to use async.



 | `False` |
| `streaming` | `bool` | 

Whether to use streaming.



 | `False` |
| `optimizer` | `Optional[BaseTokenUsageOptimizer]` | 

A BaseTokenUsageOptimizer object.



 | _required_ |

Source code in `llama-index-core/llama_index/core/query_engine/retriever_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 68</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_args</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># response synthesizer args</span>
    <span class="n">response_mode</span><span class="p">:</span> <span class="n">ResponseMode</span> <span class="o">=</span> <span class="n">ResponseMode</span><span class="o">.</span><span class="n">COMPACT</span><span class="p">,</span>
    <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">refine_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">summary_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">simple_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="c1"># deprecated</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"RetrieverQueryEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a RetrieverQueryEngine object.".</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (BaseRetriever): A retriever object.</span>
<span class="sd">        service_context (Optional[ServiceContext]): A ServiceContext object.</span>
<span class="sd">        node_postprocessors (Optional[List[BaseNodePostprocessor]]): A list of</span>
<span class="sd">            node postprocessors.</span>
<span class="sd">        verbose (bool): Whether to print out debug info.</span>
<span class="sd">        response_mode (ResponseMode): A ResponseMode object.</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): A BasePromptTemplate</span>
<span class="sd">            object.</span>
<span class="sd">        refine_template (Optional[BasePromptTemplate]): A BasePromptTemplate object.</span>
<span class="sd">        simple_template (Optional[BasePromptTemplate]): A BasePromptTemplate object.</span>

<span class="sd">        use_async (bool): Whether to use async.</span>
<span class="sd">        streaming (bool): Whether to use streaming.</span>
<span class="sd">        optimizer (Optional[BaseTokenUsageOptimizer]): A BaseTokenUsageOptimizer</span>
<span class="sd">            object.</span>

<span class="sd">    """</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

    <span class="n">response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="o">=</span><span class="n">text_qa_template</span><span class="p">,</span>
        <span class="n">refine_template</span><span class="o">=</span><span class="n">refine_template</span><span class="p">,</span>
        <span class="n">summary_template</span><span class="o">=</span><span class="n">summary_template</span><span class="p">,</span>
        <span class="n">simple_template</span><span class="o">=</span><span class="n">simple_template</span><span class="p">,</span>
        <span class="n">response_mode</span><span class="o">=</span><span class="n">response_mode</span><span class="p">,</span>
        <span class="n">output_cls</span><span class="o">=</span><span class="n">output_cls</span><span class="p">,</span>
        <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
        <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
        <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">response_synthesizer</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="o">=</span><span class="n">node_postprocessors</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pandas](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/)[Next Retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/)
