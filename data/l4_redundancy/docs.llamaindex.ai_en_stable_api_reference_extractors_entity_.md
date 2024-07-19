Title: Entity - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/

Markdown Content:
Entity - LlamaIndex


EntityExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/#llama_index.extractors.entity.EntityExtractor "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Entity extractor. Extracts `entities` into a metadata field using a default model `tomaarsen/span-marker-mbert-base-multinerd` and the SpanMarker library.

Install SpanMarker with `pip install span-marker`.

Source code in `llama-index-integrations/extractors/llama-index-extractors-entity/llama_index/extractors/entity/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 31</span>
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
<span class="normal">152</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EntityExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Entity extractor. Extracts `entities` into a metadata field using a default model</span>
<span class="sd">    `tomaarsen/span-marker-mbert-base-multinerd` and the SpanMarker library.</span>

<span class="sd">    Install SpanMarker with `pip install span-marker`.</span>
<span class="sd">    """</span>

    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_ENTITY_MODEL</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The model name of the SpanMarker model to use."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">prediction_threshold</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The confidence threshold for accepting predictions."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
        <span class="n">lte</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">span_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">" "</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The separator between entity names."</span>
    <span class="p">)</span>
    <span class="n">label_entities</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Include entity class labels or not."</span>
    <span class="p">)</span>
    <span class="n">device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Device to run model on, i.e. 'cuda', 'cpu'"</span>
    <span class="p">)</span>
    <span class="n">entity_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Mapping of entity class names to usable names."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">_tokenizer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_model</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_ENTITY_MODEL</span><span class="p">,</span>
        <span class="n">prediction_threshold</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span>
        <span class="n">span_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">" "</span><span class="p">,</span>
        <span class="n">label_entities</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">entity_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Entity extractor for extracting entities from text and inserting</span>
<span class="sd">        into node metadata.</span>

<span class="sd">        Args:</span>
<span class="sd">            model_name (str):</span>
<span class="sd">                Name of the SpanMarker model to use.</span>
<span class="sd">            prediction_threshold (float):</span>
<span class="sd">                Minimum prediction threshold for entities. Defaults to 0.5.</span>
<span class="sd">            span_joiner (str):</span>
<span class="sd">                String to join spans with. Defaults to " ".</span>
<span class="sd">            label_entities (bool):</span>
<span class="sd">                Whether to label entities with their type. Setting to true can be</span>
<span class="sd">                slightly error prone, but can be useful for downstream tasks.</span>
<span class="sd">                Defaults to False.</span>
<span class="sd">            device (Optional[str]):</span>
<span class="sd">                Device to use for SpanMarker model, i.e. "cpu" or "cuda".</span>
<span class="sd">                Loads onto "cpu" by default.</span>
<span class="sd">            entity_map (Optional[Dict[str, str]]):</span>
<span class="sd">                Mapping from entity class name to label.</span>
<span class="sd">            tokenizer (Optional[Callable[[str], List[str]]]):</span>
<span class="sd">                Tokenizer to use for splitting text into words.</span>
<span class="sd">                Defaults to NLTK word_tokenize.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="n">SpanMarkerModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">model_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">device</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span> <span class="ow">or</span> <span class="n">word_tokenize</span>

        <span class="n">base_entity_map</span> <span class="o">=</span> <span class="n">DEFAULT_ENTITY_MAP</span>
        <span class="k">if</span> <span class="n">entity_map</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">base_entity_map</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">entity_map</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">model_name</span><span class="o">=</span><span class="n">model_name</span><span class="p">,</span>
            <span class="n">prediction_threshold</span><span class="o">=</span><span class="n">prediction_threshold</span><span class="p">,</span>
            <span class="n">span_joiner</span><span class="o">=</span><span class="n">span_joiner</span><span class="p">,</span>
            <span class="n">label_entities</span><span class="o">=</span><span class="n">label_entities</span><span class="p">,</span>
            <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">,</span>
            <span class="n">entity_map</span><span class="o">=</span><span class="n">base_entity_map</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"EntityExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="c1"># Extract node-level entity metadata</span>
        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[{}</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="n">metadata_queue</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)),</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Extracting entities"</span>
        <span class="p">)</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">metadata_queue</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">metadata_list</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
            <span class="n">node_text</span> <span class="o">=</span> <span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_mode</span><span class="p">)</span>
            <span class="n">words</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">(</span><span class="n">node_text</span><span class="p">)</span>
            <span class="n">spans</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">spans</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">span</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">prediction_threshold</span><span class="p">:</span>
                    <span class="n">ent_label</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">span</span><span class="p">[</span><span class="s2">"label"</span><span class="p">],</span> <span class="n">span</span><span class="p">[</span><span class="s2">"label"</span><span class="p">])</span>
                    <span class="n">metadata_label</span> <span class="o">=</span> <span class="n">ent_label</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">label_entities</span> <span class="k">else</span> <span class="s2">"entities"</span>

                    <span class="k">if</span> <span class="n">metadata_label</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">metadata</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="p">[</span><span class="n">metadata_label</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>

                    <span class="n">metadata</span><span class="p">[</span><span class="n">metadata_label</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">span_joiner</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">span</span><span class="p">[</span><span class="s2">"span"</span><span class="p">]))</span>

        <span class="c1"># convert metadata from set to list</span>
        <span class="k">for</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="n">metadata_list</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">metadata</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">metadata</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">val</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Vector memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/extractors/)
