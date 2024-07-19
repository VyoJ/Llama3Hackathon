Title: Condense question - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/

Markdown Content:
Condense question - LlamaIndex


CondenseQuestionChatEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/#llama_index.core.chat_engine.CondenseQuestionChatEngine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "llama_index.core.chat_engine.types.BaseChatEngine")`

Condense Question Chat Engine.

First generate a standalone question from conversation context and last message, then query the query engine for a response.

Source code in `llama-index-core/llama_index/core/chat_engine/condense_question.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 56</span>
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
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CondenseQuestionChatEngine</span><span class="p">(</span><span class="n">BaseChatEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Condense Question Chat Engine.</span>

<span class="sd">    First generate a standalone question from conversation context and last message,</span>
<span class="sd">    then query the query engine for a response.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">condense_question_prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLMPredictorType</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_condense_question_prompt</span> <span class="o">=</span> <span class="n">condense_question_prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span> <span class="o">=</span> <span class="n">memory</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">condense_question_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CondenseQuestionChatEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a CondenseQuestionChatEngine from default parameters."""</span>
        <span class="n">condense_question_prompt</span> <span class="o">=</span> <span class="n">condense_question_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_PROMPT</span>

        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                <span class="s2">"system_prompt is not supported for CondenseQuestionChatEngine."</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
                <span class="s2">"prefix_messages is not supported for CondenseQuestionChatEngine."</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="p">,</span>
            <span class="n">condense_question_prompt</span><span class="p">,</span>
            <span class="n">memory</span><span class="p">,</span>
            <span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_condense_question</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="n">last_message</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generate standalone question from conversation context and last message.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">chat_history</span><span class="p">:</span>
            <span class="c1"># Keep the question as is if there's no conversation context.</span>
            <span class="k">return</span> <span class="n">last_message</span>

        <span class="n">chat_history_str</span> <span class="o">=</span> <span class="n">messages_to_history_str</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">chat_history_str</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_condense_question_prompt</span><span class="p">,</span>
            <span class="n">question</span><span class="o">=</span><span class="n">last_message</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history_str</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_acondense_question</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="n">last_message</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generate standalone question from conversation context and last message.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">chat_history</span><span class="p">:</span>
            <span class="c1"># Keep the question as is if there's no conversation context.</span>
            <span class="k">return</span> <span class="n">last_message</span>

        <span class="n">chat_history_str</span> <span class="o">=</span> <span class="n">messages_to_history_str</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">chat_history_str</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_condense_question_prompt</span><span class="p">,</span>
            <span class="n">question</span><span class="o">=</span><span class="n">last_message</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history_str</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_tool_output_from_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TYPE</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="n">StreamingResponse</span><span class="p">,</span> <span class="n">AsyncStreamingResponse</span><span class="p">)):</span>
            <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span>
                <span class="n">tool_name</span><span class="o">=</span><span class="s2">"query_engine"</span><span class="p">,</span>
                <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">},</span>
                <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
                <span class="n">tool_name</span><span class="o">=</span><span class="s2">"query_engine"</span><span class="p">,</span>
                <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">},</span>
                <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">message</span><span class="p">)</span>

        <span class="c1"># Generate standalone question from conversation context and last message</span>
        <span class="n">condensed_question</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_condense_question</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Querying with: </span><span class="si">{</span><span class="n">condensed_question</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>

        <span class="c1"># TODO: right now, query engine uses class attribute to configure streaming,</span>
        <span class="c1">#       we are moving towards separate streaming and non-streaming methods.</span>
        <span class="c1">#       In the meanwhile, use this hack to toggle streaming.</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="n">is_streaming</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="c1"># Query with standalone question</span>
        <span class="n">query_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">condensed_question</span><span class="p">)</span>

        <span class="c1"># NOTE: reset streaming flag</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">is_streaming</span>

        <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_output_from_response</span><span class="p">(</span>
            <span class="n">condensed_question</span><span class="p">,</span> <span class="n">query_response</span>
        <span class="p">)</span>

        <span class="c1"># Record response</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">query_response</span><span class="p">))</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">query_response</span><span class="p">),</span> <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="n">tool_output</span><span class="p">])</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">message</span><span class="p">)</span>

        <span class="c1"># Generate standalone question from conversation context and last message</span>
        <span class="n">condensed_question</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_condense_question</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Querying with: </span><span class="si">{</span><span class="n">condensed_question</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>

        <span class="c1"># TODO: right now, query engine uses class attribute to configure streaming,</span>
        <span class="c1">#       we are moving towards separate streaming and non-streaming methods.</span>
        <span class="c1">#       In the meanwhile, use this hack to toggle streaming.</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="n">is_streaming</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="c1"># Query with standalone question</span>
        <span class="n">query_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">condensed_question</span><span class="p">)</span>

        <span class="c1"># NOTE: reset streaming flag</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">is_streaming</span>

        <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_output_from_response</span><span class="p">(</span>
            <span class="n">condensed_question</span><span class="p">,</span> <span class="n">query_response</span>
        <span class="p">)</span>

        <span class="c1"># Record response</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="nb">isinstance</span><span class="p">(</span><span class="n">query_response</span><span class="p">,</span> <span class="n">StreamingResponse</span><span class="p">)</span>
            <span class="ow">and</span> <span class="n">query_response</span><span class="o">.</span><span class="n">response_gen</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="c1"># override the generator to include writing to chat history</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">))</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
                <span class="n">chat_stream</span><span class="o">=</span><span class="n">response_gen_from_query_engine</span><span class="p">(</span><span class="n">query_response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">),</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="n">tool_output</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span>
                <span class="n">target</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">write_response_to_history</span><span class="p">,</span>
                <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">,),</span>
            <span class="p">)</span>
            <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Streaming is not enabled. Please use chat() instead."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">message</span><span class="p">)</span>

        <span class="c1"># Generate standalone question from conversation context and last message</span>
        <span class="n">condensed_question</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_acondense_question</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Querying with: </span><span class="si">{</span><span class="n">condensed_question</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>

        <span class="c1"># TODO: right now, query engine uses class attribute to configure streaming,</span>
        <span class="c1">#       we are moving towards separate streaming and non-streaming methods.</span>
        <span class="c1">#       In the meanwhile, use this hack to toggle streaming.</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="n">is_streaming</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="c1"># Query with standalone question</span>
        <span class="n">query_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">condensed_question</span><span class="p">)</span>

        <span class="c1"># NOTE: reset streaming flag</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">is_streaming</span>

        <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_output_from_response</span><span class="p">(</span>
            <span class="n">condensed_question</span><span class="p">,</span> <span class="n">query_response</span>
        <span class="p">)</span>

        <span class="c1"># Record response</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">query_response</span><span class="p">))</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">query_response</span><span class="p">),</span> <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="n">tool_output</span><span class="p">])</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">message</span><span class="p">)</span>

        <span class="c1"># Generate standalone question from conversation context and last message</span>
        <span class="n">condensed_question</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_acondense_question</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="n">log_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Querying with: </span><span class="si">{</span><span class="n">condensed_question</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">log_str</span><span class="p">)</span>

        <span class="c1"># TODO: right now, query engine uses class attribute to configure streaming,</span>
        <span class="c1">#       we are moving towards separate streaming and non-streaming methods.</span>
        <span class="c1">#       In the meanwhile, use this hack to toggle streaming.</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="n">is_streaming</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="c1"># Query with standalone question</span>
        <span class="n">query_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">condensed_question</span><span class="p">)</span>

        <span class="c1"># NOTE: reset streaming flag</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="p">,</span> <span class="n">RetrieverQueryEngine</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">_response_synthesizer</span><span class="o">.</span><span class="n">_streaming</span> <span class="o">=</span> <span class="n">is_streaming</span>

        <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_output_from_response</span><span class="p">(</span>
            <span class="n">condensed_question</span><span class="p">,</span> <span class="n">query_response</span>
        <span class="p">)</span>

        <span class="c1"># Record response</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">query_response</span><span class="p">,</span> <span class="n">AsyncStreamingResponse</span><span class="p">):</span>
            <span class="c1"># override the generator to include writing to chat history</span>
            <span class="c1"># TODO: query engine does not support async generator yet</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">))</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
                <span class="n">achat_stream</span><span class="o">=</span><span class="n">aresponse_gen_from_query_engine</span><span class="p">(</span>
                    <span class="n">query_response</span><span class="o">.</span><span class="n">async_response_gen</span><span class="p">()</span>
                <span class="p">),</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="n">tool_output</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">awrite_response_to_history</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Streaming is not enabled. Please use achat() instead."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Clear chat history</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### chat\_history `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/#llama_index.core.chat_engine.CondenseQuestionChatEngine.chat_history "Permanent link")

