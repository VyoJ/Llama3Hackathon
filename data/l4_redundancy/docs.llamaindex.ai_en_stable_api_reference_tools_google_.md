Title: Google - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/google/

Markdown Content:
Google - LlamaIndex


GmailToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

GMail tool spec.

Gives the agent the ability to read, draft and send gmail messages

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
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
<span class="normal">279</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GmailToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GMail tool spec.</span>

<span class="sd">    Gives the agent the ability to read, draft and send gmail messages</span>

<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s2">"load_data"</span><span class="p">,</span>
        <span class="s2">"search_messages"</span><span class="p">,</span>
        <span class="s2">"create_draft"</span><span class="p">,</span>
        <span class="s2">"update_draft"</span><span class="p">,</span>
        <span class="s2">"get_draft"</span><span class="p">,</span>
        <span class="s2">"send_draft"</span><span class="p">,</span>
    <span class="p">]</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">use_iterative_parser</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">max_results</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span>
    <span class="n">service</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_cache_service</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"gmail"</span><span class="p">,</span> <span class="s2">"v1"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load emails from the user's account."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_messages</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_get_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get valid user credentials from storage.</span>

<span class="sd">        The file token.json stores the user's access and refresh tokens, and is</span>
<span class="sd">        created automatically when the authorization flow completes for the first</span>
<span class="sd">        time.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Credentials, the obtained credential.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="kn">from</span> <span class="nn">google.auth.transport.requests</span> <span class="kn">import</span> <span class="n">Request</span>
        <span class="kn">from</span> <span class="nn">google.oauth2.credentials</span> <span class="kn">import</span> <span class="n">Credentials</span>
        <span class="kn">from</span> <span class="nn">google_auth_oauthlib.flow</span> <span class="kn">import</span> <span class="n">InstalledAppFlow</span>

        <span class="n">creds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">):</span>
            <span class="n">creds</span> <span class="o">=</span> <span class="n">Credentials</span><span class="o">.</span><span class="n">from_authorized_user_file</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="n">SCOPES</span><span class="p">)</span>
        <span class="c1"># If there are no (valid) credentials available, let the user log in.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">creds</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">creds</span><span class="o">.</span><span class="n">valid</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">creds</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">expired</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">refresh_token</span><span class="p">:</span>
                <span class="n">creds</span><span class="o">.</span><span class="n">refresh</span><span class="p">(</span><span class="n">Request</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">flow</span> <span class="o">=</span> <span class="n">InstalledAppFlow</span><span class="o">.</span><span class="n">from_client_secrets_file</span><span class="p">(</span>
                    <span class="s2">"credentials.json"</span><span class="p">,</span> <span class="n">SCOPES</span>
                <span class="p">)</span>
                <span class="n">creds</span> <span class="o">=</span> <span class="n">flow</span><span class="o">.</span><span class="n">run_local_server</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
            <span class="c1"># Save the credentials for the next run</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">token</span><span class="p">:</span>
                <span class="n">token</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">creds</span><span class="o">.</span><span class="n">to_json</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">creds</span>

    <span class="k">def</span> <span class="nf">search_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">max_results</span><span class="p">:</span>
            <span class="n">max_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_results</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">messages</span><span class="p">()</span>
            <span class="o">.</span><span class="n">list</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">q</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">maxResults</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">max_results</span><span class="p">))</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
            <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"messages"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
                <span class="n">message_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_message_data</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">message_data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"body"</span><span class="p">)</span>
                <span class="n">extra_info</span> <span class="o">=</span> <span class="n">message_data</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Can't get message data"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">get_message_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
        <span class="n">message_id</span> <span class="o">=</span> <span class="n">message</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
        <span class="n">message_data</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">messages</span><span class="p">()</span>
            <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">format</span><span class="o">=</span><span class="s2">"raw"</span><span class="p">,</span> <span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">message_id</span><span class="p">)</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_iterative_parser</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body_iterative</span><span class="p">(</span><span class="n">message_data</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body</span><span class="p">(</span><span class="n">message_data</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">body</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"id"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
            <span class="s2">"threadId"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"threadId"</span><span class="p">],</span>
            <span class="s2">"snippet"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"snippet"</span><span class="p">],</span>
            <span class="s2">"body"</span><span class="p">:</span> <span class="n">body</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">extract_message_body_iterative</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf8"</span><span class="p">))</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">message_from_bytes</span><span class="p">(</span><span class="n">body</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">message</span>

        <span class="n">body_text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="n">mime_msg</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span> <span class="o"></span> <span class="s2">"multipart"</span><span class="p">:</span>
            <span class="n">msg_parts</span> <span class="o">=</span> <span class="n">mime_msg</span><span class="o">.</span><span class="n">get_payload</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">msg_part</span> <span class="ow">in</span> <span class="n">msg_parts</span><span class="p">:</span>
                <span class="n">body_text</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body_iterative</span><span class="p">(</span><span class="n">msg_part</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">body_text</span>

    <span class="k">def</span> <span class="nf">extract_message_body</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">message_from_bytes</span><span class="p">(</span><span class="n">body</span><span class="p">)</span>

            <span class="c1"># If the message body contains HTML, parse it with BeautifulSoup</span>
            <span class="k">if</span> <span class="s2">"text/html"</span> <span class="ow">in</span> <span class="n">mime_msg</span><span class="p">:</span>
                <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">body</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
                <span class="n">body</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
            <span class="k">return</span> <span class="n">body</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Can't parse message body"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_build_draft</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">to</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">subject</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">email_message</span> <span class="o">=</span> <span class="n">EmailMessage</span><span class="p">()</span>

        <span class="n">email_message</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

        <span class="n">email_message</span><span class="p">[</span><span class="s2">"To"</span><span class="p">]</span> <span class="o">=</span> <span class="n">to</span>
        <span class="n">email_message</span><span class="p">[</span><span class="s2">"Subject"</span><span class="p">]</span> <span class="o">=</span> <span class="n">subject</span>

        <span class="n">encoded_message</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64encode</span><span class="p">(</span><span class="n">email_message</span><span class="o">.</span><span class="n">as_bytes</span><span class="p">())</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"message"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"raw"</span><span class="p">:</span> <span class="n">encoded_message</span><span class="p">}}</span>

    <span class="k">def</span> <span class="nf">create_draft</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">to</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">subject</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create and insert a draft email.</span>
