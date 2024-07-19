Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/memory/

Markdown Content:
Index - LlamaIndex


BaseMemory [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`

Base class for all memory types.

NOTE: The interface for memory is not yet finalized and is subject to change.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
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
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseMemory</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base class for all memory types.</span>

<span class="sd">    NOTE: The interface for memory is not yet finalized and is subject to change.</span>
<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseMemory"</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseMemory"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a chat memory from defaults."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get chat history."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all chat history."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put chat history."""</span>

    <span class="k">def</span> <span class="nf">put_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put chat history."""</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set chat history."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset chat history."""</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseMemory"</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `abstractmethod` `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.from_defaults "Permanent link")

```
from_defaults(chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None) -> [BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")
```

Create a chat memory from defaults.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseMemory"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a chat memory from defaults."""</span>
</code></pre></div></td></tr></tbody></table>

### get `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.get "Permanent link")

```
get(input: Optional[str] = None, **kwargs: Any) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get chat history."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_all `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.get_all "Permanent link")

```
get_all() -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get all chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all chat history."""</span>
</code></pre></div></td></tr></tbody></table>

### put `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.put "Permanent link")

```
put(message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")) -> None
```

Put chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put chat history."""</span>
</code></pre></div></td></tr></tbody></table>

### put\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.put_messages "Permanent link")

```
put_messages(messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]) -> None
```

Put chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put chat history."""</span>
    <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.set "Permanent link")

```
set(messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]) -> None
```

Set chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set chat history."""</span>
</code></pre></div></td></tr></tbody></table>

### reset `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory.reset "Permanent link")

```
reset() -> None
```

Reset chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset chat history."""</span>
</code></pre></div></td></tr></tbody></table>

BaseChatStoreMemory [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseMemory "llama_index.core.memory.types.BaseMemory")`

Base class for any .

NOTE: The interface for memory is not yet finalized and is subject to change.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
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
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseChatStoreMemory</span><span class="p">(</span><span class="n">BaseMemory</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base class for any .</span>

<span class="sd">    NOTE: The interface for memory is not yet finalized and is subject to change.</span>
<span class="sd">    """</span>

    <span class="n">chat_store</span><span class="p">:</span> <span class="n">BaseChatStore</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">SimpleChatStore</span><span class="p">)</span>
    <span class="n">chat_store_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHAT_STORE_KEY</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseChatStoreMemory"</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseChatStoreMemory"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a chat memory from defaults."""</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all chat history."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put chat history."""</span>
        <span class="c1"># ensure everything is serialized</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">add_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Reset chat history."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseChatStoreMemory"</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `abstractmethod` `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.from_defaults "Permanent link")

```
from_defaults(chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, llm: Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")] = None) -> [BaseChatStoreMemory](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory "llama_index.core.memory.types.BaseChatStoreMemory")
```

Create a chat memory from defaults.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseChatStoreMemory"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a chat memory from defaults."""</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.get_all "Permanent link")

```
get_all() -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]
```

Get all chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all chat history."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.put "Permanent link")

```
put(message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")) -> None
```

Put chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put chat history."""</span>
    <span class="c1"># ensure everything is serialized</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">add_message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### set [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.set "Permanent link")

```
set(messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]) -> None
```

Set chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### reset [#](https://docs.llamaindex.ai/en/stable/api_reference/memory/#llama_index.core.memory.types.BaseChatStoreMemory.reset "Permanent link")

```
reset() -> None
```

Reset chat history.

Source code in `llama-index-core/llama_index/core/memory/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Reset chat history."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">chat_store</span><span class="o">.</span><span class="n">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">chat_store_key</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chat memory buffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/)[Next Simple composable memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/)
