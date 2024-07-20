Title: Openai legacy - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/

Markdown Content:
Openai legacy - LlamaIndex


ContextRetrieverOpenAIAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseOpenAIAgent`

ContextRetriever OpenAI Agent.

This agent performs retrieval from BaseRetriever before calling the LLM. Allows it to augment user message with context.

NOTE: this is a beta feature, function interfaces might change.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tools` | `List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]` | 
A list of tools.



 | _required_ |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 

A retriever.



 | _required_ |
| `qa_prompt` | `Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate")]` | 

A QA prompt.



 | _required_ |
| `context_separator` | `str` | 

A context separator.



 | _required_ |
| `llm` | `Optional[[OpenAI](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai/#llama_index.llms.openai.OpenAI "llama_index.llms.openai.OpenAI")]` | 

An OpenAI LLM.



 | _required_ |
| `chat_history` | `Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]]` | 

A chat history.



 | _required_ |
| `prefix_messages` | `List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 

List\[ChatMessage\]: A list of prefix messages.



 | _required_ |
| `verbose` | `bool` | 

Whether to print debug statements.



 | `False` |
| `max_function_calls` | `int` | 

Maximum number of function calls.



 | `DEFAULT_MAX_FUNCTION_CALLS` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/context_retriever_agent.py`

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
<span class="normal">199</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ContextRetrieverOpenAIAgent</span><span class="p">(</span><span class="n">BaseOpenAIAgent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ContextRetriever OpenAI Agent.</span>

<span class="sd">    This agent performs retrieval from BaseRetriever before</span>
<span class="sd">    calling the LLM. Allows it to augment user message with context.</span>

<span class="sd">    NOTE: this is a beta feature, function interfaces might change.</span>

<span class="sd">    Args:</span>
<span class="sd">        tools (List[BaseTool]): A list of tools.</span>
<span class="sd">        retriever (BaseRetriever): A retriever.</span>
<span class="sd">        qa_prompt (Optional[PromptTemplate]): A QA prompt.</span>
<span class="sd">        context_separator (str): A context separator.</span>
<span class="sd">        llm (Optional[OpenAI]): An OpenAI LLM.</span>
<span class="sd">        chat_history (Optional[List[ChatMessage]]): A chat history.</span>
<span class="sd">        prefix_messages: List[ChatMessage]: A list of prefix messages.</span>
<span class="sd">        verbose (bool): Whether to print debug statements.</span>
<span class="sd">        max_function_calls (int): Maximum number of function calls.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">qa_prompt</span><span class="p">:</span> <span class="n">PromptTemplate</span><span class="p">,</span>
        <span class="n">context_separator</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">OpenAI</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span> <span class="o">=</span> <span class="n">tools</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_qa_prompt</span> <span class="o">=</span> <span class="n">qa_prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span> <span class="o">=</span> <span class="n">retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_context_separator</span> <span class="o">=</span> <span class="n">context_separator</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_tools_and_retriever</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
        <span class="n">qa_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ContextRetrieverOpenAIAgent"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a ContextRetrieverOpenAIAgent from a retriever.</span>

<span class="sd">        Args:</span>
<span class="sd">            retriever (BaseRetriever): A retriever.</span>
<span class="sd">            qa_prompt (Optional[PromptTemplate]): A QA prompt.</span>
<span class="sd">            context_separator (str): A context separator.</span>
<span class="sd">            llm (Optional[OpenAI]): An OpenAI LLM.</span>
<span class="sd">            chat_history (Optional[ChatMessageHistory]): A chat history.</span>
<span class="sd">            verbose (bool): Whether to print debug statements.</span>
<span class="sd">            max_function_calls (int): Maximum number of function calls.</span>
<span class="sd">            callback_manager (Optional[CallbackManager]): A callback manager.</span>

<span class="sd">        """</span>
        <span class="n">qa_prompt</span> <span class="o">=</span> <span class="n">qa_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_QA_PROMPT</span>
        <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">OpenAI</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"llm must be a OpenAI instance"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

        <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">is_function_calling_model</span><span class="p">(</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Model name </span><span class="si">{</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="si">}</span><span class="s2"> does not support function calling API."</span>
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
            <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">qa_prompt</span><span class="o">=</span><span class="n">qa_prompt</span><span class="p">,</span>
            <span class="n">context_separator</span><span class="o">=</span><span class="n">context_separator</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
            <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
            <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
            <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tools</span>

    <span class="k">def</span> <span class="nf">_build_formatted_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># augment user message</span>
        <span class="n">retrieved_nodes_w_scores</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
            <span class="n">message</span>
        <span class="p">)</span>
        <span class="n">retrieved_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">retrieved_nodes_w_scores</span><span class="p">]</span>
        <span class="n">retrieved_texts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">retrieved_nodes</span><span class="p">]</span>

        <span class="c1"># format message</span>
        <span class="n">context_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_separator</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">retrieved_texts</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_qa_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">context_str</span><span class="o">=</span><span class="n">context_str</span><span class="p">,</span> <span class="n">query_str</span><span class="o">=</span><span class="n">message</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Chat."""</span>
        <span class="n">formatted_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_formatted_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="n">formatted_message</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
            <span class="n">formatted_message</span><span class="p">,</span> <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">tool_choice</span><span class="o">=</span><span class="n">tool_choice</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Chat."""</span>
        <span class="n">formatted_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_formatted_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="n">formatted_message</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

        <span class="k">return</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span>
            <span class="n">formatted_message</span><span class="p">,</span> <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">tool_choice</span><span class="o">=</span><span class="n">tool_choice</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get tools."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_tools\_and\_retriever `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent.from_tools_and_retriever "Permanent link")

```
from_tools_and_retriever(tools: List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")], retriever: [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever"), qa_prompt: Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate")] = None, context_separator: str = '\n', llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, memory: Optional[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = None, memory_cls: Type[[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.BaseMemory")] = ChatMemoryBuffer, verbose: bool = False, max_function_calls: int = DEFAULT_MAX_FUNCTION_CALLS, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")] = None, system_prompt: Optional[str] = None, prefix_messages: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None) -> [ContextRetrieverOpenAIAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent "llama_index.agent.openai_legacy.context_retriever_agent.ContextRetrieverOpenAIAgent")
```

Create a ContextRetrieverOpenAIAgent from a retriever.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `retriever` | `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")` | 
A retriever.



 | _required_ |
