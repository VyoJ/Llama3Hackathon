Title: Tonic validate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/

Markdown Content:
Tonic validate - LlamaIndex


AnswerConsistencyBinaryEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.AnswerConsistencyBinaryEvaluator "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's answer consistency binary metric.

The output score is a float that is either 0.0 or 1.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/answer_consistency_binary.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AnswerConsistencyBinaryEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's answer consistency binary metric.</span>

<span class="sd">    The output score is a float that is either 0.0 or 1.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">AnswerConsistencyBinaryMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

AnswerConsistencyEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.AnswerConsistencyEvaluator "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's answer consistency metric.

The output score is a float between 0.0 and 1.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/answer_consistency.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AnswerConsistencyEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's answer consistency metric.</span>

<span class="sd">    The output score is a float between 0.0 and 1.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">AnswerConsistencyMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

AnswerSimilarityEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.AnswerSimilarityEvaluator "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's answer similarity metric.

The output score is a float between 0.0 and 5.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/answer_similarity.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AnswerSimilarityEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's answer similarity metric.</span>

<span class="sd">    The output score is a float between 0.0 and 5.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">AnswerSimilarityMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reference_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">reference_response</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

AugmentationAccuracyEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.AugmentationAccuracyEvaluator "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's augmentation accuracy metric.

The output score is a float between 0.0 and 1.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/augmentation_accuracy.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AugmentationAccuracyEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's augmentation accuracy metric.</span>

<span class="sd">    The output score is a float between 0.0 and 1.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">AugmentationAccuracyMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

AugmentationPrecisionEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.AugmentationPrecisionEvaluator "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's augmentation precision metric.

The output score is a float between 0.0 and 1.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/augmentation_precision.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AugmentationPrecisionEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's augmentation precision metric.</span>

<span class="sd">    The output score is a float between 0.0 and 1.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">AugmentationPrecisionMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

RetrievalPrecisionEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.RetrievalPrecisionEvaluator "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's retrieval precision metric.

The output score is a float between 0.0 and 1.0.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `openai_service(OpenAIService)` |  | 
The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/retrieval_precision.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RetrievalPrecisionEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's retrieval precision metric.</span>

<span class="sd">    The output score is a float between 0.0 and 1.0.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        openai_service(OpenAIService): The OpenAI service to use. Specifies the chat</span>
<span class="sd">            completion model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">openai_service</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">openai_service</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">openai_service</span> <span class="o">=</span> <span class="n">OpenAIService</span><span class="p">(</span><span class="s2">"gpt-4"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span> <span class="o">=</span> <span class="n">openai_service</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">metric</span> <span class="o">=</span> <span class="n">RetrievalPrecisionMetric</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">response</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metric</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">llm_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_service</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">EvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span> <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

