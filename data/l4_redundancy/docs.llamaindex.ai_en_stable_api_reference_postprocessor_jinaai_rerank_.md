Title: Jinaai rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/

Markdown Content:
Jinaai rerank - LlamaIndex


JinaRerank [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/#llama_index.postprocessor.jinaai_rerank.JinaRerank "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-jinaai-rerank/llama_index/postprocessor/jinaai_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JinaRerank</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The JinaAI API key."</span><span class="p">)</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"jina-reranker-v1-base-en"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The model to use when calling Jina AI API"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Top N nodes to return."</span><span class="p">)</span>

    <span class="n">_session</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"jina-reranker-v1-base-en"</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">top_n</span><span class="o">=</span><span class="n">top_n</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">get_from_param_or_env</span><span class="p">(</span><span class="s2">"api_key"</span><span class="p">,</span> <span class="n">api_key</span><span class="p">,</span> <span class="s2">"JINAAI_API_KEY"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">headers</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
            <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="s2">"Accept-Encoding"</span><span class="p">:</span> <span class="s2">"identity"</span><span class="p">}</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"JinaRerank"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">ReRankStartEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span>
                <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing query bundle in extra info."</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">RERANKING</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">nodes</span><span class="p">,</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">MODEL_NAME</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">TOP_K</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">texts</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
            <span class="p">]</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>  <span class="c1"># type: ignore</span>
                <span class="n">API_URL</span><span class="p">,</span>
                <span class="n">json</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="s2">"documents"</span><span class="p">:</span> <span class="n">texts</span><span class="p">,</span>
                    <span class="s2">"model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
                    <span class="s2">"top_n"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">)</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="k">if</span> <span class="s2">"results"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">resp</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="n">resp</span><span class="p">[</span><span class="s2">"detail"</span><span class="p">])</span>

            <span class="n">results</span> <span class="o">=</span> <span class="n">resp</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]</span>

            <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
                <span class="n">new_node_with_score</span> <span class="o">=</span> <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">nodes</span><span class="p">[</span><span class="n">result</span><span class="p">[</span><span class="s2">"index"</span><span class="p">]]</span><span class="o">.</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"relevance_score"</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_node_with_score</span><span class="p">)</span>
            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">NODES</span><span class="p">:</span> <span class="n">new_nodes</span><span class="p">})</span>

        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">ReRankEndEvent</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">new_nodes</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/)[Next Keyword](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/)
