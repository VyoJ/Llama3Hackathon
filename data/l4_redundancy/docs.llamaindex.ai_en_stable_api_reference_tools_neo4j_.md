Title: Neo4j - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/

Markdown Content:
Neo4j - LlamaIndex


Neo4jQueryToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/#llama_index.tools.neo4j.Neo4jQueryToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

This class is responsible for querying a Neo4j graph database based on a provided schema definition.

Source code in `llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/base.py`

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
<span class="normal">154</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jQueryToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This class is responsible for querying a Neo4j graph database based on a provided schema definition.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"run_request"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">,</span> <span class="n">database</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">LLM</span><span class="p">,</span> <span class="n">validate_cypher</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes the Neo4jSchemaWiseQuery object.</span>

<span class="sd">        Args:</span>
<span class="sd">            url (str): The connection string for the Neo4j database.</span>
<span class="sd">            user (str): Username for the Neo4j database.</span>
<span class="sd">            password (str): Password for the Neo4j database.</span>
<span class="sd">            llm (obj): A language model for generating Cypher queries.</span>
<span class="sd">            validate_cypher (bool): Validate relationship directions in</span>
<span class="sd">                the generated Cypher statement. Default: False</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">find_spec</span><span class="p">(</span><span class="s2">"neo4j"</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`neo4j` package not found, please run `pip install neo4j`"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span> <span class="o">=</span> <span class="n">Neo4jGraphStore</span><span class="p">(</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">username</span><span class="o">=</span><span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">,</span> <span class="n">database</span><span class="o">=</span><span class="n">database</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">validate_cypher</span><span class="p">:</span>
            <span class="n">corrector_schema</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">Schema</span><span class="p">(</span><span class="n">el</span><span class="p">[</span><span class="s2">"start"</span><span class="p">],</span> <span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span> <span class="n">el</span><span class="p">[</span><span class="s2">"end"</span><span class="p">])</span>
                <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">structured_schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">)</span>
            <span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span> <span class="o">=</span> <span class="n">CypherQueryCorrector</span><span class="p">(</span><span class="n">corrector_schema</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_system_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generates a system message detailing the task and schema.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The system message.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        Task: Generate Cypher queries to query a Neo4j graph database based on the provided schema definition.</span>
<span class="s2">        Instructions:</span>
<span class="s2">        Use only the provided relationship types and properties.</span>
<span class="s2">        Do not use any other relationship types or properties that are not provided.</span>
<span class="s2">        If you cannot generate a Cypher statement based on the provided schema, explain the reason to the user.</span>
<span class="s2">        Schema:</span>
<span class="s2">        </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">schema</span><span class="si">}</span>

<span class="s2">        Note: Do not include any explanations or apologies in your responses.</span>
<span class="s2">        """</span>

    <span class="k">def</span> <span class="nf">query_graph_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">neo4j_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Queries the Neo4j database.</span>

<span class="sd">        Args:</span>
<span class="sd">            neo4j_query (str): The Cypher query to be executed.</span>
<span class="sd">            params (dict, optional): Parameters for the Cypher query. Defaults to None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            list: The query results.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">neo4j_query</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
            <span class="n">output</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">result</span><span class="p">]</span>
            <span class="n">output</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
            <span class="k">return</span> <span class="n">output</span>

    <span class="k">def</span> <span class="nf">construct_cypher_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Constructs a Cypher query based on a given question and history.</span>

<span class="sd">        Args:</span>
<span class="sd">            question (str): The question to construct the Cypher query for.</span>
<span class="sd">            history (list, optional): A list of previous interactions for context. Defaults to None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The constructed Cypher query.</span>
<span class="sd">        """</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_system_message</span><span class="p">()),</span>
            <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">question</span><span class="p">),</span>
        <span class="p">]</span>
        <span class="c1"># Used for Cypher healing flows</span>
        <span class="k">if</span> <span class="n">history</span><span class="p">:</span>
            <span class="n">messages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">history</span><span class="p">)</span>

        <span class="n">completions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">completions</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>

    <span class="k">def</span> <span class="nf">run_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">retry</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Executes a Cypher query based on a given question.</span>

