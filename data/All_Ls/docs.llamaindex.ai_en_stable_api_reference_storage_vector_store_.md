Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/

Markdown Content:
Index - LlamaIndex


Vector store index types.

VectorStoreQueryResult `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Vector store query result.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Vector store query result."""</span>

    <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">similarities</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

VectorStoreQueryMode [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryMode "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Vector store query mode.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorStoreQueryMode</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vector store query mode."""</span>

    <span class="n">DEFAULT</span> <span class="o">=</span> <span class="s2">"default"</span>
    <span class="n">SPARSE</span> <span class="o">=</span> <span class="s2">"sparse"</span>
    <span class="n">HYBRID</span> <span class="o">=</span> <span class="s2">"hybrid"</span>
    <span class="n">TEXT_SEARCH</span> <span class="o">=</span> <span class="s2">"text_search"</span>
    <span class="n">SEMANTIC_HYBRID</span> <span class="o">=</span> <span class="s2">"semantic_hybrid"</span>

    <span class="c1"># fit learners</span>
    <span class="n">SVM</span> <span class="o">=</span> <span class="s2">"svm"</span>
    <span class="n">LOGISTIC_REGRESSION</span> <span class="o">=</span> <span class="s2">"logistic_regression"</span>
    <span class="n">LINEAR_REGRESSION</span> <span class="o">=</span> <span class="s2">"linear_regression"</span>

    <span class="c1"># maximum marginal relevance</span>
    <span class="n">MMR</span> <span class="o">=</span> <span class="s2">"mmr"</span>
</code></pre></div></td></tr></tbody></table>

FilterOperator [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.FilterOperator "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Vector store filter operator.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">61</span>
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
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FilterOperator</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vector store filter operator."""</span>

    <span class="c1"># TODO add more operators</span>
    <span class="n">EQ</span> <span class="o">=</span> <span class="s2">"=="</span>  <span class="c1"># default operator (string, int, float)</span>
    <span class="n">GT</span> <span class="o">=</span> <span class="s2">"&gt;"</span>  <span class="c1"># greater than (int, float)</span>
    <span class="n">LT</span> <span class="o">=</span> <span class="s2">"&lt;"</span>  <span class="c1"># less than (int, float)</span>
    <span class="n">NE</span> <span class="o">=</span> <span class="s2">"!="</span>  <span class="c1"># not equal to (string, int, float)</span>
    <span class="n">GTE</span> <span class="o">=</span> <span class="s2">"&gt;="</span>  <span class="c1"># greater than or equal to (int, float)</span>
    <span class="n">LTE</span> <span class="o">=</span> <span class="s2">"&lt;="</span>  <span class="c1"># less than or equal to (int, float)</span>
    <span class="n">IN</span> <span class="o">=</span> <span class="s2">"in"</span>  <span class="c1"># In array (string or number)</span>
    <span class="n">NIN</span> <span class="o">=</span> <span class="s2">"nin"</span>  <span class="c1"># Not in array (string or number)</span>
    <span class="n">ANY</span> <span class="o">=</span> <span class="s2">"any"</span>  <span class="c1"># Contains any (array of strings)</span>
    <span class="n">ALL</span> <span class="o">=</span> <span class="s2">"all"</span>  <span class="c1"># Contains all (array of strings)</span>
    <span class="n">TEXT_MATCH</span> <span class="o">=</span> <span class="s2">"text_match"</span>  <span class="c1"># full text match (allows you to search for a specific substring, token or phrase within the text field)</span>
    <span class="n">CONTAINS</span> <span class="o">=</span> <span class="s2">"contains"</span>  <span class="c1"># metadata array contains value (string or number)</span>
</code></pre></div></td></tr></tbody></table>

FilterCondition [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.FilterCondition "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `str`, `Enum`

Vector store filter conditions to combine different filters.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FilterCondition</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vector store filter conditions to combine different filters."""</span>

    <span class="c1"># TODO add more conditions</span>
    <span class="n">AND</span> <span class="o">=</span> <span class="s2">"and"</span>
    <span class="n">OR</span> <span class="o">=</span> <span class="s2">"or"</span>
</code></pre></div></td></tr></tbody></table>

MetadataFilter [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilter "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Comprehensive metadata filter for vector stores to support more operators.

Value uses Strict\* types, as int, float and str are compatible types and were all converted to string before.

See: https://docs.pydantic.dev/latest/usage/types/#strict-types

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 87</span>
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
<span class="normal">118</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetadataFilter</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Comprehensive metadata filter for vector stores to support more operators.</span>

<span class="sd">    Value uses Strict* types, as int, float and str are compatible types and were all</span>
<span class="sd">    converted to string before.</span>

<span class="sd">    See: https://docs.pydantic.dev/latest/usage/types/#strict-types</span>
<span class="sd">    """</span>

    <span class="n">key</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
        <span class="n">StrictInt</span><span class="p">,</span>
        <span class="n">StrictFloat</span><span class="p">,</span>
        <span class="n">StrictStr</span><span class="p">,</span>
        <span class="n">List</span><span class="p">[</span><span class="n">StrictStr</span><span class="p">],</span>
        <span class="n">List</span><span class="p">[</span><span class="n">StrictFloat</span><span class="p">],</span>
        <span class="n">List</span><span class="p">[</span><span class="n">StrictInt</span><span class="p">],</span>
    <span class="p">]</span>
    <span class="n">operator</span><span class="p">:</span> <span class="n">FilterOperator</span> <span class="o">=</span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">filter_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create MetadataFilter from dictionary.</span>

<span class="sd">        Args:</span>
<span class="sd">            filter_dict: Dict with key, value and operator.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">MetadataFilter</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">filter_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_dict `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilter.from_dict "Permanent link")

