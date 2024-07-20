Title: Chat memory buffer - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/

Markdown Content:
Chat memory buffer - LlamaIndex


ChatMemoryBuffer [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatStoreMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory "llama_index.core.memory.types.BaseChatStoreMemory")`

Simple buffer for storing chat history.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
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
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatMemoryBuffer</span><span class="p">(</span><span class="n">BaseChatStoreMemory</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple buffer for storing chat history."""</span>

    <span class="n">token_limit</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">tokenizer_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="c1"># NOTE: mypy does not handle the typing here well, hence the cast</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="n">get_tokenizer</span><span class="p">,</span>
        <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">chat_store</span><span class="p">:</span> <span class="n">BaseChatStore</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">SimpleChatStore</span><span class="p">)</span>
    <span class="n">chat_store_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHAT_STORE_KEY</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"ChatMemoryBuffer"</span>

    <span class="nd">@root_validator</span><span class="p">(</span><span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_memory</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">values</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="c1"># Validate token limit</span>
        <span class="n">token_limit</span> <span class="o">=</span> <span class="n">values</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"token_limit"</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">token_limit</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Token limit must be set and greater than 0."</span><span class="p">)</span>

        <span class="c1"># Validate tokenizer -- this avoids errors when loading from json/dict</span>
        <span class="n">tokenizer_fn</span> <span class="o">=</span> <span class="n">values</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"tokenizer_fn"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">tokenizer_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">values</span><span class="p">[</span><span class="s2">"tokenizer_fn"</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_tokenizer</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">values</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseChatStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_store_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_STORE_KEY</span><span class="p">,</span>
        <span class="n">token_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMemoryBuffer"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a chat memory buffer from an LLM."""</span>
        <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">context_window</span> <span class="o">=</span> <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">context_window</span>
            <span class="n">token_limit</span> <span class="o">=</span> <span class="n">token_limit</span> <span class="ow">or</span> <span class="nb">int</span><span class="p">(</span><span class="n">context_window</span> <span class="o">*</span> <span class="n">DEFAULT_TOKEN_LIMIT_RATIO</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">token_limit</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">token_limit</span> <span class="o">=</span> <span class="n">DEFAULT_TOKEN_LIMIT</span>

        <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">chat_store</span> <span class="o">=</span> <span class="n">chat_store</span> <span class="ow">or</span> <span class="n">SimpleChatStore</span><span class="p">()</span>
            <span class="n">chat_store</span><span class="o">.</span><span class="n">set_messages</span><span class="p">(</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">token_limit</span><span class="o">=</span><span class="n">token_limit</span><span class="p">,</span>
            <span class="n">tokenizer_fn</span><span class="o">=</span><span class="n">tokenizer_fn</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">(),</span>
            <span class="n">chat_store</span><span class="o">=</span><span class="n">chat_store</span> <span class="ow">or</span> <span class="n">SimpleChatStore</span><span class="p">(),</span>
            <span class="n">chat_store_key</span><span class="o">=</span><span class="n">chat_store_key</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert memory to string."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_string</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">json_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMemoryBuffer"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a chat memory buffer from a string."""</span>
        <span class="n">dict_obj</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_str</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">dict_obj</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert memory to dict."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMemoryBuffer"</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.storage.chat_store.loading</span> <span class="kn">import</span> <span class="n">load_chat_store</span>

        <span class="c1"># NOTE: this handles backwards compatibility with the old chat history</span>
        <span class="k">if</span> <span class="s2">"chat_history"</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">chat_history</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"chat_history"</span><span class="p">)</span>
            <span class="n">chat_store</span> <span class="o">=</span> <span class="n">SimpleChatStore</span><span class="p">(</span><span class="n">store</span><span class="o">=</span><span class="p">{</span><span class="n">DEFAULT_CHAT_STORE_KEY</span><span class="p">:</span> <span class="n">chat_history</span><span class="p">})</span>
            <span class="n">data</span><span class="p">[</span><span class="s2">"chat_store"</span><span class="p">]</span> <span class="o">=</span> <span class="n">chat_store</span>
        <span class="k">elif</span> <span class="s2">"chat_store"</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">chat_store</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"chat_store"</span><span class="p">)</span>
            <span class="n">chat_store</span> <span class="o">=</span> <span class="n">load_chat_store</span><span class="p">(</span><span class="n">chat_store</span><span class="p">)</span>
            <span class="n">data</span><span class="p">[</span><span class="s2">"chat_store"</span><span class="p">]</span> <span class="o">=</span> <span class="n">chat_store</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">data</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">initial_token_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">initial_token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Initial token count exceeds token limit"</span><span class="p">)</span>

        <span class="n">message_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>

        <span class="n">cur_messages</span> <span class="o">=</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>
        <span class="n">token_count</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token_count_for_messages</span><span class="p">(</span><span class="n">cur_messages</span><span class="p">)</span> <span class="o">+</span> <span class="n">initial_token_count</span>

        <span class="k">while</span> <span class="n">token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span> <span class="ow">and</span> <span class="n">message_count</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">message_count</span> <span class="o">-=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o"></span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">:</span>
                <span class="c1"># we cannot have an assistant message at the start of the chat history</span>
                <span class="c1"># if after removal of the first, we have an assistant message,</span>
                <span class="c1"># we need to remove the assistant message too</span>
                <span class="n">message_count</span> <span class="o">-=</span> <span class="mi">1</span>

            <span class="n">cur_messages</span> <span class="o">=</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>
            <span class="n">token_count</span> <span class="o">=</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_token_count_for_messages</span><span class="p">(</span><span class="n">cur_messages</span><span class="p">)</span> <span class="o">+</span> <span class="n">initial_token_count</span>
            <span class="p">)</span>

        <span class="c1"># catch one message longer than token limit</span>
        <span class="k">if</span> <span class="n">token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span> <span class="ow">or</span> <span class="n">message_count</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>

    <span class="k">def</span> <span class="nf">_token_count_for_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="mi">0</span>

        <span class="n">msg_str</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">content</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tokenizer_fn</span><span class="p">(</span><span class="n">msg_str</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"ChatMemoryBuffer"</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.from_defaults "Permanent link")

```
from_defaults(chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, chat_store: Optional[[BaseChatStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore "llama_index.core.storage.chat_store.BaseChatStore")] = None, chat_store_key: str = DEFAULT_CHAT_STORE_KEY, token_limit: Optional[int] = None, tokenizer_fn: Optional[Callable[[str], List]] = None) -> [ChatMemoryBuffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer "llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer")
```

Create a chat memory buffer from an LLM.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">49</span>
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
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseChatStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_store_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_CHAT_STORE_KEY</span><span class="p">,</span>
    <span class="n">token_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tokenizer_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMemoryBuffer"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a chat memory buffer from an LLM."""</span>
    <span class="k">if</span> <span class="n">llm</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">context_window</span> <span class="o">=</span> <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">context_window</span>
        <span class="n">token_limit</span> <span class="o">=</span> <span class="n">token_limit</span> <span class="ow">or</span> <span class="nb">int</span><span class="p">(</span><span class="n">context_window</span> <span class="o">*</span> <span class="n">DEFAULT_TOKEN_LIMIT_RATIO</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">token_limit</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">token_limit</span> <span class="o">=</span> <span class="n">DEFAULT_TOKEN_LIMIT</span>

    <span class="k">if</span> <span class="n">chat_history</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">chat_store</span> <span class="o">=</span> <span class="n">chat_store</span> <span class="ow">or</span> <span class="n">SimpleChatStore</span><span class="p">()</span>
        <span class="n">chat_store</span><span class="o">.</span><span class="n">set_messages</span><span class="p">(</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">token_limit</span><span class="o">=</span><span class="n">token_limit</span><span class="p">,</span>
        <span class="n">tokenizer_fn</span><span class="o">=</span><span class="n">tokenizer_fn</span> <span class="ow">or</span> <span class="n">get_tokenizer</span><span class="p">(),</span>
        <span class="n">chat_store</span><span class="o">=</span><span class="n">chat_store</span> <span class="ow">or</span> <span class="n">SimpleChatStore</span><span class="p">(),</span>
        <span class="n">chat_store_key</span><span class="o">=</span><span class="n">chat_store_key</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_string [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.to_string "Permanent link")

```
to_string() -> str
```

Convert memory to string.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert memory to string."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### from\_string `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.from_string "Permanent link")

