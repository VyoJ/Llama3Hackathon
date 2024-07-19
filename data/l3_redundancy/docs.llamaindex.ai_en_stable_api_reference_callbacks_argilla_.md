Title: Argilla - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/

Markdown Content:
Argilla - LlamaIndex


argilla\_callback\_handler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/#llama_index.callbacks.argilla.argilla_callback_handler "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
argilla_callback_handler(**kwargs: Any) -> [BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")
```

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-argilla/llama_index/callbacks/argilla/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">argilla_callback_handler</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseCallbackHandler</span><span class="p">:</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="c1"># lazy import</span>
        <span class="kn">from</span> <span class="nn">argilla_llama_index</span> <span class="kn">import</span> <span class="n">ArgillaCallbackHandler</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install Argilla with `pip install argilla`"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">ArgillaCallbackHandler</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Aim](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/)[Next Arize phoenix](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/)
