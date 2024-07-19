Title: Llama guard moderator - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/

Markdown Content:
Llama guard moderator - LlamaIndex


LlamaGuardModeratorPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/#llama_index.packs.llama_guard_moderator.LlamaGuardModeratorPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-llama-guard-moderator/llama_index/packs/llama_guard_moderator/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 55</span>
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
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LlamaGuardModeratorPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">custom_taxonomy</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TAXONOMY</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">torch</span>
            <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">AutoModelForCausalLM</span><span class="p">,</span> <span class="n">AutoTokenizer</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Dependencies missing, run "</span> <span class="s2">"`pip install torch transformers`"</span>
            <span class="p">)</span>

        <span class="kn">import</span> <span class="nn">os</span>

        <span class="n">hf_access_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"HUGGINGFACE_ACCESS_TOKEN"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"HUGGINGFACE_ACCESS_TOKEN"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Hugging Face access token is missing or invalid."</span><span class="p">)</span>

        <span class="kn">from</span> <span class="nn">huggingface_hub</span> <span class="kn">import</span> <span class="n">login</span>

        <span class="n">login</span><span class="p">(</span><span class="n">token</span><span class="o">=</span><span class="n">hf_access_token</span><span class="p">)</span>

        <span class="n">model_id</span> <span class="o">=</span> <span class="s2">"meta-llama/LlamaGuard-7b"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">device</span> <span class="o">=</span> <span class="s2">"cuda"</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">bfloat16</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span> <span class="o">=</span> <span class="n">AutoTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">model_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">AutoModelForCausalLM</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="n">model_id</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span><span class="p">,</span> <span class="n">device_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">custom_taxonomy</span> <span class="o">=</span> <span class="n">custom_taxonomy</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"tokenizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">,</span>
            <span class="s2">"model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
            <span class="s2">"device"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">,</span>
            <span class="s2">"custom_taxonomy"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_taxonomy</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="c1"># tailored for query engine input/output, using "user" role</span>
        <span class="n">chat</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"role"</span><span class="p">:</span> <span class="s2">"user"</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="n">message</span><span class="p">}]</span>

        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_moderation_prompt_for_chat</span><span class="p">(</span><span class="n">chat</span><span class="p">)</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">([</span><span class="n">prompt</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">)</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">pad_token_id</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
        <span class="n">prompt_len</span> <span class="o">=</span> <span class="n">inputs</span><span class="p">[</span><span class="s2">"input_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">output</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">prompt_len</span><span class="p">:],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_moderation_prompt_for_chat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">chat</span><span class="p">):</span>
        <span class="c1"># For simplicity, we assume the chat dictionary correctly alternates "user" and "assistant" roles</span>
        <span class="n">conversation</span> <span class="o">=</span> <span class="p">[</span><span class="n">turn</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span> <span class="k">for</span> <span class="n">turn</span> <span class="ow">in</span> <span class="n">chat</span><span class="p">]</span>
        <span class="n">role</span> <span class="o">=</span> <span class="s2">"Agent"</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">conversation</span><span class="p">)</span> <span class="o">%</span> <span class="mi">2</span> <span class="o"></span> <span class="mi">0</span> <span class="k">else</span> <span class="s2">"Agent"</span>
            <span class="n">prompt</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">role</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">m</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span>
        <span class="n">prompt</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"""&lt;END CONVERSATION&gt;</span>

<span class="s2">    Provide your safety assessment for </span><span class="si">{</span><span class="n">role</span><span class="si">}</span><span class="s2"> in the above conversation:</span>
<span class="s2">    - First line must read 'safe' or 'unsafe'.</span>
<span class="s2">    - If unsafe, a second line must include a comma-separated list of violated categories. [/INST]"""</span>
        <span class="k">return</span> <span class="n">prompt</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/#llama_index.packs.llama_guard_moderator.LlamaGuardModeratorPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-llama-guard-moderator/llama_index/packs/llama_guard_moderator/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"tokenizer"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">,</span>
        <span class="s2">"model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
        <span class="s2">"device"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">,</span>
        <span class="s2">"custom_taxonomy"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">custom_taxonomy</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/#llama_index.packs.llama_guard_moderator.LlamaGuardModeratorPack.run "Permanent link")

```
run(message: str, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-llama-guard-moderator/llama_index/packs/llama_guard_moderator/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="c1"># tailored for query engine input/output, using "user" role</span>
    <span class="n">chat</span> <span class="o">=</span> <span class="p">[{</span><span class="s2">"role"</span><span class="p">:</span> <span class="s2">"user"</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="n">message</span><span class="p">}]</span>

    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_moderation_prompt_for_chat</span><span class="p">(</span><span class="n">chat</span><span class="p">)</span>
    <span class="n">inputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">([</span><span class="n">prompt</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">)</span>
    <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">pad_token_id</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">prompt_len</span> <span class="o">=</span> <span class="n">inputs</span><span class="p">[</span><span class="s2">"input_ids"</span><span class="p">]</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">output</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">prompt_len</span><span class="p">:],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llama dataset metadata](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/)[Next Llava completion](https://docs.llamaindex.ai/en/stable/api_reference/packs/llava_completion/)
