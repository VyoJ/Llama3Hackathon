Title: Azure code interpreter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/

Markdown Content:
Azure code interpreter - LlamaIndex


AzureCodeInterpreterToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Azure Code Interpreter tool spec.

Leverages Azure Dynamic Sessions to execute Python code.

Source code in `llama-index-integrations/tools/llama-index-tools-azure-code-interpreter/llama_index/tools/azure_code_interpreter/base.py`

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
<span class="normal">296</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureCodeInterpreterToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure Code Interpreter tool spec.</span>

<span class="sd">    Leverages Azure Dynamic Sessions to execute Python code.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"code_interpreter"</span><span class="p">,</span> <span class="s2">"list_files"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">pool_managment_endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">session_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">local_save_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sanitize_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pool_management_endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">pool_managment_endpoint</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AccessToken</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">def</span> <span class="nf">_access_token_provider_factory</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
            <span class="k">def</span> <span class="nf">access_token_provider</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">                </span><span class="sd">"""Create a function that returns an access token."""</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="o">.</span><span class="n">expires_on</span><span class="p">,</span> <span class="n">timezone</span><span class="o">.</span><span class="n">utc</span>
                <span class="p">)</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span> <span class="o">+</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">5</span><span class="p">)):</span>
                    <span class="n">credential</span> <span class="o">=</span> <span class="n">DefaultAzureCredential</span><span class="p">()</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span> <span class="o">=</span> <span class="n">credential</span><span class="o">.</span><span class="n">get_token</span><span class="p">(</span>
                        <span class="s2">"https://dynamicsessions.io/.default"</span>
                    <span class="p">)</span>
                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="o">.</span><span class="n">token</span>

            <span class="k">return</span> <span class="n">access_token_provider</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span>
            <span class="p">[],</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">_access_token_provider_factory</span><span class="p">()</span>
<span class="w">        </span><span class="sd">"""A function that returns the access token to use for the session pool."""</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">session_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">session_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid4</span><span class="p">())</span>
<span class="w">        </span><span class="sd">"""The session ID to use for the session pool. Defaults to a random UUID."""</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">sanitize_input</span>
<span class="w">        </span><span class="sd">"""Whether to sanitize input before executing it."""</span>

        <span class="k">if</span> <span class="n">local_save_path</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">local_save_path</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Local save path </span><span class="si">{</span><span class="n">local_save_path</span><span class="si">}</span><span class="s2"> does not exist."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">local_save_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">local_save_path</span>
<span class="w">        </span><span class="sd">"""The local path to save files generated by Python interpreter."""</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">_package_version</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">version</span><span class="p">(</span>
                <span class="s2">"llamaindex-azure-code-interpreter"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">importlib</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">PackageNotFoundError</span><span class="p">:</span>
            <span class="n">_package_version</span> <span class="o">=</span> <span class="s2">"0.0.0"</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">user_agent</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"llamaindex-azure-code-interpreter/</span><span class="si">{</span><span class="n">_package_version</span><span class="si">}</span><span class="s2"> (Language=Python)"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">pool_management_endpoint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pool_management_endpoint</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">pool_management_endpoint</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"pool_management_endpoint is not set"</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">pool_management_endpoint</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"/"</span><span class="p">):</span>
            <span class="n">pool_management_endpoint</span> <span class="o">+=</span> <span class="s2">"/"</span>

        <span class="n">encoded_session_id</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">parse</span><span class="o">.</span><span class="n">quote</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">session_id</span><span class="p">)</span>
        <span class="n">query</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"identifier=</span><span class="si">{</span><span class="n">encoded_session_id</span><span class="si">}</span><span class="s2">&amp;api-version=2024-02-02-preview"</span>
        <span class="n">query_separator</span> <span class="o">=</span> <span class="s2">"&amp;"</span> <span class="k">if</span> <span class="s2">"?"</span> <span class="ow">in</span> <span class="n">pool_management_endpoint</span> <span class="k">else</span> <span class="s2">"?"</span>

        <span class="k">return</span> <span class="n">pool_management_endpoint</span> <span class="o">+</span> <span class="n">path</span> <span class="o">+</span> <span class="n">query_separator</span> <span class="o">+</span> <span class="n">query</span>

    <span class="k">def</span> <span class="nf">code_interpreter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">python_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This tool is used to execute python commands when you need to perform calculations or computations in a Session.</span>
<span class="sd">        Input should be a valid python command. The tool returns the result, stdout, and stderr.</span>

<span class="sd">        Args:</span>
<span class="sd">            python_code (str): Python code to be executed generated by llm.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_input</span><span class="p">:</span>
            <span class="n">python_code</span> <span class="o">=</span> <span class="n">_sanitize_input</span><span class="p">(</span><span class="n">python_code</span><span class="p">)</span>

        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
        <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"code/execute"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"User-Agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">user_agent</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">body</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"properties"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"codeInputType"</span><span class="p">:</span> <span class="s2">"inline"</span><span class="p">,</span>
                <span class="s2">"executionType"</span><span class="p">:</span> <span class="s2">"synchronous"</span><span class="p">,</span>
                <span class="s2">"code"</span><span class="p">:</span> <span class="n">python_code</span><span class="p">,</span>
            <span class="p">}</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">body</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">if</span> <span class="s2">"properties"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">:</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="s2">"result"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span>
                <span class="ow">and</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]</span>
            <span class="p">):</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
                    <span class="k">if</span> <span class="s2">"base64_data"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]:</span>
                        <span class="n">base64_encoded_data</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                            <span class="s2">"base64_data"</span>
                        <span class="p">]</span>
                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">local_save_path</span><span class="p">:</span>
                            <span class="n">file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">local_save_path</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">session_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s1">'%Y%m</span><span class="si">%d</span><span class="s1">_%H%M%S'</span><span class="p">)</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="n">response_json</span><span class="p">[</span><span class="s1">'properties'</span><span class="p">][</span><span class="s1">'result'</span><span class="p">][</span><span class="s1">'format'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
                            <span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">base64_encoded_data</span><span class="p">)</span>
                            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
                            <span class="c1"># Check if file is written to the file path successfully. if so, update the response_json</span>
                            <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                                <span class="s2">"saved_to_local_path"</span>
                            <span class="p">]</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"base64_data"</span><span class="p">)</span>
                            <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">file_path</span><span class="p">):</span>
                                <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                                    <span class="s2">"saved_to_local_path"</span>
                                <span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
                            <span class="k">else</span><span class="p">:</span>
                                <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                                    <span class="s2">"saved_to_local_path"</span>
                                <span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span><span class="s2">"base64_data"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">return</span> <span class="n">response_json</span>

    <span class="k">def</span> <span class="nf">upload_file</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">local_file_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RemoteFileMetadata</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Upload a file to the session under the path /mnt/data.</span>

<span class="sd">        Args:</span>
<span class="sd">            data: The data to upload.</span>
<span class="sd">            local_file_path: The path to the local file to upload.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[RemoteFileMetadata]: The list of metadatas for the uploaded files.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">data</span> <span class="ow">and</span> <span class="n">local_file_path</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"data and local_file_path cannot be provided together"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">local_file_path</span><span class="p">:</span>
            <span class="n">remote_file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"/mnt/data/</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">data</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span>

        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">remote_file_path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"/mnt/data"</span><span class="p">):</span>
            <span class="n">remote_file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"/mnt/data/</span><span class="si">{</span><span class="n">remote_file_path</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"files/upload"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">files</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">"file"</span><span class="p">,</span> <span class="p">(</span><span class="n">remote_file_path</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="s2">"application/octet-stream"</span><span class="p">))]</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="s2">"POST"</span><span class="p">,</span> <span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">files</span><span class="o">=</span><span class="n">files</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">remote_files_metadatas</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]:</span>
            <span class="k">if</span> <span class="s2">"properties"</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">:</span>
                <span class="n">remote_files_metadatas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">RemoteFileMetadata</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">entry</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">])</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">remote_files_metadatas</span>

    <span class="k">def</span> <span class="nf">download_file_to_local</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">remote_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">local_file_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BufferedReader</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Download a file from the session back to your local environment.</span>

<span class="sd">        Args:</span>
<span class="sd">            remote_file_path: The path to download the file from, relative to `/mnt/data`.</span>
<span class="sd">            local_file_path: The path to save the downloaded file to. If not provided, the file is returned as a BufferedReader.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BufferedReader: The data of the downloaded file.</span>
<span class="sd">        """</span>
        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
        <span class="c1"># In case if the file path LLM provides is absolute, remove the /mnt/data/ prefix</span>
        <span class="n">remote_file_path</span> <span class="o">=</span> <span class="n">remote_file_path</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"/mnt/data/"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
        <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="sa">f</span><span class="s2">"files/content/</span><span class="si">{</span><span class="n">remote_file_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">local_file_path</span><span class="p">:</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">list_files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RemoteFileMetadata</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""List the files in the session.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[RemoteFileMetadata]: The metadata for the files in the session</span>
