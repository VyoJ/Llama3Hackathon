Title: Neo4j - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/

Markdown Content:
Neo4j - LlamaIndex


Neo4jGraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[GraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "llama_index.core.graph_stores.types.GraphStore")`

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

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
<span class="normal">255</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jGraphStore</span><span class="p">(</span><span class="n">GraphStore</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"neo4j"</span><span class="p">,</span>
        <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Entity"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span> <span class="o">=</span> <span class="n">node_label</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="c1"># Verify connection</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="k">as</span> <span class="n">driver</span><span class="p">:</span>
                <span class="n">driver</span><span class="o">.</span><span class="n">verify_connectivity</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ServiceUnavailable</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the url is correct"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">AuthError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the username and password are correct"</span>
            <span class="p">)</span>
        <span class="c1"># Set schema</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not use APOC procedures. "</span>
                <span class="s2">"Please ensure the APOC plugin is installed in Neo4j and that "</span>
                <span class="s2">"'apoc.meta.data()' is allowed in Neo4j configuration "</span>
            <span class="p">)</span>
        <span class="c1"># Create constraint for faster insert and retrieval</span>
        <span class="k">try</span><span class="p">:</span>  <span class="c1"># Using Neo4j 5</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                CREATE CONSTRAINT IF NOT EXISTS FOR (n:%s) REQUIRE n.id IS UNIQUE;</span>
<span class="sd">                """</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>  <span class="c1"># Using Neo4j &lt;5</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                CREATE CONSTRAINT IF NOT EXISTS ON (n:%s) ASSERT n.id IS UNIQUE;</span>
<span class="sd">                """</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>
            <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get triplets."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">            MATCH (n1:</span><span class="si">%s</span><span class="s2">)-[r]-&gt;(n2:</span><span class="si">%s</span><span class="s2">)</span>
<span class="s2">            WHERE n1.id = $subj</span>
<span class="s2">            RETURN type(r), n2.id;</span>
<span class="s2">        """</span>

        <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">})</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">record</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">subjs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Get flat rel map."""</span>
        <span class="c1"># The flat means for multi-hop relation path, we could get</span>
        <span class="c1"># knowledge like: subj -&gt; rel -&gt; obj -&gt; rel -&gt; obj -&gt; rel -&gt; obj.</span>
        <span class="c1"># This type of knowledge is useful for some tasks.</span>
        <span class="c1"># +-------------+------------------------------------+</span>
        <span class="c1"># | subj        | flattened_rels                     |</span>
        <span class="c1"># +-------------+------------------------------------+</span>
        <span class="c1"># | "player101" | [95, "player125", 2002, "team204"] |</span>
        <span class="c1"># | "player100" | [1997, "team204"]                  |</span>
        <span class="c1"># ...</span>
        <span class="c1"># +-------------+------------------------------------+</span>

        <span class="n">rel_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">subjs</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">subjs</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
        <span class="c1"># unlike simple graph_store, we don't do get_all here</span>
        <span class="k">return</span> <span class="n">rel_map</span>

    <span class="n">query</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""MATCH p=(n1:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">)-[*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-&gt;() """</span>
        <span class="sa">f</span><span class="s2">"""WHERE toLower(n1.id) IN </span><span class="si">{</span><span class="p">[</span><span class="n">subj</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">subj</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">subjs</span><span class="p">]</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">subjs</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">[]</span><span class="si">}</span><span class="s2">"""</span>
        <span class="s2">"UNWIND relationships(p) AS rel "</span>
        <span class="s2">"WITH n1.id AS subj, p, apoc.coll.flatten(apoc.coll.toSet("</span>
        <span class="s2">"collect([type(rel), endNode(rel).id]))) AS flattened_rels "</span>
        <span class="sa">f</span><span class="s2">"RETURN subj, collect(flattened_rels) AS flattened_rels LIMIT </span><span class="si">{</span><span class="n">limit</span><span class="si">}</span><span class="s2">"</span>
    <span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subjs"</span><span class="p">:</span> <span class="n">subjs</span><span class="p">}))</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">rel_map</span>

    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="n">rel_map</span><span class="p">[</span><span class="n">record</span><span class="p">[</span><span class="s2">"subj"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"flattened_rels"</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">rel_map</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_triplet [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.upsert_triplet "Permanent link")

```
upsert_triplet(subj: str, rel: str, obj: str) -> None
```

Add triplet.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
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
<span class="normal">161</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add triplet."""</span>
    <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        MERGE (n1:`</span><span class="si">%s</span><span class="s2">` {id:$subj})</span>
<span class="s2">        MERGE (n2:`</span><span class="si">%s</span><span class="s2">` {id:$obj})</span>
<span class="s2">        MERGE (n1)-[:`</span><span class="si">%s</span><span class="s2">`]-&gt;(n2)</span>
<span class="s2">    """</span>

    <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
        <span class="n">rel</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">" "</span><span class="p">,</span> <span class="s2">"_"</span><span class="p">)</span><span class="o">.</span><span class="n">upper</span><span class="p">(),</span>
    <span class="p">)</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.delete "Permanent link")

```
delete(subj: str, rel: str, obj: str) -> None
```

Delete triplet.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">163</span>
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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete triplet."""</span>

    <span class="k">def</span> <span class="nf">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="s2">"MATCH (n1:</span><span class="si">{}</span><span class="s2">)-[r:</span><span class="si">{}</span><span class="s2">]-&gt;(n2:</span><span class="si">{}</span><span class="s2">) WHERE n1.id = $subj AND n2.id"</span>
                    <span class="s2">" = $obj DELETE r"</span>
                <span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="s2">"MATCH (n:</span><span class="si">%s</span><span class="s2">) WHERE n.id = $entity DELETE n"</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
                <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">check_edges</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">is_exists_result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="s2">"MATCH (n1:</span><span class="si">%s</span><span class="s2">)--() WHERE n1.id = $entity RETURN count(*)"</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">is_exists_result</span><span class="p">))</span>

    <span class="n">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">rel</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">subj</span><span class="p">):</span>
        <span class="n">delete_entity</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
        <span class="n">delete_entity</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### refresh\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.refresh_schema "Permanent link")

```
refresh_schema() -> None
```

Refreshes the Neo4j graph schema information.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Refreshes the Neo4j graph schema information.</span>
<span class="sd">    """</span>
    <span class="n">node_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">node_properties_query</span><span class="p">)]</span>
    <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_properties_query</span><span class="p">)]</span>
    <span class="n">relationships</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_query</span><span class="p">)]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
        <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
        <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="c1"># Format node properties</span>
    <span class="n">formatted_node_props</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">:</span>
        <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
        <span class="p">)</span>
        <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'labels'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># Format relationship properties</span>
    <span class="n">formatted_rel_props</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">:</span>
        <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
        <span class="p">)</span>
        <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># Format relationships</span>
    <span class="n">formatted_rels</span> <span class="o">=</span> <span class="p">[</span>
        <span class="sa">f</span><span class="s2">"(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'start'</span><span class="p">]</span><span class="si">}</span><span class="s2">)-[:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">]-&gt;(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">relationships</span>
    <span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
        <span class="p">[</span>
            <span class="s2">"Node properties are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_node_props</span><span class="p">),</span>
            <span class="s2">"Relationship properties are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rel_props</span><span class="p">),</span>
            <span class="s2">"The relationships are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rels</span><span class="p">),</span>
        <span class="p">]</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_schema "Permanent link")

```
get_schema(refresh: bool = False) -> str
```

Get the schema of the Neo4jGraph store.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the schema of the Neo4jGraph store."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">refresh</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"get_schema() schema:</span><span class="se">\n</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>
</code></pre></div></td></tr></tbody></table>

Neo4jPropertyGraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PropertyGraphStore`

