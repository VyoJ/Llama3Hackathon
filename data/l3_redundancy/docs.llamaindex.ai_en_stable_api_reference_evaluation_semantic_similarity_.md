Title: Semantic similarity - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/

Markdown Content:
Semantic similarity - LlamaIndex


Evaluation modules.

SemanticSimilarityEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/#llama_index.core.evaluation.SemanticSimilarityEvaluator "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Embedding similarity evaluator.

Evaluate the quality of a question answering system by comparing the similarity between embeddings of the generated answer and the reference answer.

Inspired by this paper: - Semantic Answer Similarity for Evaluating Question Answering Models https://arxiv.org/pdf/2108.06130.pdf

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `service_context` | `Optional[ServiceContext]` | 
Service context.



 | `None` |
| `similarity_threshold` | `float` | 

Embedding similarity threshold for "passing". Defaults to 0.8.



 | `0.8` |

Source code in `llama-index-core/llama_index/core/evaluation/semantic_similarity.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SemanticSimilarityEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Embedding similarity evaluator.</span>

<span class="sd">    Evaluate the quality of a question answering system by</span>
<span class="sd">    comparing the similarity between embeddings of the generated answer</span>
<span class="sd">    and the reference answer.</span>

<span class="sd">    Inspired by this paper:</span>
<span class="sd">    - Semantic Answer Similarity for Evaluating Question Answering Models</span>
<span class="sd">        https://arxiv.org/pdf/2108.06130.pdf</span>

<span class="sd">    Args:</span>
<span class="sd">        service_context (Optional[ServiceContext]): Service context.</span>
<span class="sd">        similarity_threshold (float): Embedding similarity threshold for "passing".</span>
<span class="sd">            Defaults to 0.8.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_mode</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SimilarityMode</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">similarity_threshold</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.8</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">embed_model_from_settings_or_context</span><span class="p">(</span>
            <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">similarity_fn</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">similarity_mode</span> <span class="o">=</span> <span class="n">similarity_mode</span> <span class="ow">or</span> <span class="n">SimilarityMode</span><span class="o">.</span><span class="n">DEFAULT</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_fn</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">similarity</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">similarity_mode</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">similarity_mode</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify both similarity_fn and similarity_mode"</span>
                <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_fn</span> <span class="o">=</span> <span class="n">similarity_fn</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_threshold</span> <span class="o">=</span> <span class="n">similarity_threshold</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reference</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="p">,</span> <span class="n">kwargs</span>  <span class="c1"># Unused</span>

        <span class="k">if</span> <span class="n">response</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">reference</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify both response and reference"</span><span class="p">)</span>

        <span class="n">response_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">aget_text_embedding</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
        <span class="n">reference_embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">aget_text_embedding</span><span class="p">(</span><span class="n">reference</span><span class="p">)</span>

        <span class="n">similarity_score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_fn</span><span class="p">(</span><span class="n">response_embedding</span><span class="p">,</span> <span class="n">reference_embedding</span><span class="p">)</span>
        <span class="n">passing</span> <span class="o">=</span> <span class="n">similarity_score</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_threshold</span>
        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">score</span><span class="o">=</span><span class="n">similarity_score</span><span class="p">,</span>
            <span class="n">passing</span><span class="o">=</span><span class="n">passing</span><span class="p">,</span>
            <span class="n">feedback</span><span class="o">=</span><span class="sa">f</span><span class="s2">"Similarity score: </span><span class="si">{</span><span class="n">similarity_score</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retrieval](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/)[Next Tonic validate](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/)
