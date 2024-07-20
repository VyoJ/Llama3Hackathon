Title: Openalex - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/

Markdown Content:
Openalex - LlamaIndex


Init file.

OpenAlexReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/#llama_index.readers.openalex.OpenAlexReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

This class is used to search and import data from OpenAlex.

#### Parameters[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/#llama_index.readers.openalex.OpenAlexReader--parameters "Permanent link")

email : str Email address to use for OpenAlex API

#### Attributes:[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/#llama_index.readers.openalex.OpenAlexReader--attributes "Permanent link")

Works : pyalex.Works pyalex.Works object pyalex : pyalex pyalex object

Source code in `llama-index-integrations/readers/llama-index-readers-openalex/llama_index/readers/openalex/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAlexReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This class is used to search and import data from OpenAlex.</span>

<span class="sd">    Parameters</span>
<span class="sd">    ----------</span>
<span class="sd">    email : str</span>
<span class="sd">        Email address to use for OpenAlex API</span>

<span class="sd">    Attributes:</span>
<span class="sd">    ----------</span>
<span class="sd">    Works : pyalex.Works</span>
<span class="sd">        pyalex.Works object</span>
<span class="sd">    pyalex : pyalex</span>
<span class="sd">        pyalex object</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">email</span> <span class="o">=</span> <span class="n">email</span>

    <span class="k">def</span> <span class="nf">_search_openalex</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">fields</span><span class="p">):</span>
        <span class="n">base_url</span> <span class="o">=</span> <span class="s2">"https://api.openalex.org/works?search="</span>
        <span class="n">fields_param</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;select=</span><span class="si">{</span><span class="n">fields</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">email_param</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;mailto=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">full_url</span> <span class="o">=</span> <span class="n">base_url</span> <span class="o">+</span> <span class="n">query</span> <span class="o">+</span> <span class="n">fields_param</span> <span class="o">+</span> <span class="n">email_param</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">full_url</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
            <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>  <span class="c1"># Check if request is successful</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>  <span class="c1"># Parse JSON data</span>
            <span class="k">if</span> <span class="s2">"error"</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"API returned error: </span><span class="si">{</span><span class="n">data</span><span class="p">[</span><span class="s1">'error'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">data</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">HTTPError</span> <span class="k">as</span> <span class="n">http_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"HTTP error occurred: </span><span class="si">{</span><span class="n">http_error</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">request_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error occurred: </span><span class="si">{</span><span class="n">request_error</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">value_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">value_error</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_fulltext_search_openalex</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">fields</span><span class="p">):</span>
        <span class="n">base_url</span> <span class="o">=</span> <span class="s2">"https://api.openalex.org/works?filter=fulltext.search:"</span>
        <span class="n">fields_param</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;select=</span><span class="si">{</span><span class="n">fields</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">email_param</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;mailto=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">full_url</span> <span class="o">=</span> <span class="n">base_url</span> <span class="o">+</span> <span class="n">query</span> <span class="o">+</span> <span class="n">fields_param</span> <span class="o">+</span> <span class="n">email_param</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">full_url</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
            <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>  <span class="c1"># Check if request is successful</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>  <span class="c1"># Parse JSON data</span>
            <span class="k">if</span> <span class="s2">"error"</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"API returned error: </span><span class="si">{</span><span class="n">data</span><span class="p">[</span><span class="s1">'error'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">data</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">HTTPError</span> <span class="k">as</span> <span class="n">http_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"HTTP error occurred: </span><span class="si">{</span><span class="n">http_error</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">request_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error occurred: </span><span class="si">{</span><span class="n">request_error</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">value_error</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">value_error</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_invert_abstract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">inv_index</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">inv_index</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">l_inv</span> <span class="o">=</span> <span class="p">[(</span><span class="n">w</span><span class="p">,</span> <span class="n">p</span><span class="p">)</span> <span class="k">for</span> <span class="n">w</span><span class="p">,</span> <span class="n">pos</span> <span class="ow">in</span> <span class="n">inv_index</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">pos</span><span class="p">]</span>
            <span class="k">return</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">l_inv</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">full_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">fields</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">fields</span> <span class="o">=</span> <span class="s2">"title,abstract_inverted_index,publication_year,keywords,authorships,primary_location"</span>

        <span class="k">if</span> <span class="n">full_text</span><span class="p">:</span>
            <span class="n">works</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fulltext_search_openalex</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">works</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_openalex</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">work</span> <span class="ow">in</span> <span class="n">works</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="k">if</span> <span class="n">work</span><span class="p">[</span><span class="s2">"abstract_inverted_index"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">abstract</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_invert_abstract</span><span class="p">(</span><span class="n">work</span><span class="p">[</span><span class="s2">"abstract_inverted_index"</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">abstract</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">title</span> <span class="o">=</span> <span class="n">work</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"title"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="c1"># concat title and abstract</span>
            <span class="k">if</span> <span class="n">abstract</span> <span class="ow">and</span> <span class="n">title</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">abstract</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="n">abstract</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">primary_location</span> <span class="o">=</span> <span class="n">work</span><span class="p">[</span><span class="s2">"primary_location"</span><span class="p">][</span><span class="s2">"source"</span><span class="p">][</span><span class="s2">"display_name"</span><span class="p">]</span>
            <span class="k">except</span> <span class="p">(</span><span class="ne">KeyError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">):</span>
                <span class="n">primary_location</span> <span class="o">=</span> <span class="kc">None</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">work</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"title"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"keywords"</span><span class="p">:</span> <span class="n">work</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"keywords"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"primary_location"</span><span class="p">:</span> <span class="n">primary_location</span><span class="p">,</span>
                <span class="s2">"publication_year"</span><span class="p">:</span> <span class="n">work</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"publication_year"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"authorships"</span><span class="p">:</span> <span class="p">[</span>
                    <span class="n">item</span><span class="p">[</span><span class="s2">"author"</span><span class="p">][</span><span class="s2">"display_name"</span><span class="p">]</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">work</span><span class="p">[</span><span class="s2">"authorships"</span><span class="p">]</span>
                <span class="p">],</span>
            <span class="p">}</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Obsidian](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/)[Next Openapi](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/)
