Title: Raft dataset - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/

Markdown Content:
Raft dataset - LlamaIndex


RAFTDatasetPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

RAFT Dataset Generator pack.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 28</span>
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
<span class="normal">226</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RAFTDatasetPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RAFT Dataset Generator pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">num_questions_per_chunk</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">num_distract_docs</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_SIZE</span><span class="p">,</span>
        <span class="n">default_breakpoint_percentile_threshold</span><span class="o">=</span><span class="n">DEFAULT_BREAKPOINT_PERCENTILE_THRESHOLD</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_path</span> <span class="o">=</span> <span class="n">file_path</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_questions_per_chunk</span> <span class="o">=</span> <span class="n">num_questions_per_chunk</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span> <span class="o">=</span> <span class="n">num_distract_docs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span> <span class="o">=</span> <span class="n">chunk_size</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">default_breakpoint_percentile_threshold</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">default_breakpoint_percentile_threshold</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4"</span><span class="p">)</span> <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span> <span class="o">=</span> <span class="n">OpenAIEmbedding</span><span class="p">()</span> <span class="k">if</span> <span class="n">embed_model</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">embed_model</span>

    <span class="k">def</span> <span class="nf">strip_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Helper function for helping format strings returned by GPT-4.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"assistant:"</span><span class="p">):</span>  <span class="c1"># Check if the string starts with 'assistant '</span>
            <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"assistant:"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>  <span class="c1"># Replace the first occurrence</span>

        <span class="n">start_index</span><span class="p">,</span> <span class="n">end_index</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="n">beg_found</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)):</span>
            <span class="k">if</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">isalpha</span><span class="p">():</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">beg_found</span><span class="p">:</span>
                    <span class="n">start_index</span> <span class="o">=</span> <span class="n">i</span>
                    <span class="n">beg_found</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">end_index</span> <span class="o">=</span> <span class="n">i</span>
        <span class="n">end_index</span> <span class="o">+=</span> <span class="mi">2</span>
        <span class="k">return</span> <span class="n">s</span><span class="p">[</span><span class="n">start_index</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span><span class="n">end_index</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">))]</span>

    <span class="k">def</span> <span class="nf">encode_question_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">chunk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Encode multiple prompt instructions into a single string for the general case.</span>
<span class="sd">        """</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            Question: </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="se">\n</span><span class="s2">Context: </span><span class="si">{</span><span class="n">chunk</span><span class="si">}</span><span class="se">\n</span>
<span class="s2">            Answer this question using the information given in the context above. Here is things to pay attention to:</span>
<span class="s2">            - First provide step-by-step reasoning on how to answer the question.</span>
<span class="s2">            - In the reasoning, if you need to copy paste some sentences from the context, include them in ##begin_quote## and ##end_quote##. This would mean that things outside of ##begin_quote## and ##end_quote## are not directly copy paste from the context.</span>
<span class="s2">            - End your response with final answer in the form &lt;ANSWER&gt;: $answer, the answer should be succinct.</span>
<span class="s2">        """</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"You are a helpful question answerer who can provide an answer given a question and relevant context."</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">prompt</span><span class="p">),</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">generate_label</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generates the label / answer to `question` using `context` and GPT-4.</span>
<span class="sd">        """</span>
        <span class="n">question_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">encode_question_gen</span><span class="p">(</span><span class="n">question</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">question_messages</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate_instructions_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">chunk</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generates `x` questions / use cases for `chunk`. Used when the input document is of general types</span>
<span class="sd">        `pdf`, `json`, or `txt`.</span>
<span class="sd">        """</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">"You are a synthetic question-answer pair generator. Given a chunk of context about some topic(s), generate </span><span class="si">%s</span><span class="s2"> example questions a user could ask and would be answered using information from the chunk. For example, if the given context was a Wikipedia paragraph about the United States, an example question could be 'How many states are in the United States?'. The questions should be able to be answered in a few words or less."</span>
                <span class="o">%</span> <span class="p">(</span><span class="n">x</span><span class="p">),</span>
            <span class="p">),</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk</span><span class="p">)),</span>
        <span class="p">]</span>

        <span class="n">queries</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">))</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">questions</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">strip_str</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
        <span class="n">questions</span> <span class="o">=</span> <span class="p">[</span><span class="n">q</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">questions</span> <span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">isalpha</span><span class="p">()</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">q</span><span class="p">)][:</span><span class="n">x</span><span class="p">]</span>

        <span class="n">num_questions_generated</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">questions</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">num_questions_generated</span> <span class="o">&lt;</span> <span class="n">x</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Fewer questions generated (</span><span class="si">{</span><span class="n">num_questions_generated</span><span class="si">}</span><span class="s2">) "</span>
                <span class="sa">f</span><span class="s2">"than requested (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">)."</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">questions</span>

    <span class="k">def</span> <span class="nf">get_chunks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Takes in a `file_path`, retrieves the document, breaks it down into chunks of size</span>
