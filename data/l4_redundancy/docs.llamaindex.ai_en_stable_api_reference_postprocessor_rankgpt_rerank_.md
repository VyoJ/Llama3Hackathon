Title: Rankgpt rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/

Markdown Content:
Rankgpt rerank - LlamaIndex


RankGPTRerank [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/#llama_index.postprocessor.rankgpt_rerank.RankGPTRerank "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

RankGPT-based reranker.

Source code in `llama-index-integrations/postprocessor/llama-index-postprocessor-rankgpt-rerank/llama_index/postprocessor/rankgpt_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
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
<span class="normal">189</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RankGPTRerank</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RankGPT-based reranker."""</span>

    <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Top N nodes to return from reranking."</span><span class="p">)</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Whether to print intermediate steps."</span>
    <span class="p">)</span>
    <span class="n">rankgpt_rerank_prompt</span><span class="p">:</span> <span class="n">BasePromptTemplate</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"rankGPT rerank prompt."</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">rankgpt_rerank_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="n">rankgpt_rerank_prompt</span> <span class="o">=</span> <span class="n">rankgpt_rerank_prompt</span> <span class="ow">or</span> <span class="n">RANKGPT_RERANK_PROMPT</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">top_n</span><span class="o">=</span><span class="n">top_n</span><span class="p">,</span>
            <span class="n">rankgpt_rerank_prompt</span><span class="o">=</span><span class="n">rankgpt_rerank_prompt</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"RankGPTRerank"</span>

    <span class="k">def</span> <span class="nf">_ensure_llm</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">llama_index.llms.openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo-16k"</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span>
                    <span class="s2">"OpenAI LLM is not available. Please install `llama-index-llms-openai` "</span>
                    <span class="s2">"or provide an alternative LLM instance."</span>
                <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">ReRankStartEvent</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_bundle</span><span class="p">,</span>
                <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
                <span class="n">top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">,</span>
                <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query bundle must be provided."</span><span class="p">)</span>

        <span class="n">items</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="s2">"hits"</span><span class="p">:</span> <span class="p">[</span>
                <span class="p">{</span><span class="s2">"content"</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)}</span>
                <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span>
            <span class="p">],</span>
        <span class="p">}</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_permutation_instruction</span><span class="p">(</span><span class="n">item</span><span class="o">=</span><span class="n">items</span><span class="p">)</span>
        <span class="n">permutation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_llm</span><span class="p">(</span><span class="n">messages</span><span class="o">=</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">permutation</span><span class="o">.</span><span class="n">message</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">permutation</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">rerank_ranks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_receive_permutation</span><span class="p">(</span>
                <span class="n">items</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">permutation</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"After Reranking, new rank list for nodes: </span><span class="si">{</span><span class="n">rerank_ranks</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">initial_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">rerank_ranks</span><span class="p">:</span>
                <span class="n">initial_results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">nodes</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">nodes</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>
                <span class="p">)</span>

            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">ReRankEndEvent</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">initial_results</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">]))</span>
            <span class="k">return</span> <span class="n">initial_results</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span><span class="n">ReRankEndEvent</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">]))</span>
            <span class="k">return</span> <span class="n">nodes</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_n</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"rankgpt_rerank_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">rankgpt_rerank_prompt</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"rankgpt_rerank_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rankgpt_rerank_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"rankgpt_rerank_prompt"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_prefix_prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"You are RankGPT, an intelligent assistant that can rank passages based on their relevancy to the query."</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"I will provide you with </span><span class="si">{</span><span class="n">num</span><span class="si">}</span><span class="s2"> passages, each indicated by number identifier []. </span><span class="se">\n</span><span class="s2">Rank the passages based on their relevance to query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">."</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="s2">"Okay, please provide the passages."</span><span class="p">),</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_post_prompt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rankgpt_rerank_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">create_permutation_instruction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]</span>
        <span class="n">num</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">])</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_prefix_prompt</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">num</span><span class="p">)</span>
        <span class="n">rank</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">item</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">]:</span>
            <span class="n">rank</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">hit</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"Title: Content: "</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="c1"># For Japanese should cut by character: content = content[:int(max_length)]</span>
            <span class="n">content</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">content</span><span class="o">.</span><span class="n">split</span><span class="p">()[:</span><span class="mi">300</span><span class="p">])</span>
            <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="n">rank</span><span class="si">}</span><span class="s2">] </span><span class="si">{</span><span class="n">content</span><span class="si">}</span><span class="s2">"</span><span class="p">))</span>
            <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Received passage [</span><span class="si">{</span><span class="n">rank</span><span class="si">}</span><span class="s2">]."</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="n">messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_post_prompt</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">num</span><span class="p">))</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">messages</span>

    <span class="k">def</span> <span class="nf">run_llm</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_llm</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_clean_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">new_response</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">c</span><span class="o">.</span><span class="n">isdigit</span><span class="p">():</span>
                <span class="n">new_response</span> <span class="o">+=</span> <span class="s2">" "</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">new_response</span> <span class="o">+=</span> <span class="n">c</span>
        <span class="k">return</span> <span class="n">new_response</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_remove_duplicate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]:</span>
        <span class="n">new_response</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">c</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">new_response</span><span class="p">:</span>
                <span class="n">new_response</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_response</span>

    <span class="k">def</span> <span class="nf">_receive_permutation</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">permutation</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]:</span>
        <span class="n">rank_end</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">item</span><span class="p">[</span><span class="s2">"hits"</span><span class="p">])</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clean_response</span><span class="p">(</span><span class="n">permutation</span><span class="p">)</span>
        <span class="n">response_list</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">split</span><span class="p">()]</span>
        <span class="n">response_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_duplicate</span><span class="p">(</span><span class="n">response_list</span><span class="p">)</span>
        <span class="n">response_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">ss</span> <span class="k">for</span> <span class="n">ss</span> <span class="ow">in</span> <span class="n">response_list</span> <span class="k">if</span> <span class="n">ss</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">rank_end</span><span class="p">)]</span>
        <span class="k">return</span> <span class="n">response_list</span> <span class="o">+</span> <span class="p">[</span>
            <span class="n">tt</span> <span class="k">for</span> <span class="n">tt</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">rank_end</span><span class="p">)</span> <span class="k">if</span> <span class="n">tt</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">response_list</span>
        <span class="p">]</span>  <span class="c1"># add the rest of the rank</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/)[Next Rankllm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankllm_rerank/)
