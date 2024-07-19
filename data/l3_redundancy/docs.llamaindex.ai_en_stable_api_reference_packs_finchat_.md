Title: Finchat - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/finchat/

Markdown Content:
Finchat - LlamaIndex


FinanceChatPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/finchat/#llama_index.packs.finchat.FinanceChatPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-finchat/llama_index/packs/finchat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">162</span>
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
<span class="normal">375</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FinanceChatPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">polygon_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">finnhub_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">alpha_vantage_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">newsapi_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">openai_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">postgres_db_uri</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">gpt_model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4-0613"</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="n">gpt_model_name</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">openai_api_key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">db_tool_spec</span> <span class="o">=</span> <span class="n">SQLDatabaseToolSpec</span><span class="p">(</span><span class="n">uri</span><span class="o">=</span><span class="n">postgres_db_uri</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fin_tool_spec</span> <span class="o">=</span> <span class="n">FinanceAgentToolSpec</span><span class="p">(</span>
            <span class="n">polygon_api_key</span><span class="p">,</span> <span class="n">finnhub_api_key</span><span class="p">,</span> <span class="n">alpha_vantage_api_key</span><span class="p">,</span> <span class="n">newsapi_api_key</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">db_table_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_tool_spec</span><span class="o">.</span><span class="n">get_table_info</span><span class="p">()</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">construct_prefix_db_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_table_info</span><span class="p">)</span>
        <span class="c1"># add some role play in the system .</span>
        <span class="n">database_agent</span> <span class="o">=</span> <span class="n">OpenAIAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="n">tool</span>
                <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_tool_spec</span><span class="o">.</span><span class="n">to_tool_list</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s2">"run_sql_query"</span>
            <span class="p">],</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">database_agent_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">database_agent</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"database_agent"</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">""""</span>
<span class="s2">                This agent analyzes a text query and add further explanations and thoughts to help a data scientist who has access to following tables:</span>

<span class="s2">                </span><span class="si">{table_info}</span>

<span class="s2">                Be concise and do not lose any information about original query while passing to the data scientist.</span>
<span class="s2">                """</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">fin_api_agent</span> <span class="o">=</span> <span class="n">OpenAIAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">fin_tool_spec</span><span class="o">.</span><span class="n">to_tool_list</span><span class="p">(),</span>
            <span class="n">system_prompt</span><span class="o">=</span><span class="sa">f</span><span class="s2">"""</span>
<span class="s2">                You are a helpful AI financial assistant designed to understand the intent of the user query and then use relevant tools/apis to help answer it.</span>
<span class="s2">                You can use more than one tool/api only if needed, but final response should be concise and relevant. If you are not able to find</span>
<span class="s2">                relevant tool/api, respond respectfully suggesting that you don't know. Think step by step"""</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">fin_api_agent_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">fin_api_agent</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"fin_api_agent"</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="sa">f</span><span class="s2">"""</span>
<span class="s2">                This agent has access to another agent which can access certain open APIs to provide information based on user query.</span>
<span class="s2">                Analyze the query and add any information if needed which can help to decide which API to call.</span>
<span class="s2">                Be concise and do not lose any information about original query.</span>
<span class="s2">                """</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">fin_hierarchical_agent</span> <span class="o">=</span> <span class="n">OpenAIAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="p">[</span><span class="n">database_agent_tool</span><span class="p">,</span> <span class="n">fin_api_agent_tool</span><span class="p">],</span>
            <span class="n">system_prompt</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">                You are a specialized financial assistant with access to certain tools which can access open APIs and SP500 companies database containing information on</span>
<span class="s2">                daily opening price, closing price, high, low, volume, reported earnings, estimated earnings since 2010 to 2023. Before answering query you should check</span>
<span class="s2">                if the question can be answered via querying the database or using specific open APIs. If you try to find answer via querying database first and it did</span>
<span class="s2">                not work out, think if you can use other tool APIs available before replying gracefully.</span>
<span class="s2">                """</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">construct_prefix_db_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table_info</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">system_prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        You are a smart data scientist working in a reputed trading firm like Jump Trading developing automated trading algorithms. Take a deep breathe and think</span>
<span class="s2">        step by step to design queries over a SQL database.</span>

<span class="s2">        Here is a complete description of tables in SQL database you have access to:</span>

<span class="s2">        </span><span class="si">{</span><span class="n">table_info</span><span class="si">}</span>

<span class="s2">        Use responses to past questions also to guide you.</span>


<span class="s2">        """</span>

        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">))</span>

        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"What is the average price of Google in the month of July in 2023"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        SELECT AVG(close) AS AvgPrice</span>
