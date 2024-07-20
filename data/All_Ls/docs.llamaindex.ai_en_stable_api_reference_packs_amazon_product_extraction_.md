Title: Amazon product extraction - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/

Markdown Content:
Amazon product extraction - LlamaIndex


AmazonProductExtractionPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/#llama_index.packs.amazon_product_extraction.AmazonProductExtractionPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Product extraction pack.

Given a website url of a product (e.g. Amazon page), screenshot it, and use GPT-4V to extract structured outputs.

Source code in `llama-index-packs/llama-index-packs-amazon-product-extraction/llama_index/packs/amazon_product_extraction/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 46</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AmazonProductExtractionPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Product extraction pack.</span>

<span class="sd">    Given a website url of a product (e.g. Amazon page), screenshot it,</span>
<span class="sd">    and use GPT-4V to extract structured outputs.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">website_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tmp_file_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"./tmp.png"</span><span class="p">,</span>
        <span class="n">screenshot_width</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1200</span><span class="p">,</span>
        <span class="n">screenshot_height</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">800</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PROMPT_TEMPLATE_STR</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">website_url</span> <span class="o">=</span> <span class="n">website_url</span>
        <span class="c1"># download image to temporary file</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="n">_screenshot_page</span><span class="p">(</span>
                <span class="n">website_url</span><span class="p">,</span>
                <span class="n">tmp_file_path</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="n">screenshot_width</span><span class="p">,</span>
                <span class="n">height</span><span class="o">=</span><span class="n">screenshot_height</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># put your local directory here</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">image_documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
            <span class="n">input_files</span><span class="o">=</span><span class="p">[</span><span class="n">tmp_file_path</span><span class="p">]</span>
        <span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>

        <span class="c1"># initialize openai pydantic program</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_mm_llm</span> <span class="o">=</span> <span class="n">OpenAIMultiModal</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="mi">1000</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">openai_program</span> <span class="o">=</span> <span class="n">MultiModalLLMCompletionProgram</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">output_parser</span><span class="o">=</span><span class="n">PydanticOutputParser</span><span class="p">(</span><span class="n">Product</span><span class="p">),</span>
            <span class="n">image_documents</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">image_documents</span><span class="p">,</span>
            <span class="n">prompt_template_str</span><span class="o">=</span><span class="n">prompt_template_str</span><span class="p">,</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">openai_mm_llm</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"openai_program"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_program</span><span class="p">,</span>
            <span class="s2">"openai_mm_llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_mm_llm</span><span class="p">,</span>
            <span class="s2">"image_documents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_documents</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_program</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/#llama_index.packs.amazon_product_extraction.AmazonProductExtractionPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-amazon-product-extraction/llama_index/packs/amazon_product_extraction/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"openai_program"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_program</span><span class="p">,</span>
        <span class="s2">"openai_mm_llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_mm_llm</span><span class="p">,</span>
        <span class="s2">"image_documents"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">image_documents</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/#llama_index.packs.amazon_product_extraction.AmazonProductExtractionPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-amazon-product-extraction/llama_index/packs/amazon_product_extraction/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">openai_program</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Agents llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/)[Next Arize phoenix query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/)
