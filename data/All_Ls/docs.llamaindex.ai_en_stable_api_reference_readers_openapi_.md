Title: Openapi - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/

Markdown Content:
Openapi - LlamaIndex


OpenAPIReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/#llama_index.readers.openapi.OpenAPIReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

OpenAPI reader.

Reads OpenAPI specifications giving options to on how to parse them.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `depth` | `Optional[int]` | 
Depth to dive before splitting the JSON.



 | `1` |
| `exclude` | `Optional[List[str]]` | 

JSON paths to exclude, separated by commas by '.'. For example: 'components.pets' will exclude the component 'pets' from the OpenAPI specification. Useful for removing unwanted information from the OpenAPI specification.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
|  | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-openapi/llama_index/readers/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
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
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenAPIReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenAPI reader.</span>

<span class="sd">    Reads OpenAPI specifications giving options to on how to parse them.</span>

<span class="sd">    Args:</span>
<span class="sd">        depth (Optional[int]): Depth to dive before splitting the JSON.</span>
<span class="sd">        exclude (Optional[List[str]]): JSON paths to exclude, separated by commas by '.'. For example: 'components.pets' will exclude the component 'pets' from the OpenAPI specification. Useful for removing unwanted information from the OpenAPI specification.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">exclude</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span> <span class="o">=</span> <span class="n">exclude</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the name identifier of the class."""</span>
        <span class="k">return</span> <span class="s2">"OpenAPIReader"</span>

    <span class="k">def</span> <span class="nf">_should_exclude</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if the path should be excluded."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">exclude_path</span><span class="p">,</span> <span class="n">path</span><span class="p">)</span> <span class="k">for</span> <span class="n">exclude_path</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">exclude</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_docs_from_attributes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"$"</span><span class="p">,</span>
        <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Build Documents from the attributes of the OAS JSON."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">path</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_should_exclude</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">depth</span> <span class="o">==</span> <span class="n">level</span> <span class="ow">or</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"json_path"</span><span class="p">:</span> <span class="n">path</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>
                <span class="p">)</span>
            <span class="p">]</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">doc</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">value</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_docs_from_attributes</span><span class="p">(</span>
                <span class="n">k</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">level</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="p">)</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input file."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> is not a valid JSON file."</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">doc</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_docs_from_attributes</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/#llama_index.readers.openapi.OpenAPIReader.class_name "Permanent link")

```
class_name() -> str
```

Get the name identifier of the class.

Source code in `llama-index-integrations/readers/llama-index-readers-openapi/llama_index/readers/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the name identifier of the class."""</span>
    <span class="k">return</span> <span class="s2">"OpenAPIReader"</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/#llama_index.readers.openapi.OpenAPIReader.load_data "Permanent link")

```
load_data(input_file: str, extra_info: Optional[Dict] = {}) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input file.

Source code in `llama-index-integrations/readers/llama-index-readers-openapi/llama_index/readers/openapi/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">70</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input file."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecodeError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The file </span><span class="si">{</span><span class="n">input_file</span><span class="si">}</span><span class="s2"> is not a valid JSON file."</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">doc</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_docs_from_attributes</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openalex](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/)[Next Opendal](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/)
