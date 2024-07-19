Title: Metaphor - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/

Markdown Content:
Metaphor - LlamaIndex


MetaphorToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Metaphor tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
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
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetaphorToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Metaphor tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s2">"search"</span><span class="p">,</span>
        <span class="s2">"retrieve_documents"</span><span class="p">,</span>
        <span class="s2">"search_and_retrieve_documents"</span><span class="p">,</span>
        <span class="s2">"find_similar"</span><span class="p">,</span>
        <span class="s2">"current_date"</span><span class="p">,</span>
    <span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="kn">from</span> <span class="nn">metaphor_python</span> <span class="kn">import</span> <span class="n">Metaphor</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">Metaphor</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">user_agent</span><span class="o">=</span><span class="s2">"llama-index"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">search</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">include_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">exclude_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Metaphor allows you to use a natural language query to search the internet.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): A natural language query phrased as an answer for what the link provides, ie: "This is the latest news about space:"</span>
<span class="sd">            num_results (Optional[int]): Number of results to return. Defaults to 10.</span>
<span class="sd">            include_domains (Optional[List(str)]): A list of top level domains like ["wsj.com"] to limit the search to specific sites.</span>
<span class="sd">            exclude_domains (Optional[List(str)]): Top level domains to exclude.</span>
<span class="sd">            start_published_date (Optional[str]): A date string like "2020-06-15". Get the date from `current_date`</span>
<span class="sd">            end_published_date (Optional[str]): End date string</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span>
            <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
            <span class="n">include_domains</span><span class="o">=</span><span class="n">include_domains</span><span class="p">,</span>
            <span class="n">exclude_domains</span><span class="o">=</span><span class="n">exclude_domains</span><span class="p">,</span>
            <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
            <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
            <span class="n">use_autoprompt</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[Metaphor Tool] Autoprompt: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">autoprompt_string</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span><span class="p">}</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">retrieve_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieve a list of document summaries returned by `metaphor_search`, using the ID field.</span>

<span class="sd">        Args:</span>
<span class="sd">            ids (List(str)): the ids of the documents to retrieve</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_contents</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">con</span><span class="o">.</span><span class="n">extract</span><span class="p">)</span> <span class="k">for</span> <span class="n">con</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">contents</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">find_similar</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieve a list of similar documents to a given url.</span>

<span class="sd">        Args:</span>
<span class="sd">            url (str): The web page to find similar results of</span>
<span class="sd">            num_results (Optional[int]): Number of results to return. Default 3.</span>
<span class="sd">            start_published_date (Optional[str]): A date string like "2020-06-15"</span>
<span class="sd">            end_published_date (Optional[str]): End date string</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">find_similar</span><span class="p">(</span>
            <span class="n">url</span><span class="p">,</span>
            <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
            <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
            <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span><span class="p">}</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">search_and_retrieve_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">include_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">exclude_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Combines the functionality of `search` and `retrieve_documents`.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): the natural language query</span>
<span class="sd">            num_results (Optional[int]): Number of results. Defaults to 10.</span>
<span class="sd">            include_domains (Optional[List(str)]): A list of top level domains to search, like ["wsj.com"]</span>
<span class="sd">            exclude_domains (Optional[List(str)]): Top level domains to exclude.</span>
<span class="sd">            start_published_date (Optional[str]): A date string like "2020-06-15".</span>
<span class="sd">            end_published_date (Optional[str]): End date string</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span>
            <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
            <span class="n">include_domains</span><span class="o">=</span><span class="n">include_domains</span><span class="p">,</span>
            <span class="n">exclude_domains</span><span class="o">=</span><span class="n">exclude_domains</span><span class="p">,</span>
            <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
            <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
            <span class="n">use_autoprompt</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[Metaphor Tool] Autoprompt: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">autoprompt_string</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span><span class="p">]</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_contents</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">extract</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="o">.</span><span class="n">contents</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">current_date</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        A function to return todays date.</span>
<span class="sd">        Call this before any other functions that take timestamps as an argument.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### search [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec.search "Permanent link")

```
search(query: str, num_results: Optional[int] = 10, include_domains: Optional[List[str]] = None, exclude_domains: Optional[List[str]] = None, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None) -> str
```

Metaphor allows you to use a natural language query to search the internet.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
A natural language query phrased as an answer for what the link provides, ie: "This is the latest news about space:"



 | _required_ |
| `num_results` | `Optional[int]` | 

Number of results to return. Defaults to 10.



 | `10` |
| `include_domains` | `Optional[List(str)]` | 

A list of top level domains like \["wsj.com"\] to limit the search to specific sites.



 | `None` |
| `exclude_domains` | `Optional[List(str)]` | 

Top level domains to exclude.



 | `None` |
| `start_published_date` | `Optional[str]` | 

A date string like "2020-06-15". Get the date from `current_date`



 | `None` |
| `end_published_date` | `Optional[str]` | 