<span class="sd">        Args:</span>
<span class="sd">            question (str): The question to execute the Cypher query for.</span>
<span class="sd">            history (list, optional): A list of previous interactions for context. Defaults to None.</span>
<span class="sd">            retry (bool, optional): Whether to retry in case of a syntax error. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            list/str: The query results or an error message.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">neo4j.exceptions</span> <span class="kn">import</span> <span class="n">CypherSyntaxError</span>

        <span class="c1"># Construct Cypher statement</span>
        <span class="n">cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">construct_cypher_query</span><span class="p">(</span><span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="p">)</span>
        <span class="c1"># Validate Cypher statement</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span><span class="p">:</span>
            <span class="n">cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_graph_db</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
        <span class="c1"># Self-healing flow</span>
        <span class="k">except</span> <span class="n">CypherSyntaxError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># If out of retries</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">retry</span><span class="p">:</span>
                <span class="k">return</span> <span class="s2">"Invalid Cypher syntax"</span>
            <span class="c1"># Self-healing Cypher flow by</span>
            <span class="c1"># providing specific error to GPT-4</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Retrying"</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_request</span><span class="p">(</span>
                <span class="n">question</span><span class="p">,</span>
                <span class="p">[</span>
                    <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">cypher</span><span class="p">),</span>
                    <span class="n">ChatMessage</span><span class="p">(</span>
                        <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span>
                        <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"This query returns an error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span>
                        <span class="s2">"Give me a improved query that works without any explanations or apologies"</span><span class="p">,</span>
                    <span class="p">),</span>
                <span class="p">],</span>
                <span class="n">retry</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_system\_message [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/#llama_index.tools.neo4j.Neo4jQueryToolSpec.get_system_message "Permanent link")

```
get_system_message()
```

Generates a system message detailing the task and schema.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | 
The system message.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">53</span>
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
<span class="normal">70</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_system_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Generates a system message detailing the task and schema.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: The system message.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">    Task: Generate Cypher queries to query a Neo4j graph database based on the provided schema definition.</span>
<span class="s2">    Instructions:</span>
<span class="s2">    Use only the provided relationship types and properties.</span>
<span class="s2">    Do not use any other relationship types or properties that are not provided.</span>
<span class="s2">    If you cannot generate a Cypher statement based on the provided schema, explain the reason to the user.</span>
<span class="s2">    Schema:</span>
<span class="s2">    </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">schema</span><span class="si">}</span>

<span class="s2">    Note: Do not include any explanations or apologies in your responses.</span>
<span class="s2">    """</span>
</code></pre></div></td></tr></tbody></table>

### query\_graph\_db [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/#llama_index.tools.neo4j.Neo4jQueryToolSpec.query_graph_db "Permanent link")

```
query_graph_db(neo4j_query, params=None)
```

Queries the Neo4j database.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `neo4j_query` | `str` | 
The Cypher query to be executed.



 | _required_ |
| `params` | `dict` | 

Parameters for the Cypher query. Defaults to None.



 | `None` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | 
The query results.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">72</span>
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
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query_graph_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">neo4j_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Queries the Neo4j database.</span>

<span class="sd">    Args:</span>
<span class="sd">        neo4j_query (str): The Cypher query to be executed.</span>
<span class="sd">        params (dict, optional): Parameters for the Cypher query. Defaults to None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        list: The query results.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">neo4j_query</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
        <span class="n">output</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">result</span><span class="p">]</span>
        <span class="n">output</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
        <span class="k">return</span> <span class="n">output</span>
</code></pre></div></td></tr></tbody></table>

### construct\_cypher\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/#llama_index.tools.neo4j.Neo4jQueryToolSpec.construct_cypher_query "Permanent link")

```
construct_cypher_query(question, history=None)
```

Constructs a Cypher query based on a given question and history.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `question` | `str` | 
The question to construct the Cypher query for.



 | _required_ |
| `history` | `list` | 

A list of previous interactions for context. Defaults to None.



 | `None` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | 
The constructed Cypher query.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">construct_cypher_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Constructs a Cypher query based on a given question and history.</span>

<span class="sd">    Args:</span>
<span class="sd">        question (str): The question to construct the Cypher query for.</span>
<span class="sd">        history (list, optional): A list of previous interactions for context. Defaults to None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: The constructed Cypher query.</span>
<span class="sd">    """</span>
    <span class="n">messages</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get_system_message</span><span class="p">()),</span>
        <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">question</span><span class="p">),</span>
    <span class="p">]</span>
    <span class="c1"># Used for Cypher healing flows</span>
    <span class="k">if</span> <span class="n">history</span><span class="p">:</span>
        <span class="n">messages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">history</span><span class="p">)</span>

    <span class="n">completions</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">completions</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
</code></pre></div></td></tr></tbody></table>

### run\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/#llama_index.tools.neo4j.Neo4jQueryToolSpec.run_request "Permanent link")

```
run_request(question, history=None, retry=True)
```

Executes a Cypher query based on a given question.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `question` | `str` | 
The question to execute the Cypher query for.



 | _required_ |
| `history` | `list` | 

A list of previous interactions for context. Defaults to None.



 | `None` |
| `retry` | `bool` | 

Whether to retry in case of a syntax error. Defaults to True.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
|  | 
list/str: The query results or an error message.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">113</span>
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
<span class="normal">154</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">retry</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Executes a Cypher query based on a given question.</span>

<span class="sd">    Args:</span>
<span class="sd">        question (str): The question to execute the Cypher query for.</span>
<span class="sd">        history (list, optional): A list of previous interactions for context. Defaults to None.</span>
<span class="sd">        retry (bool, optional): Whether to retry in case of a syntax error. Defaults to True.</span>

<span class="sd">    Returns:</span>
<span class="sd">        list/str: The query results or an error message.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">neo4j.exceptions</span> <span class="kn">import</span> <span class="n">CypherSyntaxError</span>

    <span class="c1"># Construct Cypher statement</span>
    <span class="n">cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">construct_cypher_query</span><span class="p">(</span><span class="n">question</span><span class="p">,</span> <span class="n">history</span><span class="p">)</span>
    <span class="c1"># Validate Cypher statement</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span><span class="p">:</span>
        <span class="n">cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cypher_query_corrector</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_graph_db</span><span class="p">(</span><span class="n">cypher</span><span class="p">)</span>
    <span class="c1"># Self-healing flow</span>
    <span class="k">except</span> <span class="n">CypherSyntaxError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="c1"># If out of retries</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">retry</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"Invalid Cypher syntax"</span>
        <span class="c1"># Self-healing Cypher flow by</span>
        <span class="c1"># providing specific error to GPT-4</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Retrying"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_request</span><span class="p">(</span>
            <span class="n">question</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">cypher</span><span class="p">),</span>
                <span class="n">ChatMessage</span><span class="p">(</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">SYSTEM</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="sa">f</span><span class="s2">"This query returns an error: </span><span class="si">{</span><span class="n">e</span><span class="si">!s}</span><span class="se">\n</span><span class="s2">"</span>
                    <span class="s2">"Give me a improved query that works without any explanations or apologies"</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
            <span class="n">retry</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multion](https://docs.llamaindex.ai/en/stable/api_reference/tools/multion/)[Next Notion](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/)
