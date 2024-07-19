Title: Marvin - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/

Markdown Content:
Marvin - LlamaIndex


MarvinMetadataExtractor [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/#llama_index.extractors.marvin.MarvinMetadataExtractor "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseExtractor](https://docs.llamaindex.ai/en/stable/api_reference/extractors/#llama_index.core.extractors.interface.BaseExtractor "llama_index.core.extractors.interface.BaseExtractor")`

Source code in `llama-index-integrations/extractors/llama-index-extractors-marvin/llama_index/extractors/marvin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
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
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MarvinMetadataExtractor</span><span class="p">(</span><span class="n">BaseExtractor</span><span class="p">):</span>
    <span class="c1"># Forward reference to handle circular imports</span>
    <span class="n">marvin_model</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s2">"ai_model"</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The Marvin model to use for extracting custom metadata"</span>
    <span class="p">)</span>
    <span class="n">llm_model_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The LLM model string to use for extracting custom metadata"</span>
    <span class="p">)</span>

<span class="w">    </span><span class="sd">"""Metadata extractor for custom metadata using Marvin.</span>
<span class="sd">    Node-level extractor. Extracts</span>
<span class="sd">    `marvin_metadata` metadata field.</span>
<span class="sd">    Args:</span>
<span class="sd">        marvin_model: Marvin model to use for extracting metadata</span>
<span class="sd">        llm_model_string: (optional) LLM model string to use for extracting metadata</span>
<span class="sd">    Usage:</span>
<span class="sd">        #create extractor list</span>
<span class="sd">        extractors = [</span>
<span class="sd">            TitleExtractor(nodes=1, llm=llm),</span>
<span class="sd">            MarvinMetadataExtractor(marvin_model=YourMarvinMetadataModel),</span>
<span class="sd">        ]</span>

<span class="sd">        #create node parser to parse nodes from document</span>
<span class="sd">        node_parser = SentenceSplitter(</span>
<span class="sd">            text_splitter=text_splitter</span>
<span class="sd">        )</span>

<span class="sd">        #use node_parser to get nodes from documents</span>
<span class="sd">        from llama_index.ingestion import run_transformations</span>
<span class="sd">        nodes = run_transformations(documents, [node_parser] + extractors)</span>
<span class="sd">        print(nodes)</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">marvin_model</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">],</span>
        <span class="n">llm_model_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="kn">import</span> <span class="nn">marvin</span>
        <span class="kn">from</span> <span class="nn">marvin</span> <span class="kn">import</span> <span class="n">ai_model</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">marvin_model</span><span class="p">,</span> <span class="n">ai_model</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"marvin_model must be a subclass of ai_model"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">llm_model_string</span><span class="p">:</span>
            <span class="n">marvin</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">llm_model</span> <span class="o">=</span> <span class="n">llm_model_string</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">marvin_model</span><span class="o">=</span><span class="n">marvin_model</span><span class="p">,</span> <span class="n">llm_model_string</span><span class="o">=</span><span class="n">llm_model_string</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"MarvinEntityExtractor"</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aextract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
        <span class="kn">from</span> <span class="nn">marvin</span> <span class="kn">import</span> <span class="n">ai_model</span>

        <span class="n">ai_model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ai_model</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">marvin_model</span><span class="p">)</span>
        <span class="n">metadata_list</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">nodes_queue</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_tqdm_iterable</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_progress</span><span class="p">,</span> <span class="s2">"Extracting marvin metadata"</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes_queue</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_text_node_only</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">TextNode</span><span class="p">):</span>
                <span class="n">metadata_list</span><span class="o">.</span><span class="n">append</span><span class="p">({})</span>
                <span class="k">continue</span>

            <span class="c1"># TODO: Does marvin support async?</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">ai_model</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">())</span>

            <span class="n">metadata_list</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">"marvin_metadata"</span><span class="p">:</span> <span class="n">metadata</span><span class="o">.</span><span class="n">dict</span><span class="p">()})</span>
        <span class="k">return</span> <span class="n">metadata_list</span>
</code></pre></div></td></tr></tbody></table>

### llm\_model\_string `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/#llama_index.extractors.marvin.MarvinMetadataExtractor.llm_model_string "Permanent link")

```
llm_model_string: Optional[str] = Field(description='The LLM model string to use for extracting custom metadata')
```

Metadata extractor for custom metadata using Marvin. Node-level extractor. Extracts `marvin_metadata` metadata field. Args: marvin\_model: Marvin model to use for extracting metadata llm\_model\_string: (optional) LLM model string to use for extracting metadata Usage: #create extractor list extractors = \[ TitleExtractor(nodes=1, llm=llm), MarvinMetadataExtractor(marvin\_model=YourMarvinMetadataModel), \]

```
#create node parser to parse nodes from document
node_parser = SentenceSplitter(
    text_splitter=text_splitter
)

#use node_parser to get nodes from documents
from llama_index.ingestion import run_transformations
nodes = run_transformations(documents, [node_parser] + extractors)
print(nodes)
```

Back to top

[Previous Keyword](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/)[Next Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/)
