Title: Honeyhive - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/

Markdown Content:
Honeyhive - LlamaIndex


honeyhive\_callback\_handler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/#llama_index.callbacks.honeyhive.honeyhive_callback_handler "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
honeyhive_callback_handler(**kwargs: Any) -> [BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")
```

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-honeyhive/llama_index/callbacks/honeyhive/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">8</span>
<span class="normal">9</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">honeyhive_callback_handler</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseCallbackHandler</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">HoneyHiveLlamaIndexTracer</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Deepeval](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/)[Next Core Callback Classes](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/)
