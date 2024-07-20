Title: Obsidian - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/

Markdown Content:
Obsidian - LlamaIndex


ObsidianReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/#llama_index.readers.obsidian.ObsidianReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Utilities for loading data from an Obsidian Vault.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_dir` | `str` | 
Path to the vault.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-obsidian/llama_index/readers/obsidian/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
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
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ObsidianReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Utilities for loading data from an Obsidian Vault.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_dir (str): Path to the vault.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">input_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">input_dir</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory."""</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_dir</span><span class="p">):</span>
            <span class="n">dirnames</span><span class="p">[:]</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dirnames</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">d</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"."</span><span class="p">)]</span>
            <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".md"</span><span class="p">):</span>
                    <span class="n">filepath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span>
                    <span class="n">content</span> <span class="o">=</span> <span class="n">MarkdownReader</span><span class="p">()</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">filepath</span><span class="p">))</span>
                    <span class="n">docs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">load_langchain_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"LCDocument"</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data in LangChain document format."""</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">to_langchain_format</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/#llama_index.readers.obsidian.ObsidianReader.load_data "Permanent link")

```
load_data(*args: Any, **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

Source code in `llama-index-integrations/readers/llama-index-readers-obsidian/llama_index/readers/obsidian/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory."""</span>
    <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_dir</span><span class="p">):</span>
        <span class="n">dirnames</span><span class="p">[:]</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dirnames</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">d</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"."</span><span class="p">)]</span>
        <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".md"</span><span class="p">):</span>
                <span class="n">filepath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">MarkdownReader</span><span class="p">()</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">filepath</span><span class="p">))</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_langchain\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/#llama_index.readers.obsidian.ObsidianReader.load_langchain_documents "Permanent link")

```
load_langchain_documents(**load_kwargs: Any) -> List[Document]
```

Load data in LangChain document format.

Source code in `llama-index-integrations/readers/llama-index-readers-obsidian/llama_index/readers/obsidian/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_langchain_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="s2">"LCDocument"</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data in LangChain document format."""</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">to_langchain_format</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Nougat ocr](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/)[Next Openalex](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/)
