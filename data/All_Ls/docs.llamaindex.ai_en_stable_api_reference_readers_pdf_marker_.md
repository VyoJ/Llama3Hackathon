Title: Pdf marker - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/

Markdown Content:
Pdf marker - LlamaIndex


PDFMarkerReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/#llama_index.readers.pdf_marker.PDFMarkerReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

PDF Marker Reader. Reads a pdf to markdown format and tables with layout.

Source code in `llama-index-integrations/readers/llama-index-readers-pdf-marker/llama_index/readers/pdf_marker/base.py`

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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PDFMarkerReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    PDF Marker Reader. Reads a pdf to markdown format and tables with layout.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">max_pages</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">langs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_multiplier</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">start_page</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from PDF</span>
<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path for the PDF file.</span>
<span class="sd">            max_pages (int): is the maximum number of pages to process. Omit this to convert the entire document.</span>
<span class="sd">            langs (List[str]): List of languages to use for OCR. See supported languages : https://github.com/VikParuchuri/surya/blob/master/surya/languages.py</span>
<span class="sd">            batch_multiplier (int): is how much to multiply default batch sizes by if you have extra VRAM. Higher numbers will take more VRAM, but process faster. Set to 2 by default. The default batch sizes will take ~3GB of VRAM.</span>
<span class="sd">            start_page (int): Start page for conversion.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">marker.convert</span> <span class="kn">import</span> <span class="n">convert_single_pdf</span>
        <span class="kn">from</span> <span class="nn">marker.models</span> <span class="kn">import</span> <span class="n">load_all_models</span>

        <span class="n">model_lst</span> <span class="o">=</span> <span class="n">load_all_models</span><span class="p">()</span>
        <span class="n">full_text</span><span class="p">,</span> <span class="n">images</span><span class="p">,</span> <span class="n">out_meta</span> <span class="o">=</span> <span class="n">convert_single_pdf</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">model_lst</span><span class="p">,</span>
            <span class="n">max_pages</span><span class="o">=</span><span class="n">max_pages</span><span class="p">,</span>
            <span class="n">langs</span><span class="o">=</span><span class="n">langs</span><span class="p">,</span>
            <span class="n">batch_multiplier</span><span class="o">=</span><span class="n">batch_multiplier</span><span class="p">,</span>
            <span class="n">start_page</span><span class="o">=</span><span class="n">start_page</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">full_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">doc</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/#llama_index.readers.pdf_marker.PDFMarkerReader.load_data "Permanent link")

```
load_data(file: Path, max_pages: int = None, langs: List[str] = None, batch_multiplier: int = 2, start_page: int = None, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from PDF Args: file (Path): Path for the PDF file. max\_pages (int): is the maximum number of pages to process. Omit this to convert the entire document. langs (List\[str\]): List of languages to use for OCR. See supported languages : https://github.com/VikParuchuri/surya/blob/master/surya/languages.py batch\_multiplier (int): is how much to multiply default batch sizes by if you have extra VRAM. Higher numbers will take more VRAM, but process faster. Set to 2 by default. The default batch sizes will take ~3GB of VRAM. start\_page (int): Start page for conversion.

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-pdf-marker/llama_index/readers/pdf_marker/base.py`

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
<span class="normal">53</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">max_pages</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">langs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">batch_multiplier</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">start_page</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from PDF</span>
<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path for the PDF file.</span>
<span class="sd">        max_pages (int): is the maximum number of pages to process. Omit this to convert the entire document.</span>
<span class="sd">        langs (List[str]): List of languages to use for OCR. See supported languages : https://github.com/VikParuchuri/surya/blob/master/surya/languages.py</span>
<span class="sd">        batch_multiplier (int): is how much to multiply default batch sizes by if you have extra VRAM. Higher numbers will take more VRAM, but process faster. Set to 2 by default. The default batch sizes will take ~3GB of VRAM.</span>
<span class="sd">        start_page (int): Start page for conversion.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">marker.convert</span> <span class="kn">import</span> <span class="n">convert_single_pdf</span>
    <span class="kn">from</span> <span class="nn">marker.models</span> <span class="kn">import</span> <span class="n">load_all_models</span>

    <span class="n">model_lst</span> <span class="o">=</span> <span class="n">load_all_models</span><span class="p">()</span>
    <span class="n">full_text</span><span class="p">,</span> <span class="n">images</span><span class="p">,</span> <span class="n">out_meta</span> <span class="o">=</span> <span class="n">convert_single_pdf</span><span class="p">(</span>
        <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
        <span class="n">model_lst</span><span class="p">,</span>
        <span class="n">max_pages</span><span class="o">=</span><span class="n">max_pages</span><span class="p">,</span>
        <span class="n">langs</span><span class="o">=</span><span class="n">langs</span><span class="p">,</span>
        <span class="n">batch_multiplier</span><span class="o">=</span><span class="n">batch_multiplier</span><span class="p">,</span>
        <span class="n">start_page</span><span class="o">=</span><span class="n">start_page</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">full_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">doc</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/)[Next Pdf table](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/)
