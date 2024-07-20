Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/

Markdown Content:
Index - LlamaIndex


Base reader class.

BaseReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Utilities for loading data from a directory.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseReader</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Utilities for loading data from a directory."""</span>

    <span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory lazily."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2"> does not provide lazy_load_data method currently"</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">alazy_load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory lazily."""</span>
        <span class="c1"># Fake async - just calls the sync method. Override in subclasses for real async implementations.</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">))</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_langchain_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"LCDocument"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data in LangChain document format."""</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">to_langchain_format</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__modify_schema__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">field_schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]):</span>
        <span class="n">field_schema</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="s2">"title"</span><span class="p">:</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span><span class="p">})</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__get_pydantic_json_schema__</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">core_schema</span><span class="p">,</span> <span class="n">handler</span>
    <span class="p">):</span>  <span class="c1"># Needed for pydantic v2 to work</span>
        <span class="n">json_schema</span> <span class="o">=</span> <span class="n">handler</span><span class="p">(</span><span class="n">core_schema</span><span class="p">)</span>
        <span class="n">json_schema</span> <span class="o">=</span> <span class="n">handler</span><span class="o">.</span><span class="n">resolve_ref_schema</span><span class="p">(</span><span class="n">json_schema</span><span class="p">)</span>
        <span class="n">json_schema</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span>
        <span class="k">return</span> <span class="n">json_schema</span>
</code></pre></div></td></tr></tbody></table>

### lazy\_load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader.lazy_load_data "Permanent link")

```
lazy_load_data(*args: Any, **load_kwargs: Any) -> Iterable[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory lazily.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory lazily."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2"> does not provide lazy_load_data method currently"</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### alazy\_load\_data `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader.alazy_load_data "Permanent link")

```
alazy_load_data(*args: Any, **load_kwargs: Any) -> Iterable[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory lazily.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">alazy_load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory lazily."""</span>
    <span class="c1"># Fake async - just calls the sync method. Override in subclasses for real async implementations.</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader.load_data "Permanent link")

```
load_data(*args: Any, **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### aload\_data `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader.aload_data "Permanent link")

```
aload_data(*args: Any, **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aload_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_langchain\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader.load_langchain_documents "Permanent link")

```
load_langchain_documents(**load_kwargs: Any) -> List[Document]
```

Load data in LangChain document format.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_langchain_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"LCDocument"</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data in LangChain document format."""</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">to_langchain_format</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

BasePydanticReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`, `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`

Serialiable Data Loader with Pydantic.

Source code in `llama-index-core/llama_index/core/readers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BasePydanticReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">,</span> <span class="n">BaseComponent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Serialiable Data Loader with Pydantic."""</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Whether the data is loaded from a remote API or a local file."</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Imdb review](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/)[Next Intercom](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/)
