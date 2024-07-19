Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/schema/

Markdown Content:
Index - LlamaIndex


Base schema for data structures.

BaseComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base component object to capture class names.

Source code in `llama-index-core/llama_index/core/schema.py`

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
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseComponent</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base component object to capture class names."""</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="nd">@staticmethod</span>
        <span class="k">def</span> <span class="nf">schema_extra</span><span class="p">(</span><span class="n">schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">model</span><span class="p">:</span> <span class="s2">"BaseComponent"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">            </span><span class="sd">"""Add class name to schema."""</span>
            <span class="n">schema</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="s2">"Class Name"</span><span class="p">,</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"string"</span><span class="p">,</span>
                <span class="s2">"default"</span><span class="p">:</span> <span class="n">model</span><span class="o">.</span><span class="n">class_name</span><span class="p">(),</span>
            <span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get the class name, used as a unique ID in serialization.</span>

<span class="sd">        This provides a key that makes serialization robust against actual class</span>
<span class="sd">        name changes.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="s2">"base_component"</span>

    <span class="k">def</span> <span class="nf">json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_json</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">data</span><span class="p">[</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">data</span>

    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">state</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__getstate__</span><span class="p">()</span>

        <span class="c1"># tiktoken is not pickleable</span>
        <span class="c1"># state["__dict__"] = self.dict()</span>
        <span class="n">state</span><span class="p">[</span><span class="s2">"__dict__"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"tokenizer"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="c1"># remove local functions</span>
        <span class="n">keys_to_remove</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">state</span><span class="p">[</span><span class="s2">"__dict__"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">key</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"_fn"</span><span class="p">):</span>
                <span class="n">keys_to_remove</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
            <span class="k">if</span> <span class="s2">"&lt;lambda&gt;"</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">val</span><span class="p">):</span>
                <span class="n">keys_to_remove</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">keys_to_remove</span><span class="p">:</span>
            <span class="n">state</span><span class="p">[</span><span class="s2">"__dict__"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="c1"># remove private attributes -- kind of dangerous</span>
        <span class="n">state</span><span class="p">[</span><span class="s2">"__private_attribute_values__"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">return</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Use the __dict__ and __init__ method to set state</span>
        <span class="c1"># so that all variable initialize</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">**</span><span class="n">state</span><span class="p">[</span><span class="s2">"__dict__"</span><span class="p">])</span>  <span class="c1"># type: ignore</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="c1"># Fall back to the default __setstate__ method</span>
            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__setstate__</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">data</span><span class="p">[</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">data</span>

    <span class="k">def</span> <span class="nf">to_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="c1"># TODO: return type here not supported by current mypy version</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">data</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"class_name"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">data</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">data_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">data_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### Config [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent.Config "Permanent link")

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">schema_extra</span><span class="p">(</span><span class="n">schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">model</span><span class="p">:</span> <span class="s2">"BaseComponent"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add class name to schema."""</span>
        <span class="n">schema</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"title"</span><span class="p">:</span> <span class="s2">"Class Name"</span><span class="p">,</span>
            <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"string"</span><span class="p">,</span>
            <span class="s2">"default"</span><span class="p">:</span> <span class="n">model</span><span class="o">.</span><span class="n">class_name</span><span class="p">(),</span>
        <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

#### schema\_extra `staticmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent.Config.schema_extra "Permanent link")

```
schema_extra(schema: Dict[str, Any], model: [BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")) -> None
```

Add class name to schema.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@staticmethod</span>
<span class="k">def</span> <span class="nf">schema_extra</span><span class="p">(</span><span class="n">schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">model</span><span class="p">:</span> <span class="s2">"BaseComponent"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add class name to schema."""</span>
    <span class="n">schema</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">][</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"title"</span><span class="p">:</span> <span class="s2">"Class Name"</span><span class="p">,</span>
        <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"string"</span><span class="p">,</span>
        <span class="s2">"default"</span><span class="p">:</span> <span class="n">model</span><span class="o">.</span><span class="n">class_name</span><span class="p">(),</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent.class_name "Permanent link")

```
class_name() -> str
```

