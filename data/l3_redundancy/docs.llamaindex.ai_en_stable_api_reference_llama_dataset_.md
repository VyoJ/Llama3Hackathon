Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/

Markdown Content:
Index - LlamaIndex


Dataset Module.

BaseLlamaDataExample [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataExample "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base llama dataset example class.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseLlamaDataExample</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base llama dataset example class."""</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseLlamaDataExample"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataExample.class_name "Permanent link")

```
class_name: str
```

Class name.

BaseLlamaDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`, `Generic[P]`

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">114</span>
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
<span class="normal">322</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseLlamaDataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">P</span><span class="p">]):</span>
    <span class="n">_example_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseLlamaDataExample</span><span class="p">]</span> <span class="o">=</span> <span class="n">BaseLlamaDataExample</span>  <span class="c1"># type: ignore[misc]</span>
    <span class="n">examples</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaDataExample</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="p">[],</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Data examples of this dataset."</span>
    <span class="p">)</span>
    <span class="n">_predictions_cache</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="nb">int</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaDataExample</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Enable slicing and indexing.</span>

<span class="sd">        Returns the desired slice on `examples`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">[</span><span class="n">val</span><span class="p">]</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>

    <span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Save json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_example_type</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">]</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"examples"</span><span class="p">:</span> <span class="n">examples</span><span class="p">,</span>
            <span class="p">}</span>

            <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLlamaDataset"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

        <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="bp">cls</span><span class="o">.</span><span class="n">_example_type</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"examples"</span><span class="p">]]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_construct_prediction_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Construct the specific prediction dataset.</span>

<span class="sd">        Args:</span>
<span class="sd">            predictions (List[BaseLlamaExamplePrediction]): the list of predictions.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BaseLlamaPredictionDataset: A dataset of predictions.</span>
<span class="sd">        """</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_predict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">BaseLlamaDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Predict on a single example.</span>

<span class="sd">        NOTE: Subclasses need to implement this.</span>

<span class="sd">        Args:</span>
<span class="sd">            predictor (PredictorType): The predictor to make the prediciton with.</span>
<span class="sd">            example (BaseLlamaDataExample): The example to predict on.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BaseLlamaExamplePrediction: The prediction.</span>
<span class="sd">        """</span>

    <span class="k">def</span> <span class="nf">make_predictions_with</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Predict with a given query engine.</span>

<span class="sd">        Args:</span>
<span class="sd">            predictor (PredictorType): The predictor to make predictions with.</span>
<span class="sd">            show_progress (bool, optional): Show progress of making predictions.</span>
<span class="sd">            batch_size (int): Used to batch async calls, especially to reduce chances</span>
<span class="sd">                            of hitting RateLimitError from openai.</span>
<span class="sd">            sleep_time_in_seconds (int): Amount of time to sleep between batch call</span>
<span class="sd">                            to reduce chance of hitting RateLimitError from openai.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BaseLlamaPredictionDataset: A dataset of predictions.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">:</span>
            <span class="n">start_example_position</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">start_example_position</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples</span><span class="p">(</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">start_position</span><span class="o">=</span><span class="n">start_example_position</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                <span class="n">example_iterator</span> <span class="o">=</span> <span class="n">tqdm</span><span class="o">.</span><span class="n">tqdm</span><span class="p">(</span><span class="n">batch</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">example_iterator</span> <span class="o">=</span> <span class="n">batch</span>
            <span class="k">for</span> <span class="n">example</span> <span class="ow">in</span> <span class="n">example_iterator</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_predict_example</span><span class="p">(</span><span class="n">predictor</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_construct_prediction_dataset</span><span class="p">(</span><span class="n">predictions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>

    <span class="c1"># async methods</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_apredict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">BaseLlamaDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async predict on a single example.</span>

<span class="sd">        NOTE: Subclasses need to implement this.</span>

<span class="sd">        Args:</span>
<span class="sd">            predictor (PredictorType): The predictor to make the prediciton with.</span>
<span class="sd">            example (BaseLlamaDataExample): The example to predict on.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BaseLlamaExamplePrediction: The prediction.</span>
<span class="sd">        """</span>

    <span class="k">def</span> <span class="nf">_batch_examples</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">start_position</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaDataExample</span><span class="p">],</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Batches examples and predictions with a given batch_size."""</span>
        <span class="n">num_examples</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">ndx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start_position</span><span class="p">,</span> <span class="n">num_examples</span><span class="p">,</span> <span class="n">batch_size</span><span class="p">):</span>
            <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">[</span><span class="n">ndx</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span><span class="n">ndx</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">,</span> <span class="n">num_examples</span><span class="p">)]</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">amake_predictions_with</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async predict with a given query engine.</span>

<span class="sd">        Args:</span>
<span class="sd">            predictor (PredictorType): The predictor to make predictions with.</span>
<span class="sd">            show_progress (bool, optional): Show progress of making predictions.</span>
<span class="sd">            batch_size (int): Used to batch async calls, especially to reduce chances</span>
<span class="sd">                            of hitting RateLimitError from openai.</span>
<span class="sd">            sleep_time_in_seconds (int): Amount of time to sleep between batch call</span>
<span class="sd">                            to reduce chance of hitting RateLimitError from openai.</span>

<span class="sd">        Returns:</span>
<span class="sd">            BaseLlamaPredictionDataset: A dataset of predictions.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">:</span>
            <span class="n">start_example_position</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">start_example_position</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples</span><span class="p">(</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">start_position</span><span class="o">=</span><span class="n">start_example_position</span>
        <span class="p">):</span>
            <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">example</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_apredict_example</span><span class="p">(</span><span class="n">predictor</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="n">asyncio_mod</span> <span class="o">=</span> <span class="n">asyncio_module</span><span class="p">(</span><span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                    <span class="n">batch_predictions</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
                        <span class="o">*</span><span class="n">tasks</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Batch processing of predictions"</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">batch_predictions</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
            <span class="k">except</span> <span class="n">RateLimitError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                    <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"You've hit rate limits on your OpenAI subscription. This"</span>
                    <span class="s2">" class caches previous predictions after each successful"</span>
                    <span class="s2">" batch execution. Based off this cache, when executing this"</span>
                    <span class="s2">" command again it will attempt to predict on only the examples "</span>
                    <span class="s2">"that have not yet been predicted. Try reducing your batch_size."</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span> <span class="o">+=</span> <span class="n">batch_predictions</span>
            <span class="c1"># time.sleep(sleep_time_in_seconds)</span>

        <span class="n">prediction_dataset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_construct_prediction_dataset</span><span class="p">(</span>
            <span class="n">predictions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># clear cache</span>
        <span class="k">return</span> <span class="n">prediction_dataset</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseLlamaDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
</code></pre></div></td></tr></tbody></table>

### save\_json [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.save_json "Permanent link")

```
save_json(path: str) -> None
```

Save json.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Save json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_example_type</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">]</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"examples"</span><span class="p">:</span> <span class="n">examples</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_json `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.from_json "Permanent link")