```
chat_history: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/#llama_index.core.chat_engine.CondenseQuestionChatEngine.from_defaults "Permanent link")

```
from_defaults(query_engine: [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine"), condense_question_prompt: Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.base.BasePromptTemplate")] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = None, memory_cls: Type[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = ChatMemoryBuffer, service_context: Optional[ServiceContext] = None, verbose: bool = False, system_prompt: Optional[str] = None, prefix_messages: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, **kwargs: Any) -> [CondenseQuestionChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/#llama_index.core.chat_engine.CondenseQuestionChatEngine "llama_index.core.chat_engine.condense_question.CondenseQuestionChatEngine")
```

Initialize a CondenseQuestionChatEngine from default parameters.

Source code in `llama-index-core/llama_index/core/chat_engine/condense_question.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 80</span>
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
<span class="normal">121</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
    <span class="n">condense_question_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CondenseQuestionChatEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a CondenseQuestionChatEngine from default parameters."""</span>
    <span class="n">condense_question_prompt</span> <span class="o">=</span> <span class="n">condense_question_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_PROMPT</span>

    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

    <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"system_prompt is not supported for CondenseQuestionChatEngine."</span>
        <span class="p">)</span>
    <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"prefix_messages is not supported for CondenseQuestionChatEngine."</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">query_engine</span><span class="p">,</span>
        <span class="n">condense_question_prompt</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Condense plus context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_plus_context/)[Next Context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/)
