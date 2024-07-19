Title: Clickhouse - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/

Markdown Content:
Clickhouse - LlamaIndex


ClickHouseReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/#llama_index.readers.clickhouse.ClickHouseReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

ClickHouse reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `clickhouse_host` | `str) ` | 
An URL to connect to ClickHouse backend. Default to "localhost".



 | `'localhost'` |
| `username` | `str) ` | 

Username to login. Defaults to "default".



 | `'default'` |
| `password` | `str) ` | 

Password to login. Defaults to "".



 | `''` |
| `clickhouse_port` | `int) ` | 

URL port to connect with HTTP. Defaults to 8123.



 | `8123` |
| `database` | `str) ` | 

Database name to find the table. Defaults to 'default'.



 | `'default'` |
| `engine` | `str) ` | 

Engine. Options are "MergeTree" and "Memory". Default is "MergeTree".



 | `'MergeTree'` |
| `table` | `str) ` | 

Table name to operate on. Defaults to 'vector\_table'.



 | `'llama_index'` |
| `index_type` | `str` | 

index type string. Default to "NONE", supported are ("NONE", "HNSW", "ANNOY")



 | `'NONE'` |
| `metric` | `str) ` | 

Metric to compute distance, supported are ('l2', 'cosine', 'dot'). Defaults to 'cosine'



 | `'cosine'` |
| `batch_size` | `int` | 

the size of documents to insert. Defaults to 1000.



 | `1000` |
| `index_params` | `dict` | 

The index parameters for ClickHouse. Defaults to None.



 | `None` |
| `search_params` | `dict` | 

The search parameters for a ClicKHouse query. Defaults to None.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-clickhouse/llama_index/readers/clickhouse/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 83</span>
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
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ClickHouseReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ClickHouse reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        clickhouse_host (str) : An URL to connect to ClickHouse backend. Default to "localhost".</span>
<span class="sd">        username (str) : Username to login. Defaults to "default".</span>
<span class="sd">        password (str) : Password to login. Defaults to "".</span>
<span class="sd">        clickhouse_port (int) : URL port to connect with HTTP. Defaults to 8123.</span>
<span class="sd">        database (str) : Database name to find the table. Defaults to 'default'.</span>
<span class="sd">        engine (str) : Engine. Options are "MergeTree" and "Memory". Default is "MergeTree".</span>
<span class="sd">        table (str) : Table name to operate on. Defaults to 'vector_table'.</span>
<span class="sd">        index_type (str): index type string. Default to "NONE", supported are ("NONE", "HNSW", "ANNOY")</span>
<span class="sd">        metric (str) : Metric to compute distance, supported are ('l2', 'cosine', 'dot').</span>
<span class="sd">            Defaults to 'cosine'</span>
<span class="sd">        batch_size (int, optional): the size of documents to insert. Defaults to 1000.</span>
<span class="sd">        index_params (dict, optional): The index parameters for ClickHouse.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        search_params (dict, optional): The search parameters for a ClicKHouse query.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">clickhouse_host</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"localhost"</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">clickhouse_port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">8123</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">engine</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"MergeTree"</span><span class="p">,</span>
        <span class="n">table</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llama_index"</span><span class="p">,</span>
        <span class="n">index_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"NONE"</span><span class="p">,</span>
        <span class="n">metric</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cosine"</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span>
        <span class="n">index_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">search_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">clickhouse_connect</span><span class="o">.</span><span class="n">get_client</span><span class="p">(</span>
            <span class="n">host</span><span class="o">=</span><span class="n">clickhouse_host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">clickhouse_port</span><span class="p">,</span>
            <span class="n">username</span><span class="o">=</span><span class="n">username</span><span class="p">,</span>
            <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">config</span> <span class="o">=</span> <span class="n">ClickHouseSettings</span><span class="p">(</span>
            <span class="n">table</span><span class="o">=</span><span class="n">table</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">engine</span><span class="o">=</span><span class="n">engine</span><span class="p">,</span>
            <span class="n">index_type</span><span class="o">=</span><span class="n">index_type</span><span class="p">,</span>
            <span class="n">metric</span><span class="o">=</span><span class="n">metric</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">index_params</span><span class="o">=</span><span class="n">index_params</span><span class="p">,</span>
            <span class="n">search_params</span><span class="o">=</span><span class="n">search_params</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
        <span class="n">where_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from ClickHouse.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_vector (List[float]): Query vector.</span>
<span class="sd">            where_str (Optional[str], optional): where condition string.</span>
<span class="sd">                Defaults to None.</span>
<span class="sd">            limit (int): Number of results to return.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="n">query_statement</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">build_query_statement</span><span class="p">(</span>
            <span class="n">query_embed</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
            <span class="n">where_str</span><span class="o">=</span><span class="n">where_str</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">],</span> <span class="n">text</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span> <span class="n">metadata</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_statement</span><span class="p">)</span><span class="o">.</span><span class="n">named_results</span><span class="p">()</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/#llama_index.readers.clickhouse.ClickHouseReader.load_data "Permanent link")

```
load_data(query_vector: List[float], where_str: Optional[str] = None, limit: int = 10) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from ClickHouse.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_vector` | `List[float]` | 
Query vector.



 | _required_ |
| `where_str` | `Optional[str]` | 

where condition string. Defaults to None.



 | `None` |
| `limit` | `int` | 

Number of results to return.



 | `10` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-clickhouse/llama_index/readers/clickhouse/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
    <span class="n">where_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from ClickHouse.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_vector (List[float]): Query vector.</span>
<span class="sd">        where_str (Optional[str], optional): where condition string.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        limit (int): Number of results to return.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="n">query_statement</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">build_query_statement</span><span class="p">(</span>
        <span class="n">query_embed</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
        <span class="n">where_str</span><span class="o">=</span><span class="n">where_str</span><span class="p">,</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">Document</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">],</span> <span class="n">text</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span> <span class="n">metadata</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_statement</span><span class="p">)</span><span class="o">.</span><span class="n">named_results</span><span class="p">()</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chroma](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/)[Next Confluence](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/)
