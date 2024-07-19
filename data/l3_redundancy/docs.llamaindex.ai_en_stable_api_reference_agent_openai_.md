Title: Openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/

Markdown Content:
Openai - LlamaIndex


OpenAIAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAgent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

Bases: `[AgentRunner](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.AgentRunner "llama_index.core.agent.runner.base.AgentRunner")`

OpenAI agent.

Subclasses AgentRunner with a OpenAIAgentWorker.

For the legacy implementation see:

```
from llama_index..agent.legacy.openai.base import OpenAIAgent
```

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 36</span>
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
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIAgent</span><span class="p">(</span><span class="n">AgentRunner</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAI agent.</span>

<span class="sd">    Subclasses AgentRunner with a OpenAIAgentWorker.</span>

<span class="sd">    For the legacy implementation see:</span>
<span class="sd">    ```python</span>
<span class="sd">    from llama_index..agent.legacy.openai.base import OpenAIAgent</span>
<span class="sd">    ```</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">OpenAI</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
        <span class="n">default_tool_choice</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_call_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">OpenAIToolCall</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span>
        <span class="n">step_engine</span> <span class="o">=</span> <span class="n">OpenAIAgentWorker</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">tool_call_parser</span><span class="o">=</span><span class="n">tool_call_parser</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">step_engine</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">default_tool_choice</span><span class="o">=</span><span class="n">default_tool_choice</span><span class="p">,</span>
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
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
        <span class="n">default_tool_choice</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_call_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">OpenAIToolCall</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAgent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create an OpenAIAgent from a list of tools.</span>

<span class="sd">        Similar to `from_defaults` in other classes, this method will</span>
<span class="sd">        infer defaults for a variety of parameters, including the LLM,</span>
<span class="sd">        if they are not specified.</span>

<span class="sd">        """</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">OpenAI</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"llm must be a OpenAI instance"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">is_function_calling_model</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Model name </span><span class="si">{</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="si">}</span><span class="s2"> does not support function calling API. "</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
                <span class="p">)</span>
            <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">)]</span>

        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">default_tool_choice</span><span class="o">=</span><span class="n">default_tool_choice</span><span class="p">,</span>
            <span class="n">tool_call_parser</span><span class="o">=</span><span class="n">tool_call_parser</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAgent.from_tools "Permanent link")

```
from_tools(tools: Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, tool_retriever: Optional[[ObjectRetriever](https://docs.llamaindex.ai/en/stable/api_reference/objects/#llama_index.core.objects.ObjectRetriever "llama_index.core.objects.base.ObjectRetriever")[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")] = None, memory_cls: Type[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")] = ChatMemoryBuffer, verbose: bool = False, max_function_calls: int = DEFAULT_MAX_FUNCTION_CALLS, default_tool_choice: str = 'auto', callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, system_prompt: Optional[str] = None, prefix_messages: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, tool_call_parser: Optional[Callable[[OpenAIToolCall], Dict]] = None, **kwargs: Any) -> [OpenAIAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAgent "llama_index.agent.openai.base.OpenAIAgent")
```

Create an OpenAIAgent from a list of tools.

Similar to `from_defaults` in other classes, this method will infer defaults for a variety of parameters, including the LLM, if they are not specified.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 81</span>
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
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_retriever</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
    <span class="n">default_tool_choice</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_call_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">OpenAIToolCall</span><span class="p">],</span> <span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAgent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create an OpenAIAgent from a list of tools.</span>

<span class="sd">    Similar to `from_defaults` in other classes, this method will</span>
<span class="sd">    infer defaults for a variety of parameters, including the LLM,</span>
<span class="sd">    if they are not specified.</span>

<span class="sd">    """</span>
    <span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">OpenAI</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"llm must be a OpenAI instance"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">is_function_calling_model</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Model name </span><span class="si">{</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="si">}</span><span class="s2"> does not support function calling API. "</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">system_prompt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">prefix_messages</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify both system_prompt and prefix_messages"</span>
            <span class="p">)</span>
        <span class="n">prefix_messages</span> <span class="o">=</span> <span class="p">[</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">system_prompt</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="s2">"system"</span><span class="p">)]</span>

    <span class="n">prefix_messages</span> <span class="o">=</span> <span class="n">prefix_messages</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
        <span class="n">tool_retriever</span><span class="o">=</span><span class="n">tool_retriever</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">default_tool_choice</span><span class="o">=</span><span class="n">default_tool_choice</span><span class="p">,</span>
        <span class="n">tool_call_parser</span><span class="o">=</span><span class="n">tool_call_parser</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

OpenAIAssistantAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.BaseAgent "llama_index.core.agent.types.BaseAgent")`

OpenAIAssistant agent.

Wrapper around OpenAI assistant API: https://platform.openai.com/docs/assistants/overview

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">171</span>
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
<span class="normal">586</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIAssistantAgent</span><span class="p">(</span><span class="n">BaseAgent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAIAssistant agent.</span>

<span class="sd">    Wrapper around OpenAI assistant API: https://platform.openai.com/docs/assistants/overview</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">assistant</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]],</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">thread_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">run_retrieve_sleep_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span>
        <span class="n">file_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="kn">from</span> <span class="nn">openai.types.beta.assistant</span> <span class="kn">import</span> <span class="n">Assistant</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">OpenAI</span><span class="p">,</span> <span class="n">client</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Assistant</span><span class="p">,</span> <span class="n">assistant</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span> <span class="o">=</span> <span class="n">tools</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">thread_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">thread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">create</span><span class="p">()</span>
            <span class="n">thread_id</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span> <span class="o">=</span> <span class="n">thread_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span> <span class="o">=</span> <span class="n">instructions_prefix</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_run_retrieve_sleep_time</span> <span class="o">=</span> <span class="n">run_retrieve_sleep_time</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_dict</span> <span class="o">=</span> <span class="n">file_dict</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_new</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">instructions</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">openai_tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">thread_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4-1106-preview"</span><span class="p">,</span>
        <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">run_retrieve_sleep_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span>
        <span class="n">files</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAssistantAgent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From new assistant.</span>

<span class="sd">        Args:</span>
<span class="sd">            name: name of assistant</span>
<span class="sd">            instructions: instructions for assistant</span>
<span class="sd">            tools: list of tools</span>
<span class="sd">            openai_tools: list of openai tools</span>
<span class="sd">            thread_id: thread id</span>
<span class="sd">            model: model</span>
<span class="sd">            run_retrieve_sleep_time: run retrieve sleep time</span>
<span class="sd">            files: files</span>
<span class="sd">            instructions_prefix: instructions prefix</span>
<span class="sd">            callback_manager: callback manager</span>
<span class="sd">            verbose: verbose</span>
<span class="sd">            file_ids: list of file ids</span>
<span class="sd">            api_key: OpenAI API key</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>

        <span class="c1"># this is the set of openai tools</span>
        <span class="c1"># not to be confused with the tools we pass in for function calling</span>
        <span class="n">openai_tools</span> <span class="o">=</span> <span class="n">openai_tools</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">tool_fns</span> <span class="o">=</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">to_openai_tool</span><span class="p">()</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]</span>
        <span class="n">all_openai_tools</span> <span class="o">=</span> <span class="n">openai_tools</span> <span class="o">+</span> <span class="n">tool_fns</span>

        <span class="c1"># initialize client</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

        <span class="c1"># process files</span>
        <span class="n">files</span> <span class="o">=</span> <span class="n">files</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">file_ids</span> <span class="o">=</span> <span class="n">file_ids</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="n">file_dict</span> <span class="o">=</span> <span class="n">_process_files</span><span class="p">(</span><span class="n">client</span><span class="p">,</span> <span class="n">files</span><span class="p">)</span>

        <span class="c1"># TODO: openai's typing is a bit sus</span>
        <span class="n">all_openai_tools</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">all_openai_tools</span><span class="p">)</span>
        <span class="n">assistant</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">assistants</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">instructions</span><span class="o">=</span><span class="n">instructions</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">all_openai_tools</span><span class="p">),</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">client</span><span class="p">,</span>
            <span class="n">assistant</span><span class="p">,</span>
            <span class="n">tools</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="n">thread_id</span><span class="p">,</span>
            <span class="n">instructions_prefix</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
            <span class="n">file_dict</span><span class="o">=</span><span class="n">file_dict</span><span class="p">,</span>
            <span class="n">run_retrieve_sleep_time</span><span class="o">=</span><span class="n">run_retrieve_sleep_time</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_existing</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">assistant_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">thread_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">run_retrieve_sleep_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAssistantAgent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""From existing assistant id.</span>

<span class="sd">        Args:</span>
<span class="sd">            assistant_id: id of assistant</span>
<span class="sd">            tools: list of BaseTools Assistant can use</span>
<span class="sd">            thread_id: thread id</span>
<span class="sd">            run_retrieve_sleep_time: run retrieve sleep time</span>
<span class="sd">            instructions_prefix: instructions prefix</span>
<span class="sd">            callback_manager: callback manager</span>
<span class="sd">            api_key: OpenAI API key</span>
<span class="sd">            verbose: verbose</span>

<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>

        <span class="c1"># initialize client</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

        <span class="c1"># get assistant</span>
        <span class="n">assistant</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">assistants</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">assistant_id</span><span class="p">)</span>
        <span class="c1"># assistant.tools is incompatible with BaseTools so have to pass from params</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">client</span><span class="p">,</span>
            <span class="n">assistant</span><span class="p">,</span>
            <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="n">thread_id</span><span class="p">,</span>
            <span class="n">instructions_prefix</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
            <span class="n">run_retrieve_sleep_time</span><span class="o">=</span><span class="n">run_retrieve_sleep_time</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">assistant</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get assistant."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">thread_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get thread id."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">files_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get files dict."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_dict</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="n">raw_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">messages</span><span class="o">.</span><span class="n">list</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">order</span><span class="o">=</span><span class="s2">"asc"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">from_openai_thread_messages</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">raw_messages</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete and create a new thread."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">)</span>
        <span class="n">thread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">create</span><span class="p">()</span>
        <span class="n">thread_id</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span> <span class="o">=</span> <span class="n">thread_id</span>

    <span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span>

    <span class="k">def</span> <span class="nf">upload_files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">files</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Upload files."""</span>
        <span class="k">return</span> <span class="n">_process_files</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="n">files</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add message to assistant."""</span>
        <span class="n">attachments</span> <span class="o">=</span> <span class="n">format_attachments</span><span class="p">(</span><span class="n">file_ids</span><span class="o">=</span><span class="n">file_ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">messages</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
            <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
            <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
            <span class="n">attachments</span><span class="o">=</span><span class="n">attachments</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_run_function_calling</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run function calling."""</span>
        <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">run</span><span class="o">.</span><span class="n">required_action</span><span class="o">.</span><span class="n">submit_tool_outputs</span><span class="o">.</span><span class="n">tool_calls</span>
        <span class="n">tool_output_dicts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">tool_output_objs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">tool_call</span> <span class="ow">in</span> <span class="n">tool_calls</span><span class="p">:</span>
            <span class="n">fn_obj</span> <span class="o">=</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">function</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">tool_output</span> <span class="o">=</span> <span class="n">call_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">,</span> <span class="n">fn_obj</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">)</span>
            <span class="n">tool_output_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">{</span><span class="s2">"tool_call_id"</span><span class="p">:</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="s2">"output"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)}</span>
            <span class="p">)</span>
            <span class="n">tool_output_objs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)</span>

        <span class="c1"># submit tool outputs</span>
        <span class="c1"># TODO: openai's typing is a bit sus</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">submit_tool_outputs</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
            <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">tool_outputs</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">tool_output_dicts</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">tool_output_objs</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_arun_function_calling</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run function calling."""</span>
        <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">run</span><span class="o">.</span><span class="n">required_action</span><span class="o">.</span><span class="n">submit_tool_outputs</span><span class="o">.</span><span class="n">tool_calls</span>
        <span class="n">tool_output_dicts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">tool_output_objs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ToolOutput</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">tool_call</span> <span class="ow">in</span> <span class="n">tool_calls</span><span class="p">:</span>
            <span class="n">fn_obj</span> <span class="o">=</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">function</span>
            <span class="n">_</span><span class="p">,</span> <span class="n">tool_output</span> <span class="o">=</span> <span class="k">await</span> <span class="n">acall_function</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span><span class="p">,</span> <span class="n">fn_obj</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span>
            <span class="p">)</span>
            <span class="n">tool_output_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="p">{</span><span class="s2">"tool_call_id"</span><span class="p">:</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="s2">"output"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)}</span>
            <span class="p">)</span>
            <span class="n">tool_output_objs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool_output</span><span class="p">)</span>

        <span class="c1"># submit tool outputs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">submit_tool_outputs</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
            <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">tool_outputs</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">tool_output_dicts</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">tool_output_objs</span>

    <span class="k">def</span> <span class="nf">run_assistant</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run assistant."""</span>
        <span class="n">instructions_prefix</span> <span class="o">=</span> <span class="n">instructions_prefix</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span>
        <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
            <span class="n">assistant_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">instructions</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">openai.types.beta.threads</span> <span class="kn">import</span> <span class="n">Run</span>

        <span class="n">run</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Run</span><span class="p">,</span> <span class="n">run</span><span class="p">)</span>

        <span class="n">sources</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"queued"</span><span class="p">,</span> <span class="s2">"in_progress"</span><span class="p">,</span> <span class="s2">"requires_action"</span><span class="p">]:</span>
            <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
                <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="o"></span> <span class="s2">"failed"</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Run failed with status </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">status</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">last_error</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">run</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">arun_assistant</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run assistant."""</span>
        <span class="n">instructions_prefix</span> <span class="o">=</span> <span class="n">instructions_prefix</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span>
        <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
            <span class="n">assistant_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">instructions</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">openai.types.beta.threads</span> <span class="kn">import</span> <span class="n">Run</span>

        <span class="n">run</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Run</span><span class="p">,</span> <span class="n">run</span><span class="p">)</span>

        <span class="n">sources</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">while</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"queued"</span><span class="p">,</span> <span class="s2">"in_progress"</span><span class="p">,</span> <span class="s2">"requires_action"</span><span class="p">]:</span>
            <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
                <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="o"></span> <span class="s2">"failed"</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Run failed with status </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">status</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">last_error</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">run</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">}</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">latest_message</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatMessage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get latest message."""</span>
        <span class="n">raw_messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">messages</span><span class="o">.</span><span class="n">list</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">order</span><span class="o">=</span><span class="s2">"desc"</span>
        <span class="p">)</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">from_openai_thread_messages</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">raw_messages</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">ChatResponseMode</span> <span class="o">=</span> <span class="n">ChatResponseMode</span><span class="o">.</span><span class="n">WAIT</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Main chat interface."""</span>
        <span class="c1"># TODO: since chat interface doesn't expose additional kwargs</span>
        <span class="c1"># we can't pass in file_ids per message</span>
        <span class="n">_added_message_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">_run</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_assistant</span><span class="p">(</span>
            <span class="n">instructions_prefix</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">latest_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">latest_message</span>
        <span class="c1"># get most recent message content</span>
        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">latest_message</span><span class="o">.</span><span class="n">content</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">],</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="n">ChatResponseMode</span> <span class="o">=</span> <span class="n">ChatResponseMode</span><span class="o">.</span><span class="n">WAIT</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronous main chat interface."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="n">run</span><span class="p">,</span> <span class="n">metadata</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">arun_assistant</span><span class="p">(</span>
            <span class="n">instructions_prefix</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">latest_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">latest_message</span>
        <span class="c1"># get most recent message content</span>
        <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span>
            <span class="n">response</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">latest_message</span><span class="o">.</span><span class="n">content</span><span class="p">),</span>
            <span class="n">sources</span><span class="o">=</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"sources"</span><span class="p">],</span>
        <span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">AGENT_STEP</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">:</span> <span class="p">[</span><span class="n">message</span><span class="p">]},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">chat_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chat</span><span class="p">(</span>
                <span class="n">message</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">,</span> <span class="n">function_call</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">ChatResponseMode</span><span class="o">.</span><span class="n">WAIT</span>
            <span class="p">)</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">chat_response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span>
            <span class="n">e</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">chat_response</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">AGENT_STEP</span><span class="p">,</span>
            <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">:</span> <span class="p">[</span><span class="n">message</span><span class="p">]},</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">chat_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_achat</span><span class="p">(</span>
                <span class="n">message</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">,</span> <span class="n">function_call</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">ChatResponseMode</span><span class="o">.</span><span class="n">WAIT</span>
            <span class="p">)</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">chat_response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span>
            <span class="n">e</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">chat_response</span><span class="p">})</span>
        <span class="k">return</span> <span class="n">chat_response</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"stream_chat not implemented"</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">function_call</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"astream_chat not implemented"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### assistant `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.assistant "Permanent link")