<span class="sd">           Print the returned draft's message and id.</span>
<span class="sd">           Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">        Args:</span>
<span class="sd">            to (Optional[str]): The email addresses to send the message to</span>
<span class="sd">            subject (Optional[str]): The subject for the event</span>
<span class="sd">            message (Optional[str]): The message for the event</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">drafts</span><span class="p">()</span>
            <span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_build_draft</span><span class="p">(</span><span class="n">to</span><span class="p">,</span> <span class="n">subject</span><span class="p">,</span> <span class="n">message</span><span class="p">))</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_draft</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">to</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">subject</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update a draft email.</span>
<span class="sd">           Print the returned draft's message and id.</span>
<span class="sd">           This function is required to be passed a draft_id that is obtained when creating messages</span>
<span class="sd">           Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">        Args:</span>
<span class="sd">            to (Optional[str]): The email addresses to send the message to</span>
<span class="sd">            subject (Optional[str]): The subject for the event</span>
<span class="sd">            message (Optional[str]): The message for the event</span>
<span class="sd">            draft_id (str): the id of the draft to be updated</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>

        <span class="k">if</span> <span class="n">draft_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="s2">"You did not provide a draft id when calling this function. If you"</span>
                <span class="s2">" previously created or retrieved the draft, the id is available in"</span>
                <span class="s2">" context"</span>
            <span class="p">)</span>

        <span class="n">draft</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_draft</span><span class="p">(</span><span class="n">draft_id</span><span class="p">)</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="n">draft</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"payload"</span><span class="p">][</span><span class="s2">"headers"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">header</span> <span class="ow">in</span> <span class="n">headers</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">header</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"Subject"</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">subject</span><span class="p">:</span>
                <span class="n">subject</span> <span class="o">=</span> <span class="n">header</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">drafts</span><span class="p">()</span>
            <span class="o">.</span><span class="n">update</span><span class="p">(</span>
                <span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">draft_id</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_build_draft</span><span class="p">(</span><span class="n">to</span><span class="p">,</span> <span class="n">subject</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_draft</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get a draft email.</span>
<span class="sd">           Print the returned draft's message and id.</span>
<span class="sd">           Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">        Args:</span>
<span class="sd">            draft_id (str): the id of the draft to be updated</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>
        <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span><span class="o">.</span><span class="n">drafts</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">draft_id</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">send_draft</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Sends a draft email.</span>
<span class="sd">           Print the returned draft's message and id.</span>
<span class="sd">           Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">        Args:</span>
<span class="sd">            draft_id (str): the id of the draft to be updated</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span><span class="o">.</span><span class="n">drafts</span><span class="p">()</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">draft_id</span><span class="p">})</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load emails from the user's account.

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load emails from the user's account."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_messages</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### create\_draft [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec.create_draft "Permanent link")

```
create_draft(to: Optional[List[str]] = None, subject: Optional[str] = None, message: Optional[str] = None) -> str
```

Create and insert a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `to` | `Optional[str]` | 
The email addresses to send the message to



 | `None` |
| `subject` | `Optional[str]` | 

The subject for the event



 | `None` |
| `message` | `Optional[str]` | 

The message for the event



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">185</span>
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
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_draft</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">to</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">subject</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create and insert a draft email.</span>
<span class="sd">       Print the returned draft's message and id.</span>
<span class="sd">       Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">    Args:</span>
<span class="sd">        to (Optional[str]): The email addresses to send the message to</span>
<span class="sd">        subject (Optional[str]): The subject for the event</span>
<span class="sd">        message (Optional[str]): The message for the event</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>

    <span class="k">return</span> <span class="p">(</span>
        <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
        <span class="o">.</span><span class="n">drafts</span><span class="p">()</span>
        <span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_build_draft</span><span class="p">(</span><span class="n">to</span><span class="p">,</span> <span class="n">subject</span><span class="p">,</span> <span class="n">message</span><span class="p">))</span>
        <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update\_draft [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec.update_draft "Permanent link")

```
update_draft(to: Optional[List[str]] = None, subject: Optional[str] = None, message: Optional[str] = None, draft_id: str = None) -> str
```

Update a draft email. Print the returned draft's message and id. This function is required to be passed a draft\_id that is obtained when creating messages Returns: Draft object, including draft id and message meta data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `to` | `Optional[str]` | 
The email addresses to send the message to



 | `None` |
| `subject` | `Optional[str]` | 

The subject for the event



 | `None` |
| `message` | `Optional[str]` | 

The message for the event



 | `None` |
| `draft_id` | `str` | 

the id of the draft to be updated



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">210</span>
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
<span class="normal">253</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">update_draft</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">to</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">subject</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">message</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update a draft email.</span>
<span class="sd">       Print the returned draft's message and id.</span>
<span class="sd">       This function is required to be passed a draft_id that is obtained when creating messages</span>
<span class="sd">       Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">    Args:</span>
<span class="sd">        to (Optional[str]): The email addresses to send the message to</span>
<span class="sd">        subject (Optional[str]): The subject for the event</span>
<span class="sd">        message (Optional[str]): The message for the event</span>
<span class="sd">        draft_id (str): the id of the draft to be updated</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>

    <span class="k">if</span> <span class="n">draft_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="s2">"You did not provide a draft id when calling this function. If you"</span>
            <span class="s2">" previously created or retrieved the draft, the id is available in"</span>
            <span class="s2">" context"</span>
        <span class="p">)</span>

    <span class="n">draft</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_draft</span><span class="p">(</span><span class="n">draft_id</span><span class="p">)</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="n">draft</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"payload"</span><span class="p">][</span><span class="s2">"headers"</span><span class="p">]</span>
    <span class="k">for</span> <span class="n">header</span> <span class="ow">in</span> <span class="n">headers</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">header</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"Subject"</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">subject</span><span class="p">:</span>
            <span class="n">subject</span> <span class="o">=</span> <span class="n">header</span><span class="p">[</span><span class="s2">"value"</span><span class="p">]</span>

    <span class="k">return</span> <span class="p">(</span>
        <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
        <span class="o">.</span><span class="n">drafts</span><span class="p">()</span>
        <span class="o">.</span><span class="n">update</span><span class="p">(</span>
            <span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">draft_id</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_build_draft</span><span class="p">(</span><span class="n">to</span><span class="p">,</span> <span class="n">subject</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_draft [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec.get_draft "Permanent link")

```
get_draft(draft_id: str = None) -> str
```

Get a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `draft_id` | `str` | 
the id of the draft to be updated



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_draft</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get a draft email.</span>
<span class="sd">       Print the returned draft's message and id.</span>
<span class="sd">       Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">    Args:</span>
<span class="sd">        draft_id (str): the id of the draft to be updated</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>
    <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span><span class="o">.</span><span class="n">drafts</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">draft_id</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### send\_draft [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GmailToolSpec.send_draft "Permanent link")

```
send_draft(draft_id: str = None) -> str
```

Sends a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `draft_id` | `str` | 
the id of the draft to be updated



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">267</span>
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
<span class="normal">279</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">send_draft</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">draft_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Sends a draft email.</span>
<span class="sd">       Print the returned draft's message and id.</span>
<span class="sd">       Returns: Draft object, including draft id and message meta data.</span>

<span class="sd">    Args:</span>
<span class="sd">        draft_id (str): the id of the draft to be updated</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cache_service</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span>
    <span class="k">return</span> <span class="p">(</span>
        <span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span><span class="o">.</span><span class="n">drafts</span><span class="p">()</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">draft_id</span><span class="p">})</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

GoogleCalendarToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Google Calendar tool spec.

Currently a simple wrapper around the data loader. TODO: add more methods to the Google Calendar spec.

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/calendar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 27</span>
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
<span class="normal">202</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleCalendarToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Calendar tool spec.</span>

<span class="sd">    Currently a simple wrapper around the data loader.</span>
<span class="sd">    TODO: add more methods to the Google Calendar spec.</span>

<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"load_data"</span><span class="p">,</span> <span class="s2">"create_event"</span><span class="p">,</span> <span class="s2">"get_date"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
        <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from user's calendar.</span>

<span class="sd">        Args:</span>
<span class="sd">            number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">            start_date (Optional[Union[str, datetime.date]]): the start date to return events from in date isoformat. Defaults to today.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

        <span class="n">start_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">combine</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">min</span><span class="p">)</span>
        <span class="n">start_datetime_utc</span> <span class="o">=</span> <span class="n">start_datetime</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">Z"</span><span class="p">)</span>

        <span class="n">events_result</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span>
            <span class="o">.</span><span class="n">list</span><span class="p">(</span>
                <span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span>
                <span class="n">timeMin</span><span class="o">=</span><span class="n">start_datetime_utc</span><span class="p">,</span>
                <span class="n">maxResults</span><span class="o">=</span><span class="n">number_of_results</span><span class="p">,</span>
                <span class="n">singleEvents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">orderBy</span><span class="o">=</span><span class="s2">"startTime"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="n">events</span> <span class="o">=</span> <span class="n">events_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"items"</span><span class="p">,</span> <span class="p">[])</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">]:</span>
                <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

            <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">]:</span>
                <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

            <span class="n">event_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Status: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'status'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Summary: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'summary'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Start time: </span><span class="si">{</span><span class="n">start_time</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"End time: </span><span class="si">{</span><span class="n">end_time</span><span class="si">}</span><span class="s2">, "</span>

            <span class="n">organizer</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"organizer"</span><span class="p">,</span> <span class="p">{})</span>
            <span class="n">display_name</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"displayName"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
            <span class="n">email</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"email"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">display_name</span> <span class="o">!=</span> <span class="s2">"N/A"</span><span class="p">:</span>
                <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">)"</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">event_string</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_get_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get valid user credentials from storage.</span>

<span class="sd">        The file token.json stores the user's access and refresh tokens, and is</span>
<span class="sd">        created automatically when the authorization flow completes for the first</span>
<span class="sd">        time.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Credentials, the obtained credential.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">google_auth_oauthlib.flow</span> <span class="kn">import</span> <span class="n">InstalledAppFlow</span>

        <span class="kn">from</span> <span class="nn">google.auth.transport.requests</span> <span class="kn">import</span> <span class="n">Request</span>
        <span class="kn">from</span> <span class="nn">google.oauth2.credentials</span> <span class="kn">import</span> <span class="n">Credentials</span>

        <span class="n">creds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">):</span>
            <span class="n">creds</span> <span class="o">=</span> <span class="n">Credentials</span><span class="o">.</span><span class="n">from_authorized_user_file</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="n">SCOPES</span><span class="p">)</span>
        <span class="c1"># If there are no (valid) credentials available, let the user log in.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">creds</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">creds</span><span class="o">.</span><span class="n">valid</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">creds</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">expired</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">refresh_token</span><span class="p">:</span>
                <span class="n">creds</span><span class="o">.</span><span class="n">refresh</span><span class="p">(</span><span class="n">Request</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">flow</span> <span class="o">=</span> <span class="n">InstalledAppFlow</span><span class="o">.</span><span class="n">from_client_secrets_file</span><span class="p">(</span>
                    <span class="s2">"credentials.json"</span><span class="p">,</span> <span class="n">SCOPES</span>
                <span class="p">)</span>
                <span class="n">creds</span> <span class="o">=</span> <span class="n">flow</span><span class="o">.</span><span class="n">run_local_server</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
            <span class="c1"># Save the credentials for the next run</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">token</span><span class="p">:</span>
                <span class="n">token</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">creds</span><span class="o">.</span><span class="n">to_json</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">creds</span>

    <span class="k">def</span> <span class="nf">create_event</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">title</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">location</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">start_datetime</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_datetime</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">attendees</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">            Create an event on the users calendar.</span>

