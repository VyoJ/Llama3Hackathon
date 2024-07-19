Title: You - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/

Markdown Content:
You - LlamaIndex


YouRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/#llama_index.retrievers.you.YouRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Retriever for You.com's Search and News API.

[API reference](https://documentation.you.com/api-reference/)

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_key` | `Optional[str]` | 
you.com API key, if `YDC_API_KEY` is not set in the environment



 | `None` |
| `endpoint` | `Literal['search', 'news']` | 

you.com endpoints



 | `'search'` |
| `num_web_results` | `Optional[int]` | 

The max number of web results to return, must be under 20



 | `None` |
| `safesearch` | `Optional[Literal['off', 'moderate', 'strict']]` | 

Safesearch settings, one of "off", "moderate", "strict", defaults to moderate



 | `None` |
| `country` | `Optional[str]` | 

Country code, ex: 'US' for United States, see API reference for more info



 | `None` |
| `search_lang` | `Optional[str]` | 

(News API) Language codes, ex: 'en' for English, see API reference for more info



 | `None` |
| `ui_lang` | `Optional[str]` | 

(News API) User interface language for the response, ex: 'en' for English, see API reference for more info



 | `None` |
| `spellcheck` | `Optional[bool]` | 

(News API) Whether to spell check query or not, defaults to True



 | `None` |

Source code in `llama-index-integrations/retrievers/llama-index-retrievers-you/llama_index/retrievers/you/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">YouRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retriever for You.com's Search and News API.</span>

<span class="sd">    [API reference](https://documentation.you.com/api-reference/)</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key: you.com API key, if `YDC_API_KEY` is not set in the environment</span>
<span class="sd">        endpoint: you.com endpoints</span>
<span class="sd">        num_web_results: The max number of web results to return, must be under 20</span>
<span class="sd">        safesearch: Safesearch settings, one of "off", "moderate", "strict", defaults to moderate</span>
<span class="sd">        country: Country code, ex: 'US' for United States, see API reference for more info</span>
<span class="sd">        search_lang: (News API) Language codes, ex: 'en' for English, see API reference for more info</span>
<span class="sd">        ui_lang: (News API) User interface language for the response, ex: 'en' for English, see API reference for more info</span>
<span class="sd">        spellcheck: (News API) Whether to spell check query or not, defaults to True</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s2">"search"</span><span class="p">,</span> <span class="s2">"news"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"search"</span><span class="p">,</span>
        <span class="n">num_web_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">safesearch</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Literal</span><span class="p">[</span><span class="s2">"off"</span><span class="p">,</span> <span class="s2">"moderate"</span><span class="p">,</span> <span class="s2">"strict"</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">country</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">search_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ui_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">spellcheck</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># Should deprecate `YOU_API_KEY` in favour of `YDC_API_KEY` for standardization purposes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"YOU_API_KEY"</span><span class="p">)</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"YDC_API_KEY"</span><span class="p">]</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">endpoint</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="s2">"search"</span><span class="p">,</span> <span class="s2">"news"</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'`endpoint` must be either "search" or "news"'</span><span class="p">)</span>

        <span class="c1"># Raise warning if News API-specific fields are set but endpoint is not "news"</span>
        <span class="k">if</span> <span class="n">endpoint</span> <span class="o">!=</span> <span class="s2">"news"</span><span class="p">:</span>
            <span class="n">news_api_fields</span> <span class="o">=</span> <span class="p">(</span><span class="n">search_lang</span><span class="p">,</span> <span class="n">ui_lang</span><span class="p">,</span> <span class="n">spellcheck</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">news_api_fields</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">field</span><span class="p">:</span>
                    <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                        <span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"News API-specific field '</span><span class="si">{</span><span class="n">field</span><span class="si">}</span><span class="s2">' is set but `</span><span class="si">{</span><span class="n">endpoint</span><span class="si">=}</span><span class="s2">`. "</span>
                            <span class="s2">"This will have no effect."</span>
                        <span class="p">),</span>
                        <span class="ne">UserWarning</span><span class="p">,</span>
                    <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">endpoint</span> <span class="o">=</span> <span class="n">endpoint</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_web_results</span> <span class="o">=</span> <span class="n">num_web_results</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">safesearch</span> <span class="o">=</span> <span class="n">safesearch</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">country</span> <span class="o">=</span> <span class="n">country</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">search_lang</span> <span class="o">=</span> <span class="n">search_lang</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ui_lang</span> <span class="o">=</span> <span class="n">ui_lang</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">spellcheck</span> <span class="o">=</span> <span class="n">spellcheck</span>

    <span class="k">def</span> <span class="nf">_generate_params</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"safesearch"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">safesearch</span><span class="p">,</span> <span class="s2">"country"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">country</span><span class="p">}</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">endpoint</span> <span class="o"></span> <span class="s2">"news"</span><span class="p">:</span>
            <span class="n">params</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
                <span class="n">q</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">count</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_web_results</span><span class="p">,</span>
                <span class="n">search_lang</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">search_lang</span><span class="p">,</span>
                <span class="n">ui_lang</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ui_lang</span><span class="p">,</span>
                <span class="n">spellcheck</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">spellcheck</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="c1"># Remove `None` values</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">params</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">v</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"X-API-Key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">}</span>
        <span class="n">params</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_params</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"https://api.ydc-index.io/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">endpoint</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">endpoint</span> <span class="o">==</span> <span class="s2">"search"</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">]:</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">TextNode</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">hit</span><span class="p">[</span><span class="s2">"snippets"</span><span class="p">]),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>  <span class="c1"># news endpoint</span>
            <span class="k">for</span> <span class="n">article</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[</span><span class="s2">"news"</span><span class="p">][</span><span class="s2">"results"</span><span class="p">]:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">article</span><span class="p">[</span><span class="s2">"description"</span><span class="p">],</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"url"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span> <span class="s2">"age"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"age"</span><span class="p">]},</span>
                <span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="mf">1.0</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Videodb](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/schema/)