```
from_dict(filter_dict: Dict) -> [MetadataFilter](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilter "llama_index.core.vector_stores.types.MetadataFilter")
```

Create MetadataFilter from dictionary.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `filter_dict` | `Dict` | 
Dict with key, value and operator.



 | _required_ |

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
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
<span class="normal">118</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">filter_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create MetadataFilter from dictionary.</span>

<span class="sd">    Args:</span>
<span class="sd">        filter_dict: Dict with key, value and operator.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">MetadataFilter</span><span class="o">.</span><span class="n">parse_obj</span><span class="p">(</span><span class="n">filter_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

MetadataFilters [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Metadata filters for vector stores.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">131</span>
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
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetadataFilters</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Metadata filters for vector stores."""</span>

    <span class="c1"># Exact match filters and Advanced filters with operators like &gt;, &lt;, &gt;=, &lt;=, !=, etc.</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">MetadataFilter</span><span class="p">,</span> <span class="n">ExactMatchFilter</span><span class="p">,</span> <span class="s2">"MetadataFilters"</span><span class="p">]]</span>
    <span class="c1"># and/or such conditions for combining different filters</span>
    <span class="n">condition</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FilterCondition</span><span class="p">]</span> <span class="o">=</span> <span class="n">FilterCondition</span><span class="o">.</span><span class="n">AND</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@deprecated</span><span class="p">(</span>
        <span class="s2">"`from_dict()` is deprecated. "</span>
        <span class="s2">"Please use `MetadataFilters(filters=.., condition='and')` directly instead."</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">filter_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilters"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create MetadataFilters from json."""</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">filter_dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="n">MetadataFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="n">v</span><span class="p">,</span> <span class="n">operator</span><span class="o">=</span><span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">)</span>
            <span class="n">filters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">filter</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dicts</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">filter_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
        <span class="n">condition</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FilterCondition</span><span class="p">]</span> <span class="o">=</span> <span class="n">FilterCondition</span><span class="o">.</span><span class="n">AND</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilters"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create MetadataFilters from dicts.</span>

<span class="sd">        This takes in a list of individual MetadataFilter objects, along</span>
<span class="sd">        with the condition.</span>

<span class="sd">        Args:</span>
<span class="sd">            filter_dicts: List of dicts, each dict is a MetadataFilter.</span>
<span class="sd">            condition: FilterCondition to combine different filters.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
                <span class="n">MetadataFilter</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">filter_dict</span><span class="p">)</span> <span class="k">for</span> <span class="n">filter_dict</span> <span class="ow">in</span> <span class="n">filter_dicts</span>
            <span class="p">],</span>
            <span class="n">condition</span><span class="o">=</span><span class="n">condition</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">legacy_filters</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ExactMatchFilter</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Convert MetadataFilters to legacy ExactMatchFilters."""</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">filter</span><span class="o">.</span><span class="n">operator</span> <span class="o">!=</span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Vector Store only supports exact match filters. "</span>
                    <span class="s2">"Please use ExactMatchFilter or FilterOperator.EQ instead."</span>
                <span class="p">)</span>
            <span class="n">filters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ExactMatchFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">filters</span>
</code></pre></div></td></tr></tbody></table>

### from\_dict `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters.from_dict "Permanent link")

```
from_dict(filter_dict: Dict) -> [MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")
```

