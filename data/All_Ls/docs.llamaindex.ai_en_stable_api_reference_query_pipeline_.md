Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/

Markdown Content:
Index - LlamaIndex


Pipeline schema.

InputKeys [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Input keys.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 71</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">InputKeys</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Input keys."""</span>

    <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">set</span><span class="p">)</span>
    <span class="n">optional_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">set</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_keys</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">optional_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"InputKeys"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create InputKeys from tuple."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">required_keys</span><span class="o">=</span><span class="n">required_keys</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="n">optional_keys</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">validate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate input keys."""</span>
        <span class="c1"># check if required keys are present, and that keys all are in required or optional</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">input_keys</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Required keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="si">}</span><span class="s2"> are not present in input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">input_keys</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2"> contain keys not in required or optional keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Length of input keys."""</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all input keys."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_keys `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys.from_keys "Permanent link")

```
from_keys(required_keys: Set[str], optional_keys: Optional[Set[str]] = None) -> [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Create InputKeys from tuple.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_keys</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">optional_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"InputKeys"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create InputKeys from tuple."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">required_keys</span><span class="o">=</span><span class="n">required_keys</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="n">optional_keys</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

### validate [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys.validate "Permanent link")

```
validate(input_keys: Set[str]) -> None
```

Validate input keys.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate input keys."""</span>
    <span class="c1"># check if required keys are present, and that keys all are in required or optional</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">input_keys</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Required keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="si">}</span><span class="s2"> are not present in input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">input_keys</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2"> contain keys not in required or optional keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### all [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys.all "Permanent link")

```
all() -> Set[str]
```

Get all input keys.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all input keys."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">union</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optional_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

OutputKeys [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Output keys.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">105</span>
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
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OutputKeys</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Output keys."""</span>

    <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">set</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_keys</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OutputKeys"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create OutputKeys from tuple."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">required_keys</span><span class="o">=</span><span class="n">required_keys</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">validate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate input keys."""</span>
        <span class="c1"># validate that input keys exactly match required keys</span>
        <span class="k">if</span> <span class="n">input_keys</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2"> do not match required keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_keys `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys.from_keys "Permanent link")

```
from_keys(required_keys: Set[str]) -> [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Create OutputKeys from tuple.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_keys</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">required_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OutputKeys"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create OutputKeys from tuple."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">required_keys</span><span class="o">=</span><span class="n">required_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### validate [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys.validate "Permanent link")

```
validate(input_keys: Set[str]) -> None
```

Validate input keys.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate input keys."""</span>
    <span class="c1"># validate that input keys exactly match required keys</span>
    <span class="k">if</span> <span class="n">input_keys</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Input keys </span><span class="si">{</span><span class="n">input_keys</span><span class="si">}</span><span class="s2"> do not match required keys </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">required_keys</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ChainableMixin [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Chainable mixin.

A module that can produce a `QueryComponent` from a set of inputs through `as_query_component`.

If plugged in directly into a `QueryPipeline`, the `ChainableMixin` will be converted into a `QueryComponent` with default parameters.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
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
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChainableMixin</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chainable mixin.</span>

<span class="sd">    A module that can produce a `QueryComponent` from a set of inputs through</span>
<span class="sd">    `as_query_component`.</span>

<span class="sd">    If plugged in directly into a `QueryPipeline`, the `ChainableMixin` will be</span>
<span class="sd">    converted into a `QueryComponent` with default parameters.</span>

<span class="sd">    """</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_as_query_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"QueryComponent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get query component."""</span>

    <span class="k">def</span> <span class="nf">as_query_component</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">partial</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"QueryComponent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get query component."""</span>
        <span class="n">component</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_as_query_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">component</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="p">(</span><span class="n">partial</span> <span class="ow">or</span> <span class="p">{}))</span>
        <span class="k">return</span> <span class="n">component</span>
</code></pre></div></td></tr></tbody></table>

### as\_query\_component [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ChainableMixin.as_query_component "Permanent link")

```
as_query_component(partial: Optional[Dict[str, Any]] = None, **kwargs: Any) -> [QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")
```

Get query component.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_query_component</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">partial</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"QueryComponent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get query component."""</span>
    <span class="n">component</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_as_query_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">component</span><span class="o">.</span><span class="n">partial</span><span class="p">(</span><span class="o">**</span><span class="p">(</span><span class="n">partial</span> <span class="ow">or</span> <span class="p">{}))</span>
    <span class="k">return</span> <span class="n">component</span>
</code></pre></div></td></tr></tbody></table>

QueryComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Query component.

Represents a component that can be run in a `QueryPipeline`.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
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
<span class="normal">240</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryComponent</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Query component.</span>

<span class="sd">    Represents a component that can be run in a `QueryPipeline`.</span>

<span class="sd">    """</span>

    <span class="n">partial_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Partial arguments to run_component"</span>
    <span class="p">)</span>

    <span class="c1"># TODO: make this a subclass of BaseComponent (e.g. use Pydantic)</span>

    <span class="k">def</span> <span class="nf">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update with partial arguments."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="c1"># TODO: refactor so that callback_manager is always passed in during runtime.</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">free_req_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get free input keys."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_keys</span><span class="o">.</span><span class="n">required_keys</span><span class="o">.</span><span class="n">difference</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>

    <span class="k">def</span> <span class="nf">_validate_component_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component outputs during run_component."""</span>
        <span class="c1"># override if needed</span>
        <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs."""</span>
        <span class="c1"># make sure set of input keys  self.output_keys</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_keys</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">output</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_component_outputs</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="p">)</span>
        <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_inputs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">component_outputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_outputs</span><span class="p">(</span><span class="n">component_outputs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>
        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="p">)</span>
        <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_inputs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">component_outputs</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_outputs</span><span class="p">(</span><span class="n">component_outputs</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">_run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">sub_query_components</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"QueryComponent"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get sub query components.</span>

<span class="sd">        Certain query components may have sub query components, e.g. a</span>
<span class="sd">        query pipeline will have sub query components, and so will</span>
<span class="sd">        an IfElseComponent.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

### free\_req\_input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.free_req_input_keys "Permanent link")

```
free_req_input_keys: Set[str]
```

Get free input keys.

### input\_keys `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.input_keys "Permanent link")

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

