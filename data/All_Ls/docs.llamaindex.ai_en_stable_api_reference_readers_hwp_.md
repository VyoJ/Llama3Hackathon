Title: Hwp - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/

Markdown Content:
Hwp - LlamaIndex


HWPReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/#llama_index.readers.hwp.HWPReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Hwp Reader. Reads contents from Hwp file. Args: None.

Source code in `llama-index-integrations/readers/llama-index-readers-hwp/llama_index/readers/hwp/base.py`

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
<span class="normal">111</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HWPReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hwp Reader. Reads contents from Hwp file.</span>
<span class="sd">    Args: None.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">FILE_HEADER_SECTION</span> <span class="o">=</span> <span class="s2">"FileHeader"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">HWP_SUMMARY_SECTION</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\x05</span><span class="s2">HwpSummaryInformation"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">SECTION_NAME_LENGTH</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="s2">"Section"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">BODYTEXT_SECTION</span> <span class="o">=</span> <span class="s2">"BodyText"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">HWP_TEXT_TAGS</span> <span class="o">=</span> <span class="p">[</span><span class="mi">67</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data and extract table from Hwp file.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path for the Hwp file.</span>


<span class="sd">        Returns:</span>
<span class="sd">            List[Document].</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">olefile</span>

        <span class="n">load_file</span> <span class="o">=</span> <span class="n">olefile</span><span class="o">.</span><span class="n">OleFileIO</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">file_dir</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">listdir</span><span class="p">()</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_valid</span><span class="p">(</span><span class="n">file_dir</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Not Valid HwpFile"</span><span class="p">)</span>

        <span class="n">result_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">file_dir</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">is_valid</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span>
        <span class="k">if</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">FILE_HEADER_SECTION</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">HWP_SUMMARY_SECTION</span><span class="p">]</span> <span class="ow">in</span> <span class="n">dirs</span>

    <span class="k">def</span> <span class="nf">get_body_sections</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span>
        <span class="n">m</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">d</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o"></span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">get_text_from_section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">,</span> <span class="n">section</span><span class="p">):</span>
        <span class="n">bodytext</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">openstream</span><span class="p">(</span><span class="n">section</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">bodytext</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

        <span class="n">unpacked_data</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">zlib</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="o">-</span><span class="mi">15</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_compressed</span><span class="p">(</span><span class="n">load_file</span><span class="p">)</span> <span class="k">else</span> <span class="n">data</span>
        <span class="p">)</span>
        <span class="n">size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">unpacked_data</span><span class="p">)</span>

        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">size</span><span class="p">:</span>
            <span class="n">header</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack_from</span><span class="p">(</span><span class="s2">"&lt;I"</span><span class="p">,</span> <span class="n">unpacked_data</span><span class="p">,</span> <span class="n">i</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">rec_type</span> <span class="o">=</span> <span class="n">header</span> <span class="o">&amp;</span> <span class="mh">0x3FF</span>
            <span class="p">(</span><span class="n">header</span> <span class="o">&gt;&gt;</span> <span class="mi">10</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0x3FF</span>
            <span class="n">rec_len</span> <span class="o">=</span> <span class="p">(</span><span class="n">header</span> <span class="o">&gt;&gt;</span> <span class="mi">20</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0xFFF</span>

            <span class="k">if</span> <span class="n">rec_type</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">HWP_TEXT_TAGS</span><span class="p">:</span>
                <span class="n">rec_data</span> <span class="o">=</span> <span class="n">unpacked_data</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">4</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">rec_len</span><span class="p">]</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">rec_data</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-16"</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>

            <span class="n">i</span> <span class="o">+=</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">rec_len</span>

        <span class="k">return</span> <span class="n">text</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/#llama_index.readers.hwp.HWPReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data and extract table from Hwp file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Path` | 
Path for the Hwp file.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\].



 |

Source code in `llama-index-integrations/readers/llama-index-readers-hwp/llama_index/readers/hwp/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
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
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data and extract table from Hwp file.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path for the Hwp file.</span>


<span class="sd">    Returns:</span>
<span class="sd">        List[Document].</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">olefile</span>

    <span class="n">load_file</span> <span class="o">=</span> <span class="n">olefile</span><span class="o">.</span><span class="n">OleFileIO</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">file_dir</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">listdir</span><span class="p">()</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_valid</span><span class="p">(</span><span class="n">file_dir</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Not Valid HwpFile"</span><span class="p">)</span>

    <span class="n">result_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">file_dir</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Huggingface fs](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/)[Next Iceberg](https://docs.llamaindex.ai/en/stable/api_reference/readers/iceberg/)
