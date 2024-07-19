Title: Function - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/function/

Markdown Content:
Function - LlamaIndex


FunctionTool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")`

Function Tool.

A tool that takes in a function.

Source code in `llama-index-core/llama_index/core/tools/function_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 24</span>
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
<span class="normal">136</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FunctionTool</span><span class="p">(</span><span class="n">AsyncBaseTool</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Function Tool.</span>

<span class="sd">    A tool that takes in a function.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="n">ToolMetadata</span><span class="p">,</span>
        <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_fn</span> <span class="o">=</span> <span class="n">fn</span>
        <span class="k">if</span> <span class="n">async_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_async_fn</span> <span class="o">=</span> <span class="n">async_fn</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_async_fn</span> <span class="o">=</span> <span class="n">sync_to_async</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_fn</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">metadata</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">return_direct</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">fn_schema</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_metadata</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ToolMetadata</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"FunctionTool"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">tool_metadata</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">fn</span><span class="o">.</span><span class="vm">__name__</span>
            <span class="n">docstring</span> <span class="o">=</span> <span class="n">fn</span><span class="o">.</span><span class="vm">__doc__</span>
            <span class="n">description</span> <span class="o">=</span> <span class="n">description</span> <span class="ow">or</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">name</span><span class="si">}{</span><span class="n">signature</span><span class="p">(</span><span class="n">fn</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">docstring</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">if</span> <span class="n">fn_schema</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">fn_schema</span> <span class="o">=</span> <span class="n">create_schema_from_function</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">fn</span><span class="p">,</span> <span class="n">additional_fields</span><span class="o">=</span><span class="kc">None</span>
                <span class="p">)</span>
            <span class="n">tool_metadata</span> <span class="o">=</span> <span class="n">ToolMetadata</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
                <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
                <span class="n">fn_schema</span><span class="o">=</span><span class="n">fn_schema</span><span class="p">,</span>
                <span class="n">return_direct</span><span class="o">=</span><span class="n">return_direct</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">fn</span><span class="o">=</span><span class="n">fn</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">tool_metadata</span><span class="p">,</span> <span class="n">async_fn</span><span class="o">=</span><span class="n">async_fn</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Metadata."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">fn</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Function."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fn</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">async_fn</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncCallable</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Async function."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_fn</span>

    <span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Call."""</span>
        <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"args"</span><span class="p">:</span> <span class="n">args</span><span class="p">,</span> <span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">kwargs</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">tool_output</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Call."""</span>
        <span class="n">tool_output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"args"</span><span class="p">:</span> <span class="n">args</span><span class="p">,</span> <span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">kwargs</span><span class="p">},</span>
            <span class="n">raw_output</span><span class="o">=</span><span class="n">tool_output</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_langchain_tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Tool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To langchain tool."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Tool</span>

        <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
            <span class="n">langchain_tool_kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">Tool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
            <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">,</span>
            <span class="n">coroutine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">,</span>
            <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_langchain_structured_tool</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StructuredTool"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""To langchain structured tool."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">StructuredTool</span>

        <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
            <span class="n">langchain_tool_kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">StructuredTool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
            <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">,</span>
            <span class="n">coroutine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">,</span>
            <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### metadata `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.metadata "Permanent link")

```
metadata: [ToolMetadata](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata "llama_index.core.tools.types.ToolMetadata")
```

Metadata.

### fn `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.fn "Permanent link")

```
fn: Callable[..., Any]
```

Function.

### async\_fn `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.async_fn "Permanent link")

```
async_fn: AsyncCallable
```

Async function.

### call [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.call "Permanent link")

```
call(*args: Any, **kwargs: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

Call.

Source code in `llama-index-core/llama_index/core/tools/function_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">call</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Call."""</span>
    <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
        <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"args"</span><span class="p">:</span> <span class="n">args</span><span class="p">,</span> <span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">kwargs</span><span class="p">},</span>
        <span class="n">raw_output</span><span class="o">=</span><span class="n">tool_output</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### acall `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.acall "Permanent link")

```
acall(*args: Any, **kwargs: Any) -> [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.types.ToolOutput")
```

Call.

Source code in `llama-index-core/llama_index/core/tools/function_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Call."""</span>
    <span class="n">tool_output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ToolOutput</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
        <span class="n">tool_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"args"</span><span class="p">:</span> <span class="n">args</span><span class="p">,</span> <span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">kwargs</span><span class="p">},</span>
        <span class="n">raw_output</span><span class="o">=</span><span class="n">tool_output</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_langchain\_tool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.to_langchain_tool "Permanent link")

```
to_langchain_tool(**langchain_tool_kwargs: Any) -> Tool
```

To langchain tool.

Source code in `llama-index-core/llama_index/core/tools/function_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
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
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_langchain_tool</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Tool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To langchain tool."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Tool</span>

    <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
        <span class="n">langchain_tool_kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">Tool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
        <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">,</span>
        <span class="n">coroutine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_langchain\_structured\_tool [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/#llama_index.core.tools.function_tool.FunctionTool.to_langchain_structured_tool "Permanent link")

```
to_langchain_structured_tool(**langchain_tool_kwargs: Any) -> StructuredTool
```

To langchain structured tool.

Source code in `llama-index-core/llama_index/core/tools/function_tool.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">122</span>
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
<span class="normal">136</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_langchain_structured_tool</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StructuredTool"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""To langchain structured tool."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">StructuredTool</span>

    <span class="n">langchain_tool_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_langchain_tool_kwargs</span><span class="p">(</span>
        <span class="n">langchain_tool_kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">StructuredTool</span><span class="o">.</span><span class="n">from_function</span><span class="p">(</span>
        <span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">,</span>
        <span class="n">coroutine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">,</span>
        <span class="o">**</span><span class="n">langchain_tool_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/)[Next Google](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/)
