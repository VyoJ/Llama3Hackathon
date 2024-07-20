Title: Nougat ocr - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/

Markdown Content:
Nougat ocr - LlamaIndex


PDFNougatOCR [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/#llama_index.readers.nougat_ocr.PDFNougatOCR "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Source code in `llama-index-integrations/readers/llama-index-readers-nougat-ocr/llama_index/readers/nougat_ocr/base.py`

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
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PDFNougatOCR</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">nougat_ocr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Path</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">cli_command</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"nougat"</span><span class="p">,</span> <span class="s2">"--markdown"</span><span class="p">,</span> <span class="s2">"pdf"</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">),</span> <span class="s2">"--out"</span><span class="p">,</span> <span class="s2">"output"</span><span class="p">]</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">cli_command</span><span class="p">,</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="n">result</span><span class="o">.</span><span class="n">check_returncode</span><span class="p">()</span>
            <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">stdout</span>

        <span class="k">except</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">CalledProcessError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Nougat OCR command failed with return code </span><span class="si">{</span><span class="n">e</span><span class="o">.</span><span class="n">returncode</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">e</span><span class="o">.</span><span class="n">stderr</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">"Nougat OCR command failed."</span><span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file_path</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># Ensure the 'output' folder exists or create it if not</span>
            <span class="n">output_folder</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s2">"output"</span><span class="p">)</span>
            <span class="n">output_folder</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

            <span class="c1"># Call the method to run the Nougat OCR command</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">nougat_ocr</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

            <span class="c1"># Rest of your code for reading and processing the output</span>
            <span class="n">file_path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
            <span class="n">output_path</span> <span class="o">=</span> <span class="n">output_folder</span> <span class="o">/</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">file_path</span><span class="o">.</span><span class="n">stem</span><span class="si">}</span><span class="s2">.mmd"</span>
            <span class="k">with</span> <span class="n">output_path</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"r"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

            <span class="n">content</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">content</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="sa">r</span><span class="s2">"\("</span><span class="p">,</span> <span class="s2">"$"</span><span class="p">)</span>
                <span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="sa">r</span><span class="s2">"\)"</span><span class="p">,</span> <span class="s2">"$"</span><span class="p">)</span>
                <span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="sa">r</span><span class="s2">"\["</span><span class="p">,</span> <span class="s2">"$$"</span><span class="p">)</span>
                <span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="sa">r</span><span class="s2">"\]"</span><span class="p">,</span> <span class="s2">"$$"</span><span class="p">)</span>
            <span class="p">)</span>

            <span class="c1"># Need to chunk before creating Document</span>

            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">)]</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"An error occurred while processing the PDF: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Notion](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/)[Next Obsidian](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/)
