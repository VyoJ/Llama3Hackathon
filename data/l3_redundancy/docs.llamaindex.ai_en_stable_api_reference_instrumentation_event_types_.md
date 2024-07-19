Title: Event types - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/

Markdown Content:
Event types - LlamaIndex


BaseEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Source code in `llama-index-core/llama_index/core/instrumentation/events/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
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
<span class="normal">26</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseEvent</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">())</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="n">uuid4</span><span class="p">())</span>
    <span class="n">span_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">active_span_id</span><span class="o">.</span><span class="n">get</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Return class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseEvent"</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="n">copy_on_model_validation</span> <span class="o">=</span> <span class="s2">"deep"</span>

    <span class="k">def</span> <span class="nf">dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">data</span><span class="p">[</span><span class="s2">"class_name"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">data</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent.class_name "Permanent link")

```
class_name()
```

Return class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Return class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseEvent"</span>
</code></pre></div></td></tr></tbody></table>

AgentChatWithStepEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepEndEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

AgentChatWithStepEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `response` | `Optional[AGENT_CHAT_RESPONSE_TYPE]` | 
Agent chat response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 63</span>
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
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentChatWithStepEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentChatWithStepEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        response (Optional[AGENT_CHAT_RESPONSE_TYPE]): Agent chat response.</span>
<span class="sd">    """</span>

    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AGENT_CHAT_RESPONSE_TYPE</span><span class="p">]</span>

    <span class="nd">@root_validator</span><span class="p">(</span><span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_response</span><span class="p">(</span><span class="bp">cls</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">values</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate response."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">values</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"response"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">StreamingAgentChatResponse</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"response must be of type AgentChatResponse or StreamingAgentChatResponse"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">values</span>

    <span class="nd">@validator</span><span class="p">(</span><span class="s2">"response"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">validate_response_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate response type."""</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">StreamingAgentChatResponse</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"response must be of type AgentChatResponse or StreamingAgentChatResponse"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"AgentChatWithStepEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### validate\_response [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepEndEvent.validate_response "Permanent link")

```
validate_response(values: Any) -> Any
```

Validate response.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">72</span>
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
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@root_validator</span><span class="p">(</span><span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_response</span><span class="p">(</span><span class="bp">cls</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">values</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate response."""</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">values</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"response"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
        <span class="n">response</span><span class="p">,</span> <span class="n">StreamingAgentChatResponse</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"response must be of type AgentChatResponse or StreamingAgentChatResponse"</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">values</span>
</code></pre></div></td></tr></tbody></table>

### validate\_response\_type [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepEndEvent.validate_response_type "Permanent link")

```
validate_response_type(response: Any) -> Any
```

Validate response type.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@validator</span><span class="p">(</span><span class="s2">"response"</span><span class="p">,</span> <span class="n">pre</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">validate_response_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate response type."""</span>
    <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">response</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">AgentChatResponse</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span>
        <span class="n">response</span><span class="p">,</span> <span class="n">StreamingAgentChatResponse</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"response must be of type AgentChatResponse or StreamingAgentChatResponse"</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"AgentChatWithStepEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

AgentChatWithStepStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepStartEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

AgentChatWithStepStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `user_msg` | `str` | 
User input message.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">48</span>
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
<span class="normal">60</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentChatWithStepStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentChatWithStepStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        user_msg (str): User input message.</span>
<span class="sd">    """</span>

    <span class="n">user_msg</span><span class="p">:</span> <span class="nb">str</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"AgentChatWithStepStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentChatWithStepStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"AgentChatWithStepStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

AgentRunStepEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentRunStepEndEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

AgentRunStepEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `step_output` | `[TaskStepOutput](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStepOutput "llama_index.core.base.agent.types.TaskStepOutput")` | 
Task step output.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentRunStepEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentRunStepEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        step_output (TaskStepOutput): Task step output.</span>
<span class="sd">    """</span>

    <span class="n">step_output</span><span class="p">:</span> <span class="n">TaskStepOutput</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"AgentRunStepEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentRunStepEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"AgentRunStepEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

AgentRunStepStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentRunStepStartEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

AgentRunStepStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `task_id` | `str` | 
Task ID.



 | _required_ |
| `step` | `Optional[[TaskStep](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.TaskStep "llama_index.core.base.agent.types.TaskStep")]` | 

Task step.



 | _required_ |
| `input` | `Optional[str]` | 

Optional input.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">30</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentRunStepStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentRunStepStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        task_id (str): Task ID.</span>
<span class="sd">        step (Optional[TaskStep]): Task step.</span>
<span class="sd">        input (Optional[str]): Optional input.</span>
<span class="sd">    """</span>

    <span class="n">task_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">step</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TaskStep</span><span class="p">]</span>
    <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"AgentRunStepStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentRunStepStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"AgentRunStepStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

AgentToolCallEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentToolCallEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

AgentToolCallEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `arguments` | `str` | 
Arguments.



 | _required_ |
| `tool` | `[ToolMetadata](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.ToolMetadata "llama_index.core.tools.types.ToolMetadata")` | 

Tool metadata.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
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
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AgentToolCallEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""AgentToolCallEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        arguments (str): Arguments.</span>
<span class="sd">        tool (ToolMetadata): Tool metadata.</span>
<span class="sd">    """</span>

    <span class="n">arguments</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">tool</span><span class="p">:</span> <span class="n">ToolMetadata</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"AgentToolCallEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.agent.AgentToolCallEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/agent.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"AgentToolCallEvent"</span>
</code></pre></div></td></tr></tbody></table>

StreamChatDeltaReceivedEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatDeltaReceivedEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

StreamChatDeltaReceivedEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `delta` | `str` | 
Delta received from the stream chat.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StreamChatDeltaReceivedEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""StreamChatDeltaReceivedEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        delta (str): Delta received from the stream chat.</span>
<span class="sd">    """</span>

    <span class="n">delta</span><span class="p">:</span> <span class="nb">str</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"StreamChatDeltaReceivedEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatDeltaReceivedEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"StreamChatDeltaReceivedEvent"</span>
</code></pre></div></td></tr></tbody></table>

StreamChatEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatEndEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

StreamChatEndEvent.

Fired at the end of writing to the stream chat-engine queue.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StreamChatEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""StreamChatEndEvent.</span>

<span class="sd">    Fired at the end of writing to the stream chat-engine queue.</span>
<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"StreamChatEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"StreamChatEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

StreamChatErrorEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatErrorEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

StreamChatErrorEvent.

Fired when an exception is raised during the stream chat-engine operation.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `exception` | `Exception` | 
Exception raised during the stream chat operation.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StreamChatErrorEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""StreamChatErrorEvent.</span>

<span class="sd">    Fired when an exception is raised during the stream chat-engine operation.</span>

<span class="sd">    Args:</span>
<span class="sd">        exception (Exception): Exception raised during the stream chat operation.</span>
<span class="sd">    """</span>

    <span class="n">exception</span><span class="p">:</span> <span class="ne">Exception</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"StreamChatErrorEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatErrorEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"StreamChatErrorEvent"</span>
</code></pre></div></td></tr></tbody></table>

StreamChatStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatStartEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

StreamChatStartEvent.

Fired at the start of writing to the stream chat-engine queue.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 4</span>
<span class="normal"> 5</span>
<span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StreamChatStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""StreamChatStartEvent.</span>

<span class="sd">    Fired at the start of writing to the stream chat-engine queue.</span>
<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"StreamChatStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.chat_engine.StreamChatStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/chat_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"StreamChatStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

EmbeddingEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.embedding.EmbeddingEndEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

EmbeddingEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `chunks` | `List[str]` | 
List of chunks.



 | _required_ |
| `embeddings` | `List[List[float]]` | 

List of embeddings.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/embedding.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EmbeddingEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""EmbeddingEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        chunks (List[str]): List of chunks.</span>
<span class="sd">        embeddings (List[List[float]]): List of embeddings.</span>

<span class="sd">    """</span>

    <span class="n">chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"EmbeddingEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.embedding.EmbeddingEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/embedding.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"EmbeddingEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

EmbeddingStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.embedding.EmbeddingStartEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

EmbeddingStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model_dict` | `dict` | 
Model dictionary containing details about the embedding model.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/embedding.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EmbeddingStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""EmbeddingStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        model_dict (dict): Model dictionary containing details about the embedding model.</span>
<span class="sd">    """</span>

    <span class="n">model_dict</span><span class="p">:</span> <span class="nb">dict</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"EmbeddingStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.embedding.EmbeddingStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/embedding.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"EmbeddingStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMChatEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMChatEndEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMChatEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
List of chat messages.



 | _required_ |
| `response` | `Optional[ChatResponse]` | 

Last chat response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">169</span>
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
<span class="normal">183</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMChatEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMChatEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        messages (List[ChatMessage]): List of chat messages.</span>
<span class="sd">        response (Optional[ChatResponse]): Last chat response.</span>
<span class="sd">    """</span>

    <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatResponse</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMChatEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMChatEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMChatEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMChatStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMChatStartEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMChatStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
