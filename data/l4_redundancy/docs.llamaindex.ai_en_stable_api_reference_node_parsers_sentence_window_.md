Title: Sentence window - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/

Markdown Content:
Sentence window - LlamaIndex


Node parsers.

SentenceWindowNodeParser [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/#llama_index.core.node_parser.SentenceWindowNodeParser "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[NodeParser](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/#llama_index.core.node_parser.interface.NodeParser "llama_index.core.node_parser.interface.NodeParser")`

Sentence window node parser.

Splits a document into Nodes, with each node being a sentence. Each node contains a window from the surrounding sentences in the metadata.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sentence_splitter` | `Optional[Callable]` | 
splits text into sentences



 | _required_ |
| `include_metadata` | `bool` | 

whether to include metadata in nodes



 | _required_ |
| `include_prev_next_rel` | `bool` | 

whether to include prev/next relationships



 | _required_ |

Source code in `llama-index-core/llama_index/core/node_parser/text/sentence_window.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 21</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SentenceWindowNodeParser</span><span class="p">(</span><span class="n">NodeParser</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Sentence window node parser.</span>

<span class="sd">    Splits a document into Nodes, with each node being a sentence.</span>
<span class="sd">    Each node contains a window from the surrounding sentences in the metadata.</span>

<span class="sd">    Args:</span>
<span class="sd">        sentence_splitter (Optional[Callable]): splits text into sentences</span>
<span class="sd">        include_metadata (bool): whether to include metadata in nodes</span>
<span class="sd">        include_prev_next_rel (bool): whether to include prev/next relationships</span>
<span class="sd">    """</span>

    <span class="n">sentence_splitter</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">split_by_sentence_tokenizer</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The text splitter to use when splitting documents."</span><span class="p">,</span>
        <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">window_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_WINDOW_SIZE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of sentences on each side of a sentence to capture."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">window_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_WINDOW_METADATA_KEY</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The metadata key to store the sentence window under."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">original_text_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_OG_TEXT_METADATA_KEY</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The metadata key to store the original sentence in."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"SentenceWindowNodeParser"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">sentence_splitter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">window_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_WINDOW_SIZE</span><span class="p">,</span>
        <span class="n">window_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_WINDOW_METADATA_KEY</span><span class="p">,</span>
        <span class="n">original_text_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_OG_TEXT_METADATA_KEY</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SentenceWindowNodeParser"</span><span class="p">:</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

        <span class="n">sentence_splitter</span> <span class="o">=</span> <span class="n">sentence_splitter</span> <span class="ow">or</span> <span class="n">split_by_sentence_tokenizer</span><span class="p">()</span>

        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">sentence_splitter</span><span class="o">=</span><span class="n">sentence_splitter</span><span class="p">,</span>
            <span class="n">window_size</span><span class="o">=</span><span class="n">window_size</span><span class="p">,</span>
            <span class="n">window_metadata_key</span><span class="o">=</span><span class="n">window_metadata_key</span><span class="p">,</span>
            <span class="n">original_text_metadata_key</span><span class="o">=</span><span class="n">original_text_metadata_key</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_parse_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse document into nodes."""</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">nodes_with_progress</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Parsing nodes"</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_with_progress</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_window_nodes_from_documents</span><span class="p">([</span><span class="n">node</span><span class="p">])</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>

    <span class="k">def</span> <span class="nf">build_window_nodes_from_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Build window nodes from documents."""</span>
        <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">text</span>
            <span class="n">text_splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sentence_splitter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">build_nodes_from_splits</span><span class="p">(</span>
                <span class="n">text_splits</span><span class="p">,</span>
                <span class="n">doc</span><span class="p">,</span>
                <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># add window to each node</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
                <span class="n">window_nodes</span> <span class="o">=</span> <span class="n">nodes</span><span class="p">[</span>
                    <span class="nb">max</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">i</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">window_size</span><span class="p">)</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span>
                        <span class="n">i</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">window_size</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
                    <span class="p">)</span>
                <span class="p">]</span>

                <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">]</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">window_nodes</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">text</span>

                <span class="c1"># exclude window metadata from embed and llm</span>
                <span class="n">node</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span>
                <span class="p">)</span>

            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_nodes</span>
</code></pre></div></td></tr></tbody></table>

### build\_window\_nodes\_from\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/#llama_index.core.node_parser.SentenceWindowNodeParser.build_window_nodes_from_documents "Permanent link")

```
build_window_nodes_from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Build window nodes from documents.

Source code in `llama-index-core/llama_index/core/node_parser/text/sentence_window.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">101</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">build_window_nodes_from_documents</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Build window nodes from documents."""</span>
    <span class="n">all_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">text</span>
        <span class="n">text_splits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sentence_splitter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">build_nodes_from_splits</span><span class="p">(</span>
            <span class="n">text_splits</span><span class="p">,</span>
            <span class="n">doc</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># add window to each node</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">window_nodes</span> <span class="o">=</span> <span class="n">nodes</span><span class="p">[</span>
                <span class="nb">max</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">i</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">window_size</span><span class="p">)</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span>
                    <span class="n">i</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">window_size</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="p">]</span>

            <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">]</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">window_nodes</span><span class="p">]</span>
            <span class="p">)</span>
            <span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">text</span>

            <span class="c1"># exclude window metadata from embed and llm</span>
            <span class="n">node</span><span class="o">.</span><span class="n">excluded_embed_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span>
            <span class="p">)</span>
            <span class="n">node</span><span class="o">.</span><span class="n">excluded_llm_metadata_keys</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">window_metadata_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_text_metadata_key</span><span class="p">]</span>
            <span class="p">)</span>

        <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">all_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sentence splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/)[Next Token text splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/)
