Title: Simple - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/

Markdown Content:
Simple - LlamaIndex


SimpleChatEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/#llama_index.core.chat_engine.SimpleChatEngine "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.BaseChatEngine "llama_index.core.chat_engine.types.BaseChatEngine")`

Simple Chat Engine.

Have a conversation with the LLM. This does not make use of a knowledge base.

Source code in `llama-index-core/llama_index/core/chat_engine/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
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
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleChatEngine</span><span class="p">(</span><span class="n">BaseChatEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Simple Chat Engine.</span>

<span class="sd">    Have a conversation with the LLM.</span>
<span class="sd">    This does not make use of a knowledge base.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span> <span class="o">=</span> <span class="n">memory</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleChatEngine"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a SimpleChatEngine from default parameters."""</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
                <span class="p">)</span>
            <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">system_role</span><span class="p">)</span>
            <span class="p">]</span>

        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">),</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="n">ai_message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
            <span class="n">chat_stream</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="n">chat_response</span><span class="o">.</span><span class="n">write_response_to_history</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">,)</span>
        <span class="p">)</span>
        <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="n">ai_message</span> <span class="o">=</span> <span class="n">chat_response</span><span class="o">.</span><span class="n">message</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ai_message</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">))</span>
        <span class="n">initial_token_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span>
                <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">([(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="n">all_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prefix_messages</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">initial_token_count</span><span class="o">=</span><span class="n">initial_token_count</span>
        <span class="p">)</span>

        <span class="n">chat_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
            <span class="n">achat_stream</span><span class="o">=</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">astream_chat</span><span class="p">(</span><span class="n">all_messages</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">chat_response</span><span class="o">.</span><span class="n">awrite_response_to_history</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### chat\_history `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/#llama_index.core.chat_engine.SimpleChatEngine.chat_history "Permanent link")

```
chat_history: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/#llama_index.core.chat_engine.SimpleChatEngine.from_defaults "Permanent link")

```
from_defaults(chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = None, memory_cls: Type[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = ChatMemoryBuffer, system_prompt: Optional[str] = None, prefix_messages: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, service_context: Optional[ServiceContext] = None, **kwargs: Any) -> [SimpleChatEngine](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/#llama_index.core.chat_engine.SimpleChatEngine "llama_index.core.chat_engine.simple.SimpleChatEngine")
```

Initialize a SimpleChatEngine from default parameters.

Source code in `llama-index-core/llama_index/core/chat_engine/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
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
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># deprecated</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleChatEngine"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a SimpleChatEngine from default parameters."""</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>

    <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
            <span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">system_role</span><span class="p">)</span>
        <span class="p">]</span>

    <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/)[Next Adapter](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/)