TonicValidateEvaluator [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.TonicValidateEvaluator "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseEvaluator](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/#llama_index.core.evaluation.BaseEvaluator "llama_index.core.evaluation.base.BaseEvaluator")`

Tonic Validate's validate scorer. Calculates all of Tonic Validate's metrics.

See https://docs.tonic.ai/validate/ for more details.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metrics(List[Metric])` |  | 
The metrics to use. Defaults to all of Tonic Validate's metrics.



 | _required_ |
| `model_evaluator(str)` |  | 

The OpenAI service to use. Specifies the chat completion model to use as the LLM evaluator. Defaults to "gpt-4".



 | _required_ |

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/tonic_validate_evaluator.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 30</span>
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
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TonicValidateEvaluator</span><span class="p">(</span><span class="n">BaseEvaluator</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Tonic Validate's validate scorer. Calculates all of Tonic Validate's metrics.</span>

<span class="sd">    See https://docs.tonic.ai/validate/ for more details.</span>

<span class="sd">    Args:</span>
<span class="sd">        metrics(List[Metric]): The metrics to use. Defaults to all of Tonic Validate's</span>
<span class="sd">            metrics.</span>
<span class="sd">        model_evaluator(str): The OpenAI service to use. Specifies the chat completion</span>
<span class="sd">            model to use as the LLM evaluator. Defaults to "gpt-4".</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">metrics</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">model_evaluator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4"</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">metrics</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metrics</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">AnswerConsistencyMetric</span><span class="p">(),</span>
                <span class="n">AnswerSimilarityMetric</span><span class="p">(),</span>
                <span class="n">AugmentationAccuracyMetric</span><span class="p">(),</span>
                <span class="n">AugmentationPrecisionMetric</span><span class="p">(),</span>
                <span class="n">RetrievalPrecisionMetric</span><span class="p">(),</span>
            <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">metrics</span> <span class="o">=</span> <span class="n">metrics</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model_evaluator</span> <span class="o">=</span> <span class="n">model_evaluator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">validate_scorer</span> <span class="o">=</span> <span class="n">ValidateScorer</span><span class="p">(</span><span class="n">metrics</span><span class="p">,</span> <span class="n">model_evaluator</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_calculate_average_score</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.metrics.answer_similarity_metric</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">AnswerSimilarityMetric</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">ave_score</span> <span class="o">=</span> <span class="mf">0.0</span>
        <span class="n">metric_cnt</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">metric_name</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">run</span><span class="o">.</span><span class="n">overall_scores</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">metric_name</span> <span class="o">==</span> <span class="n">AnswerSimilarityMetric</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
                <span class="n">ave_score</span> <span class="o">+=</span> <span class="n">score</span> <span class="o">/</span> <span class="mi">5</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">ave_score</span> <span class="o">+=</span> <span class="n">score</span>
            <span class="n">metric_cnt</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">ave_score</span> <span class="o">/</span> <span class="n">metric_cnt</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">contexts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">reference_response</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TonicValidateEvaluationResult</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">reference_response</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">responses</span> <span class="o">=</span> <span class="p">[</span><span class="n">llm_response</span><span class="p">]</span>

        <span class="n">run</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_scorer</span><span class="o">.</span><span class="n">score_run</span><span class="p">(</span><span class="n">responses</span><span class="p">)</span>

        <span class="n">ave_score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_average_score</span><span class="p">(</span><span class="n">run</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">TonicValidateEvaluationResult</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">contexts</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">score</span><span class="o">=</span><span class="n">ave_score</span><span class="p">,</span>
            <span class="n">score_dict</span><span class="o">=</span><span class="n">run</span><span class="o">.</span><span class="n">run_data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">scores</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">contexts_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
        <span class="n">reference_responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluates a batch of responses.</span>

<span class="sd">        Returns a Tonic Validate Run object, which can be logged to the Tonic Validate</span>
<span class="sd">        UI. See https://docs.tonic.ai/validate/ for more details.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
        <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

        <span class="n">llm_responses</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="p">,</span> <span class="n">contexts</span><span class="p">,</span> <span class="n">reference_response</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">contexts_list</span><span class="p">,</span> <span class="n">reference_responses</span>
        <span class="p">):</span>
            <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">reference_response</span><span class="p">)</span>

            <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
                <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
                <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
                <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">llm_responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">llm_response</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_scorer</span><span class="o">.</span><span class="n">score_run</span><span class="p">(</span><span class="n">llm_responses</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">evaluate_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">contexts_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
        <span class="n">reference_responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Evaluates a batch of responses.</span>

<span class="sd">        Returns a Tonic Validate Run object, which can be logged to the Tonic Validate</span>
<span class="sd">        UI. See https://docs.tonic.ai/validate/ for more details.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_run</span><span class="p">(</span>
                <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
                <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
                <span class="n">contexts_list</span><span class="o">=</span><span class="n">contexts_list</span><span class="p">,</span>
                <span class="n">reference_responses</span><span class="o">=</span><span class="n">reference_responses</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptDictType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts_dict</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table>

### aevaluate\_run `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.TonicValidateEvaluator.aevaluate_run "Permanent link")

```
aevaluate_run(queries: List[str], responses: List[str], contexts_list: List[List[str]], reference_responses: List[str], **kwargs: Any) -> Any
```

Evaluates a batch of responses.

Returns a Tonic Validate Run object, which can be logged to the Tonic Validate UI. See https://docs.tonic.ai/validate/ for more details.

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/tonic_validate_evaluator.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aevaluate_run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">contexts_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="n">reference_responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Evaluates a batch of responses.</span>

<span class="sd">    Returns a Tonic Validate Run object, which can be logged to the Tonic Validate</span>
<span class="sd">    UI. See https://docs.tonic.ai/validate/ for more details.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">tonic_validate.classes.benchmark</span> <span class="kn">import</span> <span class="n">BenchmarkItem</span>
    <span class="kn">from</span> <span class="nn">tonic_validate.classes.llm_response</span> <span class="kn">import</span> <span class="n">LLMResponse</span>

    <span class="n">llm_responses</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">query</span><span class="p">,</span> <span class="n">response</span><span class="p">,</span> <span class="n">contexts</span><span class="p">,</span> <span class="n">reference_response</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
        <span class="n">queries</span><span class="p">,</span> <span class="n">responses</span><span class="p">,</span> <span class="n">contexts_list</span><span class="p">,</span> <span class="n">reference_responses</span>
    <span class="p">):</span>
        <span class="n">benchmark_item</span> <span class="o">=</span> <span class="n">BenchmarkItem</span><span class="p">(</span><span class="n">question</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">answer</span><span class="o">=</span><span class="n">reference_response</span><span class="p">)</span>

        <span class="n">llm_response</span> <span class="o">=</span> <span class="n">LLMResponse</span><span class="p">(</span>
            <span class="n">llm_answer</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">llm_context_list</span><span class="o">=</span><span class="n">contexts</span><span class="p">,</span>
            <span class="n">benchmark_item</span><span class="o">=</span><span class="n">benchmark_item</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">llm_responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">llm_response</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_scorer</span><span class="o">.</span><span class="n">score_run</span><span class="p">(</span><span class="n">llm_responses</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### evaluate\_run [#](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/#llama_index.evaluation.tonic_validate.TonicValidateEvaluator.evaluate_run "Permanent link")

```
evaluate_run(queries: List[str], responses: List[str], contexts_list: List[List[str]], reference_responses: List[str], **kwargs: Any) -> Any
```

Evaluates a batch of responses.

Returns a Tonic Validate Run object, which can be logged to the Tonic Validate UI. See https://docs.tonic.ai/validate/ for more details.

Source code in `llama-index-integrations/evaluation/llama-index-evaluation-tonic-validate/llama_index/evaluation/tonic_validate/tonic_validate_evaluator.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">evaluate_run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">queries</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">contexts_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="n">reference_responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Evaluates a batch of responses.</span>

<span class="sd">    Returns a Tonic Validate Run object, which can be logged to the Tonic Validate</span>
<span class="sd">    UI. See https://docs.tonic.ai/validate/ for more details.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">aevaluate_run</span><span class="p">(</span>
            <span class="n">queries</span><span class="o">=</span><span class="n">queries</span><span class="p">,</span>
            <span class="n">responses</span><span class="o">=</span><span class="n">responses</span><span class="p">,</span>
            <span class="n">contexts_list</span><span class="o">=</span><span class="n">contexts_list</span><span class="p">,</span>
            <span class="n">reference_responses</span><span class="o">=</span><span class="n">reference_responses</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Semantic similarity](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/)[Next Colbert](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/)