End date string



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">search</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">include_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">exclude_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Metaphor allows you to use a natural language query to search the internet.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): A natural language query phrased as an answer for what the link provides, ie: "This is the latest news about space:"</span>
<span class="sd">        num_results (Optional[int]): Number of results to return. Defaults to 10.</span>
<span class="sd">        include_domains (Optional[List(str)]): A list of top level domains like ["wsj.com"] to limit the search to specific sites.</span>
<span class="sd">        exclude_domains (Optional[List(str)]): Top level domains to exclude.</span>
<span class="sd">        start_published_date (Optional[str]): A date string like "2020-06-15". Get the date from `current_date`</span>
<span class="sd">        end_published_date (Optional[str]): End date string</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="n">query</span><span class="p">,</span>
        <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
        <span class="n">include_domains</span><span class="o">=</span><span class="n">include_domains</span><span class="p">,</span>
        <span class="n">exclude_domains</span><span class="o">=</span><span class="n">exclude_domains</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
        <span class="n">use_autoprompt</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[Metaphor Tool] Autoprompt: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">autoprompt_string</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span><span class="p">}</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec.retrieve_documents "Permanent link")

```
retrieve_documents(ids: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Retrieve a list of document summaries returned by `metaphor_search`, using the ID field.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ids` | `List(str` | 
the ids of the documents to retrieve



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieve a list of document summaries returned by `metaphor_search`, using the ID field.</span>

<span class="sd">    Args:</span>
<span class="sd">        ids (List(str)): the ids of the documents to retrieve</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_contents</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">con</span><span class="o">.</span><span class="n">extract</span><span class="p">)</span> <span class="k">for</span> <span class="n">con</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">contents</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### find\_similar [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec.find_similar "Permanent link")

```
find_similar(url: str, num_results: Optional[int] = 3, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None) -> str
```

Retrieve a list of similar documents to a given url.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `str` | 
The web page to find similar results of



 | _required_ |
| `num_results` | `Optional[int]` | 

Number of results to return. Default 3.



 | `3` |
| `start_published_date` | `Optional[str]` | 

A date string like "2020-06-15"



 | `None` |
| `end_published_date` | `Optional[str]` | 

End date string



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">74</span>
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
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span>
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">find_similar</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
    <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieve a list of similar documents to a given url.</span>

<span class="sd">    Args:</span>
<span class="sd">        url (str): The web page to find similar results of</span>
<span class="sd">        num_results (Optional[int]): Number of results to return. Default 3.</span>
<span class="sd">        start_published_date (Optional[str]): A date string like "2020-06-15"</span>
<span class="sd">        end_published_date (Optional[str]): End date string</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">find_similar</span><span class="p">(</span>
        <span class="n">url</span><span class="p">,</span>
        <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span><span class="p">}</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### search\_and\_retrieve\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec.search_and_retrieve_documents "Permanent link")

```
search_and_retrieve_documents(query: str, num_results: Optional[int] = 10, include_domains: Optional[List[str]] = None, exclude_domains: Optional[List[str]] = None, start_published_date: Optional[str] = None, end_published_date: Optional[str] = None) -> str
```

Combines the functionality of `search` and `retrieve_documents`.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
the natural language query



 | _required_ |
| `num_results` | `Optional[int]` | 

Number of results. Defaults to 10.



 | `10` |
| `include_domains` | `Optional[List(str)]` | 

A list of top level domains to search, like \["wsj.com"\]



 | `None` |
| `exclude_domains` | `Optional[List(str)]` | 

Top level domains to exclude.



 | `None` |
| `start_published_date` | `Optional[str]` | 

A date string like "2020-06-15".



 | `None` |
| `end_published_date` | `Optional[str]` | 

End date string



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">101</span>
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
<span class="normal">134</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">search_and_retrieve_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">num_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">include_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">exclude_domains</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">start_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_published_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Combines the functionality of `search` and `retrieve_documents`.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): the natural language query</span>
<span class="sd">        num_results (Optional[int]): Number of results. Defaults to 10.</span>
<span class="sd">        include_domains (Optional[List(str)]): A list of top level domains to search, like ["wsj.com"]</span>
<span class="sd">        exclude_domains (Optional[List(str)]): Top level domains to exclude.</span>
<span class="sd">        start_published_date (Optional[str]): A date string like "2020-06-15".</span>
<span class="sd">        end_published_date (Optional[str]): End date string</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="n">query</span><span class="p">,</span>
        <span class="n">num_results</span><span class="o">=</span><span class="n">num_results</span><span class="p">,</span>
        <span class="n">include_domains</span><span class="o">=</span><span class="n">include_domains</span><span class="p">,</span>
        <span class="n">exclude_domains</span><span class="o">=</span><span class="n">exclude_domains</span><span class="p">,</span>
        <span class="n">start_published_date</span><span class="o">=</span><span class="n">start_published_date</span><span class="p">,</span>
        <span class="n">end_published_date</span><span class="o">=</span><span class="n">end_published_date</span><span class="p">,</span>
        <span class="n">use_autoprompt</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[Metaphor Tool] Autoprompt: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">autoprompt_string</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">results</span><span class="p">]</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_contents</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">extract</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="o">.</span><span class="n">contents</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### current\_date [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/#llama_index.tools.metaphor.MetaphorToolSpec.current_date "Permanent link")

```
current_date()
```

A function to return todays date. Call this before any other functions that take timestamps as an argument.

Source code in `llama-index-integrations/tools/llama-index-tools-metaphor/llama_index/tools/metaphor/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">current_date</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A function to return todays date.</span>
<span class="sd">    Call this before any other functions that take timestamps as an argument.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Load and search](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/)[Next Multion](https://docs.llamaindex.ai/en/stable/api_reference/tools/multion/)
