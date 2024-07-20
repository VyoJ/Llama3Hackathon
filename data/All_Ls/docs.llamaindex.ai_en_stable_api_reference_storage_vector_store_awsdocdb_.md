Title: Awsdocdb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/

Markdown Content:
Awsdocdb - LlamaIndex


AWSDocDbVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/#llama_index.vector_stores.awsdocdb.AWSDocDbVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

AWS DocumentDB Vector Store.

To use, you should have both: - the `pymongo` python package installed - a connection string associated with a DocumentDB Instance

Please refer to the official Vector Search documentation for more details: https://docs.aws.amazon.com/documentdb/latest/developerguide/vector-search.html

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-awsdocdb/llama_index/vector_stores/awsdocdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
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
<span class="normal">319</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AWSDocDbVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AWS DocumentDB Vector Store.</span>

<span class="sd">    To use, you should have both:</span>
<span class="sd">    - the ``pymongo`` python package installed</span>
<span class="sd">    - a connection string associated with a DocumentDB Instance</span>

<span class="sd">    Please refer to the official Vector Search documentation for more details:</span>
<span class="sd">    https://docs.aws.amazon.com/documentdb/latest/developerguide/vector-search.html</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">_docdb_client</span><span class="p">:</span> <span class="n">MongoClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_similarity_score</span><span class="p">:</span> <span class="n">AWSDocDbVectorStoreSimilarityType</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_insert_kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_crud</span><span class="p">:</span> <span class="n">DocDbIndex</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docdb_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_db"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_index"</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default_collection"</span><span class="p">,</span>
        <span class="n">id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"id"</span><span class="p">,</span>
        <span class="n">embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embedding"</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_score</span><span class="o">=</span><span class="s2">"cosine"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            docdb_client: A DocumentDB client.</span>
<span class="sd">            db_name: A DocumentDB database name.</span>
<span class="sd">            collection_name: A DocumentDB collection name.</span>
<span class="sd">            id_key: The data field to use as the id.</span>
<span class="sd">            embedding_key: A DocumentDB field that will contain</span>
<span class="sd">            the embedding for each document.</span>
<span class="sd">            text_key: A DocumentDB field that will contain the text for each document.</span>
<span class="sd">            metadata_key: A DocumentDB field that will contain</span>
<span class="sd">            the metadata for each document.</span>
<span class="sd">            insert_kwargs: The kwargs used during `insert`.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">docdb_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_docdb_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">MongoClient</span><span class="p">,</span> <span class="n">docdb_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify connection string to DocumentDB instance "</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_score</span> <span class="o">=</span> <span class="n">similarity_score</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docdb_client</span><span class="p">[</span><span class="n">db_name</span><span class="p">][</span><span class="n">collection_name</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span> <span class="o">=</span> <span class="n">embedding_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span> <span class="o">=</span> <span class="n">id_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="o">=</span> <span class="n">text_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">=</span> <span class="n">metadata_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span> <span class="o">=</span> <span class="n">insert_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_crud</span> <span class="o">=</span> <span class="n">DocDbIndex</span><span class="p">(</span><span class="n">index_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"AWSDocDbVectorStore"</span>

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
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into DocumentDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
        <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
            <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
        <span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using by id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No document id provided to delete."</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return DocDB client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docdb_client</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="n">projection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"vector"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="s2">"path"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">,</span>
            <span class="s2">"similarity"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_score</span><span class="p">,</span>
            <span class="s2">"k"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="o">=</span> <span class="n">_to_mongodb_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">projection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">pipeline</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"$search"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"vectorSearch"</span><span class="p">:</span> <span class="n">params</span><span class="p">}}]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">pipeline</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"$search"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"vectorSearch"</span><span class="p">:</span> <span class="n">params</span><span class="p">}},</span> <span class="p">{</span><span class="s2">"$project"</span><span class="p">:</span> <span class="n">projection</span><span class="p">}]</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Running query pipeline: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">pipeline</span><span class="p">)</span>
        <span class="n">cursor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">aggregate</span><span class="p">(</span><span class="n">pipeline</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">res</span> <span class="ow">in</span> <span class="n">cursor</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">)</span>
            <span class="n">vector</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">)</span>
            <span class="nb">id</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_id_key</span><span class="p">)</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">)</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">similarity</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span> <span class="n">vector</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_score</span><span class="p">)</span>

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

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
        <span class="n">projection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query: a VectorStoreQuery object.</span>
<span class="sd">            projection: a dictionary specifying which fields to return after the search</span>

<span class="sd">        Returns:</span>
<span class="sd">            A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">projection</span><span class="o">=</span><span class="n">projection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">create_index</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dimensions</span><span class="p">,</span> <span class="n">similarity_score</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_score</span>
        <span class="k">if</span> <span class="n">similarity_score</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">similarity</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_crud</span><span class="o">.</span><span class="n">create_index</span><span class="p">(</span><span class="n">dimensions</span><span class="p">,</span> <span class="n">score</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_index</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_crud</span><span class="o">.</span><span class="n">delete_index</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docdb_client</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/#llama_index.vector_stores.awsdocdb.AWSDocDbVectorStore.client "Permanent link")

```
client: Any
```

Return DocDB client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/#llama_index.vector_stores.awsdocdb.AWSDocDbVectorStore.add "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-awsdocdb/llama_index/vector_stores/awsdocdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">184</span>
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
<span class="normal">218</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
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
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting data into DocumentDB: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">data_to_insert</span><span class="p">)</span>
    <span class="n">insert_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">insert_many</span><span class="p">(</span>
        <span class="n">data_to_insert</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_insert_kwargs</span>
    <span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Result of insert: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">insert_result</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/#llama_index.vector_stores.awsdocdb.AWSDocDbVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using by id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document to delete.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-awsdocdb/llama_index/vector_stores/awsdocdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using by id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">ref_doc_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No document id provided to delete."</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete_one</span><span class="p">({</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/#llama_index.vector_stores.awsdocdb.AWSDocDbVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), projection: Optional[Dict[str, int]] = None, **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
a VectorStoreQuery object.



 | _required_ |
| `projection` | `Optional[Dict[str, int]]` | 

a dictionary specifying which fields to return after the search



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
A VectorStoreQueryResult containing the results of the query.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-awsdocdb/llama_index/vector_stores/awsdocdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">292</span>
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
<span class="normal">307</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span>
    <span class="n">projection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query: a VectorStoreQuery object.</span>
<span class="sd">        projection: a dictionary specifying which fields to return after the search</span>

<span class="sd">    Returns:</span>
<span class="sd">        A VectorStoreQueryResult containing the results of the query.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">projection</span><span class="o">=</span><span class="n">projection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Awadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awadb/)[Next Azureaisearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/)
