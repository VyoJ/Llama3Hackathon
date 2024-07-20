Title: Knowledge graph - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/

Markdown Content:
Knowledge graph - LlamaIndex


KnowledgeGraphQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/#llama_index.core.query_engine.KnowledgeGraphQueryEngine "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Knowledge graph query engine.

Query engine to call a knowledge graph.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context` | `Optional[ServiceContext]` | 
A service context to use.



 | `None` |
| `storage_context` | `Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")]` | 

A storage context to use.



 | `None` |
| `refresh_schema` | `bool` | 

Whether to refresh the schema.



 | `False` |
| `verbose` | `bool` | 

Whether to print intermediate results.



 | `False` |
| `response_synthesizer` | `Optional[[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")]` | 

A BaseSynthesizer object.



 | `None` |
| `**kwargs` | `Any` | 

Additional keyword arguments.



 | `{}` |

Source code in `llama-index-core/llama_index/core/query_engine/knowledge_graph_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 51</span>
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
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@deprecated</span><span class="o">.</span><span class="n">deprecated</span><span class="p">(</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">"0.10.53"</span><span class="p">,</span>
    <span class="n">reason</span><span class="o">=</span><span class="p">(</span>
        <span class="s2">"KnowledgeGraphQueryEngine is deprecated. It is recommended to use "</span>
        <span class="s2">"the PropertyGraphIndex and associated retrievers instead."</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="k">class</span> <span class="nc">KnowledgeGraphQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Knowledge graph query engine.</span>

<span class="sd">    Query engine to call a knowledge graph.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context (Optional[ServiceContext]): A service context to use.</span>
<span class="sd">        storage_context (Optional[StorageContext]): A storage context to use.</span>
<span class="sd">        refresh_schema (bool): Whether to refresh the schema.</span>
<span class="sd">        verbose (bool): Whether to print intermediate results.</span>
<span class="sd">        response_synthesizer (Optional[BaseSynthesizer]):</span>
<span class="sd">            A BaseSynthesizer object.</span>
<span class="sd">        **kwargs: Additional keyword arguments.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">graph_query_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">graph_response_answer_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">refresh_schema</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="c1"># Ensure that we have a graph store</span>
        <span class="k">assert</span> <span class="n">storage_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s2">"Must provide a storage context."</span>
        <span class="k">assert</span> <span class="p">(</span>
            <span class="n">storage_context</span><span class="o">.</span><span class="n">graph_store</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">),</span> <span class="s2">"Must provide a graph store in the storage context."</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span> <span class="o">=</span> <span class="n">storage_context</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span> <span class="o">=</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">graph_store</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="c1"># Get Graph schema</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">get_schema</span><span class="p">(</span><span class="n">refresh</span><span class="o">=</span><span class="n">refresh_schema</span><span class="p">)</span>

        <span class="c1"># Get graph store query synthesis prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span> <span class="o">=</span> <span class="n">graph_query_synthesis_prompt</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_response_answer_prompt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">graph_response_answer_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_KG_RESPONSE_ANSWER_PROMPT</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"graph_query_synthesis_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span><span class="p">,</span>
            <span class="s2">"graph_response_answer_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_response_answer_prompt</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"graph_query_synthesis_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"graph_query_synthesis_prompt"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"graph_response_answer_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_response_answer_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"graph_response_answer_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"response_synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">generate_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a Graph Store Query from a query bundle."""</span>
        <span class="c1"># Get the query engine query string</span>

        <span class="n">graph_store_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">graph_store_query</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a Graph Store Query from a query bundle."""</span>
        <span class="c1"># Get the query engine query string</span>

        <span class="n">graph_store_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">graph_store_query</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes for response."""</span>
        <span class="n">graph_store_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Query:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Query:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_query</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">graph_store_query</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
            <span class="c1"># Get the graph store response</span>
            <span class="n">graph_store_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">graph_store_query</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Graph Store Response:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Response:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_response</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">graph_store_response</span><span class="p">})</span>

        <span class="n">retrieved_graph_context</span><span class="p">:</span> <span class="n">Sequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_response_answer_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">kg_query_str</span><span class="o">=</span><span class="n">graph_store_query</span><span class="p">,</span>
            <span class="n">kg_response_str</span><span class="o">=</span><span class="n">graph_store_response</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">node</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
            <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">retrieved_graph_context</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"query_str"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="s2">"graph_store_query"</span><span class="p">:</span> <span class="n">graph_store_query</span><span class="p">,</span>
                    <span class="s2">"graph_store_response"</span><span class="p">:</span> <span class="n">graph_store_response</span><span class="p">,</span>
                    <span class="s2">"graph_schema"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">),</span>
            <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query the graph store."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Final Response: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">graph_store_query</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">agenerate_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Query:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_query</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Query:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_query</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RETRIEVE</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">graph_store_query</span><span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">retrieve_event</span><span class="p">:</span>
            <span class="c1"># Get the graph store response</span>
            <span class="c1"># TBD: This is a blocking call. We need to make it async.</span>
            <span class="n">graph_store_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">graph_store_query</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Graph Store Response:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Graph Store Response:</span><span class="se">\n</span><span class="si">{</span><span class="n">graph_store_response</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">retrieve_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">graph_store_response</span><span class="p">})</span>

        <span class="n">retrieved_graph_context</span><span class="p">:</span> <span class="n">Sequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_response_answer_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">kg_query_str</span><span class="o">=</span><span class="n">graph_store_query</span><span class="p">,</span>
            <span class="n">kg_response_str</span><span class="o">=</span><span class="n">graph_store_response</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">node</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
            <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">retrieved_graph_context</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"query_str"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="s2">"graph_store_query"</span><span class="p">:</span> <span class="n">graph_store_query</span><span class="p">,</span>
                    <span class="s2">"graph_store_response"</span><span class="p">:</span> <span class="n">graph_store_response</span><span class="p">,</span>
                    <span class="s2">"graph_schema"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">),</span>
            <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query the graph store."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aretrieve</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Final Response: </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"green"</span><span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### generate\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/#llama_index.core.query_engine.KnowledgeGraphQueryEngine.generate_query "Permanent link")

```
generate_query(query_str: str) -> str
```

Generate a Graph Store Query from a query bundle.

Source code in `llama-index-core/llama_index/core/query_engine/knowledge_graph_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate a Graph Store Query from a query bundle."""</span>
    <span class="c1"># Get the query engine query string</span>

    <span class="n">graph_store_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span><span class="p">,</span>
        <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">graph_store_query</span>
</code></pre></div></td></tr></tbody></table>

### agenerate\_query `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/#llama_index.core.query_engine.KnowledgeGraphQueryEngine.agenerate_query "Permanent link")

```
agenerate_query(query_str: str) -> str
```

Generate a Graph Store Query from a query bundle.

Source code in `llama-index-core/llama_index/core/query_engine/knowledge_graph_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">agenerate_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate a Graph Store Query from a query bundle."""</span>
    <span class="c1"># Get the query engine query string</span>

    <span class="n">graph_store_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_graph_query_synthesis_prompt</span><span class="p">,</span>
        <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
        <span class="n">schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_graph_schema</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">graph_store_query</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/)[Next Multi step](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/)
