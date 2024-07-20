Title: Chatgpt plugin - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/

Markdown Content:
Chatgpt plugin - LlamaIndex


ChatGPTRetrievalPluginReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/#llama_index.readers.chatgpt_plugin.ChatGPTRetrievalPluginReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

ChatGPT Retrieval Plugin reader.

Source code in `llama-index-integrations/readers/llama-index-readers-chatgpt-plugin/llama_index/readers/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatGPTRetrievalPluginReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ChatGPT Retrieval Plugin reader."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">endpoint_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bearer_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Retry</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Chatgpt Retrieval Plugin."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span> <span class="o">=</span> <span class="n">endpoint_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span> <span class="o">=</span> <span class="n">bearer_token</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"BEARER_TOKEN"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retries</span> <span class="o">=</span> <span class="n">retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_batch_size</span> <span class="o">=</span> <span class="n">batch_size</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_s</span><span class="o">.</span><span class="n">mount</span><span class="p">(</span><span class="s2">"http://"</span><span class="p">,</span> <span class="n">HTTPAdapter</span><span class="p">(</span><span class="n">max_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_retries</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">separate_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from ChatGPT Retrieval Plugin."""</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
        <span class="n">queries</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span> <span class="s2">"top_k"</span><span class="p">:</span> <span class="n">top_k</span><span class="p">}]</span>
        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/query"</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"queries"</span><span class="p">:</span> <span class="n">queries</span><span class="p">}</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">query_result</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">query_result</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
                <span class="n">result_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
                <span class="n">result_txt</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
                <span class="n">result_embedding</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"embedding"</span><span class="p">]</span>
                <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">result_txt</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">result_id</span><span class="p">,</span>
                    <span class="n">embedding</span><span class="o">=</span><span class="n">result_embedding</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

            <span class="c1"># NOTE: there should only be one query</span>
            <span class="k">break</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/#llama_index.readers.chatgpt_plugin.ChatGPTRetrievalPluginReader.load_data "Permanent link")

```
load_data(query: str, top_k: int = 10, separate_documents: bool = True, **kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from ChatGPT Retrieval Plugin.

Source code in `llama-index-integrations/readers/llama-index-readers-chatgpt-plugin/llama_index/readers/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">separate_documents</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from ChatGPT Retrieval Plugin."""</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bearer_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
    <span class="n">queries</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span> <span class="s2">"top_k"</span><span class="p">:</span> <span class="n">top_k</span><span class="p">}]</span>
    <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_endpoint_url</span><span class="si">}</span><span class="s2">/query"</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="p">{</span><span class="s2">"queries"</span><span class="p">:</span> <span class="n">queries</span><span class="p">}</span>
    <span class="p">)</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">query_result</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"results"</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">query_result</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="n">result_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
            <span class="n">result_txt</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
            <span class="n">result_embedding</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"embedding"</span><span class="p">]</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result_txt</span><span class="p">,</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">result_id</span><span class="p">,</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">result_embedding</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="c1"># NOTE: there should only be one query</span>
        <span class="k">break</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Boarddocs](https://docs.llamaindex.ai/en/stable/api_reference/readers/boarddocs/)[Next Chroma](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/)