<span class="sd">        `chunk_size`, and returns the chunks.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">input_files</span><span class="o">=</span><span class="p">[</span><span class="n">file_path</span><span class="p">])</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="n">splitter</span> <span class="o">=</span> <span class="n">SemanticSplitterNodeParser</span><span class="p">(</span>
            <span class="n">buffer_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">breakpoint_percentile_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">default_breakpoint_percentile_threshold</span><span class="p">,</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">add_chunk_to_dataset</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">,</span>
        <span class="n">chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">x</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">num_distract</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">p</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Given a chunk, create {Q, A, D} triplets and add them to the dataset.</span>
<span class="sd">        """</span>
        <span class="n">i</span> <span class="o">=</span> <span class="n">chunks</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
        <span class="n">qs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_instructions_gen</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">qs</span><span class="p">:</span>
            <span class="n">datapt</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"id"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"question"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"context"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"oracle_context"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"cot_answer"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="p">}</span>

            <span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"seed_task_</span><span class="si">{</span><span class="mi">0</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="ow">not</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="o">.</span><span class="n">num_rows</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"general"</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="n">q</span>

            <span class="c1"># add distractor docs</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">chunk</span><span class="p">]</span>
            <span class="n">indices</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)))</span>
            <span class="n">indices</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">random</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">indices</span><span class="p">,</span> <span class="n">num_distract</span><span class="p">):</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chunks</span><span class="p">[</span><span class="n">j</span><span class="p">])</span>
            <span class="c1"># decides whether to add oracle document</span>
            <span class="n">oracle</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">p</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">oracle</span><span class="p">:</span>
                <span class="n">docs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">chunks</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">indices</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]]</span>
            <span class="n">random</span><span class="o">.</span><span class="n">shuffle</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

            <span class="n">d</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"sentences"</span><span class="p">:</span> <span class="p">[]}</span>

            <span class="n">d</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="s2">"placeholder_title"</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">num_distract</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
            <span class="n">d</span><span class="p">[</span><span class="s2">"sentences"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">d</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">chunk</span>

            <span class="c1"># add answer to q</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_label</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">chunk</span><span class="p">)</span>

            <span class="c1"># construct model instruction</span>
            <span class="n">context</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
                <span class="n">context</span> <span class="o">+=</span> <span class="s2">"&lt;DOCUMENT&gt;"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"&lt;/DOCUMENT&gt;</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">context</span> <span class="o">+=</span> <span class="n">q</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>

            <span class="c1"># add to dataset</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="p">:</span>
                <span class="c1"># init ds</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]]</span>
                <span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]]</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">ds</span> <span class="o">=</span> <span class="n">Dataset</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">datapt</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">ds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="n">datapt</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="n">chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_chunks</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_path</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Number of chunks created: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span> <span class="o">=</span> <span class="p">(</span>
            <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">))</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="p">)</span>  <span class="c1"># should be less than number of chunks/ nodes created</span>

        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">chunks</span><span class="p">):</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Processing chunk: </span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">add_chunk_to_dataset</span><span class="p">(</span>
                <span class="n">chunks</span><span class="p">,</span> <span class="n">chunk</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_questions_per_chunk</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span>
</code></pre></div></td></tr></tbody></table>

### strip\_str [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.strip_str "Permanent link")

```
strip_str(s) -> str
```

Helper function for helping format strings returned by GPT-4.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
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
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">strip_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Helper function for helping format strings returned by GPT-4.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"assistant:"</span><span class="p">):</span>  <span class="c1"># Check if the string starts with 'assistant '</span>
        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"assistant:"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>  <span class="c1"># Replace the first occurrence</span>

    <span class="n">start_index</span><span class="p">,</span> <span class="n">end_index</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">beg_found</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)):</span>
        <span class="k">if</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">isalpha</span><span class="p">():</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">beg_found</span><span class="p">:</span>
                <span class="n">start_index</span> <span class="o">=</span> <span class="n">i</span>
                <span class="n">beg_found</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">end_index</span> <span class="o">=</span> <span class="n">i</span>
    <span class="n">end_index</span> <span class="o">+=</span> <span class="mi">2</span>
    <span class="k">return</span> <span class="n">s</span><span class="p">[</span><span class="n">start_index</span> <span class="p">:</span> <span class="nb">min</span><span class="p">(</span><span class="n">end_index</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">))]</span>
</code></pre></div></td></tr></tbody></table>

### encode\_question\_gen [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.encode_question_gen "Permanent link")

```
encode_question_gen(question, chunk) -> List[str]
```

Encode multiple prompt instructions into a single string for the general case.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

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
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">encode_question_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">chunk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Encode multiple prompt instructions into a single string for the general case.</span>
<span class="sd">    """</span>
    <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        Question: </span><span class="si">{</span><span class="n">question</span><span class="si">}</span><span class="se">\n</span><span class="s2">Context: </span><span class="si">{</span><span class="n">chunk</span><span class="si">}</span><span class="se">\n</span>
