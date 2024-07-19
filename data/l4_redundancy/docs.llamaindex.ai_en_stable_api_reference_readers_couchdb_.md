Title: Couchdb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/

Markdown Content:
Couchdb - LlamaIndex


SimpleCouchDBReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/#llama_index.readers.couchdb.SimpleCouchDBReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Simple CouchDB reader.

Concatenates each CouchDB doc into Document used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `couchdb_url` | `str` | 
CouchDB Full URL.



 | `None` |
| `max_docs` | `int` | 

Maximum number of documents to load.



 | `1000` |

Source code in `llama-index-integrations/readers/llama-index-readers-couchdb/llama_index/readers/couchdb/base.py`

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
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleCouchDBReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple CouchDB reader.</span>

<span class="sd">    Concatenates each CouchDB doc into Document used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        couchdb_url (str): CouchDB Full URL.</span>
<span class="sd">        max_docs (int): Maximum number of documents to load.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">pwd</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">couchdb_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_docs</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">couchdb_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">couchdb3</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="n">couchdb_url</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">couchdb3</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="sa">f</span><span class="s2">"http://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">pwd</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_docs</span> <span class="o">=</span> <span class="n">max_docs</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            db_name (str): name of the database.</span>
<span class="sd">            query (Optional[str]): query to filter documents.</span>
<span class="sd">                Defaults to None</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">db_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># if no query is specified, return all docs in database</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"showing all docs"</span><span class="p">)</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="s2">"_all_docs"</span><span class="p">,</span> <span class="n">include_docs</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"executing query"</span><span class="p">)</span>
            <span class="n">results</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">results</span><span class="o">.</span><span class="n">rows</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

        <span class="c1"># check if more than one result</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span>
            <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="s2">"rows"</span><span class="p">)</span>
            <span class="ow">and</span> <span class="n">results</span><span class="o">.</span><span class="n">rows</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">rows</span><span class="p">:</span>
                <span class="c1"># check that the id field exists</span>
                <span class="k">if</span> <span class="s2">"id"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">row</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`id` field not found in CouchDB document."</span><span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">doc</span><span class="p">)))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># only one result</span>
            <span class="k">if</span> <span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"docs"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"docs"</span><span class="p">):</span>
                    <span class="c1"># check that the _id field exists</span>
                    <span class="k">if</span> <span class="s2">"_id"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">item</span><span class="p">:</span>
                        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`_id` field not found in CouchDB document."</span><span class="p">)</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">item</span><span class="p">)))</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/#llama_index.readers.couchdb.SimpleCouchDBReader.load_data "Permanent link")

```
load_data(db_name: str, query: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `db_name` | `str` | 
name of the database.



 | _required_ |
| `query` | `Optional[str]` | 

query to filter documents. Defaults to None



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-couchdb/llama_index/readers/couchdb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
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
<span class="normal">86</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        db_name (str): name of the database.</span>
<span class="sd">        query (Optional[str]): query to filter documents.</span>
<span class="sd">            Defaults to None</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">db_name</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># if no query is specified, return all docs in database</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"showing all docs"</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="s2">"_all_docs"</span><span class="p">,</span> <span class="n">include_docs</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"executing query"</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">results</span><span class="o">.</span><span class="n">rows</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>

    <span class="c1"># check if more than one result</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span>
        <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">results</span><span class="p">,</span> <span class="s2">"rows"</span><span class="p">)</span>
        <span class="ow">and</span> <span class="n">results</span><span class="o">.</span><span class="n">rows</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">rows</span><span class="p">:</span>
            <span class="c1"># check that the id field exists</span>
            <span class="k">if</span> <span class="s2">"id"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">row</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`id` field not found in CouchDB document."</span><span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">doc</span><span class="p">)))</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># only one result</span>
        <span class="k">if</span> <span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"docs"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"docs"</span><span class="p">):</span>
                <span class="c1"># check that the _id field exists</span>
                <span class="k">if</span> <span class="s2">"_id"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">item</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"`_id` field not found in CouchDB document."</span><span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">item</span><span class="p">)))</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/)[Next Dad jokes](https://docs.llamaindex.ai/en/stable/api_reference/readers/dad_jokes/)
