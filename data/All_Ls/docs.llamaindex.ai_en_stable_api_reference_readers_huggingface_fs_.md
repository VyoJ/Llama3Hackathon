Title: Huggingface fs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/

Markdown Content:
Huggingface fs - LlamaIndex


Init params.

HuggingFaceFSReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/#llama_index.readers.huggingface_fs.HuggingFaceFSReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Hugging Face File System reader.

Uses the new Filesystem API from the Hugging Face Hub client library.

Source code in `llama-index-integrations/readers/llama-index-readers-huggingface-fs/llama_index/readers/huggingface_fs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
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
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HuggingFaceFSReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hugging Face File System reader.</span>

<span class="sd">    Uses the new Filesystem API from the Hugging Face Hub client library.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">huggingface_hub</span> <span class="kn">import</span> <span class="n">HfFileSystem</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">fs</span> <span class="o">=</span> <span class="n">HfFileSystem</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_dicts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="n">test_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">read_bytes</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="k">if</span> <span class="s2">".gz"</span> <span class="ow">in</span> <span class="n">path</span><span class="o">.</span><span class="n">suffixes</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">gzip</span>

            <span class="k">with</span> <span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmp</span><span class="p">:</span>
                <span class="n">tmp</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">tmp</span><span class="p">)</span>
                <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">tmp</span> <span class="o">/</span> <span class="s2">"tmp.jsonl.gz"</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
                    <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">test_data</span><span class="p">)</span>

                <span class="n">f</span> <span class="o">=</span> <span class="n">gzip</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp</span> <span class="o">/</span> <span class="s2">"tmp.jsonl.gz"</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span>
                <span class="n">raw</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">raw</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">test_data</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

        <span class="n">text_lines</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">json_dicts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">text_lines</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">json_dict</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
            <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">json_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json_dict</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">json_dicts</span>

    <span class="k">def</span> <span class="nf">load_df</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load pandas dataframe."""</span>
        <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">load_dicts</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data."""</span>
        <span class="n">json_dicts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_dicts</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">json_dicts</span><span class="p">:</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)))</span>
        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_dicts [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/#llama_index.readers.huggingface_fs.HuggingFaceFSReader.load_dicts "Permanent link")

```
load_dicts(path: str) -> List[Dict]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-huggingface-fs/llama_index/readers/huggingface_fs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
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
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_dicts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="n">test_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fs</span><span class="o">.</span><span class="n">read_bytes</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="k">if</span> <span class="s2">".gz"</span> <span class="ow">in</span> <span class="n">path</span><span class="o">.</span><span class="n">suffixes</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">gzip</span>

        <span class="k">with</span> <span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmp</span><span class="p">:</span>
            <span class="n">tmp</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">tmp</span><span class="p">)</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">tmp</span> <span class="o">/</span> <span class="s2">"tmp.jsonl.gz"</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
                <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">test_data</span><span class="p">)</span>

            <span class="n">f</span> <span class="o">=</span> <span class="n">gzip</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp</span> <span class="o">/</span> <span class="s2">"tmp.jsonl.gz"</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span>
            <span class="n">raw</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">raw</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">test_data</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

    <span class="n">text_lines</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">json_dicts</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">text_lines</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">json_dict</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">json_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json_dict</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">json_dicts</span>
</code></pre></div></td></tr></tbody></table>

### load\_df [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/#llama_index.readers.huggingface_fs.HuggingFaceFSReader.load_df "Permanent link")

```
load_df(path: str) -> DataFrame
```

Load pandas dataframe.

Source code in `llama-index-integrations/readers/llama-index-readers-huggingface-fs/llama_index/readers/huggingface_fs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_df</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load pandas dataframe."""</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">load_dicts</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/#llama_index.readers.huggingface_fs.HuggingFaceFSReader.load_data "Permanent link")

```
load_data(path: str) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data.

Source code in `llama-index-integrations/readers/llama-index-readers-huggingface-fs/llama_index/readers/huggingface_fs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data."""</span>
    <span class="n">json_dicts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_dicts</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">json_dicts</span><span class="p">:</span>
        <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">d</span><span class="p">)))</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/)[Next Hwp](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/)