<span class="sd">        Args:</span>
<span class="sd">            title (Optional[str]): The title for the event</span>
<span class="sd">            description (Optional[str]): The description for the event</span>
<span class="sd">            location (Optional[str]): The location for the event</span>
<span class="sd">            start_datetime Optional[Union[str, datetime.datetime]]: The start datetime for the event</span>
<span class="sd">            end_datetime Optional[Union[str, datetime.datetime]]: The end datetime for the event</span>
<span class="sd">            attendees Optional[List[str]]: A list of email address to invite to the event</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

        <span class="n">attendees_list</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[{</span><span class="s2">"email"</span><span class="p">:</span> <span class="n">attendee</span><span class="p">}</span> <span class="k">for</span> <span class="n">attendee</span> <span class="ow">in</span> <span class="n">attendees</span><span class="p">]</span> <span class="k">if</span> <span class="n">attendees</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="n">start_time</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">start_datetime</span><span class="p">,</span> <span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S%z"</span><span class="p">)</span>
            <span class="o">.</span><span class="n">astimezone</span><span class="p">()</span>
            <span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">%z"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">end_time</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">end_datetime</span><span class="p">,</span> <span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S%z"</span><span class="p">)</span>
            <span class="o">.</span><span class="n">astimezone</span><span class="p">()</span>
            <span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">%z"</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="n">event</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"summary"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
            <span class="s2">"location"</span><span class="p">:</span> <span class="n">location</span><span class="p">,</span>
            <span class="s2">"description"</span><span class="p">:</span> <span class="n">description</span><span class="p">,</span>
            <span class="s2">"start"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"dateTime"</span><span class="p">:</span> <span class="n">start_time</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">"end"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"dateTime"</span><span class="p">:</span> <span class="n">end_time</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">"attendees"</span><span class="p">:</span> <span class="n">attendees_list</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">event</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">event</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="s2">"Your calendar event has been created successfully! You can move on to the"</span>
            <span class="s2">" next step."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_date</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        A function to return todays date. Call this before any other functions if you are unaware of the date.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.load_data "Permanent link")