```
from_json(path: str) -> [BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")
```

Load json.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

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
<span class="normal">154</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLlamaDataset"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

    <span class="n">examples</span> <span class="o">=</span> <span class="p">[</span><span class="bp">cls</span><span class="o">.</span><span class="n">_example_type</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"examples"</span><span class="p">]]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">examples</span><span class="o">=</span><span class="n">examples</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### make\_predictions\_with [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.make_predictions_with "Permanent link")

```
make_predictions_with(predictor: P, show_progress: bool = False, batch_size: int = 20, sleep_time_in_seconds: int = 0) -> [BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")
```

Predict with a given query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `predictor` | `PredictorType` | 
The predictor to make predictions with.



 | _required_ |
| `show_progress` | `bool` | 

Show progress of making predictions.



 | `False` |
| `batch_size` | `int` | 

Used to batch async calls, especially to reduce chances of hitting RateLimitError from openai.



 | `20` |
| `sleep_time_in_seconds` | `int` | 

Amount of time to sleep between batch call to reduce chance of hitting RateLimitError from openai.



 | `0` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `BaseLlamaPredictionDataset` | `[BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")` | 
A dataset of predictions.



 |

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">188</span>
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
<span class="normal">225</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">make_predictions_with</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
    <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaPredictionDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Predict with a given query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        predictor (PredictorType): The predictor to make predictions with.</span>
<span class="sd">        show_progress (bool, optional): Show progress of making predictions.</span>
<span class="sd">        batch_size (int): Used to batch async calls, especially to reduce chances</span>
<span class="sd">                        of hitting RateLimitError from openai.</span>
<span class="sd">        sleep_time_in_seconds (int): Amount of time to sleep between batch call</span>
<span class="sd">                        to reduce chance of hitting RateLimitError from openai.</span>

