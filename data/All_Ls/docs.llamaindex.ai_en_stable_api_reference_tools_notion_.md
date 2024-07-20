Title: Notion - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/

Markdown Content:
Notion - LlamaIndex


Notion tool spec.

NotionToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/#llama_index.tools.notion.NotionToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Notion tool spec.

Currently a simple wrapper around the data loader. TODO: add more methods to the Notion spec.

Source code in `llama-index-integrations/tools/llama-index-tools-notion/llama_index/tools/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 31</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NotionToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Notion tool spec.</span>

<span class="sd">    Currently a simple wrapper around the data loader.</span>
<span class="sd">    TODO: add more methods to the Notion spec.</span>

<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"load_data"</span><span class="p">,</span> <span class="s2">"search_data"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">integration_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reader</span> <span class="o">=</span> <span class="n">NotionPageReader</span><span class="p">(</span><span class="n">integration_token</span><span class="o">=</span><span class="n">integration_token</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_fn_schema_from_fn_name</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">fn_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">spec_functions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Return map from function name."""</span>
        <span class="k">if</span> <span class="n">fn_name</span> <span class="o"></span> <span class="s2">"search_data"</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">NotionSearchDataSchema</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid function name: </span><span class="si">{</span><span class="n">fn_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">page_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">database_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Loads content from a set of page ids or a database id.</span>

<span class="sd">        Don't use this endpoint if you don't know the page ids or database id.</span>

<span class="sd">        """</span>
        <span class="n">page_ids</span> <span class="o">=</span> <span class="n">page_ids</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">page_ids</span><span class="o">=</span><span class="n">page_ids</span><span class="p">,</span> <span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">search_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">direction</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">timestamp</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="nb">property</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">page_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Search a list of relevant pages.</span>

<span class="sd">        Contains metadata for each page (but not the page content).</span>

<span class="sd">        """</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
            <span class="s2">"page_size"</span><span class="p">:</span> <span class="n">page_size</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">direction</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">timestamp</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="n">direction</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">][</span><span class="s2">"direction"</span><span class="p">]</span> <span class="o">=</span> <span class="n">direction</span>
            <span class="k">if</span> <span class="n">timestamp</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">][</span><span class="s2">"timestamp"</span><span class="p">]</span> <span class="o">=</span> <span class="n">timestamp</span>

        <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">property</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">][</span><span class="s2">"value"</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
            <span class="k">if</span> <span class="nb">property</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">][</span><span class="s2">"property"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">property</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_fn\_schema\_from\_fn\_name [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/#llama_index.tools.notion.NotionToolSpec.get_fn_schema_from_fn_name "Permanent link")

```
get_fn_schema_from_fn_name(fn_name: str, spec_functions: Optional[List[SPEC_FUNCTION_TYPE]] = None) -> Optional[Type[BaseModel]]
```

Return map from function name.

Source code in `llama-index-integrations/tools/llama-index-tools-notion/llama_index/tools/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_fn_schema_from_fn_name</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">fn_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">spec_functions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">SPEC_FUNCTION_TYPE</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Return map from function name."""</span>
    <span class="k">if</span> <span class="n">fn_name</span> <span class="o"></span> <span class="s2">"search_data"</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">NotionSearchDataSchema</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid function name: </span><span class="si">{</span><span class="n">fn_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/#llama_index.tools.notion.NotionToolSpec.load_data "Permanent link")

```
load_data(page_ids: Optional[List[str]] = None, database_id: Optional[str] = None) -> str
```

Loads content from a set of page ids or a database id.

Don't use this endpoint if you don't know the page ids or database id.

Source code in `llama-index-integrations/tools/llama-index-tools-notion/llama_index/tools/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">page_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">database_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Loads content from a set of page ids or a database id.</span>

<span class="sd">    Don't use this endpoint if you don't know the page ids or database id.</span>

<span class="sd">    """</span>
    <span class="n">page_ids</span> <span class="o">=</span> <span class="n">page_ids</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">page_ids</span><span class="o">=</span><span class="n">page_ids</span><span class="p">,</span> <span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### search\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/#llama_index.tools.notion.NotionToolSpec.search_data "Permanent link")

```
search_data(query: str, direction: Optional[str] = None, timestamp: Optional[str] = None, value: Optional[str] = None, property: Optional[str] = None, page_size: int = 100) -> str
```

Search a list of relevant pages.

Contains metadata for each page (but not the page content).

Source code in `llama-index-integrations/tools/llama-index-tools-notion/llama_index/tools/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 68</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">search_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">timestamp</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="nb">property</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">page_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Search a list of relevant pages.</span>

<span class="sd">    Contains metadata for each page (but not the page content).</span>

<span class="sd">    """</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
        <span class="s2">"page_size"</span><span class="p">:</span> <span class="n">page_size</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">if</span> <span class="n">direction</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">timestamp</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">direction</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">][</span><span class="s2">"direction"</span><span class="p">]</span> <span class="o">=</span> <span class="n">direction</span>
        <span class="k">if</span> <span class="n">timestamp</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"sort"</span><span class="p">][</span><span class="s2">"timestamp"</span><span class="p">]</span> <span class="o">=</span> <span class="n">timestamp</span>

    <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">property</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">][</span><span class="s2">"value"</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
        <span class="k">if</span> <span class="nb">property</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"filter"</span><span class="p">][</span><span class="s2">"property"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">property</span>

    <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">headers</span><span class="p">)</span>
    <span class="n">response_json</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">response_json</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/)[Next Ondemand loader](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/)