| `qa_prompt` | `Optional[[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate")]` | 

A QA prompt.



 | `None` |
| `context_separator` | `str` | 

A context separator.



 | `'\n'` |
| `llm` | `Optional[[OpenAI](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai/#llama_index.llms.openai.OpenAI "llama_index.llms.openai.OpenAI")]` | 

An OpenAI LLM.



 | `None` |
| `chat_history` | `Optional[ChatMessageHistory]` | 

A chat history.



 | `None` |
| `verbose` | `bool` | 

Whether to print debug statements.



 | `False` |
| `max_function_calls` | `int` | 

Maximum number of function calls.



 | `DEFAULT_MAX_FUNCTION_CALLS` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

A callback manager.



 | `None` |

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/context_retriever_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 85</span>
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
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_tools_and_retriever</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">tools</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
    <span class="n">retriever</span><span class="p">:</span> <span class="n">BaseRetriever</span><span class="p">,</span>
    <span class="n">qa_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">context_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">memory_cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseMemory</span><span class="p">]</span> <span class="o">=</span> <span class="n">ChatMemoryBuffer</span><span class="p">,</span>
    <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">max_function_calls</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_FUNCTION_CALLS</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prefix_messages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ContextRetrieverOpenAIAgent"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a ContextRetrieverOpenAIAgent from a retriever.</span>

<span class="sd">    Args:</span>
<span class="sd">        retriever (BaseRetriever): A retriever.</span>
<span class="sd">        qa_prompt (Optional[PromptTemplate]): A QA prompt.</span>
<span class="sd">        context_separator (str): A context separator.</span>
<span class="sd">        llm (Optional[OpenAI]): An OpenAI LLM.</span>
<span class="sd">        chat_history (Optional[ChatMessageHistory]): A chat history.</span>
<span class="sd">        verbose (bool): Whether to print debug statements.</span>
<span class="sd">        max_function_calls (int): Maximum number of function calls.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): A callback manager.</span>

