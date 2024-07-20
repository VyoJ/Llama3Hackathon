Title: Evaporate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/

Markdown Content:
Evaporate - LlamaIndex


DFEvaporateProgram [#](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/#llama_index.program.evaporate.DFEvaporateProgram "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseEvaporateProgram[DataFrameRowsOnly]`

Evaporate DF program.

Given a set of fields, extracts a dataframe from a set of nodes. Each node corresponds to a row in the dataframe - each value in the row corresponds to a field value.

Source code in `llama-index-integrations/program/llama-index-program-evaporate/llama_index/program/evaporate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
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
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DFEvaporateProgram</span><span class="p">(</span><span class="n">BaseEvaporateProgram</span><span class="p">[</span><span class="n">DataFrameRowsOnly</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Evaporate DF program.</span>

<span class="sd">    Given a set of fields, extracts a dataframe from a set of nodes.</span>
<span class="sd">    Each node corresponds to a row in the dataframe - each value in the row</span>
<span class="sd">    corresponds to a field value.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">fit</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="n">field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">field_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">expected_output</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">inplace</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Given the input Nodes and fields, synthesize the python code."""</span>
        <span class="n">fn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extractor</span><span class="o">.</span><span class="n">extract_fn_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">field</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted function: </span><span class="si">{</span><span class="n">fn</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">inplace</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_field_fns</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="o">=</span> <span class="n">fn</span>
        <span class="k">return</span> <span class="n">fn</span>

    <span class="k">def</span> <span class="nf">_inference</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">fn_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">field_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Given the input, call the python code and return the result."""</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extractor</span><span class="o">.</span><span class="n">run_fn_on_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">fn_str</span><span class="p">,</span> <span class="n">field_name</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Results: </span><span class="si">{</span><span class="n">results</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">output_cls</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">[</span><span class="n">DataFrameRowsOnly</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Output class."""</span>
        <span class="k">return</span> <span class="n">DataFrameRowsOnly</span>

    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DataFrameRowsOnly</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Call evaporate on inference data."""</span>
        <span class="c1"># TODO: either specify `nodes` or `texts` in kwds</span>
        <span class="k">if</span> <span class="s2">"nodes"</span> <span class="ow">in</span> <span class="n">kwds</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="n">kwds</span><span class="p">[</span><span class="s2">"nodes"</span><span class="p">]</span>
        <span class="k">elif</span> <span class="s2">"texts"</span> <span class="ow">in</span> <span class="n">kwds</span><span class="p">:</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">kwds</span><span class="p">[</span><span class="s2">"texts"</span><span class="p">]]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either `nodes` or `texts`."</span><span class="p">)</span>

        <span class="n">col_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fields</span><span class="p">:</span>
            <span class="n">col_dict</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_inference</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_field_fns</span><span class="p">[</span><span class="n">field</span><span class="p">],</span> <span class="n">field</span><span class="p">)</span>

        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">col_dict</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_fields</span><span class="p">)</span>

        <span class="c1"># convert pd.DataFrame to DataFrameRowsOnly</span>
        <span class="n">df_row_objs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">row_arr</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">values</span><span class="p">:</span>
            <span class="n">df_row_objs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">DataFrameRow</span><span class="p">(</span><span class="n">row_values</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">row_arr</span><span class="p">)))</span>
        <span class="k">return</span> <span class="n">DataFrameRowsOnly</span><span class="p">(</span><span class="n">rows</span><span class="o">=</span><span class="n">df_row_objs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### output\_cls `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/#llama_index.program.evaporate.DFEvaporateProgram.output_cls "Permanent link")

```
output_cls: Type[DataFrameRowsOnly]
```

Output class.

### fit [#](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/#llama_index.program.evaporate.DFEvaporateProgram.fit "Permanent link")

```
fit(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], field: str, field_context: Optional[Any] = None, expected_output: Optional[Any] = None, inplace: bool = True) -> str
```

Given the input Nodes and fields, synthesize the python code.

Source code in `llama-index-integrations/program/llama-index-program-evaporate/llama_index/program/evaporate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">137</span>
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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">fit</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="n">field</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">field_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">inplace</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Given the input Nodes and fields, synthesize the python code."""</span>
    <span class="n">fn</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extractor</span><span class="o">.</span><span class="n">extract_fn_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">field</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted function: </span><span class="si">{</span><span class="n">fn</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">inplace</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_field_fns</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="o">=</span> <span class="n">fn</span>
    <span class="k">return</span> <span class="n">fn</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Selection](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/)[Next Guidance](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/)
