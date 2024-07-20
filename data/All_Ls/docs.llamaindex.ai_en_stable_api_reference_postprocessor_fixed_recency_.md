Title: Fixed recency - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/

Markdown Content:
Fixed recency - LlamaIndex


Node PostProcessor module.

FixedRecencyPostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/#llama_index.core.postprocessor.FixedRecencyPostprocessor "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Fixed Recency post-processor.

This post-processor does the following steps orders nodes by date.

Assumes the date\_key corresponds to a date field in the metadata.

Source code in `llama-index-core/llama_index/core/postprocessor/node_recency.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">40</span>
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
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FixedRecencyPostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Fixed Recency post-processor.</span>

<span class="sd">    This post-processor does the following steps orders nodes by date.</span>

<span class="sd">    Assumes the date_key corresponds to a date field in the metadata.</span>
<span class="sd">    """</span>

    <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">date_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"date"</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"FixedRecencyPostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing query bundle in extra info."</span><span class="p">)</span>

        <span class="c1"># sort nodes by date</span>
        <span class="n">node_dates</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">date_key</span><span class="p">]</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">sorted_node_idxs</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">node_dates</span><span class="o">.</span><span class="n">argsort</span><span class="p">())</span>
        <span class="n">sorted_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">nodes</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">sorted_node_idxs</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">sorted_nodes</span><span class="p">[:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_k</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Embedding recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/)[Next Flag embedding reranker](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/flag_embedding_reranker/)
