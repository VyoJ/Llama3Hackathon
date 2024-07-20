Title: File - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/file/

Markdown Content:
File - LlamaIndex


CSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

CSV parser.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""CSV parser.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Union[str, List[str]]: a string or a List of strings.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">csv</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"csv module is required to read CSV files."</span><span class="p">)</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
                <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">))</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
Union\[str, List\[str\]\]: a string or a List of strings.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Union[str, List[str]]: a string or a List of strings.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">csv</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"csv module is required to read CSV files."</span><span class="p">)</span>
    <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
            <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">))</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

DocxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Docx parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DocxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Docx parser."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">docx2txt</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"docx2txt is required to read Microsoft Word files: "</span>
                <span class="s2">"`pip install docx2txt`"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">docx2txt</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"docx2txt is required to read Microsoft Word files: "</span>
            <span class="s2">"`pip install docx2txt`"</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

EpubReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Epub Parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/epub/base.py`

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
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EpubReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Epub Parser."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">ebooklib</span>
            <span class="kn">import</span> <span class="nn">html2text</span>
            <span class="kn">from</span> <span class="nn">ebooklib</span> <span class="kn">import</span> <span class="n">epub</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install extra dependencies that are required for "</span>
                <span class="s2">"the EpubReader: "</span>
                <span class="s2">"`pip install EbookLib html2text`"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"fs was specified but EpubReader doesn't support loading "</span>
                <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
            <span class="p">)</span>

        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">book</span> <span class="o">=</span> <span class="n">epub</span><span class="o">.</span><span class="n">read_epub</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s2">"ignore_ncx"</span><span class="p">:</span> <span class="kc">True</span><span class="p">})</span>

        <span class="c1"># Iterate through all chapters.</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">book</span><span class="o">.</span><span class="n">get_items</span><span class="p">():</span>
            <span class="c1"># Chapters are typically located in epub documents items.</span>
            <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">get_type</span><span class="p">()</span> <span class="o"></span> <span class="n">ebooklib</span><span class="o">.</span><span class="n">ITEM_DOCUMENT</span><span class="p">:</span>
            <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">html2text</span><span class="o">.</span><span class="n">html2text</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="p">)</span>

    <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

FlatReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Flat reader.

Extract raw text from a file and save the file type in the metadata

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/flat/base.py`

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
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FlatReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Flat reader.</span>

<span class="sd">    Extract raw text from a file and save the file type in the metadata</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file into string.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/flat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file into string."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

HTMLTagReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HTMLTagReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Read HTML files and extract text from a specific tag with BeautifulSoup.