### output\_keys `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.output_keys "Permanent link")

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

### sub\_query\_components `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.sub_query_components "Permanent link")

```
sub_query_components: List[[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")]
```

Get sub query components.

Certain query components may have sub query components, e.g. a query pipeline will have sub query components, and so will an IfElseComponent.

### partial [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.partial "Permanent link")

```
partial(**kwargs: Any) -> None
```

Update with partial arguments.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Update with partial arguments."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set\_callback\_manager `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.set_callback_manager "Permanent link")

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
</code></pre></div></td></tr></tbody></table>

### validate\_component\_inputs [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.validate_component_inputs "Permanent link")

```
validate_component_inputs(input: Dict[str, Any]) -> Dict[str, Any]
```

Validate component inputs.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Validate component inputs."""</span>
    <span class="c1"># make sure set of input keys  self.output_keys</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">output_keys</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">output</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_component_outputs</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run\_component [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.run_component "Permanent link")

```
run_component(**kwargs: Any) -> Dict[str, Any]
```

Run component.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run component."""</span>
    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="p">)</span>
    <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_inputs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">component_outputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_outputs</span><span class="p">(</span><span class="n">component_outputs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### arun\_component `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent.arun_component "Permanent link")

```
arun_component(**kwargs: Any) -> Dict[str, Any]
```

Run component.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run component."""</span>
    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_dict</span><span class="p">)</span>
    <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_inputs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">component_outputs</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_component</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_component_outputs</span><span class="p">(</span><span class="n">component_outputs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

CustomQueryComponent [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.CustomQueryComponent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")`

Custom query component.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">243</span>
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
<span class="normal">297</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CustomQueryComponent</span><span class="p">(</span><span class="n">QueryComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Custom query component."""</span>

    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Callback manager"</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="k">def</span> <span class="nf">_validate_component_inputs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Validate component inputs during run_component."""</span>
        <span class="c1"># NOTE: user can override this method to validate inputs</span>
        <span class="c1"># but we do this by default for convenience</span>
        <span class="k">return</span> <span class="nb">input</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run component (async)."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"This component does not support async run."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Input keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_optional_input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Optional input keys dict."""</span>
        <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Output keys dict."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Not implemented yet. Please override this method."</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">input_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Input keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>

        <span class="k">return</span> <span class="n">InputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span>
            <span class="n">required_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_input_keys</span><span class="p">,</span> <span class="n">optional_keys</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_optional_input_keys</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OutputKeys</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Output keys."""</span>
        <span class="c1"># NOTE: user can override this too, but we have them implement an</span>
        <span class="c1"># abstract method to make sure they do it</span>
        <span class="k">return</span> <span class="n">OutputKeys</span><span class="o">.</span><span class="n">from_keys</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_output_keys</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### input\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.input_keys "Permanent link")

```
input_keys: [InputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.InputKeys "llama_index.core.base.query_pipeline.query.InputKeys")
```

Input keys.

### output\_keys `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.output_keys "Permanent link")

```
output_keys: [OutputKeys](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.OutputKeys "llama_index.core.base.query_pipeline.query.OutputKeys")
```

Output keys.

### set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.CustomQueryComponent.set_callback_manager "Permanent link")

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

Link [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.Link "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Link between two components.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">300</span>
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
<span class="normal">337</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Link</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Link between two components."""</span>

    <span class="n">src</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Source component name"</span><span class="p">)</span>
    <span class="n">dest</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Destination component name"</span><span class="p">)</span>
    <span class="n">src_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Source component output key"</span>
    <span class="p">)</span>
    <span class="n">dest_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Destination component input key"</span>
    <span class="p">)</span>

    <span class="n">condition_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Condition to determine if link should be followed"</span>
    <span class="p">)</span>
    <span class="n">input_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Input to destination component"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">src</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">dest</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">src_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">dest_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">condition_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">input_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># NOTE: This is to enable positional args.</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">src</span><span class="o">=</span><span class="n">src</span><span class="p">,</span>
            <span class="n">dest</span><span class="o">=</span><span class="n">dest</span><span class="p">,</span>
            <span class="n">src_key</span><span class="o">=</span><span class="n">src_key</span><span class="p">,</span>
            <span class="n">dest_key</span><span class="o">=</span><span class="n">dest_key</span><span class="p">,</span>
            <span class="n">condition_fn</span><span class="o">=</span><span class="n">condition_fn</span><span class="p">,</span>
            <span class="n">input_fn</span><span class="o">=</span><span class="n">input_fn</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ComponentIntermediates [#](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.ComponentIntermediates "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Component intermediate inputs and outputs.

Source code in `llama-index-core/llama_index/core/base/query_pipeline/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">340</span>
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
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ComponentIntermediates</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Component intermediate inputs and outputs."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">inputs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">outputs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">inputs</span> <span class="o">=</span> <span class="n">inputs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">outputs</span> <span class="o">=</span> <span class="n">outputs</span>

    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"ComponentIntermediates(inputs=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">inputs</span><span class="si">!s}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"outputs=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">outputs</span><span class="si">!s}</span><span class="s2">)"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__repr__</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Function](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/)[Next Input](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/input/)