<span class="sd">    Returns:</span>
<span class="sd">        BaseLlamaPredictionDataset: A dataset of predictions.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">:</span>
        <span class="n">start_example_position</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">start_example_position</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples</span><span class="p">(</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">start_position</span><span class="o">=</span><span class="n">start_example_position</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
            <span class="n">example_iterator</span> <span class="o">=</span> <span class="n">tqdm</span><span class="o">.</span><span class="n">tqdm</span><span class="p">(</span><span class="n">batch</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">example_iterator</span> <span class="o">=</span> <span class="n">batch</span>
        <span class="k">for</span> <span class="n">example</span> <span class="ow">in</span> <span class="n">example_iterator</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_predict_example</span><span class="p">(</span><span class="n">predictor</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_construct_prediction_dataset</span><span class="p">(</span><span class="n">predictions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### amake\_predictions\_with `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset.amake_predictions_with "Permanent link")

```
amake_predictions_with(predictor: P, show_progress: bool = False, batch_size: int = 20, sleep_time_in_seconds: int = 1) -> [BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")
```

Async predict with a given query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `predictor` | `PredictorType` | 
The predictor to make predictions with.



 | _required_ |
| `show_progress` | `bool` | 

Show progress of making predictions.



 | `False` |
| `batch_size` | `int` | 

Used to batch async calls, especially to reduce chances of hitting RateLimitError from openai.



 | `20` |
| `sleep_time_in_seconds` | `int` | 

Amount of time to sleep between batch call to reduce chance of hitting RateLimitError from openai.



 | `1` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `BaseLlamaPredictionDataset` | `[BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")` | 
A dataset of predictions.



 |

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">257</span>
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
<span class="normal">316</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">amake_predictions_with</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">predictor</span><span class="p">:</span> <span class="n">P</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span>
    <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseLlamaPredictionDataset</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Async predict with a given query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        predictor (PredictorType): The predictor to make predictions with.</span>
<span class="sd">        show_progress (bool, optional): Show progress of making predictions.</span>
<span class="sd">        batch_size (int): Used to batch async calls, especially to reduce chances</span>
<span class="sd">                        of hitting RateLimitError from openai.</span>
<span class="sd">        sleep_time_in_seconds (int): Amount of time to sleep between batch call</span>
<span class="sd">                        to reduce chance of hitting RateLimitError from openai.</span>

<span class="sd">    Returns:</span>
<span class="sd">        BaseLlamaPredictionDataset: A dataset of predictions.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">:</span>
        <span class="n">start_example_position</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">start_example_position</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_batch_examples</span><span class="p">(</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">start_position</span><span class="o">=</span><span class="n">start_example_position</span>
    <span class="p">):</span>
        <span class="n">tasks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">example</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
            <span class="n">tasks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_apredict_example</span><span class="p">(</span><span class="n">predictor</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">sleep_time_in_seconds</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="n">asyncio_mod</span> <span class="o">=</span> <span class="n">asyncio_module</span><span class="p">(</span><span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                <span class="n">batch_predictions</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
                    <span class="o">*</span><span class="n">tasks</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="s2">"Batch processing of predictions"</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">batch_predictions</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">RateLimitError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">show_progress</span><span class="p">:</span>
                <span class="n">asyncio_mod</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"You've hit rate limits on your OpenAI subscription. This"</span>
                <span class="s2">" class caches previous predictions after each successful"</span>
                <span class="s2">" batch execution. Based off this cache, when executing this"</span>
                <span class="s2">" command again it will attempt to predict on only the examples "</span>
                <span class="s2">"that have not yet been predicted. Try reducing your batch_size."</span>
            <span class="p">)</span> <span class="kn">from</span> <span class="nn">err</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span> <span class="o">+=</span> <span class="n">batch_predictions</span>
        <span class="c1"># time.sleep(sleep_time_in_seconds)</span>

    <span class="n">prediction_dataset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_construct_prediction_dataset</span><span class="p">(</span>
        <span class="n">predictions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_predictions_cache</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c1"># clear cache</span>
    <span class="k">return</span> <span class="n">prediction_dataset</span>
</code></pre></div></td></tr></tbody></table>

BaseLlamaExamplePrediction [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaExamplePrediction "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base llama dataset example class.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseLlamaExamplePrediction</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base llama dataset example class."""</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseLlamaPrediction"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaExamplePrediction.class_name "Permanent link")

```
class_name: str
```

Class name.

BaseLlamaPredictionDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 64</span>
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
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseLlamaPredictionDataset</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">_prediction_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">]</span> <span class="o">=</span> <span class="n">BaseLlamaExamplePrediction</span>  <span class="c1"># type: ignore[misc]</span>
    <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Predictions on train_examples."</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="nb">int</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Enable slicing and indexing.</span>

<span class="sd">        Returns the desired slice on `predictions`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">[</span><span class="n">val</span><span class="p">]</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>

    <span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Save json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">predictions</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
                <span class="n">predictions</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_prediction_type</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span>
                <span class="p">]</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"predictions"</span><span class="p">:</span> <span class="n">predictions</span><span class="p">,</span>
            <span class="p">}</span>

            <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLlamaPredictionDataset"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load json."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

        <span class="n">predictions</span> <span class="o">=</span> <span class="p">[</span><span class="bp">cls</span><span class="o">.</span><span class="n">_prediction_type</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"predictions"</span><span class="p">]]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">predictions</span><span class="o">=</span><span class="n">predictions</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseLlamaPredictionDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
</code></pre></div></td></tr></tbody></table>

### save\_json [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset.save_json "Permanent link")

```
save_json(path: str) -> None
```

Save json.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">81</span>
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
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">save_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Save json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">predictions</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
            <span class="n">predictions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_prediction_type</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span>
            <span class="p">]</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"predictions"</span><span class="p">:</span> <span class="n">predictions</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_json `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset.from_json "Permanent link")

```
from_json(path: str) -> [BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")
```

Load json.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseLlamaPredictionDataset"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load json."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

    <span class="n">predictions</span> <span class="o">=</span> <span class="p">[</span><span class="bp">cls</span><span class="o">.</span><span class="n">_prediction_type</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">el</span><span class="p">)</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"predictions"</span><span class="p">]]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">predictions</span><span class="o">=</span><span class="n">predictions</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

CreatedByType [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.CreatedByType "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

The kinds of rag data examples.

Source code in `llama-index-core/llama_index/core/llama_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CreatedByType</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""The kinds of rag data examples."""</span>

    <span class="n">HUMAN</span> <span class="o">=</span> <span class="s2">"human"</span>
    <span class="n">AI</span> <span class="o">=</span> <span class="s2">"ai"</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</code></pre></div></td></tr></tbody></table>

EvaluatorExamplePrediction [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.EvaluatorExamplePrediction "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaExamplePrediction](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaExamplePrediction "llama_index.core.llama_dataset.base.BaseLlamaExamplePrediction")`

Evaluation example prediction class.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `feedback` | `Optional[str]` | 
The evaluator's feedback.



 | _required_ |
| `score` | `Optional[float]` | 

The evaluator's score.



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
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
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EvaluatorExamplePrediction</span><span class="p">(</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Evaluation example prediction class.</span>

<span class="sd">    Args:</span>
<span class="sd">        feedback (Optional[str]): The evaluator's feedback.</span>
<span class="sd">        score (Optional[float]): The evaluator's score.</span>
<span class="sd">    """</span>

    <span class="n">feedback</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The generated (predicted) response that can be compared to a reference (ground-truth) answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The generated (predicted) response that can be compared to a reference (ground-truth) answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">invalid_prediction</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether or not the prediction is a valid one."</span>
    <span class="p">)</span>
    <span class="n">invalid_reason</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Reason as to why prediction is invalid."</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"EvaluatorExamplePrediction"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.EvaluatorExamplePrediction.class_name "Permanent link")