```
load_data(number_of_results: Optional[int] = 100, start_date: Optional[Union[str, date]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from user's calendar.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `number_of_results` | `Optional[int]` | 
the number of events to return. Defaults to 100.



 | `100` |
| `start_date` | `Optional[Union[str, date]]` | 

the start date to return events from in date isoformat. Defaults to today.



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/calendar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
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
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from user's calendar.</span>

<span class="sd">    Args:</span>
<span class="sd">        number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">        start_date (Optional[Union[str, datetime.date]]): the start date to return events from in date isoformat. Defaults to today.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

    <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

    <span class="n">start_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">combine</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">min</span><span class="p">)</span>
    <span class="n">start_datetime_utc</span> <span class="o">=</span> <span class="n">start_datetime</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">Z"</span><span class="p">)</span>

    <span class="n">events_result</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span>
        <span class="o">.</span><span class="n">list</span><span class="p">(</span>
            <span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span>
            <span class="n">timeMin</span><span class="o">=</span><span class="n">start_datetime_utc</span><span class="p">,</span>
            <span class="n">maxResults</span><span class="o">=</span><span class="n">number_of_results</span><span class="p">,</span>
            <span class="n">singleEvents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">orderBy</span><span class="o">=</span><span class="s2">"startTime"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="p">)</span>

    <span class="n">events</span> <span class="o">=</span> <span class="n">events_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"items"</span><span class="p">,</span> <span class="p">[])</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">]:</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

        <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">]:</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

        <span class="n">event_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Status: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'status'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Summary: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'summary'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Start time: </span><span class="si">{</span><span class="n">start_time</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"End time: </span><span class="si">{</span><span class="n">end_time</span><span class="si">}</span><span class="s2">, "</span>

        <span class="n">organizer</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"organizer"</span><span class="p">,</span> <span class="p">{})</span>
        <span class="n">display_name</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"displayName"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
        <span class="n">email</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"email"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">display_name</span> <span class="o">!=</span> <span class="s2">"N/A"</span><span class="p">:</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">)"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">event_string</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### create\_event [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.create_event "Permanent link")

```
create_event(title: Optional[str] = None, description: Optional[str] = None, location: Optional[str] = None, start_datetime: Optional[Union[str, datetime]] = None, end_datetime: Optional[Union[str, datetime]] = None, attendees: Optional[List[str]] = None) -> str
```

```
Create an event on the users calendar.
```

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `title` | `Optional[str]` | 
The title for the event



 | `None` |
| `description` | `Optional[str]` | 

The description for the event



 | `None` |
| `location` | `Optional[str]` | 

The location for the event



 | `None` |
| `start_datetime` | `Optional[Union[str, datetime]]` | 

The start datetime for the event



 | `None` |
| `end_datetime` | `Optional[Union[str, datetime]]` | 

The end datetime for the event



 | `None` |
| `attendees` | `Optional[List[str]]` | 

A list of email address to invite to the event



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/calendar/base.py`

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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_event</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">title</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">location</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">start_datetime</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_datetime</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">attendees</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">        Create an event on the users calendar.</span>