```
assistant: Any
```

Get assistant.

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.client "Permanent link")

```
client: Any
```

Get client.

### thread\_id `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.thread_id "Permanent link")

```
thread_id: str
```

Get thread id.

### files\_dict `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.files_dict "Permanent link")

```
files_dict: Dict[str, str]
```

Get files dict.

### latest\_message `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.latest_message "Permanent link")

```
latest_message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")
```

Get latest message.

### from\_new `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.from_new "Permanent link")

```
from_new(name: str, instructions: str, tools: Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, openai_tools: Optional[List[Dict]] = None, thread_id: Optional[str] = None, model: str = 'gpt-4-1106-preview', instructions_prefix: Optional[str] = None, run_retrieve_sleep_time: float = 0.1, files: Optional[List[str]] = None, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, verbose: bool = False, file_ids: Optional[List[str]] = None, api_key: Optional[str] = None) -> [OpenAIAssistantAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent "llama_index.agent.openai.openai_assistant_agent.OpenAIAssistantAgent")
```

From new assistant.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | 
name of assistant



 | _required_ |
| `instructions` | `str` | 

instructions for assistant



 | _required_ |
| `tools` | `Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]]` | 

list of tools



 | `None` |
| `openai_tools` | `Optional[List[Dict]]` | 

list of openai tools



 | `None` |