Get the class name, used as a unique ID in serialization.

This provides a key that makes serialization robust against actual class name changes.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Get the class name, used as a unique ID in serialization.</span>

<span class="sd">    This provides a key that makes serialization robust against actual class</span>
<span class="sd">    name changes.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="s2">"base_component"</span>
</code></pre></div></td></tr></tbody></table>

TransformComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`, `DispatcherSpanMixin`

Base class for transform components.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
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
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TransformComponent</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">,</span> <span class="n">DispatcherSpanMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base class for transform components."""</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Transform nodes."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Async transform nodes."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### acall `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent.acall "Permanent link")

```
acall(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Async transform nodes.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">acall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"BaseNode"</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Async transform nodes."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

NodeRelationship [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeRelationship "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Node relationships used in `BaseNode` class.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `SOURCE` |  | 
The node is the source document.



 |
| `PREVIOUS` |  | 

The node is the previous node in the document.



 |
| `NEXT` |  | 

The node is the next node in the document.



 |
| `PARENT` |  | 

The node is the parent node in the document.



 |
| `CHILD` |  | 

The node is a child node in the document.



 |

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NodeRelationship</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Node relationships used in `BaseNode` class.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        SOURCE: The node is the source document.</span>
<span class="sd">        PREVIOUS: The node is the previous node in the document.</span>
<span class="sd">        NEXT: The node is the next node in the document.</span>
<span class="sd">        PARENT: The node is the parent node in the document.</span>
<span class="sd">        CHILD: The node is a child node in the document.</span>

<span class="sd">    """</span>

    <span class="n">SOURCE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">PREVIOUS</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">NEXT</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">PARENT</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">CHILD</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

BaseNode [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "Permanent link")
--------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`

Base node Object.

Generic abstract interface for retrievable nodes

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseNode</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base node Object.</span>

<span class="sd">    Generic abstract interface for retrievable nodes</span>

<span class="sd">    """</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">allow_population_by_field_name</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="c1"># hash is computed on local field, during the validation process</span>
        <span class="n">validate_assignment</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Unique ID of the node."</span>
    <span class="p">)</span>
    <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Embedding of the node."</span>
    <span class="p">)</span>

<span class="w">    </span><span class="sd">""""</span>
<span class="sd">    metadata fields</span>
<span class="sd">    - injected as part of the text shown to LLMs as context</span>
<span class="sd">    - injected as part of the text for generating embeddings</span>
<span class="sd">    - used by vector DBs for metadata filtering</span>

<span class="sd">    """</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"A flat dictionary of metadata fields"</span><span class="p">,</span>
        <span class="n">alias</span><span class="o">=</span><span class="s2">"extra_info"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">excluded_embed_metadata_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Metadata keys that are excluded from text for the embed model."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">excluded_llm_metadata_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Metadata keys that are excluded from text for the LLM."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">relationships</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="p">,</span> <span class="n">RelatedNodeType</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"A mapping of relationships to other node information."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get Object type."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get object content."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_metadata_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Metadata string."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set the content of the node."""</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">hash</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get hash of node."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">node_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span>

    <span class="nd">@node_id</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">node_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="n">value</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">source_node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelatedNodeInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Source object node.</span>

