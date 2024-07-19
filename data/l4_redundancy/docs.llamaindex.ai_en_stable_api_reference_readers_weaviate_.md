Title: Weaviate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/

Markdown Content:
Weaviate - LlamaIndex


WeaviateReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/#llama_index.readers.weaviate.WeaviateReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Weaviate reader.

Retrieves documents from Weaviate through vector lookup. Allows option to concatenate retrieved documents into one Document, or to return separate Document objects per document.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `host` | `str` | 
host.



 | _required_ |
| `auth_client_secret` | `Optional[AuthCredentials]` | 

auth\_client\_secret.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-weaviate/llama_index/readers/weaviate/base.py`

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
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WeaviateReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Weaviate reader.</span>

<span class="sd">    Retrieves documents from Weaviate through vector lookup. Allows option</span>
<span class="sd">    to concatenate retrieved documents into one Document, or to return</span>
<span class="sd">    separate Document objects per document.</span>

<span class="sd">    Args:</span>
<span class="sd">        host (str): host.</span>
<span class="sd">        auth_client_secret (Optional[weaviate.auth.AuthCredentials]):</span>
<span class="sd">            auth_client_secret.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">auth_client_secret</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">weaviate</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">weaviate</span> <span class="kn">import</span> <span class="n">Client</span>
            <span class="kn">from</span> <span class="nn">weaviate.auth</span> <span class="kn">import</span> <span class="n">AuthCredentials</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`weaviate` package not found, please run `pip install weaviate-client`"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">:</span> <span class="n">Client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">auth_client_secret</span><span class="o">=</span><span class="n">auth_client_secret</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">class_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">graphql_query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">separate_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Weaviate.</span>

<span class="sd">        If `graphql_query` is not found in load_kwargs, we assume that</span>
<span class="sd">        `class_name` and `properties` are provided.</span>

<span class="sd">        Args:</span>
<span class="sd">            class_name (Optional[str]): class_name to retrieve documents from.</span>
<span class="sd">            properties (Optional[List[str]]): properties to retrieve from documents.</span>
<span class="sd">            graphql_query (Optional[str]): Raw GraphQL Query.</span>
<span class="sd">                We assume that the query is a Get query.</span>
<span class="sd">            separate_documents (Optional[bool]): Whether to return separate</span>
<span class="sd">                documents. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">class_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">properties</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">props_txt</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">properties</span><span class="p">)</span>
            <span class="n">graphql_query</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            </span><span class="se">{{</span>
<span class="s2">                Get </span><span class="se">{{</span>
<span class="s2">                    </span><span class="si">{</span><span class="n">class_name</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span>
<span class="s2">                        </span><span class="si">{</span><span class="n">props_txt</span><span class="si">}</span>
<span class="s2">                    </span><span class="se">}}</span>
<span class="s2">                </span><span class="se">}}</span>
<span class="s2">            </span><span class="se">}}</span>
<span class="s2">            """</span>
        <span class="k">elif</span> <span class="n">graphql_query</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Either `class_name` and `properties` must be specified, "</span>
                <span class="s2">"or `graphql_query` must be specified."</span>
            <span class="p">)</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">raw</span><span class="p">(</span><span class="n">graphql_query</span><span class="p">)</span>
        <span class="k">if</span> <span class="s2">"errors"</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid query, got errors: </span><span class="si">{}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s2">"errors"</span><span class="p">]))</span>

        <span class="n">data_response</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"data"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"Get"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">data_response</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid query response, must be a Get query."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">class_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># infer class_name if only graphql_query was provided</span>
            <span class="n">class_name</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">data_response</span><span class="p">[</span><span class="s2">"Get"</span><span class="p">]</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
        <span class="n">entries</span> <span class="o">=</span> <span class="n">data_response</span><span class="p">[</span><span class="s2">"Get"</span><span class="p">][</span><span class="n">class_name</span><span class="p">]</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">entries</span><span class="p">:</span>
            <span class="n">embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="c1"># for each entry, join properties into &lt;property&gt;:&lt;value&gt;</span>
            <span class="c1"># separated by newlines</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">entry</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">k</span> <span class="o"></span> <span class="s2">"_additional"</span><span class="p">:</span>
                <span class="k">if</span> <span class="s2">"vector"</span> <span class="ow">in</span> <span class="n">v</span><span class="p">:</span>
                    <span class="n">embedding</span> <span class="o">=</span> <span class="n">v</span><span class="p">[</span><span class="s2">"vector"</span><span class="p">]</span>
                <span class="k">continue</span>
            <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">))</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">separate_documents</span><span class="p">:</span>
        <span class="c1"># join all documents into one</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">doc</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">)]</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Weather](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/)[Next Web](https://docs.llamaindex.ai/en/stable/api_reference/readers/web/)
