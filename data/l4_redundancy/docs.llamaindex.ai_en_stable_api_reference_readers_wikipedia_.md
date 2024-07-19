Title: Wikipedia - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/

Markdown Content:
Wikipedia - LlamaIndex


WikipediaReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/#llama_index.readers.wikipedia.WikipediaReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Wikipedia reader.

Reads a page.

Source code in `llama-index-integrations/readers/llama-index-readers-wikipedia/llama_index/readers/wikipedia/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WikipediaReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Wikipedia reader.</span>

<span class="sd">    Reads a page.</span>

<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">wikipedia</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`wikipedia` package not found, please run `pip install wikipedia`"</span>
            <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"WikipediaReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">pages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">lang_prefix</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            pages (List[str]): List of pages to read.</span>
<span class="sd">            lang_prefix (str): Language prefix for Wikipedia. Defaults to English. Valid Wikipedia language codes</span>
<span class="sd">            can be found at https://en.wikipedia.org/wiki/List_of_Wikipedias.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">wikipedia</span>

        <span class="k">if</span> <span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="s2">"en"</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">wikipedia</span><span class="o">.</span><span class="n">languages</span><span class="p">():</span>
                <span class="n">wikipedia</span><span class="o">.</span><span class="n">set_lang</span><span class="p">(</span><span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Language prefix '</span><span class="si">{</span><span class="n">lang_prefix</span><span class="si">}</span><span class="s2">' for Wikipedia is not supported. Check supported languages at https://en.wikipedia.org/wiki/List_of_Wikipedias."</span>
                <span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">:</span>
            <span class="n">wiki_page</span> <span class="o">=</span> <span class="n">wikipedia</span><span class="o">.</span><span class="n">page</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
            <span class="n">page_content</span> <span class="o">=</span> <span class="n">wiki_page</span><span class="o">.</span><span class="n">content</span>
            <span class="n">page_id</span> <span class="o">=</span> <span class="n">wiki_page</span><span class="o">.</span><span class="n">pageid</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">page_content</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/#llama_index.readers.wikipedia.WikipediaReader.load_data "Permanent link")

```
load_data(pages: List[str], lang_prefix: str = 'en', **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pages` | `List[str]` | 
List of pages to read.



 | _required_ |
| `lang_prefix` | `str` | 

Language prefix for Wikipedia. Defaults to English. Valid Wikipedia language codes



 | `'en'` |
| `can` | `be found at https` | 

//en.wikipedia.org/wiki/List\_of\_Wikipedias.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-wikipedia/llama_index/readers/wikipedia/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">pages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">lang_prefix</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        pages (List[str]): List of pages to read.</span>
<span class="sd">        lang_prefix (str): Language prefix for Wikipedia. Defaults to English. Valid Wikipedia language codes</span>
<span class="sd">        can be found at https://en.wikipedia.org/wiki/List_of_Wikipedias.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">wikipedia</span>

    <span class="k">if</span> <span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="s2">"en"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">wikipedia</span><span class="o">.</span><span class="n">languages</span><span class="p">():</span>
            <span class="n">wikipedia</span><span class="o">.</span><span class="n">set_lang</span><span class="p">(</span><span class="n">lang_prefix</span><span class="o">.</span><span class="n">lower</span><span class="p">())</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Language prefix '</span><span class="si">{</span><span class="n">lang_prefix</span><span class="si">}</span><span class="s2">' for Wikipedia is not supported. Check supported languages at https://en.wikipedia.org/wiki/List_of_Wikipedias."</span>
            <span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">:</span>
        <span class="n">wiki_page</span> <span class="o">=</span> <span class="n">wikipedia</span><span class="o">.</span><span class="n">page</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
        <span class="n">page_content</span> <span class="o">=</span> <span class="n">wiki_page</span><span class="o">.</span><span class="n">content</span>
        <span class="n">page_id</span> <span class="o">=</span> <span class="n">wiki_page</span><span class="o">.</span><span class="n">pageid</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">page_content</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Whatsapp](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/)[Next Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordlift/)
