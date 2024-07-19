Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/

Markdown Content:
Index - LlamaIndex


Evaluation modules.

BaseEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PromptMixin`

Base Evaluator class.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 42</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseEvaluator</span><span class="p">(</span><span class="n">PromptMixin</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base Evaluator class."""</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">        and generated response string.</span>

<span class="sd">        Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">        take in additional arguments.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">        and generated response string.</span>

<span class="sd">        Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">        take in additional arguments.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">evaluate_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Response</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with query string and generated Response object.</span>

<span class="sd">        Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">        take in additional arguments.</span>
<span class="sd">        """</span>
        <span class="n">response_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
            <span class="n">contexts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Response</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run evaluation with query string and generated Response object.</span>

<span class="sd">        Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">        take in additional arguments.</span>
<span class="sd">        """</span>
        <span class="n">response_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
            <span class="n">contexts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator.evaluate "Permanent link")

```
evaluate(query: Optional[str] = None, response: Optional[str] = None, contexts: Optional[Sequence[str]] = None, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Run evaluation with query string, retrieved contexts, and generated response string.

Subclasses can override this method to provide custom evaluation logic and take in additional arguments.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">49</span>
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
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">    and generated response string.</span>

<span class="sd">    Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">    take in additional arguments.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator.aevaluate "Permanent link")

```
aevaluate(query: Optional[str] = None, response: Optional[str] = None, contexts: Optional[Sequence[str]] = None, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Run evaluation with query string, retrieved contexts, and generated response string.

Subclasses can override this method to provide custom evaluation logic and take in additional arguments.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
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
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with query string, retrieved contexts,</span>
<span class="sd">    and generated response string.</span>

<span class="sd">    Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">    take in additional arguments.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### evaluate\_response [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator.evaluate_response "Permanent link")

```
evaluate_response(query: Optional[str] = None, response: Optional[Response] = None, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Run evaluation with query string and generated Response object.

Subclasses can override this method to provide custom evaluation logic and take in additional arguments.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 87</span>
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
<span class="normal">106</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Response</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with query string and generated Response object.</span>

<span class="sd">    Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">    take in additional arguments.</span>
<span class="sd">    """</span>
    <span class="n">response_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">response_str</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
        <span class="n">contexts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_response `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator.aevaluate_response "Permanent link")

```
aevaluate_response(query: Optional[str] = None, response: Optional[Response] = None, **kwargs: Any) -> [EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")
```

Run evaluation with query string and generated Response object.

Subclasses can override this method to provide custom evaluation logic and take in additional arguments.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">108</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_response</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Response</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run evaluation with query string and generated Response object.</span>

<span class="sd">    Subclasses can override this method to provide custom evaluation logic and</span>
<span class="sd">    take in additional arguments.</span>
<span class="sd">    """</span>
    <span class="n">response_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">response_str</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
        <span class="n">contexts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">source_nodes</span><span class="p">]</span>

    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

EvaluationResult [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Evaluation result.

Output of an BaseEvaluator.

Source code in `llama-index-core/llama_index/core/evaluation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
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
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EvaluationResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Evaluation result.</span>

<span class="sd">    Output of an BaseEvaluator.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Query string"</span><span class="p">)</span>
    <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Context strings"</span><span class="p">)</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Response string"</span><span class="p">)</span>
    <span class="n">passing</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Binary evaluation result (passing or not)"</span>
    <span class="p">)</span>
    <span class="n">feedback</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Feedback or reasoning for the response"</span>
    <span class="p">)</span>
    <span class="n">score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Score for the response"</span><span class="p">)</span>
    <span class="n">pairwise_source</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
            <span class="s2">"Used only for pairwise and specifies whether it is from original order of"</span>
            <span class="s2">" presented answers or flipped order"</span>
        <span class="p">),</span>
    <span class="p">)</span>
    <span class="n">invalid_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether the evaluation result is an invalid one."</span>
    <span class="p">)</span>
    <span class="n">invalid_reason</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Reason for invalid evaluation."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BatchEvalRunner [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------

Batch evaluation runner.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `evaluators` | `Dict[str, [BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")]` | 
Dictionary of evaluators.



 | _required_ |
| `workers` | `int` | 

Number of workers to use for parallelization. Defaults to 2.



 | `2` |
| `show_progress` | `bool` | 

Whether to show progress bars. Defaults to False.



 | `False` |

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 75</span>
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
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
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
<span class="normal">442</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BatchEvalRunner</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Batch evaluation runner.</span>

<span class="sd">    Args:</span>
<span class="sd">        evaluators (Dict[str, BaseEvaluator]): Dictionary of evaluators.</span>
<span class="sd">        workers (int): Number of workers to use for parallelization.</span>
<span class="sd">            Defaults to 2.</span>
<span class="sd">        show_progress (bool): Whether to show progress bars. Defaults to False.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">evaluators</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseEvaluator</span><span class="p">],</span>
        <span class="n">workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span> <span class="o">=</span> <span class="n">evaluators</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">workers</span> <span class="o">=</span> <span class="n">workers</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Semaphore</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">workers</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span> <span class="o">=</span> <span class="n">show_progress</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span> <span class="o">=</span> <span class="n">asyncio_module</span><span class="p">(</span><span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_format_results</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Format results."""</span>
        <span class="c1"># Format results</span>
        <span class="n">results_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">name</span><span class="p">:</span> <span class="p">[]</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">results_dict</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">results_dict</span>

    <span class="k">def</span> <span class="nf">_validate_and_clean_inputs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">inputs_list</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Validate and clean input lists.</span>

<span class="sd">        Enforce that at least one of the inputs is not None.</span>
<span class="sd">        Make sure that all inputs have the same length.</span>
<span class="sd">        Make sure that None inputs are replaced with [None] * len(inputs).</span>

<span class="sd">        """</span>
        <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">inputs_list</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
        <span class="c1"># first, make sure at least one of queries or response_strs is not None</span>
        <span class="n">input_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">for</span> <span class="n">inputs</span> <span class="ow">in</span> <span class="n">inputs_list</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">inputs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">input_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span>
                <span class="k">break</span>
        <span class="k">if</span> <span class="n">input_len</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"At least one item in inputs_list must be provided."</span><span class="p">)</span>

        <span class="n">new_inputs_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">inputs</span> <span class="ow">in</span> <span class="n">inputs_list</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">inputs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">new_inputs_list</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="kc">None</span><span class="p">]</span> <span class="o">*</span> <span class="n">input_len</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span> <span class="o">!=</span> <span class="n">input_len</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"All inputs must have the same length."</span><span class="p">)</span>
                <span class="n">new_inputs_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">inputs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_inputs_list</span>

    <span class="k">def</span> <span class="nf">_validate_nested_eval_kwargs_types</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Ensure eval kwargs are acceptable format.</span>
<span class="sd">            either a Dict[str, List] or a Dict[str, Dict[str, List]].</span>

<span class="sd">        Allows use of different kwargs (e.g. references) with different evaluators</span>
<span class="sd">            while keeping backwards compatibility for single evaluators</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"eval_kwargs_lists must be a dict. Got </span><span class="si">{</span><span class="n">eval_kwargs_lists</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">evaluator</span><span class="p">,</span> <span class="n">eval_kwargs</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_kwargs</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="c1"># maintain backwards compatibility - for use with single evaluator</span>
                <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">evaluator</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span>
                    <span class="n">eval_kwargs</span>
                <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">eval_kwargs</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="c1"># for use with multiple evaluators</span>
                <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">eval_kwargs</span><span class="p">:</span>
                    <span class="n">v</span> <span class="o">=</span> <span class="n">eval_kwargs</span><span class="p">[</span><span class="n">k</span><span class="p">]</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"nested inner values in eval_kwargs must be a list. Got </span><span class="si">{</span><span class="n">evaluator</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span>
                        <span class="p">)</span>
                    <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">evaluator</span><span class="p">][</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span>
                        <span class="n">v</span>
                    <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"eval_kwargs must be a list or a dict. Got </span><span class="si">{</span><span class="n">evaluator</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">eval_kwargs</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">eval_kwargs_lists</span>

    <span class="k">def</span> <span class="nf">_get_eval_kwargs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Get eval kwargs from eval_kwargs_lists at a given idx.</span>

<span class="sd">        Since eval_kwargs_lists is a dict of lists, we need to get the</span>
<span class="sd">        value at idx for each key.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_response_strs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_strs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts_list</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate query, response pairs.</span>

<span class="sd">        This evaluates queries, responses, contexts as string inputs.</span>
<span class="sd">        Can supply additional kwargs to the evaluator in eval_kwargs_lists.</span>

<span class="sd">        Args:</span>
<span class="sd">            queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">            response_strs (Optional[List[str]]): List of response strings.</span>
<span class="sd">                Defaults to None.</span>
<span class="sd">            contexts_list (Optional[List[List[str]]]): List of context lists.</span>
<span class="sd">                Defaults to None.</span>
<span class="sd">            **eval_kwargs_lists (Dict[str, Any]): Dict of either dicts or lists</span>
<span class="sd">                of kwargs to pass to evaluator. Defaults to None.</span>
<span class="sd">                    multiple evaluators: {evaluator: {kwarg: [list of values]},...}</span>
<span class="sd">                    single evaluator:    {kwarg: [list of values]}</span>

<span class="sd">        """</span>
        <span class="n">queries</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">,</span> <span class="n">contexts_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span>
            <span class="n">queries</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">,</span> <span class="n">contexts_list</span>
        <span class="p">)</span>
        <span class="n">eval_kwargs_lists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_nested_eval_kwargs_types</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span>

        <span class="c1"># boolean to check if using multi kwarg evaluator</span>
        <span class="n">multi_kwargs</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">values</span><span class="p">())),</span> <span class="nb">dict</span>
        <span class="p">)</span>

        <span class="c1"># run evaluations</span>
        <span class="n">eval_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">queries</span><span class="p">)):</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
            <span class="n">contexts</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">contexts_list</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">multi_kwargs</span><span class="p">:</span>
                    <span class="c1"># multi-evaluator - get appropriate runtime kwargs if present</span>
                    <span class="n">kwargs</span> <span class="o">=</span> <span class="p">(</span>
                        <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span> <span class="k">else</span> <span class="p">{}</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># single evaluator (maintain backwards compatibility)</span>
                    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">eval_kwargs_lists</span>
                <span class="n">eval_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_kwargs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">idx</span><span class="p">)</span>
                <span class="n">eval_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">eval_worker</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span>
                        <span class="n">evaluator</span><span class="p">,</span>
                        <span class="n">name</span><span class="p">,</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                        <span class="n">response_str</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span>
                        <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
                        <span class="n">eval_kwargs</span><span class="o">=</span><span class="n">eval_kwargs</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">eval_jobs</span><span class="p">)</span>

        <span class="c1"># Format results</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_results</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_responses</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">responses</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Response</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate query, response pairs.</span>

<span class="sd">        This evaluates queries and response objects.</span>

<span class="sd">        Args:</span>
<span class="sd">            queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">            responses (Optional[List[Response]]): List of response objects.</span>
<span class="sd">                Defaults to None.</span>
<span class="sd">            **eval_kwargs_lists (Dict[str, Any]): Dict of either dicts or lists</span>
<span class="sd">                of kwargs to pass to evaluator. Defaults to None.</span>
<span class="sd">                    multiple evaluators: {evaluator: {kwarg: [list of values]},...}</span>
<span class="sd">                    single evaluator:    {kwarg: [list of values]}</span>

<span class="sd">        """</span>
        <span class="n">queries</span><span class="p">,</span> <span class="n">responses</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span><span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="p">)</span>
        <span class="n">eval_kwargs_lists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_nested_eval_kwargs_types</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span>

        <span class="c1"># boolean to check if using multi kwarg evaluator</span>
        <span class="n">multi_kwargs</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">values</span><span class="p">())),</span> <span class="nb">dict</span>
        <span class="p">)</span>

        <span class="c1"># run evaluations</span>
        <span class="n">eval_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">queries</span><span class="p">)):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">responses</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">multi_kwargs</span><span class="p">:</span>
                    <span class="c1"># multi-evaluator - get appropriate runtime kwargs if present</span>
                    <span class="n">kwargs</span> <span class="o">=</span> <span class="p">(</span>
                        <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span> <span class="k">else</span> <span class="p">{}</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># single evaluator (maintain backwards compatibility)</span>
                    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">eval_kwargs_lists</span>
                <span class="n">eval_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_kwargs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">idx</span><span class="p">)</span>
                <span class="n">eval_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">eval_response_worker</span><span class="p">(</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span>
                        <span class="n">evaluator</span><span class="p">,</span>
                        <span class="n">name</span><span class="p">,</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                        <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                        <span class="n">eval_kwargs</span><span class="o">=</span><span class="n">eval_kwargs</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">eval_jobs</span><span class="p">)</span>

        <span class="c1"># Format results</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_results</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_queries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate queries.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_engine (BaseQueryEngine): Query engine.</span>
<span class="sd">            queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">            **eval_kwargs_lists (Dict[str, Any]): Dict of lists of kwargs to</span>
<span class="sd">                pass to evaluator. Defaults to None.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">queries</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`queries` must be provided"</span><span class="p">)</span>

        <span class="c1"># gather responses</span>
        <span class="n">response_jobs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">:</span>
            <span class="n">response_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">response_worker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span> <span class="n">query_engine</span><span class="p">,</span> <span class="n">query</span><span class="p">))</span>
        <span class="n">responses</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_responses</span><span class="p">(</span>
            <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
            <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
            <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">evaluate_response_strs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response_strs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts_list</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">List</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate query, response pairs.</span>

<span class="sd">        Sync version of aevaluate_response_strs.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_response_strs</span><span class="p">(</span>
                <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
                <span class="n">response_strs</span><span class="o">=</span><span class="n">response_strs</span><span class="p">,</span>
                <span class="n">contexts_list</span><span class="o">=</span><span class="n">contexts_list</span><span class="p">,</span>
                <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">evaluate_responses</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">responses</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Response</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate query, response objs.</span>

<span class="sd">        Sync version of aevaluate_responses.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_responses</span><span class="p">(</span>
                <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
                <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
                <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">evaluate_queries</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Evaluate queries.</span>

<span class="sd">        Sync version of aevaluate_queries.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_queries</span><span class="p">(</span>
                <span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">,</span>
                <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
                <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">upload_eval_results</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">app_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Upload the evaluation results to LlamaCloud.</span>

<span class="sd">        Args:</span>
<span class="sd">            project_name (str): The name of the project.</span>
<span class="sd">            app_name (str): The name of the app.</span>
<span class="sd">            results (Dict[str, List[EvaluationResult]]):</span>
<span class="sd">                The evaluation results, a mapping of metric name to a list of EvaluationResult objects.</span>

<span class="sd">        Examples:</span>
<span class="sd">            ```python</span>
<span class="sd">            results = batch_runner.evaluate_responses(...)</span>

<span class="sd">            batch_runner.upload_eval_results(</span>
<span class="sd">                project_name="my_project",</span>
<span class="sd">                app_name="my_app",</span>
<span class="sd">                results=results</span>
<span class="sd">            )</span>
<span class="sd">            ```</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.evaluation.eval_utils</span> <span class="kn">import</span> <span class="n">upload_eval_results</span>

        <span class="n">upload_eval_results</span><span class="p">(</span>
            <span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">,</span> <span class="n">app_name</span><span class="o">=</span><span class="n">app_name</span><span class="p">,</span> <span class="n">results</span><span class="o">=</span><span class="n">results</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_response\_strs `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.aevaluate_response_strs "Permanent link")

```
aevaluate_response_strs(queries: Optional[List[str]] = None, response_strs: Optional[List[str]] = None, contexts_list: Optional[List[List[str]]] = None, **eval_kwargs_lists: Dict[str, Any]) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate query, response pairs.

This evaluates queries, responses, contexts as string inputs. Can supply additional kwargs to the evaluator in eval\_kwargs\_lists.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `queries` | `Optional[List[str]]` | 
List of query strings. Defaults to None.



 | `None` |
| `response_strs` | `Optional[List[str]]` | 

List of response strings. Defaults to None.



 | `None` |
| `contexts_list` | `Optional[List[List[str]]]` | 

List of context lists. Defaults to None.



 | `None` |
| `**eval_kwargs_lists` | `Dict[str, Any]` | 

Dict of either dicts or lists of kwargs to pass to evaluator. Defaults to None. multiple evaluators: {evaluator: {kwarg: \[list of values\]},...} single evaluator: {kwarg: \[list of values\]}



 | `{}` |

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">195</span>
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
<span class="normal">259</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_response_strs</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response_strs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts_list</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate query, response pairs.</span>

<span class="sd">    This evaluates queries, responses, contexts as string inputs.</span>
<span class="sd">    Can supply additional kwargs to the evaluator in eval_kwargs_lists.</span>

<span class="sd">    Args:</span>
<span class="sd">        queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">        response_strs (Optional[List[str]]): List of response strings.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        contexts_list (Optional[List[List[str]]]): List of context lists.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        **eval_kwargs_lists (Dict[str, Any]): Dict of either dicts or lists</span>
<span class="sd">            of kwargs to pass to evaluator. Defaults to None.</span>
<span class="sd">                multiple evaluators: {evaluator: {kwarg: [list of values]},...}</span>
<span class="sd">                single evaluator:    {kwarg: [list of values]}</span>

<span class="sd">    """</span>
    <span class="n">queries</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">,</span> <span class="n">contexts_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span>
        <span class="n">queries</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">,</span> <span class="n">contexts_list</span>
    <span class="p">)</span>
    <span class="n">eval_kwargs_lists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_nested_eval_kwargs_types</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span>

    <span class="c1"># boolean to check if using multi kwarg evaluator</span>
    <span class="n">multi_kwargs</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span>
        <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">values</span><span class="p">())),</span> <span class="nb">dict</span>
    <span class="p">)</span>

    <span class="c1"># run evaluations</span>
    <span class="n">eval_jobs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">queries</span><span class="p">)):</span>
        <span class="n">response_str</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">response_strs</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
        <span class="n">contexts</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">contexts_list</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">multi_kwargs</span><span class="p">:</span>
                <span class="c1"># multi-evaluator - get appropriate runtime kwargs if present</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span> <span class="k">else</span> <span class="p">{}</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># single evaluator (maintain backwards compatibility)</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="n">eval_kwargs_lists</span>
            <span class="n">eval_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_kwargs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">idx</span><span class="p">)</span>
            <span class="n">eval_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">eval_worker</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span>
                    <span class="n">evaluator</span><span class="p">,</span>
                    <span class="n">name</span><span class="p">,</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                    <span class="n">response_str</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span>
                    <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
                    <span class="n">eval_kwargs</span><span class="o">=</span><span class="n">eval_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">eval_jobs</span><span class="p">)</span>

    <span class="c1"># Format results</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_results</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_responses `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.aevaluate_responses "Permanent link")

```
aevaluate_responses(queries: Optional[List[str]] = None, responses: Optional[List[Response]] = None, **eval_kwargs_lists: Dict[str, Any]) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate query, response pairs.

This evaluates queries and response objects.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `queries` | `Optional[List[str]]` | 
List of query strings. Defaults to None.



 | `None` |
| `responses` | `Optional[List[Response]]` | 

List of response objects. Defaults to None.



 | `None` |
| `**eval_kwargs_lists` | `Dict[str, Any]` | 

Dict of either dicts or lists of kwargs to pass to evaluator. Defaults to None. multiple evaluators: {evaluator: {kwarg: \[list of values\]},...} single evaluator: {kwarg: \[list of values\]}



 | `{}` |

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">261</span>
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
<span class="normal">317</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_responses</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">responses</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Response</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate query, response pairs.</span>

<span class="sd">    This evaluates queries and response objects.</span>

<span class="sd">    Args:</span>
<span class="sd">        queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">        responses (Optional[List[Response]]): List of response objects.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        **eval_kwargs_lists (Dict[str, Any]): Dict of either dicts or lists</span>
<span class="sd">            of kwargs to pass to evaluator. Defaults to None.</span>
<span class="sd">                multiple evaluators: {evaluator: {kwarg: [list of values]},...}</span>
<span class="sd">                single evaluator:    {kwarg: [list of values]}</span>

<span class="sd">    """</span>
    <span class="n">queries</span><span class="p">,</span> <span class="n">responses</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_and_clean_inputs</span><span class="p">(</span><span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="p">)</span>
    <span class="n">eval_kwargs_lists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_nested_eval_kwargs_types</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span>

    <span class="c1"># boolean to check if using multi kwarg evaluator</span>
    <span class="n">multi_kwargs</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span>
        <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">eval_kwargs_lists</span><span class="o">.</span><span class="n">values</span><span class="p">())),</span> <span class="nb">dict</span>
    <span class="p">)</span>

    <span class="c1"># run evaluations</span>
    <span class="n">eval_jobs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">query</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">queries</span><span class="p">)):</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">,</span> <span class="n">responses</span><span class="p">)[</span><span class="n">idx</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">evaluator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluators</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">multi_kwargs</span><span class="p">:</span>
                <span class="c1"># multi-evaluator - get appropriate runtime kwargs if present</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">eval_kwargs_lists</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">eval_kwargs_lists</span> <span class="k">else</span> <span class="p">{}</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># single evaluator (maintain backwards compatibility)</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="n">eval_kwargs_lists</span>
            <span class="n">eval_kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_eval_kwargs</span><span class="p">(</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">idx</span><span class="p">)</span>
            <span class="n">eval_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">eval_response_worker</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span>
                    <span class="n">evaluator</span><span class="p">,</span>
                    <span class="n">name</span><span class="p">,</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                    <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                    <span class="n">eval_kwargs</span><span class="o">=</span><span class="n">eval_kwargs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">eval_jobs</span><span class="p">)</span>

    <span class="c1"># Format results</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_results</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_queries `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.aevaluate_queries "Permanent link")

```
aevaluate_queries(query_engine: [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine"), queries: Optional[List[str]] = None, **eval_kwargs_lists: Dict[str, Any]) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate queries.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_engine` | `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")` | 
Query engine.



 | _required_ |
| `queries` | `Optional[List[str]]` | 

List of query strings. Defaults to None.



 | `None` |
| `**eval_kwargs_lists` | `Dict[str, Any]` | 

Dict of lists of kwargs to pass to evaluator. Defaults to None.



 | `{}` |

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">319</span>
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
<span class="normal">348</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_queries</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate queries.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_engine (BaseQueryEngine): Query engine.</span>
<span class="sd">        queries (Optional[List[str]]): List of query strings. Defaults to None.</span>
<span class="sd">        **eval_kwargs_lists (Dict[str, Any]): Dict of lists of kwargs to</span>
<span class="sd">            pass to evaluator. Defaults to None.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">queries</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`queries` must be provided"</span><span class="p">)</span>

    <span class="c1"># gather responses</span>
    <span class="n">response_jobs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">:</span>
        <span class="n">response_jobs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">response_worker</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">semaphore</span><span class="p">,</span> <span class="n">query_engine</span><span class="p">,</span> <span class="n">query</span><span class="p">))</span>
    <span class="n">responses</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_mod</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">response_jobs</span><span class="p">)</span>

    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_responses</span><span class="p">(</span>
        <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
        <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
        <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate\_response\_strs [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.evaluate_response_strs "Permanent link")

```
evaluate_response_strs(queries: Optional[List[str]] = None, response_strs: Optional[List[str]] = None, contexts_list: Optional[List[List[str]]] = None, **eval_kwargs_lists: List) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate query, response pairs.

Sync version of aevaluate\_response\_strs.

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
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
<span class="normal">370</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate_response_strs</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">response_strs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">contexts_list</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">List</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate query, response pairs.</span>

<span class="sd">    Sync version of aevaluate_response_strs.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_response_strs</span><span class="p">(</span>
            <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
            <span class="n">response_strs</span><span class="o">=</span><span class="n">response_strs</span><span class="p">,</span>
            <span class="n">contexts_list</span><span class="o">=</span><span class="n">contexts_list</span><span class="p">,</span>
            <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate\_responses [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.evaluate_responses "Permanent link")

```
evaluate_responses(queries: Optional[List[str]] = None, responses: Optional[List[Response]] = None, **eval_kwargs_lists: Dict[str, Any]) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate query, response objs.

Sync version of aevaluate\_responses.

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">372</span>
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
<span class="normal">390</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate_responses</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">responses</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Response</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate query, response objs.</span>

<span class="sd">    Sync version of aevaluate_responses.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_responses</span><span class="p">(</span>
            <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
            <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
            <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate\_queries [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.evaluate_queries "Permanent link")

```
evaluate_queries(query_engine: [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine"), queries: Optional[List[str]] = None, **eval_kwargs_lists: Dict[str, Any]) -> Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]
```

Evaluate queries.

Sync version of aevaluate\_queries.

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">392</span>
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
<span class="normal">410</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate_queries</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Evaluate queries.</span>

<span class="sd">    Sync version of aevaluate_queries.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_queries</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
            <span class="o">**</span><span class="n">eval_kwargs_lists</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### upload\_eval\_results [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BatchEvalRunner.upload_eval_results "Permanent link")

```
upload_eval_results(project_name: str, app_name: str, results: Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]) -> None
```

Upload the evaluation results to LlamaCloud.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `project_name` | `str` | 
The name of the project.



 | _required_ |
| `app_name` | `str` | 

The name of the app.



 | _required_ |
| `results` | `Dict[str, List[[EvaluationResult](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.EvaluationResult "llama_index.core.evaluation.base.EvaluationResult")]]` | 

The evaluation results, a mapping of metric name to a list of EvaluationResult objects.



 | _required_ |

**Examples:**

```
results = batch_runner.evaluate_responses(...)

batch_runner.upload_eval_results(
    project_name="my_project",
    app_name="my_app",
    results=results
)
```

Source code in `llama-index-core/llama_index/core/evaluation/batch_runner.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">412</span>
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
<span class="normal">442</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upload_eval_results</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">app_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">EvaluationResult</span><span class="p">]],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Upload the evaluation results to LlamaCloud.</span>

<span class="sd">    Args:</span>
<span class="sd">        project_name (str): The name of the project.</span>
<span class="sd">        app_name (str): The name of the app.</span>
<span class="sd">        results (Dict[str, List[EvaluationResult]]):</span>
<span class="sd">            The evaluation results, a mapping of metric name to a list of EvaluationResult objects.</span>

<span class="sd">    Examples:</span>
<span class="sd">        ```python</span>
<span class="sd">        results = batch_runner.evaluate_responses(...)</span>

<span class="sd">        batch_runner.upload_eval_results(</span>
<span class="sd">            project_name="my_project",</span>
<span class="sd">            app_name="my_app",</span>
<span class="sd">            results=results</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.evaluation.eval_utils</span> <span class="kn">import</span> <span class="n">upload_eval_results</span>

    <span class="n">upload_eval_results</span><span class="p">(</span>
        <span class="n">project_name</span><span class="o">=</span><span class="n">project_name</span><span class="p">,</span> <span class="n">app_name</span><span class="o">=</span><span class="n">app_name</span><span class="p">,</span> <span class="n">results</span><span class="o">=</span><span class="n">results</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Guideline](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/)[Next Metrics](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/)
