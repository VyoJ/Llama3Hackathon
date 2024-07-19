Title: Neptune - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/

Markdown Content:
Neptune - LlamaIndex


NeptuneAnalyticsGraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/#llama_index.graph_stores.neptune.NeptuneAnalyticsGraphStore "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `NeptuneBaseGraphStore`

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neptune/llama_index/graph_stores/neptune/analytics.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 11</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NeptuneAnalyticsGraphStore</span><span class="p">(</span><span class="n">NeptuneBaseGraphStore</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">graph_identifier</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">credentials_profile_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Entity"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Neptune Analytics graph wrapper instance."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span> <span class="o">=</span> <span class="n">node_label</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">boto3</span>

                <span class="k">if</span> <span class="n">credentials_profile_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">(</span><span class="n">profile_name</span><span class="o">=</span><span class="n">credentials_profile_name</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># use default credentials</span>
                    <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">graph_identifier</span> <span class="o">=</span> <span class="n">graph_identifier</span>

                <span class="k">if</span> <span class="n">region_name</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>
                        <span class="s2">"neptune-graph"</span><span class="p">,</span> <span class="n">region_name</span><span class="o">=</span><span class="n">region_name</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">client</span><span class="p">(</span><span class="s2">"neptune-graph"</span><span class="p">)</span>

        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ModuleNotFoundError</span><span class="p">(</span>
                <span class="s2">"Could not import boto3 python package. "</span>
                <span class="s2">"Please install it with `pip install boto3`."</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span> <span class="o"></span> <span class="s2">"UnknownServiceError"</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ModuleNotFoundError</span><span class="p">(</span>
                    <span class="s2">"Neptune Database requires a boto3 version 1.34.40 or greater."</span>
                    <span class="s2">"Please install it with `pip install -U boto3`."</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Could not load credentials to authenticate with AWS client. "</span>
                    <span class="s2">"Please check that credentials in the specified "</span>
                    <span class="s2">"profile name are valid."</span>
                <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_refresh_schema</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Could not retrieve schema for Neptune due to the following error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Query Neptune database."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query() query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> parameters: </span><span class="si">{</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute_open_cypher_query</span><span class="p">(</span>
                <span class="n">openCypherQuery</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span>
            <span class="p">)[</span><span class="s2">"results"</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NeptuneQueryException</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"message"</span><span class="p">:</span> <span class="s2">"An error occurred while executing the query."</span><span class="p">,</span>
                    <span class="s2">"details"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
                <span class="p">}</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_summary</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_propertygraph_summary</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NeptuneQueryException</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"message"</span><span class="p">:</span> <span class="p">(</span>
                        <span class="s2">"Summary API is not available for this instance of Neptune,"</span>
                        <span class="s2">"ensure the engine version is &gt;=1.2.1.0"</span>
                    <span class="p">),</span>
                    <span class="s2">"details"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
                <span class="p">}</span>
            <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">summary</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"payload"</span><span class="p">][</span><span class="s2">"graphSummary"</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NeptuneQueryException</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"message"</span><span class="p">:</span> <span class="s2">"Summary API did not return a valid response."</span><span class="p">,</span>
                    <span class="s2">"details"</span><span class="p">:</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">decode</span><span class="p">(),</span>
                <span class="p">}</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">summary</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/#llama_index.graph_stores.neptune.NeptuneDatabaseGraphStore.query "Permanent link")

```
query(query: str, params: dict = {}) -> Dict[str, Any]
```

Query Neptune database.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neptune/llama_index/graph_stores/neptune/database.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Query Neptune database."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query() query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> parameters: </span><span class="si">{</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">execute_open_cypher_query</span><span class="p">(</span>
            <span class="n">openCypherQuery</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span>
        <span class="p">)[</span><span class="s2">"results"</span><span class="p">]</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">NeptuneQueryException</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"message"</span><span class="p">:</span> <span class="s2">"An error occurred while executing the query."</span><span class="p">,</span>
                <span class="s2">"details"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
            <span class="p">}</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/)[Next Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/simple/)
