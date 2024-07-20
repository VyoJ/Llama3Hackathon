Title: Selection - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/

Markdown Content:
Selection - LlamaIndex


Output parsers.

SelectionOutputParser [#](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/#llama_index.core.output_parsers.SelectionOutputParser "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/#llama_index.core.types.BaseOutputParser "llama_index.core.types.BaseOutputParser")`

Source code in `llama-index-core/llama_index/core/output_parsers/selection.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 38</span>
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
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SelectionOutputParser</span><span class="p">(</span><span class="n">BaseOutputParser</span><span class="p">):</span>
    <span class="n">REQUIRED_KEYS</span> <span class="o">=</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">Answer</span><span class="o">.</span><span class="vm">__annotations__</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_filter_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">json_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Filter recursively until a dictionary matches all REQUIRED_KEYS."""</span>
        <span class="n">output_dict</span> <span class="o">=</span> <span class="n">json_dict</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">REQUIRED_KEYS</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="n">output_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_dict</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">val</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                        <span class="n">output_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_dict</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">output_dict</span>

    <span class="k">def</span> <span class="nf">_format_output</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
        <span class="n">output_json</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">json_dict</span> <span class="ow">in</span> <span class="n">output</span><span class="p">:</span>
            <span class="n">valid</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">REQUIRED_KEYS</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="p">:</span>
                    <span class="n">valid</span> <span class="o">=</span> <span class="kc">False</span>
                    <span class="k">break</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">valid</span><span class="p">:</span>
                <span class="n">json_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_dict</span><span class="p">(</span><span class="n">json_dict</span><span class="p">)</span>

            <span class="n">output_json</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json_dict</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">output_json</span>

    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="n">json_string</span> <span class="o">=</span> <span class="n">_marshal_llm_to_json</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">json_obj</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_string</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecodeError</span> <span class="k">as</span> <span class="n">e_json</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">yaml</span>

                <span class="c1"># NOTE: parsing again with pyyaml</span>
                <span class="c1">#       pyyaml is less strict, and allows for trailing commas</span>
                <span class="c1">#       right now we rely on this since guidance program generates</span>
                <span class="c1">#       trailing commas</span>
                <span class="n">json_obj</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">json_string</span><span class="p">)</span>
            <span class="k">except</span> <span class="n">yaml</span><span class="o">.</span><span class="n">YAMLError</span> <span class="k">as</span> <span class="n">e_yaml</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">OutputParserException</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Got invalid JSON object. Error: </span><span class="si">{</span><span class="n">e_json</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">e_yaml</span><span class="si">}</span><span class="s2">. "</span>
                    <span class="sa">f</span><span class="s2">"Got JSON string: </span><span class="si">{</span><span class="n">json_string</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">NameError</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please pip install PyYAML."</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">exc</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_obj</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">json_obj</span> <span class="o">=</span> <span class="p">[</span><span class="n">json_obj</span><span class="p">]</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">json_obj</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to convert output to JSON: </span><span class="si">{</span><span class="n">output</span><span class="si">!r}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">json_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_output</span><span class="p">(</span><span class="n">json_obj</span><span class="p">)</span>
        <span class="n">answers</span> <span class="o">=</span> <span class="p">[</span><span class="n">Answer</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">json_dict</span><span class="p">)</span> <span class="k">for</span> <span class="n">json_dict</span> <span class="ow">in</span> <span class="n">json_output</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">StructuredOutput</span><span class="p">(</span><span class="n">raw_output</span><span class="o">=</span><span class="n">output</span><span class="p">,</span> <span class="n">parsed_output</span><span class="o">=</span><span class="n">answers</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompt_template</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">prompt_template</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">_escape_curly_braces</span><span class="p">(</span><span class="n">FORMAT_STR</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/)[Next Evaporate](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/)