<span class="sd">        Extracted from the relationships field.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">relation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">relation</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Source object must be a single RelatedNodeInfo object"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">relation</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">prev_node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelatedNodeInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Prev node."""</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">PREVIOUS</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">relation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">PREVIOUS</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">relation</span><span class="p">,</span> <span class="n">RelatedNodeInfo</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Previous object must be a single RelatedNodeInfo object"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">relation</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">next_node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelatedNodeInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Next node."""</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">NEXT</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">relation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">NEXT</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">relation</span><span class="p">,</span> <span class="n">RelatedNodeInfo</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Next object must be a single RelatedNodeInfo object"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">relation</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">parent_node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelatedNodeInfo</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parent node."""</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">PARENT</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">relation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">PARENT</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">relation</span><span class="p">,</span> <span class="n">RelatedNodeInfo</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Parent object must be a single RelatedNodeInfo object"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">relation</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">child_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">RelatedNodeInfo</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Child nodes."""</span>
        <span class="k">if</span> <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">CHILD</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="n">relation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relationships</span><span class="p">[</span><span class="n">NodeRelationship</span><span class="o">.</span><span class="n">CHILD</span><span class="p">]</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">relation</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Child objects must be a list of RelatedNodeInfo objects."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">relation</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">ref_doc_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Deprecated: Get ref doc id."""</span>
        <span class="n">source_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">source_node</span>
        <span class="k">if</span> <span class="n">source_node</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">source_node</span><span class="o">.</span><span class="n">node_id</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">extra_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""TODO: DEPRECATED: Extra info."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">source_text_truncated</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="n">TRUNCATE_LENGTH</span>
        <span class="p">)</span>
        <span class="n">source_text_wrapped</span> <span class="o">=</span> <span class="n">textwrap</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Text: </span><span class="si">{</span><span class="n">source_text_truncated</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">WRAP_WIDTH</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"Node ID: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_id</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">source_text_wrapped</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">get_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get embedding.</span>

<span class="sd">        Errors if embedding is None.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"embedding not set."</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span>

    <span class="k">def</span> <span class="nf">as_related_node_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RelatedNodeInfo</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get node as RelatedNodeInfo."""</span>
        <span class="k">return</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span>
            <span class="n">node_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
            <span class="n">node_type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_type</span><span class="p">(),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
            <span class="nb">hash</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">hash</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### embedding `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.embedding "Permanent link")

```
embedding: Optional[List[float]] = Field(default=None, description='Embedding of the node.')
```

" metadata fields - injected as part of the text shown to LLMs as context - injected as part of the text for generating embeddings - used by vector DBs for metadata filtering

### hash `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.hash "Permanent link")

```
hash: str
```

Get hash of node.

### source\_node `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.source_node "Permanent link")

```
source_node: Optional[RelatedNodeInfo]
```

Source object node.

Extracted from the relationships field.

### prev\_node `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.prev_node "Permanent link")

```
prev_node: Optional[RelatedNodeInfo]
```

Prev node.

### next\_node `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.next_node "Permanent link")

```
next_node: Optional[RelatedNodeInfo]
```

Next node.

### parent\_node `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.parent_node "Permanent link")

```
parent_node: Optional[RelatedNodeInfo]
```

Parent node.

### child\_nodes `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.child_nodes "Permanent link")

```
child_nodes: Optional[List[RelatedNodeInfo]]
```

Child nodes.

### ref\_doc\_id `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.ref_doc_id "Permanent link")

```
ref_doc_id: Optional[str]
```

Deprecated: Get ref doc id.

### extra\_info `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.extra_info "Permanent link")

```
extra_info: Dict[str, Any]
```

TODO: DEPRECATED: Extra info.

### get\_type `abstractmethod` `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.get_type "Permanent link")

```
get_type() -> str
```

Get Object type.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get Object type."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_content `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.get_content "Permanent link")

```
get_content(metadata_mode: MetadataMode = MetadataMode.ALL) -> str
```

Get object content.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get object content."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_metadata\_str `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.get_metadata_str "Permanent link")

```
get_metadata_str(mode: MetadataMode = MetadataMode.ALL) -> str
```

Metadata string.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_metadata_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Metadata string."""</span>
</code></pre></div></td></tr></tbody></table>

### set\_content `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.set_content "Permanent link")

```
set_content(value: Any) -> None
```

Set the content of the node.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">set_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the content of the node."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_embedding [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.get_embedding "Permanent link")

```
get_embedding() -> List[float]
```

Get embedding.

Errors if embedding is None.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get embedding.</span>

<span class="sd">    Errors if embedding is None.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"embedding not set."</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span>
</code></pre></div></td></tr></tbody></table>

### as\_related\_node\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode.as_related_node_info "Permanent link")

```
as_related_node_info() -> RelatedNodeInfo
```

Get node as RelatedNodeInfo.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_related_node_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RelatedNodeInfo</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get node as RelatedNodeInfo."""</span>
    <span class="k">return</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span>
        <span class="n">node_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span>
        <span class="n">node_type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_type</span><span class="p">(),</span>
        <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
        <span class="nb">hash</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">hash</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

TextNode [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "Permanent link")
--------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")`

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TextNode</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">):</span>
    <span class="n">text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Text content of the node."</span><span class="p">)</span>
    <span class="n">mimetype</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"text/plain"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"MIME type of the node content."</span>
    <span class="p">)</span>
    <span class="n">start_char_idx</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Start char index of the node."</span>
    <span class="p">)</span>
    <span class="n">end_char_idx</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"End char index of the node."</span>
    <span class="p">)</span>
    <span class="n">text_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_TEXT_NODE_TMPL</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Template for how text is formatted, with </span><span class="si">{content}</span><span class="s2"> and "</span>
            <span class="s2">"</span><span class="si">{metadata_str}</span><span class="s2"> placeholders."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">metadata_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_METADATA_TMPL</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Template for how metadata is formatted, with </span><span class="si">{key}</span><span class="s2"> and "</span>
            <span class="s2">"</span><span class="si">{value}</span><span class="s2"> placeholders."</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">metadata_seperator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Separator between metadata fields when converting to string."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"TextNode"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">hash</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">doc_identity</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">)</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">sha256</span><span class="p">(</span><span class="n">doc_identity</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">,</span> <span class="s2">"surrogatepass"</span><span class="p">))</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">())</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get Object type."""</span>
        <span class="k">return</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">TEXT</span>

    <span class="k">def</span> <span class="nf">get_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get object content."""</span>
        <span class="n">metadata_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_metadata_str</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="n">metadata_mode</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">metadata_str</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata_str</span><span class="o">=</span><span class="n">metadata_str</span>
        <span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_metadata_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">ALL</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Metadata info string."""</span>
        <span class="k">if</span> <span class="n">mode</span> <span class="o"></span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">usable_metadata_keys</span><span class="p">:</span>
                    <span class="n">usable_metadata_keys</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">mode</span> <span class="o"></span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">""</span>

    <span class="n">usable_metadata_keys</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
    <span class="k">if</span> <span class="n">mode</span> <span class="o"></span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">usable_metadata_keys</span><span class="p">:</span>
                <span class="n">usable_metadata_keys</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata_seperator</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
        <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">metadata_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">usable_metadata_keys</span>
        <span class="p">]</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set\_content [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode.set_content "Permanent link")

