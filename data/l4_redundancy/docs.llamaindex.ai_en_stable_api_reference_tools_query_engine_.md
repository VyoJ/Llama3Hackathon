Title: Query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/

Markdown Content:
Query engine - LlamaIndex


QueryEngineTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/#llama_index.core.tools.query_engine.QueryEngineTool "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")`

Query engine tool.

A tool making use of a query engine.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
A query engine.



 | _required_ |
| `metadata` | `[ToolMetadata](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata "llama_index.core.tools.types.ToolMetadata")` | 

The associated metadata of the query engine.



 | _required_ |

Source code in `llama-index-core/llama_index/core/tools/query_engine.py`

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
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryEngineTool</span><span class="p">(</span><span class="n">AsyncBaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Query engine tool.</span>

<span class="sd">    A tool making use of a query engine.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): A query engine.</span>
<span class="sd">        metadata (ToolMetadata): The associated metadata of the query engine.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">ToolMetadata</span><span class="p">,</span>
        <span class="n">resolve_input_errors</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span> <span class="o">=</span> <span class="n">query_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_resolve_input_errors</span> <span class="o">=</span> <span class="n">resolve_input_errors</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">return_direct</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">resolve_input_errors</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"QueryEngineTool"</span><span class="p">:</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">DEFAULT_NAME</span>
        <span class="n">description</span> <span class="o">=</span> <span class="n">description</span> <span class="ow">or</span> <span class="n">DEFAULT_DESCRIPTION</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span> <span class="n">return_direct</span><span class="o">=</span><span class="n">return_direct</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">resolve_input_errors</span><span class="o">=</span><span class="n">resolve_input_errors</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">query_engine</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span>

    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_query_str</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"input"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
        <span class="n">query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_query_str</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query_engine</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"input"</span><span class="p">:</span> <span class="n">query_str</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_langchain_tool</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LlamaIndexTool"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.langchain_helpers.agents.tools</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">IndexToolConfig</span><span class="p">,</span>
            <span class="n">LlamaIndexTool</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">tool_config</span> <span class="o">=</span> <span class="n">IndexToolConfig</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">LlamaIndexTool</span><span class="o">.</span><span class="n">from_tool_config</span><span class="p">(</span><span class="n">tool_config</span><span class="o">=</span><span class="n">tool_config</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_query_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">args</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">elif</span> <span class="n">kwargs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="s2">"input"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="c1"># NOTE: this assumes our default function schema of `input`</span>
            <span class="n">query_str</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s2">"input"</span><span class="p">]</span>
        <span class="k">elif</span> <span class="n">kwargs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_resolve_input_errors</span><span class="p">:</span>
            <span class="n">query_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot call query engine without specifying `input` parameter."</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">query_str</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Python file](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/)[Next Query plan](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/)
