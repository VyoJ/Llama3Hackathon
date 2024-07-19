Title: Openapi - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/

Markdown Content:
Openapi - LlamaIndex


OpenAPIToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/#llama_index.tools.openapi.OpenAPIToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

OpenAPI Tool.

This tool can be used to parse an OpenAPI spec for endpoints and operations Use the RequestsToolSpec to automate requests to the openapi server

Source code in `llama-index-integrations/tools/llama-index-tools-openapi/llama_index/tools/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 10</span>
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
<span class="normal">115</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAPIToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAPI Tool.</span>

<span class="sd">    This tool can be used to parse an OpenAPI spec for endpoints and operations</span>
<span class="sd">    Use the RequestsToolSpec to automate requests to the openapi server</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"load_openapi_spec"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spec</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="kn">import</span> <span class="nn">yaml</span>

        <span class="k">if</span> <span class="n">spec</span> <span class="ow">and</span> <span class="n">url</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Only provide one of OpenAPI dict or url"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">spec</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">elif</span> <span class="n">url</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">text</span>
            <span class="n">spec</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must provide a url or OpenAPI spec as a dict"</span><span class="p">)</span>

        <span class="n">parsed_spec</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_api_spec</span><span class="p">(</span><span class="n">spec</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">spec</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">parsed_spec</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">load_openapi_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.</span>

<span class="sd">        Here's a step-by-step guide to assist you in answering questions:</span>

<span class="sd">        1. Determine the base URL required for making the request</span>

<span class="sd">        2. Identify the relevant paths necessary to address the question</span>

<span class="sd">        3. Find the required parameters for making the request</span>

<span class="sd">        4. Perform the necessary requests to obtain the answer</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: A List of Document objects.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">spec</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">process_api_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spec</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Perform simplification and reduction on an OpenAPI specification.</span>

<span class="sd">        The goal is to create a more concise and efficient representation</span>
<span class="sd">        for retrieval purposes.</span>
<span class="sd">        """</span>

        <span class="k">def</span> <span class="nf">reduce_details</span><span class="p">(</span><span class="n">details</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
            <span class="n">reduced</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">):</span>
                <span class="n">reduced</span><span class="p">[</span><span class="s2">"description"</span><span class="p">]</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parameters"</span><span class="p">):</span>
                <span class="n">reduced</span><span class="p">[</span><span class="s2">"parameters"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">param</span>
                    <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parameters"</span><span class="p">,</span> <span class="p">[])</span>
                    <span class="k">if</span> <span class="n">param</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"required"</span><span class="p">)</span>
                <span class="p">]</span>
            <span class="k">if</span> <span class="s2">"200"</span> <span class="ow">in</span> <span class="n">details</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">]:</span>
                <span class="n">reduced</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">]</span> <span class="o">=</span> <span class="n">details</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">][</span><span class="s2">"200"</span><span class="p">]</span>
            <span class="k">return</span> <span class="n">reduced</span>

        <span class="k">def</span> <span class="nf">dereference_openapi</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">):</span>
<span class="w">            </span><span class="sd">"""Dereferences a Swagger/OpenAPI document by resolving all $ref pointers."""</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">jsonschema</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"The jsonschema library is required to parse OpenAPI documents. "</span>
                    <span class="s2">"Please install it with `pip install jsonschema`."</span>
                <span class="p">)</span>

            <span class="n">resolver</span> <span class="o">=</span> <span class="n">jsonschema</span><span class="o">.</span><span class="n">RefResolver</span><span class="o">.</span><span class="n">from_schema</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">)</span>

            <span class="k">def</span> <span class="nf">_dereference</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                    <span class="k">if</span> <span class="s2">"$ref"</span> <span class="ow">in</span> <span class="n">obj</span><span class="p">:</span>
                        <span class="k">with</span> <span class="n">resolver</span><span class="o">.</span><span class="n">resolving</span><span class="p">(</span><span class="n">obj</span><span class="p">[</span><span class="s2">"$ref"</span><span class="p">])</span> <span class="k">as</span> <span class="n">resolved</span><span class="p">:</span>
                            <span class="k">return</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">resolved</span><span class="p">)</span>
                    <span class="k">return</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">obj</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                    <span class="k">return</span> <span class="p">[</span><span class="n">_dereference</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">obj</span><span class="p">]</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">return</span> <span class="n">obj</span>

            <span class="k">return</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">)</span>

        <span class="n">spec</span> <span class="o">=</span> <span class="n">dereference_openapi</span><span class="p">(</span><span class="n">spec</span><span class="p">)</span>
        <span class="n">endpoints</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">route</span><span class="p">,</span> <span class="n">operations</span> <span class="ow">in</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"paths"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">operation</span><span class="p">,</span> <span class="n">details</span> <span class="ow">in</span> <span class="n">operations</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">operation</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"get"</span><span class="p">,</span> <span class="s2">"post"</span><span class="p">,</span> <span class="s2">"patch"</span><span class="p">]:</span>
                    <span class="n">endpoint_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">operation</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">route</span><span class="si">}</span><span class="s2">"</span>
                    <span class="n">description</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>
                    <span class="n">endpoints</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="p">(</span><span class="n">endpoint_name</span><span class="p">,</span> <span class="n">description</span><span class="p">,</span> <span class="n">reduce_details</span><span class="p">(</span><span class="n">details</span><span class="p">))</span>
                    <span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"servers"</span><span class="p">:</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"servers"</span><span class="p">],</span>
            <span class="s2">"description"</span><span class="p">:</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"info"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">),</span>
            <span class="s2">"endpoints"</span><span class="p">:</span> <span class="n">endpoints</span><span class="p">,</span>
        <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### load\_openapi\_spec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/#llama_index.tools.openapi.OpenAPIToolSpec.load_openapi_spec "Permanent link")

```
load_openapi_spec() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.