<span class="sd">    """</span>
    <span class="n">qa_prompt</span> <span class="o">=</span> <span class="n">qa_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_QA_PROMPT</span>
    <span class="n">chat_history</span> <span class="o">=</span> <span class="n">chat_history</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">llm</span><span class="p">,</span> <span class="n">OpenAI</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"llm must be a OpenAI instance"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">callback_manager</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">llm</span><span class="o">.</span><span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span>

    <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">memory_cls</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">is_function_calling_model</span><span class="p">(</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Model name </span><span class="si">{</span><span class="n">llm</span><span class="o">.</span><span class="n">model</span><span class="si">}</span><span class="s2"> does not support function calling API."</span>
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
        <span class="n">retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span>
        <span class="n">qa_prompt</span><span class="o">=</span><span class="n">qa_prompt</span><span class="p">,</span>
        <span class="n">context_separator</span><span class="o">=</span><span class="n">context_separator</span><span class="p">,</span>
        <span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">,</span>
        <span class="n">memory</span><span class="o">=</span><span class="n">memory</span><span class="p">,</span>
        <span class="n">prefix_messages</span><span class="o">=</span><span class="n">prefix_messages</span><span class="p">,</span>
        <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="n">max_function_calls</span><span class="o">=</span><span class="n">max_function_calls</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### chat [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent.chat "Permanent link")

```
chat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, tool_choice: Union[str, dict] = 'auto') -> [AgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse "llama_index.core.chat_engine.types.AgentChatResponse")
```

Chat.

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/context_retriever_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">167</span>
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
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Chat."""</span>
    <span class="n">formatted_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_formatted_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="n">print_text</span><span class="p">(</span><span class="n">formatted_message</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

    <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
        <span class="n">formatted_message</span><span class="p">,</span> <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">tool_choice</span><span class="o">=</span><span class="n">tool_choice</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### achat `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent.achat "Permanent link")

```
achat(message: str, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, tool_choice: Union[str, dict] = 'auto') -> [AgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse "llama_index.core.chat_engine.types.AgentChatResponse")
```

Chat.

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/context_retriever_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">182</span>
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
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">tool_choice</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Chat."""</span>
    <span class="n">formatted_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_formatted_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
        <span class="n">print_text</span><span class="p">(</span><span class="n">formatted_message</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"yellow"</span><span class="p">)</span>

    <span class="k">return</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">achat</span><span class="p">(</span>
        <span class="n">formatted_message</span><span class="p">,</span> <span class="n">chat_history</span><span class="o">=</span><span class="n">chat_history</span><span class="p">,</span> <span class="n">tool_choice</span><span class="o">=</span><span class="n">tool_choice</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_tools [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.ContextRetrieverOpenAIAgent.get_tools "Permanent link")

```
get_tools(message: str) -> List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.BaseTool")]
```

Get tools.

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/context_retriever_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_tools</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get tools."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tools</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

FnRetrieverOpenAIAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/#llama_index.agent.openai_legacy.FnRetrieverOpenAIAgent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `OpenAIAgent`

Function Retriever OpenAI Agent.

Uses our object retriever module to retrieve openai agent.

NOTE: This is deprecated, you can just use the base `OpenAIAgent` class by specifying the following:

```
agent = OpenAIAgent.from_tools(tool_retriever=retriever, ...)
```

Source code in `llama-index-integrations/agent/llama-index-agent-openai-legacy/llama_index/agent/openai_legacy/retriever_openai_agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FnRetrieverOpenAIAgent</span><span class="p">(</span><span class="n">OpenAIAgent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Function Retriever OpenAI Agent.</span>

<span class="sd">    Uses our object retriever module to retrieve openai agent.</span>

<span class="sd">    NOTE: This is deprecated, you can just use the base `OpenAIAgent` class by</span>
<span class="sd">    specifying the following:</span>
<span class="sd">    ```</span>
<span class="sd">    agent = OpenAIAgent.from_tools(tool_retriever=retriever, ...)</span>
<span class="sd">    ```</span>

<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_retriever</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">retriever</span><span class="p">:</span> <span class="n">ObjectRetriever</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"FnRetrieverOpenAIAgent"</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span>
            <span class="n">FnRetrieverOpenAIAgent</span><span class="p">,</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tools</span><span class="p">(</span><span class="n">tool_retriever</span><span class="o">=</span><span class="n">retriever</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openai](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/)[Next React](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/)
