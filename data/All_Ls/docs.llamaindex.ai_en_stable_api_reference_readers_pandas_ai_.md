Title: Pandas ai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/

Markdown Content:
Pandas ai - LlamaIndex


PandasAIReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/#llama_index.readers.pandas_ai.PandasAIReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pandas AI reader.

Light wrapper around https://github.com/gventuri/pandas-ai.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `llm` | `Optional[llm]` | 
LLM to use. Defaults to None.



 | `None` |
| `concat_rows` | `bool` | 

whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |
| `col_joiner` | `str` | 

Separator to use for joining cols per row. Set to ", " by default.



 | `', '` |
| `row_joiner` | `str` | 

Separator to use for joining each row. Only used when `concat_rows=True`. Set to "\\n" by default.



 | `'\n'` |
| `pandas_config` | `dict` | 

Options for the `pandas.read_csv` function call. Refer to https://pandas.pydata.org/docs/reference/api/pandas.read\_csv.html for more information. Set to empty dict by default, this means pandas will try to figure out the separators, table head, etc. on its own.



 | `{}` |

Source code in `llama-index-integrations/readers/llama-index-readers-pandas-ai/llama_index/readers/pandas_ai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasAIReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""Pandas AI reader.</span>

<span class="sd">    Light wrapper around https://github.com/gventuri/pandas-ai.</span>

<span class="sd">    Args:</span>
<span class="sd">        llm (Optional[pandas.llm]): LLM to use. Defaults to None.</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">        col_joiner (str): Separator to use for joining cols per row.</span>
<span class="sd">            Set to ", " by default.</span>

<span class="sd">        row_joiner (str): Separator to use for joining each row.</span>
<span class="sd">            Only used when `concat_rows=True`.</span>
<span class="sd">            Set to "\n" by default.</span>

<span class="sd">        pandas_config (dict): Options for the `pandas.read_csv` function call.</span>
<span class="sd">            Refer to https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html</span>
<span class="sd">            for more information.</span>
<span class="sd">            Set to empty dict by default, this means pandas will try to figure</span>
<span class="sd">            out the separators, table head, etc. on its own.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">col_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">", "</span><span class="p">,</span>
        <span class="n">row_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">pandas_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pandasai</span> <span class="kn">import</span> <span class="n">PandasAI</span>
            <span class="kn">from</span> <span class="nn">pandasai.llm.openai</span> <span class="kn">import</span> <span class="n">OpenAI</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install pandasai to use this reader."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_ai</span> <span class="o">=</span> <span class="n">PandasAI</span><span class="p">(</span><span class="n">llm</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span> <span class="o">=</span> <span class="n">col_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span> <span class="o">=</span> <span class="n">row_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span> <span class="o">=</span> <span class="n">pandas_config</span>

    <span class="k">def</span> <span class="nf">run_pandas_ai</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">initial_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">is_conversational_answer</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load dataframe."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_ai</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">initial_df</span><span class="p">,</span> <span class="n">prompt</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">is_conversational_answer</span><span class="o">=</span><span class="n">is_conversational_answer</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">initial_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">is_conversational_answer</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_pandas_ai</span><span class="p">(</span>
            <span class="n">initial_df</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">is_conversational_answer</span><span class="o">=</span><span class="n">is_conversational_answer</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">is_conversational_answer</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">)]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">generic</span><span class="p">)):</span>
                <span class="n">result</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)):</span>
                <span class="k">pass</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unexpected type for result: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="c1"># if not conversational answer, use Pandas CSV Reader</span>
            <span class="n">reader</span> <span class="o">=</span> <span class="n">PandasCSVReader</span><span class="p">(</span>
                <span class="n">concat_rows</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">,</span>
                <span class="n">col_joiner</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">,</span>
                <span class="n">row_joiner</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">,</span>
                <span class="n">pandas_config</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">with</span> <span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmpdir</span><span class="p">:</span>
                <span class="n">outpath</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">tmpdir</span><span class="p">)</span> <span class="o">/</span> <span class="s2">"out.csv"</span>
                <span class="k">with</span> <span class="n">outpath</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                    <span class="c1"># TODO: add option to specify index=False</span>
                    <span class="n">result</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

                <span class="k">return</span> <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">outpath</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run\_pandas\_ai [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/#llama_index.readers.pandas_ai.PandasAIReader.run_pandas_ai "Permanent link")

```
run_pandas_ai(initial_df: DataFrame, query: str, is_conversational_answer: bool = False) -> Any
```

Load dataframe.

Source code in `llama-index-integrations/readers/llama-index-readers-pandas-ai/llama_index/readers/pandas_ai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run_pandas_ai</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">initial_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">is_conversational_answer</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load dataframe."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_ai</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
        <span class="n">initial_df</span><span class="p">,</span> <span class="n">prompt</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">is_conversational_answer</span><span class="o">=</span><span class="n">is_conversational_answer</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/#llama_index.readers.pandas_ai.PandasAIReader.load_data "Permanent link")

```
load_data(initial_df: DataFrame, query: str, is_conversational_answer: bool = False) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-pandas-ai/llama_index/readers/pandas_ai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 74</span>
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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">initial_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">is_conversational_answer</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">run_pandas_ai</span><span class="p">(</span>
        <span class="n">initial_df</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">is_conversational_answer</span><span class="o">=</span><span class="n">is_conversational_answer</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">is_conversational_answer</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">)]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">generic</span><span class="p">)):</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)):</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unexpected type for result: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="c1"># if not conversational answer, use Pandas CSV Reader</span>
        <span class="n">reader</span> <span class="o">=</span> <span class="n">PandasCSVReader</span><span class="p">(</span>
            <span class="n">concat_rows</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">,</span>
            <span class="n">col_joiner</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">,</span>
            <span class="n">row_joiner</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">,</span>
            <span class="n">pandas_config</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">with</span> <span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmpdir</span><span class="p">:</span>
            <span class="n">outpath</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">tmpdir</span><span class="p">)</span> <span class="o">/</span> <span class="s2">"out.csv"</span>
            <span class="k">with</span> <span class="n">outpath</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="c1"># TODO: add option to specify index=False</span>
                <span class="n">result</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

            <span class="k">return</span> <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">outpath</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/)[Next Papers](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/)
