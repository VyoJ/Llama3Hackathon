Title: Database - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/database/

Markdown Content:
Database - LlamaIndex


DatabaseToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/database/#llama_index.tools.database.DatabaseToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`, `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Simple Database tool.

Concatenates each row into Document used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sql_database` | `Optional[SQLDatabase]` | 
SQL database to use, including table names to specify. See :ref:`Ref-Struct-Store` for more details.



 | `None` |
| `engine` | `Optional[Engine]` | 

SQLAlchemy Engine object of the database connection.



 | `None` |
| `uri` | `Optional[str]` | 

uri of the database connection.



 | `None` |
| `scheme` | `Optional[str]` | 

scheme of the database connection.



 | `None` |
| `host` | `Optional[str]` | 

host of the database connection.



 | `None` |
| `port` | `Optional[int]` | 

port of the database connection.



 | `None` |
| `user` | `Optional[str]` | 

user of the database connection.



 | `None` |
| `password` | `Optional[str]` | 

password of the database connection.



 | `None` |
| `dbname` | `Optional[str]` | 

dbname of the database connection.



 | `None` |

Source code in `llama-index-integrations/tools/llama-index-tools-database/llama_index/tools/database/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 15</span>
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
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DatabaseToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Database tool.</span>

<span class="sd">    Concatenates each row into Document used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        sql_database (Optional[SQLDatabase]): SQL database to use,</span>
<span class="sd">            including table names to specify.</span>
<span class="sd">            See :ref:`Ref-Struct-Store` for more details.</span>

<span class="sd">        OR</span>

<span class="sd">        engine (Optional[Engine]): SQLAlchemy Engine object of the database connection.</span>

<span class="sd">        OR</span>

<span class="sd">        uri (Optional[str]): uri of the database connection.</span>

<span class="sd">        OR</span>

<span class="sd">        scheme (Optional[str]): scheme of the database connection.</span>
<span class="sd">        host (Optional[str]): host of the database connection.</span>
<span class="sd">        port (Optional[int]): port of the database connection.</span>
<span class="sd">        user (Optional[str]): user of the database connection.</span>
<span class="sd">        password (Optional[str]): password of the database connection.</span>
<span class="sd">        dbname (Optional[str]): dbname of the database connection.</span>

<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"load_data"</span><span class="p">,</span> <span class="s2">"describe_tables"</span><span class="p">,</span> <span class="s2">"list_tables"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sql_database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SQLDatabase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">engine</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Engine</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">uri</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">scheme</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">dbname</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">sql_database</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span> <span class="o">=</span> <span class="n">sql_database</span>
        <span class="k">elif</span> <span class="n">engine</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span> <span class="o">=</span> <span class="n">SQLDatabase</span><span class="p">(</span><span class="n">engine</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">uri</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uri</span> <span class="o">=</span> <span class="n">uri</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span> <span class="o">=</span> <span class="n">SQLDatabase</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">scheme</span> <span class="ow">and</span> <span class="n">host</span> <span class="ow">and</span> <span class="n">port</span> <span class="ow">and</span> <span class="n">user</span> <span class="ow">and</span> <span class="n">password</span> <span class="ow">and</span> <span class="n">dbname</span><span class="p">:</span>
            <span class="n">uri</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">scheme</span><span class="si">}</span><span class="s2">://</span><span class="si">{</span><span class="n">user</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">password</span><span class="si">}</span><span class="s2">@</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">dbname</span><span class="si">}</span><span class="s2">"</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">uri</span> <span class="o">=</span> <span class="n">uri</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span> <span class="o">=</span> <span class="n">SQLDatabase</span><span class="o">.</span><span class="n">from_uri</span><span class="p">(</span><span class="n">uri</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"You must provide either a SQLDatabase, "</span>
                <span class="s2">"a SQL Alchemy Engine, a valid connection URI, or a valid "</span>
                <span class="s2">"set of credentials."</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span> <span class="o">=</span> <span class="n">MetaData</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">reflect</span><span class="p">(</span><span class="n">bind</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span><span class="o">.</span><span class="n">engine</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Query and load data from the Database, returning a list of Documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): an SQL query to filter tables and rows.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span><span class="o">.</span><span class="n">engine</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span> <span class="k">as</span> <span class="n">connection</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">query</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"A query parameter is necessary to filter the data"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">result</span> <span class="o">=</span> <span class="n">connection</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">text</span><span class="p">(</span><span class="n">query</span><span class="p">))</span>

            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">fetchall</span><span class="p">():</span>
                <span class="c1"># fetch each item</span>
                <span class="n">doc_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span> <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">item</span><span class="p">])</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc_str</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">list_tables</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns a list of available tables in the database.</span>
<span class="sd">        To retrieve details about the columns of specific tables, use</span>
<span class="sd">        the describe_tables endpoint.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">sorted_tables</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">describe_tables</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Describes the specified tables in the database.</span>

<span class="sd">        Args:</span>
<span class="sd">            tables (List[str]): A list of table names to retrieve details about</span>
<span class="sd">        """</span>
        <span class="n">table_names</span> <span class="o">=</span> <span class="n">tables</span> <span class="ow">or</span> <span class="p">[</span><span class="n">table</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">sorted_tables</span><span class="p">]</span>
        <span class="n">table_schemas</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">table_name</span> <span class="ow">in</span> <span class="n">table_names</span><span class="p">:</span>
            <span class="n">table</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="n">table</span>
                    <span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata</span><span class="o">.</span><span class="n">sorted_tables</span>
                    <span class="k">if</span> <span class="n">table</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="n">table_name</span>
            <span class="p">),</span>
            <span class="kc">None</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">table</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NoSuchTableError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Table '</span><span class="si">{</span><span class="n">table_name</span><span class="si">}</span><span class="s2">' does not exist."</span><span class="p">)</span>
        <span class="n">schema</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">CreateTable</span><span class="p">(</span><span class="n">table</span><span class="p">)</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sql_database</span><span class="o">.</span><span class="n">_engine</span><span class="p">))</span>
        <span class="n">table_schemas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">schema</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">table_schemas</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/tools/cogniswitch/)[Next Duckduckgo](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/)
