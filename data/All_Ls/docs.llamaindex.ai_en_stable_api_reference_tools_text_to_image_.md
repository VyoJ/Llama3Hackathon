Title: Text to image - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/

Markdown Content:
Text to image - LlamaIndex


TextToImageToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/#llama_index.tools.text_to_image.TextToImageToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Text to Image tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-text-to-image/llama_index/tools/text_to_image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TextToImageToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Text to Image tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"generate_images"</span><span class="p">,</span> <span class="s2">"show_images"</span><span class="p">,</span> <span class="s2">"generate_image_variation"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="n">openai</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>

    <span class="k">def</span> <span class="nf">generate_images</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">n</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"256x256"</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Pass a prompt to OpenAIs text to image API to produce an image from the supplied query.</span>

<span class="sd">        Args:</span>
<span class="sd">            prompt (str): The prompt to generate an image(s) based on</span>
<span class="sd">            n (int): The number of images to generate. Defaults to 1.</span>
<span class="sd">            size (str): The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512</span>

<span class="sd">        When handling the urls returned from this function, NEVER strip any parameters or try to modify the url, they are necessary for authorization to view the image</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">openai</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">size</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">image</span><span class="p">[</span><span class="s2">"url"</span><span class="p">]</span> <span class="k">for</span> <span class="n">image</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]]</span>
        <span class="k">except</span> <span class="n">openai</span><span class="o">.</span><span class="n">error</span><span class="o">.</span><span class="n">OpenAIError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">error</span>

    <span class="k">def</span> <span class="nf">generate_image_variation</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">n</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"256x256"</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Accepts the url of an image and uses OpenAIs api to generate a variation of the image.</span>
<span class="sd">        This tool can take smaller images and create higher resolution variations, or vice versa.</span>

<span class="sd">        When passing a url from "generate_images" ALWAYS pass the url exactly as it was returned from the function, including ALL query parameters</span>
<span class="sd">        args:</span>
<span class="sd">            url (str): The url of the image to create a variation of</span>
<span class="sd">            n (int): The number of images to generate. Defaults to 1.</span>
<span class="sd">            size (str): The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">openai</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">create_variation</span><span class="p">(</span>
                <span class="n">image</span><span class="o">=</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(),</span> <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">size</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">image</span><span class="p">[</span><span class="s2">"url"</span><span class="p">]</span> <span class="k">for</span> <span class="n">image</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]]</span>
        <span class="k">except</span> <span class="n">openai</span><span class="o">.</span><span class="n">error</span><span class="o">.</span><span class="n">OpenAIError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">error</span>

    <span class="k">def</span> <span class="nf">show_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">urls</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this function to display image(s) using pyplot and pillow. This works in a jupyter notebook.</span>

<span class="sd">        Args:</span>
<span class="sd">            urls (str): The url(s) of the image(s) to show</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="k">for</span> <span class="n">url</span> <span class="ow">in</span> <span class="n">urls</span><span class="p">:</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span><span class="p">)))</span>
        <span class="k">return</span> <span class="s2">"images rendered successfully"</span>
</code></pre></div></td></tr></tbody></table>

### generate\_images [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/#llama_index.tools.text_to_image.TextToImageToolSpec.generate_images "Permanent link")

```
generate_images(prompt: str, n: Optional[int] = 1, size: Optional[str] = '256x256') -> List[str]
```

Pass a prompt to OpenAIs text to image API to produce an image from the supplied query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
The prompt to generate an image(s) based on



 | _required_ |
| `n` | `int` | 

The number of images to generate. Defaults to 1.



 | `1` |
| `size` | `str` | 

The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512



 | `'256x256'` |

When handling the urls returned from this function, NEVER strip any parameters or try to modify the url, they are necessary for authorization to view the image

Source code in `llama-index-integrations/tools/llama-index-tools-text-to-image/llama_index/tools/text_to_image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_images</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">n</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"256x256"</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Pass a prompt to OpenAIs text to image API to produce an image from the supplied query.</span>

<span class="sd">    Args:</span>
<span class="sd">        prompt (str): The prompt to generate an image(s) based on</span>
<span class="sd">        n (int): The number of images to generate. Defaults to 1.</span>
<span class="sd">        size (str): The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512</span>

<span class="sd">    When handling the urls returned from this function, NEVER strip any parameters or try to modify the url, they are necessary for authorization to view the image</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">openai</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">size</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">image</span><span class="p">[</span><span class="s2">"url"</span><span class="p">]</span> <span class="k">for</span> <span class="n">image</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]]</span>
    <span class="k">except</span> <span class="n">openai</span><span class="o">.</span><span class="n">error</span><span class="o">.</span><span class="n">OpenAIError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">error</span>
</code></pre></div></td></tr></tbody></table>

### generate\_image\_variation [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/#llama_index.tools.text_to_image.TextToImageToolSpec.generate_image_variation "Permanent link")

```
generate_image_variation(url: str, n: Optional[int] = 1, size: Optional[str] = '256x256') -> str
```

Accepts the url of an image and uses OpenAIs api to generate a variation of the image. This tool can take smaller images and create higher resolution variations, or vice versa.

When passing a url from "generate\_images" ALWAYS pass the url exactly as it was returned from the function, including ALL query parameters args: url (str): The url of the image to create a variation of n (int): The number of images to generate. Defaults to 1. size (str): The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512

Source code in `llama-index-integrations/tools/llama-index-tools-text-to-image/llama_index/tools/text_to_image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">generate_image_variation</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">n</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"256x256"</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Accepts the url of an image and uses OpenAIs api to generate a variation of the image.</span>
<span class="sd">    This tool can take smaller images and create higher resolution variations, or vice versa.</span>

<span class="sd">    When passing a url from "generate_images" ALWAYS pass the url exactly as it was returned from the function, including ALL query parameters</span>
<span class="sd">    args:</span>
<span class="sd">        url (str): The url of the image to create a variation of</span>
<span class="sd">        n (int): The number of images to generate. Defaults to 1.</span>
<span class="sd">        size (str): The size of the image(s) to generate. Defaults to 256x256. Other accepted values are 1024x1024 and 512x512</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">openai</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">create_variation</span><span class="p">(</span>
            <span class="n">image</span><span class="o">=</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(),</span> <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="n">size</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">image</span><span class="p">[</span><span class="s2">"url"</span><span class="p">]</span> <span class="k">for</span> <span class="n">image</span> <span class="ow">in</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]]</span>
    <span class="k">except</span> <span class="n">openai</span><span class="o">.</span><span class="n">error</span><span class="o">.</span><span class="n">OpenAIError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">error</span>
</code></pre></div></td></tr></tbody></table>

### show\_images [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/#llama_index.tools.text_to_image.TextToImageToolSpec.show_images "Permanent link")

```
show_images(urls: List[str])
```

Use this function to display image(s) using pyplot and pillow. This works in a jupyter notebook.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `urls` | `str` | 
The url(s) of the image(s) to show



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-text-to-image/llama_index/tools/text_to_image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">60</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">show_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">urls</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this function to display image(s) using pyplot and pillow. This works in a jupyter notebook.</span>

<span class="sd">    Args:</span>
<span class="sd">        urls (str): The url(s) of the image(s) to show</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="k">for</span> <span class="n">url</span> <span class="ow">in</span> <span class="n">urls</span><span class="p">:</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span><span class="p">)))</span>
    <span class="k">return</span> <span class="s2">"images rendered successfully"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tavily research](https://docs.llamaindex.ai/en/stable/api_reference/tools/tavily_research/)[Next Tool spec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/)