Neo4j Property Graph Store.

This class implements a Neo4j property graph store.

If you are using local Neo4j instead of aura, here's a helpful command for launching the docker container:

```
dockerrun\
-p7474:7474-p7687:7687\
-v$PWD/data:/data-v$PWD/plugins:/plugins\
--nameneo4j-apoc\
-eNEO4J_apoc_export_file_enabled=true\
-eNEO4J_apoc_import_file_enabled=true\
-eNEO4J_apoc_import_file_use__neo4j__config=true\
-eNEO4JLABS_PLUGINS=\\[\"apoc\"\\]\
neo4j:latest
```

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `username` | `str` | 
The username for the Neo4j database.



 | _required_ |
| `password` | `str` | 

The password for the Neo4j database.



 | _required_ |
| `url` | `str` | 

The URL for the Neo4j database.



 | _required_ |
| `database` | `Optional[str]` | 

The name of the database to connect to. Defaults to "neo4j".



 | `'neo4j'` |

**Examples:**

`pip install llama-index-graph-stores-neo4j`

```
from llama_index.core.indices.property_graph import PropertyGraphIndex
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

# Create a Neo4jPropertyGraphStore instance
graph_store = Neo4jPropertyGraphStore(
    username="neo4j",
    password="neo4j",
    url="bolt://localhost:7687",
    database="neo4j"
)

# create the index
index = PropertyGraphIndex.from_documents(
    documents,
    property_graph_store=graph_store,
)
```

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 73</span>
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
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span>
<span class="normal">819</span>
<span class="normal">820</span>
<span class="normal">821</span>
<span class="normal">822</span>
<span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span>
<span class="normal">842</span>
<span class="normal">843</span>
<span class="normal">844</span>
<span class="normal">845</span>
<span class="normal">846</span>
<span class="normal">847</span>
<span class="normal">848</span>
<span class="normal">849</span>
<span class="normal">850</span>
<span class="normal">851</span>
<span class="normal">852</span>
<span class="normal">853</span>
<span class="normal">854</span>
<span class="normal">855</span>
<span class="normal">856</span>
<span class="normal">857</span>
<span class="normal">858</span>
<span class="normal">859</span>
<span class="normal">860</span>
<span class="normal">861</span>
<span class="normal">862</span>
<span class="normal">863</span>
<span class="normal">864</span>
<span class="normal">865</span>
<span class="normal">866</span>
<span class="normal">867</span>
<span class="normal">868</span>
<span class="normal">869</span>
<span class="normal">870</span>
<span class="normal">871</span>
<span class="normal">872</span>
<span class="normal">873</span>
<span class="normal">874</span>
<span class="normal">875</span>
<span class="normal">876</span>
<span class="normal">877</span>
<span class="normal">878</span>
<span class="normal">879</span>
<span class="normal">880</span>
<span class="normal">881</span>
<span class="normal">882</span>
<span class="normal">883</span>
<span class="normal">884</span>
<span class="normal">885</span>
<span class="normal">886</span>
<span class="normal">887</span>
<span class="normal">888</span>
<span class="normal">889</span>
<span class="normal">890</span>
<span class="normal">891</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jPropertyGraphStore</span><span class="p">(</span><span class="n">PropertyGraphStore</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""</span>
<span class="sd">    Neo4j Property Graph Store.</span>

<span class="sd">    This class implements a Neo4j property graph store.</span>

<span class="sd">    If you are using local Neo4j instead of aura, here's a helpful</span>
<span class="sd">    command for launching the docker container:</span>

<span class="sd">    ```bash</span>
<span class="sd">    docker run \</span>
<span class="sd">        -p 7474:7474 -p 7687:7687 \</span>
<span class="sd">        -v $PWD/data:/data -v $PWD/plugins:/plugins \</span>
<span class="sd">        --name neo4j-apoc \</span>
<span class="sd">        -e NEO4J_apoc_export_file_enabled=true \</span>
<span class="sd">        -e NEO4J_apoc_import_file_enabled=true \</span>
<span class="sd">        -e NEO4J_apoc_import_file_use__neo4j__config=true \</span>
<span class="sd">        -e NEO4JLABS_PLUGINS=\\[\"apoc\"\\] \</span>
<span class="sd">        neo4j:latest</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        username (str): The username for the Neo4j database.</span>
<span class="sd">        password (str): The password for the Neo4j database.</span>
<span class="sd">        url (str): The URL for the Neo4j database.</span>
<span class="sd">        database (Optional[str]): The name of the database to connect to. Defaults to "neo4j".</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-graph-stores-neo4j`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.core.indices.property_graph import PropertyGraphIndex</span>
<span class="sd">        from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore</span>

<span class="sd">        # Create a Neo4jPropertyGraphStore instance</span>
<span class="sd">        graph_store = Neo4jPropertyGraphStore(</span>
<span class="sd">            username="neo4j",</span>
<span class="sd">            password="neo4j",</span>
<span class="sd">            url="bolt://localhost:7687",</span>
<span class="sd">            database="neo4j"</span>
<span class="sd">        )</span>

<span class="sd">        # create the index</span>
<span class="sd">        index = PropertyGraphIndex.from_documents(</span>
<span class="sd">            documents,</span>
<span class="sd">            property_graph_store=graph_store,</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">supports_structured_queries</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">supports_vector_queries</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">text_to_cypher_template</span><span class="p">:</span> <span class="n">PromptTemplate</span> <span class="o">=</span> <span class="n">DEFAULT_CYPHER_TEMPALTE</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"neo4j"</span><span class="p">,</span>
        <span class="n">refresh_schema</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">sanitize_query_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">enhanced_schema</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">neo4j_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_query_output</span> <span class="o">=</span> <span class="n">sanitize_query_output</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">enhanced_schema</span> <span class="o">=</span> <span class="n">enhanced_schema</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span>
            <span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">),</span> <span class="o">**</span><span class="n">neo4j_kwargs</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">AsyncGraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span>
            <span class="n">url</span><span class="p">,</span>
            <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">),</span>
            <span class="o">**</span><span class="n">neo4j_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">refresh_schema</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span>

    <span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Refresh the schema."""</span>
        <span class="n">node_query_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">node_properties_query</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
        <span class="p">)</span>
        <span class="n">node_properties</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_query_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">node_query_results</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="n">rels_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">rel_properties_query</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="n">EXCLUDED_RELS</span><span class="p">}</span>
        <span class="p">)</span>
        <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rels_query_result</span><span class="p">]</span> <span class="k">if</span> <span class="n">rels_query_result</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="n">rel_objs_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">rel_query</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
        <span class="p">)</span>
        <span class="n">relationships</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_objs_query_result</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">rel_objs_query_result</span>
            <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="c1"># Get constraints &amp; indexes</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">constraint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="s2">"SHOW CONSTRAINTS"</span><span class="p">)</span>
            <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
                <span class="s2">"CALL apoc.schema.nodes() YIELD label, properties, type, size, "</span>
                <span class="s2">"valuesSelectivity WHERE type = 'RANGE' RETURN *, "</span>
                <span class="s2">"size * valuesSelectivity as distinctValues"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="p">(</span>
            <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span>
        <span class="p">):</span>  <span class="c1"># Read-only user might not have access to schema information</span>
            <span class="n">constraint</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">index</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
            <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
            <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
            <span class="s2">"metadata"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"constraint"</span><span class="p">:</span> <span class="n">constraint</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="n">index</span><span class="p">},</span>
        <span class="p">}</span>
        <span class="n">schema_counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"CALL apoc.meta.graphSample() YIELD nodes, relationships "</span>
            <span class="s2">"RETURN nodes, [rel in relationships | {name:apoc.any.property"</span>
            <span class="s2">"(rel, 'type'), count: apoc.any.property(rel, 'count')}]"</span>
            <span class="s2">" AS relationships"</span>
        <span class="p">)</span>
        <span class="c1"># Update node info</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="c1"># Skip bloom labels</span>
            <span class="k">if</span> <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_LABELS</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">node_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">node_props</span><span class="p">:</span>  <span class="c1"># The node has no properties</span>
                <span class="k">continue</span>
            <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
                <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">node_props</span><span class="p">,</span> <span class="n">node</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span>
            <span class="p">)</span>
            <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">node_props</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                    <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
        <span class="c1"># Update rel info</span>
        <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="c1"># Skip bloom labels</span>
            <span class="k">if</span> <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_RELS</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">rel_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_props</span><span class="p">:</span>  <span class="c1"># The rel has no properties</span>
                <span class="k">continue</span>
            <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
                <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                <span class="n">rel_props</span><span class="p">,</span>
                <span class="n">rel</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span><span class="p">,</span>
                <span class="n">is_relationship</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">rel_props</span><span class="p">:</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                        <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
            <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
                <span class="c1"># Sometimes the types are not consistent in the db</span>
                <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">upsert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Lists to hold separated types</span>
        <span class="n">entity_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">chunk_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># Sort by type</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">EntityNode</span><span class="p">):</span>
                <span class="n">entity_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="o">**</span><span class="n">item</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">id</span><span class="p">})</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">ChunkNode</span><span class="p">):</span>
                <span class="n">chunk_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="o">**</span><span class="n">item</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">id</span><span class="p">})</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Log that we do not support these types of nodes</span>
                <span class="c1"># Or raise an error?</span>
                <span class="k">pass</span>

        <span class="k">if</span> <span class="n">chunk_dicts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                UNWIND $data AS row</span>
<span class="sd">                MERGE (c:Chunk {id: row.id})</span>
<span class="sd">                SET c.text = row.text</span>
<span class="sd">                WITH c, row</span>
<span class="sd">                SET c += row.properties</span>
<span class="sd">                WITH c, row.embedding AS embedding</span>
<span class="sd">                WHERE embedding IS NOT NULL</span>
<span class="sd">                CALL db.create.setNodeVectorProperty(c, 'embedding', embedding)</span>
<span class="sd">                RETURN count(*)</span>
<span class="sd">                """</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">chunk_dicts</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">entity_dicts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                UNWIND $data AS row</span>
<span class="sd">                MERGE (e:`__Entity__` {id: row.id})</span>
<span class="sd">                SET e += apoc.map.clean(row.properties, [], [])</span>
<span class="sd">                SET e.name = row.name</span>
<span class="sd">                WITH e, row</span>
<span class="sd">                CALL apoc.create.addLabels(e, [row.label])</span>
<span class="sd">                YIELD node</span>
<span class="sd">                WITH e, row</span>
<span class="sd">                CALL {</span>
<span class="sd">                    WITH e, row</span>
<span class="sd">                    WITH e, row</span>
<span class="sd">                    WHERE row.embedding IS NOT NULL</span>
<span class="sd">                    CALL db.create.setNodeVectorProperty(e, 'embedding', row.embedding)</span>
<span class="sd">                    RETURN count(*) AS count</span>
<span class="sd">                }</span>
<span class="sd">                WITH e, row WHERE row.properties.triplet_source_id IS NOT NULL</span>
<span class="sd">                MERGE (c:Chunk {id: row.properties.triplet_source_id})</span>
<span class="sd">                MERGE (e)&lt;-[:MENTIONS]-(c)</span>
<span class="sd">                """</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">entity_dicts</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">upsert_relations</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">relations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Relation</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add relations."""</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">relations</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">            </span><span class="sd">"""</span>
<span class="sd">            UNWIND $data AS row</span>
<span class="sd">            MERGE (source {id: row.source_id})</span>
<span class="sd">            ON CREATE SET source:Chunk</span>
<span class="sd">            MERGE (target {id: row.target_id})</span>
<span class="sd">            ON CREATE SET target:Chunk</span>
<span class="sd">            WITH source, target, row</span>
<span class="sd">            CALL apoc.merge.relationship(source, row.label, {}, row.properties, target) YIELD rel</span>
<span class="sd">            RETURN count(*)</span>
<span class="sd">            """</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">params</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes."""</span>
        <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e) "</span>

        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

        <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

        <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
            <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
                <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

        <span class="n">return_statement</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        WITH e</span>
<span class="s2">        RETURN e.id AS name,</span>
<span class="s2">               [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">               e{.* , embedding: Null, id: Null} AS properties</span>
<span class="s2">        """</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="c1"># text indicates a chunk node</span>
            <span class="c1"># none on the type indicates an implicit node, likely a chunk node</span>
            <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">in</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="ow">or</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">ChunkNode</span><span class="p">(</span>
                        <span class="n">id_</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">EntityNode</span><span class="p">(</span>
                        <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                        <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                        <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">get_triplets</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">entity_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">relation_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
        <span class="c1"># TODO: handle ids of chunk nodes</span>
        <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e:`__Entity__`) "</span>

        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">entity_names</span> <span class="ow">or</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

        <span class="k">if</span> <span class="n">entity_names</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.name in $entity_names "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"entity_names"</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_names</span>

        <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

        <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
            <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
                <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

        <span class="n">return_statement</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        WITH e</span>
<span class="s2">        CALL </span><span class="se">{{</span>
<span class="s2">            WITH e</span>
<span class="s2">            MATCH (e)-[r</span><span class="si">{</span><span class="s1">':`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`|`'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">relation_names</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">relation_names</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s1">''</span><span class="si">}</span><span class="s2">]-&gt;(t)</span>
<span class="s2">            RETURN e.name AS source_id, [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                   e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                   type(r) AS type,</span>
<span class="s2">                   t.name AS target_id, [l in labels(t) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                   t</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS target_properties</span>
<span class="s2">            UNION ALL</span>
<span class="s2">            WITH e</span>
<span class="s2">            MATCH (e)&lt;-[r</span><span class="si">{</span><span class="s1">':`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`|`'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">relation_names</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">relation_names</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s1">''</span><span class="si">}</span><span class="s2">]-(t)</span>
<span class="s2">            RETURN t.name AS source_id, [l in labels(t) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                   e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                   type(r) AS type,</span>
<span class="s2">                   e.name AS target_id, [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                   t</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS target_properties</span>
<span class="s2">        </span><span class="se">}}</span>
<span class="s2">        RETURN source_id, source_type, type, target_id, target_type, source_properties, target_properties"""</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="k">if</span> <span class="n">data</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
                <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">triples</span>

    <span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">graph_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span>
        <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>
        <span class="n">ignore_rels</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get depth-aware rel map."""</span>
        <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_nodes</span><span class="p">]</span>
        <span class="c1"># Needs some optimization</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            WITH $ids AS id_list</span>
<span class="s2">            UNWIND range(0, size(id_list) - 1) AS idx</span>
<span class="s2">            MATCH (e:`__Entity__`)</span>
<span class="s2">            WHERE e.id = id_list[idx]</span>
<span class="s2">            MATCH p=(e)-[r*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-(other)</span>
<span class="s2">            WHERE ALL(rel in relationships(p) WHERE type(rel) &lt;&gt; 'MENTIONS')</span>
<span class="s2">            UNWIND relationships(p) AS rel</span>
<span class="s2">            WITH distinct rel, idx</span>
<span class="s2">            WITH startNode(rel) AS source,</span>
<span class="s2">                type(rel) AS type,</span>
<span class="s2">                endNode(rel) AS endNode,</span>
<span class="s2">                idx</span>
<span class="s2">            LIMIT toInteger($limit)</span>
<span class="s2">            RETURN source.id AS source_id, [l in labels(source) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                source</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                type,</span>
<span class="s2">                endNode.id AS target_id, [l in labels(endNode) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                endNode</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS target_properties,</span>
<span class="s2">                idx</span>
<span class="s2">            ORDER BY idx</span>
<span class="s2">            LIMIT toInteger($limit)</span>
<span class="s2">            """</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">,</span> <span class="s2">"limit"</span><span class="p">:</span> <span class="n">limit</span><span class="p">},</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">ignore_rels</span> <span class="o">=</span> <span class="n">ignore_rels</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">ignore_rels</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
                <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">triples</span>

    <span class="k">def</span> <span class="nf">structured_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">param_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="n">param_map</span> <span class="o">=</span> <span class="n">param_map</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">param_map</span><span class="p">)</span>
            <span class="n">full_result</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">data</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">result</span><span class="p">]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_query_output</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">value_sanitize</span><span class="p">(</span><span class="n">full_result</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">full_result</span>

    <span class="k">def</span> <span class="nf">vector_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Query the graph store with a vector store query."""</span>
        <span class="n">conditions</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="n">conditions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="sa">f</span><span class="s2">"e.</span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">operator</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>
                <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">filters</span>
            <span class="p">]</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">conditions</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span> <span class="s2">"STRING"</span><span class="p">:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"collect(distinct substring(toString(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`), 0, 50)) "</span>
                        <span class="sa">f</span><span class="s2">"AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"values:`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`[..</span><span class="si">{</span><span class="n">DISTINCT_VALUE_LIMIT</span><span class="si">}</span><span class="s2">],"</span>
                        <span class="sa">f</span><span class="s2">" distinct_count: size(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`)"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span>
                    <span class="s2">"INTEGER"</span><span class="p">,</span>
                    <span class="s2">"FLOAT"</span><span class="p">,</span>
                    <span class="s2">"DATE"</span><span class="p">,</span>
                    <span class="s2">"DATE_TIME"</span><span class="p">,</span>
                    <span class="s2">"LOCAL_DATE_TIME"</span><span class="p">,</span>
                <span class="p">]:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"min(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`"</span><span class="p">)</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"max(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`"</span><span class="p">)</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"count(distinct n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`), "</span>
                        <span class="sa">f</span><span class="s2">"max: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`), "</span>
                        <span class="sa">f</span><span class="s2">"distinct_count: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="o"></span> <span class="n">label_or_type</span>
                    <span class="ow">and</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"RANGE"</span>
                <span class="p">]</span>
                <span class="k">if</span> <span class="n">prop_type</span> <span class="o"></span> <span class="s2">"LIST"</span><span class="p">:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"BOOLEAN"</span><span class="p">,</span> <span class="s2">"POINT"</span><span class="p">,</span> <span class="s2">"DURATION"</span><span class="p">]:</span>
                    <span class="k">continue</span>

                <span class="n">output_dict</span><span class="p">[</span><span class="n">prop_name</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"{"</span> <span class="o">+</span> <span class="n">return_clauses</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span> <span class="o">+</span> <span class="s2">"}"</span>

        <span class="n">with_clause</span> <span class="o">=</span> <span class="s2">"WITH "</span> <span class="o">+</span> <span class="s2">",</span><span class="se">\n</span><span class="s2">     "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">with_clauses</span><span class="p">)</span>
        <span class="n">return_clause</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"RETURN {"</span>
            <span class="o">+</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s2">"`</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">`: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">output_dict</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
            <span class="o">+</span> <span class="s2">"} AS output"</span>
        <span class="p">)</span>

        <span class="c1"># Combine all parts of the Cypher query</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">match_clause</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">with_clause</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">return_clause</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">refresh</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span>

    <span class="k">def</span> <span class="nf">get_schema_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">schema</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_schema</span><span class="p">(</span><span class="n">refresh</span><span class="o">=</span><span class="n">refresh</span><span class="p">)</span>

        <span class="n">formatted_node_props</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">formatted_rel_props</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enhanced_schema</span><span class="p">:</span>
            <span class="c1"># Enhanced formatting for nodes</span>
            <span class="k">for</span> <span class="n">node_type</span><span class="p">,</span> <span class="n">properties</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"- **</span><span class="si">{</span><span class="n">node_type</span><span class="si">}</span><span class="s2">**"</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                    <span class="n">example</span> <span class="o">=</span> <span class="s2">""</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"LIST"</span><span class="p">:</span>
                        <span class="c1"># Skip embeddings</span>
                        <span class="k">if</span> <span class="ow">not</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"min_size"</span><span class="p">)</span> <span class="ow">or</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">LIST_LIMIT</span><span class="p">:</span>
                            <span class="k">continue</span>
                        <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                    <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"  - `</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">`: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">example</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>

            <span class="c1"># Enhanced formatting for relationships</span>
            <span class="k">for</span> <span class="n">rel_type</span><span class="p">,</span> <span class="n">properties</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"- **</span><span class="si">{</span><span class="n">rel_type</span><span class="si">}</span><span class="s2">**"</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                    <span class="n">example</span> <span class="o">=</span> <span class="s2">""</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"LIST"</span><span class="p">:</span>
                        <span class="c1"># Skip embeddings</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">LIST_LIMIT</span><span class="p">:</span>
                            <span class="k">continue</span>
                        <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                    <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"  - `</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">` </span><span class="si">{</span><span class="n">example</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Format node properties</span>
            <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">props</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">props</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">label</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

            <span class="c1"># Format relationship properties using structured_schema</span>
            <span class="k">for</span> <span class="nb">type</span><span class="p">,</span> <span class="n">props</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">props</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="nb">type</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Format relationships</span>
        <span class="n">formatted_rels</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'start'</span><span class="p">]</span><span class="si">}</span><span class="s2">)-[:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">]-&gt;(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span>
            <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"relationships"</span><span class="p">]</span>
        <span class="p">]</span>

        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="s2">"Node properties:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_node_props</span><span class="p">),</span>
                <span class="s2">"Relationship properties:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rel_props</span><span class="p">),</span>
                <span class="s2">"The relationships:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rels</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### refresh\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.refresh_schema "Permanent link")

```
refresh_schema() -> None
```

Refresh the schema.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
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
<span class="normal">246</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Refresh the schema."""</span>
    <span class="n">node_query_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">node_properties_query</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
    <span class="p">)</span>
    <span class="n">node_properties</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_query_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">node_query_results</span> <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="n">rels_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">rel_properties_query</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="n">EXCLUDED_RELS</span><span class="p">}</span>
    <span class="p">)</span>
    <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rels_query_result</span><span class="p">]</span> <span class="k">if</span> <span class="n">rels_query_result</span> <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="n">rel_objs_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">rel_query</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
    <span class="p">)</span>
    <span class="n">relationships</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_objs_query_result</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">rel_objs_query_result</span>
        <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="c1"># Get constraints &amp; indexes</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">constraint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="s2">"SHOW CONSTRAINTS"</span><span class="p">)</span>
        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"CALL apoc.schema.nodes() YIELD label, properties, type, size, "</span>
            <span class="s2">"valuesSelectivity WHERE type = 'RANGE' RETURN *, "</span>
            <span class="s2">"size * valuesSelectivity as distinctValues"</span>
        <span class="p">)</span>
    <span class="k">except</span> <span class="p">(</span>
        <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span>
    <span class="p">):</span>  <span class="c1"># Read-only user might not have access to schema information</span>
        <span class="n">constraint</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">index</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
        <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
        <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
        <span class="s2">"metadata"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"constraint"</span><span class="p">:</span> <span class="n">constraint</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="n">index</span><span class="p">},</span>
    <span class="p">}</span>
    <span class="n">schema_counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="s2">"CALL apoc.meta.graphSample() YIELD nodes, relationships "</span>
        <span class="s2">"RETURN nodes, [rel in relationships | {name:apoc.any.property"</span>
        <span class="s2">"(rel, 'type'), count: apoc.any.property(rel, 'count')}]"</span>
        <span class="s2">" AS relationships"</span>
    <span class="p">)</span>
    <span class="c1"># Update node info</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[]):</span>
        <span class="c1"># Skip bloom labels</span>
        <span class="k">if</span> <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_LABELS</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">node_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">node_props</span><span class="p">:</span>  <span class="c1"># The node has no properties</span>
            <span class="k">continue</span>
        <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
            <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">node_props</span><span class="p">,</span> <span class="n">node</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span>
        <span class="p">)</span>
        <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">node_props</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
    <span class="c1"># Update rel info</span>
    <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">,</span> <span class="p">[]):</span>
        <span class="c1"># Skip bloom labels</span>
        <span class="k">if</span> <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_RELS</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">rel_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_props</span><span class="p">:</span>  <span class="c1"># The rel has no properties</span>
            <span class="k">continue</span>
        <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
            <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
            <span class="n">rel_props</span><span class="p">,</span>
            <span class="n">rel</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span><span class="p">,</span>
            <span class="n">is_relationship</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">rel_props</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                    <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
            <span class="c1"># Sometimes the types are not consistent in the db</span>
            <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_relations [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.upsert_relations "Permanent link")

