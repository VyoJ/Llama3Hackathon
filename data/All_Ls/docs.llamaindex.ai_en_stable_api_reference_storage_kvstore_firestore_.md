Title: Firestore - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/

Markdown Content:
Firestore - LlamaIndex


FirestoreKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

Firestore Key-Value store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `project` | `str` | 
The project which the client acts on behalf of.



 | `None` |
| `database` | `str` | 

The database name that the client targets.



 | `DEFAULT_FIRESTORE_DATABASE` |
| `credentials` | `Credentials` | 

The OAuth2 Credentials to access Firestore. If not passed, falls back to the default inferred from the environment.



 | `None` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 25</span>
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
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FirestoreKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Firestore Key-Value store.</span>

<span class="sd">    Args:</span>
<span class="sd">        project (str): The project which the client acts on behalf of.</span>
<span class="sd">        database (str): The database name that the client targets.</span>
<span class="sd">        credentials (google.auth.credentials.Credentials): The OAuth2</span>
<span class="sd">            Credentials to access Firestore. If not passed, falls back</span>
<span class="sd">            to the default inferred from the environment.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">project</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_FIRESTORE_DATABASE</span><span class="p">,</span>
        <span class="n">credentials</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Credentials</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">client_info</span> <span class="o">=</span> <span class="n">DEFAULT_CLIENT_INFO</span>
        <span class="n">client_info</span><span class="o">.</span><span class="n">user_agent</span> <span class="o">=</span> <span class="n">USER_AGENT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span>
            <span class="n">project</span><span class="o">=</span><span class="n">project</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">client_info</span><span class="o">=</span><span class="n">client_info</span><span class="p">,</span>
            <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_db</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span>
            <span class="n">project</span><span class="o">=</span><span class="n">project</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">client_info</span><span class="o">=</span><span class="n">client_info</span><span class="p">,</span>
            <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">firestore_collection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">collection</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"/"</span><span class="p">,</span> <span class="n">SLASH_REPLACEMENT</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">replace_field_name_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">val</span> <span class="o">=</span> <span class="n">val</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">FIELD_NAME_REPLACE_SET</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">val</span><span class="p">:</span>
                <span class="n">val</span><span class="p">[</span><span class="n">v</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span><span class="p">[</span><span class="n">k</span><span class="p">]</span>
                <span class="n">val</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">val</span>

    <span class="k">def</span> <span class="nf">replace_field_name_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">val</span> <span class="o">=</span> <span class="n">val</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">FIELD_NAME_REPLACE_GET</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">val</span><span class="p">:</span>
                <span class="n">val</span><span class="p">[</span><span class="n">v</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span><span class="p">[</span><span class="n">k</span><span class="p">]</span>
                <span class="n">val</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">val</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the Firestore collection.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="n">doc</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the Firestore collection.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">put_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">batch</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">kv_pairs</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span>
            <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
            <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
            <span class="n">batch</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">),</span> <span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="n">batch_size</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">await</span> <span class="n">batch</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
                <span class="n">batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">batch</span><span class="p">()</span>
        <span class="k">await</span> <span class="n">batch</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a key-value pair from the Firestore.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a key-value pair from the Firestore.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the Firestore collection.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">list_documents</span><span class="p">()</span>
        <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">id</span>
            <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">to_dict</span><span class="p">())</span>
            <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the Firestore collection.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">list_documents</span><span class="p">()</span>
        <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">id</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">())</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
            <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the Firestore.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="n">doc</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the Firestore.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
        <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.put "Permanent link")

```
put(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the Firestore collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the Firestore collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="n">doc</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.aput "Permanent link")

```
aput(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the Firestore collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 94</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the Firestore collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.aput_all "Permanent link")

```
aput_all(kv_pairs: List[Tuple[str, dict]], collection: str = DEFAULT_COLLECTION, batch_size: int = DEFAULT_BATCH_SIZE) -> None
```

Put a dictionary of key-value pairs into the Firestore collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `kv_pairs` | `List[Tuple[str, dict]]` | 
key-value pairs



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
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
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
    <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a dictionary of key-value pairs into the Firestore collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        kv_pairs (List[Tuple[str, dict]]): key-value pairs</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">batch</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">kv_pairs</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_set</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
        <span class="n">batch</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">merge</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="n">batch_size</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">await</span> <span class="n">batch</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
            <span class="n">batch</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">batch</span><span class="p">()</span>
    <span class="k">await</span> <span class="n">batch</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.get "Permanent link")

```
get(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a key-value pair from the Firestore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">151</span>
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
<span class="normal">163</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a key-value pair from the Firestore.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.aget "Permanent link")

```
aget(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a key-value pair from the Firestore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">165</span>
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
<span class="normal">181</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a key-value pair from the Firestore.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">(</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.get_all "Permanent link")

```
get_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the Firestore collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">183</span>
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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the Firestore collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">list_documents</span><span class="p">()</span>
    <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
        <span class="n">key</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">id</span>
        <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">()</span><span class="o">.</span><span class="n">to_dict</span><span class="p">())</span>
        <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.aget_all "Permanent link")

```
aget_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the Firestore collection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

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
<span class="normal">214</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the Firestore collection.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">list_documents</span><span class="p">()</span>
    <span class="n">output</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">async</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
        <span class="n">key</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">id</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">())</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">replace_field_name_get</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
        <span class="n">output</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
    <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.delete "Permanent link")

```
delete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the Firestore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the Firestore.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="n">doc</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
    <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/#llama_index.storage.kvstore.firestore.FirestoreKVStore.adelete "Permanent link")

```
adelete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the Firestore.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-firestore/llama_index/storage/kvstore/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the Firestore.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">collection_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">firestore_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adb</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="k">await</span> <span class="n">doc</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
    <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/)
