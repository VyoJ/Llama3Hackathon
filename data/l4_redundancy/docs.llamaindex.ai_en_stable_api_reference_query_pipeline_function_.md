Title: Function - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/

Markdown Content:
Function - LlamaIndex


Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Query component that takes in an arbitrary function.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/function.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 35</span>
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
<span class="normal">116</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FnComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Query component that takes in an arbitrary function."""</span>

    <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Function to run."</span><span class="p">)</span>
    <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Async function to run. If not provided, will run `fn`."</span>
    <span class="p">)</span>
    <span class="n">output_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"output"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Output key for component output."</span>
    <span class="p">)</span>

    <span class="n">_req_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_opt_params</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span>
        <span class="n">async_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">req_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">opt_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"output"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="c1"># determine parameters</span>
        <span class="n">default_req_params</span><span class="p">,</span> <span class="n">default_opt_params</span> <span class="o">=</span> <span class="n">get_parameters</span><span class="p">(</span><span class="n">fn</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">req_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">req_params</span> <span class="o">=</span> <span class="n">default_req_params</span>
        <span class="k">if</span> <span class="n">opt_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">opt_params</span> <span class="o">=</span> <span class="n">default_opt_params</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span> <span class="o">=</span> <span class="n">req_params</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span> <span class="o">=</span> <span class="n">opt_params</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">fn</span><span class="o">=</span><span class="n">fn</span><span class="p">,</span> <span class="n">async_fn</span><span class="o">=</span><span class="n">async_fn</span><span class="p">,</span> <span class="n">output_key</span><span class="o">=</span><span class="n">output_key</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="c1"># TODO: implement</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># check that all required parameters are present</span>
        <span class="n">missing_params</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="nb">input</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">missing_params</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Missing required parameters: </span><span class="si">{</span><span class="n">missing_params</span><span class="si">}</span><span class="s2">. "</span>
                <span class="sa">f</span><span class="s2">"Input keys: </span><span class="si">{</span><span class="nb">input</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="c1"># check that no extra parameters are present</span>
        <span class="n">extra_params</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">input</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span>
        <span class="k">if</span> <span class="n">extra_params</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Extra parameters: </span><span class="si">{</span><span class="n">extra_params</span><span class="si">}</span><span class="s2">. "</span> <span class="sa">f</span><span class="s2">"Input keys: </span><span class="si">{</span><span class="nb">input</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">output_key</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">output_key</span><span class="p">:</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_fn</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_req_params</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_opt_params</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">({</span><span class="bp">self</span><span class="o">.</span><span class="n">output_key</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/#llama_index.core.query_pipeline.components.function.FnComponent.input_keys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/#llama_index.core.query_pipeline.components.function.FnComponent.output_keys "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/#llama_index.core.query_pipeline.components.function.FnComponent.set_callback_manager "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/query_pipeline/components/function.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/)
