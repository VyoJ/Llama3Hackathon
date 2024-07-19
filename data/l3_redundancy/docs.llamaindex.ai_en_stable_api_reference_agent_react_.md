Title: React - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/react/

Markdown Content:
React - LlamaIndex


ReActAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgent "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AgentRunner](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.AgentRunner "llama_index.core.agent.runner.base.AgentRunner")`

ReAct agent.

Subclasses AgentRunner with a ReActAgentWorker.

For the legacy implementation see:

```
from llama_index.core.agent.legacy.react.base import ReActAgent
```

Source code in `llama-index-core/llama_index/core/agent/react/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
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
<span class="normal">151</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ReActAgent</span><span class="p">(</span><span class="n">AgentRunner</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ReAct agent.</span>

<span class="sd">    Subclasses AgentRunner with a ReActAgentWorker.</span>

<span class="sd">    For the legacy implementation see:</span>
<span class="sd">    ```python</span>
<span class="sd">    from llama_index.core.agent.legacy.react.base import ReActAgent</span>
<span class="sd">    ```</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="k">if</span> <span class="n">context</span> <span class="ow">and</span> <span class="n">react_chat_formatter</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot provide both context and react_chat_formatter"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
            <span class="n">react_chat_formatter</span> <span class="o">=</span> <span class="n">ReActChatFormatter</span><span class="o">.</span><span class="n">from_context</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>

        <span class="n">step_engine</span> <span class="o">=</span> <span class="n">ReActAgentWorker</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">max_iterations</span><span class="o">=</span><span class="n">max_iterations</span><span class="p">,</span>
            <span class="n">react_chat_formatter</span><span class="o">=</span><span class="n">react_chat_formatter</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">handle_reasoning_failure_fn</span><span class="o">=</span><span class="n">handle_reasoning_failure_fn</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">step_engine</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActAgent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convenience constructor method from set of BaseTools (Optional).</span>

<span class="sd">        NOTE: kwargs should have been exhausted by this point. In other words</span>
<span class="sd">        the various upstream components such as BaseSynthesizer (response synthesizer)</span>
<span class="sd">        or BaseRetriever should have picked up off their respective kwargs in their</span>
<span class="sd">        constructions.</span>

<span class="sd">        If `handle_reasoning_failure_fn` is provided, when LLM fails to follow the response templates specified in</span>
<span class="sd">        the System Prompt, this function will be called. This function should provide to the Agent, so that the Agent</span>
<span class="sd">        can have a second chance to fix its mistakes.</span>
<span class="sd">        To handle the exception yourself, you can provide a function that raises the `Exception`.</span>

<span class="sd">        Note: If you modified any response template in the System Prompt, you should override the method</span>
<span class="sd">        `_extract_reasoning_step` in `ReActAgentWorker`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            ReActAgent</span>
<span class="sd">        """</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[],</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">max_iterations</span><span class="o">=</span><span class="n">max_iterations</span><span class="p">,</span>
            <span class="n">react_chat_formatter</span><span class="o">=</span><span class="n">react_chat_formatter</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">,</span>
            <span class="n">handle_reasoning_failure_fn</span><span class="o">=</span><span class="n">handle_reasoning_failure_fn</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt modules."""</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"agent_worker"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent_worker</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgent.from_tools "Permanent link")

```
from_tools(tools: Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, tool_retriever: Optional[[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")] = None, memory_cls: Type[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")] = ChatMemoryBuffer, max_iterations: int = 10, react_chat_formatter: Optional[[ReActChatFormatter](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter "llama_index.core.agent.react.formatter.ReActChatFormatter")] = None, output_parser: Optional[ReActOutputParser] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, verbose: bool = False, context: Optional[str] = None, handle_reasoning_failure_fn: Optional[Callable[[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager"), Exception], [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.ToolOutput")]] = None, **kwargs: Any) -> [ReActAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgent "llama_index.core.agent.react.base.ReActAgent")
```

Convenience constructor method from set of BaseTools (Optional).

NOTE: kwargs should have been exhausted by this point. In other words the various upstream components such as BaseSynthesizer (response synthesizer) or BaseRetriever should have picked up off their respective kwargs in their constructions.

If `handle_reasoning_failure_fn` is provided, when LLM fails to follow the response templates specified in the System Prompt, this function will be called. This function should provide to the Agent, so that the Agent can have a second chance to fix its mistakes. To handle the exception yourself, you can provide a function that raises the `Exception`.

Note: If you modified any response template in the System Prompt, you should override the method `_extract_reasoning_step` in `ReActAgentWorker`.

**Returns:**

| Type | Description |
| --- | --- |
| `[ReActAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgent "llama_index.core.agent.react.base.ReActAgent")` | 
ReActAgent



 |

Source code in `llama-index-core/llama_index/core/agent/react/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
    <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
        <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActAgent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convenience constructor method from set of BaseTools (Optional).</span>

<span class="sd">    NOTE: kwargs should have been exhausted by this point. In other words</span>
<span class="sd">    the various upstream components such as BaseSynthesizer (response synthesizer)</span>
<span class="sd">    or BaseRetriever should have picked up off their respective kwargs in their</span>
<span class="sd">    constructions.</span>