Create MetadataFilters from json.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@deprecated</span><span class="p">(</span>
    <span class="s2">"`from_dict()` is deprecated. "</span>
    <span class="s2">"Please use `MetadataFilters(filters=.., condition='and')` directly instead."</span>
<span class="p">)</span>
<span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">filter_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilters"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create MetadataFilters from json."""</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">filter_dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="nb">filter</span> <span class="o">=</span> <span class="n">MetadataFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="n">v</span><span class="p">,</span> <span class="n">operator</span><span class="o">=</span><span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">)</span>
        <span class="n">filters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">filter</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_dicts `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters.from_dicts "Permanent link")

```
from_dicts(filter_dicts: List[Dict], condition: Optional[[FilterCondition](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.FilterCondition "llama_index.core.vector_stores.types.FilterCondition")] = FilterCondition.AND) -> [MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")
```

Create MetadataFilters from dicts.

This takes in a list of individual MetadataFilter objects, along with the condition.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `filter_dicts` | `List[Dict]` | 
List of dicts, each dict is a MetadataFilter.



 | _required_ |
| `condition` | `Optional[[FilterCondition](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.FilterCondition "llama_index.core.vector_stores.types.FilterCondition")]` | 

FilterCondition to combine different filters.



 | `AND` |

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
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
<span class="normal">173</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_dicts</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">filter_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
    <span class="n">condition</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FilterCondition</span><span class="p">]</span> <span class="o">=</span> <span class="n">FilterCondition</span><span class="o">.</span><span class="n">AND</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"MetadataFilters"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create MetadataFilters from dicts.</span>

<span class="sd">    This takes in a list of individual MetadataFilter objects, along</span>
<span class="sd">    with the condition.</span>

<span class="sd">    Args:</span>
<span class="sd">        filter_dicts: List of dicts, each dict is a MetadataFilter.</span>
<span class="sd">        condition: FilterCondition to combine different filters.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
            <span class="n">MetadataFilter</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">filter_dict</span><span class="p">)</span> <span class="k">for</span> <span class="n">filter_dict</span> <span class="ow">in</span> <span class="n">filter_dicts</span>
        <span class="p">],</span>
        <span class="n">condition</span><span class="o">=</span><span class="n">condition</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### legacy\_filters [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters.legacy_filters "Permanent link")

```
legacy_filters() -> List[ExactMatchFilter]
```

Convert MetadataFilters to legacy ExactMatchFilters.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">legacy_filters</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ExactMatchFilter</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Convert MetadataFilters to legacy ExactMatchFilters."""</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">filter</span><span class="o">.</span><span class="n">operator</span> <span class="o">!=</span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Vector Store only supports exact match filters. "</span>
                <span class="s2">"Please use ExactMatchFilter or FilterOperator.EQ instead."</span>
            <span class="p">)</span>
        <span class="n">filters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ExactMatchFilter</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">filters</span>
</code></pre></div></td></tr></tbody></table>

