Title: Sub question - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/

Markdown Content:
Sub question - LlamaIndex


SubQuestionQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/#llama_index.core.query_engine.SubQuestionQueryEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Sub question query engine.

A query engine that breaks down a complex query (e.g. compare and contrast) into many sub questions and their target query engine for execution. After executing all sub questions, all responses are gathered and sent to response synthesizer to produce the final response.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `question_gen` | `[BaseQuestionGenerator](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/#llama_index.core.question_gen.types.BaseQuestionGenerator "llama_index.core.question_gen.types.BaseQuestionGenerator")` | 
A module for generating sub questions given a complex question and tools.



 | _required_ |
| `response_synthesizer` | `[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.BaseSynthesizer")` | 

A response synthesizer for generating the final response



 | _required_ |
| `query_engine_tools` | `Sequence[[QueryEngineTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/#llama_index.core.tools.query_engine.QueryEngineTool "llama_index.core.tools.query_engine.QueryEngineTool")]` | 

Tools to answer the sub questions.



 | _required_ |
| `verbose` | `bool` | 

whether to print intermediate questions and answers. Defaults to True



 | `True` |
| `use_async` | `bool` | 

whether to execute the sub questions with asyncio. Defaults to True



 | `False` |

Source code in `llama-index-core/llama_index/core/query_engine/sub_question_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 42</span>
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
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubQuestionQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Sub question query engine.</span>

<span class="sd">    A query engine that breaks down a complex query (e.g. compare and contrast) into</span>
<span class="sd">        many sub questions and their target query engine for execution.</span>
<span class="sd">        After executing all sub questions, all responses are gathered and sent to</span>
<span class="sd">        response synthesizer to produce the final response.</span>

<span class="sd">    Args:</span>
<span class="sd">        question_gen (BaseQuestionGenerator): A module for generating sub questions</span>
<span class="sd">            given a complex question and tools.</span>
<span class="sd">        response_synthesizer (BaseSynthesizer): A response synthesizer for</span>
<span class="sd">            generating the final response</span>
<span class="sd">        query_engine_tools (Sequence[QueryEngineTool]): Tools to answer the</span>
<span class="sd">            sub questions.</span>
<span class="sd">        verbose (bool): whether to print intermediate questions and answers.</span>
<span class="sd">            Defaults to True</span>
<span class="sd">        use_async (bool): whether to execute the sub questions with asyncio.</span>
<span class="sd">            Defaults to True</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">question_gen</span><span class="p">:</span> <span class="n">BaseQuestionGenerator</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">BaseSynthesizer</span><span class="p">,</span>
        <span class="n">query_engine_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_question_gen</span> <span class="o">=</span> <span class="n">question_gen</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span> <span class="o">=</span> <span class="n">response_synthesizer</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">query_engine_tools</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">tool</span><span class="o">.</span><span class="n">query_engine</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">query_engine_tools</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span> <span class="o">=</span> <span class="n">use_async</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"question_gen"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_question_gen</span><span class="p">,</span>
            <span class="s2">"response_synthesizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">query_engine_tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">QueryEngineTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">question_gen</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseQuestionGenerator</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_synthesizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseSynthesizer</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">use_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SubQuestionQueryEngine"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_engine_tools</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">query_engine_tools</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">callback_manager</span>

        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">question_gen</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.question_gen.openai</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">OpenAIQuestionGenerator</span><span class="p">,</span>
                <span class="p">)</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="c1"># try to use OpenAI function calling based question generator.</span>
                <span class="c1"># if incompatible, use general LLM question generator</span>
                <span class="n">question_gen</span> <span class="o">=</span> <span class="n">OpenAIQuestionGenerator</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

            <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"`llama-index-question-gen-openai` package cannot be found. "</span>
                    <span class="s2">"Please install it by using `pip install `llama-index-question-gen-openai`"</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                <span class="n">question_gen</span> <span class="o">=</span> <span class="n">LLMQuestionGenerator</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="n">synth</span> <span class="o">=</span> <span class="n">response_synthesizer</span> <span class="ow">or</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">question_gen</span><span class="p">,</span>
            <span class="n">synth</span><span class="p">,</span>
            <span class="n">query_engine_tools</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="n">use_async</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">sub_questions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_question_gen</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">)</span>

            <span class="n">colors</span> <span class="o">=</span> <span class="n">get_color_mapping</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">))])</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Generated </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">)</span><span class="si">}</span><span class="s2"> sub questions.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_async</span><span class="p">:</span>
                <span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_aquery_subq</span><span class="p">(</span><span class="n">sub_q</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">colors</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">ind</span><span class="p">)])</span>
                    <span class="k">for</span> <span class="n">ind</span><span class="p">,</span> <span class="n">sub_q</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">)</span>
                <span class="p">]</span>

                <span class="n">qa_pairs_all</span> <span class="o">=</span> <span class="n">run_async_tasks</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
                <span class="n">qa_pairs_all</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]],</span> <span class="n">qa_pairs_all</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">qa_pairs_all</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_query_subq</span><span class="p">(</span><span class="n">sub_q</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">colors</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">ind</span><span class="p">)])</span>
                    <span class="k">for</span> <span class="n">ind</span><span class="p">,</span> <span class="n">sub_q</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">)</span>
                <span class="p">]</span>

            <span class="c1"># filter out sub questions that failed</span>
            <span class="n">qa_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">qa_pairs_all</span><span class="p">))</span>

            <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_construct_node</span><span class="p">(</span><span class="n">pair</span><span class="p">)</span> <span class="k">for</span> <span class="n">pair</span> <span class="ow">in</span> <span class="n">qa_pairs</span><span class="p">]</span>

            <span class="n">source_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span> <span class="k">for</span> <span class="n">qa_pair</span> <span class="ow">in</span> <span class="n">qa_pairs</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">qa_pair</span><span class="o">.</span><span class="n">sources</span><span class="p">]</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">synthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">QUERY</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">query_event</span><span class="p">:</span>
            <span class="n">sub_questions</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_question_gen</span><span class="o">.</span><span class="n">agenerate</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadatas</span><span class="p">,</span> <span class="n">query_bundle</span>
            <span class="p">)</span>

            <span class="n">colors</span> <span class="o">=</span> <span class="n">get_color_mapping</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">))])</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Generated </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">)</span><span class="si">}</span><span class="s2"> sub questions.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_aquery_subq</span><span class="p">(</span><span class="n">sub_q</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">colors</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">ind</span><span class="p">)])</span>
                <span class="k">for</span> <span class="n">ind</span><span class="p">,</span> <span class="n">sub_q</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">)</span>
            <span class="p">]</span>

            <span class="n">qa_pairs_all</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
            <span class="n">qa_pairs_all</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]],</span> <span class="n">qa_pairs_all</span><span class="p">)</span>

            <span class="c1"># filter out sub questions that failed</span>
            <span class="n">qa_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">qa_pairs_all</span><span class="p">))</span>

            <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_construct_node</span><span class="p">(</span><span class="n">pair</span><span class="p">)</span> <span class="k">for</span> <span class="n">pair</span> <span class="ow">in</span> <span class="n">qa_pairs</span><span class="p">]</span>

            <span class="n">source_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span> <span class="k">for</span> <span class="n">qa_pair</span> <span class="ow">in</span> <span class="n">qa_pairs</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">qa_pair</span><span class="o">.</span><span class="n">sources</span><span class="p">]</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">asynthesize</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">additional_source_nodes</span><span class="o">=</span><span class="n">source_nodes</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">query_event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">response</span><span class="p">})</span>

        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">_construct_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">qa_pair</span><span class="p">:</span> <span class="n">SubQuestionAnswerPair</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NodeWithScore</span><span class="p">:</span>
        <span class="n">node_text</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Sub question: </span><span class="si">{</span><span class="n">qa_pair</span><span class="o">.</span><span class="n">sub_q</span><span class="o">.</span><span class="n">sub_question</span><span class="si">}</span><span class="se">\n</span><span class="s2">Response: </span><span class="si">{</span><span class="n">qa_pair</span><span class="o">.</span><span class="n">answer</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">node_text</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery_subq</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sub_q</span><span class="p">:</span> <span class="n">SubQuestion</span><span class="p">,</span> <span class="n">color</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span> <span class="n">SubQuestionAnswerPair</span><span class="p">(</span><span class="n">sub_q</span><span class="o">=</span><span class="n">sub_q</span><span class="p">)},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                <span class="n">question</span> <span class="o">=</span> <span class="n">sub_q</span><span class="o">.</span><span class="n">sub_question</span>
                <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="p">]</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] Q: </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>

                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
                <span class="n">response_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] A: </span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>

                <span class="n">qa_pair</span> <span class="o">=</span> <span class="n">SubQuestionAnswerPair</span><span class="p">(</span>
                    <span class="n">sub_q</span><span class="o">=</span><span class="n">sub_q</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">response_text</span><span class="p">,</span> <span class="n">sources</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span>
                <span class="p">)</span>

                <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span> <span class="n">qa_pair</span><span class="p">})</span>

            <span class="k">return</span> <span class="n">qa_pair</span>
        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] Failed to run </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_query_subq</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">sub_q</span><span class="p">:</span> <span class="n">SubQuestion</span><span class="p">,</span> <span class="n">color</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SubQuestionAnswerPair</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                <span class="n">CBEventType</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">,</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span> <span class="n">SubQuestionAnswerPair</span><span class="p">(</span><span class="n">sub_q</span><span class="o">=</span><span class="n">sub_q</span><span class="p">)},</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                <span class="n">question</span> <span class="o">=</span> <span class="n">sub_q</span><span class="o">.</span><span class="n">sub_question</span>
                <span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engines</span><span class="p">[</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="p">]</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] Q: </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>

                <span class="n">response</span> <span class="o">=</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">question</span><span class="p">)</span>
                <span class="n">response_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                    <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] A: </span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>

                <span class="n">qa_pair</span> <span class="o">=</span> <span class="n">SubQuestionAnswerPair</span><span class="p">(</span>
                    <span class="n">sub_q</span><span class="o">=</span><span class="n">sub_q</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">response_text</span><span class="p">,</span> <span class="n">sources</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span>
                <span class="p">)</span>

                <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span> <span class="n">qa_pair</span><span class="p">})</span>

            <span class="k">return</span> <span class="n">qa_pair</span>
        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">sub_q</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s2">] Failed to run </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

SubQuestionAnswerPair [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/#llama_index.core.query_engine.SubQuestionAnswerPair "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Pair of the sub question and optionally its answer (if its been answered yet).

Source code in `llama-index-core/llama_index/core/query_engine/sub_question_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubQuestionAnswerPair</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Pair of the sub question and optionally its answer (if its been answered yet).</span>
<span class="sd">    """</span>

    <span class="n">sub_q</span><span class="p">:</span> <span class="n">SubQuestion</span>
    <span class="n">answer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/)[Next Tool retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/)
