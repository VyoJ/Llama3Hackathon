Title: Pdf table - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/

Markdown Content:
Pdf table - LlamaIndex


PDFTableReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/#llama_index.readers.pdf_table.PDFTableReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

PDF Table Reader. Reads table from PDF.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `row_separator` | `str` | 
Row separator used to join rows of a DataFrame.



 | `'\n'` |
| `col_separator` | `str` | 

Col separator used to join columns of a DataFrame.



 | `', '` |

Source code in `llama-index-integrations/readers/llama-index-readers-pdf-table/llama_index/readers/pdf_table/base.py`

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
<span class="normal">63</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PDFTableReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PDF Table Reader. Reads table from PDF.</span>

<span class="sd">    Args:</span>
<span class="sd">        row_separator (str): Row separator used to join rows of a DataFrame.</span>
<span class="sd">        col_separator (str): Col separator used to join columns of a DataFrame.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">row_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">col_separator</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">", "</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_row_separator</span> <span class="o">=</span> <span class="n">row_separator</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_col_separator</span> <span class="o">=</span> <span class="n">col_separator</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">pages</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"1"</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data and extract table from PDF file.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path for the PDF file.</span>
<span class="sd">            pages (str): Pages to read tables from.</span>
<span class="sd">            extra_info (Optional[Dict]): Extra information.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">camelot</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">tables</span> <span class="o">=</span> <span class="n">camelot</span><span class="o">.</span><span class="n">read_pdf</span><span class="p">(</span><span class="n">filepath</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">pages</span><span class="o">=</span><span class="n">pages</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="n">tables</span><span class="p">:</span>
            <span class="n">document</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dataframe_to_document</span><span class="p">(</span><span class="n">df</span><span class="o">=</span><span class="n">table</span><span class="o">.</span><span class="n">df</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_dataframe_to_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
        <span class="n">df_list</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
            <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_separator</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
        <span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_separator</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">df_list</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/#llama_index.readers.pdf_table.PDFTableReader.load_data "Permanent link")

```
load_data(file: Path, pages: str = '1', extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data and extract table from PDF file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Path` | 
Path for the PDF file.



 | _required_ |
| `pages` | `str` | 

Pages to read tables from.



 | `'1'` |
| `extra_info` | `Optional[Dict]` | 

Extra information.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-pdf-table/llama_index/readers/pdf_table/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">30</span>
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
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">pages</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"1"</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data and extract table from PDF file.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path for the PDF file.</span>
<span class="sd">        pages (str): Pages to read tables from.</span>
<span class="sd">        extra_info (Optional[Dict]): Extra information.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">camelot</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">tables</span> <span class="o">=</span> <span class="n">camelot</span><span class="o">.</span><span class="n">read_pdf</span><span class="p">(</span><span class="n">filepath</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">pages</span><span class="o">=</span><span class="n">pages</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="n">tables</span><span class="p">:</span>
        <span class="n">document</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dataframe_to_document</span><span class="p">(</span><span class="n">df</span><span class="o">=</span><span class="n">table</span><span class="o">.</span><span class="n">df</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pdf marker](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/)[Next Pebblo](https://docs.llamaindex.ai/en/stable/api_reference/readers/pebblo/)