By default, reads the text from the `<section>` tag.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/html/base.py`

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
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HTMLTagReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Read HTML files and extract text from a specific tag with BeautifulSoup.</span>

<span class="sd">    By default, reads the text from the ``&lt;section&gt;`` tag.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tag</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"section"</span><span class="p">,</span>
        <span class="n">ignore_no_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tag</span> <span class="o">=</span> <span class="n">tag</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ignore_no_id</span> <span class="o">=</span> <span class="n">ignore_no_id</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"bs4 is required to read HTML files."</span><span class="p">)</span>

        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">html_file</span><span class="p">:</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">html_file</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>

        <span class="n">tags</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">find_all</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tag</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
            <span class="n">tag_id</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span>
            <span class="n">tag_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_text_from_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ignore_no_id</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tag_id</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"tag"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tag</span><span class="p">,</span>
                <span class="s2">"tag_id"</span><span class="p">:</span> <span class="n">tag_id</span><span class="p">,</span>
                <span class="s2">"file_path"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="p">}</span>
            <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">tag_text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">_extract_text_from_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">:</span> <span class="s2">"Tag"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">NavigableString</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"bs4 is required to read HTML files."</span><span class="p">)</span>

        <span class="n">texts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">tag</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">elem</span><span class="p">,</span> <span class="n">NavigableString</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">strip</span><span class="p">():</span>
                    <span class="n">texts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
            <span class="k">elif</span> <span class="n">elem</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">BODYTEXT_SECTION</span><span class="p">:</span>
                <span class="n">m</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="bp">self</span><span class="o">.</span><span class="n">SECTION_NAME_LENGTH</span> <span class="p">:]))</span>

        <span class="k">return</span> <span class="p">[</span><span class="s2">"BodyText/Section"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">m</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">_text_to_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

    <span class="k">def</span> <span class="nf">get_text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>

        <span class="c1"># 전체 text 추출</span>

    <span class="k">def</span> <span class="nf">_get_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">file_dirs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">sections</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_body_sections</span><span class="p">(</span><span class="n">file_dirs</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">section</span> <span class="ow">in</span> <span class="n">sections</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_text_from_section</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">section</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>

    <span class="k">def</span> <span class="nf">is_compressed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">header</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">openstream</span><span class="p">(</span><span class="s2">"FileHeader"</span><span class="p">)</span>
        <span class="n">header_data</span> <span class="o">=</span> <span class="n">header</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">header_data</span><span class="p">[</span><span class="mi">36</span><span class="p">]</span> <span class="o">&amp;</span> <span class="mi">1</span><span class="p">)</span> <span class="o"></span> <span class="s2">"plain_text"</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="kn">import</span> <span class="nn">pytesseract</span>
                <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                        <span class="s2">"Please install extra dependencies that are required for "</span>
                        <span class="s2">"the ImageReader when text_type is 'plain_text': "</span>
                        <span class="s2">"`pip install pytesseract`"</span>
                    <span class="p">)</span>
                <span class="n">processor</span> <span class="o">=</span> <span class="kc">None</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">pytesseract</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="kn">import</span> <span class="nn">sentencepiece</span>  <span class="c1"># noqa</span>
                    <span class="kn">import</span> <span class="nn">torch</span>  <span class="c1"># noqa</span>
                    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
                    <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">DonutProcessor</span><span class="p">,</span> <span class="n">VisionEncoderDecoderModel</span>
                <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                        <span class="s2">"Please install extra dependencies that are required for "</span>
                        <span class="s2">"the ImageCaptionReader: "</span>
                        <span class="s2">"`pip install torch transformers sentencepiece Pillow`"</span>
                    <span class="p">)</span>

                <span class="n">processor</span> <span class="o">=</span> <span class="n">DonutProcessor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                    <span class="s2">"naver-clova-ix/donut-base-finetuned-cord-v2"</span>
                <span class="p">)</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">VisionEncoderDecoderModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                    <span class="s2">"naver-clova-ix/donut-base-finetuned-cord-v2"</span>
                <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span> <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span> <span class="o">=</span> <span class="n">parse_text</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span> <span class="o">=</span> <span class="n">pytesseract_model_kwargs</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">text_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span><span class="p">:</span>
            <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

            <span class="k">if</span> <span class="n">processor</span><span class="p">:</span>
                <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
                <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

                <span class="c1"># prepare decoder inputs</span>
                <span class="n">task_prompt</span> <span class="o">=</span> <span class="s2">"&lt;s_cord-v2&gt;"</span>
                <span class="n">decoder_input_ids</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">(</span>
                    <span class="n">task_prompt</span><span class="p">,</span> <span class="n">add_special_tokens</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
                <span class="p">)</span><span class="o">.</span><span class="n">input_ids</span>

                <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>

                <span class="n">outputs</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
                    <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                    <span class="n">decoder_input_ids</span><span class="o">=</span><span class="n">decoder_input_ids</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                    <span class="n">max_length</span><span class="o">=</span><span class="n">model</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">max_position_embeddings</span><span class="p">,</span>
                    <span class="n">early_stopping</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">pad_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token_id</span><span class="p">,</span>
                    <span class="n">eos_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token_id</span><span class="p">,</span>
                    <span class="n">use_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">num_beams</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                    <span class="n">bad_words_ids</span><span class="o">=</span><span class="p">[[</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">unk_token_id</span><span class="p">]],</span>
                    <span class="n">return_dict_in_generate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="n">sequence</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">outputs</span><span class="o">.</span><span class="n">sequences</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">sequence</span> <span class="o">=</span> <span class="n">sequence</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
                    <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token</span><span class="p">,</span> <span class="s2">""</span>
                <span class="p">)</span>
                <span class="c1"># remove first task start token</span>
                <span class="n">text_str</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">sequence</span><span class="p">,</span> <span class="n">count</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">pytesseract</span>

                <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">pytesseract</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
                <span class="n">text_str</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span>
                    <span class="n">image</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 72</span>
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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">text_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span><span class="p">:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="k">if</span> <span class="n">processor</span><span class="p">:</span>
            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

            <span class="c1"># prepare decoder inputs</span>
            <span class="n">task_prompt</span> <span class="o">=</span> <span class="s2">"&lt;s_cord-v2&gt;"</span>
            <span class="n">decoder_input_ids</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">(</span>
                <span class="n">task_prompt</span><span class="p">,</span> <span class="n">add_special_tokens</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
            <span class="p">)</span><span class="o">.</span><span class="n">input_ids</span>

            <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>

            <span class="n">outputs</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
                <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                <span class="n">decoder_input_ids</span><span class="o">=</span><span class="n">decoder_input_ids</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                <span class="n">max_length</span><span class="o">=</span><span class="n">model</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">max_position_embeddings</span><span class="p">,</span>
                <span class="n">early_stopping</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">pad_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token_id</span><span class="p">,</span>
                <span class="n">eos_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token_id</span><span class="p">,</span>
                <span class="n">use_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">num_beams</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">bad_words_ids</span><span class="o">=</span><span class="p">[[</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">unk_token_id</span><span class="p">]],</span>
                <span class="n">return_dict_in_generate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">sequence</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">outputs</span><span class="o">.</span><span class="n">sequences</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">sequence</span> <span class="o">=</span> <span class="n">sequence</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
                <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token</span><span class="p">,</span> <span class="s2">""</span>
            <span class="p">)</span>
            <span class="c1"># remove first task start token</span>
            <span class="n">text_str</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">sequence</span><span class="p">,</span> <span class="n">count</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pytesseract</span>

            <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">pytesseract</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
            <span class="n">text_str</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span>
                <span class="n">image</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

ImageTabularChartReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Extract tabular data from a chart or figure.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageTabularChartReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Extract tabular data from a chart or figure.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_output_tokens</span><span class="o">=</span><span class="mi">512</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Generate underlying data table of the figure below:"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">torch</span>
                <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa: F401</span>
                <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">Pix2StructForConditionalGeneration</span><span class="p">,</span>
                    <span class="n">Pix2StructProcessor</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install extra dependencies that are required for "</span>
                    <span class="s2">"the ImageCaptionReader: "</span>
                    <span class="s2">"`pip install torch transformers Pillow`"</span>
                <span class="p">)</span>

            <span class="n">device</span> <span class="o">=</span> <span class="s2">"cuda"</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">"cpu"</span>
            <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">float16</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="n">torch</span><span class="o">.</span><span class="n">float32</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="n">Pix2StructProcessor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"google/deplot"</span><span class="p">)</span>
            <span class="n">model</span> <span class="o">=</span> <span class="n">Pix2StructForConditionalGeneration</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"google/deplot"</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span>
            <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span>
                <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
                <span class="s2">"device"</span><span class="p">:</span> <span class="n">device</span><span class="p">,</span>
                <span class="s2">"dtype"</span><span class="p">:</span> <span class="n">dtype</span><span class="p">,</span>
            <span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span> <span class="o">=</span> <span class="n">max_output_tokens</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="c1"># unconditional image captioning</span>

        <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span><span class="p">)</span>
        <span class="n">text_str</span> <span class="o">=</span> <span class="s2">"Figure or chart with tabular data: "</span> <span class="o">+</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span>
            <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
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
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
    <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="c1"># unconditional image captioning</span>

    <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

    <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span><span class="p">)</span>
    <span class="n">text_str</span> <span class="o">=</span> <span class="s2">"Figure or chart with tabular data: "</span> <span class="o">+</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span>
        <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

ImageVisionLLMReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Caption image using Blip2 (a multimodal VisionLLM similar to GPT4).

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_vision_llm/base.py`

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
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageVisionLLMReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Caption image using Blip2 (a multimodal VisionLLM similar to GPT4).</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Question: describe what you see in this image. Answer:"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">sentencepiece</span>  <span class="c1"># noqa</span>
                <span class="kn">import</span> <span class="nn">torch</span>
                <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
                <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">Blip2ForConditionalGeneration</span><span class="p">,</span> <span class="n">Blip2Processor</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install extra dependencies that are required for "</span>
                    <span class="s2">"the ImageCaptionReader: "</span>
                    <span class="s2">"`pip install torch transformers sentencepiece Pillow`"</span>
                <span class="p">)</span>

            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">float16</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="n">torch</span><span class="o">.</span><span class="n">float32</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="n">Blip2Processor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"Salesforce/blip2-opt-2.7b"</span><span class="p">)</span>
            <span class="n">model</span> <span class="o">=</span> <span class="n">Blip2ForConditionalGeneration</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"Salesforce/blip2-opt-2.7b"</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span>
            <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span>
                <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
                <span class="s2">"device"</span><span class="p">:</span> <span class="n">device</span><span class="p">,</span>
                <span class="s2">"dtype"</span><span class="p">:</span> <span class="n">dtype</span><span class="p">,</span>
            <span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="c1"># unconditional image captioning</span>

        <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
        <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_vision_llm/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">53</span>
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
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
    <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="c1"># unconditional image captioning</span>

    <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

    <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
    <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

MarkdownReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Markdown parser.

Extract text from markdown files. Returns dictionary with keys as headers and values as the text between headers.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
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
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MarkdownReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Markdown parser.</span>

<span class="sd">    Extract text from markdown files.</span>
<span class="sd">    Returns dictionary with keys as headers and values as the text between headers.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">remove_hyperlinks</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">remove_images</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span> <span class="o">=</span> <span class="n">remove_hyperlinks</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span> <span class="o">=</span> <span class="n">remove_images</span>

    <span class="k">def</span> <span class="nf">markdown_to_tups</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">markdown_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Convert a markdown file to a dictionary.</span>

<span class="sd">        The keys are the headers and the values are the text under each header.</span>

<span class="sd">        """</span>
        <span class="n">markdown_tups</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="n">markdown_text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">current_header</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">current_lines</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">in_code_block</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"```"</span><span class="p">):</span>
                <span class="c1"># This is the end of a code block if we are already in it, and vice versa.</span>
                <span class="n">in_code_block</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">in_code_block</span>

            <span class="n">header_match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^#+\s"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">in_code_block</span> <span class="ow">and</span> <span class="n">header_match</span><span class="p">:</span>
                <span class="c1"># Upon first header, skip if current text chunk is empty</span>
                <span class="k">if</span> <span class="n">current_header</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

                <span class="n">current_header</span> <span class="o">=</span> <span class="n">line</span>
                <span class="n">current_lines</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">current_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

        <span class="c1"># Append final text chunk</span>
        <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

        <span class="c1"># Postprocess the tuples before returning</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="p">(</span>
                <span class="n">key</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"#"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span>
                <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">value</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">markdown_tups</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">remove_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Remove images in markdown content."""</span>
        <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"!</span><span class="si">{1}</span><span class="s2">\[\[(.*)\]\]"</span>
        <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">remove_hyperlinks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Remove hyperlinks in markdown content."""</span>
        <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"\[(.*?)\]\((.*?)\)"</span>
        <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="sa">r</span><span class="s2">"\1"</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_init_parser</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the parser with the config."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">parse_tups</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">filepath</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Parse file into tuples."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">LocalFileSystem</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_hyperlinks</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_images</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">markdown_to_tups</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="n">tups</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_tups</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># TODO: don't include headers right now</span>
        <span class="k">for</span> <span class="n">header</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">tups</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">header</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="si">{</span><span class="n">header</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### markdown\_to\_tups [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.markdown_to_tups "Permanent link")

```
markdown_to_tups(markdown_text: str) -> List[Tuple[Optional[str], str]]
```

Convert a markdown file to a dictionary.

The keys are the headers and the values are the text under each header.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
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
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">markdown_to_tups</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">markdown_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Convert a markdown file to a dictionary.</span>

<span class="sd">    The keys are the headers and the values are the text under each header.</span>

<span class="sd">    """</span>
    <span class="n">markdown_tups</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">lines</span> <span class="o">=</span> <span class="n">markdown_text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">current_header</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">current_lines</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">in_code_block</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"```"</span><span class="p">):</span>
            <span class="c1"># This is the end of a code block if we are already in it, and vice versa.</span>
            <span class="n">in_code_block</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">in_code_block</span>

        <span class="n">header_match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^#+\s"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">in_code_block</span> <span class="ow">and</span> <span class="n">header_match</span><span class="p">:</span>
            <span class="c1"># Upon first header, skip if current text chunk is empty</span>
            <span class="k">if</span> <span class="n">current_header</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

            <span class="n">current_header</span> <span class="o">=</span> <span class="n">line</span>
            <span class="n">current_lines</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">current_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

    <span class="c1"># Append final text chunk</span>
    <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

    <span class="c1"># Postprocess the tuples before returning</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="p">(</span>
            <span class="n">key</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"#"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span>
            <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">value</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">markdown_tups</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### remove\_images [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_images "Permanent link")

```
remove_images(content: str) -> str
```

Remove images in markdown content.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">remove_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Remove images in markdown content."""</span>
    <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"!</span><span class="si">{1}</span><span class="s2">\[\[(.*)\]\]"</span>
    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### remove\_hyperlinks [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_hyperlinks "Permanent link")

```
remove_hyperlinks(content: str) -> str
```

Remove hyperlinks in markdown content.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">remove_hyperlinks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Remove hyperlinks in markdown content."""</span>
    <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"\[(.*?)\]\((.*?)\)"</span>
    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="sa">r</span><span class="s2">"\1"</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### parse\_tups [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.parse_tups "Permanent link")

```
parse_tups(filepath: Path, errors: str = 'ignore', fs: Optional[AbstractFileSystem] = None) -> List[Tuple[Optional[str], str]]
```

Parse file into tuples.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse_tups</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">filepath</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Parse file into tuples."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">LocalFileSystem</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_hyperlinks</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_images</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">markdown_to_tups</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file into string.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
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
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file into string."""</span>
    <span class="n">tups</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_tups</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># TODO: don't include headers right now</span>
    <span class="k">for</span> <span class="n">header</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">tups</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">header</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="si">{</span><span class="n">header</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

MboxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Mbox parser.

Extract messages from mailbox files. Returns string including date, subject, sender, receiver and content for each message.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/mbox/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
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
<span class="normal">117</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MboxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Mbox parser.</span>

<span class="sd">    Extract messages from mailbox files.</span>
<span class="sd">    Returns string including date, subject, sender, receiver and</span>
<span class="sd">    content for each message.</span>

<span class="sd">    """</span>

    <span class="n">DEFAULT_MESSAGE_FORMAT</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="p">(</span>
        <span class="s2">"Date: </span><span class="si">{_date}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"From: </span><span class="si">{_from}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"To: </span><span class="si">{_to}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"Subject: </span><span class="si">{_subject}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"Content: </span><span class="si">{_content}</span><span class="s2">"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">max_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">message_format</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_MESSAGE_FORMAT</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`beautifulsoup4` package not found: `pip install beautifulsoup4`"</span>
            <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span> <span class="o">=</span> <span class="n">max_count</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">message_format</span> <span class="o">=</span> <span class="n">message_format</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="c1"># Import required libraries</span>
        <span class="kn">import</span> <span class="nn">mailbox</span>
        <span class="kn">from</span> <span class="nn">email.parser</span> <span class="kn">import</span> <span class="n">BytesParser</span>
        <span class="kn">from</span> <span class="nn">email.policy</span> <span class="kn">import</span> <span class="n">default</span>

        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"fs was specified but MboxReader doesn't support loading "</span>
                <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
            <span class="p">)</span>

        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Load file using mailbox</span>
        <span class="n">bytes_parser</span> <span class="o">=</span> <span class="n">BytesParser</span><span class="p">(</span><span class="n">policy</span><span class="o">=</span><span class="n">default</span><span class="p">)</span><span class="o">.</span><span class="n">parse</span>
        <span class="n">mbox</span> <span class="o">=</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">factory</span><span class="o">=</span><span class="n">bytes_parser</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

        <span class="c1"># Iterate through all messages</span>
        <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">_msg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">mbox</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">msg</span><span class="p">:</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mboxMessage</span> <span class="o">=</span> <span class="n">_msg</span>
                <span class="c1"># Parse multipart messages</span>
                <span class="k">if</span> <span class="n">msg</span><span class="o">.</span><span class="n">is_multipart</span><span class="p">():</span>
                    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">walk</span><span class="p">():</span>
                        <span class="n">ctype</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span>
                        <span class="n">cdispo</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Content-Disposition"</span><span class="p">))</span>
                        <span class="k">if</span> <span class="n">ctype</span> <span class="o"></span> <span class="s2">"text/plain"</span> <span class="ow">and</span> <span class="s2">"attachment"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">cdispo</span><span class="p">:</span>
                        <span class="n">content</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># decode</span>
                        <span class="k">break</span>
            <span class="c1"># Get plain message payload for non-multipart messages</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">msg</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

            <span class="c1"># Parse message HTML content and remove unneeded whitespace</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
            <span class="n">stripped_content</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
            <span class="c1"># Format message to include date, sender, receiver and subject</span>
            <span class="n">msg_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">message_format</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">_date</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"date"</span><span class="p">],</span>
                <span class="n">_from</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"from"</span><span class="p">],</span>
                <span class="n">_to</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"to"</span><span class="p">],</span>
                <span class="n">_subject</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"subject"</span><span class="p">],</span>
                <span class="n">_content</span><span class="o">=</span><span class="n">stripped_content</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="c1"># Add message string to results</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msg_string</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to parse message:</span><span class="se">\n</span><span class="si">{</span><span class="n">_msg</span><span class="si">}</span><span class="se">\n</span><span class="s2"> with exception </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Increment counter and return if max count is met</span>
        <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span><span class="p">:</span>
            <span class="k">break</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

PDFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

PDF parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">27</span>
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
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PDFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PDF parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">return_full_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize PDFReader.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span> <span class="o">=</span> <span class="n">return_full_document</span>

    <span class="nd">@retry</span><span class="p">(</span>
        <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_attempt</span><span class="p">(</span><span class="n">RETRY_TIMES</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pypdf</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"pypdf is required to read PDF files: `pip install pypdf`"</span>
            <span class="p">)</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="c1"># Load the file in memory if the filesystem is not the default one to avoid</span>
            <span class="c1"># issues with pypdf</span>
            <span class="n">stream</span> <span class="o">=</span> <span class="n">fp</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>

            <span class="c1"># Create a PDF object</span>
            <span class="n">pdf</span> <span class="o">=</span> <span class="n">pypdf</span><span class="o">.</span><span class="n">PdfReader</span><span class="p">(</span><span class="n">stream</span><span class="p">)</span>

            <span class="c1"># Get the number of pages in the PDF document</span>
            <span class="n">num_pages</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">)</span>

            <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="c1"># This block returns a whole PDF as a single Document</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                <span class="c1"># Join text extracted from each page</span>
                <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">)</span>
                <span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

            <span class="c1"># This block returns each page of a PDF as its own Document</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Iterate over every page</span>

                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">):</span>
                    <span class="c1"># Extract the text from the page</span>
                    <span class="n">page_text</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span>
                    <span class="n">page_label</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">page_labels</span><span class="p">[</span><span class="n">page</span><span class="p">]</span>

                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_label"</span><span class="p">:</span> <span class="n">page_label</span><span class="p">,</span> <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                    <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                    <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

            <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
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
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@retry</span><span class="p">(</span>
    <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_attempt</span><span class="p">(</span><span class="n">RETRY_TIMES</span><span class="p">),</span>
<span class="p">)</span>
<span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">pypdf</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"pypdf is required to read PDF files: `pip install pypdf`"</span>
        <span class="p">)</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="c1"># Load the file in memory if the filesystem is not the default one to avoid</span>
        <span class="c1"># issues with pypdf</span>
        <span class="n">stream</span> <span class="o">=</span> <span class="n">fp</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>

        <span class="c1"># Create a PDF object</span>
        <span class="n">pdf</span> <span class="o">=</span> <span class="n">pypdf</span><span class="o">.</span><span class="n">PdfReader</span><span class="p">(</span><span class="n">stream</span><span class="p">)</span>

        <span class="c1"># Get the number of pages in the PDF document</span>
        <span class="n">num_pages</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># This block returns a whole PDF as a single Document</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
            <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

            <span class="c1"># Join text extracted from each page</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">)</span>
            <span class="p">)</span>

            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="c1"># This block returns each page of a PDF as its own Document</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Iterate over every page</span>

            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">):</span>
                <span class="c1"># Extract the text from the page</span>
                <span class="n">page_text</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span>
                <span class="n">page_label</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">page_labels</span><span class="p">[</span><span class="n">page</span><span class="p">]</span>

                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_label"</span><span class="p">:</span> <span class="n">page_label</span><span class="p">,</span> <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

PagedCSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Paged CSV parser.