<span class="s2">        Answer this question using the information given in the context above. Here is things to pay attention to:</span>
<span class="s2">        - First provide step-by-step reasoning on how to answer the question.</span>
<span class="s2">        - In the reasoning, if you need to copy paste some sentences from the context, include them in ##begin_quote## and ##end_quote##. This would mean that things outside of ##begin_quote## and ##end_quote## are not directly copy paste from the context.</span>
<span class="s2">        - End your response with final answer in the form &lt;ANSWER&gt;: $answer, the answer should be succinct.</span>
<span class="s2">    """</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="p">(</span>
            <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span>
            <span class="n">content</span><span class="o">=</span><span class="s2">"You are a helpful question answerer who can provide an answer given a question and relevant context."</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">prompt</span><span class="p">),</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### generate\_label [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.generate_label "Permanent link")

```
generate_label(question, context) -> str
```

Generates the label / answer to `question` using `context` and GPT-4.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_label</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Generates the label / answer to `question` using `context` and GPT-4.</span>
<span class="sd">    """</span>
    <span class="n">question_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">encode_question_gen</span><span class="p">(</span><span class="n">question</span><span class="p">,</span> <span class="n">context</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">question_messages</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### generate\_instructions\_gen [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.generate_instructions_gen "Permanent link")

```
generate_instructions_gen(chunk, x=5) -> List[str]
```

