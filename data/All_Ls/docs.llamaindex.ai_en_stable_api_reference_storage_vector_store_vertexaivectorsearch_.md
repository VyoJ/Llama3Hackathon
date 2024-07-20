Title: Vertexaivectorsearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/

Markdown Content:
Vertexaivectorsearch - LlamaIndex


VertexAIVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Vertex AI Vector Search vector store.

In this vector store, embeddings are stored in Vertex AI Vector Store and docs are stored within Cloud Storage bucket.

During query time, the index uses Vertex AI Vector Search to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `project_id` | `str) ` | 
The Google Cloud Project ID.



 | `None` |
| `region` | `str)     ` | 

The default location making the API calls. It must be the same location as where Vector Search index created and must be regional.



 | `None` |
| `index_id` | `str)   ` | 

The fully qualified resource name of the created index in Vertex AI Vector Search.



 | `None` |
| `endpoint_id` | `str` | 

The fully qualified resource name of the created index endpoint in Vertex AI Vector Search.



 | `None` |
| `gcs_bucket_name` | `Optional[str]` | 

```
           The location where the vectors will be stored for
           the index to be created in batch mode.
```



 | `None` |
| `credentials_path` | `Optional[str]` | 

```
           The path of the Google credentials on the local file
           system.
```



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-vertexaivectorsearch`

```
from
vector_store = VertexAIVectorStore(
    project_id=PROJECT_ID,
    region=REGION,
    index_id="<index_resource_name>"
    endpoint_id="<index_endpoint_resource_name>"
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-vertexaivectorsearch/llama_index/vector_stores/vertexaivectorsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 33</span>
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
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VertexAIVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vertex AI Vector Search vector store.</span>

<span class="sd">    In this vector store, embeddings are stored in Vertex AI Vector Store and</span>
<span class="sd">    docs are stored within Cloud Storage bucket.</span>

<span class="sd">    During query time, the index uses Vertex AI Vector Search to query for the</span>
<span class="sd">    top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        project_id (str) : The Google Cloud Project ID.</span>
<span class="sd">        region (str)     : The default location making the API calls.</span>
<span class="sd">                           It must be the same location as where Vector Search</span>
<span class="sd">                           index created and must be regional.</span>
<span class="sd">        index_id (str)   : The fully qualified resource name of the created</span>
<span class="sd">                           index in Vertex AI Vector Search.</span>
<span class="sd">        endpoint_id (str): The fully qualified resource name of the created</span>
<span class="sd">                           index endpoint in Vertex AI Vector Search.</span>
<span class="sd">        gcs_bucket_name (Optional[str]):</span>
<span class="sd">                           The location where the vectors will be stored for</span>
<span class="sd">                           the index to be created in batch mode.</span>
<span class="sd">        credentials_path (Optional[str]):</span>
<span class="sd">                           The path of the Google credentials on the local file</span>
<span class="sd">                           system.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-vertexaivectorsearch`</span>

<span class="sd">        ```python</span>
<span class="sd">        from</span>
<span class="sd">        vector_store = VertexAIVectorStore(</span>
<span class="sd">            project_id=PROJECT_ID,</span>
<span class="sd">            region=REGION,</span>
<span class="sd">            index_id="&lt;index_resource_name&gt;"</span>
<span class="sd">            endpoint_id="&lt;index_endpoint_resource_name&gt;"</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">remove_text_from_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span>

    <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">region</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">endpoint_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">gcs_bucket_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">credentials_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">_index</span><span class="p">:</span> <span class="n">MatchingEngineIndex</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_endpoint</span><span class="p">:</span> <span class="n">MatchingEngineIndexEndpoint</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_metadata</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_stream_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_staging_bucket</span><span class="p">:</span> <span class="n">storage</span><span class="o">.</span><span class="n">Bucket</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="c1"># _document_storage: GCSDocumentStorage = PrivateAttr()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">endpoint_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">gcs_bucket_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">credentials_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
        <span class="n">remove_text_from_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span>
            <span class="n">region</span><span class="o">=</span><span class="n">region</span><span class="p">,</span>
            <span class="n">index_id</span><span class="o">=</span><span class="n">index_id</span><span class="p">,</span>
            <span class="n">endpoint_id</span><span class="o">=</span><span class="n">endpoint_id</span><span class="p">,</span>
            <span class="n">gcs_bucket_name</span><span class="o">=</span><span class="n">gcs_bucket_name</span><span class="p">,</span>
            <span class="n">credentials_path</span><span class="o">=</span><span class="n">credentials_path</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="n">remove_text_from_metadata</span><span class="o">=</span><span class="n">remove_text_from_metadata</span><span class="p">,</span>
        <span class="p">)</span>

<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="n">_sdk_manager</span> <span class="o">=</span> <span class="n">VectorSearchSDKManager</span><span class="p">(</span>
            <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="n">region</span><span class="p">,</span> <span class="n">credentials_path</span><span class="o">=</span><span class="n">credentials_path</span>
        <span class="p">)</span>

        <span class="c1"># get index and endpoint resource names including metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">_sdk_manager</span><span class="o">.</span><span class="n">get_index</span><span class="p">(</span><span class="n">index_id</span><span class="o">=</span><span class="n">index_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_endpoint</span> <span class="o">=</span> <span class="n">_sdk_manager</span><span class="o">.</span><span class="n">get_endpoint</span><span class="p">(</span><span class="n">endpoint_id</span><span class="o">=</span><span class="n">endpoint_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>

        <span class="c1"># get index update method from index metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_update</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_metadata</span><span class="p">[</span><span class="s2">"indexUpdateMethod"</span><span class="p">]</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)]</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify filter via both query and kwargs. "</span>
                    <span class="s2">"Use kwargs only for Vertex AI Vector Search specific items that are "</span>
                    <span class="s2">"not supported via the generic query interface such as numeric filters."</span>
                <span class="p">)</span>
            <span class="nb">filter</span><span class="p">,</span> <span class="n">num_filter</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">to_vectorsearch_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">num_filter</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="n">matches</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">find_neighbors</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="n">endpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint</span><span class="p">,</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
            <span class="n">numeric_filter</span><span class="o">=</span><span class="n">num_filter</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">to_node</span><span class="p">(</span><span class="n">match</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">)</span>
            <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
            <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">distance</span><span class="p">)</span>
            <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### index `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.index "Permanent link")