Displayed each row in an LLM-friendly format on a separate document.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `encoding` | `str` | 
Encoding used to open the file. utf-8 by default.



 | `'utf-8'` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/paged_csv/base.py`

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
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PagedCSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Paged CSV parser.</span>

<span class="sd">    Displayed each row in an LLM-friendly format on a separate document.</span>

<span class="sd">    Args:</span>
<span class="sd">        encoding (str): Encoding used to open the file.</span>
<span class="sd">            utf-8 by default.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">encoding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span> <span class="o">=</span> <span class="n">encoding</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">delimiter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">","</span><span class="p">,</span>
        <span class="n">quotechar</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'"'</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">import</span> <span class="nn">csv</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">DictReader</span><span class="p">(</span><span class="n">f</span><span class="o">=</span><span class="n">fp</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">delimiter</span><span class="p">,</span> <span class="n">quotechar</span><span class="o">=</span><span class="n">quotechar</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                        <span class="p">),</span>
                        <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, delimiter: str = ',', quotechar: str = '"') -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/paged_csv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
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
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">delimiter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">","</span><span class="p">,</span>
    <span class="n">quotechar</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'"'</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">import</span> <span class="nn">csv</span>

    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">DictReader</span><span class="p">(</span><span class="n">f</span><span class="o">=</span><span class="n">fp</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">delimiter</span><span class="p">,</span> <span class="n">quotechar</span><span class="o">=</span><span class="n">quotechar</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                    <span class="p">),</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
                <span class="p">)</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

PandasCSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pandas-based CSV parser.

Parses CSVs using the separator detection from Pandas `read_csv`function. If special parameters are required, use the `pandas_config` dict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |
| `col_joiner` | `str` | 

Separator to use for joining cols per row. Set to ", " by default.



 | `', '` |
| `row_joiner` | `str` | 

Separator to use for joining each row. Only used when `concat_rows=True`. Set to "\\n" by default.



 | `'\n'` |
| `pandas_config` | `dict` | 

Options for the `pandas.read_csv` function call. Refer to https://pandas.pydata.org/docs/reference/api/pandas.read\_csv.html for more information. Set to empty dict by default, this means pandas will try to figure out the separators, table head, etc. on its own.



 | `{}` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 61</span>
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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasCSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""Pandas-based CSV parser.</span>

<span class="sd">    Parses CSVs using the separator detection from Pandas `read_csv`function.</span>
<span class="sd">    If special parameters are required, use the `pandas_config` dict.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">        col_joiner (str): Separator to use for joining cols per row.</span>
<span class="sd">            Set to ", " by default.</span>

<span class="sd">        row_joiner (str): Separator to use for joining each row.</span>
<span class="sd">            Only used when `concat_rows=True`.</span>
<span class="sd">            Set to "\n" by default.</span>

<span class="sd">        pandas_config (dict): Options for the `pandas.read_csv` function call.</span>
<span class="sd">            Refer to https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html</span>
<span class="sd">            for more information.</span>
<span class="sd">            Set to empty dict by default, this means pandas will try to figure</span>
<span class="sd">            out the separators, table head, etc. on its own.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">col_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">", "</span><span class="p">,</span>
        <span class="n">row_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">pandas_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span> <span class="o">=</span> <span class="n">col_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span> <span class="o">=</span> <span class="n">row_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span> <span class="o">=</span> <span class="n">pandas_config</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

        <span class="n">text_list</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
            <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
        <span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
            <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

    <span class="n">text_list</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
        <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
    <span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="p">)</span>
        <span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

PandasExcelReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pandas-based Excel parser.

Parses Excel files using the Pandas `read_excel`function. If special parameters are required, use the `pandas_config` dict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |
| `sheet_name` | `str | int | None` | 

Defaults to None, for all sheets, otherwise pass a str or int to specify the sheet to read.



 | `None` |
| `pandas_config` | `dict` | 

Options for the `pandas.read_excel` function call. Refer to https://pandas.pydata.org/docs/reference/api/pandas.read\_excel.html for more information. Set to empty dict by default.



 | `{}` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">132</span>
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
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasExcelReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""Pandas-based Excel parser.</span>

<span class="sd">    Parses Excel files using the Pandas `read_excel`function.</span>
<span class="sd">    If special parameters are required, use the `pandas_config` dict.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">        sheet_name (str | int | None): Defaults to None, for all sheets, otherwise pass a str or int to specify the sheet to read.</span>

<span class="sd">        pandas_config (dict): Options for the `pandas.read_excel` function call.</span>
<span class="sd">            Refer to https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html</span>
<span class="sd">            for more information.</span>
<span class="sd">            Set to empty dict by default.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">sheet_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">pandas_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span> <span class="o">=</span> <span class="n">sheet_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span> <span class="o">=</span> <span class="n">pandas_config</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="n">openpyxl_spec</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span><span class="s2">"openpyxl"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">openpyxl_spec</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install openpyxl to read Excel files. You can install it with 'pip install openpyxl'"</span>
            <span class="p">)</span>

        <span class="c1"># sheet_name of None is all sheets, otherwise indexing starts at 0</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># handle the case where only a single DataFrame is returned</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dfs</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">):</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">dfs</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

            <span class="c1"># Convert DataFrame to list of rows</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">values</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                    <span class="p">]</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">df</span> <span class="ow">in</span> <span class="n">dfs</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
                <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

                <span class="c1"># Convert DataFrame to list of rows</span>
                <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
                <span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                        <span class="p">[</span>
                            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                            <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                        <span class="p">]</span>
                    <span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="n">openpyxl_spec</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span><span class="s2">"openpyxl"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">openpyxl_spec</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install openpyxl to read Excel files. You can install it with 'pip install openpyxl'"</span>
        <span class="p">)</span>

    <span class="c1"># sheet_name of None is all sheets, otherwise indexing starts at 0</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># handle the case where only a single DataFrame is returned</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dfs</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">dfs</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

        <span class="c1"># Convert DataFrame to list of rows</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">values</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                    <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                <span class="p">]</span>
            <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">df</span> <span class="ow">in</span> <span class="n">dfs</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

            <span class="c1"># Convert DataFrame to list of rows</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                    <span class="p">]</span>
                <span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

PptxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Powerpoint parser.

Extract text, caption images, and specify slides.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
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
<span class="normal">122</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PptxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Powerpoint parser.</span>

<span class="sd">    Extract text, caption images, and specify slides.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init parser."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">torch</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">AutoTokenizer</span><span class="p">,</span>
                <span class="n">VisionEncoderDecoderModel</span><span class="p">,</span>
                <span class="n">ViTFeatureExtractor</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install extra dependencies that are required for "</span>
                <span class="s2">"the PptxReader: "</span>
                <span class="s2">"`pip install torch transformers python-pptx Pillow`"</span>
            <span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">VisionEncoderDecoderModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>
        <span class="n">feature_extractor</span> <span class="o">=</span> <span class="n">ViTFeatureExtractor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>
        <span class="n">tokenizer</span> <span class="o">=</span> <span class="n">AutoTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"feature_extractor"</span><span class="p">:</span> <span class="n">feature_extractor</span><span class="p">,</span>
            <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
            <span class="s2">"tokenizer"</span><span class="p">:</span> <span class="n">tokenizer</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">caption_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tmp_image_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate text caption of image."""</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">feature_extractor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"feature_extractor"</span><span class="p">]</span>
        <span class="n">tokenizer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"tokenizer"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">max_length</span> <span class="o">=</span> <span class="mi">16</span>
        <span class="n">num_beams</span> <span class="o">=</span> <span class="mi">4</span>
        <span class="n">gen_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"max_length"</span><span class="p">:</span> <span class="n">max_length</span><span class="p">,</span> <span class="s2">"num_beams"</span><span class="p">:</span> <span class="n">num_beams</span><span class="p">}</span>

        <span class="n">i_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp_image_file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">i_image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">i_image</span> <span class="o">=</span> <span class="n">i_image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">feature_extractor</span><span class="p">(</span>
            <span class="n">images</span><span class="o">=</span><span class="p">[</span><span class="n">i_image</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>
        <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">output_ids</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">pixel_values</span><span class="p">,</span> <span class="o">**</span><span class="n">gen_kwargs</span><span class="p">)</span>

        <span class="n">preds</span> <span class="o">=</span> <span class="n">tokenizer</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">output_ids</span><span class="p">,</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">preds</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">slide</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">presentation</span><span class="o">.</span><span class="n">slides</span><span class="p">):</span>
            <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">Slide #</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">: </span><span class="se">\n</span><span class="s2">"</span>
            <span class="k">for</span> <span class="n">shape</span> <span class="ow">in</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"image"</span><span class="p">):</span>
                    <span class="n">image</span> <span class="o">=</span> <span class="n">shape</span><span class="o">.</span><span class="n">image</span>
                    <span class="c1"># get image "file" contents</span>
                    <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">blob</span>
                    <span class="c1"># temporarily save the image to feed into model</span>
                    <span class="n">f</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">(</span><span class="s2">"wb"</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">)</span>
                        <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                        <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"> Image: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">caption_image</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span>
                    <span class="k">finally</span><span class="p">:</span>
                        <span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">):</span>
                    <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">shape</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### caption\_image [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.caption_image "Permanent link")

```
caption_image(tmp_image_file: str) -> str
```

Generate text caption of image.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

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
<span class="normal">86</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">caption_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tmp_image_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate text caption of image."""</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">feature_extractor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"feature_extractor"</span><span class="p">]</span>
    <span class="n">tokenizer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"tokenizer"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="n">max_length</span> <span class="o">=</span> <span class="mi">16</span>
    <span class="n">num_beams</span> <span class="o">=</span> <span class="mi">4</span>
    <span class="n">gen_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"max_length"</span><span class="p">:</span> <span class="n">max_length</span><span class="p">,</span> <span class="s2">"num_beams"</span><span class="p">:</span> <span class="n">num_beams</span><span class="p">}</span>

    <span class="n">i_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp_image_file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">i_image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">i_image</span> <span class="o">=</span> <span class="n">i_image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">feature_extractor</span><span class="p">(</span>
        <span class="n">images</span><span class="o">=</span><span class="p">[</span><span class="n">i_image</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
    <span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>
    <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="n">output_ids</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">pixel_values</span><span class="p">,</span> <span class="o">**</span><span class="n">gen_kwargs</span><span class="p">)</span>

    <span class="n">preds</span> <span class="o">=</span> <span class="n">tokenizer</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">output_ids</span><span class="p">,</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">preds</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 88</span>
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
<span class="normal">122</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">slide</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">presentation</span><span class="o">.</span><span class="n">slides</span><span class="p">):</span>
        <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">Slide #</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">: </span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">for</span> <span class="n">shape</span> <span class="ow">in</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"image"</span><span class="p">):</span>
                <span class="n">image</span> <span class="o">=</span> <span class="n">shape</span><span class="o">.</span><span class="n">image</span>
                <span class="c1"># get image "file" contents</span>
                <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">blob</span>
                <span class="c1"># temporarily save the image to feed into model</span>
                <span class="n">f</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">(</span><span class="s2">"wb"</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">)</span>
                    <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                    <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"> Image: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">caption_image</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span>
                <span class="k">finally</span><span class="p">:</span>
                    <span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">):</span>
                <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">shape</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

PyMuPDFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Read PDF files using PyMuPDF library.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
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
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PyMuPDFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Read PDF files using PyMuPDF library."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format.</span>

<span class="sd">        Args:</span>
<span class="sd">            file_path (Union[Path, str]): file path of PDF file (accepts string or Path).</span>
<span class="sd">            metadata (bool, optional): if metadata to be included or not. Defaults to True.</span>
<span class="sd">            extra_info (Optional[Dict], optional): extra information related to each document in dict format. Defaults to None.</span>

<span class="sd">        Raises:</span>
<span class="sd">            TypeError: if extra_info is not a dictionary.</span>
<span class="sd">            TypeError: if file_path is not a string or Path.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: list of documents.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">fitz</span>

        <span class="c1"># check if file_path is a string or Path</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"file_path must be a string or Path."</span><span class="p">)</span>

        <span class="c1"># open PDF file</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="n">fitz</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="c1"># if extra_info is not None, check if it is a dictionary</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">extra_info</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"extra_info must be a dictionary."</span><span class="p">)</span>

        <span class="c1"># if metadata is True, add metadata to each document</span>
        <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">extra_info</span><span class="p">:</span>
                <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"total_pages"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

            <span class="c1"># return list of documents</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                        <span class="n">extra_info</span><span class="p">,</span>
                        <span class="o">**</span><span class="p">{</span>
                            <span class="s2">"source"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">page</span><span class="o">.</span><span class="n">number</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">),</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
            <span class="p">]</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
            <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load_data "Permanent link")

```
load_data(file_path: Union[Path, str], metadata: bool = True, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads list of documents from PDF file and also accepts extra information in dict format.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load "Permanent link")