List of chat messages.



 | _required_ |
| `additional_kwargs` | `dict` | 

Additional keyword arguments.



 | _required_ |
| `model_dict` | `dict` | 

Model dictionary.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
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
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMChatStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMChatStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        messages (List[ChatMessage]): List of chat messages.</span>
<span class="sd">        additional_kwargs (dict): Additional keyword arguments.</span>
<span class="sd">        model_dict (dict): Model dictionary.</span>
<span class="sd">    """</span>

    <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="n">model_dict</span><span class="p">:</span> <span class="nb">dict</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMChatStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMChatStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMChatStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMCompletionEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMCompletionEndEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMCompletionEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
The prompt to be completed.



 | _required_ |
| `response` | `CompletionResponse` | 

Completion response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">116</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMCompletionEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMCompletionEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        prompt (str): The prompt to be completed.</span>
<span class="sd">        response (CompletionResponse): Completion response.</span>
<span class="sd">    """</span>

    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">CompletionResponse</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMCompletionEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMCompletionEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMCompletionEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMCompletionStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMCompletionStartEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMCompletionStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
The prompt to be completed.



 | _required_ |
| `additional_kwargs` | `dict` | 

Additional keyword arguments.



 | _required_ |
| `model_dict` | `dict` | 