<span class="sd">        """</span>
        <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
        <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"files"</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">RemoteFileMetadata</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">entry</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### access\_token\_provider `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.access_token_provider "Permanent link")

```
access_token_provider: Callable[[], Optional[str]] = _access_token_provider_factory()
```

A function that returns the access token to use for the session pool.

### session\_id `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.session_id "Permanent link")

```
session_id: str = [session_id](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.session_id "llama_index.tools.azure_code_interpreter.base.AzureCodeInterpreterToolSpec.session_id") or str(uuid4())
```

The session ID to use for the session pool. Defaults to a random UUID.

### sanitize\_input `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.sanitize_input "Permanent link")

```
sanitize_input: bool = [sanitize_input](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.sanitize_input "llama_index.tools.azure_code_interpreter.base.AzureCodeInterpreterToolSpec.sanitize_input")
```

Whether to sanitize input before executing it.

### local\_save\_path `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.local_save_path "Permanent link")

```
local_save_path: Optional[str] = [local_save_path](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.local_save_path "llama_index.tools.azure_code_interpreter.base.AzureCodeInterpreterToolSpec.local_save_path")
```

The local path to save files generated by Python interpreter.

### code\_interpreter [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.code_interpreter "Permanent link")

```
code_interpreter(python_code: str) -> dict
```

This tool is used to execute python commands when you need to perform calculations or computations in a Session. Input should be a valid python command. The tool returns the result, stdout, and stderr.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `python_code` | `str` | 
Python code to be executed generated by llm.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-code-interpreter/llama_index/tools/azure_code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">144</span>
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
<span class="normal">202</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">code_interpreter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">python_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This tool is used to execute python commands when you need to perform calculations or computations in a Session.</span>
<span class="sd">    Input should be a valid python command. The tool returns the result, stdout, and stderr.</span>

<span class="sd">    Args:</span>
<span class="sd">        python_code (str): Python code to be executed generated by llm.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_input</span><span class="p">:</span>
        <span class="n">python_code</span> <span class="o">=</span> <span class="n">_sanitize_input</span><span class="p">(</span><span class="n">python_code</span><span class="p">)</span>

    <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
    <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"code/execute"</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="s2">"User-Agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">user_agent</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">body</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"properties"</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">"codeInputType"</span><span class="p">:</span> <span class="s2">"inline"</span><span class="p">,</span>
            <span class="s2">"executionType"</span><span class="p">:</span> <span class="s2">"synchronous"</span><span class="p">,</span>
            <span class="s2">"code"</span><span class="p">:</span> <span class="n">python_code</span><span class="p">,</span>
        <span class="p">}</span>
    <span class="p">}</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">body</span><span class="p">)</span>
    <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
    <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">if</span> <span class="s2">"properties"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="s2">"result"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span>
            <span class="ow">and</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">if</span> <span class="s2">"base64_data"</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]:</span>
                    <span class="n">base64_encoded_data</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                        <span class="s2">"base64_data"</span>
                    <span class="p">]</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">local_save_path</span><span class="p">:</span>
                        <span class="n">file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">local_save_path</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">session_id</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s1">'%Y%m</span><span class="si">%d</span><span class="s1">_%H%M%S'</span><span class="p">)</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="n">response_json</span><span class="p">[</span><span class="s1">'properties'</span><span class="p">][</span><span class="s1">'result'</span><span class="p">][</span><span class="s1">'format'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
                        <span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">base64_encoded_data</span><span class="p">)</span>
                        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
                        <span class="c1"># Check if file is written to the file path successfully. if so, update the response_json</span>
                        <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                            <span class="s2">"saved_to_local_path"</span>
                        <span class="p">]</span> <span class="o">=</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"base64_data"</span><span class="p">)</span>
                        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">file_path</span><span class="p">):</span>
                            <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                                <span class="s2">"saved_to_local_path"</span>
                            <span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span>
                                <span class="s2">"saved_to_local_path"</span>
                            <span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">response_json</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"result"</span><span class="p">][</span><span class="s2">"base64_data"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">return</span> <span class="n">response_json</span>
</code></pre></div></td></tr></tbody></table>

### upload\_file [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.upload_file "Permanent link")

```
upload_file(data: Optional[Any] = None, local_file_path: Optional[str] = None) -> List[RemoteFileMetadata]
```

Upload a file to the session under the path /mnt/data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `data` | `Optional[Any]` | 
The data to upload.



 | `None` |
| `local_file_path` | `Optional[str]` | 

The path to the local file to upload.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[RemoteFileMetadata]` | 
List\[RemoteFileMetadata\]: The list of metadatas for the uploaded files.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-code-interpreter/llama_index/tools/azure_code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">204</span>
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
<span class="normal">245</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upload_file</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">local_file_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RemoteFileMetadata</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Upload a file to the session under the path /mnt/data.</span>

<span class="sd">    Args:</span>
<span class="sd">        data: The data to upload.</span>
<span class="sd">        local_file_path: The path to the local file to upload.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[RemoteFileMetadata]: The list of metadatas for the uploaded files.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">data</span> <span class="ow">and</span> <span class="n">local_file_path</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"data and local_file_path cannot be provided together"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">local_file_path</span><span class="p">:</span>
        <span class="n">remote_file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"/mnt/data/</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">data</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span>

    <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">remote_file_path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"/mnt/data"</span><span class="p">):</span>
        <span class="n">remote_file_path</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"/mnt/data/</span><span class="si">{</span><span class="n">remote_file_path</span><span class="si">}</span><span class="s2">"</span>
    <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"files/upload"</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">files</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">"file"</span><span class="p">,</span> <span class="p">(</span><span class="n">remote_file_path</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="s2">"application/octet-stream"</span><span class="p">))]</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="s2">"POST"</span><span class="p">,</span> <span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">files</span><span class="o">=</span><span class="n">files</span><span class="p">)</span>
    <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

    <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="n">remote_files_metadatas</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]:</span>
        <span class="k">if</span> <span class="s2">"properties"</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">:</span>
            <span class="n">remote_files_metadatas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">RemoteFileMetadata</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">entry</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">])</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">remote_files_metadatas</span>
</code></pre></div></td></tr></tbody></table>

### download\_file\_to\_local [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.download_file_to_local "Permanent link")

```
download_file_to_local(remote_file_path: str, local_file_path: Optional[str] = None) -> Optional[BufferedReader]
```

Download a file from the session back to your local environment.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `remote_file_path` | `str` | 
The path to download the file from, relative to `/mnt/data`.



 | _required_ |
| `local_file_path` | `Optional[str]` | 

The path to save the downloaded file to. If not provided, the file is returned as a BufferedReader.



 | `None` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `BufferedReader` | `Optional[BufferedReader]` | 
The data of the downloaded file.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-code-interpreter/llama_index/tools/azure_code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">247</span>
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
<span class="normal">275</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">download_file_to_local</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">remote_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">local_file_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BufferedReader</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Download a file from the session back to your local environment.</span>

<span class="sd">    Args:</span>
<span class="sd">        remote_file_path: The path to download the file from, relative to `/mnt/data`.</span>
<span class="sd">        local_file_path: The path to save the downloaded file to. If not provided, the file is returned as a BufferedReader.</span>

<span class="sd">    Returns:</span>
<span class="sd">        BufferedReader: The data of the downloaded file.</span>
<span class="sd">    """</span>
    <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
    <span class="c1"># In case if the file path LLM provides is absolute, remove the /mnt/data/ prefix</span>
    <span class="n">remote_file_path</span> <span class="o">=</span> <span class="n">remote_file_path</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"/mnt/data/"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
    <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="sa">f</span><span class="s2">"files/content/</span><span class="si">{</span><span class="n">remote_file_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
    <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

    <span class="k">if</span> <span class="n">local_file_path</span><span class="p">:</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">local_file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### list\_files [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/#llama_index.tools.azure_code_interpreter.AzureCodeInterpreterToolSpec.list_files "Permanent link")

```
list_files() -> List[RemoteFileMetadata]
```

List the files in the session.

**Returns:**

| Type | Description |
| --- | --- |
| `List[RemoteFileMetadata]` | 
List\[RemoteFileMetadata\]: The metadata for the files in the session



 |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-code-interpreter/llama_index/tools/azure_code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">277</span>
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
<span class="normal">296</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">RemoteFileMetadata</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""List the files in the session.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[RemoteFileMetadata]: The metadata for the files in the session</span>
<span class="sd">    """</span>
    <span class="n">access_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token_provider</span><span class="p">()</span>
    <span class="n">api_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_url</span><span class="p">(</span><span class="s2">"files"</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">api_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
    <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

    <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="n">RemoteFileMetadata</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">entry</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/)[Next Azure cv](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/)