```
load(file_path: Union[Path, str], metadata: bool = True, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads list of documents from PDF file and also accepts extra information in dict format.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file_path` | `Union[Path, str]` | 
file path of PDF file (accepts string or Path).



 | _required_ |
| `metadata` | `bool` | 

if metadata to be included or not. Defaults to True.



 | `True` |
| `extra_info` | `Optional[Dict]` | 

extra information related to each document in dict format. Defaults to None.



 | `None` |

**Raises:**

| Type | Description |
| --- | --- |
| `TypeError` | 
if extra\_info is not a dictionary.



 |
| `TypeError` | 

if file\_path is not a string or Path.



 |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

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
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format.</span>

<span class="sd">    Args:</span>
<span class="sd">        file_path (Union[Path, str]): file path of PDF file (accepts string or Path).</span>
<span class="sd">        metadata (bool, optional): if metadata to be included or not. Defaults to True.</span>
<span class="sd">        extra_info (Optional[Dict], optional): extra information related to each document in dict format. Defaults to None.</span>

<span class="sd">    Raises:</span>
<span class="sd">        TypeError: if extra_info is not a dictionary.</span>
<span class="sd">        TypeError: if file_path is not a string or Path.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: list of documents.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">fitz</span>

    <span class="c1"># check if file_path is a string or Path</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"file_path must be a string or Path."</span><span class="p">)</span>

    <span class="c1"># open PDF file</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="n">fitz</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

    <span class="c1"># if extra_info is not None, check if it is a dictionary</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">extra_info</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"extra_info must be a dictionary."</span><span class="p">)</span>

    <span class="c1"># if metadata is True, add metadata to each document</span>
    <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"total_pages"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="c1"># return list of documents</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                    <span class="n">extra_info</span><span class="p">,</span>
                    <span class="o">**</span><span class="p">{</span>
                        <span class="s2">"source"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">page</span><span class="o">.</span><span class="n">number</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
        <span class="p">]</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

RTFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

RTF (Rich Text Format) Reader. Reads rtf file and convert to Document.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/base.py`

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
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RTFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RTF (Rich Text Format) Reader. Reads rtf file and convert to Document."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">input_file</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">extra_info</span><span class="o">=</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from RTF file.</span>

<span class="sd">        Args:</span>
<span class="sd">            input_file (Path | str): Path for the RTF file.</span>
<span class="sd">            extra_info (Dict[str, Any]): Path for the RTF file.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">striprtf.striprtf</span> <span class="kn">import</span> <span class="n">rtf_to_text</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"striprtf is required to read RTF files."</span><span class="p">)</span>

        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">rtf_to_text</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">())]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader.load_data "Permanent link")

```
load_data(input_file: Union[Path, str], extra_info=Dict[str, Any], **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from RTF file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_file` | `Path | str` | 
Path for the RTF file.



 | _required_ |
| `extra_info` | `Dict[str, Any]` | 

Path for the RTF file.



 | `Dict[str, Any]` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/base.py`

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
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">input_file</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">extra_info</span><span class="o">=</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from RTF file.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_file (Path | str): Path for the RTF file.</span>
<span class="sd">        extra_info (Dict[str, Any]): Path for the RTF file.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">striprtf.striprtf</span> <span class="kn">import</span> <span class="n">rtf_to_text</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"striprtf is required to read RTF files."</span><span class="p">)</span>

    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">rtf_to_text</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">())]</span>
</code></pre></div></td></tr></tbody></table>

UnstructuredReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General unstructured text reader for a variety of files.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
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
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">UnstructuredReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General unstructured text reader for a variety of files."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">allowed_metadata_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize UnstructuredReader.</span>

<span class="sd">        Args:</span>
<span class="sd">            *args (Any): Additional arguments passed to the BaseReader.</span>
<span class="sd">            api_key (str, optional): API key for accessing the Unstructured.io API. If provided, the reader will use the API for parsing files. Defaults to None.</span>
<span class="sd">            url (str, optional): URL for the Unstructured.io API. If not provided and an api_key is given, defaults to "http://localhost:8000". Ignored if api_key is not provided. Defaults to None.</span>
<span class="sd">            allowed_metadata_types (Optional[Tuple], optional): Tuple of types that are allowed in the metadata. Defaults to (str, int, float, type(None)).</span>
<span class="sd">            excluded_metadata_keys (Optional[Set], optional): Set of metadata keys to exclude from the final document. Defaults to {"orig_elements"}.</span>

<span class="sd">        Attributes:</span>
<span class="sd">            api_key (str or None): Stores the API key.</span>
<span class="sd">            use_api (bool): Indicates whether to use the API for parsing files, based on the presence of the api_key.</span>
<span class="sd">            url (str or None): URL for the Unstructured.io API if using the API.</span>
<span class="sd">            allowed_metadata_types (Tuple): Tuple of types that are allowed in the metadata.</span>
<span class="sd">            excluded_metadata_keys (Set): Set of metadata keys to exclude from the final document.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>  <span class="c1"># not passing kwargs to parent bc it cannot accept it</span>

        <span class="k">if</span> <span class="n">Element</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Unstructured is not installed. Please install it using 'pip install -U unstructured'."</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span> <span class="ow">or</span> <span class="s2">"http://localhost:8000"</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_metadata_types</span> <span class="o">=</span> <span class="n">allowed_metadata_types</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="nb">str</span><span class="p">,</span>
            <span class="nb">int</span><span class="p">,</span>
            <span class="nb">float</span><span class="p">,</span>
            <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">excluded_metadata_keys</span> <span class="o">=</span> <span class="n">excluded_metadata_keys</span> <span class="ow">or</span> <span class="p">{</span><span class="s2">"orig_elements"</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_api</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Set the server url and api key."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data using Unstructured.io.</span>

<span class="sd">        Depending on the configuration, if url is set or use_api is True,</span>
<span class="sd">        it'll parse the file using an API call, otherwise it parses it locally.</span>
<span class="sd">        extra_info is extended by the returned metadata if split_documents is True.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">            unstructured_kwargs (Optional[Dict]): Additional arguments for unstructured partitioning.</span>
<span class="sd">            document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">            extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">            split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">            excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of parsed documents.</span>
<span class="sd">        """</span>
        <span class="n">unstructured_kwargs</span> <span class="o">=</span> <span class="n">unstructured_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">unstructured_kwargs</span> <span class="k">else</span> <span class="p">{}</span>

        <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_partition_elements</span><span class="p">(</span><span class="n">unstructured_kwargs</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_documents</span><span class="p">(</span>
            <span class="n">elements</span><span class="p">,</span>
            <span class="n">document_kwargs</span><span class="p">,</span>
            <span class="n">extra_info</span><span class="p">,</span>
            <span class="n">split_documents</span><span class="p">,</span>
            <span class="n">excluded_metadata_keys</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_partition_elements</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Partition the elements from the file or via API.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">            unstructured_kwargs (Dict): Additional arguments for unstructured partitioning.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Element]: List of partitioned elements.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">file</span><span class="p">:</span>
            <span class="n">unstructured_kwargs</span><span class="p">[</span><span class="s2">"filename"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">unstructured.partition.api</span> <span class="kn">import</span> <span class="n">partition_via_api</span>

            <span class="k">return</span> <span class="n">partition_via_api</span><span class="p">(</span>
                <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
                <span class="n">api_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">+</span> <span class="s2">"/general/v0/general"</span><span class="p">,</span>
                <span class="o">**</span><span class="n">unstructured_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">unstructured.partition.auto</span> <span class="kn">import</span> <span class="n">partition</span>

            <span class="k">return</span> <span class="n">partition</span><span class="p">(</span><span class="o">**</span><span class="n">unstructured_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">],</span>
        <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
        <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">],</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create documents from partitioned elements.</span>

<span class="sd">        Args:</span>
<span class="sd">            elements (List): List of partitioned elements.</span>
<span class="sd">            document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">            extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">            split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">            excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of parsed documents.</span>
<span class="sd">        """</span>
        <span class="n">document_kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">document_kwargs</span> <span class="k">else</span> <span class="p">{}</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">split_documents</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">sequence_number</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">elements</span><span class="p">):</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span>

                <span class="n">excluded_keys</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span>
                    <span class="n">excluded_metadata_keys</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">excluded_metadata_keys</span>
                <span class="p">)</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">extra_info</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">extra_info</span> <span class="k">else</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">excluded_keys</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
                            <span class="n">value</span>
                            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">allowed_metadata_types</span><span class="p">)</span>
                            <span class="k">else</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
                        <span class="p">)</span>

                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"extra_info"</span><span class="p">]</span> <span class="o">=</span> <span class="n">metadata</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">id_to_hash</span><span class="p">(</span><span class="n">sequence_number</span><span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">text_chunks</span> <span class="o">=</span> <span class="p">[</span><span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">())</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">elements</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_chunks</span><span class="p">)</span>

            <span class="n">kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="o">=</span> <span class="n">text</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="n">extra_info</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">extra_info</span> <span class="k">else</span> <span class="p">{}</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">filename</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">filename</span>
                <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"filename"</span><span class="p">]</span> <span class="o">=</span> <span class="n">filename</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"extra_info"</span><span class="p">]</span> <span class="o">=</span> <span class="n">metadata</span>

            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### from\_api `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.from_api "Permanent link")

