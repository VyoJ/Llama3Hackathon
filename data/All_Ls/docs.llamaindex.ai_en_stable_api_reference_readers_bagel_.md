Title: Bagel - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/

Markdown Content:
Bagel - LlamaIndex


BagelReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/#llama_index.readers.bagel.BagelReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Reader for Bagel files.

Source code in `llama-index-integrations/readers/llama-index-readers-bagel/llama_index/readers/bagel/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 51</span>
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
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BagelReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Reader for Bagel files."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize BagelReader.</span>

<span class="sd">        Args: collection_name: Name of the collection to load from.</span>

<span class="sd">        Returns: None</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">bagel</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`bagel` package not found, please run `pip install bagel`"</span>
            <span class="p">)</span>
        <span class="kn">from</span> <span class="nn">bagel.config</span> <span class="kn">import</span> <span class="n">Settings</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">collection_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"collection_name cannot be empty"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span> <span class="o">=</span> <span class="n">collection_name</span>

        <span class="n">server_settings</span> <span class="o">=</span> <span class="n">Settings</span><span class="p">(</span>
            <span class="n">bagel_api_impl</span><span class="o">=</span><span class="s2">"rest"</span><span class="p">,</span> <span class="n">bagel_server_host</span><span class="o">=</span><span class="s2">"api.bageldb.ai"</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">bagel</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="n">server_settings</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get_cluster</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">create_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create documents from the results.</span>

<span class="sd">        Args:</span>
<span class="sd">            results: Results from the query.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of documents.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># create a list of results</span>
        <span class="n">all_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span>
            <span class="nb">zip</span><span class="p">(</span>
                <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
                <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
                <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
                <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="c1"># iterate through the results</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">all_results</span><span class="p">:</span>
            <span class="c1"># create a Llama Document</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">doc_id</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
                <span class="n">embedding</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">OneOrMany</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">OneOrMany</span><span class="p">[</span><span class="n">Doc</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Where</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">where_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WhereDocument</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include</span><span class="p">:</span> <span class="n">Include</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the top n_results documents for provided query_embeddings or query_texts.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_embeddings: The embeddings to get the closes neighbors of. Optional.</span>
<span class="sd">            query_texts: The document texts to get the closes neighbors of. Optional.</span>
<span class="sd">            n_results: The number of neighbors to return for each query. Optional.</span>
<span class="sd">            where: A Where type dict used to filter results by. Optional.</span>
<span class="sd">            where_document: A WhereDocument type dict used to filter. Optional.</span>
<span class="sd">            include: A list of what to include in the results. Optional.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Llama Index Document(s) with the closest embeddings to the</span>
<span class="sd">            query_embeddings or query_texts.</span>
<span class="sd">        """</span>
        <span class="c1"># get the results from the collection</span>
        <span class="c1"># If neither query_embeddings nor query_texts are provided,</span>
        <span class="c1"># or both are provided, raise an error</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">query_vector</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query_texts</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="n">query_vector</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query_texts</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"You must provide either embeddings or texts to find, but not both"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">where</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="n">where_document</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">where_document</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
            <span class="n">query_embeddings</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
            <span class="n">query_texts</span><span class="o">=</span><span class="n">query_texts</span><span class="p">,</span>
            <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
            <span class="n">include</span><span class="o">=</span><span class="n">include</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># check if there are results</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">results</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No results found"</span><span class="p">)</span>

        <span class="c1"># check if there are embeddings or documents</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">]</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">]:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No embeddings or documents found"</span><span class="p">)</span>

        <span class="c1"># create documents from the results</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/#llama_index.readers.bagel.BagelReader.create_documents "Permanent link")

```
create_documents(results: Any) -> Any
```

Create documents from the results.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `results` | `Any` | 
Results from the query.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `Any` | 
List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-bagel/llama_index/readers/bagel/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 82</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">results</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create documents from the results.</span>

<span class="sd">    Args:</span>
<span class="sd">        results: Results from the query.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of documents.</span>
<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># create a list of results</span>
    <span class="n">all_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span>
        <span class="nb">zip</span><span class="p">(</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="p">)</span>
    <span class="p">)</span>
    <span class="c1"># iterate through the results</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">all_results</span><span class="p">:</span>
        <span class="c1"># create a Llama Document</span>
        <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">doc_id</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
            <span class="n">embedding</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/#llama_index.readers.bagel.BagelReader.load_data "Permanent link")

```
load_data(query_vector: Optional[OneOrMany[Embedding]] = None, query_texts: Optional[OneOrMany[Doc]] = None, limit: int = 10, where: Optional[Where] = None, where_document: Optional[WhereDocument] = None, include: Include = ['metadatas', 'documents', 'embeddings', 'distances']) -> Any
```

Get the top n\_results documents for provided query\_embeddings or query\_texts.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_embeddings` |  | 
The embeddings to get the closes neighbors of. Optional.



 | _required_ |
