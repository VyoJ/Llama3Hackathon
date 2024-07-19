Title: Jaguar - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/

Markdown Content:
Jaguar - LlamaIndex


JaguarReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/#llama_index.readers.jaguar.JaguarReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Jaguar reader. Retrieve documents from existing persisted Jaguar store.

Source code in `llama-index-integrations/readers/llama-index-readers-jaguar/llama_index/readers/jaguar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
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
<span class="normal">248</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JaguarReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Jaguar reader.</span>
<span class="sd">    Retrieve documents from existing persisted Jaguar store.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">pod</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">store</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_index</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">vector_dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Constructor of JaguarReader.</span>

<span class="sd">        Args:</span>
<span class="sd">            pod: name of the pod (database)</span>
<span class="sd">            store: name of vector store in the pod</span>
<span class="sd">            vector_index: name of vector index of the store</span>
<span class="sd">            vector_type: type of the vector index</span>
<span class="sd">            vector_dimension: dimension of the vector index</span>
<span class="sd">            url: end point URL of jaguar http server</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">=</span> <span class="n">pod</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_store</span> <span class="o">=</span> <span class="n">store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span> <span class="o">=</span> <span class="n">vector_index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_type</span> <span class="o">=</span> <span class="n">vector_type</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_dimension</span> <span class="o">=</span> <span class="n">vector_dimension</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span> <span class="o">=</span> <span class="n">JaguarHttpClient</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="k">def</span> <span class="nf">login</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">jaguar_api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Login to jaguar server with a jaguar_api_key or let self._jag find a key.</span>

<span class="sd">        Args:</span>
<span class="sd">            optional jaguar_api_key (str): API key of user to jaguardb server.</span>
<span class="sd">            If not provided, jaguar api key is read from environment variable</span>
<span class="sd">            JAGUAR_API_KEY or from file $HOME/.jagrc</span>
<span class="sd">        Returns:</span>
<span class="sd">            True if successful; False if not successful</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">jaguar_api_key</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">logout</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logout from jaguar server to cleanup resources.</span>

<span class="sd">        Args: no args</span>
<span class="sd">        Returns: None</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">logout</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_token</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the jaguar vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            embedding: list of float number for vector. If this</span>
<span class="sd">                       is given, it returns topk similar documents.</span>
<span class="sd">            k: Number of results to return.</span>
<span class="sd">            where: "a = '100' or ( b &gt; 100 and c &lt; 200 )"</span>
<span class="sd">                   If embedding is not given, it finds values</span>
<span class="sd">                   of columns in metadata_fields, and the text value.</span>
<span class="sd">            metadata_fields: Optional[List[str]] a list of metadata fields to load</span>
<span class="sd">                       in addition to the text document</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of documents</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_similar_data</span><span class="p">(</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">,</span>
                <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span>
                <span class="n">metadata_fields</span><span class="o">=</span><span class="n">metadata_fields</span><span class="p">,</span>
                <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_store_data</span><span class="p">(</span>
                <span class="n">k</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">metadata_fields</span><span class="o">=</span><span class="n">metadata_fields</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_similar_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embedding</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
        <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data by similarity search from the jaguar store."""</span>
        <span class="c1">### args is additional search conditions, such as time decay</span>
        <span class="n">args</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"args"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">fetch_k</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fetch_k"</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>

        <span class="n">vcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span>
        <span class="n">vtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_type</span>
        <span class="n">str_embeddings</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">f</span><span class="p">)</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">embedding</span><span class="p">]</span>
        <span class="n">qv_comma</span> <span class="o">=</span> <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">str_embeddings</span><span class="p">)</span>
        <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
        <span class="n">q</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"select similarity("</span>
            <span class="o">+</span> <span class="n">vcol</span>
            <span class="o">+</span> <span class="s2">",'"</span>
            <span class="o">+</span> <span class="n">qv_comma</span>
            <span class="o">+</span> <span class="s2">"','topk="</span>
            <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
            <span class="o">+</span> <span class="s2">",fetch_k="</span>
            <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">fetch_k</span><span class="p">)</span>
            <span class="o">+</span> <span class="s2">",type="</span>
            <span class="o">+</span> <span class="n">vtype</span>
        <span class="p">)</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="s2">",with_score,with_text"</span>
        <span class="k">if</span> <span class="n">args</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">q</span> <span class="o">+=</span> <span class="s2">","</span> <span class="o">+</span> <span class="n">args</span>

        <span class="k">if</span> <span class="n">metadata_fields</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">x</span> <span class="o">=</span> <span class="s2">"&amp;"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">metadata_fields</span><span class="p">)</span>
            <span class="n">q</span> <span class="o">+=</span> <span class="s2">",metadata="</span> <span class="o">+</span> <span class="n">x</span>

        <span class="n">q</span> <span class="o">+=</span> <span class="s2">"') from "</span> <span class="o">+</span> <span class="n">podstore</span>

        <span class="k">if</span> <span class="n">where</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">q</span> <span class="o">+=</span> <span class="s2">" where "</span> <span class="o">+</span> <span class="n">where</span>

        <span class="n">jarr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">jarr</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">js</span> <span class="ow">in</span> <span class="n">jarr</span><span class="p">:</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
            <span class="n">zid</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="s2">"zid"</span><span class="p">]</span>

            <span class="n">md</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">md</span><span class="p">[</span><span class="s2">"zid"</span><span class="p">]</span> <span class="o">=</span> <span class="n">zid</span>
            <span class="n">md</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span> <span class="o">=</span> <span class="n">score</span>
            <span class="k">if</span> <span class="n">metadata_fields</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">metadata_fields</span><span class="p">:</span>
                    <span class="n">md</span><span class="p">[</span><span class="n">m</span><span class="p">]</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="n">m</span><span class="p">]</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">_load_store_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load a number of document from the jaguar store."""</span>
        <span class="n">vcol</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_index</span>
        <span class="n">podstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pod</span> <span class="o">+</span> <span class="s2">"."</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span>
        <span class="n">txtcol</span> <span class="o">=</span> <span class="n">vcol</span> <span class="o">+</span> <span class="s2">":text"</span>

        <span class="n">sel_str</span> <span class="o">=</span> <span class="s2">"zid,"</span> <span class="o">+</span> <span class="n">txtcol</span>
        <span class="k">if</span> <span class="n">metadata_fields</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">sel_str</span> <span class="o">+=</span> <span class="s2">","</span> <span class="o">+</span> <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">metadata_fields</span><span class="p">)</span>

        <span class="n">q</span> <span class="o">=</span> <span class="s2">"select "</span> <span class="o">+</span> <span class="n">sel_str</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="s2">" from "</span> <span class="o">+</span> <span class="n">podstore</span>

        <span class="k">if</span> <span class="n">where</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">q</span> <span class="o">+=</span> <span class="s2">" where "</span> <span class="o">+</span> <span class="n">where</span>
        <span class="n">q</span> <span class="o">+=</span> <span class="s2">" limit "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>

        <span class="n">jarr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">q</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">jarr</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">ds</span> <span class="ow">in</span> <span class="n">jarr</span><span class="p">:</span>
            <span class="n">js</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">ds</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="n">txtcol</span><span class="p">]</span>
            <span class="n">zid</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="s2">"zid"</span><span class="p">]</span>

            <span class="n">md</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">md</span><span class="p">[</span><span class="s2">"zid"</span><span class="p">]</span> <span class="o">=</span> <span class="n">zid</span>
            <span class="k">if</span> <span class="n">metadata_fields</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">metadata_fields</span><span class="p">:</span>
                    <span class="n">md</span><span class="p">[</span><span class="n">m</span><span class="p">]</span> <span class="o">=</span> <span class="n">js</span><span class="p">[</span><span class="n">m</span><span class="p">]</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">zid</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">md</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run any query statement in jaguardb.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): query statement to jaguardb</span>
<span class="sd">        Returns:</span>
<span class="sd">            None for invalid token, or</span>
<span class="sd">            json result string</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
        <span class="n">jaguar_api_key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">getApiKey</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_jaguar_api_key</span> <span class="o">=</span> <span class="n">jaguar_api_key</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">jaguar_api_key</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span> <span class="o"></span> <span class="s2">""</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_jag</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
    <span class="n">txt</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">text</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">txt</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Intercom](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/)[Next Jira](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/)
