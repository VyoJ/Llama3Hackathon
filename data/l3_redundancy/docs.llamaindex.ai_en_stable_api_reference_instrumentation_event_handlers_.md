Title: Event handlers - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/

Markdown Content:
Event handlers - LlamaIndex


BaseEventHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/#llama_index.core.instrumentation.event_handlers.base.BaseEventHandler "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base callback handler that can be used to track event starts and ends.

Source code in `llama-index-core/llama_index/core/instrumentation/event_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
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
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseEventHandler</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base callback handler that can be used to track event starts and ends."""</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseEventHandler"</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">BaseEvent</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for handling event."""</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/#llama_index.core.instrumentation.event_handlers.base.BaseEventHandler.class_name "Permanent link")

```
class_name() -> str
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/event_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseEventHandler"</span>
</code></pre></div></td></tr></tbody></table>

### handle `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/#llama_index.core.instrumentation.event_handlers.base.BaseEventHandler.handle "Permanent link")

```
handle(event: [BaseEvent](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/#llama_index.core.instrumentation.events.base.BaseEvent "llama_index.core.instrumentation.events.base.BaseEvent"), **kwargs) -> Any
```

Logic for handling event.

Source code in `llama-index-core/llama_index/core/instrumentation/event_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">BaseEvent</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for handling event."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/)[Next Event types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/)