| `thread_id` | `Optional[str]` | 

thread id



 | `None` |
| `model` | `str` | 

model



 | `'gpt-4-1106-preview'` |
| `run_retrieve_sleep_time` | `float` | 

run retrieve sleep time



 | `0.1` |
| `files` | `Optional[List[str]]` | 

files



 | `None` |
| `instructions_prefix` | `Optional[str]` | 

instructions prefix



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

callback manager



 | `None` |
| `verbose` | `bool` | 

verbose



 | `False` |
| `file_ids` | `Optional[List[str]]` | 

list of file ids



 | `None` |
| `api_key` | `Optional[str]` | 

OpenAI API key



 | `None` |

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">208</span>
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
<span class="normal">279</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_new</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">instructions</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">openai_tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">thread_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4-1106-preview"</span><span class="p">,</span>
    <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">run_retrieve_sleep_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span>
    <span class="n">files</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAssistantAgent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From new assistant.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: name of assistant</span>
<span class="sd">        instructions: instructions for assistant</span>
<span class="sd">        tools: list of tools</span>
<span class="sd">        openai_tools: list of openai tools</span>
<span class="sd">        thread_id: thread id</span>
<span class="sd">        model: model</span>
<span class="sd">        run_retrieve_sleep_time: run retrieve sleep time</span>
<span class="sd">        files: files</span>
<span class="sd">        instructions_prefix: instructions prefix</span>
<span class="sd">        callback_manager: callback manager</span>
<span class="sd">        verbose: verbose</span>
<span class="sd">        file_ids: list of file ids</span>
<span class="sd">        api_key: OpenAI API key</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>

    <span class="c1"># this is the set of openai tools</span>
    <span class="c1"># not to be confused with the tools we pass in for function calling</span>
    <span class="n">openai_tools</span> <span class="o">=</span> <span class="n">openai_tools</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">tools</span> <span class="o">=</span> <span class="n">tools</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">tool_fns</span> <span class="o">=</span> <span class="p">[</span><span class="n">t</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">to_openai_tool</span><span class="p">()</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tools</span><span class="p">]</span>
    <span class="n">all_openai_tools</span> <span class="o">=</span> <span class="n">openai_tools</span> <span class="o">+</span> <span class="n">tool_fns</span>

    <span class="c1"># initialize client</span>
    <span class="n">client</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

    <span class="c1"># process files</span>
    <span class="n">files</span> <span class="o">=</span> <span class="n">files</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">file_ids</span> <span class="o">=</span> <span class="n">file_ids</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="n">file_dict</span> <span class="o">=</span> <span class="n">_process_files</span><span class="p">(</span><span class="n">client</span><span class="p">,</span> <span class="n">files</span><span class="p">)</span>

    <span class="c1"># TODO: openai's typing is a bit sus</span>
    <span class="n">all_openai_tools</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">all_openai_tools</span><span class="p">)</span>
    <span class="n">assistant</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">assistants</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
        <span class="n">instructions</span><span class="o">=</span><span class="n">instructions</span><span class="p">,</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">all_openai_tools</span><span class="p">),</span>
        <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">client</span><span class="p">,</span>
        <span class="n">assistant</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">thread_id</span><span class="o">=</span><span class="n">thread_id</span><span class="p">,</span>
        <span class="n">instructions_prefix</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
        <span class="n">file_dict</span><span class="o">=</span><span class="n">file_dict</span><span class="p">,</span>
        <span class="n">run_retrieve_sleep_time</span><span class="o">=</span><span class="n">run_retrieve_sleep_time</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_existing `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.from_existing "Permanent link")

```
from_existing(assistant_id: str, tools: Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]] = None, thread_id: Optional[str] = None, instructions_prefix: Optional[str] = None, run_retrieve_sleep_time: float = 0.1, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, api_key: Optional[str] = None, verbose: bool = False) -> [OpenAIAssistantAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent "llama_index.agent.openai.openai_assistant_agent.OpenAIAssistantAgent")
```

From existing assistant id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `assistant_id` | `str` | 
id of assistant



 | _required_ |
| `tools` | `Optional[List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]]` | 

list of BaseTools Assistant can use



 | `None` |
| `thread_id` | `Optional[str]` | 

thread id



 | `None` |
| `run_retrieve_sleep_time` | `float` | 

run retrieve sleep time



 | `0.1` |
| `instructions_prefix` | `Optional[str]` | 

instructions prefix



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

callback manager



 | `None` |
| `api_key` | `Optional[str]` | 

OpenAI API key



 | `None` |
| `verbose` | `bool` | 

verbose



 | `False` |

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">281</span>
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
<span class="normal">324</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_existing</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">assistant_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">thread_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">run_retrieve_sleep_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"OpenAIAssistantAgent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""From existing assistant id.</span>

<span class="sd">    Args:</span>
<span class="sd">        assistant_id: id of assistant</span>
<span class="sd">        tools: list of BaseTools Assistant can use</span>
<span class="sd">        thread_id: thread id</span>
<span class="sd">        run_retrieve_sleep_time: run retrieve sleep time</span>
<span class="sd">        instructions_prefix: instructions prefix</span>
<span class="sd">        callback_manager: callback manager</span>
<span class="sd">        api_key: OpenAI API key</span>
<span class="sd">        verbose: verbose</span>

<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>

    <span class="c1"># initialize client</span>
    <span class="n">client</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>

    <span class="c1"># get assistant</span>
    <span class="n">assistant</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">assistants</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">assistant_id</span><span class="p">)</span>
    <span class="c1"># assistant.tools is incompatible with BaseTools so have to pass from params</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">client</span><span class="p">,</span>
        <span class="n">assistant</span><span class="p">,</span>
        <span class="n">tools</span><span class="o">=</span><span class="n">tools</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">thread_id</span><span class="o">=</span><span class="n">thread_id</span><span class="p">,</span>
        <span class="n">instructions_prefix</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
        <span class="n">run_retrieve_sleep_time</span><span class="o">=</span><span class="n">run_retrieve_sleep_time</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### reset [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.reset "Permanent link")

```
reset() -> None
```

Delete and create a new thread.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete and create a new thread."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">)</span>
    <span class="n">thread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">create</span><span class="p">()</span>
    <span class="n">thread_id</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span> <span class="o">=</span> <span class="n">thread_id</span>
</code></pre></div></td></tr></tbody></table>

### get\_tools [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.get_tools "Permanent link")

```
get_tools(message: str) -> List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]
```

Get tools.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get tools."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span>
</code></pre></div></td></tr></tbody></table>

### upload\_files [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.upload_files "Permanent link")

```
upload_files(files: List[str]) -> Dict[str, Any]
```

Upload files.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upload_files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">files</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Upload files."""</span>
    <span class="k">return</span> <span class="n">_process_files</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">,</span> <span class="n">files</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.add_message "Permanent link")

```
add_message(message: str, file_ids: Optional[List[str]] = None) -> Any
```

Add message to assistant.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add message to assistant."""</span>
    <span class="n">attachments</span> <span class="o">=</span> <span class="n">format_attachments</span><span class="p">(</span><span class="n">file_ids</span><span class="o">=</span><span class="n">file_ids</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">messages</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
        <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
        <span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span>
        <span class="n">content</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
        <span class="n">attachments</span><span class="o">=</span><span class="n">attachments</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run\_assistant [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.run_assistant "Permanent link")

```
run_assistant(instructions_prefix: Optional[str] = None) -> Tuple[Any, Dict]
```

Run assistant.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">424</span>
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
<span class="normal">452</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run_assistant</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run assistant."""</span>
    <span class="n">instructions_prefix</span> <span class="o">=</span> <span class="n">instructions_prefix</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span>
    <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
        <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
        <span class="n">assistant_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">instructions</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="kn">from</span> <span class="nn">openai.types.beta.threads</span> <span class="kn">import</span> <span class="n">Run</span>

    <span class="n">run</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Run</span><span class="p">,</span> <span class="n">run</span><span class="p">)</span>

    <span class="n">sources</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"queued"</span><span class="p">,</span> <span class="s2">"in_progress"</span><span class="p">,</span> <span class="s2">"requires_action"</span><span class="p">]:</span>
        <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="o"></span> <span class="s2">"failed"</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Run failed with status </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">status</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">last_error</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">run</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### arun\_assistant `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/#llama_index.agent.openai.OpenAIAssistantAgent.arun_assistant "Permanent link")

