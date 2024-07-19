Title: Multi document agents - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/

Markdown Content:
Multi document agents - LlamaIndex


MultiDocumentAgentsPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/#llama_index.packs.multi_document_agents.MultiDocumentAgentsPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Multi-document Agents pack.

Given a set of documents, build our multi-document agents architecture. - setup a document agent over agent doc (capable of QA and summarization) - setup a top-level agent over doc agents

Source code in `llama-index-packs/llama-index-packs-multi-document-agents/llama_index/packs/multi_document_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
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
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MultiDocumentAgentsPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Multi-document Agents pack.</span>

<span class="sd">    Given a set of documents, build our multi-document agents architecture.</span>
<span class="sd">    - setup a document agent over agent doc (capable of QA and summarization)</span>
<span class="sd">    - setup a top-level agent over doc agents</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">doc_titles</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">doc_descriptions</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>

        <span class="c1"># Build agents dictionary</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agents</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="c1"># this is for the baseline</span>
        <span class="n">all_nodes</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># build agent for each document</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
            <span class="n">doc_title</span> <span class="o">=</span> <span class="n">doc_titles</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="n">doc_description</span> <span class="o">=</span> <span class="n">doc_descriptions</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">([</span><span class="n">doc</span><span class="p">])</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

            <span class="c1"># build vector index</span>
            <span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>

            <span class="c1"># build summary index</span>
            <span class="n">summary_index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">)</span>
            <span class="c1"># define query engines</span>
            <span class="n">vector_query_engine</span> <span class="o">=</span> <span class="n">vector_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
            <span class="n">summary_query_engine</span> <span class="o">=</span> <span class="n">summary_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

            <span class="c1"># define tools</span>
            <span class="n">query_engine_tools</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">QueryEngineTool</span><span class="p">(</span>
                    <span class="n">query_engine</span><span class="o">=</span><span class="n">vector_query_engine</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">ToolMetadata</span><span class="p">(</span>
                        <span class="n">name</span><span class="o">=</span><span class="s2">"vector_tool"</span><span class="p">,</span>
                        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
                            <span class="s2">"Useful for questions related to specific aspects of"</span>
                            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">doc_title</span><span class="si">}</span><span class="s2">."</span>
                        <span class="p">),</span>
                    <span class="p">),</span>
                <span class="p">),</span>
                <span class="n">QueryEngineTool</span><span class="p">(</span>
                    <span class="n">query_engine</span><span class="o">=</span><span class="n">summary_query_engine</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">ToolMetadata</span><span class="p">(</span>
                        <span class="n">name</span><span class="o">=</span><span class="s2">"summary_tool"</span><span class="p">,</span>
                        <span class="n">description</span><span class="o">=</span><span class="p">(</span>
                            <span class="s2">"Useful for any requests that require a holistic summary"</span>
                            <span class="sa">f</span><span class="s2">" of EVERYTHING about </span><span class="si">{</span><span class="n">doc_title</span><span class="si">}</span><span class="s2">. "</span>
                        <span class="p">),</span>
                    <span class="p">),</span>
                <span class="p">),</span>
            <span class="p">]</span>

            <span class="c1"># build agent</span>
            <span class="n">function_llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">)</span>
            <span class="n">agent</span> <span class="o">=</span> <span class="n">OpenAIAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
                <span class="n">query_engine_tools</span><span class="p">,</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">function_llm</span><span class="p">,</span>
                <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">system_prompt</span><span class="o">=</span><span class="sa">f</span><span class="s2">"""</span><span class="se">\</span>
<span class="s2">        You are a specialized agent designed to answer queries about </span><span class="si">{</span><span class="n">doc_title</span><span class="si">}</span><span class="s2">.</span>
<span class="s2">        You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.</span><span class="se">\</span>
<span class="s2">        """</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">[</span><span class="n">doc_title</span><span class="p">]</span> <span class="o">=</span> <span class="n">agent</span>

        <span class="c1"># build top-level, retrieval-enabled OpenAI Agent</span>
        <span class="c1"># define tool for each document agent</span>
        <span class="n">all_tools</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">doc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">docs</span><span class="p">):</span>
            <span class="n">doc_title</span> <span class="o">=</span> <span class="n">doc_titles</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="n">doc_description</span> <span class="o">=</span> <span class="n">doc_descriptions</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="n">wiki_summary</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Use this tool if you want to answer any questions about </span><span class="si">{</span><span class="n">doc_title</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="sa">f</span><span class="s2">"Doc description: </span><span class="si">{</span><span class="n">doc_description</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">doc_tool</span> <span class="o">=</span> <span class="n">QueryEngineTool</span><span class="p">(</span>
                <span class="n">query_engine</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">[</span><span class="n">doc_title</span><span class="p">],</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">ToolMetadata</span><span class="p">(</span>
                    <span class="n">name</span><span class="o">=</span><span class="sa">f</span><span class="s2">"tool_</span><span class="si">{</span><span class="n">doc_title</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">description</span><span class="o">=</span><span class="n">wiki_summary</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="n">all_tools</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc_tool</span><span class="p">)</span>

        <span class="n">tool_mapping</span> <span class="o">=</span> <span class="n">SimpleToolNodeMapping</span><span class="o">.</span><span class="n">from_objects</span><span class="p">(</span><span class="n">all_tools</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">obj_index</span> <span class="o">=</span> <span class="n">ObjectIndex</span><span class="o">.</span><span class="n">from_objects</span><span class="p">(</span>
            <span class="n">all_tools</span><span class="p">,</span>
            <span class="n">tool_mapping</span><span class="p">,</span>
            <span class="n">VectorStoreIndex</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">top_agent</span> <span class="o">=</span> <span class="n">FnRetrieverOpenAIAgent</span><span class="o">.</span><span class="n">from_retriever</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">obj_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">3</span><span class="p">),</span>
            <span class="n">system_prompt</span><span class="o">=</span><span class="s2">""" </span><span class="se">\</span>
<span class="s2">        You are an agent designed to answer queries about a set of given cities.</span>
<span class="s2">        Please always use the tools provided to answer a question. Do not rely on prior knowledge.</span><span class="se">\</span>

<span class="s2">        """</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"top_agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_agent</span><span class="p">,</span>
            <span class="s2">"obj_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">obj_index</span><span class="p">,</span>
            <span class="s2">"doc_agents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_agent</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/#llama_index.packs.multi_document_agents.MultiDocumentAgentsPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-multi-document-agents/llama_index/packs/multi_document_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"top_agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_agent</span><span class="p">,</span>
        <span class="s2">"obj_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">obj_index</span><span class="p">,</span>
        <span class="s2">"doc_agents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/#llama_index.packs.multi_document_agents.MultiDocumentAgentsPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-multi-document-agents/llama_index/packs/multi_document_agents/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_agent</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mixture of agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/)[Next Multi tenancy rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/)
