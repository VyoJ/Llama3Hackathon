Title: Openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/

Markdown Content:
Openai - LlamaIndex


OpenAIImageGenerationToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/#llama_index.tools.openai.OpenAIImageGenerationToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

OpenAI Image Generation tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-openai/llama_index/tools/openai/image_generation/base.py`

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
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAIImageGenerationToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAI Image Generation tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"image_generation"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">cache_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install openai with `pip install openai` to use this tool"</span>
            <span class="p">)</span>

<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cache_dir</span> <span class="o">=</span> <span class="n">cache_dir</span> <span class="ow">or</span> <span class="n">DEFAULT_CACHE_DIR</span>

    <span class="k">def</span> <span class="nf">get_cache_dir</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache_dir</span>

    <span class="k">def</span> <span class="nf">save_base64_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base64_str</span><span class="p">,</span> <span class="n">image_name</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>

            <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install Pillow with `pip install Pillow` to use this tool"</span>
            <span class="p">)</span>
        <span class="n">cache_dir</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache_dir</span>

        <span class="c1"># Create cache directory if it doesn't exist</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">cache_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">cache_dir</span><span class="p">)</span>

        <span class="c1"># Decode the base64 string</span>
        <span class="n">image_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">base64_str</span><span class="p">)</span>

        <span class="c1"># Create an image from the decoded bytes and save it</span>
        <span class="n">image_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">cache_dir</span><span class="p">,</span> <span class="n">image_name</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">image_data</span><span class="p">))</span> <span class="k">as</span> <span class="n">img</span><span class="p">:</span>
            <span class="n">img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">image_path</span>

    <span class="k">def</span> <span class="nf">image_generation</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"dall-e-3"</span><span class="p">,</span>
        <span class="n">quality</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"standard"</span><span class="p">,</span>
        <span class="n">num_images</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This tool accepts a natural language string and will use OpenAI's DALL-E model to generate an image.</span>

<span class="sd">        Args:</span>
<span class="sd">            text (str): The text to generate an image from.</span>
<span class="sd">            size (str): The size of the image to generate (1024x1024, 256x256, 512x512).</span>
<span class="sd">            model (str): The model to use to generate the image (dall-e-3, dall-e-2).</span>
<span class="sd">            quality (str): The quality of the image to generate (standard, hd).</span>
<span class="sd">            num_images (int): The number of images to generate.</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">images</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
            <span class="n">size</span><span class="o">=</span><span class="n">DEFAULT_SIZE</span><span class="p">,</span>
            <span class="n">quality</span><span class="o">=</span><span class="n">quality</span><span class="p">,</span>
            <span class="n">n</span><span class="o">=</span><span class="n">num_images</span><span class="p">,</span>
            <span class="n">response_format</span><span class="o">=</span><span class="s2">"b64_json"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">b64_json</span>

        <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span><span class="si">}</span><span class="s2">.jpg"</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">save_base64_image</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### image\_generation [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/#llama_index.tools.openai.OpenAIImageGenerationToolSpec.image_generation "Permanent link")

```
image_generation(text: str, model: Optional[str] = 'dall-e-3', quality: Optional[str] = 'standard', num_images: Optional[int] = 1) -> str
```

This tool accepts a natural language string and will use OpenAI's DALL-E model to generate an image.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text` | `str` | 
The text to generate an image from.



 | _required_ |
| `size` | `str` | 

The size of the image to generate (1024x1024, 256x256, 512x512).



 | _required_ |
| `model` | `str` | 

The model to use to generate the image (dall-e-3, dall-e-2).



 | `'dall-e-3'` |
| `quality` | `str` | 

The quality of the image to generate (standard, hd).



 | `'standard'` |
| `num_images` | `int` | 

The number of images to generate.



 | `1` |

Source code in `llama-index-integrations/tools/llama-index-tools-openai/llama_index/tools/openai/image_generation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
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
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">image_generation</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"dall-e-3"</span><span class="p">,</span>
    <span class="n">quality</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"standard"</span><span class="p">,</span>
    <span class="n">num_images</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This tool accepts a natural language string and will use OpenAI's DALL-E model to generate an image.</span>

<span class="sd">    Args:</span>
<span class="sd">        text (str): The text to generate an image from.</span>
<span class="sd">        size (str): The size of the image to generate (1024x1024, 256x256, 512x512).</span>
<span class="sd">        model (str): The model to use to generate the image (dall-e-3, dall-e-2).</span>
<span class="sd">        quality (str): The quality of the image to generate (standard, hd).</span>
<span class="sd">        num_images (int): The number of images to generate.</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">images</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
        <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
        <span class="n">prompt</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
        <span class="n">size</span><span class="o">=</span><span class="n">DEFAULT_SIZE</span><span class="p">,</span>
        <span class="n">quality</span><span class="o">=</span><span class="n">quality</span><span class="p">,</span>
        <span class="n">n</span><span class="o">=</span><span class="n">num_images</span><span class="p">,</span>
        <span class="n">response_format</span><span class="o">=</span><span class="s2">"b64_json"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">b64_json</span>

    <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span><span class="si">}</span><span class="s2">.jpg"</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">save_base64_image</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Ondemand loader](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/)[Next Openapi](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/)