```
from_api(api_key: str, url: str = None)
```

Set the server url and api key.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_api</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Set the server url and api key."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.load_data "Permanent link")

```
load_data(file: Optional[Path] = None, unstructured_kwargs: Optional[Dict] = None, document_kwargs: Optional[Dict] = None, extra_info: Optional[Dict] = None, split_documents: Optional[bool] = False, excluded_metadata_keys: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data using Unstructured.io.

Depending on the configuration, if url is set or use\_api is True, it'll parse the file using an API call, otherwise it parses it locally. extra\_info is extended by the returned metadata if split\_documents is True.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Optional[Path]` | 
Path to the file to be loaded.



 | `None` |
| `unstructured_kwargs` | `Optional[Dict]` | 

Additional arguments for unstructured partitioning.



 | `None` |
| `document_kwargs` | `Optional[Dict]` | 

Additional arguments for document creation.



 | `None` |
| `extra_info` | `Optional[Dict]` | 

Extra information to add to the document metadata.



 | `None` |
| `split_documents` | `Optional[bool]` | 

Whether to split the documents.



 | `False` |
| `excluded_metadata_keys` | `Optional[List[str]]` | 

Keys to exclude from the metadata.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of parsed documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 73</span>
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
<span class="normal">109</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data using Unstructured.io.</span>

<span class="sd">    Depending on the configuration, if url is set or use_api is True,</span>
<span class="sd">    it'll parse the file using an API call, otherwise it parses it locally.</span>
<span class="sd">    extra_info is extended by the returned metadata if split_documents is True.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">        unstructured_kwargs (Optional[Dict]): Additional arguments for unstructured partitioning.</span>
<span class="sd">        document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">        extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">        split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">        excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of parsed documents.</span>
<span class="sd">    """</span>
    <span class="n">unstructured_kwargs</span> <span class="o">=</span> <span class="n">unstructured_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">unstructured_kwargs</span> <span class="k">else</span> <span class="p">{}</span>

    <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_partition_elements</span><span class="p">(</span><span class="n">unstructured_kwargs</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_documents</span><span class="p">(</span>
        <span class="n">elements</span><span class="p">,</span>
        <span class="n">document_kwargs</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">,</span>
        <span class="n">split_documents</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

VideoAudioReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Video audio parser.

Extract text from transcript of video/audio files.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/video_audio/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
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
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VideoAudioReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Video audio parser.</span>

<span class="sd">    Extract text from transcript of video/audio files.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">model_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"base"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init parser."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model_version</span> <span class="o">=</span> <span class="n">model_version</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">whisper</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install OpenAI whisper model "</span>
                <span class="s2">"'pip install git+https://github.com/openai/whisper.git' "</span>
                <span class="s2">"to use the model"</span>
            <span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">whisper</span><span class="o">.</span><span class="n">load_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_version</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">import</span> <span class="nn">whisper</span>

        <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"mp4"</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">pydub</span> <span class="kn">import</span> <span class="n">AudioSegment</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install pydub 'pip install pydub' "</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
                <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                    <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># open file</span>
                <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>

            <span class="c1"># Extract audio from video</span>
            <span class="n">audio</span> <span class="o">=</span> <span class="n">video</span><span class="o">.</span><span class="n">split_to_mono</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

            <span class="n">file_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)[:</span><span class="o">-</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="s2">".mp3"</span>
            <span class="c1"># export file</span>
            <span class="n">audio</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="n">file_str</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">whisper</span><span class="o">.</span><span class="n">Whisper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">transcribe</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>

        <span class="n">transcript</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/video_audio/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
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
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">import</span> <span class="nn">whisper</span>

    <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"mp4"</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pydub</span> <span class="kn">import</span> <span class="n">AudioSegment</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install pydub 'pip install pydub' "</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># open file</span>
            <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>

        <span class="c1"># Extract audio from video</span>
        <span class="n">audio</span> <span class="o">=</span> <span class="n">video</span><span class="o">.</span><span class="n">split_to_mono</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

        <span class="n">file_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)[:</span><span class="o">-</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="s2">".mp3"</span>
        <span class="c1"># export file</span>
        <span class="n">audio</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="n">file_str</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>

    <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">whisper</span><span class="o">.</span><span class="n">Whisper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">transcribe</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>

    <span class="n">transcript</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

XMLReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

XML reader.

Reads XML documents with options to help suss out relationships between nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tree_level_split` | `int` | 
From which level in the xml tree we split documents,



 | `0` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/xml/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
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
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">XMLReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""XML reader.</span>

<span class="sd">    Reads XML documents with options to help suss out relationships between nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        tree_level_split (int): From which level in the xml tree we split documents,</span>
<span class="sd">        the default level is the root which is level 0</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tree_level_split</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with arguments."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree_level_split</span> <span class="o">=</span> <span class="n">tree_level_split</span>

    <span class="k">def</span> <span class="nf">_parse_xmlelt_to_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">root</span><span class="p">:</span> <span class="n">ET</span><span class="o">.</span><span class="n">Element</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse the xml object into a list of Documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            root: The XML Element to be converted.</span>
<span class="sd">            extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: The documents.</span>
<span class="sd">        """</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">_get_leaf_nodes_up_to_level</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree_level_split</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">tostring</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf8"</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^&lt;\?xml.*"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input file.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path to the input file.</span>
<span class="sd">            extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_xmlelt_to_document</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">(),</span> <span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Path` | 
Path to the input file.



 | _required_ |
| `extra_info` | `Optional[Dict]` | 

Additional information. Default is None.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/xml/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">75</span>
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
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input file.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path to the input file.</span>
<span class="sd">        extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_xmlelt_to_document</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">(),</span> <span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Feishu wiki](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_wiki/)[Next Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)
