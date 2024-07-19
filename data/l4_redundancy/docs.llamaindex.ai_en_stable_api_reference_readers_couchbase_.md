Title: Couchbase - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/

Markdown Content:
Couchbase - LlamaIndex


CouchbaseReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/#llama_index.readers.couchbase.CouchbaseReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Couchbase document loader.

Loads data from a Couchbase cluster into Document used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `client(Optional[Any])` |  | 
A Couchbase client to use. If not provided, the client will be created based on the connection\_string and database credentials.



 | _required_ |
| `connection_string` | `Optional[str]` | 

The connection string to the Couchbase cluster.



 | `None` |
| `db_username` | `Optional[str]` | 

The username to connect to the Couchbase cluster.



 | `None` |
| `db_password` | `Optional[str]` | 

The password to connect to the Couchbase cluster.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-couchbase/llama_index/readers/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  9</span>
<span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
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
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CouchbaseReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Couchbase document loader.</span>

<span class="sd">    Loads data from a Couchbase cluster into Document used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        client(Optional[Any]): A Couchbase client to use.</span>
<span class="sd">            If not provided, the client will be created based on the connection_string</span>
<span class="sd">            and database credentials.</span>
<span class="sd">        connection_string (Optional[str]): The connection string to the Couchbase cluster.</span>
<span class="sd">        db_username (Optional[str]): The username to connect to the Couchbase cluster.</span>
<span class="sd">        db_password (Optional[str]): The password to connect to the Couchbase cluster.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_username</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">db_password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Couchbase document loader."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="s2">"`couchbase` package not found, please run `pip install --upgrade couchbase`"</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">couchbase.auth</span> <span class="kn">import</span> <span class="n">PasswordAuthenticator</span>
            <span class="kn">from</span> <span class="nn">couchbase.cluster</span> <span class="kn">import</span> <span class="n">Cluster</span>
            <span class="kn">from</span> <span class="nn">couchbase.options</span> <span class="kn">import</span> <span class="n">ClusterOptions</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">client</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">connection_string</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">db_username</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">db_password</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"You need to pass either a couchbase client or connection_string and credentials must be provided."</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">auth</span> <span class="o">=</span> <span class="n">PasswordAuthenticator</span><span class="p">(</span>
                    <span class="n">db_username</span><span class="p">,</span>
                    <span class="n">db_password</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">:</span> <span class="n">Cluster</span> <span class="o">=</span> <span class="n">Cluster</span><span class="p">(</span><span class="n">connection_string</span><span class="p">,</span> <span class="n">ClusterOptions</span><span class="p">(</span><span class="n">auth</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>

    <span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the Couchbase cluster lazily.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The SQL++ query to execute.</span>
<span class="sd">            text_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">                `text` field of the document. By default, all columns are</span>
<span class="sd">                written.</span>
<span class="sd">            metadata_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">                `metadata` field of the document. By default, no columns are written.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">timedelta</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">query</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query must be provided."</span><span class="p">)</span>

        <span class="c1"># Ensure connection to Couchbase cluster</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">wait_until_ready</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="mi">5</span><span class="p">))</span>

        <span class="c1"># Run SQL++ Query</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">text_fields</span><span class="p">:</span>
                <span class="n">text_fields</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="n">field</span><span class="p">:</span> <span class="n">row</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">metadata_fields</span><span class="p">}</span>

            <span class="n">document</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">text_fields</span>
            <span class="p">)</span>

            <span class="k">yield</span> <span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the Couchbase cluster.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The SQL++ query to execute.</span>
<span class="sd">            text_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">                `text` field of the document. By default, all columns are</span>
<span class="sd">                written.</span>
<span class="sd">            metadata_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">                `metadata` field of the document. By default, no columns are written.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">text_fields</span><span class="p">,</span> <span class="n">metadata_fields</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### lazy\_load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/#llama_index.readers.couchbase.CouchbaseReader.lazy_load_data "Permanent link")

```
lazy_load_data(query: str, text_fields: Optional[List[str]] = None, metadata_fields: Optional[List[str]] = []) -> Iterable[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the Couchbase cluster lazily.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The SQL++ query to execute.



 | _required_ |
| `text_fields` | `Optional[List[str]]` | 

The columns to write into the `text` field of the document. By default, all columns are written.



 | `None` |
| `metadata_fields` | `Optional[List[str]]` | 

The columns to write into the `metadata` field of the document. By default, no columns are written.



 | `[]` |

Source code in `llama-index-integrations/readers/llama-index-readers-couchbase/llama_index/readers/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
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
<span class="normal">90</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the Couchbase cluster lazily.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The SQL++ query to execute.</span>
<span class="sd">        text_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">            `text` field of the document. By default, all columns are</span>
<span class="sd">            written.</span>
<span class="sd">        metadata_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">            `metadata` field of the document. By default, no columns are written.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">timedelta</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">query</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query must be provided."</span><span class="p">)</span>

    <span class="c1"># Ensure connection to Couchbase cluster</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">wait_until_ready</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="mi">5</span><span class="p">))</span>

    <span class="c1"># Run SQL++ Query</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">text_fields</span><span class="p">:</span>
            <span class="n">text_fields</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="n">field</span><span class="p">:</span> <span class="n">row</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">metadata_fields</span><span class="p">}</span>

        <span class="n">document</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">text_fields</span>
        <span class="p">)</span>

        <span class="k">yield</span> <span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/#llama_index.readers.couchbase.CouchbaseReader.load_data "Permanent link")

```
load_data(query: str, text_fields: Optional[List[str]] = None, metadata_fields: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the Couchbase cluster.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The SQL++ query to execute.



 | _required_ |
| `text_fields` | `Optional[List[str]]` | 

The columns to write into the `text` field of the document. By default, all columns are written.



 | `None` |
| `metadata_fields` | `Optional[List[str]]` | 

The columns to write into the `metadata` field of the document. By default, no columns are written.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-couchbase/llama_index/readers/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 92</span>
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
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">text_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the Couchbase cluster.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The SQL++ query to execute.</span>
<span class="sd">        text_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">            `text` field of the document. By default, all columns are</span>
<span class="sd">            written.</span>
<span class="sd">        metadata_fields (Optional[List[str]]): The columns to write into the</span>
<span class="sd">            `metadata` field of the document. By default, no columns are written.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lazy_load_data</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">text_fields</span><span class="p">,</span> <span class="n">metadata_fields</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Confluence](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/)[Next Couchdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/)
