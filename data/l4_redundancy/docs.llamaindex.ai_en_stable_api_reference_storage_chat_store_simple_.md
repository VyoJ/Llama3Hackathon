Title: Simple - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/

Markdown Content:
Simple - LlamaIndex


SimpleChatStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseChatStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/#llama_index.core.storage.chat_store.base.BaseChatStore "llama_index.core.storage.chat_store.base.BaseChatStore")`

Simple chat store.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleChatStore</span><span class="p">(</span><span class="n">BaseChatStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple chat store."""</span>

    <span class="n">store</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get class name."""</span>
        <span class="k">return</span> <span class="s2">"SimpleChatStore"</span>

    <span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set messages for a key."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">messages</span>

    <span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get messages for a key."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span>

    <span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add a message for a key."""</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">idx</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Delete messages for a key."""</span>
        <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Delete specific message for a key."""</span>
        <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">idx</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]):</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Delete last message for a key."""</span>
        <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all keys."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"chat_store.json"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the docstore to a file."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
        <span class="n">dirpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">persist_path</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dirpath</span><span class="p">):</span>
            <span class="n">fs</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">json</span><span class="p">()))</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"chat_store.json"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleChatStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a SimpleChatStore from a persist path."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_path</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">cls</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"r"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.class_name "Permanent link")

```
class_name() -> str
```

Get class name.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get class name."""</span>
    <span class="k">return</span> <span class="s2">"SimpleChatStore"</span>
</code></pre></div></td></tr></tbody></table>

### set\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.set_messages "Permanent link")

```
set_messages(key: str, messages: List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]) -> None
```

Set messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">set_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Set messages for a key."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">messages</span>
</code></pre></div></td></tr></tbody></table>

### get\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.get_messages "Permanent link")

```
get_messages(key: str) -> List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Get messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get messages for a key."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span>
</code></pre></div></td></tr></tbody></table>

### add\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.add_message "Permanent link")

```
add_message(key: str, message: [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage"), idx: Optional[int] = None) -> None
```

Add a message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_message</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ChatMessage</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add a message for a key."""</span>
    <span class="k">if</span> <span class="n">idx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">idx</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_messages [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.delete_messages "Permanent link")

```
delete_messages(key: str) -> Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]]
```

Delete messages for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Delete messages for a key."""</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.delete_message "Permanent link")

```
delete_message(key: str, idx: int) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete specific message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">idx</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete specific message for a key."""</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">idx</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]):</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_last\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.delete_last_message "Permanent link")

```
delete_last_message(key: str) -> Optional[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.llms.ChatMessage")]
```

Delete last message for a key.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_last_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Delete last message for a key."""</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_keys [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.get_keys "Permanent link")

```
get_keys() -> List[str]
```

Get all keys.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_keys</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all keys."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.persist "Permanent link")

```
persist(persist_path: str = 'chat_store.json', fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the docstore to a file.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
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
<span class="normal">74</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"chat_store.json"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the docstore to a file."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
    <span class="n">dirpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">persist_path</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dirpath</span><span class="p">):</span>
        <span class="n">fs</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">json</span><span class="p">()))</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_path `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore.from_persist_path "Permanent link")

```
from_persist_path(persist_path: str = 'chat_store.json', fs: Optional[AbstractFileSystem] = None) -> [SimpleChatStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/#llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore "llama_index.core.storage.chat_store.simple_chat_store.SimpleChatStore")
```

Create a SimpleChatStore from a persist path.

Source code in `llama-index-core/llama_index/core/storage/chat_store/simple_chat_store.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">76</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"chat_store.json"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleChatStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a SimpleChatStore from a persist path."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_path</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"r"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">parse_raw</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/)[Next Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/)
