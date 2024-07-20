Title: Simple multi modal - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/

Markdown Content:
Simple multi modal - LlamaIndex


SimpleMultiModalQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/#llama_index.core.query_engine.SimpleMultiModalQueryEngine "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")`

Simple Multi Modal Retriever query engine.

Assumes that retrieved text context fits within context window of LLM, along with images.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `MultiModalVectorIndexRetriever` | 
A retriever object.



 | _required_ |
| `multi_modal_llm` | `Optional[[MultiModalLLM](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "llama_index.core.multi_modal_llms.base.MultiModalLLM")]` | 

MultiModalLLM Models.



 | `None` |
| `text_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Text QA Prompt Template.



 | `None` |
| `image_qa_template` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Image QA Prompt Template.



 | `None` |
| `node_postprocessors` | `Optional[List[[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")]]` | 

Node Postprocessors.



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-core/llama_index/core/query_engine/multi_modal.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 32</span>
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
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleMultiModalQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Multi Modal Retriever query engine.</span>

<span class="sd">    Assumes that retrieved text context fits within context window of LLM, along with images.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (MultiModalVectorIndexRetriever): A retriever object.</span>
<span class="sd">        multi_modal_llm (Optional[MultiModalLLM]): MultiModalLLM Models.</span>
<span class="sd">        text_qa_template (Optional[BasePromptTemplate]): Text QA Prompt Template.</span>
<span class="sd">        image_qa_template (Optional[BasePromptTemplate]): Image QA Prompt Template.</span>
<span class="sd">        node_postprocessors (Optional[List[BaseNodePostprocessor]]): Node Postprocessors.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="s2">"MultiModalVectorIndexRetriever"</span><span class="p">,</span>
        <span class="n">multi_modal_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MultiModalLLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">image_qa_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_postprocessors</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNodePostprocessor</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="k">if</span> <span class="n">multi_modal_llm</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span> <span class="o">=</span> <span class="n">multi_modal_llm</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.multi_modal_llms.openai</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">OpenAIMultiModal</span><span class="p">,</span>
                <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span> <span class="o">=</span> <span class="n">OpenAIMultiModal</span><span class="p">(</span>
                    <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">1000</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"`llama-index-multi-modal-llms-openai` package cannot be found. "</span>
                    <span class="s2">"Please install it by using `pip install `llama-index-multi-modal-llms-openai`"</span>
                <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span> <span class="o">=</span> <span class="n">text_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_image_qa_template</span> <span class="o">=</span> <span class="n">image_qa_template</span> <span class="ow">or</span> <span class="n">DEFAULT_TEXT_QA_PROMPT</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span> <span class="o">=</span> <span class="n">node_postprocessors</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="k">for</span> <span class="n">node_postprocessor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_node_postprocessors</span><span class="p">:</span>
            <span class="n">node_postprocessor</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"text_qa_template"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

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

    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">image_nodes</span><span class="p">,</span> <span class="n">text_nodes</span> <span class="o">=</span> <span class="n">_get_image_and_text_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">context_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">text_nodes</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">fmt_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">fmt_prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="p">[</span><span class="n">image_node</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">image_node</span> <span class="ow">in</span> <span class="n">image_nodes</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">llm_response</span><span class="p">),</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"text_nodes"</span><span class="p">:</span> <span class="n">text_nodes</span><span class="p">,</span> <span class="s2">"image_nodes"</span><span class="p">:</span> <span class="n">image_nodes</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_response_with_images</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">prompt_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">image_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ImageNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">fmt_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_image_qa_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">prompt_str</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">fmt_prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="p">[</span><span class="n">image_node</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">image_node</span> <span class="ow">in</span> <span class="n">image_nodes</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">llm_response</span><span class="p">),</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">image_nodes</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"image_nodes"</span><span class="p">:</span> <span class="n">image_nodes</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">asynthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="n">image_nodes</span><span class="p">,</span> <span class="n">text_nodes</span> <span class="o">=</span> <span class="n">_get_image_and_text_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">context_str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">text_nodes</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">fmt_prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_qa_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>
        <span class="p">)</span>
        <span class="n">llm_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_multi_modal_llm</span><span class="o">.</span><span class="n">acomplete</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">fmt_prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="p">[</span><span class="n">image_node</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">image_node</span> <span class="ow">in</span> <span class="n">image_nodes</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">llm_response</span><span class="p">),</span>
            <span class="n">source_nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"text_nodes"</span><span class="p">:</span> <span class="n">text_nodes</span><span class="p">,</span> <span class="s2">"image_nodes"</span><span class="p">:</span> <span class="n">image_nodes</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
                <span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">image_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">image_path</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">,</span> <span class="n">prompt_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a image query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">image_path</span><span class="p">)}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">image_path</span><span class="p">)},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">image_to_image_retrieve</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span>

                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
                <span class="p">)</span>

            <span class="n">image_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">_get_image_and_text_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response_with_images</span><span class="p">(</span>
                <span class="n">prompt_str</span><span class="o">=</span><span class="n">prompt_str</span><span class="p">,</span>
                <span class="n">image_nodes</span><span class="o">=</span><span class="n">image_nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
                <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

                <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
                <span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MultiModalVectorIndexRetriever"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the retriever object."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span>
</code></pre></div></td></tr></tbody></table>

### retriever `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/#llama_index.core.query_engine.SimpleMultiModalQueryEngine.retriever "Permanent link")

```
retriever: MultiModalVectorIndexRetriever
```

Get the retriever object.

### image\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/#llama_index.core.query_engine.SimpleMultiModalQueryEngine.image_query "Permanent link")

```
image_query(image_path: QueryType, prompt_str: str) -> RESPONSE_TYPE
```

Answer a image query.

Source code in `llama-index-core/llama_index/core/query_engine/multi_modal.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
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
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">image_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">image_path</span><span class="p">:</span> <span class="n">QueryType</span><span class="p">,</span> <span class="n">prompt_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Answer a image query."""</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">image_path</span><span class="p">)}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">image_path</span><span class="p">)},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">image_to_image_retrieve</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span>

            <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="n">image_nodes</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">_get_image_and_text_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response_with_images</span><span class="p">(</span>
            <span class="n">prompt_str</span><span class="o">=</span><span class="n">prompt_str</span><span class="p">,</span>
            <span class="n">image_nodes</span><span class="o">=</span><span class="n">image_nodes</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

    <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/)[Next Sub question](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/)