<span class="s2">        FROM stock_data</span>
<span class="s2">        WHERE stock = 'GOOG'</span>
<span class="s2">            AND date &gt;= '2023-07-01'</span>
<span class="s2">            AND date &lt;= '2023-07-31';</span>
<span class="s2">        """</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"Which stock has the maximum </span><span class="si">% c</span><span class="s2">hange in any month in 2023"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="c1"># prefix_messages.append(ChatMessage(role="user", content="Which stocks gave more than 2% return constantly in month of July from past 5 years"))</span>
        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        WITH MonthlyPrices AS (</span>
<span class="s2">            SELECT</span>
<span class="s2">                stock,</span>
<span class="s2">                EXTRACT(YEAR FROM date) AS year,</span>
<span class="s2">                EXTRACT(MONTH FROM date) AS month,</span>
<span class="s2">                FIRST_VALUE(close) OVER (PARTITION BY stock, EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date) ORDER BY date ASC) AS opening_price,</span>
<span class="s2">                LAST_VALUE(close) OVER (PARTITION BY stock, EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date) ORDER BY date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS closing_price</span>
<span class="s2">            FROM</span>
<span class="s2">                stock_data</span>
<span class="s2">            WHERE</span>
<span class="s2">                EXTRACT(YEAR FROM date) = 2023</span>
<span class="s2">        ),</span>
<span class="s2">        PercentageChanges AS (</span>
<span class="s2">            SELECT</span>
<span class="s2">                stock,</span>
<span class="s2">                year,</span>
<span class="s2">                month,</span>
<span class="s2">                CASE</span>
<span class="s2">                    WHEN opening_rice IS NULL OR closing_price IS NULL THEN NULL</span>
<span class="s2">                    WHEN opening_price = 0 THEN NULL</span>
<span class="s2">                    ELSE ((closing_price - opening_price) / opening_price) * 100</span>
<span class="s2">                END AS pct</span>
<span class="s2">            FROM</span>
<span class="s2">                MonthlyPrices</span>
<span class="s2">        )</span>
<span class="s2">        SELECT *</span>
<span class="s2">        FROM</span>
<span class="s2">            PercentageChanges</span>
<span class="s2">        WHERE pct IS NOT NULL</span>
<span class="s2">        ORDER BY</span>
<span class="s2">            pct DESC</span>
<span class="s2">        LIMIT 1;</span>
<span class="s2">        """</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"How many times Microsoft beat earnings estimates in 2022"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        SELECT</span>
<span class="s2">            COUNT(*)</span>
<span class="s2">        FROM</span>
<span class="s2">            earnings</span>
<span class="s2">        WHERE</span>
<span class="s2">            stock = 'MSFT' AND reported &gt; estimated and EXTRACT(YEAR FROM date) = 2022</span>
<span class="s2">        """</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"Which stocks have beaten earnings estimate by more than 1$ consecutively from last 4 reportings?"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">prefix_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"""</span>
<span class="s2">        WITH RankedEarnings AS(</span>
<span class="s2">            SELECT</span>
<span class="s2">                stock,</span>
<span class="s2">                date,</span>
<span class="s2">                reported,</span>
<span class="s2">                estimated,</span>
<span class="s2">                RANK() OVER (PARTITION BY stock ORDER BY date DESC) as ranking</span>
<span class="s2">            FROM</span>
<span class="s2">                earnings</span>
<span class="s2">        )</span>
<span class="s2">        SELECT</span>
<span class="s2">            stock</span>
<span class="s2">        FROM</span>
<span class="s2">            RankedEarnings</span>
<span class="s2">        WHERE</span>
<span class="s2">            ranking &lt;= 4 AND reported - estimated &gt; 1</span>
<span class="s2">        GROUP BY</span>
<span class="s2">            stock</span>
<span class="s2">        HAVING COUNT(*) = 4</span>
<span class="s2">        """</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">prefix_messages</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fin_hierarchical_agent</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Evaluator benchmarker](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/)[Next Fusion retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/)