```
upsert_relations(relations: List[Relation]) -> None
```

Add relations.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">305</span>
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
<span class="normal">321</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_relations</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">relations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Relation</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add relations."""</span>
    <span class="n">params</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">relations</span><span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        UNWIND $data AS row</span>
<span class="sd">        MERGE (source {id: row.source_id})</span>
<span class="sd">        ON CREATE SET source:Chunk</span>
<span class="sd">        MERGE (target {id: row.target_id})</span>
<span class="sd">        ON CREATE SET target:Chunk</span>
<span class="sd">        WITH source, target, row</span>
<span class="sd">        CALL apoc.merge.relationship(source, row.label, {}, row.properties, target) YIELD rel</span>
<span class="sd">        RETURN count(*)</span>
<span class="sd">        """</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">params</span><span class="p">},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get "Permanent link")

```
get(properties: Optional[dict] = None, ids: Optional[List[str]] = None) -> List[LabelledNode]
```

Get nodes.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">323</span>
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
<span class="normal">379</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes."""</span>
    <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e) "</span>

    <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

    <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
        <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

    <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
        <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
            <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

    <span class="n">return_statement</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    WITH e</span>
<span class="s2">    RETURN e.id AS name,</span>
<span class="s2">           [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">           e{.* , embedding: Null, id: Null} AS properties</span>
<span class="s2">    """</span>
    <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="c1"># text indicates a chunk node</span>
        <span class="c1"># none on the type indicates an implicit node, likely a chunk node</span>
        <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">in</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="ow">or</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">ChunkNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">EntityNode</span><span class="p">(</span>
                    <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                    <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                    <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### get\_rel\_map [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get_rel_map "Permanent link")

```
get_rel_map(graph_nodes: List[LabelledNode], depth: int = 2, limit: int = 30, ignore_rels: Optional[List[str]] = None) -> List[Triplet]
```

Get depth-aware rel map.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">graph_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span>
    <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>
    <span class="n">ignore_rels</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get depth-aware rel map."""</span>
    <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_nodes</span><span class="p">]</span>
    <span class="c1"># Needs some optimization</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        WITH $ids AS id_list</span>