VectorStoreQuerySpec [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuerySpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Schema for a structured request for vector store (i.e. to be converted to a VectorStoreQuery).

Currently only used by VectorIndexAutoRetriever.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorStoreQuerySpec</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Schema for a structured request for vector store</span>
<span class="sd">    (i.e. to be converted to a VectorStoreQuery).</span>

<span class="sd">    Currently only used by VectorIndexAutoRetriever.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">MetadataFilter</span><span class="p">]</span>
    <span class="n">top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

MetadataInfo [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataInfo "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Information about a metadata filter supported by a vector store.

Currently only used by VectorIndexAutoRetriever.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetadataInfo</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Information about a metadata filter supported by a vector store.</span>

<span class="sd">    Currently only used by VectorIndexAutoRetriever.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="nb">type</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span>
</code></pre></div></td></tr></tbody></table>

VectorStoreInfo [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreInfo "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Information about a vector store (content and supported metadata filters).

Currently only used by VectorIndexAutoRetriever.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorStoreInfo</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Information about a vector store (content and supported metadata filters).</span>

<span class="sd">    Currently only used by VectorIndexAutoRetriever.</span>
<span class="sd">    """</span>

    <span class="n">metadata_info</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">MetadataInfo</span><span class="p">]</span>
    <span class="n">content_info</span><span class="p">:</span> <span class="nb">str</span>
</code></pre></div></td></tr></tbody></table>

VectorStoreQuery `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Vector store query.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">221</span>
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
<span class="normal">247</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">VectorStoreQuery</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Vector store query."""</span>

    <span class="n">query_embedding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">doc_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">query_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">output_fields</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">embedding_field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">mode</span><span class="p">:</span> <span class="n">VectorStoreQueryMode</span> <span class="o">=</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span>

    <span class="c1"># NOTE: only for hybrid search (0 for bm25, 1 for vector search)</span>
    <span class="n">alpha</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="c1"># metadata filters</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="c1"># only for mmr</span>
    <span class="n">mmr_threshold</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="c1"># NOTE: currently only used by postgres hybrid search</span>
    <span class="n">sparse_top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="c1"># NOTE: return top k results from hybrid search. similarity_top_k is used for dense search top k</span>
    <span class="n">hybrid_top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

VectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `Protocol`

Abstract vector store protocol.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">250</span>
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
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@runtime_checkable</span>
<span class="k">class</span> <span class="nc">VectorStore</span><span class="p">(</span><span class="n">Protocol</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Abstract vector store protocol."""</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">is_embedding_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="o">...</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes with embedding to vector store."""</span>
        <span class="o">...</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Asynchronously add nodes with embedding to vector store.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call add synchronously.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id."""</span>
        <span class="o">...</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call delete synchronously.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query vector store."""</span>
        <span class="o">...</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Asynchronously query vector store.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call query synchronously.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.client "Permanent link")

```
client: Any
```

Get client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes with embedding to vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes with embedding to vector store."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### async\_add `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.async_add "Permanent link")

```
async_add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[str]
```

Asynchronously add nodes with embedding to vector store. NOTE: this is not implemented for all vector stores. If not implemented, it will just call add synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Asynchronously add nodes with embedding to vector store.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call add synchronously.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.adelete "Permanent link")

```
adelete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id. NOTE: this is not implemented for all vector stores. If not implemented, it will just call delete synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call delete synchronously.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query vector store."""</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### aquery `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStore.aquery "Permanent link")

```
aquery(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Asynchronously query vector store. NOTE: this is not implemented for all vector stores. If not implemented, it will just call query synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Asynchronously query vector store.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call query synchronously.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

BasePydanticVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseComponent "llama_index.core.schema.BaseComponent")`, `ABC`

Abstract vector store protocol.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BasePydanticVectorStore</span><span class="p">(</span><span class="n">BaseComponent</span><span class="p">,</span> <span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Abstract vector store protocol."""</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">is_embedding_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>

    <span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from vector store."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"get_nodes not implemented"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Asynchronously get nodes from vector store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">filters</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to vector store."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Asynchronously add nodes to vector store.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call add synchronously.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call delete synchronously.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete nodes from vector store."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"delete_nodes not implemented"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronously delete nodes from vector store."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">filters</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Clear all nodes from configured vector store."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"clear not implemented"</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aclear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Asynchronously clear all nodes from configured vector store."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query vector store."""</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Asynchronously query vector store.</span>
<span class="sd">        NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">        it will just call query synchronously.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### client `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.client "Permanent link")

```
client: Any
```

Get client.

### get\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.get_nodes "Permanent link")

```
get_nodes(node_ids: Optional[List[str]] = None, filters: Optional[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")] = None) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from vector store."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"get_nodes not implemented"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aget\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.aget_nodes "Permanent link")

```
aget_nodes(node_ids: Optional[List[str]] = None, filters: Optional[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")] = None) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Asynchronously get nodes from vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Asynchronously get nodes from vector store."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">filters</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]) -> List[str]
```

Add nodes to vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to vector store."""</span>
</code></pre></div></td></tr></tbody></table>

### async\_add `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.async_add "Permanent link")

```
async_add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[str]
```

Asynchronously add nodes to vector store. NOTE: this is not implemented for all vector stores. If not implemented, it will just call add synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">async_add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Asynchronously add nodes to vector store.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call add synchronously.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id."""</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.adelete "Permanent link")

```
adelete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id. NOTE: this is not implemented for all vector stores. If not implemented, it will just call delete synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call delete synchronously.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.delete_nodes "Permanent link")

```
delete_nodes(node_ids: Optional[List[str]] = None, filters: Optional[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")] = None, **delete_kwargs: Any) -> None
```

Delete nodes from vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete nodes from vector store."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"delete_nodes not implemented"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### adelete\_nodes `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.adelete_nodes "Permanent link")

```
adelete_nodes(node_ids: Optional[List[str]] = None, filters: Optional[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")] = None, **delete_kwargs: Any) -> None
```

Asynchronously delete nodes from vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Asynchronously delete nodes from vector store."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">delete_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">filters</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### clear [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.clear "Permanent link")

```
clear() -> None
```

Clear all nodes from configured vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Clear all nodes from configured vector store."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"clear not implemented"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aclear `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.aclear "Permanent link")

```
aclear() -> None
```

Asynchronously clear all nodes from configured vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aclear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Asynchronously clear all nodes from configured vector store."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### query `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query vector store.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query vector store."""</span>
</code></pre></div></td></tr></tbody></table>

### aquery `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore.aquery "Permanent link")

```
aquery(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Asynchronously query vector store. NOTE: this is not implemented for all vector stores. If not implemented, it will just call query synchronously.

Source code in `llama-index-core/llama_index/core/vector_stores/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aquery</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Asynchronously query vector store.</span>
<span class="sd">    NOTE: this is not implemented for all vector stores. If not implemented,</span>
<span class="sd">    it will just call query synchronously.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Hologres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/)[Next Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/)