Here's a step-by-step guide to assist you in answering questions:

1.  Determine the base URL required for making the request
    
2.  Identify the relevant paths necessary to address the question
    
3.  Find the required parameters for making the request
    
4.  Perform the necessary requests to obtain the answer
    

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Document` | `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
A List of Document objects.



 |

Source code in `llama-index-integrations/tools/llama-index-tools-openapi/llama_index/tools/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
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
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_openapi_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.</span>

<span class="sd">    Here's a step-by-step guide to assist you in answering questions:</span>

<span class="sd">    1. Determine the base URL required for making the request</span>

<span class="sd">    2. Identify the relevant paths necessary to address the question</span>

<span class="sd">    3. Find the required parameters for making the request</span>

<span class="sd">    4. Perform the necessary requests to obtain the answer</span>

<span class="sd">    Returns:</span>
<span class="sd">        Document: A List of Document objects.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">spec</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### process\_api\_spec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/#llama_index.tools.openapi.OpenAPIToolSpec.process_api_spec "Permanent link")

```
process_api_spec(spec: dict) -> dict
```

Perform simplification and reduction on an OpenAPI specification.

The goal is to create a more concise and efficient representation for retrieval purposes.

Source code in `llama-index-integrations/tools/llama-index-tools-openapi/llama_index/tools/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
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
<span class="normal">115</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">process_api_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spec</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Perform simplification and reduction on an OpenAPI specification.</span>

<span class="sd">    The goal is to create a more concise and efficient representation</span>
<span class="sd">    for retrieval purposes.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">reduce_details</span><span class="p">(</span><span class="n">details</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="n">reduced</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">):</span>
            <span class="n">reduced</span><span class="p">[</span><span class="s2">"description"</span><span class="p">]</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parameters"</span><span class="p">):</span>
            <span class="n">reduced</span><span class="p">[</span><span class="s2">"parameters"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">param</span>
                <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"parameters"</span><span class="p">,</span> <span class="p">[])</span>
                <span class="k">if</span> <span class="n">param</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"required"</span><span class="p">)</span>
            <span class="p">]</span>
        <span class="k">if</span> <span class="s2">"200"</span> <span class="ow">in</span> <span class="n">details</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">]:</span>
            <span class="n">reduced</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">]</span> <span class="o">=</span> <span class="n">details</span><span class="p">[</span><span class="s2">"responses"</span><span class="p">][</span><span class="s2">"200"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">reduced</span>

    <span class="k">def</span> <span class="nf">dereference_openapi</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Dereferences a Swagger/OpenAPI document by resolving all $ref pointers."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">jsonschema</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"The jsonschema library is required to parse OpenAPI documents. "</span>
                <span class="s2">"Please install it with `pip install jsonschema`."</span>
            <span class="p">)</span>

        <span class="n">resolver</span> <span class="o">=</span> <span class="n">jsonschema</span><span class="o">.</span><span class="n">RefResolver</span><span class="o">.</span><span class="n">from_schema</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">_dereference</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">if</span> <span class="s2">"$ref"</span> <span class="ow">in</span> <span class="n">obj</span><span class="p">:</span>
                    <span class="k">with</span> <span class="n">resolver</span><span class="o">.</span><span class="n">resolving</span><span class="p">(</span><span class="n">obj</span><span class="p">[</span><span class="s2">"$ref"</span><span class="p">])</span> <span class="k">as</span> <span class="n">resolved</span><span class="p">:</span>
                        <span class="k">return</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">resolved</span><span class="p">)</span>
                <span class="k">return</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">obj</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="k">return</span> <span class="p">[</span><span class="n">_dereference</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">obj</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">obj</span>

        <span class="k">return</span> <span class="n">_dereference</span><span class="p">(</span><span class="n">openapi_doc</span><span class="p">)</span>

    <span class="n">spec</span> <span class="o">=</span> <span class="n">dereference_openapi</span><span class="p">(</span><span class="n">spec</span><span class="p">)</span>
    <span class="n">endpoints</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">route</span><span class="p">,</span> <span class="n">operations</span> <span class="ow">in</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"paths"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="k">for</span> <span class="n">operation</span><span class="p">,</span> <span class="n">details</span> <span class="ow">in</span> <span class="n">operations</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">operation</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"get"</span><span class="p">,</span> <span class="s2">"post"</span><span class="p">,</span> <span class="s2">"patch"</span><span class="p">]:</span>
                <span class="n">endpoint_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">operation</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">route</span><span class="si">}</span><span class="s2">"</span>
                <span class="n">description</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">)</span>
                <span class="n">endpoints</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="p">(</span><span class="n">endpoint_name</span><span class="p">,</span> <span class="n">description</span><span class="p">,</span> <span class="n">reduce_details</span><span class="p">(</span><span class="n">details</span><span class="p">))</span>
                <span class="p">)</span>

    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"servers"</span><span class="p">:</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"servers"</span><span class="p">],</span>
        <span class="s2">"description"</span><span class="p">:</span> <span class="n">spec</span><span class="p">[</span><span class="s2">"info"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"description"</span><span class="p">),</span>
        <span class="s2">"endpoints"</span><span class="p">:</span> <span class="n">endpoints</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openai](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/)[Next Passio nutrition ai](https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/)