Model dictionary.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">80</span>
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
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMCompletionStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMCompletionStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        prompt (str): The prompt to be completed.</span>
<span class="sd">        additional_kwargs (dict): Additional keyword arguments.</span>
<span class="sd">        model_dict (dict): Model dictionary.</span>
<span class="sd">    """</span>

    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="n">model_dict</span><span class="p">:</span> <span class="nb">dict</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMCompletionStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMCompletionStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMCompletionStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMPredictEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMPredictEndEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMPredictEndEvent.

The result of an llm.predict() call.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `output` | `str` | 
Output.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMPredictEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMPredictEndEvent.</span>

<span class="sd">    The result of an llm.predict() call.</span>

<span class="sd">    Args:</span>
<span class="sd">        output (str): Output.</span>
<span class="sd">    """</span>

    <span class="n">output</span><span class="p">:</span> <span class="nb">str</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMPredictEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMPredictEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMPredictEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

LLMPredictStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMPredictStartEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

LLMPredictStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `template` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 
Prompt template.



 | _required_ |
| `template_args` | `Optional[dict]` | 

Prompt template arguments.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

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
<span class="normal">26</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LLMPredictStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""LLMPredictStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        template (BasePromptTemplate): Prompt template.</span>
<span class="sd">        template_args (Optional[dict]): Prompt template arguments.</span>
<span class="sd">    """</span>

    <span class="n">template</span><span class="p">:</span> <span class="n">BasePromptTemplate</span>
    <span class="n">template_args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"LLMPredictStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.llm.LLMPredictStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/llm.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"LLMPredictStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

QueryEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.query.QueryEndEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

QueryEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `QueryType` | 
Query as a string or query bundle.



 | _required_ |
| `response` | `RESPONSE_TYPE` | 

Response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""QueryEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (QueryType): Query as a string or query bundle.</span>
<span class="sd">        response (RESPONSE_TYPE): Response.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TYPE</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"QueryEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.query.QueryEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"QueryEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

QueryStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.query.QueryStartEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

QueryStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `QueryType` | 
Query as a string or query bundle.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""QueryStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (QueryType): Query as a string or query bundle.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">QueryType</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"QueryStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.query.QueryStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/query.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"QueryStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

RetrievalEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.retrieval.RetrievalEndEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

RetrievalEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `str_or_query_bundle` | `QueryType` | 
Query bundle.



 | _required_ |
| `nodes` | `List[[NodeWithScore](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.NodeWithScore "llama_index.core.schema.NodeWithScore")]` | 

List of nodes with scores.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/retrieval.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrievalEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RetrievalEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        str_or_query_bundle (QueryType): Query bundle.</span>
<span class="sd">        nodes (List[NodeWithScore]): List of nodes with scores.</span>
<span class="sd">    """</span>

    <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"RetrievalEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.retrieval.RetrievalEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/retrieval.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"RetrievalEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

RetrievalStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.retrieval.RetrievalStartEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

RetrievalStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `str_or_query_bundle` | `QueryType` | 
Query bundle.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/retrieval.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrievalStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RetrievalStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        str_or_query_bundle (QueryType): Query bundle.</span>
<span class="sd">    """</span>

    <span class="n">str_or_query_bundle</span><span class="p">:</span> <span class="n">QueryType</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"RetrievalStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.retrieval.RetrievalStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/retrieval.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"RetrievalStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

GetResponseEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.GetResponseEndEvent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

GetResponseEndEvent.

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GetResponseEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GetResponseEndEvent."""</span>

    <span class="c1"># TODO: consumes the first chunk of generators??</span>
    <span class="c1"># response: RESPONSE_TEXT_TYPE</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"GetResponseEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.GetResponseEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"GetResponseEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

GetResponseStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.GetResponseStartEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

GetResponseStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_str` | `str` | 
Query string.



 | _required_ |
| `text_chunks` | `List[str]` | 

List of text chunks.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

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
<span class="normal">53</span>
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GetResponseStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GetResponseStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_str (str): Query string.</span>
<span class="sd">        text_chunks (List[str]): List of text chunks.</span>
<span class="sd">    """</span>

    <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">text_chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"GetResponseStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.GetResponseStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"GetResponseStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

SynthesizeEndEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.SynthesizeEndEvent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

SynthesizeEndEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `QueryType` | 
Query as a string or query bundle.



 | _required_ |
| `response` | `RESPONSE_TYPE` | 

Response.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SynthesizeEndEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SynthesizeEndEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (QueryType): Query as a string or query bundle.</span>
<span class="sd">        response (RESPONSE_TYPE): Response.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">QueryType</span>
    <span class="n">response</span><span class="p">:</span> <span class="n">RESPONSE_TYPE</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"SynthesizeEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.SynthesizeEndEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"SynthesizeEndEvent"</span>
</code></pre></div></td></tr></tbody></table>

SynthesizeStartEvent [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.SynthesizeStartEvent "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent")`

SynthesizeStartEvent.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `QueryType` | 
Query as a string or query bundle.



 | _required_ |

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SynthesizeStartEvent</span><span class="p">(</span><span class="n">BaseEvent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SynthesizeStartEvent.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (QueryType): Query as a string or query bundle.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">QueryType</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"SynthesizeStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.synthesis.SynthesizeStartEvent.class_name "Permanent link")

```
class_name()
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/events/synthesis.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"SynthesizeStartEvent"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Event handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/)[Next Instrumentation](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)
