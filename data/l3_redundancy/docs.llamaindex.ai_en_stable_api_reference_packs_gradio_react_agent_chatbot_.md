Title: Gradio react agent chatbot - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/

Markdown Content:
Gradio react agent chatbot - LlamaIndex


GradioReActAgentPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/#llama_index.packs.gradio_react_agent_chatbot.GradioReActAgentPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Gradio chatbot to chat with a ReActAgent pack.

Source code in `llama-index-packs/llama-index-packs-gradio-react-agent-chatbot/llama_index/packs/gradio_react_agent_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 35</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GradioReActAgentPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Gradio chatbot to chat with a ReActAgent pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools_list</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">SUPPORTED_TOOLS</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">ansi2html</span> <span class="kn">import</span> <span class="n">Ansi2HTMLConverter</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install ansi2html via `pip install ansi2html`"</span><span class="p">)</span>

        <span class="n">tools</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tools_list</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">tools</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">SUPPORTED_TOOLS</span><span class="p">[</span><span class="n">t</span><span class="p">]())</span>
            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">KeyError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Tool </span><span class="si">{</span><span class="n">t</span><span class="si">}</span><span class="s2"> is not supported."</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4-1106-preview"</span><span class="p">,</span> <span class="n">max_tokens</span><span class="o">=</span><span class="mi">2000</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">ReActAgent</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">functools</span><span class="o">.</span><span class="n">reduce</span><span class="p">(</span>
                <span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">to_tool_list</span><span class="p">()</span> <span class="o">+</span> <span class="n">y</span><span class="o">.</span><span class="n">to_tool_list</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span>
            <span class="p">),</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">thoughts</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">conv</span> <span class="o">=</span> <span class="n">Ansi2HTMLConverter</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span> <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"tools"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">_handle_user_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user_message</span><span class="p">,</span> <span class="n">history</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Handle the user submitted message. Clear message box, and append</span>
<span class="sd">        to the history.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="s2">""</span><span class="p">,</span> <span class="p">[</span><span class="o">*</span><span class="n">history</span><span class="p">,</span> <span class="p">(</span><span class="n">user_message</span><span class="p">,</span> <span class="s2">""</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">_generate_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Generate the response from agent, and capture the stdout of the</span>
<span class="sd">        ReActAgent's thoughts.</span>
<span class="sd">        """</span>
        <span class="k">with</span> <span class="n">Capturing</span><span class="p">()</span> <span class="k">as</span> <span class="n">output</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>
        <span class="n">ansi</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2"></span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
        <span class="n">html_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">conv</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="n">ansi</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">token</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">response_gen</span><span class="p">:</span>
            <span class="n">chat_history</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span> <span class="o">+=</span> <span class="n">token</span>
            <span class="k">yield</span> <span class="n">chat_history</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">html_output</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_reset_chat</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Reset the agent's chat history. And clear all dialogue boxes."""</span>
        <span class="c1"># clear agent history</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
        <span class="k">return</span> <span class="s2">""</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="s2">""</span>  <span class="c1"># clear textboxes</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="kn">import</span> <span class="nn">gradio</span> <span class="k">as</span> <span class="nn">gr</span>

        <span class="n">demo</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Blocks</span><span class="p">(</span>
            <span class="n">theme</span><span class="o">=</span><span class="s2">"gstaff/xkcd"</span><span class="p">,</span>
            <span class="n">css</span><span class="o">=</span><span class="s2">"#box { height: 420px; overflow-y: scroll !important}"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="n">demo</span><span class="p">:</span>
            <span class="n">gr</span><span class="o">.</span><span class="n">Markdown</span><span class="p">(</span>
                <span class="s2">"# Gradio ReActAgent Powered by LlamaIndex and LlamaHub 🦙</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"This Gradio app is powered by LlamaIndex's `ReActAgent` with</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"OpenAI's GPT-4-Turbo as the LLM. The tools are listed below.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"## Tools</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"- [ArxivToolSpec](https://llamahub.ai/l/tools-arxiv)</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"- [WikipediaToolSpec](https://llamahub.ai/l/tools-wikipedia)"</span>
            <span class="p">)</span>
            <span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Row</span><span class="p">():</span>
                <span class="n">chat_window</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Chatbot</span><span class="p">(</span>
                    <span class="n">label</span><span class="o">=</span><span class="s2">"Message History"</span><span class="p">,</span>
                    <span class="n">scale</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">console</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">HTML</span><span class="p">(</span><span class="n">elem_id</span><span class="o">=</span><span class="s2">"box"</span><span class="p">)</span>
            <span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Row</span><span class="p">():</span>
                <span class="n">message</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Textbox</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="s2">"Write A Message"</span><span class="p">,</span> <span class="n">scale</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
                <span class="n">clear</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">ClearButton</span><span class="p">()</span>

            <span class="n">message</span><span class="o">.</span><span class="n">submit</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_handle_user_message</span><span class="p">,</span>
                <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">],</span>
                <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">],</span>
                <span class="n">queue</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span><span class="o">.</span><span class="n">then</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_generate_response</span><span class="p">,</span>
                <span class="n">chat_window</span><span class="p">,</span>
                <span class="p">[</span><span class="n">chat_window</span><span class="p">,</span> <span class="n">console</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">clear</span><span class="o">.</span><span class="n">click</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_reset_chat</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">,</span> <span class="n">console</span><span class="p">])</span>

        <span class="n">demo</span><span class="o">.</span><span class="n">launch</span><span class="p">(</span><span class="n">server_name</span><span class="o">=</span><span class="s2">"0.0.0.0"</span><span class="p">,</span> <span class="n">server_port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/#llama_index.packs.gradio_react_agent_chatbot.GradioReActAgentPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-gradio-react-agent-chatbot/llama_index/packs/gradio_react_agent_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span><span class="s2">"agent"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="p">,</span> <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="s2">"tools"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tools</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/#llama_index.packs.gradio_react_agent_chatbot.GradioReActAgentPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-gradio-react-agent-chatbot/llama_index/packs/gradio_react_agent_chatbot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="kn">import</span> <span class="nn">gradio</span> <span class="k">as</span> <span class="nn">gr</span>

    <span class="n">demo</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Blocks</span><span class="p">(</span>
        <span class="n">theme</span><span class="o">=</span><span class="s2">"gstaff/xkcd"</span><span class="p">,</span>
        <span class="n">css</span><span class="o">=</span><span class="s2">"#box { height: 420px; overflow-y: scroll !important}"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="n">demo</span><span class="p">:</span>
        <span class="n">gr</span><span class="o">.</span><span class="n">Markdown</span><span class="p">(</span>
            <span class="s2">"# Gradio ReActAgent Powered by LlamaIndex and LlamaHub 🦙</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"This Gradio app is powered by LlamaIndex's `ReActAgent` with</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"OpenAI's GPT-4-Turbo as the LLM. The tools are listed below.</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"## Tools</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"- [ArxivToolSpec](https://llamahub.ai/l/tools-arxiv)</span><span class="se">\n</span><span class="s2">"</span>
            <span class="s2">"- [WikipediaToolSpec](https://llamahub.ai/l/tools-wikipedia)"</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Row</span><span class="p">():</span>
            <span class="n">chat_window</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Chatbot</span><span class="p">(</span>
                <span class="n">label</span><span class="o">=</span><span class="s2">"Message History"</span><span class="p">,</span>
                <span class="n">scale</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">console</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">HTML</span><span class="p">(</span><span class="n">elem_id</span><span class="o">=</span><span class="s2">"box"</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Row</span><span class="p">():</span>
            <span class="n">message</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Textbox</span><span class="p">(</span><span class="n">label</span><span class="o">=</span><span class="s2">"Write A Message"</span><span class="p">,</span> <span class="n">scale</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
            <span class="n">clear</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">ClearButton</span><span class="p">()</span>

        <span class="n">message</span><span class="o">.</span><span class="n">submit</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_handle_user_message</span><span class="p">,</span>
            <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">],</span>
            <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">],</span>
            <span class="n">queue</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span><span class="o">.</span><span class="n">then</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_generate_response</span><span class="p">,</span>
            <span class="n">chat_window</span><span class="p">,</span>
            <span class="p">[</span><span class="n">chat_window</span><span class="p">,</span> <span class="n">console</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">clear</span><span class="o">.</span><span class="n">click</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_reset_chat</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="p">[</span><span class="n">message</span><span class="p">,</span> <span class="n">chat_window</span><span class="p">,</span> <span class="n">console</span><span class="p">])</span>

    <span class="n">demo</span><span class="o">.</span><span class="n">launch</span><span class="p">(</span><span class="n">server_name</span><span class="o">=</span><span class="s2">"0.0.0.0"</span><span class="p">,</span> <span class="n">server_port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Gradio agent chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_agent_chat/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/packs/)