```
index: Any
```

Get client.

### endpoint `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.endpoint "Permanent link")

```
endpoint: Any
```

Get client.

### staging\_bucket `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.staging_bucket "Permanent link")

```
staging_bucket: Any
```

Get client.

### from\_params `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.from_params "Permanent link")

```
from_params(project_id: Optional[str] = None, region: Optional[str] = None, index_id: Optional[str] = None, endpoint_id: Optional[str] = None, gcs_bucket_name: Optional[str] = None, credentials_path: Optional[str] = None, text_key: str = DEFAULT_TEXT_KEY, **kwargs: Any) -> [VertexAIVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore "llama_index.vector_stores.vertexaivectorsearch.base.VertexAIVectorStore")
```

Create VertexAIVectorStore from config.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-vertexaivectorsearch/llama_index/vector_stores/vertexaivectorsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">138</span>
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
<span class="normal">160</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">project_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">endpoint_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">gcs_bucket_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">credentials_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"VertexAIVectorStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create VertexAIVectorStore from config."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span>
        <span class="n">region</span><span class="o">=</span><span class="n">region</span><span class="p">,</span>
        <span class="n">index_name</span><span class="o">=</span><span class="n">index_id</span><span class="p">,</span>
        <span class="n">endpoint_id</span><span class="o">=</span><span class="n">endpoint_id</span><span class="p">,</span>
        <span class="n">gcs_bucket_name</span><span class="o">=</span><span class="n">gcs_bucket_name</span><span class="p">,</span>
        <span class="n">credentials_path</span><span class="o">=</span><span class="n">credentials_path</span><span class="p">,</span>
        <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], is_complete_overwrite: bool = False, **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-vertexaivectorsearch/llama_index/vector_stores/vertexaivectorsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">186</span>
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
<span class="normal">229</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="n">is_complete_overwrite</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">embeddings</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">metadatas</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>

        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
        <span class="n">embeddings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">embedding</span><span class="p">)</span>
        <span class="n">metadatas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>

    <span class="n">data_points</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">to_data_points</span><span class="p">(</span><span class="n">ids</span><span class="p">,</span> <span class="n">embeddings</span><span class="p">,</span> <span class="n">metadatas</span><span class="p">)</span>
    <span class="c1"># self._document_storage.add_documents(list(zip(ids, nodes)))</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_update</span><span class="p">:</span>
        <span class="n">utils</span><span class="o">.</span><span class="n">stream_update_index</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span> <span class="n">data_points</span><span class="o">=</span><span class="n">data_points</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_staging_bucket</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"To update a Vector Search index a staging bucket must"</span>
                <span class="s2">" be defined."</span>
            <span class="p">)</span>
        <span class="n">utils</span><span class="o">.</span><span class="n">batch_update_index</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="n">data_points</span><span class="o">=</span><span class="n">data_points</span><span class="p">,</span>
            <span class="n">staging_bucket</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_staging_bucket</span><span class="p">,</span>
            <span class="n">is_complete_overwrite</span><span class="o">=</span><span class="n">is_complete_overwrite</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document to delete.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-vertexaivectorsearch/llama_index/vector_stores/vertexaivectorsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">231</span>
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
<span class="normal">244</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>
<span class="sd">    """</span>
    <span class="c1"># get datapoint ids by filter</span>
    <span class="nb">filter</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">}</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">get_datapoints_by_filter</span><span class="p">(</span>
        <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">endpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">endpoint</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="nb">filter</span>
    <span class="p">)</span>
    <span class="c1"># remove datapoints</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">remove_datapoints</span><span class="p">(</span><span class="n">datapoint_ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/#llama_index.vector_stores.vertexaivectorsearch.VertexAIVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-vertexaivectorsearch/llama_index/vector_stores/vertexaivectorsearch/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">246</span>
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
<span class="normal">285</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes."""</span>
    <span class="n">query_embedding</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)]</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify filter via both query and kwargs. "</span>
                <span class="s2">"Use kwargs only for Vertex AI Vector Search specific items that are "</span>
                <span class="s2">"not supported via the generic query interface such as numeric filters."</span>
            <span class="p">)</span>
        <span class="nb">filter</span><span class="p">,</span> <span class="n">num_filter</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">to_vectorsearch_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">filter</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">num_filter</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">matches</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">find_neighbors</span><span class="p">(</span>
        <span class="n">index</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint</span><span class="p">,</span>
        <span class="n">embeddings</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
        <span class="n">numeric_filter</span><span class="o">=</span><span class="n">num_filter</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">to_node</span><span class="p">(</span><span class="n">match</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">)</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
        <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">distance</span><span class="p">)</span>
        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vearch/)[Next Vespa](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vespa/)