```
set_content(value: str) -> None
```

Set the content of the node.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set the content of the node."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">value</span>
</code></pre></div></td></tr></tbody></table>

### get\_node\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode.get_node_info "Permanent link")

```
get_node_info() -> Dict[str, Any]
```

Get node info.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_node_info</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get node info."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"start"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_char_idx</span><span class="p">,</span> <span class="s2">"end"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">end_char_idx</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

ImageNode [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageNode "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

Bases: `[TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")`

Node with image.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageNode</span><span class="p">(</span><span class="n">TextNode</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Node with image."""</span>

    <span class="c1"># TODO: store reference instead of actual image</span>
    <span class="c1"># base64 encoded image str</span>
    <span class="n">image</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">image_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">image_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">image_mimetype</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">text_embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Text embedding of image node, if text field is filled out"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">IMAGE</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ImageNode"</span>

    <span class="k">def</span> <span class="nf">resolve_image</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImageType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Resolve an image such that PIL can read it."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">image</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">base64</span>

            <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">image</span><span class="p">))</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_path</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_path</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># load image from URL</span>
            <span class="kn">import</span> <span class="nn">requests</span>

            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">image_url</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No image found in node."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### resolve\_image [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageNode.resolve_image "Permanent link")

```
resolve_image() -> ImageType
```

Resolve an image such that PIL can read it.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">resolve_image</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ImageType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Resolve an image such that PIL can read it."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">image</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">base64</span>

        <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">image</span><span class="p">))</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_path</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_path</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># load image from URL</span>
        <span class="kn">import</span> <span class="nn">requests</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">image_url</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">BytesIO</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No image found in node."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

IndexNode [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.IndexNode "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

Bases: `[TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")`

Node with reference to any object.

This can include other indices, query engines, retrievers.

This can also include other nodes (though this is overlapping with `relationships` on the Node class).

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IndexNode</span><span class="p">(</span><span class="n">TextNode</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Node with reference to any object.</span>

<span class="sd">    This can include other indices, query engines, retrievers.</span>

<span class="sd">    This can also include other nodes (though this is overlapping with `relationships`</span>
<span class="sd">    on the Node class).</span>

<span class="sd">    """</span>

    <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.storage.docstore.utils</span> <span class="kn">import</span> <span class="n">doc_to_json</span>

        <span class="n">data</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">obj</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">data</span><span class="p">[</span><span class="s2">"obj"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
                <span class="n">data</span><span class="p">[</span><span class="s2">"obj"</span><span class="p">]</span> <span class="o">=</span> <span class="n">doc_to_json</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="p">,</span> <span class="n">BaseModel</span><span class="p">):</span>
                <span class="n">data</span><span class="p">[</span><span class="s2">"obj"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">data</span><span class="p">[</span><span class="s2">"obj"</span><span class="p">]</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"IndexNode obj is not serializable: "</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">obj</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">data</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_text_node</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">,</span>
        <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"IndexNode"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create index node from text node."""</span>
        <span class="c1"># copy all attributes from text node, add index id</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="o">**</span><span class="n">node</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span>
            <span class="n">index_id</span><span class="o">=</span><span class="n">index_id</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="c1"># TODO: return type here not supported by current mypy version</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Self</span><span class="p">:</span>  <span class="c1"># type: ignore</span>
        <span class="n">output</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="n">obj</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"obj"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">parsed_obj</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">parsed_obj</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">obj</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.storage.docstore.utils</span> <span class="kn">import</span> <span class="n">json_to_doc</span>

            <span class="c1"># check if its a node, else assume stringable</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">parsed_obj</span> <span class="o">=</span> <span class="n">json_to_doc</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="n">parsed_obj</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">obj</span><span class="p">))</span>

        <span class="n">output</span><span class="o">.</span><span class="n">obj</span> <span class="o">=</span> <span class="n">parsed_obj</span>

        <span class="k">return</span> <span class="n">output</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">INDEX</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"IndexNode"</span>
</code></pre></div></td></tr></tbody></table>

### from\_text\_node `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.IndexNode.from_text_node "Permanent link")

```
from_text_node(node: [TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode"), index_id: str) -> [IndexNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.IndexNode "llama_index.core.schema.IndexNode")
```

Create index node from text node.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_text_node</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">,</span>
    <span class="n">index_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"IndexNode"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create index node from text node."""</span>
    <span class="c1"># copy all attributes from text node, add index id</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="o">**</span><span class="n">node</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span>
        <span class="n">index_id</span><span class="o">=</span><span class="n">index_id</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

NodeWithScore [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NodeWithScore</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">):</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span>
    <span class="n">score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">score_str</span> <span class="o">=</span> <span class="s2">"None"</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">score</span><span class="si">:</span><span class="s2"> 0.3f</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="si">}</span><span class="se">\n</span><span class="s2">Score: </span><span class="si">{</span><span class="n">score_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">get_score</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get score."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">raise_error</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Score not set."</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">return</span> <span class="mf">0.0</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"NodeWithScore"</span>

    <span class="c1">##### pass through methods to BaseNode #####</span>
    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">node_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">id_</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">id_</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">text</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Node must be a TextNode to get text."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">embedding</span>

    <span class="k">def</span> <span class="nf">get_text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Node must be a TextNode to get text."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">metadata_mode</span><span class="p">:</span> <span class="n">MetadataMode</span> <span class="o">=</span> <span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">metadata_mode</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_score [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore.get_score "Permanent link")

```
get_score(raise_error: bool = False) -> float
```

Get score.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_score</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_error</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get score."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">raise_error</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Score not set."</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">0.0</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span>
</code></pre></div></td></tr></tbody></table>

Document [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "Permanent link")
--------------------------------------------------------------------------------------------------------------------------

Bases: `[TextNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TextNode "llama_index.core.schema.TextNode")`

Generic interface for a data document.

This document connects to data sources.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Document</span><span class="p">(</span><span class="n">TextNode</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Generic interface for a data document.</span>

<span class="sd">    This document connects to data sources.</span>

<span class="sd">    """</span>

    <span class="c1"># TODO: A lot of backwards compatibility logic here, clean up</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Unique ID of the node."</span><span class="p">,</span>
        <span class="n">alias</span><span class="o">=</span><span class="s2">"doc_id"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">_compat_fields</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="s2">"id_"</span><span class="p">,</span> <span class="s2">"extra_info"</span><span class="p">:</span> <span class="s2">"metadata"</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get Document type."""</span>
        <span class="k">return</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">DOCUMENT</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">doc_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get document ID."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">source_text_truncated</span> <span class="o">=</span> <span class="n">truncate_text</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="n">TRUNCATE_LENGTH</span>
        <span class="p">)</span>
        <span class="n">source_text_wrapped</span> <span class="o">=</span> <span class="n">textwrap</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Text: </span><span class="si">{</span><span class="n">source_text_truncated</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">WRAP_WIDTH</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"Doc ID: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">doc_id</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">source_text_wrapped</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">get_doc_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""TODO: Deprecated: Get document ID."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span>

    <span class="k">def</span> <span class="fm">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_compat_fields</span><span class="p">:</span>
            <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_compat_fields</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__setattr__</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_langchain_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LCDocument"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct to LangChain document format."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Document</span> <span class="k">as</span> <span class="n">LCDocument</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">return</span> <span class="n">LCDocument</span><span class="p">(</span><span class="n">page_content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_langchain_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"LCDocument"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct from LangChain document format."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">page_content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_haystack_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HaystackDocument"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct to Haystack document format."""</span>
        <span class="kn">from</span> <span class="nn">haystack.schema</span> <span class="kn">import</span> <span class="n">Document</span> <span class="k">as</span> <span class="n">HaystackDocument</span>

        <span class="k">return</span> <span class="n">HaystackDocument</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">meta</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_haystack_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"HaystackDocument"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct from Haystack document format."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">meta</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_embedchain_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Convert struct to EmbedChain document format."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"doc_id"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
            <span class="s2">"data"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"content"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="s2">"meta_data"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">},</span>
        <span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_embedchain_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct from EmbedChain document format."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">],</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"meta_data"</span><span class="p">],</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">],</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_semantic_kernel_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MemoryRecord"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct to Semantic Kernel document format."""</span>
        <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
        <span class="kn">from</span> <span class="nn">semantic_kernel.memory.memory_record</span> <span class="kn">import</span> <span class="n">MemoryRecord</span>

        <span class="k">return</span> <span class="n">MemoryRecord</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
            <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="n">additional_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_metadata_str</span><span class="p">(),</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_semantic_kernel_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"MemoryRecord"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert struct from Semantic Kernel document format."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_text</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"additional_metadata"</span><span class="p">:</span> <span class="n">doc</span><span class="o">.</span><span class="n">_additional_metadata</span><span class="p">},</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_embedding</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="k">if</span> <span class="n">doc</span><span class="o">.</span><span class="n">_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_id</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_vectorflow</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Send a document to vectorflow, since they don't have a document object."""</span>
        <span class="c1"># write document to temp file</span>
        <span class="kn">import</span> <span class="nn">tempfile</span>

        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">()</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="n">f</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
            <span class="n">client</span><span class="o">.</span><span class="n">embed</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">example</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">SAMPLE_TEXT</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="s2">"README.md"</span><span class="p">,</span> <span class="s2">"category"</span><span class="p">:</span> <span class="s2">"codebase"</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"Document"</span>

    <span class="k">def</span> <span class="nf">to_cloud_document</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CloudDocument"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert to LlamaCloud document type."""</span>
        <span class="kn">from</span> <span class="nn">llama_cloud.types.cloud_document</span> <span class="kn">import</span> <span class="n">CloudDocument</span>

        <span class="k">return</span> <span class="n">CloudDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
            <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_cloud_document</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">doc</span><span class="p">:</span> <span class="s2">"CloudDocument"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert from LlamaCloud document type."""</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
            <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
            <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### doc\_id `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.doc_id "Permanent link")

```
doc_id: str
```

Get document ID.

### get\_type `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.get_type "Permanent link")

```
get_type() -> str
```

Get Document type.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">get_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get Document type."""</span>
    <span class="k">return</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">DOCUMENT</span>
</code></pre></div></td></tr></tbody></table>

### get\_doc\_id [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.get_doc_id "Permanent link")

```
get_doc_id() -> str
```

TODO: Deprecated: Get document ID.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_doc_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""TODO: Deprecated: Get document ID."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span>
</code></pre></div></td></tr></tbody></table>

### to\_langchain\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_langchain_format "Permanent link")

```
to_langchain_format() -> Document
```

Convert struct to LangChain document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_langchain_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"LCDocument"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct to LangChain document format."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.bridge.langchain</span> <span class="kn">import</span> <span class="n">Document</span> <span class="k">as</span> <span class="n">LCDocument</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">return</span> <span class="n">LCDocument</span><span class="p">(</span><span class="n">page_content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_langchain\_format `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.from_langchain_format "Permanent link")

```
from_langchain_format(doc: Document) -> [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")
```

Convert struct from LangChain document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_langchain_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"LCDocument"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct from LangChain document format."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">page_content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_haystack\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_haystack_format "Permanent link")

```
to_haystack_format() -> Document
```

Convert struct to Haystack document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_haystack_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"HaystackDocument"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct to Haystack document format."""</span>
    <span class="kn">from</span> <span class="nn">haystack.schema</span> <span class="kn">import</span> <span class="n">Document</span> <span class="k">as</span> <span class="n">HaystackDocument</span>

    <span class="k">return</span> <span class="n">HaystackDocument</span><span class="p">(</span>
        <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">meta</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_haystack\_format `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.from_haystack_format "Permanent link")

```
from_haystack_format(doc: Document) -> [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")
```

Convert struct from Haystack document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_haystack_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"HaystackDocument"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct from Haystack document format."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">meta</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_embedchain\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_embedchain_format "Permanent link")

```
to_embedchain_format() -> Dict[str, Any]
```

Convert struct to EmbedChain document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_embedchain_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Convert struct to EmbedChain document format."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"doc_id"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
        <span class="s2">"data"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"content"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="s2">"meta_data"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">},</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### from\_embedchain\_format `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.from_embedchain_format "Permanent link")

```
from_embedchain_format(doc: Dict[str, Any]) -> [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")
```

Convert struct from EmbedChain document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_embedchain_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct from EmbedChain document format."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">],</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"data"</span><span class="p">][</span><span class="s2">"meta_data"</span><span class="p">],</span>
        <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">],</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_semantic\_kernel\_format [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_semantic_kernel_format "Permanent link")

```
to_semantic_kernel_format() -> MemoryRecord
```

Convert struct to Semantic Kernel document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_semantic_kernel_format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MemoryRecord"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct to Semantic Kernel document format."""</span>
    <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
    <span class="kn">from</span> <span class="nn">semantic_kernel.memory.memory_record</span> <span class="kn">import</span> <span class="n">MemoryRecord</span>

    <span class="k">return</span> <span class="n">MemoryRecord</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
        <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
        <span class="n">additional_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_metadata_str</span><span class="p">(),</span>
        <span class="n">embedding</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_semantic\_kernel\_format `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.from_semantic_kernel_format "Permanent link")

```
from_semantic_kernel_format(doc: MemoryRecord) -> [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")
```

Convert struct from Semantic Kernel document format.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_semantic_kernel_format</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">doc</span><span class="p">:</span> <span class="s2">"MemoryRecord"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert struct from Semantic Kernel document format."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_text</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"additional_metadata"</span><span class="p">:</span> <span class="n">doc</span><span class="o">.</span><span class="n">_additional_metadata</span><span class="p">},</span>
        <span class="n">embedding</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_embedding</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> <span class="k">if</span> <span class="n">doc</span><span class="o">.</span><span class="n">_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">_id</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_vectorflow [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_vectorflow "Permanent link")

```
to_vectorflow(client: Any) -> None
```

Send a document to vectorflow, since they don't have a document object.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_vectorflow</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Send a document to vectorflow, since they don't have a document object."""</span>
    <span class="c1"># write document to temp file</span>
    <span class="kn">import</span> <span class="nn">tempfile</span>

    <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">()</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
        <span class="n">f</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
        <span class="n">client</span><span class="o">.</span><span class="n">embed</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_cloud\_document [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.to_cloud_document "Permanent link")

```
to_cloud_document() -> CloudDocument
```

Convert to LlamaCloud document type.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_cloud_document</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CloudDocument"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert to LlamaCloud document type."""</span>
    <span class="kn">from</span> <span class="nn">llama_cloud.types.cloud_document</span> <span class="kn">import</span> <span class="n">CloudDocument</span>

    <span class="k">return</span> <span class="n">CloudDocument</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_cloud\_document `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document.from_cloud_document "Permanent link")

```
from_cloud_document(doc: CloudDocument) -> [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")
```

Convert from LlamaCloud document type.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_cloud_document</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">doc</span><span class="p">:</span> <span class="s2">"CloudDocument"</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"Document"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert from LlamaCloud document type."""</span>
    <span class="k">return</span> <span class="n">Document</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
        <span class="n">metadata</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
        <span class="n">excluded_embed_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="p">,</span>
        <span class="n">excluded_llm_metadata_keys</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="p">,</span>
        <span class="n">id_</span><span class="o">=</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ImageDocument [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------

Bases: `[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")`, `[ImageNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageNode "llama_index.core.schema.ImageNode")`

Data document containing an image.

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageDocument</span><span class="p">(</span><span class="n">Document</span><span class="p">,</span> <span class="n">ImageNode</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Data document containing an image."""</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ImageDocument"</span>
</code></pre></div></td></tr></tbody></table>

QueryBundle `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.QueryBundle "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Bases: `DataClassJsonMixin`

Query bundle.

This dataclass contains the original query string and associated transformations.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_str` | `str` | 
the original user-specified query string. This is currently used by all non embedding-based queries.



 | _required_ |
| `custom_embedding_strs` | `list[str]` | 

list of strings used for embedding the query. This is currently used by all embedding-based queries.



 | `None` |
| `embedding` | `list[float]` | 

the stored embedding for the query.



 | `None` |

Source code in `llama-index-core/llama_index/core/schema.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span>
<span class="normal">819</span>
<span class="normal">820</span>
<span class="normal">821</span>
<span class="normal">822</span>
<span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">QueryBundle</span><span class="p">(</span><span class="n">DataClassJsonMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query bundle.</span>

<span class="sd">    This dataclass contains the original query string and associated transformations.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_str (str): the original user-specified query string.</span>
<span class="sd">            This is currently used by all non embedding-based queries.</span>
<span class="sd">        custom_embedding_strs (list[str]): list of strings used for embedding the query.</span>
<span class="sd">            This is currently used by all embedding-based queries.</span>
<span class="sd">        embedding (list[float]): the stored embedding for the query.</span>
<span class="sd">    """</span>

    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span>
    <span class="c1"># using single image path as query input</span>
    <span class="n">image_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">custom_embedding_strs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">embedding_strs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Use custom embedding strs if specified, otherwise use query str."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_embedding_strs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query_str</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">return</span> <span class="p">[]</span>
            <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">query_str</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_embedding_strs</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">embedding_image</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ImageType</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Use image path for image retrieval."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_path</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">image_path</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert to string representation."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_str</span>
</code></pre></div></td></tr></tbody></table>

### embedding\_strs `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.QueryBundle.embedding_strs "Permanent link")

```
embedding_strs: List[str]
```

Use custom embedding strs if specified, otherwise use query str.

### embedding\_image `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.QueryBundle.embedding_image "Permanent link")

```
embedding_image: List[ImageType]
```

Use image path for image retrieval.

Back to top

[Previous You](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/)[Next Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/)
