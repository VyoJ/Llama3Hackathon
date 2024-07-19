Title: Presidio - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/

Markdown Content:
Presidio - LlamaIndex


PresidioPIINodePostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/#llama_index.postprocessor.presidio.PresidioPIINodePostprocessor "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

presidio PII Node processor. Uses a presidio to analyse PIIs.

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-presidio/llama_index/postprocessor/presidio/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 57</span>
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
<span class="normal">110</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PresidioPIINodePostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""presidio PII Node processor.</span>
<span class="sd">    Uses a presidio to analyse PIIs.</span>
<span class="sd">    """</span>

    <span class="n">pii_node_info_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"__pii_node_info__"</span>
    <span class="n">entity_mapping</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">mapping</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PresidioPIINodePostprocessor"</span>

    <span class="k">def</span> <span class="nf">mask_pii</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
        <span class="n">analyzer</span> <span class="o">=</span> <span class="n">AnalyzerEngine</span><span class="p">()</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">analyzer</span><span class="o">.</span><span class="n">analyze</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">language</span><span class="o">=</span><span class="s2">"en"</span><span class="p">)</span>
        <span class="n">engine</span> <span class="o">=</span> <span class="n">AnonymizerEngine</span><span class="p">()</span>
        <span class="n">engine</span><span class="o">.</span><span class="n">add_anonymizer</span><span class="p">(</span><span class="n">EntityTypeCountAnonymizer</span><span class="p">)</span>

        <span class="n">new_text</span> <span class="o">=</span> <span class="n">engine</span><span class="o">.</span><span class="n">anonymize</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
            <span class="n">analyzer_results</span><span class="o">=</span><span class="n">results</span><span class="p">,</span>
            <span class="n">operators</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"DEFAULT"</span><span class="p">:</span> <span class="n">OperatorConfig</span><span class="p">(</span>
                    <span class="s2">"EntityTypeCountAnonymizer"</span><span class="p">,</span>
                    <span class="p">{</span>
                        <span class="s2">"entity_mapping"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity_mapping</span><span class="p">,</span>
                        <span class="s2">"deanonymize_mapping"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">mapping</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">},</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">new_text</span><span class="o">.</span><span class="n">text</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="c1"># swap out text from nodes, with the original node mappings</span>
        <span class="n">new_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_with_score</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node_with_score</span><span class="o">.</span><span class="n">node</span>
            <span class="n">new_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">mask_pii</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">))</span>
            <span class="n">new_node</span> <span class="o">=</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">new_node</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pii_node_info_key</span><span class="p">)</span>
            <span class="n">new_node</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pii_node_info_key</span><span class="p">)</span>
            <span class="n">new_node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">pii_node_info_key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">mapping</span>
            <span class="n">new_node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">new_text</span><span class="p">)</span>
            <span class="n">new_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">new_node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">node_with_score</span><span class="o">.</span><span class="n">score</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">new_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openvino rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/openvino_rerank/)[Next Prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/)