```
from_string(json_str: str) -> [ChatMemoryBuffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer "llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer")
```

Create a chat memory buffer from a string.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_string</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">json_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChatMemoryBuffer"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a chat memory buffer from a string."""</span>
    <span class="n">dict_obj</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_str</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">dict_obj</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_dict [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.to_dict "Permanent link")

```
to_dict(**kwargs: Any) -> dict
```

Convert memory to dict.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convert memory to dict."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/#llama_index.core.memory.chat_memory_buffer.ChatMemoryBuffer.get "Permanent link")

```
get(input: Optional[str] = None, initial_token_count: int = 0, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

Source code in `llama-index-core/llama_index/core/memory/chat_memory_buffer.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
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
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">initial_token_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get chat history."""</span>
    <span class="n">chat_history</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>

    <span class="k">if</span> <span class="n">initial_token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Initial token count exceeds token limit"</span><span class="p">)</span>

    <span class="n">message_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">chat_history</span><span class="p">)</span>

    <span class="n">cur_messages</span> <span class="o">=</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>
    <span class="n">token_count</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_token_count_for_messages</span><span class="p">(</span><span class="n">cur_messages</span><span class="p">)</span> <span class="o">+</span> <span class="n">initial_token_count</span>

    <span class="k">while</span> <span class="n">token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span> <span class="ow">and</span> <span class="n">message_count</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">message_count</span> <span class="o">-=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o"></span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">:</span>
            <span class="c1"># we cannot have an assistant message at the start of the chat history</span>
            <span class="c1"># if after removal of the first, we have an assistant message,</span>
            <span class="c1"># we need to remove the assistant message too</span>
            <span class="n">message_count</span> <span class="o">-=</span> <span class="mi">1</span>

        <span class="n">cur_messages</span> <span class="o">=</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>
        <span class="n">token_count</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_token_count_for_messages</span><span class="p">(</span><span class="n">cur_messages</span><span class="p">)</span> <span class="o">+</span> <span class="n">initial_token_count</span>
        <span class="p">)</span>

    <span class="c1"># catch one message longer than token limit</span>
    <span class="k">if</span> <span class="n">token_count</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">token_limit</span> <span class="ow">or</span> <span class="n">message_count</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="n">message_count</span><span class="p">:]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Zephyr query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/memory/)
