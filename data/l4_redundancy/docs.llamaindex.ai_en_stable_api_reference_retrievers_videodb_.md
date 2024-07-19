Title: Videodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/

Markdown Content:
Videodb - LlamaIndex


VideoDBRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/#llama_index.retrievers.videodb.VideoDBRetriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-videodb/llama_index/retrievers/videodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VideoDBRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">video</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">score_threshold</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.2</span><span class="p">,</span>
        <span class="n">result_threshold</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">search_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">SearchType</span><span class="o">.</span><span class="n">semantic</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates a new VideoDB Retriever."""</span>
        <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"VIDEO_DB_API_KEY"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span>
                <span class="s2">"No API key provided. Set an API key either as an environment variable (VIDEO_DB_API_KEY) or pass it as an argument."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="n">base_url</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">video</span> <span class="o">=</span> <span class="n">video</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="o">=</span> <span class="n">collection</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">score_threshold</span> <span class="o">=</span> <span class="n">score_threshold</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">result_threshold</span> <span class="o">=</span> <span class="n">result_threshold</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">search_type</span> <span class="o">=</span> <span class="n">search_type</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"api_key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"base_url"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span>
        <span class="n">conn</span> <span class="o">=</span> <span class="n">connect</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">video</span><span class="p">:</span>
            <span class="n">coll</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="p">)</span>
            <span class="n">video</span> <span class="o">=</span> <span class="n">coll</span><span class="o">.</span><span class="n">get_video</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">video</span><span class="p">)</span>
            <span class="n">search_res</span> <span class="o">=</span> <span class="n">video</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">search_type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">search_type</span><span class="p">,</span>
                <span class="n">score_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">score_threshold</span><span class="p">,</span>
                <span class="n">result_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">result_threshold</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">coll</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">get_collection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="p">)</span>
            <span class="n">search_res</span> <span class="o">=</span> <span class="n">coll</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">search_type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">search_type</span><span class="p">,</span>
                <span class="n">score_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">score_threshold</span><span class="p">,</span>
                <span class="n">result_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">result_threshold</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">collection_id</span> <span class="o">=</span> <span class="n">search_res</span><span class="o">.</span><span class="n">collection_id</span>
        <span class="k">for</span> <span class="n">shot</span> <span class="ow">in</span> <span class="n">search_res</span><span class="o">.</span><span class="n">get_shots</span><span class="p">():</span>
            <span class="n">score</span> <span class="o">=</span> <span class="n">shot</span><span class="o">.</span><span class="n">search_score</span>
            <span class="n">textnode</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">shot</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"collection_id"</span><span class="p">:</span> <span class="n">collection_id</span><span class="p">,</span>
                    <span class="s2">"video_id"</span><span class="p">:</span> <span class="n">shot</span><span class="o">.</span><span class="n">video_id</span><span class="p">,</span>
                    <span class="s2">"length"</span><span class="p">:</span> <span class="n">shot</span><span class="o">.</span><span class="n">video_length</span><span class="p">,</span>
                    <span class="s2">"title"</span><span class="p">:</span> <span class="n">shot</span><span class="o">.</span><span class="n">video_title</span><span class="p">,</span>
                    <span class="s2">"start"</span><span class="p">:</span> <span class="n">shot</span><span class="o">.</span><span class="n">start</span><span class="p">,</span>
                    <span class="s2">"end"</span><span class="p">:</span> <span class="n">shot</span><span class="o">.</span><span class="n">end</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">textnode</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vector](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/)[Next You](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/)
