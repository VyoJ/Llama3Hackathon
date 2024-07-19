Title: Whatsapp - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/

Markdown Content:
Whatsapp - LlamaIndex


WhatsappChatLoader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/#llama_index.readers.whatsapp.WhatsappChatLoader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Whatsapp chat data loader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str` | 
Path to Whatsapp chat file.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-whatsapp/llama_index/readers/whatsapp/base.py`

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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WhatsappChatLoader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Whatsapp chat data loader.</span>

<span class="sd">    Args:</span>
<span class="sd">        path (str): Path to Whatsapp chat file.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with path."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_path</span> <span class="o">=</span> <span class="n">path</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Parse Whatsapp file into Documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">chatminer.chatparsers</span> <span class="kn">import</span> <span class="n">WhatsAppParser</span>

        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_path</span><span class="p">)</span>

        <span class="n">parser</span> <span class="o">=</span> <span class="n">WhatsAppParser</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">parser</span><span class="o">.</span><span class="n">parse_file</span><span class="p">()</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parsed_messages</span><span class="o">.</span><span class="n">get_df</span><span class="p">()</span>

        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Number of messages: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">n</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">itertuples</span><span class="p">():</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"source"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">".txt"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
                <span class="s2">"author"</span><span class="p">:</span> <span class="n">row</span><span class="o">.</span><span class="n">author</span><span class="p">,</span>
                <span class="s2">"timestamp"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">timestamp</span><span class="p">),</span>
            <span class="p">}</span>

            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">timestamp</span><span class="p">)</span>
                    <span class="o">+</span> <span class="s2">" "</span>
                    <span class="o">+</span> <span class="n">row</span><span class="o">.</span><span class="n">author</span>
                    <span class="o">+</span> <span class="s2">":"</span>
                    <span class="o">+</span> <span class="s2">" "</span>
                    <span class="o">+</span> <span class="n">row</span><span class="o">.</span><span class="n">message</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

            <span class="n">n</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Added </span><span class="si">{</span><span class="n">n</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span><span class="si">}</span><span class="s2"> messages."</span><span class="p">)</span>

        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Document creation for </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is complete."</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/#llama_index.readers.whatsapp.WhatsappChatLoader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse Whatsapp file into Documents.

Source code in `llama-index-integrations/readers/llama-index-readers-whatsapp/llama_index/readers/whatsapp/base.py`

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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Parse Whatsapp file into Documents.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">chatminer.chatparsers</span> <span class="kn">import</span> <span class="n">WhatsAppParser</span>

    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_path</span><span class="p">)</span>

    <span class="n">parser</span> <span class="o">=</span> <span class="n">WhatsAppParser</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">parse_file</span><span class="p">()</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parsed_messages</span><span class="o">.</span><span class="n">get_df</span><span class="p">()</span>

    <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Number of messages: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>

    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">n</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">itertuples</span><span class="p">():</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"source"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">".txt"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
            <span class="s2">"author"</span><span class="p">:</span> <span class="n">row</span><span class="o">.</span><span class="n">author</span><span class="p">,</span>
            <span class="s2">"timestamp"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">timestamp</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">timestamp</span><span class="p">)</span>
                <span class="o">+</span> <span class="s2">" "</span>
                <span class="o">+</span> <span class="n">row</span><span class="o">.</span><span class="n">author</span>
                <span class="o">+</span> <span class="s2">":"</span>
                <span class="o">+</span> <span class="s2">" "</span>
                <span class="o">+</span> <span class="n">row</span><span class="o">.</span><span class="n">message</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">n</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Added </span><span class="si">{</span><span class="n">n</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span><span class="si">}</span><span class="s2"> messages."</span><span class="p">)</span>

    <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Document creation for </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is complete."</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Web](https://docs.llamaindex.ai/en/stable/api_reference/readers/web/)[Next Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/)
