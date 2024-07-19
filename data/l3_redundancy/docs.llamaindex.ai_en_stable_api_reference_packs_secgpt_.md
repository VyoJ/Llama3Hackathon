Title: Secgpt - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/

Markdown Content:
Secgpt - LlamaIndex


SecGPTPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/#llama_index.packs.secgpt.SecGPTPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

SecGPT Hub.

A central trustworthy entity that routes user queries to appropriate isolated apps.

Source code in `llama-index-packs/llama-index-packs-secgpt/llama_index/packs/secgpt/hub.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
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
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
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
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SecGPTPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SecGPT Hub.</span>

<span class="sd">    A central trustworthy entity that routes user queries to appropriate isolated apps.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tools</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseTool</span><span class="p">],</span>
        <span class="n">tool_specs</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseToolSpec</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">memory</span><span class="p">:</span> <span class="n">BaseMemory</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReActOutputParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">handle_reasoning_failure_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Callable</span><span class="p">[[</span><span class="n">CallbackManager</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">],</span> <span class="n">ToolOutput</span><span class="p">]</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"0"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the SecGPTPack.</span>

<span class="sd">        Args:</span>
<span class="sd">            tools (Sequence[BaseTool]): A sequence of available tools.</span>
<span class="sd">            tool_specs (Sequence[BaseToolSpec]): Specifications for the tools.</span>
<span class="sd">            llm (LLM, optional): Language Model used for processing. Defaults to Settings.llm.</span>
<span class="sd">            memory (BaseMemory, optional): Memory component to keep track of conversation history. Defaults to ChatMemoryBuffer.</span>
<span class="sd">            output_parser (Optional[ReActOutputParser], optional): Parser for handling the output. Defaults to None.</span>
<span class="sd">            verbose (bool, optional): Flag to enable verbose output. Defaults to False.</span>
<span class="sd">            handle_reasoning_failure_fn (Optional[Callable[[CallbackManager, Exception], ToolOutput]], optional): Callable function to handle reasoning failures. Defaults to None.</span>
<span class="sd">            user_id (Optional[str], optional): User identifier. Defaults to "0".</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">Settings</span><span class="o">.</span><span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span> <span class="ow">or</span> <span class="n">ChatMemoryBuffer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">chat_history</span><span class="o">=</span><span class="p">[],</span> <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">output_parser</span> <span class="o">=</span> <span class="n">output_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">handle_reasoning_failure_fn</span> <span class="o">=</span> <span class="n">handle_reasoning_failure_fn</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">user_id</span> <span class="o">=</span> <span class="n">user_id</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">planner</span> <span class="o">=</span> <span class="n">HubPlanner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tool_importer</span> <span class="o">=</span> <span class="n">ToolImporter</span><span class="p">(</span><span class="n">tools</span><span class="p">,</span> <span class="n">tool_specs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">hub_operator</span> <span class="o">=</span> <span class="n">HubOperator</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tool_importer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">user_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Process a user query and generate a response.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The user query to process.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The response generated by SecGPT.</span>
<span class="sd">        """</span>
        <span class="n">memory_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="p">(</span><span class="n">query</span><span class="p">)))</span>
        <span class="n">tool_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_importer</span><span class="o">.</span><span class="n">get_tool_info</span><span class="p">()</span>
        <span class="n">plan</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">planner</span><span class="o">.</span><span class="n">plan_generate</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">tool_info</span><span class="p">,</span> <span class="n">memory_content</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hub_operator</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">plan</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">CHATBOT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="p">(</span><span class="n">response</span><span class="p">)))</span>

        <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

### chat [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/#llama_index.packs.secgpt.SecGPTPack.chat "Permanent link")

```
chat(query: str) -> str
```

Process a user query and generate a response.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The user query to process.



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
The response generated by SecGPT.



 |

Source code in `llama-index-packs/llama-index-packs-secgpt/llama_index/packs/secgpt/hub.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">70</span>
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
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Process a user query and generate a response.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The user query to process.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: The response generated by SecGPT.</span>
<span class="sd">    """</span>
    <span class="n">memory_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="p">(</span><span class="n">query</span><span class="p">)))</span>
    <span class="n">tool_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tool_importer</span><span class="o">.</span><span class="n">get_tool_info</span><span class="p">()</span>
    <span class="n">plan</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">planner</span><span class="o">.</span><span class="n">plan_generate</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">tool_info</span><span class="p">,</span> <span class="n">memory_content</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hub_operator</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">plan</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">CHATBOT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="p">(</span><span class="n">response</span><span class="p">)))</span>

    <span class="k">return</span> <span class="n">response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Searchain](https://docs.llamaindex.ai/en/stable/api_reference/packs/searchain/)[Next Self discover](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/)