<span class="sd">    If `handle_reasoning_failure_fn` is provided, when LLM fails to follow the response templates specified in</span>
<span class="sd">    the System Prompt, this function will be called. This function should provide to the Agent, so that the Agent</span>
<span class="sd">    can have a second chance to fix its mistakes.</span>
<span class="sd">    To handle the exception yourself, you can provide a function that raises the `Exception`.</span>

<span class="sd">    Note: If you modified any response template in the System Prompt, you should override the method</span>
<span class="sd">    `_extract_reasoning_step` in `ReActAgentWorker`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        ReActAgent</span>
<span class="sd">    """</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[],</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
        <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="o">=</span><span class="n">max_iterations</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="o">=</span><span class="n">react_chat_formatter</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="o">=</span><span class="n">handle_reasoning_failure_fn</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

ReActAgentWorker [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.BaseAgentWorker "llama_index.core.agent.types.BaseAgentWorker")`

OpenAI Agent worker.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">108</span>
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
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ReActAgentWorker</span><span class="p">(</span><span class="n">BaseAgentWorker</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAI Agent worker."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_iterations</span> <span class="o">=</span> <span class="n">max_iterations</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span> <span class="o">=</span> <span class="n">react_chat_formatter</span> <span class="ow">or</span> <span class="n">ReActChatFormatter</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span> <span class="o">=</span> <span class="n">output_parser</span> <span class="ow">or</span> <span class="n">ReActOutputParser</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_handle_reasoning_failure_fn</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">handle_reasoning_failure_fn</span>
            <span class="ow">or</span> <span class="n">tell_llm_about_failure_in_extract_reasoning_step</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">tool_retriever</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot specify both tools and tool_retriever"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">tools</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="n">tools</span>
        <span class="k">elif</span> <span class="n">tool_retriever</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">tool_retriever_c</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span> <span class="n">tool_retriever</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">message</span><span class="p">:</span> <span class="n">tool_retriever_c</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="p">[]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActAgentWorker"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convenience constructor method from set of BaseTools (Optional).</span>

<span class="sd">        NOTE: kwargs should have been exhausted by this point. In other words</span>
<span class="sd">        the various upstream components such as BaseSynthesizer (response synthesizer)</span>
<span class="sd">        or BaseRetriever should have picked up off their respective kwargs in their</span>
<span class="sd">        constructions.</span>

<span class="sd">        Returns:</span>
<span class="sd">            ReActAgentWorker</span>
<span class="sd">        """</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">max_iterations</span><span class="o">=</span><span class="n">max_iterations</span><span class="p">,</span>
            <span class="n">react_chat_formatter</span><span class="o">=</span><span class="n">react_chat_formatter</span><span class="p">,</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">handle_reasoning_failure_fn</span><span class="o">=</span><span class="n">handle_reasoning_failure_fn</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="c1"># TODO: the ReAct formatter does not explicitly specify PromptTemplate</span>
        <span class="c1"># objects, but wrap it in this to obey the interface</span>
        <span class="n">sys_header</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">system_header</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"system_prompt"</span><span class="p">:</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">sys_header</span><span class="p">)}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"system_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="n">sys_prompt</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">PromptTemplate</span><span class="p">,</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"system_prompt"</span><span class="p">])</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">system_header</span> <span class="o">=</span> <span class="n">sys_prompt</span><span class="o">.</span><span class="n">template</span>

    <span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize step from task."""</span>
        <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># temporary memory for new messages</span>
        <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

        <span class="c1"># initialize task state</span>
        <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
            <span class="s2">"current_reasoning"</span><span class="p">:</span> <span class="n">current_reasoning</span><span class="p">,</span>
            <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
            <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
            <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
            <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
            <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"is_first"</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span><span class="p">(</span><span class="nb">input</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">_extract_reasoning_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">output</span><span class="p">:</span> <span class="n">ChatResponse</span><span class="p">,</span> <span class="n">is_streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Extracts the reasoning step from the given output.</span>

<span class="sd">        This method parses the message content from the output,</span>
<span class="sd">        extracts the reasoning step, and determines whether the processing is</span>
<span class="sd">        complete. It also performs validation checks on the output and</span>
<span class="sd">        handles possible errors.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">output</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Got empty message."</span><span class="p">)</span>
        <span class="n">message_content</span> <span class="o">=</span> <span class="n">output</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
        <span class="n">current_reasoning</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">message_content</span><span class="p">,</span> <span class="n">is_streaming</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">BaseException</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Could not parse output: </span><span class="si">{</span><span class="n">message_content</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">exc</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>
        <span class="n">current_reasoning</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">is_done</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">message_content</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="kc">True</span>

        <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ActionReasoningStep</span><span class="p">,</span> <span class="n">reasoning_step</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">,</span> <span class="n">ActionReasoningStep</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Expected ActionReasoningStep, got </span><span class="si">{</span><span class="n">reasoning_step</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">message_content</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">_process_actions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">],</span>
        <span class="n">output</span><span class="p">:</span> <span class="n">ChatResponse</span><span class="p">,</span>
        <span class="n">is_streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
        <span class="n">tools_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">AsyncBaseTool</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get_name</span><span class="p">():</span> <span class="n">tool</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span>
        <span class="p">}</span>
        <span class="n">tool</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_reasoning_step</span><span class="p">(</span>
                <span class="n">output</span><span class="p">,</span> <span class="n">is_streaming</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">current_reasoning</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_reasoning_failure_fn</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="kc">True</span>

            <span class="c1"># call tool with input</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ActionReasoningStep</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
            <span class="k">if</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span> <span class="ow">in</span> <span class="n">tools_dict</span><span class="p">:</span>
                <span class="n">tool</span> <span class="o">=</span> <span class="n">tools_dict</span><span class="p">[</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="p">]</span>
                <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">CBEventType</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">,</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">,</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">TOOL</span><span class="p">:</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                            <span class="n">AgentToolCallEvent</span><span class="p">(</span>
                                <span class="n">arguments</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="o">**</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">}),</span>
                                <span class="n">tool</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                            <span class="p">)</span>
                        <span class="p">)</span>
                        <span class="n">tool_output</span> <span class="o">=</span> <span class="n">tool</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="o">**</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">)</span>
                    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                        <span class="n">tool_output</span> <span class="o">=</span> <span class="n">ToolOutput</span><span class="p">(</span>
                            <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">,</span>
                            <span class="n">tool_name</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">},</span>
                            <span class="n">raw_output</span><span class="o">=</span><span class="n">e</span><span class="p">,</span>
                            <span class="n">is_error</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                        <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_OUTPUT</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)}</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_nonexistent_tool_name</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">)</span>

        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)</span>

        <span class="n">observation_step</span> <span class="o">=</span> <span class="n">ObservationReasoningStep</span><span class="p">(</span>
            <span class="n">observation</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
            <span class="n">return_direct</span><span class="o">=</span><span class="p">(</span>
                <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">return_direct</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tool_output</span><span class="o">.</span><span class="n">is_error</span>
                <span class="k">if</span> <span class="n">tool</span>
                <span class="k">else</span> <span class="kc">False</span>
            <span class="p">),</span>
        <span class="p">)</span>
        <span class="n">current_reasoning</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">observation_step</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">observation_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="n">current_reasoning</span><span class="p">,</span>
            <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">return_direct</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tool_output</span><span class="o">.</span><span class="n">is_error</span> <span class="k">if</span> <span class="n">tool</span> <span class="k">else</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aprocess_actions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">],</span>
        <span class="n">output</span><span class="p">:</span> <span class="n">ChatResponse</span><span class="p">,</span>
        <span class="n">is_streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span>
        <span class="n">tools_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">tool</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">}</span>
        <span class="n">tool</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_reasoning_step</span><span class="p">(</span>
                <span class="n">output</span><span class="p">,</span> <span class="n">is_streaming</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">exp</span><span class="p">:</span>
            <span class="n">current_reasoning</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_reasoning_failure_fn</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="p">,</span> <span class="n">exp</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">current_reasoning</span><span class="p">,</span> <span class="kc">True</span>

            <span class="c1"># call tool with input</span>
            <span class="n">reasoning_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ActionReasoningStep</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
            <span class="k">if</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span> <span class="ow">in</span> <span class="n">tools_dict</span><span class="p">:</span>
                <span class="n">tool</span> <span class="o">=</span> <span class="n">tools_dict</span><span class="p">[</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="p">]</span>
                <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                    <span class="n">CBEventType</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">,</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">,</span>
                        <span class="n">EventPayload</span><span class="o">.</span><span class="n">TOOL</span><span class="p">:</span> <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">dispatcher</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
                            <span class="n">AgentToolCallEvent</span><span class="p">(</span>
                                <span class="n">arguments</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span><span class="o">**</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">}),</span>
                                <span class="n">tool</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                            <span class="p">)</span>
                        <span class="p">)</span>
                        <span class="n">tool_output</span> <span class="o">=</span> <span class="k">await</span> <span class="n">tool</span><span class="o">.</span><span class="n">acall</span><span class="p">(</span><span class="o">**</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">)</span>
                    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                        <span class="n">tool_output</span> <span class="o">=</span> <span class="n">ToolOutput</span><span class="p">(</span>
                            <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">,</span>
                            <span class="n">tool_name</span><span class="o">=</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                            <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">},</span>
                            <span class="n">raw_output</span><span class="o">=</span><span class="n">e</span><span class="p">,</span>
                            <span class="n">is_error</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                        <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_OUTPUT</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)}</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">tool_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_handle_nonexistent_tool_name</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">)</span>

        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)</span>

        <span class="n">observation_step</span> <span class="o">=</span> <span class="n">ObservationReasoningStep</span><span class="p">(</span>
            <span class="n">observation</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">),</span>
            <span class="n">return_direct</span><span class="o">=</span><span class="p">(</span>
                <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">return_direct</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tool_output</span><span class="o">.</span><span class="n">is_error</span>
                <span class="k">if</span> <span class="n">tool</span>
                <span class="k">else</span> <span class="kc">False</span>
            <span class="p">),</span>
        <span class="p">)</span>
        <span class="n">current_reasoning</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">observation_step</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">observation_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="n">current_reasoning</span><span class="p">,</span>
            <span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">return_direct</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tool_output</span><span class="o">.</span><span class="n">is_error</span> <span class="k">if</span> <span class="n">tool</span> <span class="k">else</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_handle_nonexistent_tool_name</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reasoning_step</span><span class="p">):</span>
        <span class="c1"># We still emit a `tool_output` object to the task, so that the LLM can know</span>
        <span class="c1"># it has hallucinated in the next reasoning step.</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
                <span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_CALL</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="c1"># TODO(L10N): This should be localized.</span>
            <span class="n">content</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Error: No such tool named `</span><span class="si">{</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="si">}</span><span class="s2">`."</span>
            <span class="n">tool_output</span> <span class="o">=</span> <span class="n">ToolOutput</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
                <span class="n">tool_name</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">action</span><span class="p">,</span>
                <span class="n">raw_input</span><span class="o">=</span><span class="p">{</span><span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">reasoning_step</span><span class="o">.</span><span class="n">action_input</span><span class="p">},</span>
                <span class="n">raw_output</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
                <span class="n">is_error</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">FUNCTION_OUTPUT</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)})</span>
        <span class="k">return</span> <span class="n">tool_output</span>

    <span class="k">def</span> <span class="nf">_get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">],</span>
        <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get response from reasoning steps."""</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_reasoning</span><span class="p">)</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">_max_iterations</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Reached max iterations."</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">ResponseReasoningStep</span><span class="p">):</span>
            <span class="n">response_step</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ResponseReasoningStep</span><span class="p">,</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">response_step</span><span class="o">.</span><span class="n">response</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="nb">isinstance</span><span class="p">(</span><span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">ObservationReasoningStep</span><span class="p">)</span>
            <span class="ow">and</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">return_direct</span>
        <span class="p">):</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">observation</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="n">current_reasoning</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span>

        <span class="c1"># TODO: add sources from reasoning steps</span>
        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">sources</span><span class="o">=</span><span class="n">sources</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_task_step_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">agent_response</span><span class="p">:</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">is_done</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get task step response."""</span>
        <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">new_steps</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">step</span><span class="o">.</span><span class="n">get_next_step</span><span class="p">(</span>
                    <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
                    <span class="c1"># NOTE: input is unused</span>
                    <span class="nb">input</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">]</span>

        <span class="k">return</span> <span class="n">TaskStepOutput</span><span class="p">(</span>
            <span class="n">output</span><span class="o">=</span><span class="n">agent_response</span><span class="p">,</span>
            <span class="n">task_step</span><span class="o">=</span><span class="n">step</span><span class="p">,</span>
            <span class="n">is_last</span><span class="o">=</span><span class="n">is_done</span><span class="p">,</span>
            <span class="n">next_steps</span><span class="o">=</span><span class="n">new_steps</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_infer_stream_chunk_is_final</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">chunk</span><span class="p">:</span> <span class="n">ChatResponse</span><span class="p">,</span> <span class="n">missed_chunks_storage</span><span class="p">:</span> <span class="nb">list</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Infers if a chunk from a live stream is the start of the final</span>
<span class="sd">        reasoning step. (i.e., and should eventually become</span>
<span class="sd">        ResponseReasoningStep — not part of this function's logic tho.).</span>

<span class="sd">        Args:</span>
<span class="sd">            chunk (ChatResponse): the current chunk stream to check</span>
<span class="sd">            missed_chunks_storage (list): list to store missed chunks</span>

<span class="sd">        Returns:</span>
<span class="sd">            bool: Boolean on whether the chunk is the start of the final response</span>
<span class="sd">        """</span>
        <span class="n">latest_content</span> <span class="o">=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
        <span class="k">if</span> <span class="n">latest_content</span><span class="p">:</span>
            <span class="c1"># doesn't follow thought-action format</span>
            <span class="c1"># keep first chunks</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">latest_content</span><span class="p">)</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="s2">"Thought"</span><span class="p">):</span>
                <span class="n">missed_chunks_storage</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="n">latest_content</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"Thought"</span><span class="p">):</span>
                <span class="k">return</span> <span class="kc">True</span>
            <span class="k">elif</span> <span class="s2">"Answer: "</span> <span class="ow">in</span> <span class="n">latest_content</span><span class="p">:</span>
                <span class="n">missed_chunks_storage</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
                <span class="k">return</span> <span class="kc">True</span>
        <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">_add_back_chunk_to_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">],</span>
        <span class="n">chat_stream</span><span class="p">:</span> <span class="n">Generator</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Helper method for adding back initial chunk stream of final response</span>
<span class="sd">        back to the rest of the chat_stream.</span>

<span class="sd">        Args:</span>
<span class="sd">            chunks List[ChatResponse]: the chunks to add back to the beginning of the</span>
<span class="sd">                                    chat_stream.</span>

<span class="sd">        Return:</span>
<span class="sd">            Generator[ChatResponse, None, None]: the updated chat_stream</span>
<span class="sd">        """</span>

        <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
            <span class="k">yield from</span> <span class="n">chunks</span>
            <span class="k">yield from</span> <span class="n">chat_stream</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_async_add_back_chunk_to_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">],</span>
        <span class="n">chat_stream</span><span class="p">:</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">,</span> <span class="kc">None</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGenerator</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Helper method for adding back initial chunk stream of final response</span>
<span class="sd">        back to the rest of the chat_stream.</span>

<span class="sd">        NOTE: this itself is not an async function.</span>

<span class="sd">        Args:</span>
<span class="sd">            chunks List[ChatResponse]: the chunks to add back to the beginning of the</span>
<span class="sd">                                    chat_stream.</span>

<span class="sd">        Return:</span>
<span class="sd">            AsyncGenerator[ChatResponse, None]: the updated async chat_stream</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">chunks</span><span class="p">:</span>
            <span class="k">yield</span> <span class="n">chunk</span>

        <span class="k">async</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">chat_stream</span><span class="p">:</span>
            <span class="k">yield</span> <span class="n">item</span>

    <span class="k">def</span> <span class="nf">_run_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">if</span> <span class="n">step</span><span class="o">.</span><span class="n">input</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">add_user_step_to_reasoning</span><span class="p">(</span>
                <span class="n">step</span><span class="p">,</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># TODO: see if we want to do step-based inputs</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tools</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
        <span class="n">input_chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">(),</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="c1"># send prompt</span>
        <span class="n">chat_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">input_chat</span><span class="p">)</span>
        <span class="c1"># given react prompt outputs, call tools or return response</span>
        <span class="n">reasoning_steps</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_actions</span><span class="p">(</span>
            <span class="n">task</span><span class="p">,</span> <span class="n">tools</span><span class="p">,</span> <span class="n">output</span><span class="o">=</span><span class="n">chat_response</span>
        <span class="p">)</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">reasoning_steps</span><span class="p">)</span>
        <span class="n">agent_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response</span><span class="p">(</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">agent_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_task_step_response</span><span class="p">(</span><span class="n">agent_response</span><span class="p">,</span> <span class="n">step</span><span class="p">,</span> <span class="n">is_done</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">if</span> <span class="n">step</span><span class="o">.</span><span class="n">input</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">add_user_step_to_reasoning</span><span class="p">(</span>
                <span class="n">step</span><span class="p">,</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># TODO: see if we want to do step-based inputs</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tools</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>

        <span class="n">input_chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">(),</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="c1"># send prompt</span>
        <span class="n">chat_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span><span class="n">input_chat</span><span class="p">)</span>
        <span class="c1"># given react prompt outputs, call tools or return response</span>
        <span class="n">reasoning_steps</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aprocess_actions</span><span class="p">(</span>
            <span class="n">task</span><span class="p">,</span> <span class="n">tools</span><span class="p">,</span> <span class="n">output</span><span class="o">=</span><span class="n">chat_response</span>
        <span class="p">)</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">reasoning_steps</span><span class="p">)</span>
        <span class="n">agent_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response</span><span class="p">(</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">agent_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_task_step_response</span><span class="p">(</span><span class="n">agent_response</span><span class="p">,</span> <span class="n">step</span><span class="p">,</span> <span class="n">is_done</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_run_step_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">if</span> <span class="n">step</span><span class="o">.</span><span class="n">input</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">add_user_step_to_reasoning</span><span class="p">(</span>
                <span class="n">step</span><span class="p">,</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># TODO: see if we want to do step-based inputs</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tools</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>

        <span class="n">input_chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">(),</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="n">chat_stream</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">stream_chat</span><span class="p">(</span><span class="n">input_chat</span><span class="p">)</span>

        <span class="c1"># iterate over stream, break out if is final answer after the "Answer: "</span>
        <span class="n">full_response</span> <span class="o">=</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">missed_chunks_storage</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">for</span> <span class="n">latest_chunk</span> <span class="ow">in</span> <span class="n">chat_stream</span><span class="p">:</span>
            <span class="n">full_response</span> <span class="o">=</span> <span class="n">latest_chunk</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_stream_chunk_is_final</span><span class="p">(</span>
                <span class="n">latest_chunk</span><span class="p">,</span> <span class="n">missed_chunks_storage</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="c1"># given react prompt outputs, call tools or return response</span>
            <span class="n">reasoning_steps</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_actions</span><span class="p">(</span>
                <span class="n">task</span><span class="p">,</span> <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span> <span class="n">output</span><span class="o">=</span><span class="n">full_response</span><span class="p">,</span> <span class="n">is_streaming</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">reasoning_steps</span><span class="p">)</span>
            <span class="c1"># use _get_response to return intermediate response</span>
            <span class="n">agent_response</span><span class="p">:</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response</span><span class="p">(</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="n">agent_response</span><span class="o">.</span><span class="n">is_dummy_stream</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                    <span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">content</span><span class="o">=</span><span class="n">agent_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Get the response in a separate thread so we can yield the response</span>
            <span class="n">response_stream</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_back_chunk_to_stream</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="o">*</span><span class="n">missed_chunks_storage</span><span class="p">,</span> <span class="n">latest_chunk</span><span class="p">],</span> <span class="n">chat_stream</span><span class="o">=</span><span class="n">chat_stream</span>
            <span class="p">)</span>

            <span class="n">agent_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
                <span class="n">chat_stream</span><span class="o">=</span><span class="n">response_stream</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span>
                <span class="n">target</span><span class="o">=</span><span class="n">agent_response</span><span class="o">.</span><span class="n">write_response_to_history</span><span class="p">,</span>
                <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],),</span>
                <span class="n">kwargs</span><span class="o">=</span><span class="p">{</span><span class="s2">"on_stream_end_fn"</span><span class="p">:</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">finalize_task</span><span class="p">,</span> <span class="n">task</span><span class="p">)},</span>
            <span class="p">)</span>
            <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_task_step_response</span><span class="p">(</span><span class="n">agent_response</span><span class="p">,</span> <span class="n">step</span><span class="p">,</span> <span class="n">is_done</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_step_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span>
        <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">if</span> <span class="n">step</span><span class="o">.</span><span class="n">input</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">add_user_step_to_reasoning</span><span class="p">(</span>
                <span class="n">step</span><span class="p">,</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># TODO: see if we want to do step-based inputs</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tools</span><span class="p">(</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>

        <span class="n">input_chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_react_chat_formatter</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">)</span>
            <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">(),</span>
            <span class="n">current_reasoning</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="n">chat_stream</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">astream_chat</span><span class="p">(</span><span class="n">input_chat</span><span class="p">)</span>

        <span class="c1"># iterate over stream, break out if is final answer after the "Answer: "</span>
        <span class="n">full_response</span> <span class="o">=</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"assistant"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">missed_chunks_storage</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">is_done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">latest_chunk</span> <span class="ow">in</span> <span class="n">chat_stream</span><span class="p">:</span>
            <span class="n">full_response</span> <span class="o">=</span> <span class="n">latest_chunk</span>
            <span class="n">is_done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_stream_chunk_is_final</span><span class="p">(</span>
                <span class="n">latest_chunk</span><span class="p">,</span> <span class="n">missed_chunks_storage</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">is_done</span><span class="p">:</span>
            <span class="c1"># given react prompt outputs, call tools or return response</span>
            <span class="n">reasoning_steps</span><span class="p">,</span> <span class="n">is_done</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aprocess_actions</span><span class="p">(</span>
                <span class="n">task</span><span class="p">,</span> <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span> <span class="n">output</span><span class="o">=</span><span class="n">full_response</span><span class="p">,</span> <span class="n">is_streaming</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>
            <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">reasoning_steps</span><span class="p">)</span>
            <span class="c1"># use _get_response to return intermediate response</span>
            <span class="n">agent_response</span><span class="p">:</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_response</span><span class="p">(</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"current_reasoning"</span><span class="p">],</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">]</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="n">is_done</span><span class="p">:</span>
                <span class="n">agent_response</span><span class="o">.</span><span class="n">is_dummy_stream</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">put</span><span class="p">(</span>
                    <span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">content</span><span class="o">=</span><span class="n">agent_response</span><span class="o">.</span><span class="n">response</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Get the response in a separate thread so we can yield the response</span>
            <span class="n">response_stream</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_async_add_back_chunk_to_stream</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="o">*</span><span class="n">missed_chunks_storage</span><span class="p">,</span> <span class="n">latest_chunk</span><span class="p">],</span> <span class="n">chat_stream</span><span class="o">=</span><span class="n">chat_stream</span>
            <span class="p">)</span>

            <span class="n">agent_response</span> <span class="o">=</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
                <span class="n">achat_stream</span><span class="o">=</span><span class="n">response_stream</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="c1"># create task to write chat response to history</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span>
                <span class="n">agent_response</span><span class="o">.</span><span class="n">awrite_response_to_history</span><span class="p">(</span>
                    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">],</span>
                    <span class="n">on_stream_end_fn</span><span class="o">=</span><span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">finalize_task</span><span class="p">,</span> <span class="n">task</span><span class="p">),</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="c1"># wait until response writing is done</span>
            <span class="n">agent_response</span><span class="o">.</span><span class="n">_ensure_async_setup</span><span class="p">()</span>

            <span class="k">await</span> <span class="n">agent_response</span><span class="o">.</span><span class="n">is_function_false_event</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_task_step_response</span><span class="p">(</span><span class="n">agent_response</span><span class="p">,</span> <span class="n">step</span><span class="p">,</span> <span class="n">is_done</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (async)."""</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (stream)."""</span>
        <span class="c1"># TODO: figure out if we need a different type for TaskStepOutput</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_step_stream</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_step</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run step (async stream)."""</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step_stream</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
        <span class="c1"># add new messages to memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span>
            <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span> <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="c1"># reset new memory</span>
        <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set callback manager."""</span>
        <span class="c1"># TODO: make this abstractmethod (right now will break some agent impls)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.from_tools "Permanent link")

```
from_tools(tools: Optional[Sequence[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, tool_retriever: Optional[[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, max_iterations: int = 10, react_chat_formatter: Optional[[ReActChatFormatter](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter "llama_index.core.agent.react.formatter.ReActChatFormatter")] = None, output_parser: Optional[ReActOutputParser] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, verbose: bool = False, handle_reasoning_failure_fn: Optional[Callable[[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager"), Exception], [ToolOutput](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolOutput "llama_index.core.tools.ToolOutput")]] = None, **kwargs: Any) -> [ReActAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker "llama_index.core.agent.react.step.ReActAgentWorker")
```

Convenience constructor method from set of BaseTools (Optional).

NOTE: kwargs should have been exhausted by this point. In other words the various upstream components such as BaseSynthesizer (response synthesizer) or BaseRetriever should have picked up off their respective kwargs in their constructions.

**Returns:**

| Type | Description |
| --- | --- |
| `[ReActAgentWorker](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker "llama_index.core.agent.react.step.ReActAgentWorker")` | 
ReActAgentWorker



 |

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
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
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">react_chat_formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActChatFormatter</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
        <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
    <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActAgentWorker"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Convenience constructor method from set of BaseTools (Optional).</span>

<span class="sd">    NOTE: kwargs should have been exhausted by this point. In other words</span>
<span class="sd">    the various upstream components such as BaseSynthesizer (response synthesizer)</span>
<span class="sd">    or BaseRetriever should have picked up off their respective kwargs in their</span>
<span class="sd">    constructions.</span>

<span class="sd">    Returns:</span>
<span class="sd">        ReActAgentWorker</span>
<span class="sd">    """</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span> <span class="ow">or</span> <span class="p">[],</span>
        <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">max_iterations</span><span class="o">=</span><span class="n">max_iterations</span><span class="p">,</span>
        <span class="n">react_chat_formatter</span><span class="o">=</span><span class="n">react_chat_formatter</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="o">=</span><span class="n">output_parser</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="o">=</span><span class="n">handle_reasoning_failure_fn</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### initialize\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.initialize_step "Permanent link")

```
initialize_step(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep")
```

Initialize step from task.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
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
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">initialize_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStep</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize step from task."""</span>
    <span class="n">sources</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># temporary memory for new messages</span>
    <span class="n">new_memory</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>

    <span class="c1"># initialize task state</span>
    <span class="n">task_state</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">,</span>
        <span class="s2">"current_reasoning"</span><span class="p">:</span> <span class="n">current_reasoning</span><span class="p">,</span>
        <span class="s2">"new_memory"</span><span class="p">:</span> <span class="n">new_memory</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task_state</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">TaskStep</span><span class="p">(</span>
        <span class="n">task_id</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">task_id</span><span class="p">,</span>
        <span class="n">step_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()),</span>
        <span class="nb">input</span><span class="o">=</span><span class="n">task</span><span class="o">.</span><span class="n">input</span><span class="p">,</span>
        <span class="n">step_state</span><span class="o">=</span><span class="p">{</span><span class="s2">"is_first"</span><span class="p">:</span> <span class="kc">True</span><span class="p">},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_tools [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.get_tools "Permanent link")

```
get_tools(input: str) -> List[[AsyncBaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.AsyncBaseTool "llama_index.core.tools.types.AsyncBaseTool")]
```

Get tools.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">AsyncBaseTool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get tools."""</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">adapt_to_async_tool</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span><span class="p">(</span><span class="nb">input</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### run\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.run_step "Permanent link")

```
run_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">run_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### arun\_step `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.arun_step "Permanent link")

```
arun_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (async).

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">arun_step</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (async)."""</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### stream\_step [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.stream_step "Permanent link")

```
stream_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (stream).

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">stream_step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (stream)."""</span>
    <span class="c1"># TODO: figure out if we need a different type for TaskStepOutput</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_step_stream</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### astream\_step `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.astream_step "Permanent link")

```
astream_step(step: [TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.agent.types.TaskStep"), task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> [TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.agent.types.TaskStepOutput")
```

Run step (async stream).

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"run_step"</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span> <span class="nf">astream_step</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">step</span><span class="p">:</span> <span class="n">TaskStep</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TaskStepOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run step (async stream)."""</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_arun_step_stream</span><span class="p">(</span><span class="n">step</span><span class="p">,</span> <span class="n">task</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### finalize\_task [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.finalize_task "Permanent link")

```
finalize_task(task: [Task](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.Task "llama_index.core.agent.types.Task"), **kwargs: Any) -> None
```

Finalize task, after all the steps are completed.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">finalize_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">Task</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Finalize task, after all the steps are completed."""</span>
    <span class="c1"># add new messages to memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">set</span><span class="p">(</span>
        <span class="n">task</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span> <span class="o">+</span> <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
    <span class="p">)</span>
    <span class="c1"># reset new memory</span>
    <span class="n">task</span><span class="o">.</span><span class="n">extra_state</span><span class="p">[</span><span class="s2">"new_memory"</span><span class="p">]</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### set\_callback\_manager [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActAgentWorker.set_callback_manager "Permanent link")

```
set_callback_manager(callback_manager: [CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")) -> None
```

Set callback manager.

Source code in `llama-index-core/llama_index/core/agent/react/step.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_callback_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback_manager</span><span class="p">:</span> <span class="n">CallbackManager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set callback manager."""</span>
    <span class="c1"># TODO: make this abstractmethod (right now will break some agent impls)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>
</code></pre></div></td></tr></tbody></table>

ReActChatFormatter [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseAgentChatFormatter`

ReAct chat formatter.

Source code in `llama-index-core/llama_index/core/agent/react/formatter.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 52</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ReActChatFormatter</span><span class="p">(</span><span class="n">BaseAgentChatFormatter</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ReAct chat formatter."""</span>

    <span class="n">system_header</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">REACT_CHAT_SYSTEM_HEADER</span>  <span class="c1"># default</span>
    <span class="n">context</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>  <span class="c1"># not needed w/ default</span>

    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Format chat history into list of ChatMessage."""</span>
        <span class="n">current_reasoning</span> <span class="o">=</span> <span class="n">current_reasoning</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="n">format_args</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"tool_desc"</span><span class="p">:</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">get_react_tool_descriptions</span><span class="p">(</span><span class="n">tools</span><span class="p">)),</span>
            <span class="s2">"tool_names"</span><span class="p">:</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get_name</span><span class="p">()</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]),</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">context</span><span class="p">:</span>
            <span class="n">format_args</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">context</span>

        <span class="n">fmt_sys_header</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_header</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">format_args</span><span class="p">)</span>

        <span class="c1"># format reasoning history as alternating user and assistant messages</span>
        <span class="c1"># where the assistant messages are thoughts and actions and the user</span>
        <span class="c1"># messages are observations</span>
        <span class="n">reasoning_history</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">reasoning_step</span> <span class="ow">in</span> <span class="n">current_reasoning</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">,</span> <span class="n">ObservationReasoningStep</span><span class="p">):</span>
                <span class="n">message</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">message</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span>
                <span class="p">)</span>
            <span class="n">reasoning_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">fmt_sys_header</span><span class="p">),</span>
            <span class="o">*</span><span class="n">chat_history</span><span class="p">,</span>
            <span class="o">*</span><span class="n">reasoning_history</span><span class="p">,</span>
        <span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">system_header</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActChatFormatter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create ReActChatFormatter from defaults."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">system_header</span><span class="p">:</span>
            <span class="n">system_header</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">REACT_CHAT_SYSTEM_HEADER</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">context</span>
                <span class="k">else</span> <span class="n">CONTEXT_REACT_CHAT_SYSTEM_HEADER</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">ReActChatFormatter</span><span class="p">(</span>
            <span class="n">system_header</span><span class="o">=</span><span class="n">system_header</span><span class="p">,</span>
            <span class="n">context</span><span class="o">=</span><span class="n">context</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_context</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">context</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActChatFormatter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create ReActChatFormatter from context.</span>

<span class="sd">        NOTE: deprecated</span>

<span class="sd">        """</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"ReActChatFormatter.from_context is deprecated, please use `from_defaults` instead."</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">ReActChatFormatter</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">system_header</span><span class="o">=</span><span class="n">CONTEXT_REACT_CHAT_SYSTEM_HEADER</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### format [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter.format "Permanent link")

```
format(tools: Sequence[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")], chat_history: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], current_reasoning: Optional[List[BaseReasoningStep]] = None) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Format chat history into list of ChatMessage.

Source code in `llama-index-core/llama_index/core/agent/react/formatter.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
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
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
    <span class="n">current_reasoning</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseReasoningStep</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Format chat history into list of ChatMessage."""</span>
    <span class="n">current_reasoning</span> <span class="o">=</span> <span class="n">current_reasoning</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="n">format_args</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"tool_desc"</span><span class="p">:</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">get_react_tool_descriptions</span><span class="p">(</span><span class="n">tools</span><span class="p">)),</span>
        <span class="s2">"tool_names"</span><span class="p">:</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">tool</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get_name</span><span class="p">()</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]),</span>
    <span class="p">}</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">context</span><span class="p">:</span>
        <span class="n">format_args</span><span class="p">[</span><span class="s2">"context"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">context</span>

    <span class="n">fmt_sys_header</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">system_header</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">format_args</span><span class="p">)</span>

    <span class="c1"># format reasoning history as alternating user and assistant messages</span>
    <span class="c1"># where the assistant messages are thoughts and actions and the user</span>
    <span class="c1"># messages are observations</span>
    <span class="n">reasoning_history</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">reasoning_step</span> <span class="ow">in</span> <span class="n">current_reasoning</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">reasoning_step</span><span class="p">,</span> <span class="n">ObservationReasoningStep</span><span class="p">):</span>
            <span class="n">message</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">message</span> <span class="o">=</span> <span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="n">reasoning_step</span><span class="o">.</span><span class="n">get_content</span><span class="p">(),</span>
            <span class="p">)</span>
        <span class="n">reasoning_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">fmt_sys_header</span><span class="p">),</span>
        <span class="o">*</span><span class="n">chat_history</span><span class="p">,</span>
        <span class="o">*</span><span class="n">reasoning_history</span><span class="p">,</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter.from_defaults "Permanent link")

```
from_defaults(system_header: Optional[str] = None, context: Optional[str] = None) -> [ReActChatFormatter](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter "llama_index.core.agent.react.formatter.ReActChatFormatter")
```

Create ReActChatFormatter from defaults.

Source code in `llama-index-core/llama_index/core/agent/react/formatter.py`

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
<span class="normal">116</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">system_header</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActChatFormatter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create ReActChatFormatter from defaults."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">system_header</span><span class="p">:</span>
        <span class="n">system_header</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">REACT_CHAT_SYSTEM_HEADER</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">context</span>
            <span class="k">else</span> <span class="n">CONTEXT_REACT_CHAT_SYSTEM_HEADER</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">ReActChatFormatter</span><span class="p">(</span>
        <span class="n">system_header</span><span class="o">=</span><span class="n">system_header</span><span class="p">,</span>
        <span class="n">context</span><span class="o">=</span><span class="n">context</span> <span class="ow">or</span> <span class="s2">""</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_context `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter.from_context "Permanent link")

```
from_context(context: str) -> [ReActChatFormatter](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/#llama_index.core.agent.react.ReActChatFormatter "llama_index.core.agent.react.formatter.ReActChatFormatter")
```

Create ReActChatFormatter from context.

NOTE: deprecated

Source code in `llama-index-core/llama_index/core/agent/react/formatter.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">118</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_context</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">context</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ReActChatFormatter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create ReActChatFormatter from context.</span>

<span class="sd">    NOTE: deprecated</span>

<span class="sd">    """</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
        <span class="s2">"ReActChatFormatter.from_context is deprecated, please use `from_defaults` instead."</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">ReActChatFormatter</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">system_header</span><span class="o">=</span><span class="n">CONTEXT_REACT_CHAT_SYSTEM_HEADER</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openai legacy](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/)[Next Agentops](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/agentops/)
