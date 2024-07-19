Title: Redis - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/

Markdown Content:
Redis - LlamaIndex


RedisChatStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore "llama_index.core.storage.chat_store.base.BaseChatStore")`

Redis chat store.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 26</span>
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
<span class="normal">243</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RedisChatStore</span><span class="p">(</span><span class="n">BaseChatStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Redis chat store."""</span>

    <span class="n">redis_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Redis client."</span><span class="p">)</span>
    <span class="n">ttl</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Time to live in seconds."</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">redis_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"redis://localhost:6379"</span><span class="p">,</span>
        <span class="n">redis_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ttl</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="n">redis_client</span> <span class="o">=</span> <span class="n">redis_client</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_client</span><span class="p">(</span><span class="n">redis_url</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">redis_client</span><span class="o">=</span><span class="n">redis_client</span><span class="p">,</span> <span class="n">ttl</span><span class="o">=</span><span class="n">ttl</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"RedisChatStore"</span>

    <span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set messages for a key."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">add_message</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ttl</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">expire</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ttl</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get messages for a key."""</span>
        <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">lrange</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">items</span><span class="p">)</span> <span class="o"></span> <span class="mi">1</span>
        <span class="k">except</span> <span class="n">redis</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RedisError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">_redis_sentinel_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">redis_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Redis"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper method to parse an (un-official) redis+sentinel url</span>
<span class="sd">        and create a Sentinel connection to fetch the final redis client</span>
<span class="sd">        connection to a replica-master for read-write operations.</span>

<span class="sd">        If username and/or password for authentication is given the</span>
<span class="sd">        same credentials are used for the Redis Sentinel as well as Redis Server.</span>
<span class="sd">        With this implementation using a redis url only it is not possible</span>
<span class="sd">        to use different data for authentication on booth systems.</span>
<span class="sd">        """</span>
        <span class="n">parsed_url</span> <span class="o">=</span> <span class="n">urlparse</span><span class="p">(</span><span class="n">redis_url</span><span class="p">)</span>
        <span class="c1"># sentinel needs list with (host, port) tuple, use default port if none available</span>
        <span class="n">sentinel_list</span> <span class="o">=</span> <span class="p">[(</span><span class="n">parsed_url</span><span class="o">.</span><span class="n">hostname</span> <span class="ow">or</span> <span class="s2">"localhost"</span><span class="p">,</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">port</span> <span class="ow">or</span> <span class="mi">26379</span><span class="p">)]</span>
        <span class="k">if</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">path</span><span class="p">:</span>
            <span class="c1"># "/mymaster/0" first part is service name, optional second part is db number</span>
            <span class="n">path_parts</span> <span class="o">=</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)</span>
            <span class="n">service_name</span> <span class="o">=</span> <span class="n">path_parts</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">"mymaster"</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">path_parts</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="p">:</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"db"</span><span class="p">]</span> <span class="o">=</span> <span class="n">path_parts</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">service_name</span> <span class="o">=</span> <span class="s2">"mymaster"</span>

        <span class="n">sentinel_args</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">password</span><span class="p">:</span>
            <span class="n">sentinel_args</span><span class="p">[</span><span class="s2">"password"</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">password</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"password"</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">password</span>
        <span class="k">if</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">username</span><span class="p">:</span>
            <span class="n">sentinel_args</span><span class="p">[</span><span class="s2">"username"</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">username</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"username"</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed_url</span><span class="o">.</span><span class="n">username</span>

        <span class="c1"># check for all SSL related properties and copy them into sentinel_kwargs too,</span>
        <span class="c1"># add client_name also</span>
        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">arg</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"ssl"</span><span class="p">)</span> <span class="ow">or</span> <span class="n">arg</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="n">items_json</span> <span class="o">=</span> <span class="p">[</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">items</span><span class="p">]</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">_dict_to_message</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">items_json</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### add\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore.add_message "Permanent link")

```
add_message(key: str, message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage"), idx: Optional[int] = None) -> None
```

Add a message for a key.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add a message for a key."""</span>
    <span class="k">if</span> <span class="n">idx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">item</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">_message_to_dict</span><span class="p">(</span><span class="n">message</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">rpush</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">item</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_element_at_index</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">idx</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ttl</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">expire</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ttl</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore.delete_messages "Permanent link")

```
delete_messages(key: str) -> Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]]
```

Delete messages for a key.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Delete messages for a key."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### delete\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore.delete_message "Permanent link")

```
delete_message(key: str, idx: int) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete specific message for a key.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete specific message for a key."""</span>
    <span class="n">current_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">lrange</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">idx</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_list</span><span class="p">):</span>
        <span class="n">removed_item</span> <span class="o">=</span> <span class="n">current_list</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">lpush</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="o">*</span><span class="n">current_list</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">removed_item</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### delete\_last\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore.delete_last_message "Permanent link")

```
delete_last_message(key: str) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete last message for a key.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete last message for a key."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">rpop</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_keys [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/#llama_index.storage.chat_store.redis.RedisChatStore.get_keys "Permanent link")

```
get_keys() -> List[str]
```

Get all keys.

Source code in `llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-redis/llama_index/storage/chat_store/redis/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all keys."""</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">key</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">redis_client</span><span class="o">.</span><span class="n">keys</span><span class="p">(</span><span class="s2">"*"</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/)[Next Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/)
