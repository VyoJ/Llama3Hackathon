Title: Cogniswitch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/

Markdown Content:
Cogniswitch - LlamaIndex


CogniswitchQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/#llama_index.core.query_engine.CogniswitchQueryEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Source code in `llama-index-core/llama_index/core/query_engine/cogniswitch_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
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
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CogniswitchQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cs_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">OAI_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">apiKey</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The required fields.</span>

<span class="sd">        Args:</span>
<span class="sd">            cs_token (str): Cogniswitch token.</span>
<span class="sd">            OAI_token (str): OpenAI token.</span>
<span class="sd">            apiKey (str): Oauth token.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cs_token</span> <span class="o">=</span> <span class="n">cs_token</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">OAI_token</span> <span class="o">=</span> <span class="n">OAI_token</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">apiKey</span> <span class="o">=</span> <span class="n">apiKey</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">knowledge_request_endpoint</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeRequest"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"apiKey"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">apiKey</span><span class="p">,</span>
            <span class="s2">"platformToken"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">cs_token</span><span class="p">,</span>
            <span class="s2">"openAIToken"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">OAI_token</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">query_knowledge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Send a query to the Cogniswitch service and retrieve the response.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): Query to be answered.</span>

<span class="sd">        Returns:</span>
<span class="sd">            dict: Response JSON from the Cogniswitch service.</span>
<span class="sd">        """</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">}</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">knowledge_request_endpoint</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">data</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o"></span> <span class="mi">200</span><span class="p">:</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">answer</span> <span class="o">=</span> <span class="n">resp</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"answer"</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">answer</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">error_message</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"message"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">error_message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Citation](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/)[Next Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/)
