Title: Pdb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/

Markdown Content:
Pdb - LlamaIndex


PdbAbstractReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/#llama_index.readers.pdb.PdbAbstractReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Protein Data Bank entries' primary citation abstract reader.

Source code in `llama-index-integrations/readers/llama-index-readers-pdb/llama_index/readers/pdb/base.py`

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
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PdbAbstractReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Protein Data Bank entries' primary citation abstract reader."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pdb_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from RCSB or EBI REST API.</span>

<span class="sd">        Args:</span>
<span class="sd">            pdb_ids (List[str]): List of PDB ids \</span>
<span class="sd">                for which primary citation abstract are to be read.</span>
<span class="sd">        """</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">pdb_id</span> <span class="ow">in</span> <span class="n">pdb_ids</span><span class="p">:</span>
            <span class="n">title</span><span class="p">,</span> <span class="n">abstracts</span> <span class="o">=</span> <span class="n">get_pdb_abstract</span><span class="p">(</span><span class="n">pdb_id</span><span class="p">)</span>
            <span class="n">primary_citation</span> <span class="o">=</span> <span class="n">abstracts</span><span class="p">[</span><span class="n">title</span><span class="p">]</span>
            <span class="n">abstract</span> <span class="o">=</span> <span class="n">primary_citation</span><span class="p">[</span><span class="s2">"abstract"</span><span class="p">]</span>
            <span class="n">abstract_text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">),</span> <span class="nb">str</span><span class="p">(</span><span class="n">v</span><span class="p">)])</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">abstract</span><span class="o">.</span><span class="n">items</span><span class="p">()]</span>
            <span class="p">)</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">abstract_text</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"pdb_id"</span><span class="p">:</span> <span class="n">pdb_id</span><span class="p">,</span> <span class="s2">"primary_citation"</span><span class="p">:</span> <span class="n">primary_citation</span><span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/#llama_index.readers.pdb.PdbAbstractReader.load_data "Permanent link")

```
load_data(pdb_ids: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from RCSB or EBI REST API.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pdb_ids` | `List[str]` | 
List of PDB ids for which primary citation abstract are to be read.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-pdb/llama_index/readers/pdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
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
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pdb_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from RCSB or EBI REST API.</span>

<span class="sd">    Args:</span>
<span class="sd">        pdb_ids (List[str]): List of PDB ids \</span>
<span class="sd">            for which primary citation abstract are to be read.</span>
<span class="sd">    """</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">pdb_id</span> <span class="ow">in</span> <span class="n">pdb_ids</span><span class="p">:</span>
        <span class="n">title</span><span class="p">,</span> <span class="n">abstracts</span> <span class="o">=</span> <span class="n">get_pdb_abstract</span><span class="p">(</span><span class="n">pdb_id</span><span class="p">)</span>
        <span class="n">primary_citation</span> <span class="o">=</span> <span class="n">abstracts</span><span class="p">[</span><span class="n">title</span><span class="p">]</span>
        <span class="n">abstract</span> <span class="o">=</span> <span class="n">primary_citation</span><span class="p">[</span><span class="s2">"abstract"</span><span class="p">]</span>
        <span class="n">abstract_text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">),</span> <span class="nb">str</span><span class="p">(</span><span class="n">v</span><span class="p">)])</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">abstract</span><span class="o">.</span><span class="n">items</span><span class="p">()]</span>
        <span class="p">)</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">abstract_text</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"pdb_id"</span><span class="p">:</span> <span class="n">pdb_id</span><span class="p">,</span> <span class="s2">"primary_citation"</span><span class="p">:</span> <span class="n">primary_citation</span><span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pathway](https://docs.llamaindex.ai/en/stable/api_reference/readers/pathway/)[Next Pdf marker](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/)