```
class_name: str
```

Data example class name.

EvaluatorPredictionDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.EvaluatorPredictionDataset "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")`

Evaluation Prediction Dataset Class.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">113</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EvaluatorPredictionDataset</span><span class="p">(</span><span class="n">BaseLlamaPredictionDataset</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Evaluation Prediction Dataset Class."""</span>

    <span class="n">_prediction_type</span> <span class="o">=</span> <span class="n">EvaluatorExamplePrediction</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
                <span class="s2">"score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"EvaluatorPredictionDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.EvaluatorPredictionDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.EvaluatorPredictionDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="s2">"score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
        <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

LabelledEvaluatorDataExample [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataExample "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaDataExample](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataExample "llama_index.core.llama_dataset.base.BaseLlamaDataExample")`

Evaluation example class.

This data class contains the ingredients to perform a new "prediction" i.e., evaluation. Here an evaluator is meant to evaluate a response against an associated query as well as optionally contexts.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The user query



 | _required_ |
| `query_by` | `CreatedBy` | 

Query generated by human or ai (model-name)



 | _required_ |
| `contexts` | `Optional[List[str]]` | 

The contexts used for response



 | _required_ |
| `answer` | `str` | 

Answer to the query that is to be evaluated.



 | _required_ |
| `answer_by` |  | 

The reference answer generated by human or ai (model-name).



 | _required_ |
| `ground_truth_answer` | `Optional[str]` | 

 | _required_ |
| `ground_truth_answer_by` | `Optional[CreatedBy]` | 

 | _required_ |
| `reference_feedback` | `str` | 

The reference feedback evaluation.



 | _required_ |
| `reference_score` | `float` | 

The reference score evaluation.



 | _required_ |
| `reference_evaluation_by` | `CreatedBy` | 

Evaluation generated by human or ai (model-name)



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 52</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledEvaluatorDataExample</span><span class="p">(</span><span class="n">BaseLlamaDataExample</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Evaluation example class.</span>

<span class="sd">    This data class contains the ingredients to perform a new "prediction" i.e.,</span>
<span class="sd">    evaluation. Here an evaluator is meant to evaluate a response against an</span>
<span class="sd">    associated query as well as optionally contexts.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The user query</span>
<span class="sd">        query_by (CreatedBy): Query generated by human or ai (model-name)</span>
<span class="sd">        contexts (Optional[List[str]]): The contexts used for response</span>
<span class="sd">        answer (str): Answer to the query that is to be evaluated.</span>
<span class="sd">        answer_by: The reference answer generated by human or ai (model-name).</span>
<span class="sd">        ground_truth_answer (Optional[str]):</span>
<span class="sd">        ground_truth_answer_by (Optional[CreatedBy]):</span>
<span class="sd">        reference_feedback (str): The reference feedback evaluation.</span>
<span class="sd">        reference_score (float): The reference score evaluation.</span>
<span class="sd">        reference_evaluation_by (CreatedBy): Evaluation generated by human or ai (model-name)</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The user query for the example."</span>
    <span class="p">)</span>
    <span class="n">query_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the query."</span>
    <span class="p">)</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The contexts used to generate the answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">answer</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The provided answer to the example that is to be evaluated."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">answer_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the answer."</span>
    <span class="p">)</span>
    <span class="n">ground_truth_answer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The ground truth answer to the example that is used to evaluate the provided `answer`."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">ground_truth_answer_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the ground-truth answer."</span>
    <span class="p">)</span>
    <span class="n">reference_feedback</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The reference feedback (ground-truth)."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">reference_score</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">float</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The reference score (ground-truth)."</span>
    <span class="p">)</span>
    <span class="n">reference_evaluation_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the evaluation (feedback and score)."</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledEvaluatorDataExample"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataExample.class_name "Permanent link")

```
class_name: str
```

Data example class name.

LabelledEvaluatorDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataset "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")[[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.BaseEvaluator")]`

LabelledEvalationDataset class.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">135</span>
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
<span class="normal">232</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledEvaluatorDataset</span><span class="p">(</span><span class="n">BaseLlamaDataset</span><span class="p">[</span><span class="n">BaseEvaluator</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""LabelledEvalationDataset class."""</span>

    <span class="n">_example_type</span> <span class="o">=</span> <span class="n">LabelledEvaluatorDataExample</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"ground_truth_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"ground_truth_answer_by"</span><span class="p">:</span> <span class="p">[</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
            <span class="p">],</span>
            <span class="s2">"reference_feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_evaluation_by"</span><span class="p">:</span> <span class="p">[</span>
                <span class="n">t</span><span class="o">.</span><span class="n">reference_evaluation_by</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
            <span class="p">],</span>
        <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_apredict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledEvaluatorDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async predict RAG example with a query engine."""</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span> <span class="o">=</span> <span class="k">await</span> <span class="n">predictor</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
                <span class="n">contexts</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
                <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">ground_truth_answer</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="c1"># TODO: raise warning here as well</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Caught error </span><span class="si">{</span><span class="n">err</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_reason</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_predict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledEvaluatorDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Predict RAG example with a query engine."""</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span> <span class="o">=</span> <span class="n">predictor</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
                <span class="n">contexts</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
                <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">ground_truth_answer</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="c1"># TODO: raise warning here as well</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Caught error </span><span class="si">{</span><span class="n">err</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">EvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_reason</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_construct_prediction_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluatorExamplePrediction</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluatorPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Construct prediction dataset."""</span>
        <span class="k">return</span> <span class="n">EvaluatorPredictionDataset</span><span class="p">(</span><span class="n">predictions</span><span class="o">=</span><span class="n">predictions</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledEvaluatorDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

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
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"ground_truth_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"ground_truth_answer_by"</span><span class="p">:</span> <span class="p">[</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
        <span class="p">],</span>
        <span class="s2">"reference_feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_evaluation_by"</span><span class="p">:</span> <span class="p">[</span>
            <span class="n">t</span><span class="o">.</span><span class="n">reference_evaluation_by</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
        <span class="p">],</span>
    <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

LabelledPairwiseEvaluatorDataExample [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataExample "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[LabelledEvaluatorDataExample](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledEvaluatorDataExample "llama_index.core.llama_dataset.evaluator_evaluation.LabelledEvaluatorDataExample")`

Labelled pairwise evaluation data example class.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">294</span>
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
<span class="normal">308</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledPairwiseEvaluatorDataExample</span><span class="p">(</span><span class="n">LabelledEvaluatorDataExample</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Labelled pairwise evaluation data example class."""</span>

    <span class="n">second_answer</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The second answer to the example that is to be evaluated along versus `answer`."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">second_answer_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the second answer."</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledPairwiseEvaluatorDataExample"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataExample.class_name "Permanent link")

```
class_name: str
```

Data example class name.

LabelledPairwiseEvaluatorDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataset "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")[[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.BaseEvaluator")]`

Labelled pairwise evaluation dataset. For evaluating the evaluator in performing pairwise evaluations.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `BaseLlamaDataset` | `_type_` | 
_description_



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">311</span>
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
<span class="normal">421</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledPairwiseEvaluatorDataset</span><span class="p">(</span><span class="n">BaseLlamaDataset</span><span class="p">[</span><span class="n">BaseEvaluator</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Labelled pairwise evaluation dataset. For evaluating the evaluator in</span>
<span class="sd">    performing pairwise evaluations.</span>

<span class="sd">    Args:</span>
<span class="sd">        BaseLlamaDataset (_type_): _description_</span>
<span class="sd">    """</span>

    <span class="n">_example_type</span> <span class="o">=</span> <span class="n">LabelledPairwiseEvaluatorDataExample</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"second_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">second_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"ground_truth_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"second_answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">second_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"ground_truth_answer_by"</span><span class="p">:</span> <span class="p">[</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
            <span class="p">],</span>
            <span class="s2">"reference_feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_evaluation_by"</span><span class="p">:</span> <span class="p">[</span>
                <span class="n">t</span><span class="o">.</span><span class="n">reference_evaluation_by</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
            <span class="p">],</span>
        <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_apredict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledPairwiseEvaluatorDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async predict evaluation example with an Evaluator."""</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span> <span class="o">=</span> <span class="k">await</span> <span class="n">predictor</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
                <span class="n">second_response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">second_answer</span><span class="p">,</span>
                <span class="n">contexts</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
                <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">ground_truth_answer</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="c1"># TODO: raise warning here as well</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Caught error </span><span class="si">{</span><span class="n">err</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span>
                <span class="n">score</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span><span class="p">,</span>
                <span class="n">evaluation_source</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">pairwise_source</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_reason</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_predict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseEvaluator</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledPairwiseEvaluatorDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Predict RAG example with a query engine."""</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">eval_result</span><span class="p">:</span> <span class="n">EvaluationResult</span> <span class="o">=</span> <span class="n">predictor</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
                <span class="n">second_response</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">second_answer</span><span class="p">,</span>
                <span class="n">contexts</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">contexts</span><span class="p">,</span>
                <span class="n">reference</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">ground_truth_answer</span><span class="p">,</span>
                <span class="n">sleep_time_in_seconds</span><span class="o">=</span><span class="n">sleep_time_in_seconds</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
            <span class="c1"># TODO: raise warning here as well</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Caught error </span><span class="si">{</span><span class="n">err</span><span class="si">!s}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">feedback</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">feedback</span><span class="p">,</span>
                <span class="n">score</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">score</span><span class="p">,</span>
                <span class="n">evaluation_source</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">pairwise_source</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span>
                <span class="n">invalid_prediction</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">invalid_reason</span><span class="o">=</span><span class="n">eval_result</span><span class="o">.</span><span class="n">invalid_reason</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_construct_prediction_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PairwiseEvaluatorExamplePrediction</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PairwiseEvaluatorPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Construct prediction dataset."""</span>
        <span class="k">return</span> <span class="n">PairwiseEvaluatorPredictionDataset</span><span class="p">(</span><span class="n">predictions</span><span class="o">=</span><span class="n">predictions</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledPairwiseEvaluatorDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledPairwiseEvaluatorDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">321</span>
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
<span class="normal">342</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"second_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">second_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"ground_truth_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"second_answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">second_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"ground_truth_answer_by"</span><span class="p">:</span> <span class="p">[</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">ground_truth_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
        <span class="p">],</span>
        <span class="s2">"reference_feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_evaluation_by"</span><span class="p">:</span> <span class="p">[</span>
            <span class="n">t</span><span class="o">.</span><span class="n">reference_evaluation_by</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span>
        <span class="p">],</span>
    <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

PairwiseEvaluatorExamplePrediction [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.PairwiseEvaluatorExamplePrediction "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaExamplePrediction](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaExamplePrediction "llama_index.core.llama_dataset.base.BaseLlamaExamplePrediction")`

Pairwise evaluation example prediction class.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `feedback` | `Optional[str]` | 
The evaluator's feedback.



 | _required_ |
| `score` | `Optional[float]` | 

The evaluator's score.



 | _required_ |
| `evaluation_source` | `EvaluationSource` | 

If the evaluation came from original order or flipped; or inconclusive.



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">235</span>
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
<span class="normal">268</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PairwiseEvaluatorExamplePrediction</span><span class="p">(</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pairwise evaluation example prediction class.</span>

<span class="sd">    Args:</span>
<span class="sd">        feedback (Optional[str]): The evaluator's feedback.</span>
<span class="sd">        score (Optional[float]): The evaluator's score.</span>
<span class="sd">        evaluation_source (EvaluationSource): If the evaluation came from original order or flipped; or inconclusive.</span>
<span class="sd">    """</span>

    <span class="n">feedback</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The generated (predicted) response that can be compared to a reference (ground-truth) answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The generated (predicted) response that can be compared to a reference (ground-truth) answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">evaluation_source</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">EvaluationSource</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Whether the evaluation comes from original, or flipped ordering. Can also be neither here indicating inconclusive judgement."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">invalid_prediction</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether or not the prediction is a valid one."</span>
    <span class="p">)</span>
    <span class="n">invalid_reason</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Reason as to why prediction is invalid."</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"PairwiseEvaluatorExamplePrediction"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.PairwiseEvaluatorExamplePrediction.class_name "Permanent link")

```
class_name: str
```

Data example class name.

PairwiseEvaluatorPredictionDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.PairwiseEvaluatorPredictionDataset "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")`

Pairwise evaluation predictions dataset class.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">271</span>
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
<span class="normal">291</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PairwiseEvaluatorPredictionDataset</span><span class="p">(</span><span class="n">BaseLlamaPredictionDataset</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pairwise evaluation predictions dataset class."""</span>

    <span class="n">_prediction_type</span> <span class="o">=</span> <span class="n">PairwiseEvaluatorExamplePrediction</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
                <span class="s2">"score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
                <span class="s2">"ordering"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">evaluation_source</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"PairwiseEvaluatorPredictionDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.PairwiseEvaluatorPredictionDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.PairwiseEvaluatorPredictionDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/evaluator_evaluation.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"feedback"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">feedback</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="s2">"score"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">score</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="s2">"ordering"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">evaluation_source</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
        <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

LabelledRagDataExample [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataExample "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaDataExample](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataExample "llama_index.core.llama_dataset.base.BaseLlamaDataExample")`

RAG example class. Analogous to traditional ML datasets, this dataset contains the "features" (i.e., query + context) to make a prediction and the "label" (i.e., response) to evaluate the prediction.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The user query



 | _required_ |
| `query_by` | `CreatedBy` | 

Query generated by human or ai (model-name)



 | _required_ |
| `reference_contexts` | `Optional[List[str]]` | 

The contexts used for response



 | _required_ |
| `reference_answer` | `[str]` | 

Reference answer to the query. An answer that would receive full marks upon evaluation.



 | _required_ |
| `reference_answer_by` |  | 

The reference answer generated by human or ai (model-name).



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
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
<span class="normal">77</span>
<span class="normal">78</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledRagDataExample</span><span class="p">(</span><span class="n">BaseLlamaDataExample</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAG example class. Analogous to traditional ML datasets, this dataset contains</span>
<span class="sd">    the "features" (i.e., query + context) to make a prediction and the "label" (i.e., response)</span>
<span class="sd">    to evaluate the prediction.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The user query</span>
<span class="sd">        query_by (CreatedBy): Query generated by human or ai (model-name)</span>
<span class="sd">        reference_contexts (Optional[List[str]]): The contexts used for response</span>
<span class="sd">        reference_answer ([str]): Reference answer to the query. An answer</span>
<span class="sd">                                    that would receive full marks upon evaluation.</span>
<span class="sd">        reference_answer_by: The reference answer generated by human or ai (model-name).</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The user query for the example."</span>
    <span class="p">)</span>
    <span class="n">query_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the query."</span>
    <span class="p">)</span>
    <span class="n">reference_contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The contexts used to generate the reference answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">reference_answer</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The reference (ground-truth) answer to the example."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">reference_answer_by</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CreatedBy</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"What generated the reference answer."</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledRagDataExample"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataExample.class_name "Permanent link")

```
class_name: str
```

Data example class name.

LabelledRagDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataset "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")[[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")]`

RagDataset class.

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
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
<span class="normal">155</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LabelledRagDataset</span><span class="p">(</span><span class="n">BaseLlamaDataset</span><span class="p">[</span><span class="n">BaseQueryEngine</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""RagDataset class."""</span>

    <span class="n">_example_type</span> <span class="o">=</span> <span class="n">LabelledRagDataExample</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"reference_answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">reference_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
            <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_apredict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledRagDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RagExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async predict RAG example with a query engine."""</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">predictor</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">RagExamplePrediction</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span> <span class="n">contexts</span><span class="o">=</span><span class="p">[</span><span class="n">s</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_predict_example</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">predictor</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">example</span><span class="p">:</span> <span class="n">LabelledRagDataExample</span><span class="p">,</span>
        <span class="n">sleep_time_in_seconds</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RagExamplePrediction</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Predict RAG example with a query engine."""</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_time_in_seconds</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">predictor</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">query</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">RagExamplePrediction</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span> <span class="n">contexts</span><span class="o">=</span><span class="p">[</span><span class="n">s</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_construct_prediction_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predictions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">RagExamplePrediction</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RagPredictionDataset</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Construct prediction dataset."""</span>
        <span class="k">return</span> <span class="n">RagPredictionDataset</span><span class="p">(</span><span class="n">predictions</span><span class="o">=</span><span class="n">predictions</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LabelledRagDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"query"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">query</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_answer"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">reference_answer</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"reference_answer_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">reference_answer_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
        <span class="s2">"query_by"</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="o">.</span><span class="n">query_by</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">],</span>
    <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RagExamplePrediction [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.RagExamplePrediction "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaExamplePrediction](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaExamplePrediction "llama_index.core.llama_dataset.base.BaseLlamaExamplePrediction")`

RAG example prediction class.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `response` | `str` | 
The response generated by the LLM.



 | _required_ |
| `contexts` | `Optional[List[str]]` | 

The retrieved context (text) for generating response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
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
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RagExamplePrediction</span><span class="p">(</span><span class="n">BaseLlamaExamplePrediction</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAG example prediction class.</span>

<span class="sd">    Args:</span>
<span class="sd">        response (str): The response generated by the LLM.</span>
<span class="sd">        contexts (Optional[List[str]]): The retrieved context (text) for generating</span>
<span class="sd">                                        response.</span>
<span class="sd">    """</span>

    <span class="n">response</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The generated (predicted) response that can be compared to a reference (ground-truth) answer."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The contexts in raw text form used to generate the response."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Data example class name."""</span>
        <span class="k">return</span> <span class="s2">"RagExamplePrediction"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.RagExamplePrediction.class_name "Permanent link")

```
class_name: str
```

Data example class name.

RagPredictionDataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.RagPredictionDataset "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPredictionDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaPredictionDataset "llama_index.core.llama_dataset.base.BaseLlamaPredictionDataset")`

RagDataset class.

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 81</span>
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
<span class="normal">100</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RagPredictionDataset</span><span class="p">(</span><span class="n">BaseLlamaPredictionDataset</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RagDataset class."""</span>

    <span class="n">_prediction_type</span> <span class="o">=</span> <span class="n">RagExamplePrediction</span>

    <span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create pandas dataframe."""</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"response"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">response</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
                <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="p">}</span>

        <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"RagPredictionDataset"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.RagPredictionDataset.class_name "Permanent link")

```
class_name: str
```

Class name.

### to\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.RagPredictionDataset.to_pandas "Permanent link")

```
to_pandas() -> DataFrame
```

Create pandas dataframe.

Source code in `llama-index-core/llama_index/core/llama_dataset/rag.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PandasDataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create pandas dataframe."""</span>
    <span class="n">data</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"response"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">response</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
            <span class="s2">"contexts"</span><span class="p">:</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">contexts</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predictions</span><span class="p">],</span>
        <span class="p">}</span>

    <span class="k">return</span> <span class="n">PandasDataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

download\_llama\_dataset [#](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.download_llama_dataset "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
download_llama_dataset(llama_dataset_class: str, download_dir: str, llama_datasets_url: str = LLAMA_DATASETS_URL, llama_datasets_lfs_url: str = LLAMA_DATASETS_LFS_URL, llama_datasets_source_files_tree_url: str = LLAMA_DATASETS_SOURCE_FILES_GITHUB_TREE_URL, show_progress: bool = False, load_documents: bool = True) -> Tuple[Type[[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")], List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]]
```

Download dataset from datasets-LFS and llamahub.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dataset_class` |  | 
The name of the llamadataset class you want to download, such as `PaulGrahamEssayDataset`.



 | _required_ |
| `custom_dir` |  | 

Custom dir name to download loader into (under parent folder).



 | _required_ |
| `custom_path` |  | 

Custom dirpath to download loader into.



 | _required_ |
| `llama_datasets_url` | `str` | 

Url for getting ordinary files from llama\_datasets repo



 | `LLAMA_DATASETS_URL` |
| `llama_datasets_lfs_url` | `str` | 

Url for lfs-traced files llama\_datasets repo



 | `LLAMA_DATASETS_LFS_URL` |
| `llama_datasets_source_files_tree_url` | `str` | 

Url for listing source\_files contents



 | `LLAMA_DATASETS_SOURCE_FILES_GITHUB_TREE_URL` |
| `refresh_cache` |  | 

If true, the local cache will be skipped and the loader will be fetched directly from the remote repo.



 | _required_ |
| `source_files_dirpath` |  | 

The directory for storing source files



 | _required_ |
| `library_path` |  | 

File name of the library file.



 | _required_ |
| `base_file_name` |  | 

The rag dataset json file



 | _required_ |
| `disable_library_cache` |  | 

Boolean to control library cache



 | _required_ |
| `override_path` |  | 

Boolean to control overriding path



 | _required_ |
| `show_progress` | `bool` | 

Boolean for showing progress on downloading source files



 | `False` |
| `load_documents` | `bool` | 

Boolean for whether or not source\_files for LabelledRagDataset should be loaded.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
| `Tuple[Type[[BaseLlamaDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.BaseLlamaDataset "llama_index.core.llama_dataset.base.BaseLlamaDataset")], List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]]` | 
a `BaseLlamaDataset` and a `List[Document]`



 |

Source code in `llama-index-core/llama_index/core/llama_dataset/download.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
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
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
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
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">download_llama_dataset</span><span class="p">(</span>
    <span class="n">llama_dataset_class</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">download_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">llama_datasets_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">LLAMA_DATASETS_URL</span><span class="p">,</span>
    <span class="n">llama_datasets_lfs_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">LLAMA_DATASETS_LFS_URL</span><span class="p">,</span>
    <span class="n">llama_datasets_source_files_tree_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">LLAMA_DATASETS_SOURCE_FILES_GITHUB_TREE_URL</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">load_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseLlamaDataset</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Download dataset from datasets-LFS and llamahub.</span>

<span class="sd">    Args:</span>
<span class="sd">        dataset_class: The name of the llamadataset class you want to download,</span>
<span class="sd">            such as `PaulGrahamEssayDataset`.</span>
<span class="sd">        custom_dir: Custom dir name to download loader into (under parent folder).</span>
<span class="sd">        custom_path: Custom dirpath to download loader into.</span>
<span class="sd">        llama_datasets_url: Url for getting ordinary files from llama_datasets repo</span>
<span class="sd">        llama_datasets_lfs_url: Url for lfs-traced files llama_datasets repo</span>
<span class="sd">        llama_datasets_source_files_tree_url: Url for listing source_files contents</span>
<span class="sd">        refresh_cache: If true, the local cache will be skipped and the</span>
<span class="sd">            loader will be fetched directly from the remote repo.</span>
<span class="sd">        source_files_dirpath: The directory for storing source files</span>
<span class="sd">        library_path: File name of the library file.</span>
<span class="sd">        base_file_name: The rag dataset json file</span>
<span class="sd">        disable_library_cache: Boolean to control library cache</span>
<span class="sd">        override_path: Boolean to control overriding path</span>
<span class="sd">        show_progress: Boolean for showing progress on downloading source files</span>
<span class="sd">        load_documents: Boolean for whether or not source_files for LabelledRagDataset should</span>
<span class="sd">                        be loaded.</span>

<span class="sd">    Returns:</span>
<span class="sd">        a `BaseLlamaDataset` and a `List[Document]`</span>
<span class="sd">    """</span>
    <span class="n">filenames</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">download</span><span class="p">(</span>
        <span class="n">llama_dataset_class</span><span class="p">,</span>
        <span class="n">llama_datasets_url</span><span class="o">=</span><span class="n">llama_datasets_url</span><span class="p">,</span>
        <span class="n">llama_datasets_lfs_url</span><span class="o">=</span><span class="n">llama_datasets_lfs_url</span><span class="p">,</span>
        <span class="n">llama_datasets_source_files_tree_url</span><span class="o">=</span><span class="n">llama_datasets_source_files_tree_url</span><span class="p">,</span>
        <span class="n">refresh_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">custom_path</span><span class="o">=</span><span class="n">download_dir</span><span class="p">,</span>
        <span class="n">library_path</span><span class="o">=</span><span class="s2">"library.json"</span><span class="p">,</span>
        <span class="n">disable_library_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">override_path</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">dataset_filename</span><span class="p">,</span> <span class="n">source_files_dir</span> <span class="o">=</span> <span class="n">filenames</span>
    <span class="n">track_download</span><span class="p">(</span><span class="n">llama_dataset_class</span><span class="p">,</span> <span class="n">MODULE_TYPE</span><span class="o">.</span><span class="n">DATASETS</span><span class="p">)</span>

    <span class="n">dataset</span> <span class="o">=</span> <span class="n">_resolve_dataset_class</span><span class="p">(</span><span class="n">dataset_filename</span><span class="p">)</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="n">dataset_filename</span><span class="p">)</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># for now only rag datasets need to provide the documents</span>
    <span class="c1"># in order to build an index over them</span>
    <span class="k">if</span> <span class="s2">"rag_dataset.json"</span> <span class="ow">in</span> <span class="n">dataset_filename</span> <span class="ow">and</span> <span class="n">load_documents</span><span class="p">:</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">input_dir</span><span class="o">=</span><span class="n">source_files_dir</span><span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="p">(</span><span class="n">dataset</span><span class="p">,</span> <span class="n">documents</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous You](https://docs.llamaindex.ai/en/stable/api_reference/llms/you/)[Next Agent search retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/agent_search_retriever/)