| `query_texts` | `Optional[OneOrMany[Doc]]` | 

The document texts to get the closes neighbors of. Optional.



 | `None` |
| `n_results` |  | 

The number of neighbors to return for each query. Optional.



 | _required_ |
| `where` | `Optional[Where]` | 

A Where type dict used to filter results by. Optional.



 | `None` |
| `where_document` | `Optional[WhereDocument]` | 

A WhereDocument type dict used to filter. Optional.



 | `None` |
| `include` | `Include` | 

A list of what to include in the results. Optional.



 | `['metadatas', 'documents', 'embeddings', 'distances']` |

**Returns:**

| Type | Description |
| --- | --- |
| `Any` | 
Llama Index Document(s) with the closest embeddings to the



 |
| `Any` | 

query\_embeddings or query\_texts.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-bagel/llama_index/readers/bagel/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">114</span>
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
<span class="normal">171</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">OneOrMany</span><span class="p">[</span><span class="n">Embedding</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">query_texts</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">OneOrMany</span><span class="p">[</span><span class="n">Doc</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Where</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">where_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WhereDocument</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include</span><span class="p">:</span> <span class="n">Include</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"metadatas"</span><span class="p">,</span> <span class="s2">"documents"</span><span class="p">,</span> <span class="s2">"embeddings"</span><span class="p">,</span> <span class="s2">"distances"</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the top n_results documents for provided query_embeddings or query_texts.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_embeddings: The embeddings to get the closes neighbors of. Optional.</span>
<span class="sd">        query_texts: The document texts to get the closes neighbors of. Optional.</span>
<span class="sd">        n_results: The number of neighbors to return for each query. Optional.</span>
<span class="sd">        where: A Where type dict used to filter results by. Optional.</span>
<span class="sd">        where_document: A WhereDocument type dict used to filter. Optional.</span>
<span class="sd">        include: A list of what to include in the results. Optional.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Llama Index Document(s) with the closest embeddings to the</span>
<span class="sd">        query_embeddings or query_texts.</span>
<span class="sd">    """</span>
    <span class="c1"># get the results from the collection</span>
    <span class="c1"># If neither query_embeddings nor query_texts are provided,</span>
    <span class="c1"># or both are provided, raise an error</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">query_vector</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query_texts</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
        <span class="n">query_vector</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">query_texts</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"You must provide either embeddings or texts to find, but not both"</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">where</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="k">if</span> <span class="n">where_document</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">where_document</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">find</span><span class="p">(</span>
        <span class="n">query_embeddings</span><span class="o">=</span><span class="n">query_vector</span><span class="p">,</span>
        <span class="n">query_texts</span><span class="o">=</span><span class="n">query_texts</span><span class="p">,</span>
        <span class="n">n_results</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
        <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
        <span class="n">where_document</span><span class="o">=</span><span class="n">where_document</span><span class="p">,</span>
        <span class="n">include</span><span class="o">=</span><span class="n">include</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="c1"># check if there are results</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">results</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No results found"</span><span class="p">)</span>

    <span class="c1"># check if there are embeddings or documents</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">results</span><span class="p">[</span><span class="s2">"embeddings"</span><span class="p">]</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"No embeddings or documents found"</span><span class="p">)</span>

    <span class="c1"># create documents from the results</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_documents</span><span class="p">(</span><span class="n">results</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure devops](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/)[Next Bilibili](https://docs.llamaindex.ai/en/stable/api_reference/readers/bilibili/)
