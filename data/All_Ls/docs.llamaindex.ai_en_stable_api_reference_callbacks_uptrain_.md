Title: Uptrain - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/

Markdown Content:
Uptrain - LlamaIndex


UpTrainCallbackHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/#llama_index.callbacks.uptrain.UpTrainCallbackHandler "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`

UpTrain callback handler.

This class is responsible for handling the UpTrain API and logging events to UpTrain.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-uptrain/llama_index/callbacks/uptrain/base.py`

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
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">UpTrainCallbackHandler</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    UpTrain callback handler.</span>

<span class="sd">    This class is responsible for handling the UpTrain API and logging events to UpTrain.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">key_type</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s2">"uptrain"</span><span class="p">,</span> <span class="s2">"openai"</span><span class="p">],</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"uptrain_llamaindex"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the UpTrain callback handler."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">uptrain</span> <span class="kn">import</span> <span class="n">APIClient</span><span class="p">,</span> <span class="n">EvalLLM</span><span class="p">,</span> <span class="n">Settings</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"UpTrainCallbackHandler requires the 'uptrain' package. "</span>
                <span class="s2">"Please install it using 'pip install uptrain'."</span>
            <span class="p">)</span>
        <span class="n">nest_asyncio</span><span class="o">.</span><span class="n">apply</span><span class="p">()</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="p">[],</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="n">UpTrainDataSchema</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>

        <span class="c1"># Based on whether the user enters an UpTrain API key or an OpenAI API key, the client is initialized</span>
        <span class="c1"># If both are entered, the UpTrain API key is used</span>
        <span class="k">if</span> <span class="n">key_type</span> <span class="o"></span> <span class="s2">"openai"</span><span class="p">:</span>
            <span class="n">settings</span> <span class="o">=</span> <span class="n">Settings</span><span class="p">(</span><span class="n">openai_api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_client</span> <span class="o">=</span> <span class="n">EvalLLM</span><span class="p">(</span><span class="n">settings</span><span class="o">=</span><span class="n">settings</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid key type: Must be 'uptrain' or 'openai'"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">uptrain_evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">evaluation_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">data</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span>
        <span class="n">checks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run an evaluation on the UpTrain server using UpTrain client."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_client</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span> <span class="o"></span> <span class="s2">"question"</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Question: </span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="n">column</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="k">elif</span> <span class="n">column</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_parent_id</span><span class="p">:</span>
            <span class="c1"># Perform individual evaluations for sub questions (but send all sub questions at once)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"sub_question_answering"</span><span class="p">,</span>
                <span class="n">data</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span>
                <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_RELEVANCE</span><span class="p">,</span>
                    <span class="n">Evals</span><span class="o">.</span><span class="n">FACTUAL_ACCURACY</span><span class="p">,</span>
                    <span class="n">Evals</span><span class="o">.</span><span class="n">RESPONSE_COMPLETENESS</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">)</span>
            <span class="c1"># Perform evaluation for question and all sub questions (as a whole)</span>
            <span class="n">sub_questions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">sub_question</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">sub_question</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
            <span class="p">]</span>
            <span class="n">sub_questions_formatted</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"sub_query_completeness"</span><span class="p">,</span>
                <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">parent_question</span><span class="p">,</span>
                        <span class="s2">"sub_questions"</span><span class="p">:</span> <span class="n">sub_questions_formatted</span><span class="p">,</span>
                    <span class="p">}</span>
                <span class="p">],</span>
                <span class="n">checks</span><span class="o">=</span><span class="p">[</span><span class="n">Evals</span><span class="o">.</span><span class="n">SUB_QUERY_COMPLETENESS</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">"sub_question"</span><span class="p">)</span>
        <span class="c1"># Should not be called for sub questions</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">SYNTHESIZE</span>
            <span class="ow">and</span> <span class="s2">"sub_question"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span>
        <span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span><span class="s2">"response"</span><span class="p">]</span><span class="o">.</span><span class="n">response</span>
            <span class="c1"># Perform evaluation for synthesization</span>
            <span class="k">if</span> <span class="s2">"reranking"</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o"></span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o">=</span> <span class="s2">"rerank"</span>
                <span class="n">context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">old_context</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                    <span class="p">]</span>
                <span class="p">)</span>
                <span class="n">reranked_context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                    <span class="p">]</span>
                <span class="p">)</span>
                <span class="c1"># Perform evaluation for reranking</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                    <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"context_reranking"</span><span class="p">,</span>
                    <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">question</span><span class="p">,</span>
                            <span class="s2">"context"</span><span class="p">:</span> <span class="n">context</span><span class="p">,</span>
                            <span class="s2">"reranked_context"</span><span class="p">:</span> <span class="n">reranked_context</span><span class="p">,</span>
                        <span class="p">}</span>
                    <span class="p">],</span>
                    <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                        <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_RERANKING</span><span class="p">,</span>
                    <span class="p">],</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o">=</span> <span class="s2">"resize"</span>
                <span class="n">context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">old_context</span><span class="p">)</span>
                <span class="n">concise_context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">)</span>
                <span class="c1"># Perform evaluation for resizing</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                    <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"context_conciseness"</span><span class="p">,</span>
                    <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">question</span><span class="p">,</span>
                            <span class="s2">"context"</span><span class="p">:</span> <span class="n">context</span><span class="p">,</span>
                            <span class="s2">"concise_context"</span><span class="p">:</span> <span class="n">concise_context</span><span class="p">,</span>
                        <span class="p">}</span>
                    <span class="p">],</span>
                    <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                        <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_CONCISENESS</span><span class="p">,</span>
                    <span class="p">],</span>
                <span class="p">)</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span>
            <span class="c1"># Store sub question data</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span>
                <span class="s2">"sub_question"</span>
            <span class="p">]</span><span class="o">.</span><span class="n">sub_q</span><span class="o">.</span><span class="n">sub_question</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">payload</span><span class="p">[</span><span class="s2">"sub_question"</span><span class="p">]</span><span class="o">.</span><span class="n">sources</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"response"</span><span class="p">]</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span>
                <span class="s2">"sub_question"</span>
            <span class="p">]</span><span class="o">.</span><span class="n">answer</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">start_trace</span><span class="p">(</span><span class="n">trace_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">trace_map</span> <span class="ow">or</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">end_trace</span><span class="p">(</span><span class="n">trace_id</span><span class="p">,</span> <span class="n">trace_map</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">build_trace_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cur_event_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">event_pair</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">cur_event_id</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">event_pair</span><span class="p">:</span>
            <span class="n">event_data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"event_type"</span><span class="p">:</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">event_type</span><span class="p">,</span>
                <span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                <span class="s2">"children"</span><span class="p">:</span> <span class="p">{},</span>
            <span class="p">}</span>
            <span class="n">trace_map</span><span class="p">[</span><span class="n">cur_event_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">event_data</span>

        <span class="n">child_event_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">[</span><span class="n">cur_event_id</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">child_event_id</span> <span class="ow">in</span> <span class="n">child_event_ids</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">build_trace_map</span><span class="p">(</span><span class="n">child_event_id</span><span class="p">,</span> <span class="n">event_data</span><span class="p">[</span><span class="s2">"children"</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">trace_map</span>
</code></pre></div></td></tr></tbody></table>

### uptrain\_evaluate [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/#llama_index.callbacks.uptrain.UpTrainCallbackHandler.uptrain_evaluate "Permanent link")

```
uptrain_evaluate(evaluation_name: str, data: List[Dict[str, str]], checks: List[str]) -> None
```

Run an evaluation on the UpTrain server using UpTrain client.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-uptrain/llama_index/callbacks/uptrain/base.py`

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
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">uptrain_evaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">evaluation_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">data</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span>
    <span class="n">checks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run an evaluation on the UpTrain server using UpTrain client."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_client</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span> <span class="o"></span> <span class="s2">"question"</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Question: </span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="n">column</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">column</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_parent_id</span><span class="p">:</span>
        <span class="c1"># Perform individual evaluations for sub questions (but send all sub questions at once)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
            <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"sub_question_answering"</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span>
            <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_RELEVANCE</span><span class="p">,</span>
                <span class="n">Evals</span><span class="o">.</span><span class="n">FACTUAL_ACCURACY</span><span class="p">,</span>
                <span class="n">Evals</span><span class="o">.</span><span class="n">RESPONSE_COMPLETENESS</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">)</span>
        <span class="c1"># Perform evaluation for question and all sub questions (as a whole)</span>
        <span class="n">sub_questions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">sub_question</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">sub_question</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
        <span class="p">]</span>
        <span class="n">sub_questions_formatted</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sub_questions</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
            <span class="p">]</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
            <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"sub_query_completeness"</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                <span class="p">{</span>
                    <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">parent_question</span><span class="p">,</span>
                    <span class="s2">"sub_questions"</span><span class="p">:</span> <span class="n">sub_questions_formatted</span><span class="p">,</span>
                <span class="p">}</span>
            <span class="p">],</span>
            <span class="n">checks</span><span class="o">=</span><span class="p">[</span><span class="n">Evals</span><span class="o">.</span><span class="n">SUB_QUERY_COMPLETENESS</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">"sub_question"</span><span class="p">)</span>
    <span class="c1"># Should not be called for sub questions</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">SYNTHESIZE</span>
        <span class="ow">and</span> <span class="s2">"sub_question"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span><span class="s2">"response"</span><span class="p">]</span><span class="o">.</span><span class="n">response</span>
        <span class="c1"># Perform evaluation for synthesization</span>
        <span class="k">if</span> <span class="s2">"reranking"</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">eval_types</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o"></span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o">=</span> <span class="s2">"rerank"</span>
            <span class="n">context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">old_context</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="p">)</span>
            <span class="n">reranked_context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">. </span><span class="si">{</span><span class="n">string</span><span class="si">}</span><span class="s2">"</span>
                    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">string</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="p">)</span>
            <span class="c1"># Perform evaluation for reranking</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"context_reranking"</span><span class="p">,</span>
                <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">question</span><span class="p">,</span>
                        <span class="s2">"context"</span><span class="p">:</span> <span class="n">context</span><span class="p">,</span>
                        <span class="s2">"reranked_context"</span><span class="p">:</span> <span class="n">reranked_context</span><span class="p">,</span>
                    <span class="p">}</span>
                <span class="p">],</span>
                <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_RERANKING</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">reranking_type</span> <span class="o">=</span> <span class="s2">"resize"</span>
            <span class="n">context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">old_context</span><span class="p">)</span>
            <span class="n">concise_context</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">new_context</span><span class="p">)</span>
            <span class="c1"># Perform evaluation for resizing</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uptrain_evaluate</span><span class="p">(</span>
                <span class="n">evaluation_name</span><span class="o">=</span><span class="s2">"context_conciseness"</span><span class="p">,</span>
                <span class="n">data</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">"question"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">question</span><span class="p">,</span>
                        <span class="s2">"context"</span><span class="p">:</span> <span class="n">context</span><span class="p">,</span>
                        <span class="s2">"concise_context"</span><span class="p">:</span> <span class="n">concise_context</span><span class="p">,</span>
                    <span class="p">}</span>
                <span class="p">],</span>
                <span class="n">checks</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">Evals</span><span class="o">.</span><span class="n">CONTEXT_CONCISENESS</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">)</span>
    <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">SUB_QUESTION</span><span class="p">:</span>
        <span class="c1"># Store sub question data</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span>
            <span class="s2">"sub_question"</span>
        <span class="p">]</span><span class="o">.</span><span class="n">sub_q</span><span class="o">.</span><span class="n">sub_question</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"sub_question"</span><span class="p">]</span><span class="o">.</span><span class="n">sources</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="o">.</span><span class="n">sub_question_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">][</span><span class="s2">"response"</span><span class="p">]</span> <span class="o">=</span> <span class="n">payload</span><span class="p">[</span>
            <span class="s2">"sub_question"</span>
        <span class="p">]</span><span class="o">.</span><span class="n">answer</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Token counter](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/)[Next Wandb](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/)
