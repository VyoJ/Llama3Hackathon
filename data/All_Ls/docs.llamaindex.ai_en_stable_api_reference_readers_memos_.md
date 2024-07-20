Title: Memos - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/

Markdown Content:
Memos - LlamaIndex


Init file.

MemosReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/#llama_index.readers.memos.MemosReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Memos reader.

Reads content from an Memos.

Source code in `llama-index-integrations/readers/llama-index-readers-memos/llama_index/readers/memos/base.py`

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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MemosReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Memos reader.</span>

<span class="sd">    Reads content from an Memos.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"https://demo.usememos.com/"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_memoUrl</span> <span class="o">=</span> <span class="n">urljoin</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="s2">"api/memo"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from RSS feeds.</span>

<span class="sd">        Args:</span>
<span class="sd">            params (Dict): Filtering parameters.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>

<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">requests</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">realUrl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memoUrl</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">params</span><span class="p">:</span>
            <span class="n">realUrl</span> <span class="o">=</span> <span class="n">urljoin</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memoUrl</span><span class="p">,</span> <span class="s2">"all"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">req</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">realUrl</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
            <span class="n">res</span> <span class="o">=</span> <span class="n">req</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Your Memo URL is not valid"</span><span class="p">)</span>

        <span class="k">if</span> <span class="s2">"data"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">res</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid Memo response"</span><span class="p">)</span>

        <span class="n">memos</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">memo</span> <span class="ow">in</span> <span class="n">memos</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"creator"</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"creator"</span><span class="p">],</span>
                <span class="s2">"resource_list"</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"resourceList"</span><span class="p">],</span>
                <span class="nb">id</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
            <span class="p">}</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/#llama_index.readers.memos.MemosReader.load_data "Permanent link")

```
load_data(params: Dict = {}) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from RSS feeds.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `params` | `Dict` | 
Filtering parameters.



 | `{}` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-memos/llama_index/readers/memos/base.py`

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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from RSS feeds.</span>

<span class="sd">    Args:</span>
<span class="sd">        params (Dict): Filtering parameters.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">requests</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">realUrl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_memoUrl</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">params</span><span class="p">:</span>
        <span class="n">realUrl</span> <span class="o">=</span> <span class="n">urljoin</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_memoUrl</span><span class="p">,</span> <span class="s2">"all"</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">req</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">realUrl</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
        <span class="n">res</span> <span class="o">=</span> <span class="n">req</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Your Memo URL is not valid"</span><span class="p">)</span>

    <span class="k">if</span> <span class="s2">"data"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">res</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid Memo response"</span><span class="p">)</span>

    <span class="n">memos</span> <span class="o">=</span> <span class="n">res</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
    <span class="k">for</span> <span class="n">memo</span> <span class="ow">in</span> <span class="n">memos</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"content"</span><span class="p">]</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"creator"</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"creator"</span><span class="p">],</span>
            <span class="s2">"resource_list"</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"resourceList"</span><span class="p">],</span>
            <span class="nb">id</span><span class="p">:</span> <span class="n">memo</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
        <span class="p">}</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mbox](https://docs.llamaindex.ai/en/stable/api_reference/readers/mbox/)[Next Metal](https://docs.llamaindex.ai/en/stable/api_reference/readers/metal/)
