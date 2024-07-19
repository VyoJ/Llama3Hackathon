Title: Azurecosmosmongo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/

Markdown Content:
Azurecosmosmongo - LlamaIndex


AzureCosmosDBMongoDBVectorSearch [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/#llama_index.vector_stores.azurecosmosmongo.AzureCosmosDBMongoDBVectorSearch "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Azure CosmosDB MongoDB vCore Vector Store.

To use, you should have both: - the `pymongo` python package installed - a connection string associated with an Azure Cosmodb MongoDB vCore Cluster

**Examples:**

`pip install llama-index-vector-stores-azurecosmosmongo`

```
import pymongo
from llama_index.vector_stores.azurecosmosmongo import AzureCosmosDBMongoDBVectorSearch

# Set up the connection string with your Azure CosmosDB MongoDB URI
connection_string = "YOUR_AZURE_COSMOSDB_MONGODB_URI"
mongodb_client = pymongo.MongoClient(connection_string)

# Create an instance of AzureCosmosDBMongoDBVectorSearch
vector_store = AzureCosmosDBMongoDBVectorSearch(
    mongodb_client=mongodb_client,
    db_name="demo_vectordb",
    collection_name="paul_graham_essay",
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azurecosmosmongo/llama_index/vector_stores/azurecosmosmongo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 28</span>
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
<span class="normal">278</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureCosmosDBMongoDBVectorSearch</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure CosmosDB MongoDB vCore Vector Store.</span>

<span class="sd">    To use, you should have both:</span>
<span class="sd">    - the ``pymongo`` python package installed</span>
<span class="sd">    - a connection string associated with an Azure Cosmodb MongoDB vCore Cluster</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-azurecosmosmongo`</span>

<span class="sd">        ```python</span>
<span class="sd">        import pymongo</span>
<span class="sd">        from llama_index.vector_stores.azurecosmosmongo import AzureCosmosDBMongoDBVectorSearch</span>

<span class="sd">        # Set up the connection string with your Azure CosmosDB MongoDB URI</span>
<span class="sd">        connection_string = "YOUR_AZURE_COSMOSDB_MONGODB_URI"</span>
<span class="sd">        mongodb_client = pymongo.MongoClient(connection_string)</span>

<span class="sd">        # Create an instance of AzureCosmosDBMongoDBVectorSearch</span>
<span class="sd">        vector_store = AzureCosmosDBMongoDBVectorSearch(</span>
<span class="sd">            mongodb_client=mongodb_client,</span>
<span class="sd">            db_name="demo_vectordb",</span>
<span class="sd">            collection_name="paul_graham_essay",</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_insert_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_db_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_cosmos_search_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_mongodb_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">mongodb_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_db"</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_collection"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_vector_search_index"</span><span class="p">,</span>
        <span class="n">id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"id"</span><span class="p">,</span>
        <span class="n">embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"content_vector"</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">cosmos_search_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            mongodb_client: An Azure CosmoDB MongoDB client (type: MongoClient, shown any for lazy import).</span>
<span class="sd">            db_name: An Azure CosmosDB MongoDB database name.</span>
<span class="sd">            collection_name: An Azure CosmosDB collection name.</span>
<span class="sd">            index_name: An Azure CosmosDB MongoDB vCore Vector Search index name.</span>
<span class="sd">            id_key: The data field to use as the id.</span>
<span class="sd">            embedding_key: An Azure CosmosDB MongoDB field that will contain</span>
<span class="sd">            the embedding for each document.</span>
<span class="sd">            text_key: An Azure CosmosDB MongoDB field that will contain the text for each document.</span>
<span class="sd">            metadata_key: An Azure CosmosDB MongoDB field that will contain</span>
<span class="sd">            the metadata for each document.</span>
<span class="sd">            cosmos_search_kwargs: An Azure CosmosDB MongoDB field that will</span>
<span class="sd">            contain search options, such as kind, numLists, similarity, and dimensions.</span>
<span class="sd">            insert_kwargs: The kwargs used during `insert`.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">mongodb_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">pymongo</span><span class="o">.</span><span class="n">MongoClient</span><span class="p">,</span> <span class="n">mongodb_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"AZURE_COSMOSDB_MONGODB_URI"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify Azure cosmodb 'AZURE_COSMOSDB_MONGODB_URI' via env variable "</span>
                    <span class="s2">"if not directly passing in client."</span>
                <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span> <span class="o">=</span> <span class="n">pymongo</span><span class="o">.</span><span class="n">MongoClient</span><span class="p">(</span>
                <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"AZURE_COSMOSDB_MONGODB_URI"</span><span class="p">]</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span><span class="p">[</span><span class="n">db_name</span><span class="p">][</span><span class="n">collection_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="o">=</span> <span class="n">index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span> <span class="o">=</span> <span class="n">embedding_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span> <span class="o">=</span> <span class="n">id_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="o">=</span> <span class="n">text_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">=</span> <span class="n">metadata_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span> <span class="o">=</span> <span class="n">insert_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_db_name</span> <span class="o">=</span> <span class="n">db_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span> <span class="o">=</span> <span class="n">collection_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cosmos_search_kwargs</span> <span class="o">=</span> <span class="n">cosmos_search_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_create_vector_search_index</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_create_vector_search_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_db_name</span><span class="p">]</span>
        <span class="n">db</span><span class="o">.</span><span class="n">command</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"createIndexes"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="p">,</span>
                <span class="s2">"indexes"</span><span class="p">:</span> <span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">"name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                        <span class="s2">"key"</span><span class="p">:</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="s2">"cosmosSearch"</span><span class="p">},</span>
                        <span class="s2">"cosmosSearchOptions"</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">"kind"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cosmos_search_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                                <span class="s2">"kind"</span><span class="p">,</span> <span class="s2">"vector-ivf"</span>
                            <span class="p">),</span>
                            <span class="s2">"numLists"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cosmos_search_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"numLists"</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span>
                            <span class="s2">"similarity"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cosmos_search_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                                <span class="s2">"similarity"</span><span class="p">,</span> <span class="s2">"COS"</span>
                            <span class="p">),</span>
                            <span class="s2">"dimensions"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cosmos_search_kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                                <span class="s2">"dimensions"</span><span class="p">,</span> <span class="mi">1536</span>
                            <span class="p">),</span>
                        <span class="p">},</span>
                    <span class="p">}</span>
                <span class="p">],</span>
            <span class="p">}</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        Returns:</span>
<span class="sd">            A List of ids for successfully added nodes.</span>

<span class="sd">        """</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">data_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>

            <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="n">data_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into MongoDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
        <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
            <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="c1"># delete by filtering on the doc_id metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_one</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span> <span class="o">**</span><span class="n">delete_kwargs</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return MongoDB client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mongodb_client</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"vector"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="s2">"path"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">,</span>
            <span class="s2">"k"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Metadata filters not implemented for azure cosmosdb mongodb yet."</span>
            <span class="p">)</span>

        <span class="n">query_field</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"$search"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"cosmosSearch"</span><span class="p">:</span> <span class="n">params</span><span class="p">,</span> <span class="s2">"returnStoredSource"</span><span class="p">:</span> <span class="kc">True</span><span class="p">}}</span>

        <span class="n">pipeline</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">query_field</span><span class="p">,</span>
            <span class="p">{</span>
                <span class="s2">"$project"</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">"similarityScore"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$meta"</span><span class="p">:</span> <span class="s2">"searchScore"</span><span class="p">},</span>
                    <span class="s2">"document"</span><span class="p">:</span> <span class="s2">"$$ROOT"</span><span class="p">,</span>
                <span class="p">}</span>
            <span class="p">},</span>
        <span class="p">]</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Running query pipeline: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">pipeline</span><span class="p">)</span>
        <span class="n">cursor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">aggregate</span><span class="p">(</span><span class="n">pipeline</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">res</span> <span class="ow">in</span> <span class="n">cursor</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"document"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">)</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"similarityScore"</span><span class="p">)</span>
            <span class="nb">id</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"document"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">)</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"document"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                    <span class="n">metadata_dict</span>
                <span class="p">)</span>

                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span>
            <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of query: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query: a VectorStoreQuery object.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/#llama_index.vector_stores.azurecosmosmongo.AzureCosmosDBMongoDBVectorSearch.client "Permanent link")

```
client: Any
```

Return MongoDB client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/#llama_index.vector_stores.azurecosmosmongo.AzureCosmosDBMongoDBVectorSearch.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
A List of ids for successfully added nodes.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azurecosmosmongo/llama_index/vector_stores/azurecosmosmongo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">153</span>
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
<span class="normal">187</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    Returns:</span>
<span class="sd">        A List of ids for successfully added nodes.</span>

<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">data_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
        <span class="p">)</span>

        <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">data_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into MongoDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
    <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
        <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
    <span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/#llama_index.vector_stores.azurecosmosmongo.AzureCosmosDBMongoDBVectorSearch.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azurecosmosmongo/llama_index/vector_stores/azurecosmosmongo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">189</span>
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
<span class="normal">200</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="c1"># delete by filtering on the doc_id metadata</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_one</span><span class="p">(</span>
        <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span> <span class="o">**</span><span class="n">delete_kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/#llama_index.vector_stores.azurecosmosmongo.AzureCosmosDBMongoDBVectorSearch.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
a VectorStoreQuery object.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
A VectorStoreQueryResult containing the results of the query.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-azurecosmosmongo/llama_index/vector_stores/azurecosmosmongo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query: a VectorStoreQuery object.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azureaisearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/)[Next Bagel](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/bagel/)