Generates `x` questions / use cases for `chunk`. Used when the input document is of general types `pdf`, `json`, or `txt`.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 98</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_instructions_gen</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">chunk</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Generates `x` questions / use cases for `chunk`. Used when the input document is of general types</span>
<span class="sd">    `pdf`, `json`, or `txt`.</span>
<span class="sd">    """</span>
    <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="p">(</span>
            <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">,</span>
            <span class="n">content</span><span class="o">=</span><span class="s2">"You are a synthetic question-answer pair generator. Given a chunk of context about some topic(s), generate </span><span class="si">%s</span><span class="s2"> example questions a user could ask and would be answered using information from the chunk. For example, if the given context was a Wikipedia paragraph about the United States, an example question could be 'How many states are in the United States?'. The questions should be able to be answered in a few words or less."</span>
            <span class="o">%</span> <span class="p">(</span><span class="n">x</span><span class="p">),</span>
        <span class="p">),</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk</span><span class="p">)),</span>
    <span class="p">]</span>

    <span class="n">queries</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">))</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">questions</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">strip_str</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">]</span>
    <span class="n">questions</span> <span class="o">=</span> <span class="p">[</span><span class="n">q</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">questions</span> <span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">isalpha</span><span class="p">()</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">q</span><span class="p">)][:</span><span class="n">x</span><span class="p">]</span>

    <span class="n">num_questions_generated</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">questions</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">num_questions_generated</span> <span class="o">&lt;</span> <span class="n">x</span><span class="p">:</span>
        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Fewer questions generated (</span><span class="si">{</span><span class="n">num_questions_generated</span><span class="si">}</span><span class="s2">) "</span>
            <span class="sa">f</span><span class="s2">"than requested (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">)."</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">questions</span>
</code></pre></div></td></tr></tbody></table>

### get\_chunks [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.get_chunks "Permanent link")

```
get_chunks(file_path: str, chunk_size: int) -> List[str]
```

Takes in a `file_path`, retrieves the document, breaks it down into chunks of size `chunk_size`, and returns the chunks.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">125</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_chunks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Takes in a `file_path`, retrieves the document, breaks it down into chunks of size</span>
<span class="sd">    `chunk_size`, and returns the chunks.</span>
<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">input_files</span><span class="o">=</span><span class="p">[</span><span class="n">file_path</span><span class="p">])</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
    <span class="n">splitter</span> <span class="o">=</span> <span class="n">SemanticSplitterNodeParser</span><span class="p">(</span>
        <span class="n">buffer_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">breakpoint_percentile_threshold</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">default_breakpoint_percentile_threshold</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="n">splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### add\_chunk\_to\_dataset [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.add_chunk_to_dataset "Permanent link")

```
add_chunk_to_dataset(chunks: List, chunk: str, x: int = 5, num_distract: int = 3, p: float = 1.0)
```

Given a chunk, create {Q, A, D} triplets and add them to the dataset.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
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
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_chunk_to_dataset</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">,</span>
    <span class="n">chunk</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">x</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
    <span class="n">num_distract</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
    <span class="n">p</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Given a chunk, create {Q, A, D} triplets and add them to the dataset.</span>
<span class="sd">    """</span>
    <span class="n">i</span> <span class="o">=</span> <span class="n">chunks</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
    <span class="n">qs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_instructions_gen</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">qs</span><span class="p">:</span>
        <span class="n">datapt</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"id"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"type"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"question"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"context"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"oracle_context"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"cot_answer"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"seed_task_</span><span class="si">{</span><span class="mi">0</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="ow">not</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="o">.</span><span class="n">num_rows</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"general"</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="n">q</span>

        <span class="c1"># add distractor docs</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">chunk</span><span class="p">]</span>
        <span class="n">indices</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)))</span>
        <span class="n">indices</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">random</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">indices</span><span class="p">,</span> <span class="n">num_distract</span><span class="p">):</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chunks</span><span class="p">[</span><span class="n">j</span><span class="p">])</span>
        <span class="c1"># decides whether to add oracle document</span>
        <span class="n">oracle</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">p</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">oracle</span><span class="p">:</span>
            <span class="n">docs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">chunks</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">indices</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]]</span>
        <span class="n">random</span><span class="o">.</span><span class="n">shuffle</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

        <span class="n">d</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"title"</span><span class="p">:</span> <span class="p">[],</span> <span class="s2">"sentences"</span><span class="p">:</span> <span class="p">[]}</span>

        <span class="n">d</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="s2">"placeholder_title"</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">num_distract</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
        <span class="n">d</span><span class="p">[</span><span class="s2">"sentences"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">d</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]</span> <span class="o">=</span> <span class="n">chunk</span>

        <span class="c1"># add answer to q</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_label</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">chunk</span><span class="p">)</span>

        <span class="c1"># construct model instruction</span>
        <span class="n">context</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">context</span> <span class="o">+=</span> <span class="s2">"&lt;DOCUMENT&gt;"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"&lt;/DOCUMENT&gt;</span><span class="se">\n</span><span class="s2">"</span>
        <span class="n">context</span> <span class="o">+=</span> <span class="n">q</span>
        <span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>

        <span class="c1"># add to dataset</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="p">:</span>
            <span class="c1"># init ds</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"question"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"oracle_context"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"cot_answer"</span><span class="p">]]</span>
            <span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datapt</span><span class="p">[</span><span class="s2">"instruction"</span><span class="p">]]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">ds</span> <span class="o">=</span> <span class="n">Dataset</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">datapt</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">ds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="n">datapt</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/#llama_index.packs.raft_dataset.RAFTDatasetPack.run "Permanent link")

```
run() -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-raft-dataset/llama_index/packs/raft_dataset/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">210</span>
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
<span class="normal">226</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="n">chunks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_chunks</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_path</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">chunk_size</span><span class="p">)</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Number of chunks created: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span> <span class="o">=</span> <span class="p">(</span>
        <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">))</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="p">)</span>  <span class="c1"># should be less than number of chunks/ nodes created</span>

    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">chunks</span><span class="p">):</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Processing chunk: </span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_chunk_to_dataset</span><span class="p">(</span>
            <span class="n">chunks</span><span class="p">,</span> <span class="n">chunk</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_questions_per_chunk</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_distract_docs</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">ds</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Query understanding agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/query_understanding_agent/)[Next Rag cli local](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/)
