Title: Corrective rag - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/

Markdown Content:
Corrective rag - LlamaIndex


CorrectiveRAGPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/#llama_index.packs.corrective_rag.CorrectiveRAGPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-corrective-rag/llama_index/packs/corrective_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CorrectiveRAGPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">tavily_ai_apikey</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">relevancy_pipeline</span> <span class="o">=</span> <span class="n">QueryPipeline</span><span class="p">(</span>
            <span class="n">chain</span><span class="o">=</span><span class="p">[</span><span class="n">DEFAULT_RELEVANCY_PROMPT_TEMPLATE</span><span class="p">,</span> <span class="n">llm</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">transform_query_pipeline</span> <span class="o">=</span> <span class="n">QueryPipeline</span><span class="p">(</span>
            <span class="n">chain</span><span class="o">=</span><span class="p">[</span><span class="n">DEFAULT_TRANSFORM_QUERY_TEMPLATE</span><span class="p">,</span> <span class="n">llm</span><span class="p">]</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tavily_tool</span> <span class="o">=</span> <span class="n">TavilyToolSpec</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">tavily_ai_apikey</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">retrieve_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Retrieve the relevant nodes for the query."""</span>
        <span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">evaluate_relevancy</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">retrieved_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Evaluate relevancy of retrieved documents with the query."""</span>
        <span class="n">relevancy_results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span><span class="p">:</span>
            <span class="n">relevancy</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">relevancy_pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="n">context_str</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span>
            <span class="p">)</span>
            <span class="n">relevancy_results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">relevancy</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">relevancy_results</span>

    <span class="k">def</span> <span class="nf">extract_relevant_texts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">retrieved_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span> <span class="n">relevancy_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Extract relevant texts from retrieved documents."""</span>
        <span class="n">relevant_texts</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">retrieved_nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">text</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">result</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">relevancy_results</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">result</span> <span class="o"></span> <span class="s2">"yes"</span>
    <span class="p">]</span>
    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">relevant_texts</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### search\_with\_transformed\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/#llama_index.packs.corrective_rag.CorrectiveRAGPack.search_with_transformed_query "Permanent link")

```
search_with_transformed_query(query_str: str) -> str
```

Search the transformed query with Tavily API.

Source code in `llama-index-packs/llama-index-packs-corrective-rag/llama_index/packs/corrective_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">search_with_transformed_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Search the transformed query with Tavily API."""</span>
    <span class="n">search_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tavily_tool</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">max_results</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">result</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### get\_result [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/#llama_index.packs.corrective_rag.CorrectiveRAGPack.get_result "Permanent link")

```
get_result(relevant_text: str, search_text: str, query_str: str) -> Any
```

Get result with relevant text.

Source code in `llama-index-packs/llama-index-packs-corrective-rag/llama_index/packs/corrective_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">relevant_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">search_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get result with relevant text."""</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">relevant_text</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">search_text</span><span class="p">)]</span>
    <span class="n">index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
    <span class="n">query_engine</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/#llama_index.packs.corrective_rag.CorrectiveRAGPack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-corrective-rag/llama_index/packs/corrective_rag/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="c1"># Retrieve nodes based on the input query string.</span>
    <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_nodes</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="c1"># Evaluate the relevancy of each retrieved document in relation to the query string.</span>
    <span class="n">relevancy_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate_relevancy</span><span class="p">(</span><span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">query_str</span><span class="p">)</span>
    <span class="c1"># Extract texts from documents that are deemed relevant based on the evaluation.</span>
    <span class="n">relevant_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_relevant_texts</span><span class="p">(</span><span class="n">retrieved_nodes</span><span class="p">,</span> <span class="n">relevancy_results</span><span class="p">)</span>

    <span class="c1"># Initialize search_text variable to handle cases where it might not get defined.</span>
    <span class="n">search_text</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="c1"># If any document is found irrelevant, transform the query string for better search results.</span>
    <span class="k">if</span> <span class="s2">"no"</span> <span class="ow">in</span> <span class="n">relevancy_results</span><span class="p">:</span>
        <span class="n">transformed_query_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">transform_query_pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_str</span>
        <span class="p">)</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
        <span class="c1"># Conduct a search with the transformed query string and collect the results.</span>
        <span class="n">search_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_with_transformed_query</span><span class="p">(</span><span class="n">transformed_query_str</span><span class="p">)</span>

    <span class="c1"># Compile the final result. If there's additional search text from the transformed query,</span>
    <span class="c1"># it's included; otherwise, only the relevant text from the initial retrieval is returned.</span>
    <span class="k">if</span> <span class="n">search_text</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_result</span><span class="p">(</span><span class="n">relevant_text</span><span class="p">,</span> <span class="n">search_text</span><span class="p">,</span> <span class="n">query_str</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_result</span><span class="p">(</span><span class="n">relevant_text</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cohere citation chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/)[Next Deeplake deepmemory retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/)
