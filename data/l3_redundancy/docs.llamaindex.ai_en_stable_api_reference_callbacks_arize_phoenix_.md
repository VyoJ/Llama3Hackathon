Title: Arize phoenix - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/

Markdown Content:
Arize phoenix - LlamaIndex


arize\_phoenix\_callback\_handler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/#llama_index.callbacks.arize_phoenix.arize_phoenix_callback_handler "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
arize_phoenix_callback_handler(**kwargs: Any) -> [BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")
```

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-arize-phoenix/llama_index/callbacks/arize_phoenix/base.py`

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
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">arize_phoenix_callback_handler</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseCallbackHandler</span><span class="p">:</span>
    <span class="c1"># newer versions of arize, v2.x</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">openinference.instrumentation.llama_index</span> <span class="kn">import</span> <span class="n">LlamaIndexInstrumentor</span>
        <span class="kn">from</span> <span class="nn">opentelemetry.exporter.otlp.proto.http.trace_exporter</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">OTLPSpanExporter</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">opentelemetry.sdk</span> <span class="kn">import</span> <span class="n">trace</span> <span class="k">as</span> <span class="n">trace_sdk</span>
        <span class="kn">from</span> <span class="nn">opentelemetry.sdk.trace.export</span> <span class="kn">import</span> <span class="n">SimpleSpanProcessor</span>

        <span class="n">endpoint</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"endpoint"</span><span class="p">,</span> <span class="s2">"http://127.0.0.1:6006/v1/traces"</span><span class="p">)</span>
        <span class="n">tracer_provider</span> <span class="o">=</span> <span class="n">trace_sdk</span><span class="o">.</span><span class="n">TracerProvider</span><span class="p">()</span>
        <span class="n">tracer_provider</span><span class="o">.</span><span class="n">add_span_processor</span><span class="p">(</span>
            <span class="n">SimpleSpanProcessor</span><span class="p">(</span><span class="n">OTLPSpanExporter</span><span class="p">(</span><span class="n">endpoint</span><span class="p">))</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">LlamaIndexInstrumentor</span><span class="p">()</span><span class="o">.</span><span class="n">instrument</span><span class="p">(</span>
            <span class="n">tracer_provider</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"tracer_provider"</span><span class="p">,</span> <span class="n">tracer_provider</span><span class="p">)</span>
        <span class="p">)</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="c1"># using an older version of arize</span>
        <span class="k">pass</span>

    <span class="c1"># older versions of arize, v1.x</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">phoenix.trace.llama_index</span> <span class="kn">import</span> <span class="n">OpenInferenceTraceCallbackHandler</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install Arize Phoenix with `pip install -q arize-phoenix`"</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">OpenInferenceTraceCallbackHandler</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Argilla](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/)[Next Deepeval](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/)
