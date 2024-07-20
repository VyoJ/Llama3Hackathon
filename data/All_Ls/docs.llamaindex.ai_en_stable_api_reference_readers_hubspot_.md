Title: Hubspot - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/

Markdown Content:
Hubspot - LlamaIndex


HubspotReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/#llama_index.readers.hubspot.HubspotReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Hubspot reader. Reads data from a Hubspot account.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `access_token(str)` |  | 
Hubspot API key.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-hubspot/llama_index/readers/hubspot/base.py`

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
<span class="normal">44</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HubspotReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hubspot reader. Reads data from a Hubspot account.</span>

<span class="sd">    Args:</span>
<span class="sd">        access_token(str): Hubspot API key.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">access_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Hubspot reader."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span> <span class="o">=</span> <span class="n">access_token</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load deals, contacts and companies data from Hubspot.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents, where each document represensts a list of Hubspot objects</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">hubspot</span> <span class="kn">import</span> <span class="n">HubSpot</span>

        <span class="n">api_client</span> <span class="o">=</span> <span class="n">HubSpot</span><span class="p">(</span><span class="n">access_token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">)</span>
        <span class="n">all_deals</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">deals</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
        <span class="n">all_contacts</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">contacts</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
        <span class="n">all_companies</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">companies</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_deals</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"deals"</span><span class="p">}</span>
            <span class="p">),</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_contacts</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"contacts"</span><span class="p">},</span>
            <span class="p">),</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_companies</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"companies"</span><span class="p">},</span>
            <span class="p">),</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/#llama_index.readers.hubspot.HubspotReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load deals, contacts and companies data from Hubspot.

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents, where each document represensts a list of Hubspot objects



 |

Source code in `llama-index-integrations/readers/llama-index-readers-hubspot/llama_index/readers/hubspot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">44</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load deals, contacts and companies data from Hubspot.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents, where each document represensts a list of Hubspot objects</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">hubspot</span> <span class="kn">import</span> <span class="n">HubSpot</span>

    <span class="n">api_client</span> <span class="o">=</span> <span class="n">HubSpot</span><span class="p">(</span><span class="n">access_token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">)</span>
    <span class="n">all_deals</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">deals</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
    <span class="n">all_contacts</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">contacts</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
    <span class="n">all_companies</span> <span class="o">=</span> <span class="n">api_client</span><span class="o">.</span><span class="n">crm</span><span class="o">.</span><span class="n">companies</span><span class="o">.</span><span class="n">get_all</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_deals</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"deals"</span><span class="p">}</span>
        <span class="p">),</span>
        <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_contacts</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"contacts"</span><span class="p">},</span>
        <span class="p">),</span>
        <span class="n">Document</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">all_companies</span><span class="si">}</span><span class="s2">"</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="s2">""</span><span class="p">),</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"companies"</span><span class="p">},</span>
        <span class="p">),</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Hive](https://docs.llamaindex.ai/en/stable/api_reference/readers/hive/)[Next Huggingface fs](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/)