<span class="sd">    Args:</span>
<span class="sd">        title (Optional[str]): The title for the event</span>
<span class="sd">        description (Optional[str]): The description for the event</span>
<span class="sd">        location (Optional[str]): The location for the event</span>
<span class="sd">        start_datetime Optional[Union[str, datetime.datetime]]: The start datetime for the event</span>
<span class="sd">        end_datetime Optional[Union[str, datetime.datetime]]: The end datetime for the event</span>
<span class="sd">        attendees Optional[List[str]]: A list of email address to invite to the event</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

    <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

    <span class="n">attendees_list</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[{</span><span class="s2">"email"</span><span class="p">:</span> <span class="n">attendee</span><span class="p">}</span> <span class="k">for</span> <span class="n">attendee</span> <span class="ow">in</span> <span class="n">attendees</span><span class="p">]</span> <span class="k">if</span> <span class="n">attendees</span> <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="n">start_time</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">start_datetime</span><span class="p">,</span> <span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S%z"</span><span class="p">)</span>
        <span class="o">.</span><span class="n">astimezone</span><span class="p">()</span>
        <span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">%z"</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="n">end_time</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">end_datetime</span><span class="p">,</span> <span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S%z"</span><span class="p">)</span>
        <span class="o">.</span><span class="n">astimezone</span><span class="p">()</span>
        <span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">%z"</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="n">event</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"summary"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
        <span class="s2">"location"</span><span class="p">:</span> <span class="n">location</span><span class="p">,</span>
        <span class="s2">"description"</span><span class="p">:</span> <span class="n">description</span><span class="p">,</span>
        <span class="s2">"start"</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">"dateTime"</span><span class="p">:</span> <span class="n">start_time</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">"end"</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">"dateTime"</span><span class="p">:</span> <span class="n">end_time</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">"attendees"</span><span class="p">:</span> <span class="n">attendees_list</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">event</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">event</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">(</span>
        <span class="s2">"Your calendar event has been created successfully! You can move on to the"</span>
        <span class="s2">" next step."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_date [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.get_date "Permanent link")

