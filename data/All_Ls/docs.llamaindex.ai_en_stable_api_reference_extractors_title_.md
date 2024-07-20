Title: Title - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/

Markdown Content:
Title - LlamaIndex


TitleExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/#llama_index.core.extractors.TitleExtractor "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Title extractor. Useful for long documents. Extracts `document_title` metadata field.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 
LLM



 | `None` |
| `nodes` | `int` | 

number of nodes from front to use for title extraction



 | `5` |
| `node_template` | `str` | 

template for node-level title clues extraction



 | `DEFAULT_TITLE_NODE_TEMPLATE` |
| `combine_template` | `str` | 

template for combining node-level clues into a document-level title



 | `DEFAULT_TITLE_COMBINE_TEMPLATE` |

Source code in `llama-index-core/llama_index/core/extractors/metadata_extractors.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 46</span>
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
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TitleExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Title extractor. Useful for long documents. Extracts `document_title`</span>
<span class="sd">    metadata field.</span>

<span class="sd">    Args:</span>
<span class="sd">        llm (Optional[LLM]): LLM</span>
<span class="sd">        nodes (int): number of nodes from front to use for title extraction</span>
<span class="sd">        node_template (str): template for node-level title clues extraction</span>
<span class="sd">        combine_template (str): template for combining node-level clues into</span>
<span class="sd">            a document-level title</span>
<span class="sd">    """</span>

    <span class="n">is_text_node_only</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># can work for mixture of text and non-text nodes</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">LLMPredictorType</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The LLM to use for generation."</span><span class="p">)</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of nodes to extract titles from."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">node_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_TITLE_NODE_TEMPLATE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The prompt template to extract titles with."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">combine_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_TITLE_COMBINE_TEMPLATE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The prompt template to merge titles with."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># TODO: llm_predictor arg is deprecated</span>
        <span class="n">llm_predictor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMPredictorType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">node_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TITLE_NODE_TEMPLATE</span><span class="p">,</span>
        <span class="n">combine_template</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TITLE_COMBINE_TEMPLATE</span><span class="p">,</span>
        <span class="n">num_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_NUM_WORKERS</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">nodes</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"num_nodes must be &gt;= 1"</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_predictor</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">node_template</span><span class="o">=</span><span class="n">node_template</span><span class="p">,</span>
            <span class="n">combine_template</span><span class="o">=</span><span class="n">combine_template</span><span class="p">,</span>
            <span class="n">num_workers</span><span class="o">=</span><span class="n">num_workers</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"TitleExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="n">nodes_by_doc_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">separate_nodes_by_ref_id</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">titles_by_doc_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_titles</span><span class="p">(</span><span class="n">nodes_by_doc_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[{</span><span class="s2">"document_title"</span><span class="p">:</span> <span class="n">titles_by_doc_id</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">]}</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">filter_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
        <span class="n">filtered_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
                <span class="k">continue</span>
            <span class="n">filtered_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">filtered_nodes</span>

    <span class="k">def</span> <span class="nf">separate_nodes_by_ref_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="n">separated_items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">ref_doc_id</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">separated_items</span><span class="p">:</span>
                <span class="n">separated_items</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">separated_items</span><span class="p">[</span><span class="n">key</span><span class="p">])</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">:</span>
                <span class="n">separated_items</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">separated_items</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">extract_titles</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes_by_doc_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="n">titles_by_doc_id</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">nodes_by_doc_id</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">title_candidates</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_title_candidates</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
            <span class="n">combined_titles</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">title_candidates</span><span class="p">)</span>
            <span class="n">titles_by_doc_id</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
                <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">combine_template</span><span class="p">),</span>
                <span class="n">context_str</span><span class="o">=</span><span class="n">combined_titles</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">titles_by_doc_id</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">get_title_candidates</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">title_jobs</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
                <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node_template</span><span class="p">),</span>
                <span class="n">context_str</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">TextNode</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">run_jobs</span><span class="p">(</span>
            <span class="n">title_jobs</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="n">workers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_workers</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Summary](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/)[Next Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/anthropic/)