<span class="s2">        UNWIND range(0, size(id_list) - 1) AS idx</span>
<span class="s2">        MATCH (e:`__Entity__`)</span>
<span class="s2">        WHERE e.id = id_list[idx]</span>
<span class="s2">        MATCH p=(e)-[r*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-(other)</span>
<span class="s2">        WHERE ALL(rel in relationships(p) WHERE type(rel) &lt;&gt; 'MENTIONS')</span>
<span class="s2">        UNWIND relationships(p) AS rel</span>
<span class="s2">        WITH distinct rel, idx</span>
<span class="s2">        WITH startNode(rel) AS source,</span>
<span class="s2">            type(rel) AS type,</span>
<span class="s2">            endNode(rel) AS endNode,</span>
<span class="s2">            idx</span>
<span class="s2">        LIMIT toInteger($limit)</span>
<span class="s2">        RETURN source.id AS source_id, [l in labels(source) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">            source</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">            type,</span>
<span class="s2">            endNode.id AS target_id, [l in labels(endNode) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">            endNode</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS target_properties,</span>
<span class="s2">            idx</span>
<span class="s2">        ORDER BY idx</span>
<span class="s2">        LIMIT toInteger($limit)</span>
<span class="s2">        """</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">,</span> <span class="s2">"limit"</span><span class="p">:</span> <span class="n">limit</span><span class="p">},</span>
    <span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">ignore_rels</span> <span class="o">=</span> <span class="n">ignore_rels</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">ignore_rels</span><span class="p">:</span>
            <span class="k">continue</span>

        <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
            <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
            <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>

    <span class="k">return</span> <span class="n">triples</span>
</code></pre></div></td></tr></tbody></table>

### vector\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.vector_query "Permanent link")

```
vector_query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> Tuple[List[LabelledNode], List[float]]
```

Query the graph store with a vector store query.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">vector_query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Query the graph store with a vector store query."""</span>
    <span class="n">conditions</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
        <span class="n">conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"e.</span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">operator</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">filters</span>
        <span class="p">]</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">conditions</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"=="</span><span class="p">,</span> <span class="s2">"="</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">conditions</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="k">else</span> <span class="s2">"1 = 1"</span>
    <span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""MATCH (e:`__Entity__`)</span>
<span class="s2">        WHERE e.embedding IS NOT NULL AND size(e.embedding) = $dimension AND (</span><span class="si">{</span><span class="n">filters</span><span class="si">}</span><span class="s2">)</span>
<span class="s2">        WITH e, vector.similarity.cosine(e.embedding, $embedding) AS score</span>
<span class="s2">        ORDER BY score DESC LIMIT toInteger($limit)</span>
<span class="s2">        RETURN e.id AS name,</span>
<span class="s2">           [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">           e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS properties,</span>
<span class="s2">           score"""</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="s2">"dimension"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">),</span>
            <span class="s2">"limit"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="k">if</span> <span class="n">data</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>

    <span class="k">return</span> <span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.delete "Permanent link")

```
delete(entity_names: Optional[List[str]] = None, relation_names: Optional[List[str]] = None, properties: Optional[dict] = None, ids: Optional[List[str]] = None) -> None
```

Delete matching data.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">entity_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">relation_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete matching data."""</span>
    <span class="k">if</span> <span class="n">entity_names</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"MATCH (n) WHERE n.name IN $entity_names DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"entity_names"</span><span class="p">:</span> <span class="n">entity_names</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"MATCH (n) WHERE n.id IN $ids DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">relation_names</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">relation_names</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="sa">f</span><span class="s2">"MATCH ()-[r:`</span><span class="si">{</span><span class="n">rel</span><span class="si">}</span><span class="s2">`]-&gt;() DELETE r"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
        <span class="n">cypher</span> <span class="o">=</span> <span class="s2">"MATCH (e) WHERE "</span>
        <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
            <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
        <span class="n">cypher</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher</span> <span class="o">+</span> <span class="s2">" DETACH DELETE e"</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Nebula](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/nebula/)[Next Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/)