```
get_date()
```

A function to return todays date. Call this before any other functions if you are unaware of the date.

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/calendar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_date</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A function to return todays date. Call this before any other functions if you are unaware of the date.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

GoogleSearchToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleSearchToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Google Search tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
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
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleSearchToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Search tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"google_search"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">engine</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">key</span> <span class="o">=</span> <span class="n">key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">engine</span> <span class="o">=</span> <span class="n">engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num</span> <span class="o">=</span> <span class="n">num</span>

    <span class="k">def</span> <span class="nf">google_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a query to the Google search engine to receive a list of results.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The query to be passed to Google search.</span>
<span class="sd">            num (int, optional): The number of search results to return. Defaults to None.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: If the 'num' is not an integer between 1 and 10.</span>
<span class="sd">        """</span>
        <span class="n">url</span> <span class="o">=</span> <span class="n">QUERY_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">key</span><span class="p">,</span> <span class="n">engine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">engine</span><span class="p">,</span> <span class="n">query</span><span class="o">=</span><span class="n">urllib</span><span class="o">.</span><span class="n">parse</span><span class="o">.</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">num</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">num</span> <span class="o">&lt;=</span> <span class="mi">10</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"num should be an integer between 1 and 10, inclusive"</span><span class="p">)</span>
            <span class="n">url</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"&amp;num=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">num</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### google\_search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/#llama_index.tools.google.GoogleSearchToolSpec.google_search "Permanent link")

```
google_search(query: str)
```

Make a query to the Google search engine to receive a list of results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The query to be passed to Google search.



 | _required_ |
| `num` | `int` | 

The number of search results to return. Defaults to None.



 | _required_ |

**Raises:**

| Type | Description |
| --- | --- |
| `ValueError` | 
If the 'num' is not an integer between 1 and 10.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/search/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
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
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">google_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a query to the Google search engine to receive a list of results.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The query to be passed to Google search.</span>
<span class="sd">        num (int, optional): The number of search results to return. Defaults to None.</span>

<span class="sd">    Raises:</span>
<span class="sd">        ValueError: If the 'num' is not an integer between 1 and 10.</span>
<span class="sd">    """</span>
    <span class="n">url</span> <span class="o">=</span> <span class="n">QUERY_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
        <span class="n">key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">key</span><span class="p">,</span> <span class="n">engine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">engine</span><span class="p">,</span> <span class="n">query</span><span class="o">=</span><span class="n">urllib</span><span class="o">.</span><span class="n">parse</span><span class="o">.</span><span class="n">quote_plus</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">num</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">num</span> <span class="o">&lt;=</span> <span class="mi">10</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"num should be an integer between 1 and 10, inclusive"</span><span class="p">)</span>
        <span class="n">url</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"&amp;num=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">num</span><span class="si">}</span><span class="s2">"</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Function](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/)[Next Graphql](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/)
