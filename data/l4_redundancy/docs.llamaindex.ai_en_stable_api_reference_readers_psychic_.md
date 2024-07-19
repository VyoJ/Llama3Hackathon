Title: Psychic - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/

Markdown Content:
Psychic - LlamaIndex


PsychicReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/#llama_index.readers.psychic.PsychicReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Psychic reader.

Psychic is a platform that allows syncing data from many SaaS apps through one universal API. This reader connects to an instance of Psychic and reads data from it, given a connector ID, account ID, and API key.

Learn more at docs.psychic.dev.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `psychic_key` | `str` | 
Secret key for Psychic. Get one at https://dashboard.psychic.dev/api-keys.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-psychic/llama_index/readers/psychic/base.py`

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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PsychicReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Psychic reader.</span>

<span class="sd">    Psychic is a platform that allows syncing data from many SaaS apps through one</span>
<span class="sd">        universal API.</span>
<span class="sd">    This reader connects to an instance of Psychic and reads data from it, given a</span>
<span class="sd">        connector ID, account ID, and API key.</span>

<span class="sd">    Learn more at docs.psychic.dev.</span>

<span class="sd">    Args:</span>
<span class="sd">        psychic_key (str): Secret key for Psychic.</span>
<span class="sd">            Get one at https://dashboard.psychic.dev/api-keys.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">psychic_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">psychicapi</span> <span class="kn">import</span> <span class="n">ConnectorId</span><span class="p">,</span> <span class="n">Psychic</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`psychicapi` package not found, please run `pip install psychicapi`"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">psychic_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">psychic_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"PSYCHIC_SECRET_KEY"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">psychic_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify `psychic_key` or set environment "</span>
                    <span class="s2">"variable `PSYCHIC_SECRET_KEY`."</span>
                <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">psychic</span> <span class="o">=</span> <span class="n">Psychic</span><span class="p">(</span><span class="n">secret_key</span><span class="o">=</span><span class="n">psychic_key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ConnectorId</span> <span class="o">=</span> <span class="n">ConnectorId</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">connector_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">account_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from a Psychic connection.</span>

<span class="sd">        Args:</span>
<span class="sd">            connector_id (str): The connector ID to connect to</span>
<span class="sd">            account_id (str): The account ID to connect to</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">connector_id</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">account_id</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify both `connector_id` and `account_id`."</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">connector_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">ConnectorId</span><span class="o">.</span><span class="n">__members__</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid connector ID."</span><span class="p">)</span>

        <span class="c1"># get all the documents in the database</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">psychic</span><span class="o">.</span><span class="n">get_documents</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ConnectorId</span><span class="p">[</span><span class="n">connector_id</span><span class="p">],</span> <span class="n">account_id</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">resource</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span>
            <span class="n">doc_id</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"uri"</span><span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">doc_id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"connector_id"</span><span class="p">:</span> <span class="n">connector_id</span><span class="p">,</span> <span class="s2">"account_id"</span><span class="p">:</span> <span class="n">account_id</span><span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/#llama_index.readers.psychic.PsychicReader.load_data "Permanent link")

```
load_data(connector_id: Optional[str] = None, account_id: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from a Psychic connection.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `connector_id` | `str` | 
The connector ID to connect to



 | `None` |
| `account_id` | `str` | 

The account ID to connect to



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-psychic/llama_index/readers/psychic/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">47</span>
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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">connector_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">account_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from a Psychic connection.</span>

<span class="sd">    Args:</span>
<span class="sd">        connector_id (str): The connector ID to connect to</span>
<span class="sd">        account_id (str): The account ID to connect to</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">connector_id</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">account_id</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify both `connector_id` and `account_id`."</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">connector_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">ConnectorId</span><span class="o">.</span><span class="n">__members__</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid connector ID."</span><span class="p">)</span>

    <span class="c1"># get all the documents in the database</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">psychic</span><span class="o">.</span><span class="n">get_documents</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ConnectorId</span><span class="p">[</span><span class="n">connector_id</span><span class="p">],</span> <span class="n">account_id</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">resource</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span>
        <span class="n">doc_id</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"uri"</span><span class="p">)</span>
        <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">doc_id</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"connector_id"</span><span class="p">:</span> <span class="n">connector_id</span><span class="p">,</span> <span class="s2">"account_id"</span><span class="p">:</span> <span class="n">account_id</span><span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Preprocess](https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/)[Next Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/)
