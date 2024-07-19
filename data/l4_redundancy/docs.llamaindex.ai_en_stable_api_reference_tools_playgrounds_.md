Title: Playgrounds - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/

Markdown Content:
Playgrounds - LlamaIndex


PlaygroundsSubgraphConnectorToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphConnectorToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[GraphQLToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/#llama_index.tools.graphql.GraphQLToolSpec "llama_index.tools.graphql.base.GraphQLToolSpec")`

Connects to subgraphs on The Graph's decentralized network via the Playgrounds API.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `spec_functions` | `list` | 
List of functions that specify the tool's capabilities.



 |
| `url` | `str` | 

The endpoint URL for the GraphQL requests.



 |
| `headers` | `dict` | 

Headers used for the GraphQL requests.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_connector/base.py`

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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PlaygroundsSubgraphConnectorToolSpec</span><span class="p">(</span><span class="n">GraphQLToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Connects to subgraphs on The Graph's decentralized network via the Playgrounds API.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        spec_functions (list): List of functions that specify the tool's capabilities.</span>
<span class="sd">        url (str): The endpoint URL for the GraphQL requests.</span>
<span class="sd">        headers (dict): Headers used for the GraphQL requests.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"graphql_request"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">identifier</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">use_deployment_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize the connector.</span>

<span class="sd">        Args:</span>
<span class="sd">            identifier (str): Subgraph identifier or Deployment ID.</span>
<span class="sd">            api_key (str): API key for the Playgrounds API.</span>
<span class="sd">            use_deployment_id (bool): Flag to indicate if the identifier is a deployment ID. Default is False.</span>
<span class="sd">        """</span>
        <span class="n">endpoint</span> <span class="o">=</span> <span class="s2">"deployments"</span> <span class="k">if</span> <span class="n">use_deployment_id</span> <span class="k">else</span> <span class="s2">"subgraphs"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"https://api.playgrounds.network/v1/proxy/</span><span class="si">{</span><span class="n">endpoint</span><span class="si">}</span><span class="s2">/id/</span><span class="si">{</span><span class="n">identifier</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Playgrounds-Api-Key"</span><span class="p">:</span> <span class="n">api_key</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">graphql_request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">variables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">operation_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Make a GraphQL query.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The GraphQL query string to execute.</span>
<span class="sd">            variables (dict, optional): Variables for the GraphQL query. Default is None.</span>
<span class="sd">            operation_name (str, optional): Name of the operation, if multiple operations are present in the query. Default is None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            dict: The response from the GraphQL server if successful.</span>
<span class="sd">            str: Error message if the request fails.</span>
<span class="sd">        """</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">strip</span><span class="p">()}</span>

        <span class="k">if</span> <span class="n">variables</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"variables"</span><span class="p">]</span> <span class="o">=</span> <span class="n">variables</span>

        <span class="k">if</span> <span class="n">operation_name</span><span class="p">:</span>
            <span class="n">payload</span><span class="p">[</span><span class="s2">"operationName"</span><span class="p">]</span> <span class="o">=</span> <span class="n">operation_name</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">)</span>

            <span class="c1"># Check if the request was successful</span>
            <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

            <span class="c1"># Return the JSON response</span>
            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># Handle request errors</span>
            <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="c1"># Handle JSON decoding errors</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s2">"Error decoding JSON: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

### graphql\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphConnectorToolSpec.graphql_request "Permanent link")

```
graphql_request(query: str, variables: Optional[dict] = None, operation_name: Optional[str] = None) -> Union[dict, str]
```

Make a GraphQL query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The GraphQL query string to execute.



 | _required_ |
| `variables` | `dict` | 

Variables for the GraphQL query. Default is None.



 | `None` |
| `operation_name` | `str` | 

Name of the operation, if multiple operations are present in the query. Default is None.



 | `None` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `dict` | `Union[dict, str]` | 
The response from the GraphQL server if successful.



 |
| `str` | `Union[dict, str]` | 

Error message if the request fails.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_connector/base.py`

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
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">graphql_request</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">variables</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">operation_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Make a GraphQL query.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The GraphQL query string to execute.</span>
<span class="sd">        variables (dict, optional): Variables for the GraphQL query. Default is None.</span>
<span class="sd">        operation_name (str, optional): Name of the operation, if multiple operations are present in the query. Default is None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        dict: The response from the GraphQL server if successful.</span>
<span class="sd">        str: Error message if the request fails.</span>
<span class="sd">    """</span>
    <span class="n">payload</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">strip</span><span class="p">()}</span>

    <span class="k">if</span> <span class="n">variables</span><span class="p">:</span>
        <span class="n">payload</span><span class="p">[</span><span class="s2">"variables"</span><span class="p">]</span> <span class="o">=</span> <span class="n">variables</span>

    <span class="k">if</span> <span class="n">operation_name</span><span class="p">:</span>
        <span class="n">payload</span><span class="p">[</span><span class="s2">"operationName"</span><span class="p">]</span> <span class="o">=</span> <span class="n">operation_name</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">)</span>

        <span class="c1"># Check if the request was successful</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>

        <span class="c1"># Return the JSON response</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="c1"># Handle request errors</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="c1"># Handle JSON decoding errors</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"Error decoding JSON: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

PlaygroundsSubgraphInspectorToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphInspectorToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[GraphQLToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/#llama_index.tools.graphql.GraphQLToolSpec "llama_index.tools.graphql.base.GraphQLToolSpec")`

Connects to subgraphs on The Graph's decentralized network via the Playgrounds API and introspects the subgraph. Provides functionalities to process and summarize the introspected schema for easy comprehension.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `spec_functions` | `list` | 
List of functions that specify the tool's capabilities.



 |
| `url` | `str` | 

The endpoint URL for the GraphQL requests.



 |
| `headers` | `dict` | 

Headers used for the GraphQL requests.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_inspector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  7</span>
<span class="normal">  8</span>
<span class="normal">  9</span>
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
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PlaygroundsSubgraphInspectorToolSpec</span><span class="p">(</span><span class="n">GraphQLToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Connects to subgraphs on The Graph's decentralized network via the Playgrounds API and introspects the subgraph.</span>
<span class="sd">    Provides functionalities to process and summarize the introspected schema for easy comprehension.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        spec_functions (list): List of functions that specify the tool's capabilities.</span>
<span class="sd">        url (str): The endpoint URL for the GraphQL requests.</span>
<span class="sd">        headers (dict): Headers used for the GraphQL requests.</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"introspect_and_summarize_subgraph"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">identifier</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">use_deployment_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize the connection to the specified subgraph on The Graph's network.</span>

<span class="sd">        Args:</span>
<span class="sd">            identifier (str): The subgraph's identifier or deployment ID.</span>
<span class="sd">            api_key (str): API key for the Playgrounds API.</span>
<span class="sd">            use_deployment_id (bool): If True, treats the identifier as a deployment ID. Default is False.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_url</span><span class="p">(</span><span class="n">identifier</span><span class="p">,</span> <span class="n">use_deployment_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Playgrounds-Api-Key"</span><span class="p">:</span> <span class="n">api_key</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_generate_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">identifier</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">use_deployment_id</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generate the appropriate URL based on the identifier and whether it's a deployment ID or not.</span>

<span class="sd">        Args:</span>
<span class="sd">            identifier (str): The subgraph's identifier or deployment ID.</span>
<span class="sd">            use_deployment_id (bool): If True, constructs the URL using the deployment ID.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: The constructed URL.</span>
<span class="sd">        """</span>
        <span class="n">endpoint</span> <span class="o">=</span> <span class="s2">"deployments"</span> <span class="k">if</span> <span class="n">use_deployment_id</span> <span class="k">else</span> <span class="s2">"subgraphs"</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"https://api.playgrounds.network/v1/proxy/</span><span class="si">{</span><span class="n">endpoint</span><span class="si">}</span><span class="s2">/id/</span><span class="si">{</span><span class="n">identifier</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">introspect_and_summarize_subgraph</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Introspects the subgraph and summarizes its schema into textual categories.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: A textual summary of the introspected subgraph schema.</span>
<span class="sd">        """</span>
        <span class="n">introspection_query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        query {</span>
<span class="s2">            __schema {</span>
<span class="s2">                types {</span>
<span class="s2">                    kind</span>
<span class="s2">                    name</span>
<span class="s2">                    description</span>
<span class="s2">                    enumValues {</span>
<span class="s2">                        name</span>
<span class="s2">                    }</span>
<span class="s2">                    fields {</span>
<span class="s2">                        name</span>
<span class="s2">                        args {</span>
<span class="s2">                            name</span>
<span class="s2">                        }</span>
<span class="s2">                        type {</span>
<span class="s2">                            kind</span>
<span class="s2">                            name</span>
<span class="s2">                            ofType {</span>
<span class="s2">                                name</span>
<span class="s2">                            }</span>
<span class="s2">                        }</span>
<span class="s2">                    }</span>
<span class="s2">                }</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graphql_request</span><span class="p">(</span><span class="n">introspection_query</span><span class="p">)</span>
        <span class="k">if</span> <span class="s2">"data"</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
            <span class="n">processed_subgraph</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_subgraph</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">subgraph_to_text</span><span class="p">(</span><span class="n">processed_subgraph</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">"Error during introspection."</span>

    <span class="k">def</span> <span class="nf">_graphql_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Execute a GraphQL query against the subgraph's endpoint.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The GraphQL query string.</span>

<span class="sd">        Returns:</span>
<span class="sd">            dict: Response from the GraphQL server, either containing the data or an error.</span>
<span class="sd">        """</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">strip</span><span class="p">()}</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">)</span>
            <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span><span class="s2">"error"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">)}</span>

    <span class="k">def</span> <span class="nf">_process_subgraph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Processes the introspected subgraph schema into categories based on naming conventions.</span>

