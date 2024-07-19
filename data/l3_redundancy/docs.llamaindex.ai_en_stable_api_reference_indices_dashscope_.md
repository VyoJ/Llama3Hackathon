Title: Dashscope - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/

Markdown Content:
Dashscope - LlamaIndex


DashScopeCloudIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/#llama_index.indices.managed.dashscope.DashScopeCloudIndex "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

DashScope Cloud Platform Index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-dashscope/llama_index/indices/managed/dashscope/base.py`

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
<span class="normal">279</span>
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DashScopeCloudIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DashScope Cloud Platform Index."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">60</span><span class="p">,</span>
        <span class="n">workspace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the Platform Index."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">transformations</span> <span class="o">=</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"DashScopeCloudIndex does not support nodes on initialization"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">workspace_id</span> <span class="o">=</span> <span class="n">workspace_id</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_WORKSPACE_ID"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_BASE_URL"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="n">base_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Accept-Encoding"</span><span class="p">:</span> <span class="s2">"utf-8"</span><span class="p">,</span>
            <span class="s2">"X-DashScope-WorkSpace"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">workspace_id</span><span class="p">,</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="s2">"Bearer "</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span>
            <span class="s2">"X-DashScope-OpenAPISource"</span><span class="p">:</span> <span class="s2">"CloudSDK"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span> <span class="o">=</span> <span class="n">timeout</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">callback_manager</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s2">"DashScopeCloudIndex"</span><span class="p">],</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">workspace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">60</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"DashScopeCloudIndex"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build a DashScope index from a sequence of documents."""</span>
        <span class="n">pipeline_create</span> <span class="o">=</span> <span class="n">get_pipeline_create</span><span class="p">(</span>
            <span class="n">name</span><span class="p">,</span> <span class="n">transformations</span> <span class="ow">or</span> <span class="n">default_transformations</span><span class="p">(),</span> <span class="n">documents</span>
        <span class="p">)</span>

        <span class="n">workspace_id</span> <span class="o">=</span> <span class="n">workspace_id</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_WORKSPACE_ID"</span><span class="p">)</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_API_KEY"</span><span class="p">)</span>
        <span class="n">base_url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">base_url</span>
            <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"DASHSCOPE_BASE_URL"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="ow">or</span> <span class="n">DASHSCOPE_DEFAULT_BASE_URL</span>
        <span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Accept-Encoding"</span><span class="p">:</span> <span class="s2">"utf-8"</span><span class="p">,</span>
            <span class="s2">"X-DashScope-WorkSpace"</span><span class="p">:</span> <span class="n">workspace_id</span><span class="p">,</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="s2">"Bearer "</span> <span class="o">+</span> <span class="n">api_key</span><span class="p">,</span>
            <span class="s2">"X-DashScope-OpenAPISource"</span><span class="p">:</span> <span class="s2">"CloudSDK"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
            <span class="n">base_url</span> <span class="o">+</span> <span class="n">UPSERT_PIPELINE_ENDPOINT</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">pipeline_create</span><span class="p">),</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response_text</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">pipeline_id</span> <span class="o">=</span> <span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"code"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span> <span class="o">!=</span> <span class="n">Status</span><span class="o">.</span><span class="n">SUCCESS</span><span class="o">.</span><span class="n">value</span> <span class="ow">or</span> <span class="n">pipeline_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Failed to create index: </span><span class="si">{</span><span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'message'</span><span class="p">,</span><span class="w"> </span><span class="s1">''</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Starting creating index </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">, pipeline_id: </span><span class="si">{</span><span class="n">pipeline_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="n">base_url</span> <span class="o">+</span> <span class="n">START_PIPELINE_ENDPOINT</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">),</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response_text</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">ingestion_id</span> <span class="o">=</span> <span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"ingestionId"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"code"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span> <span class="o">!=</span> <span class="n">Status</span><span class="o">.</span><span class="n">SUCCESS</span><span class="o">.</span><span class="n">value</span>
            <span class="ow">or</span> <span class="n">ingestion_id</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Failed to start ingestion: </span><span class="si">{</span><span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'message'</span><span class="p">,</span><span class="w"> </span><span class="s1">''</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Starting ingestion for index </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">, ingestion_id: </span><span class="si">{</span><span class="n">ingestion_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">ingestion_status</span><span class="p">,</span> <span class="n">failed_docs</span> <span class="o">=</span> <span class="n">run_ingestion</span><span class="p">(</span>
            <span class="n">base_url</span>
            <span class="o">+</span> <span class="n">CHECK_INGESTION_ENDPOINT</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">,</span> <span class="n">ingestion_id</span><span class="o">=</span><span class="n">ingestion_id</span>
            <span class="p">),</span>
            <span class="n">headers</span><span class="p">,</span>
            <span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"ingestion_status </span><span class="si">{</span><span class="n">ingestion_status</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"failed_docs: </span><span class="si">{</span><span class="n">failed_docs</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">ingestion_status</span> <span class="o"></span> <span class="s2">"FAILED"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Index </span><span class="si">{name}</span><span class="s2"> created failed!"</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2"> created successfully!"</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">name</span><span class="p">,</span>
        <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
        <span class="n">workspace_id</span><span class="o">=</span><span class="n">workspace_id</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
        <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/#llama_index.indices.managed.dashscope.DashScopeCloudIndex.as_retriever "Permanent link")

```
as_retriever(**kwargs: Any) -> [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")
```

Return a Retriever for this managed index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-dashscope/llama_index/indices/managed/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a Retriever for this managed index."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.indices.managed.dashscope.retriever</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">DashScopeCloudRetriever</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">DashScopeCloudRetriever</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/#llama_index.indices.managed.dashscope.DashScopeCloudIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_ids: Union[str, List[str]], verbose: bool = True, **delete_kwargs: Any) -> None
```

Delete documents in index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-dashscope/llama_index/indices/managed/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">250</span>
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
<span class="normal">276</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">ref_doc_ids</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete documents in index."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ref_doc_ids</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">ref_doc_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">ref_doc_ids</span><span class="p">]</span>
    <span class="n">pipeline_id</span> <span class="o">=</span> <span class="n">get_pipeline_id</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">+</span> <span class="n">PIPELINE_SIMPLE_ENDPOINT</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">,</span>
        <span class="p">{</span><span class="s2">"pipeline_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">},</span>
    <span class="p">)</span>
    <span class="n">doc_delete</span> <span class="o">=</span> <span class="n">get_doc_delete</span><span class="p">(</span><span class="n">ref_doc_ids</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">+</span> <span class="n">DELETE_DOC_ENDPOINT</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">pipeline_id</span><span class="o">=</span><span class="n">pipeline_id</span><span class="p">),</span>
        <span class="n">json</span><span class="o">=</span><span class="n">doc_delete</span><span class="p">,</span>
        <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">response_text</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"code"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span> <span class="o">!=</span> <span class="n">Status</span><span class="o">.</span><span class="n">SUCCESS</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Failed to delete documents: </span><span class="si">{</span><span class="n">response_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'message'</span><span class="p">,</span><span class="w"> </span><span class="s1">''</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">response_text</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Delete documents </span><span class="si">{</span><span class="n">ref_doc_ids</span><span class="si">}</span><span class="s2"> successfully!"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/#llama_index.indices.managed.dashscope.DashScopeCloudIndex.update_ref_doc "Permanent link")

```
update_ref_doc(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **update_kwargs: Any) -> None
```

Update a document and it's corresponding nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-dashscope/llama_index/indices/managed/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update a document and it's corresponding nodes."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"update_ref_doc not implemented."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Colbert](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/)[Next Document summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/)
