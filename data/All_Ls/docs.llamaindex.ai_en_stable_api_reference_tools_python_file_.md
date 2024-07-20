Title: Python file - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/

Markdown Content:
Python file - LlamaIndex


PythonFileToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/#llama_index.tools.python_file.PythonFileToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Source code in `llama-index-integrations/tools/llama-index-tools-python-file/llama_index/tools/python_file/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PythonFileToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"function_definitions"</span><span class="p">,</span> <span class="s2">"get_function"</span><span class="p">,</span> <span class="s2">"get_functions"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">function_definitions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this function to get the name and arguments of all function definitions in the python file.</span>

<span class="sd">        Args:</span>
<span class="sd">            external (Optional[bool]): Defaults to true. If false, this function will also return functions that start with _</span>
<span class="sd">        """</span>
        <span class="n">functions</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">ast</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">ast</span><span class="o">.</span><span class="n">FunctionDef</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">external</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"_"</span><span class="p">):</span>
                    <span class="k">continue</span>
                <span class="n">functions</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">name: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="si">}</span>
<span class="s2">arguments: </span><span class="si">{</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">args</span><span class="p">)</span><span class="si">}</span>
<span class="s2">                    """</span>
        <span class="k">return</span> <span class="n">functions</span>

    <span class="k">def</span> <span class="nf">get_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this function to get the name and arguments of a single function definition in the python file.</span>

<span class="sd">        Args:</span>
<span class="sd">            name (str): The name of the function to retrieve</span>
<span class="sd">        """</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">ast</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">ast</span><span class="o">.</span><span class="n">FunctionDef</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="n">name</span><span class="p">:</span>
                    <span class="k">return</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">name: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="si">}</span>
<span class="s2">arguments: </span><span class="si">{</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">args</span><span class="p">)</span><span class="si">}</span>
<span class="s2">docstring: </span><span class="si">{</span><span class="n">ast</span><span class="o">.</span><span class="n">get_docstring</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="si">}</span>
<span class="s2">                        """</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### get\_functions [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/#llama_index.tools.python_file.PythonFileToolSpec.get_functions "Permanent link")

```
get_functions(names: List[str]) -> str
```

Use this function to get the name and arguments of a list of function definition in the python file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `List[str]` | 
The names of the functions to retrieve



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-python-file/llama_index/tools/python_file/base.py`

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
<span class="normal">59</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_functions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this function to get the name and arguments of a list of function definition in the python file.</span>

<span class="sd">    Args:</span>
<span class="sd">        name (List[str]): The names of the functions to retrieve</span>
<span class="sd">    """</span>
    <span class="n">functions</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">names</span><span class="p">:</span>
        <span class="n">functions</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_function</span><span class="p">(</span><span class="n">name</span><span class="p">)</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
    <span class="k">return</span> <span class="n">functions</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Playgrounds](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/)[Next Query engine](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/)
