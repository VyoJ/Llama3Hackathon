Title: Deepeval - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/

Markdown Content:
Deepeval - LlamaIndex


deepeval\_callback\_handler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/#llama_index.callbacks.deepeval.deepeval_callback_handler "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
deepeval_callback_handler(**eval_params: Any) -> [BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")
```

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-deepeval/llama_index/callbacks/deepeval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">8</span>
<span class="normal">9</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">deepeval_callback_handler</span><span class="p">(</span><span class="o">**</span><span class="n">eval_params</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseCallbackHandler</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">LlamaIndexCallbackHandler</span><span class="p">(</span><span class="o">**</span><span class="n">eval_params</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Arize phoenix](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/)[Next Honeyhive](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/)
