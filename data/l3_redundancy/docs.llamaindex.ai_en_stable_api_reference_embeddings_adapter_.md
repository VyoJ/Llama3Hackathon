Title: Adapter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/

Markdown Content:
Adapter - LlamaIndex


LinearAdapterEmbeddingModel `module-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/#llama_index.embeddings.adapter.LinearAdapterEmbeddingModel "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
LinearAdapterEmbeddingModel = [AdapterEmbeddingModel](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/#llama_index.embeddings.adapter.AdapterEmbeddingModel "llama_index.embeddings.adapter.base.AdapterEmbeddingModel")
```

AdapterEmbeddingModel [#](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/#llama_index.embeddings.adapter.AdapterEmbeddingModel "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEmbedding](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "llama_index.core.base.embeddings.base.BaseEmbedding")`

Adapter for any embedding model.

This is a wrapper around any embedding model that adds an adapter layer on top of it. This is useful for finetuning an embedding model on a downstream task. The embedding model can be any model - it does not need to expose gradients.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `base_embed_model` | `[BaseEmbedding](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "llama_index.core.base.embeddings.base.BaseEmbedding")` | 
Base embedding model.



 | _required_ |
| `adapter_path` | `str` | 

Path to adapter.



 | _required_ |
| `adapter_cls` | `Optional[Type[Any]]` | 

Adapter class. Defaults to None, in which case a linear adapter is used.



 | `None` |
| `transform_query` | `bool` | 

Whether to transform query embeddings. Defaults to True.



 | `True` |
| `device` | `Optional[str]` | 

Device to use. Defaults to None.



 | `None` |
| `embed_batch_size` | `int` | 

Batch size for embedding. Defaults to 10.



 | `DEFAULT_EMBED_BATCH_SIZE` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.CallbackManager")]` | 

Callback manager. Defaults to None.



 | `None` |

Source code in `llama-index-integrations/embeddings/llama-index-embeddings-adapter/llama_index/embeddings/adapter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
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
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AdapterEmbeddingModel</span><span class="p">(</span><span class="n">BaseEmbedding</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Adapter for any embedding model.</span>

<span class="sd">    This is a wrapper around any embedding model that adds an adapter layer \</span>
<span class="sd">        on top of it.</span>
<span class="sd">    This is useful for finetuning an embedding model on a downstream task.</span>
<span class="sd">    The embedding model can be any model - it does not need to expose gradients.</span>

<span class="sd">    Args:</span>
<span class="sd">        base_embed_model (BaseEmbedding): Base embedding model.</span>
<span class="sd">        adapter_path (str): Path to adapter.</span>
<span class="sd">        adapter_cls (Optional[Type[Any]]): Adapter class. Defaults to None, in which \</span>
<span class="sd">            case a linear adapter is used.</span>
<span class="sd">        transform_query (bool): Whether to transform query embeddings. Defaults to True.</span>
<span class="sd">        device (Optional[str]): Device to use. Defaults to None.</span>
<span class="sd">        embed_batch_size (int): Batch size for embedding. Defaults to 10.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): Callback manager. \</span>
<span class="sd">            Defaults to None.</span>

<span class="sd">    """</span>

    <span class="n">_base_embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_adapter</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_transform_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_target_device</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">base_embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span><span class="p">,</span>
        <span class="n">adapter_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">adapter_cls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transform_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">device</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_EMBED_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="kn">import</span> <span class="nn">torch</span>
        <span class="kn">from</span> <span class="nn">llama_index.embeddings.adapter.utils</span> <span class="kn">import</span> <span class="n">BaseAdapter</span><span class="p">,</span> <span class="n">LinearLayer</span>

        <span class="k">if</span> <span class="n">device</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Use pytorch device: </span><span class="si">{</span><span class="n">device</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_target_device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_base_embed_model</span> <span class="o">=</span> <span class="n">base_embed_model</span>

        <span class="k">if</span> <span class="n">adapter_cls</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">adapter_cls</span> <span class="o">=</span> <span class="n">LinearLayer</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">adapter_cls</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Type</span><span class="p">[</span><span class="n">BaseAdapter</span><span class="p">],</span> <span class="n">adapter_cls</span><span class="p">)</span>

        <span class="n">adapter</span> <span class="o">=</span> <span class="n">adapter_cls</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">adapter_path</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_adapter</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseAdapter</span><span class="p">,</span> <span class="n">adapter</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_adapter</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_target_device</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_transform_query</span> <span class="o">=</span> <span class="n">transform_query</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">embed_batch_size</span><span class="o">=</span><span class="n">embed_batch_size</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Adapter for </span><span class="si">{</span><span class="n">base_embed_model</span><span class="o">.</span><span class="n">model_name</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"AdapterEmbeddingModel"</span>

    <span class="k">def</span> <span class="nf">_get_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get query embedding."""</span>
        <span class="kn">import</span> <span class="nn">torch</span>

        <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_embed_model</span><span class="o">.</span><span class="n">_get_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transform_query</span><span class="p">:</span>
            <span class="n">query_embedding_t</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">query_embedding</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_target_device</span><span class="p">)</span>
            <span class="n">query_embedding_t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adapter</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">query_embedding_t</span><span class="p">)</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">query_embedding_t</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">query_embedding</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_query_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get query embedding."""</span>
        <span class="kn">import</span> <span class="nn">torch</span>

        <span class="n">query_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_embed_model</span><span class="o">.</span><span class="n">_aget_query_embedding</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transform_query</span><span class="p">:</span>
            <span class="n">query_embedding_t</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">query_embedding</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_target_device</span><span class="p">)</span>
            <span class="n">query_embedding_t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_adapter</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="n">query_embedding_t</span><span class="p">)</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">query_embedding_t</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">query_embedding</span>

    <span class="k">def</span> <span class="nf">_get_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_embed_model</span><span class="o">.</span><span class="n">_get_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_text_embedding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_embed_model</span><span class="o">.</span><span class="n">_aget_text_embedding</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/)[Next Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alephalpha/)
