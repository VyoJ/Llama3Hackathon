Title: Streamlit chatbot - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/

Markdown Content:
Streamlit chatbot - LlamaIndex


StreamlitChatPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/#llama_index.packs.streamlit_chatbot.StreamlitChatPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Streamlit chatbot pack.

Source code in `llama-index-packs/llama-index-packs-streamlit-chatbot/llama_index/packs/streamlit_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 19</span>
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
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StreamlitChatPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Streamlit chatbot pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">wikipedia_page</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Snowflake Inc."</span><span class="p">,</span>
        <span class="n">run_from_main</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">run_from_main</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Please run this llama-pack directly with "</span>
                <span class="s2">"`streamlit run [download_dir]/streamlit_chatbot/base.py`"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span> <span class="o">=</span> <span class="n">wikipedia_page</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="kn">import</span> <span class="nn">streamlit</span> <span class="k">as</span> <span class="nn">st</span>
        <span class="kn">from</span> <span class="nn">streamlit_pills</span> <span class="kn">import</span> <span class="n">pills</span>

        <span class="n">st</span><span class="o">.</span><span class="n">set_page_config</span><span class="p">(</span>
            <span class="n">page_title</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Chat with </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="si">}</span><span class="s2">'s Wikipedia page, powered by LlamaIndex"</span><span class="p">,</span>
            <span class="n">page_icon</span><span class="o">=</span><span class="s2">"🦙"</span><span class="p">,</span>
            <span class="n">layout</span><span class="o">=</span><span class="s2">"centered"</span><span class="p">,</span>
            <span class="n">initial_sidebar_state</span><span class="o">=</span><span class="s2">"auto"</span><span class="p">,</span>
            <span class="n">menu_items</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="s2">"messages"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">:</span>  <span class="c1"># Initialize the chat messages history</span>
            <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                <span class="p">{</span><span class="s2">"role"</span><span class="p">:</span> <span class="s2">"assistant"</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="s2">"Ask me a question about Snowflake!"</span><span class="p">}</span>
            <span class="p">]</span>

        <span class="n">st</span><span class="o">.</span><span class="n">title</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Chat with </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="si">}</span><span class="s2">'s Wikipedia page, powered by LlamaIndex 💬🦙"</span>
        <span class="p">)</span>
        <span class="n">st</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
            <span class="s2">"This example is powered by the **[Llama Hub Wikipedia Loader](https://llamahub.ai/l/wikipedia)**. Use any of [Llama Hub's many loaders](https://llamahub.ai/) to retrieve and chat with your data via a Streamlit app."</span><span class="p">,</span>
            <span class="n">icon</span><span class="o">=</span><span class="s2">"ℹ️"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">def</span> <span class="nf">add_to_message_history</span><span class="p">(</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
            <span class="n">message</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"role"</span><span class="p">:</span> <span class="n">role</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">content</span><span class="p">)}</span>
            <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">message</span>
            <span class="p">)</span>  <span class="c1"># Add response to message history</span>

        <span class="nd">@st</span><span class="o">.</span><span class="n">cache_resource</span>
        <span class="k">def</span> <span class="nf">load_index_data</span><span class="p">():</span>
            <span class="n">loader</span> <span class="o">=</span> <span class="n">WikipediaReader</span><span class="p">()</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">pages</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="p">])</span>
            <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">llm</span><span class="o">=</span><span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">,</span> <span class="n">temperature</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
                <span class="n">docs</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
            <span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="n">load_index_data</span><span class="p">()</span>

        <span class="n">selected</span> <span class="o">=</span> <span class="n">pills</span><span class="p">(</span>
            <span class="s2">"Choose a question to get started or write your own below."</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="s2">"What is Snowflake?"</span><span class="p">,</span>
                <span class="s2">"What company did Snowflake announce they would acquire in October 2023?"</span><span class="p">,</span>
                <span class="s2">"What company did Snowflake acquire in March 2022?"</span><span class="p">,</span>
                <span class="s2">"When did Snowflake IPO?"</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">clearable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">index</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="s2">"chat_engine"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">:</span>  <span class="c1"># Initialize the query engine</span>
            <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_chat_engine</span><span class="p">(</span>
                <span class="n">chat_mode</span><span class="o">=</span><span class="s2">"context"</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]:</span>  <span class="c1"># Display the prior chat messages</span>
            <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"role"</span><span class="p">]):</span>
                <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"content"</span><span class="p">])</span>

        <span class="c1"># To avoid duplicated display of answered pill questions each rerun</span>
        <span class="k">if</span> <span class="n">selected</span> <span class="ow">and</span> <span class="n">selected</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s2">"displayed_pill_questions"</span><span class="p">,</span> <span class="nb">set</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="s2">"displayed_pill_questions"</span><span class="p">,</span> <span class="nb">set</span><span class="p">())</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
            <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"user"</span><span class="p">):</span>
                <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
            <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
                <span class="n">response_str</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">response_container</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
                <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
                    <span class="n">response_str</span> <span class="o">+=</span> <span class="n">token</span>
                    <span class="n">response_container</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response_str</span><span class="p">)</span>
                <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">selected</span><span class="p">)</span>
                <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">prompt</span> <span class="o">:=</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_input</span><span class="p">(</span>
            <span class="s2">"Your question"</span>
        <span class="p">):</span>  <span class="c1"># Prompt for user input and save to chat history</span>
            <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>

            <span class="c1"># Display the new question immediately after it is entered</span>
            <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"user"</span><span class="p">):</span>
                <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

            <span class="c1"># If last message is not from assistant, generate a new response</span>
            <span class="c1"># if st.session_state["messages"][-1]["role"] != "assistant":</span>
            <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">):</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
                <span class="n">response_str</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">response_container</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
                <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
                    <span class="n">response_str</span> <span class="o">+=</span> <span class="n">token</span>
                    <span class="n">response_container</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response_str</span><span class="p">)</span>
                <span class="c1"># st.write(response.response)</span>
                <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span><span class="p">)</span>

            <span class="c1"># Save the state of the generator</span>
            <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"response_gen"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/#llama_index.packs.streamlit_chatbot.StreamlitChatPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-streamlit-chatbot/llama_index/packs/streamlit_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/#llama_index.packs.streamlit_chatbot.StreamlitChatPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-streamlit-chatbot/llama_index/packs/streamlit_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
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
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="kn">import</span> <span class="nn">streamlit</span> <span class="k">as</span> <span class="nn">st</span>
    <span class="kn">from</span> <span class="nn">streamlit_pills</span> <span class="kn">import</span> <span class="n">pills</span>

    <span class="n">st</span><span class="o">.</span><span class="n">set_page_config</span><span class="p">(</span>
        <span class="n">page_title</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Chat with </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="si">}</span><span class="s2">'s Wikipedia page, powered by LlamaIndex"</span><span class="p">,</span>
        <span class="n">page_icon</span><span class="o">=</span><span class="s2">"🦙"</span><span class="p">,</span>
        <span class="n">layout</span><span class="o">=</span><span class="s2">"centered"</span><span class="p">,</span>
        <span class="n">initial_sidebar_state</span><span class="o">=</span><span class="s2">"auto"</span><span class="p">,</span>
        <span class="n">menu_items</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="s2">"messages"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">:</span>  <span class="c1"># Initialize the chat messages history</span>
        <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">{</span><span class="s2">"role"</span><span class="p">:</span> <span class="s2">"assistant"</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="s2">"Ask me a question about Snowflake!"</span><span class="p">}</span>
        <span class="p">]</span>

    <span class="n">st</span><span class="o">.</span><span class="n">title</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"Chat with </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="si">}</span><span class="s2">'s Wikipedia page, powered by LlamaIndex 💬🦙"</span>
    <span class="p">)</span>
    <span class="n">st</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
        <span class="s2">"This example is powered by the **[Llama Hub Wikipedia Loader](https://llamahub.ai/l/wikipedia)**. Use any of [Llama Hub's many loaders](https://llamahub.ai/) to retrieve and chat with your data via a Streamlit app."</span><span class="p">,</span>
        <span class="n">icon</span><span class="o">=</span><span class="s2">"ℹ️"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_to_message_history</span><span class="p">(</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="n">message</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"role"</span><span class="p">:</span> <span class="n">role</span><span class="p">,</span> <span class="s2">"content"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">content</span><span class="p">)}</span>
        <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">message</span>
        <span class="p">)</span>  <span class="c1"># Add response to message history</span>

    <span class="nd">@st</span><span class="o">.</span><span class="n">cache_resource</span>
    <span class="k">def</span> <span class="nf">load_index_data</span><span class="p">():</span>
        <span class="n">loader</span> <span class="o">=</span> <span class="n">WikipediaReader</span><span class="p">()</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">pages</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">wikipedia_page</span><span class="p">])</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">,</span> <span class="n">temperature</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">docs</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="n">index</span> <span class="o">=</span> <span class="n">load_index_data</span><span class="p">()</span>

    <span class="n">selected</span> <span class="o">=</span> <span class="n">pills</span><span class="p">(</span>
        <span class="s2">"Choose a question to get started or write your own below."</span><span class="p">,</span>
        <span class="p">[</span>
            <span class="s2">"What is Snowflake?"</span><span class="p">,</span>
            <span class="s2">"What company did Snowflake announce they would acquire in October 2023?"</span><span class="p">,</span>
            <span class="s2">"What company did Snowflake acquire in March 2022?"</span><span class="p">,</span>
            <span class="s2">"When did Snowflake IPO?"</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">clearable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">index</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="s2">"chat_engine"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">:</span>  <span class="c1"># Initialize the query engine</span>
        <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_chat_engine</span><span class="p">(</span>
            <span class="n">chat_mode</span><span class="o">=</span><span class="s2">"context"</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

    <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">]:</span>  <span class="c1"># Display the prior chat messages</span>
        <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"role"</span><span class="p">]):</span>
            <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"content"</span><span class="p">])</span>

    <span class="c1"># To avoid duplicated display of answered pill questions each rerun</span>
    <span class="k">if</span> <span class="n">selected</span> <span class="ow">and</span> <span class="n">selected</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
        <span class="s2">"displayed_pill_questions"</span><span class="p">,</span> <span class="nb">set</span><span class="p">()</span>
    <span class="p">):</span>
        <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="s2">"displayed_pill_questions"</span><span class="p">,</span> <span class="nb">set</span><span class="p">())</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"user"</span><span class="p">):</span>
            <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">selected</span><span class="p">)</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">response_container</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
                <span class="n">response_str</span> <span class="o">+=</span> <span class="n">token</span>
                <span class="n">response_container</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response_str</span><span class="p">)</span>
            <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">selected</span><span class="p">)</span>
            <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">prompt</span> <span class="o">:=</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_input</span><span class="p">(</span>
        <span class="s2">"Your question"</span>
    <span class="p">):</span>  <span class="c1"># Prompt for user input and save to chat history</span>
        <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>

        <span class="c1"># Display the new question immediately after it is entered</span>
        <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"user"</span><span class="p">):</span>
            <span class="n">st</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>

        <span class="c1"># If last message is not from assistant, generate a new response</span>
        <span class="c1"># if st.session_state["messages"][-1]["role"] != "assistant":</span>
        <span class="k">with</span> <span class="n">st</span><span class="o">.</span><span class="n">chat_message</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"chat_engine"</span><span class="p">]</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">response_container</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
                <span class="n">response_str</span> <span class="o">+=</span> <span class="n">token</span>
                <span class="n">response_container</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response_str</span><span class="p">)</span>
            <span class="c1"># st.write(response.response)</span>
            <span class="n">add_to_message_history</span><span class="p">(</span><span class="s2">"assistant"</span><span class="p">,</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span><span class="p">)</span>

        <span class="c1"># Save the state of the generator</span>
        <span class="n">st</span><span class="o">.</span><span class="n">session_state</span><span class="p">[</span><span class="s2">"response_gen"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Stock market data query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/)[Next Sub question weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/sub_question_weaviate/)