<span class="sd">        Args:</span>
<span class="sd">            result (dict): Introspected schema result from the GraphQL query.</span>

<span class="sd">        Returns:</span>
<span class="sd">            dict: A processed representation of the introspected schema, categorized into specific entity queries, list entity queries, and other entities.</span>
<span class="sd">        """</span>
        <span class="n">processed_subgraph</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"specific_entity_queries"</span><span class="p">:</span> <span class="p">{},</span>
            <span class="s2">"list_entity_queries"</span><span class="p">:</span> <span class="p">{},</span>
            <span class="s2">"other_entities"</span><span class="p">:</span> <span class="p">{},</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">type_</span> <span class="ow">in</span> <span class="n">result</span><span class="p">[</span><span class="s2">"__schema"</span><span class="p">][</span><span class="s2">"types"</span><span class="p">]:</span>
            <span class="k">if</span> <span class="n">type_</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"__"</span><span class="p">):</span>
                <span class="k">continue</span>  <span class="c1"># Skip meta entities</span>

            <span class="n">entity_name</span> <span class="o">=</span> <span class="n">type_</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="n">fields</span><span class="p">,</span> <span class="n">args_required</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_fields</span><span class="p">(</span><span class="n">type_</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">fields</span><span class="p">:</span>
                <span class="c1"># Determine category based on naming convention</span>
                <span class="k">if</span> <span class="n">entity_name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"s"</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">args_required</span><span class="p">:</span>
                    <span class="n">processed_subgraph</span><span class="p">[</span><span class="s2">"list_entity_queries"</span><span class="p">][</span><span class="n">entity_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">fields</span>
                <span class="k">elif</span> <span class="ow">not</span> <span class="n">entity_name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"s"</span><span class="p">)</span> <span class="ow">and</span> <span class="n">args_required</span><span class="p">:</span>
                    <span class="n">processed_subgraph</span><span class="p">[</span><span class="s2">"specific_entity_queries"</span><span class="p">][</span><span class="n">entity_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">fields</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">processed_subgraph</span><span class="p">[</span><span class="s2">"other_entities"</span><span class="p">][</span><span class="n">entity_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">fields</span>

        <span class="k">return</span> <span class="n">processed_subgraph</span>

    <span class="k">def</span> <span class="nf">_get_fields</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Extracts relevant fields and their details from a given type within the introspected schema.</span>

<span class="sd">        Args:</span>
<span class="sd">            type_ (dict): A type within the introspected schema.</span>

<span class="sd">        Returns:</span>
<span class="sd">            tuple: A tuple containing a list of relevant fields and a boolean indicating if arguments are required for the fields.</span>
<span class="sd">        """</span>
        <span class="n">fields</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">args_required</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">type_</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fields"</span><span class="p">)</span> <span class="ow">or</span> <span class="p">[]:</span>
            <span class="k">if</span> <span class="n">f</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">"__typename"</span> <span class="ow">and</span> <span class="ow">not</span> <span class="p">(</span>
                <span class="n">f</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"_filter"</span><span class="p">)</span>
                <span class="ow">or</span> <span class="n">f</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"_orderBy"</span><span class="p">)</span>
                <span class="ow">or</span> <span class="n">f</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="o">.</span><span class="n">islower</span><span class="p">()</span>
            <span class="p">):</span>
                <span class="n">field_info</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"name"</span><span class="p">:</span> <span class="n">f</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]}</span>

                <span class="c1"># Check for enum values</span>
                <span class="k">if</span> <span class="s2">"enumValues"</span> <span class="ow">in</span> <span class="n">f</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">and</span> <span class="n">f</span><span class="p">[</span><span class="s2">"type"</span><span class="p">][</span><span class="s2">"enumValues"</span><span class="p">]:</span>
                    <span class="n">field_info</span><span class="p">[</span><span class="s2">"enumValues"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                        <span class="n">enum_val</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="k">for</span> <span class="n">enum_val</span> <span class="ow">in</span> <span class="n">f</span><span class="p">[</span><span class="s2">"type"</span><span class="p">][</span><span class="s2">"enumValues"</span><span class="p">]</span>
                    <span class="p">]</span>

                <span class="n">fields</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">field_info</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"args"</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">[</span><span class="s2">"args"</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">args_required</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"type"</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"fields"</span><span class="p">):</span>
                    <span class="n">subfields</span><span class="p">,</span> <span class="n">sub_args_required</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_fields</span><span class="p">(</span><span class="n">f</span><span class="p">[</span><span class="s2">"type"</span><span class="p">])</span>
                    <span class="n">fields</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">subfields</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">sub_args_required</span><span class="p">:</span>
                        <span class="n">args_required</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">return</span> <span class="n">fields</span><span class="p">,</span> <span class="n">args_required</span>

    <span class="k">def</span> <span class="nf">format_section</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">category</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">example</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entities</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Formats a given section of the subgraph introspection result into a readable string format.</span>

<span class="sd">        Args:</span>
<span class="sd">            category (str): The category name of the entities.</span>
<span class="sd">            description (str): A description explaining the category.</span>
<span class="sd">            example (str): A generic GraphQL query example related to the category.</span>
<span class="sd">            entities (dict): Dictionary containing entities and their fields related to the category.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: A formatted string representation of the provided section data.</span>
<span class="sd">        """</span>
        <span class="n">section</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"Category: </span><span class="si">{</span><span class="n">category</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"Description: </span><span class="si">{</span><span class="n">description</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"Generic Example:"</span><span class="p">,</span>
            <span class="n">example</span><span class="p">,</span>
            <span class="s2">"</span><span class="se">\n</span><span class="s2">Detailed Breakdown:"</span><span class="p">,</span>
        <span class="p">]</span>

        <span class="k">for</span> <span class="n">entity</span><span class="p">,</span> <span class="n">fields</span> <span class="ow">in</span> <span class="n">entities</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Entity: </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">field_info</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">:</span>
                <span class="n">field_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"    - </span><span class="si">{</span><span class="n">field_info</span><span class="p">[</span><span class="s1">'name'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
                <span class="k">if</span> <span class="s2">"enumValues"</span> <span class="ow">in</span> <span class="n">field_info</span><span class="p">:</span>
                    <span class="n">field_str</span> <span class="o">+=</span> <span class="p">(</span>
                        <span class="sa">f</span><span class="s2">" (Enum values: </span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">field_info</span><span class="p">[</span><span class="s1">'enumValues'</span><span class="p">])</span><span class="si">}</span><span class="s2">)"</span>
                    <span class="p">)</span>
                <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">field_str</span><span class="p">)</span>
            <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>  <span class="c1"># Add a blank line for separation</span>

        <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>  <span class="c1"># Add another blank line for separation between sections</span>
        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">section</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">subgraph_to_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subgraph</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Converts a processed subgraph representation into a textual summary based on entity categories.</span>

<span class="sd">        Args:</span>
<span class="sd">            subgraph (dict): A processed representation of the introspected schema, categorized into specific entity queries, list entity queries, and other entities.</span>

<span class="sd">        Returns:</span>
<span class="sd">            str: A textual summary of the processed subgraph schema.</span>
<span class="sd">        """</span>
        <span class="n">sections</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">(</span>
                <span class="s2">"Specific Entity Queries (Requires Arguments)"</span><span class="p">,</span>
                <span class="s2">"These queries target a singular entity and require specific arguments (like an ID) to fetch data."</span><span class="p">,</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">            {</span>
<span class="sd">                entityName(id: "specific_id") {</span>
<span class="sd">                    fieldName1</span>
<span class="sd">                    fieldName2</span>
<span class="sd">                    ...</span>
<span class="sd">                }</span>
<span class="sd">            }</span>
<span class="sd">            """</span><span class="p">,</span>
                <span class="n">subgraph</span><span class="p">[</span><span class="s2">"specific_entity_queries"</span><span class="p">],</span>
            <span class="p">),</span>
            <span class="p">(</span>
                <span class="s2">"List Entity Queries (Optional Arguments)"</span><span class="p">,</span>
                <span class="s2">"These queries fetch a list of entities. They don't strictly require arguments but often accept optional parameters for filtering, sorting, and pagination."</span><span class="p">,</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">            {</span>
<span class="sd">                entityNames(first: 10, orderBy: "someField", orderDirection: "asc") {</span>
<span class="sd">                    fieldName1</span>
<span class="sd">                    fieldName2</span>
<span class="sd">                    ...</span>
<span class="sd">                }</span>
<span class="sd">            }</span>
<span class="sd">            """</span><span class="p">,</span>
                <span class="n">subgraph</span><span class="p">[</span><span class="s2">"list_entity_queries"</span><span class="p">],</span>
            <span class="p">),</span>
            <span class="p">(</span>
                <span class="s2">"Other Entities"</span><span class="p">,</span>
                <span class="s2">"These are additional entities that may not fit the conventional singular/plural querying pattern of subgraphs."</span><span class="p">,</span>
                <span class="s2">""</span><span class="p">,</span>
                <span class="n">subgraph</span><span class="p">[</span><span class="s2">"other_entities"</span><span class="p">],</span>
            <span class="p">),</span>
        <span class="p">]</span>

        <span class="n">result_lines</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">category</span><span class="p">,</span> <span class="n">desc</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">entities</span> <span class="ow">in</span> <span class="n">sections</span><span class="p">:</span>
            <span class="n">result_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_section</span><span class="p">(</span><span class="n">category</span><span class="p">,</span> <span class="n">desc</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">entities</span><span class="p">))</span>

        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">result_lines</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### introspect\_and\_summarize\_subgraph [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphInspectorToolSpec.introspect_and_summarize_subgraph "Permanent link")

```
introspect_and_summarize_subgraph() -> str
```

Introspects the subgraph and summarizes its schema into textual categories.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
A textual summary of the introspected subgraph schema.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_inspector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">49</span>
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
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">introspect_and_summarize_subgraph</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Introspects the subgraph and summarizes its schema into textual categories.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: A textual summary of the introspected subgraph schema.</span>
<span class="sd">    """</span>
    <span class="n">introspection_query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    query {</span>
<span class="s2">        __schema {</span>
<span class="s2">            types {</span>
<span class="s2">                kind</span>
<span class="s2">                name</span>
<span class="s2">                description</span>
<span class="s2">                enumValues {</span>
<span class="s2">                    name</span>
<span class="s2">                }</span>
<span class="s2">                fields {</span>
<span class="s2">                    name</span>
<span class="s2">                    args {</span>
<span class="s2">                        name</span>
<span class="s2">                    }</span>
<span class="s2">                    type {</span>
<span class="s2">                        kind</span>
<span class="s2">                        name</span>
<span class="s2">                        ofType {</span>
<span class="s2">                            name</span>
<span class="s2">                        }</span>
<span class="s2">                    }</span>
<span class="s2">                }</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    }</span>
<span class="s2">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_graphql_request</span><span class="p">(</span><span class="n">introspection_query</span><span class="p">)</span>
    <span class="k">if</span> <span class="s2">"data"</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
        <span class="n">processed_subgraph</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_subgraph</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">subgraph_to_text</span><span class="p">(</span><span class="n">processed_subgraph</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"Error during introspection."</span>
</code></pre></div></td></tr></tbody></table>

### format\_section [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphInspectorToolSpec.format_section "Permanent link")

```
format_section(category: str, description: str, example: str, entities: dict) -> str
```

Formats a given section of the subgraph introspection result into a readable string format.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `category` | `str` | 
The category name of the entities.



 | _required_ |
| `description` | `str` | 

A description explaining the category.



 | _required_ |
| `example` | `str` | 

A generic GraphQL query example related to the category.



 | _required_ |
| `entities` | `dict` | 

Dictionary containing entities and their fields related to the category.



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
A formatted string representation of the provided section data.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_inspector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">format_section</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">category</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">example</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entities</span><span class="p">:</span> <span class="nb">dict</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Formats a given section of the subgraph introspection result into a readable string format.</span>

<span class="sd">    Args:</span>
<span class="sd">        category (str): The category name of the entities.</span>
<span class="sd">        description (str): A description explaining the category.</span>
<span class="sd">        example (str): A generic GraphQL query example related to the category.</span>
<span class="sd">        entities (dict): Dictionary containing entities and their fields related to the category.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: A formatted string representation of the provided section data.</span>
<span class="sd">    """</span>
    <span class="n">section</span> <span class="o">=</span> <span class="p">[</span>
        <span class="sa">f</span><span class="s2">"Category: </span><span class="si">{</span><span class="n">category</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="sa">f</span><span class="s2">"Description: </span><span class="si">{</span><span class="n">description</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="s2">"Generic Example:"</span><span class="p">,</span>
        <span class="n">example</span><span class="p">,</span>
        <span class="s2">"</span><span class="se">\n</span><span class="s2">Detailed Breakdown:"</span><span class="p">,</span>
    <span class="p">]</span>

    <span class="k">for</span> <span class="n">entity</span><span class="p">,</span> <span class="n">fields</span> <span class="ow">in</span> <span class="n">entities</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Entity: </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">field_info</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">:</span>
            <span class="n">field_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"    - </span><span class="si">{</span><span class="n">field_info</span><span class="p">[</span><span class="s1">'name'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">if</span> <span class="s2">"enumValues"</span> <span class="ow">in</span> <span class="n">field_info</span><span class="p">:</span>
                <span class="n">field_str</span> <span class="o">+=</span> <span class="p">(</span>
                    <span class="sa">f</span><span class="s2">" (Enum values: </span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">field_info</span><span class="p">[</span><span class="s1">'enumValues'</span><span class="p">])</span><span class="si">}</span><span class="s2">)"</span>
                <span class="p">)</span>
            <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">field_str</span><span class="p">)</span>
        <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>  <span class="c1"># Add a blank line for separation</span>

    <span class="n">section</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>  <span class="c1"># Add another blank line for separation between sections</span>
    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">section</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### subgraph\_to\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/#llama_index.tools.playgrounds.PlaygroundsSubgraphInspectorToolSpec.subgraph_to_text "Permanent link")

