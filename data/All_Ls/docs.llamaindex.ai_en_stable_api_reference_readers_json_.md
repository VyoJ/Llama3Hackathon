Title: Json - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/json/

Markdown Content:
Json - LlamaIndex


JSONReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/#llama_index.readers.json.JSONReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

JSON reader.

Reads JSON documents with options to help us out relationships between nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `levels_back` | `int` | 
the number of levels to go back in the JSON tree, 0 if you want all levels. If levels\_back is None, then we just format the JSON and make each line an embedding



 | `None` |
| `collapse_length` | `int` | 

the maximum number of characters a JSON fragment would be collapsed in the output (levels\_back needs to be not None) ex: if collapse\_length = 10, and input is {a: \[1, 2, 3\], b: {"hello": "world", "foo": "bar"}} then a would be collapsed into one line, while b would not. Recommend starting around 100 and then adjusting from there.



 | `None` |
| `is_jsonl` | `Optional[bool]` | 

If True, indicates that the file is in JSONL format.



 | `False` |
| `clean_json` | `Optional[bool]` | 

If True, lines containing only JSON structure are removed.



 | `True` |

Source code in `llama-index-integrations/readers/llama-index-readers-json/llama_index/readers/json/base.py`

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
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JSONReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""JSON reader.</span>

<span class="sd">    Reads JSON documents with options to help us out relationships between nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        levels_back (int): the number of levels to go back in the JSON tree, 0</span>
<span class="sd">          if you want all levels. If levels_back is None, then we just format the</span>
<span class="sd">          JSON and make each line an embedding</span>

<span class="sd">        collapse_length (int): the maximum number of characters a JSON fragment</span>
<span class="sd">          would be collapsed in the output (levels_back needs to be not None)</span>
<span class="sd">          ex: if collapse_length = 10, and</span>
<span class="sd">          input is {a: [1, 2, 3], b: {"hello": "world", "foo": "bar"}}</span>
<span class="sd">          then a would be collapsed into one line, while b would not.</span>
<span class="sd">          Recommend starting around 100 and then adjusting from there.</span>

<span class="sd">        is_jsonl (Optional[bool]): If True, indicates that the file is in JSONL format.</span>
<span class="sd">        Defaults to False.</span>

<span class="sd">        clean_json (Optional[bool]): If True, lines containing only JSON structure are removed.</span>
<span class="sd">        This removes lines that are not as useful. If False, no lines are removed and the document maintains a valid JSON object structure.</span>
<span class="sd">        If levels_back is set the json is not cleaned and this option is ignored.</span>
<span class="sd">        Defaults to True.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">levels_back</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collapse_length</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ensure_ascii</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">is_jsonl</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">clean_json</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with arguments."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="o">=</span> <span class="n">levels_back</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">collapse_length</span> <span class="o">=</span> <span class="n">collapse_length</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span> <span class="o">=</span> <span class="n">ensure_ascii</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_jsonl</span> <span class="o">=</span> <span class="n">is_jsonl</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">clean_json</span> <span class="o">=</span> <span class="n">clean_json</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input file."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">load_data</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_jsonl</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span>
                    <span class="n">load_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">load_data</span> <span class="o">=</span> <span class="p">[</span><span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)]</span>

            <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">load_data</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">clean_json</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
                    <span class="c1"># If levels_back isn't set and clean json is set,</span>
                    <span class="c1"># remove lines containing only formatting, we just format and make each</span>
                    <span class="c1"># line an embedding</span>
                    <span class="n">json_output</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                        <span class="n">data</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span>
                    <span class="p">)</span>
                    <span class="n">lines</span> <span class="o">=</span> <span class="n">json_output</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
                    <span class="n">useful_lines</span> <span class="o">=</span> <span class="p">[</span>
                        <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^[</span><span class="si">{}</span><span class="s2">\[\],]*$"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
                    <span class="p">]</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">useful_lines</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
                    <span class="p">)</span>

                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">clean_json</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
                    <span class="c1"># If levels_back isn't set  and clean json is False, create documents without cleaning</span>
                    <span class="n">json_output</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span><span class="p">)</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json_output</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="c1"># If levels_back is set, we make the embeddings contain the labels</span>
                    <span class="c1"># from further up the JSON tree</span>
                    <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span>
                        <span class="o">*</span><span class="n">_depth_first_yield</span><span class="p">(</span>
                            <span class="n">data</span><span class="p">,</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span><span class="p">,</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">collapse_length</span><span class="p">,</span>
                            <span class="p">[],</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span><span class="p">,</span>
                        <span class="p">)</span>
                    <span class="p">]</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
                    <span class="p">)</span>
            <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/#llama_index.readers.json.JSONReader.load_data "Permanent link")

```
load_data(input_file: str, extra_info: Optional[Dict] = {}) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input file.

Source code in `llama-index-integrations/readers/llama-index-readers-json/llama_index/readers/json/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 93</span>
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
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input file."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">input_file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">load_data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_jsonl</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">load_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">load_data</span> <span class="o">=</span> <span class="p">[</span><span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)]</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">load_data</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">clean_json</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
                <span class="c1"># If levels_back isn't set and clean json is set,</span>
                <span class="c1"># remove lines containing only formatting, we just format and make each</span>
                <span class="c1"># line an embedding</span>
                <span class="n">json_output</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                    <span class="n">data</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span>
                <span class="p">)</span>
                <span class="n">lines</span> <span class="o">=</span> <span class="n">json_output</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">useful_lines</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^[</span><span class="si">{}</span><span class="s2">\[\],]*$"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
                <span class="p">]</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">useful_lines</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
                <span class="p">)</span>

            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">clean_json</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
                <span class="c1"># If levels_back isn't set  and clean json is False, create documents without cleaning</span>
                <span class="n">json_output</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span><span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">json_output</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="c1"># If levels_back is set, we make the embeddings contain the labels</span>
                <span class="c1"># from further up the JSON tree</span>
                <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="o">*</span><span class="n">_depth_first_yield</span><span class="p">(</span>
                        <span class="n">data</span><span class="p">,</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">levels_back</span><span class="p">,</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">collapse_length</span><span class="p">,</span>
                        <span class="p">[],</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">]</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Joplin](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/)[Next Kaltura esearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/kaltura_esearch/)
