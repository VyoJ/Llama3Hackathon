Title: Gpt repo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/

Markdown Content:
Gpt repo - LlamaIndex


Init file.

GPTRepoReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/#llama_index.readers.gpt_repo.GPTRepoReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

GPTRepoReader.

Reads a github repo in a prompt-friendly format.

Source code in `llama-index-integrations/readers/llama-index-readers-gpt-repo/llama_index/readers/gpt_repo/base.py`

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
<span class="normal">162</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GPTRepoReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""GPTRepoReader.</span>

<span class="sd">    Reads a github repo in a prompt-friendly format.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">concatenate</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">concatenate</span> <span class="o">=</span> <span class="n">concatenate</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">repo_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">preamble_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">extensions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">encoding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            pages (List[str]): List of pages to read.</span>

<span class="sd">        """</span>
        <span class="n">ignore_file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">repo_path</span><span class="p">,</span> <span class="s2">".gptignore"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">ignore_file_path</span><span class="p">):</span>
            <span class="n">ignore_list</span> <span class="o">=</span> <span class="n">get_ignore_list</span><span class="p">(</span><span class="n">ignore_file_path</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">ignore_list</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">output_text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="n">preamble_str</span><span class="p">:</span>
            <span class="n">output_text</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">preamble_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">concatenate</span><span class="p">:</span>
            <span class="n">output_text</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="s2">"The following text is a Git repository with code. "</span>
                <span class="s2">"The structure of the text are sections that begin with ----, "</span>
                <span class="s2">"followed by a single line containing the file path and file "</span>
                <span class="s2">"name, followed by a variable amount of lines containing the "</span>
                <span class="s2">"file contents. The text representing the Git repository ends "</span>
                <span class="s2">"when the symbols --END-- are encountered. Any further text beyond "</span>
                <span class="s2">"--END-- are meant to be interpreted as instructions using the "</span>
                <span class="s2">"aforementioned Git repository as context.</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># self.concatenate is False</span>
            <span class="n">output_text</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="s2">"The following text is a file in a Git repository. "</span>
                <span class="s2">"The structure of the text are sections that begin with ----, "</span>
                <span class="s2">"followed by a single line containing the file path and file "</span>
                <span class="s2">"name, followed by a variable amount of lines containing the "</span>
                <span class="s2">"file contents. The text representing the file ends "</span>
                <span class="s2">"when the symbols --END-- are encountered. Any further text beyond "</span>
                <span class="s2">"--END-- are meant to be interpreted as instructions using the "</span>
                <span class="s2">"aforementioned file as context.</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="n">process_repository</span><span class="p">(</span>
            <span class="n">repo_path</span><span class="p">,</span>
            <span class="n">ignore_list</span><span class="p">,</span>
            <span class="n">concatenate</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">concatenate</span><span class="p">,</span>
            <span class="n">extensions</span><span class="o">=</span><span class="n">extensions</span><span class="p">,</span>
            <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">:</span>
            <span class="n">doc_text</span> <span class="o">=</span> <span class="n">output_text</span> <span class="o">+</span> <span class="n">text</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">--END--</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc_text</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/#llama_index.readers.gpt_repo.GPTRepoReader.load_data "Permanent link")

```
load_data(repo_path: str, preamble_str: Optional[str] = None, extensions: Optional[List[str]] = None, encoding: Optional[str] = 'utf-8') -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pages` | `List[str]` | 
List of pages to read.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-gpt-repo/llama_index/readers/gpt_repo/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">104</span>
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
<span class="normal">162</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">repo_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">preamble_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">extensions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">encoding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        pages (List[str]): List of pages to read.</span>

<span class="sd">    """</span>
    <span class="n">ignore_file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">repo_path</span><span class="p">,</span> <span class="s2">".gptignore"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">ignore_file_path</span><span class="p">):</span>
        <span class="n">ignore_list</span> <span class="o">=</span> <span class="n">get_ignore_list</span><span class="p">(</span><span class="n">ignore_file_path</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">ignore_list</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">output_text</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">if</span> <span class="n">preamble_str</span><span class="p">:</span>
        <span class="n">output_text</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">preamble_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">concatenate</span><span class="p">:</span>
        <span class="n">output_text</span> <span class="o">+=</span> <span class="p">(</span>
            <span class="s2">"The following text is a Git repository with code. "</span>
            <span class="s2">"The structure of the text are sections that begin with ----, "</span>
            <span class="s2">"followed by a single line containing the file path and file "</span>
            <span class="s2">"name, followed by a variable amount of lines containing the "</span>
            <span class="s2">"file contents. The text representing the Git repository ends "</span>
            <span class="s2">"when the symbols --END-- are encountered. Any further text beyond "</span>
            <span class="s2">"--END-- are meant to be interpreted as instructions using the "</span>
            <span class="s2">"aforementioned Git repository as context.</span><span class="se">\n</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># self.concatenate is False</span>
        <span class="n">output_text</span> <span class="o">+=</span> <span class="p">(</span>
            <span class="s2">"The following text is a file in a Git repository. "</span>
            <span class="s2">"The structure of the text are sections that begin with ----, "</span>
            <span class="s2">"followed by a single line containing the file path and file "</span>
            <span class="s2">"name, followed by a variable amount of lines containing the "</span>
            <span class="s2">"file contents. The text representing the file ends "</span>
            <span class="s2">"when the symbols --END-- are encountered. Any further text beyond "</span>
            <span class="s2">"--END-- are meant to be interpreted as instructions using the "</span>
            <span class="s2">"aforementioned file as context.</span><span class="se">\n</span><span class="s2">"</span>
        <span class="p">)</span>
    <span class="n">text_list</span> <span class="o">=</span> <span class="n">process_repository</span><span class="p">(</span>
        <span class="n">repo_path</span><span class="p">,</span>
        <span class="n">ignore_list</span><span class="p">,</span>
        <span class="n">concatenate</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">concatenate</span><span class="p">,</span>
        <span class="n">extensions</span><span class="o">=</span><span class="n">extensions</span><span class="p">,</span>
        <span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">:</span>
        <span class="n">doc_text</span> <span class="o">=</span> <span class="n">output_text</span> <span class="o">+</span> <span class="n">text</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">--END--</span><span class="se">\n</span><span class="s2">"</span>
        <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc_text</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Google](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/)[Next Graphdb cypher](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/)