```
subgraph_to_text(subgraph: dict) -> str
```

Converts a processed subgraph representation into a textual summary based on entity categories.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `subgraph` | `dict` | 
A processed representation of the introspected schema, categorized into specific entity queries, list entity queries, and other entities.



 | _required_ |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
A textual summary of the processed subgraph schema.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-playgrounds/llama_index/tools/playgrounds/subgraph_inspector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">subgraph_to_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subgraph</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Converts a processed subgraph representation into a textual summary based on entity categories.</span>

<span class="sd">    Args:</span>
<span class="sd">        subgraph (dict): A processed representation of the introspected schema, categorized into specific entity queries, list entity queries, and other entities.</span>

<span class="sd">    Returns:</span>
<span class="sd">        str: A textual summary of the processed subgraph schema.</span>
<span class="sd">    """</span>
    <span class="n">sections</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">(</span>
            <span class="s2">"Specific Entity Queries (Requires Arguments)"</span><span class="p">,</span>
            <span class="s2">"These queries target a singular entity and require specific arguments (like an ID) to fetch data."</span><span class="p">,</span>
<span class="w">            </span><span class="sd">"""</span>
<span class="sd">        {</span>
<span class="sd">            entityName(id: "specific_id") {</span>
<span class="sd">                fieldName1</span>
<span class="sd">                fieldName2</span>
<span class="sd">                ...</span>
<span class="sd">            }</span>
<span class="sd">        }</span>
<span class="sd">        """</span><span class="p">,</span>
            <span class="n">subgraph</span><span class="p">[</span><span class="s2">"specific_entity_queries"</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="p">(</span>
            <span class="s2">"List Entity Queries (Optional Arguments)"</span><span class="p">,</span>
            <span class="s2">"These queries fetch a list of entities. They don't strictly require arguments but often accept optional parameters for filtering, sorting, and pagination."</span><span class="p">,</span>
<span class="w">            </span><span class="sd">"""</span>
<span class="sd">        {</span>
<span class="sd">            entityNames(first: 10, orderBy: "someField", orderDirection: "asc") {</span>
<span class="sd">                fieldName1</span>
<span class="sd">                fieldName2</span>
<span class="sd">                ...</span>
<span class="sd">            }</span>
<span class="sd">        }</span>
<span class="sd">        """</span><span class="p">,</span>
            <span class="n">subgraph</span><span class="p">[</span><span class="s2">"list_entity_queries"</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="p">(</span>
            <span class="s2">"Other Entities"</span><span class="p">,</span>
            <span class="s2">"These are additional entities that may not fit the conventional singular/plural querying pattern of subgraphs."</span><span class="p">,</span>
            <span class="s2">""</span><span class="p">,</span>
            <span class="n">subgraph</span><span class="p">[</span><span class="s2">"other_entities"</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">]</span>

    <span class="n">result_lines</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">category</span><span class="p">,</span> <span class="n">desc</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">entities</span> <span class="ow">in</span> <span class="n">sections</span><span class="p">:</span>
        <span class="n">result_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_section</span><span class="p">(</span><span class="n">category</span><span class="p">,</span> <span class="n">desc</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">entities</span><span class="p">))</span>

    <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">result_lines</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Passio nutrition ai](https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/)[Next Python file](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/)
