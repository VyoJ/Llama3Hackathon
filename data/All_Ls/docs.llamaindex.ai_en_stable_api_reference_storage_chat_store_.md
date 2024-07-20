Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/

Markdown Content:
Index - LlamaIndex


Base interface class for storing chat history per user.

BaseChatStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

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
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseChatStore</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">):</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseChatStore"</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set messages for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get messages for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add a message for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Delete messages for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Delete specific message for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Delete last message for a key."""</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all keys."""</span>
        <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseChatStore"</span>
</code></pre></div></td></tr></tbody></table>

### set\_messages `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.set_messages "Permanent link")

```
set_messages(key: str, messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]) -> None
```

Set messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set messages for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### get\_messages `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.get_messages "Permanent link")

```
get_messages(key: str) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Get messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get messages for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### add\_message `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.add_message "Permanent link")

```
add_message(key: str, message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")) -> None
```

Add a message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add a message for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### delete\_messages `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.delete_messages "Permanent link")

```
delete_messages(key: str) -> Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]]
```

Delete messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Delete messages for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### delete\_message `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.delete_message "Permanent link")

```
delete_message(key: str, idx: int) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete specific message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete specific message for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### delete\_last\_message `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.delete_last_message "Permanent link")

```
delete_last_message(key: str) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete last message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete last message for a key."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### get\_keys `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore.get_keys "Permanent link")

```
get_keys() -> List[str]
```

Get all keys.

Source code in `llama-index-core/llama_index/core/storage/chat_store/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all keys."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/)[Next Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/)
