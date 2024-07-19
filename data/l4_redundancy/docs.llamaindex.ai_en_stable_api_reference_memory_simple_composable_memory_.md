Title: Simple composable memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/

Markdown Content:
Simple composable memory - LlamaIndex


SimpleComposableMemory [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")`

A simple composition of potentially several memory sources.

This composable memory considers one of the memory sources as the main one and the others as secondary. The secondary memory sources get added to the chat history only in either the system prompt or to the first user message within the chat history.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `primary_memory` |  | 
(BaseMemory) The main memory buffer for agent.



 | _required_ |
| `secondary_memory_sources` |  | 

(List(BaseMemory)) Secondary memory sources. Retrieved messages from these sources get added to the system prompt message.



 | _required_ |

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
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
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleComposableMemory</span><span class="p">(</span><span class="n">BaseMemory</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A simple composition of potentially several memory sources.</span>

<span class="sd">    This composable memory considers one of the memory sources as the main</span>
<span class="sd">    one and the others as secondary. The secondary memory sources get added to</span>
<span class="sd">    the chat history only in either the system prompt or to the first user</span>
<span class="sd">    message within the chat history.</span>

<span class="sd">    Args:</span>
<span class="sd">        primary_memory: (BaseMemory) The main memory buffer for agent.</span>
<span class="sd">        secondary_memory_sources: (List(BaseMemory)) Secondary memory sources.</span>
<span class="sd">            Retrieved messages from these sources get added to the system prompt message.</span>
<span class="sd">    """</span>

    <span class="n">primary_memory</span><span class="p">:</span> <span class="n">BaseMemory</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Primary memory source for chat agent."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">secondary_memory_sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Secondary memory sources."</span>
    <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"SimpleComposableMemory"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">primary_memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">secondary_memory_sources</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleComposableMemory"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a simple composable memory from an LLM."""</span>
        <span class="n">primary_memory</span> <span class="o">=</span> <span class="n">primary_memory</span> <span class="ow">or</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
        <span class="n">secondary_memory_sources</span> <span class="o">=</span> <span class="n">secondary_memory_sources</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">primary_memory</span><span class="o">=</span><span class="n">primary_memory</span><span class="p">,</span>
            <span class="n">secondary_memory_sources</span><span class="o">=</span><span class="n">secondary_memory_sources</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_format_secondary_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">secondary_chat_histories</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Formats retrieved historical messages into a single string."""</span>
        <span class="c1"># TODO: use PromptTemplate for this</span>
        <span class="n">formatted_history</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span> <span class="o">+</span> <span class="n">DEFAULT_INTRO_HISTORY_MESSAGE</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">for</span> <span class="n">ix</span><span class="p">,</span> <span class="n">chat_history</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">secondary_chat_histories</span><span class="p">):</span>
            <span class="n">formatted_history</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"></span><span class="se">\n\n</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">chat_history</span><span class="p">:</span>
                <span class="n">formatted_history</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\t</span><span class="si">{</span><span class="n">m</span><span class="o">.</span><span class="n">role</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">m</span><span class="o">.</span><span class="n">content</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">formatted_history</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"></span><span class="se">\n\n</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="n">formatted_history</span> <span class="o">+=</span> <span class="n">DEFAULT_OUTRO_HISTORY_MESSAGE</span>
        <span class="k">return</span> <span class="n">formatted_history</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_compose_message_histories</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_compose_message_histories</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>
        <span class="c1"># get from primary</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="c1"># get from secondary</span>
        <span class="c1"># TODO: remove any repeated messages in secondary and primary memory</span>
        <span class="n">secondary_histories</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
            <span class="n">secondary_history</span> <span class="o">=</span> <span class="n">mem</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="n">secondary_history</span> <span class="o">=</span> <span class="p">[</span><span class="n">m</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">secondary_history</span> <span class="k">if</span> <span class="n">m</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">]</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">secondary_history</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">secondary_histories</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">secondary_history</span><span class="p">)</span>

        <span class="c1"># format secondary memory</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">secondary_histories</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">single_secondary_memory_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_secondary_messages</span><span class="p">(</span>
                <span class="n">secondary_histories</span>
            <span class="p">)</span>

            <span class="c1"># add single_secondary_memory_str to chat_history</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">role</span> <span class="o">==</span> <span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">:</span>
                <span class="n">system_message</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">split</span><span class="p">(</span>
                    <span class="n">DEFAULT_INTRO_HISTORY_MESSAGE</span>
                <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span>
                    <span class="n">content</span><span class="o">=</span><span class="n">system_message</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">+</span> <span class="n">single_secondary_memory_str</span><span class="p">,</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">messages</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span>
                    <span class="mi">0</span><span class="p">,</span>
                    <span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">content</span><span class="o">=</span><span class="s2">"You are a helpful assistant."</span>
                        <span class="o">+</span> <span class="n">single_secondary_memory_str</span><span class="p">,</span>
                        <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span>
                    <span class="p">),</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">messages</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all chat history.</span>

<span class="sd">        Uses primary memory get_all only.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
            <span class="n">mem</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
            <span class="c1"># finalize task often sets, but secondary memory is meant for</span>
            <span class="c1"># long-term memory rather than main chat memory buffer</span>
            <span class="c1"># so use put_messages instead</span>
            <span class="n">mem</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
            <span class="n">mem</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.class_name "Permanent link")

```
class_name() -> str
```

Class name.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"SimpleComposableMemory"</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.from_defaults "Permanent link")

```
from_defaults(primary_memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")] = None, secondary_memory_sources: Optional[List[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")]] = None) -> [SimpleComposableMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory "llama_index.core.memory.simple_composable_memory.SimpleComposableMemory")
```

Create a simple composable memory from an LLM.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">primary_memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">secondary_memory_sources</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleComposableMemory"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a simple composable memory from an LLM."""</span>
    <span class="n">primary_memory</span> <span class="o">=</span> <span class="n">primary_memory</span> <span class="ow">or</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
    <span class="n">secondary_memory_sources</span> <span class="o">=</span> <span class="n">secondary_memory_sources</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">primary_memory</span><span class="o">=</span><span class="n">primary_memory</span><span class="p">,</span>
        <span class="n">secondary_memory_sources</span><span class="o">=</span><span class="n">secondary_memory_sources</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.get "Permanent link")

```
get(input: Optional[str] = None, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get chat history."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_compose_message_histories</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.get_all "Permanent link")

```
get_all() -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get all chat history.

Uses primary memory get\_all only.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all chat history.</span>

<span class="sd">    Uses primary memory get_all only.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.put "Permanent link")

```
put(message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")) -> None
```

Put chat history.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
        <span class="n">mem</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.set "Permanent link")

```
set(messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]) -> None
```

Set chat history.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
        <span class="c1"># finalize task often sets, but secondary memory is meant for</span>
        <span class="c1"># long-term memory rather than main chat memory buffer</span>
        <span class="c1"># so use put_messages instead</span>
        <span class="n">mem</span><span class="o">.</span><span class="n">put_messages</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### reset [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/#llama_index.core.memory.simple_composable_memory.SimpleComposableMemory.reset "Permanent link")

```
reset() -> None
```

Reset chat history.

Source code in `llama-index-core/llama_index/core/memory/simple_composable_memory.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">primary_memory</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">secondary_memory_sources</span><span class="p">:</span>
        <span class="n">mem</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/memory/)[Next Vector memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/)