```
arun_assistant(instructions_prefix: Optional[str] = None) -> Tuple[Any, Dict]
```

Run assistant.

Source code in `llama-index-integrations/agent/llama-index-agent-openai/llama_index/agent/openai/openai_assistant_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">454</span>
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
<span class="normal">483</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">arun_assistant</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">instructions_prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run assistant."""</span>
    <span class="n">instructions_prefix</span> <span class="o">=</span> <span class="n">instructions_prefix</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instructions_prefix</span>
    <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
        <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span>
        <span class="n">assistant_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_assistant</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">instructions</span><span class="o">=</span><span class="n">instructions_prefix</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="kn">from</span> <span class="nn">openai.types.beta.threads</span> <span class="kn">import</span> <span class="n">Run</span>

    <span class="n">run</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Run</span><span class="p">,</span> <span class="n">run</span><span class="p">)</span>

    <span class="n">sources</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">while</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"queued"</span><span class="p">,</span> <span class="s2">"in_progress"</span><span class="p">,</span> <span class="s2">"requires_action"</span><span class="p">]:</span>
        <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">beta</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">runs</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
            <span class="n">thread_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_thread_id</span><span class="p">,</span> <span class="n">run_id</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">id</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">run</span><span class="o">.</span><span class="n">status</span> <span class="o"></span> <span class="s2">"failed"</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Run failed with status </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">status</span><span class="si">}</span><span class="s2">.</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"Error: </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">last_error</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">run</span><span class="p">,</span> <span class="p">{</span><span class="s2">"sources"</span><span class="p">:</span> <span class="n">sources</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/)[Next Openai legacy](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/)
