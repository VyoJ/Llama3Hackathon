Title: Code - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/

Markdown Content:
Code - LlamaIndex


Node parsers.

CodeSplitter [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/#llama_index.core.node_parser.CodeSplitter "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `TextSplitter`

Split code using a AST parser.

Thank you to Kevin Lu / SweepAI for suggesting this elegant code splitting solution. https://docs.sweep.dev/blogs/chunking-2m-files

Source code in `llama-index-core/llama_index/core/node_parser/text/code.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
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
<span class="normal">161</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CodeSplitter</span><span class="p">(</span><span class="n">TextSplitter</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Split code using a AST parser.</span>

<span class="sd">    Thank you to Kevin Lu / SweepAI for suggesting this elegant code splitting solution.</span>
<span class="sd">    https://docs.sweep.dev/blogs/chunking-2m-files</span>
<span class="sd">    """</span>

    <span class="n">language</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The programming language of the code being split."</span>
    <span class="p">)</span>
    <span class="n">chunk_lines</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CHUNK_LINES</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of lines to include in each chunk."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">chunk_lines_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_LINES_OVERLAP</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"How many lines of code each chunk overlaps with."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">max_chars</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_MAX_CHARS</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Maximum number of characters per chunk."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">_parser</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">language</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chunk_lines</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_LINES</span><span class="p">,</span>
        <span class="n">chunk_lines_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_LINES_OVERLAP</span><span class="p">,</span>
        <span class="n">max_chars</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_CHARS</span><span class="p">,</span>
        <span class="n">parser</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_prev_next_rel</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">id_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Document</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a CodeSplitter."""</span>
        <span class="kn">from</span> <span class="nn">tree_sitter</span> <span class="kn">import</span> <span class="n">Parser</span>  <span class="c1"># pants: no-infer-dep</span>

        <span class="k">if</span> <span class="n">parser</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">tree_sitter_languages</span>  <span class="c1"># pants: no-infer-dep</span>

                <span class="n">parser</span> <span class="o">=</span> <span class="n">tree_sitter_languages</span><span class="o">.</span><span class="n">get_parser</span><span class="p">(</span><span class="n">language</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install tree_sitter_languages to use CodeSplitter."</span>
                    <span class="s2">"Or pass in a parser object."</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Could not get parser for language </span><span class="si">{</span><span class="n">language</span><span class="si">}</span><span class="s2">. Check "</span>
                    <span class="s2">"https://github.com/grantjenks/py-tree-sitter-languages#license "</span>
                    <span class="s2">"for a list of valid languages."</span>
                <span class="p">)</span>
                <span class="k">raise</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">parser</span><span class="p">,</span> <span class="n">Parser</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Parser must be a tree-sitter Parser object."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="o">=</span> <span class="n">parser</span>

        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">([])</span>
        <span class="n">id_func</span> <span class="o">=</span> <span class="n">id_func</span> <span class="ow">or</span> <span class="n">default_id_func</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">language</span><span class="o">=</span><span class="n">language</span><span class="p">,</span>
            <span class="n">chunk_lines</span><span class="o">=</span><span class="n">chunk_lines</span><span class="p">,</span>
            <span class="n">chunk_lines_overlap</span><span class="o">=</span><span class="n">chunk_lines_overlap</span><span class="p">,</span>
            <span class="n">max_chars</span><span class="o">=</span><span class="n">max_chars</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_prev_next_rel</span><span class="o">=</span><span class="n">include_prev_next_rel</span><span class="p">,</span>
            <span class="n">id_func</span><span class="o">=</span><span class="n">id_func</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">language</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chunk_lines</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_LINES</span><span class="p">,</span>
        <span class="n">chunk_lines_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_LINES_OVERLAP</span><span class="p">,</span>
        <span class="n">max_chars</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_CHARS</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parser</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CodeSplitter"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a CodeSplitter with default values."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">language</span><span class="o">=</span><span class="n">language</span><span class="p">,</span>
            <span class="n">chunk_lines</span><span class="o">=</span><span class="n">chunk_lines</span><span class="p">,</span>
            <span class="n">chunk_lines_overlap</span><span class="o">=</span><span class="n">chunk_lines_overlap</span><span class="p">,</span>
            <span class="n">max_chars</span><span class="o">=</span><span class="n">max_chars</span><span class="p">,</span>
            <span class="n">parser</span><span class="o">=</span><span class="n">parser</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"CodeSplitter"</span>

    <span class="k">def</span> <span class="nf">_chunk_node</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">last_end</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">new_chunks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">current_chunk</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">child</span><span class="o">.</span><span class="n">end_byte</span> <span class="o">-</span> <span class="n">child</span><span class="o">.</span><span class="n">start_byte</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_chars</span><span class="p">:</span>
                <span class="c1"># Child is too big, recursively chunk the child</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">new_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span>
                <span class="n">current_chunk</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">new_chunks</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_chunk_node</span><span class="p">(</span><span class="n">child</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">last_end</span><span class="p">))</span>
            <span class="k">elif</span> <span class="p">(</span>
                <span class="nb">len</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span> <span class="o">+</span> <span class="n">child</span><span class="o">.</span><span class="n">end_byte</span> <span class="o">-</span> <span class="n">child</span><span class="o">.</span><span class="n">start_byte</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_chars</span>
            <span class="p">):</span>
                <span class="c1"># Child would make the current chunk too big, so start a new chunk</span>
                <span class="n">new_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span>
                <span class="n">current_chunk</span> <span class="o">=</span> <span class="n">text</span><span class="p">[</span><span class="n">last_end</span> <span class="p">:</span> <span class="n">child</span><span class="o">.</span><span class="n">end_byte</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">current_chunk</span> <span class="o">+=</span> <span class="n">text</span><span class="p">[</span><span class="n">last_end</span> <span class="p">:</span> <span class="n">child</span><span class="o">.</span><span class="n">end_byte</span><span class="p">]</span>
            <span class="n">last_end</span> <span class="o">=</span> <span class="n">child</span><span class="o">.</span><span class="n">end_byte</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">new_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_chunk</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">new_chunks</span>

    <span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Split incoming code and return chunks using the AST."""</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
            <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">]}</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
            <span class="n">tree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="s2">"utf-8"</span><span class="p">))</span>

            <span class="k">if</span> <span class="p">(</span>
                <span class="ow">not</span> <span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="o">.</span><span class="n">children</span>
                <span class="ow">or</span> <span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="o">.</span><span class="n">children</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">type</span> <span class="o">!=</span> <span class="s2">"ERROR"</span>
            <span class="p">):</span>
                <span class="n">chunks</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">chunk</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chunk_node</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
                <span class="p">]</span>
                <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                    <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">chunks</span><span class="p">},</span>
                <span class="p">)</span>

                <span class="k">return</span> <span class="n">chunks</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Could not parse code with language </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">language</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/#llama_index.core.node_parser.CodeSplitter.from_defaults "Permanent link")

```
from_defaults(language: str, chunk_lines: int = DEFAULT_CHUNK_LINES, chunk_lines_overlap: int = DEFAULT_LINES_OVERLAP, max_chars: int = DEFAULT_MAX_CHARS, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, parser: Any = None) -> [CodeSplitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/#llama_index.core.node_parser.CodeSplitter "llama_index.core.node_parser.text.code.CodeSplitter")
```

Create a CodeSplitter with default values.

Source code in `llama-index-core/llama_index/core/node_parser/text/code.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 95</span>
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
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">language</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">chunk_lines</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CHUNK_LINES</span><span class="p">,</span>
    <span class="n">chunk_lines_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_LINES_OVERLAP</span><span class="p">,</span>
    <span class="n">max_chars</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_MAX_CHARS</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">parser</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"CodeSplitter"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a CodeSplitter with default values."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">language</span><span class="o">=</span><span class="n">language</span><span class="p">,</span>
        <span class="n">chunk_lines</span><span class="o">=</span><span class="n">chunk_lines</span><span class="p">,</span>
        <span class="n">chunk_lines_overlap</span><span class="o">=</span><span class="n">chunk_lines_overlap</span><span class="p">,</span>
        <span class="n">max_chars</span><span class="o">=</span><span class="n">max_chars</span><span class="p">,</span>
        <span class="n">parser</span><span class="o">=</span><span class="n">parser</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### split\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/#llama_index.core.node_parser.CodeSplitter.split_text "Permanent link")

```
split_text(text: str) -> List[str]
```

Split incoming code and return chunks using the AST.

Source code in `llama-index-core/llama_index/core/node_parser/text/code.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">141</span>
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
<span class="normal">161</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">split_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Split incoming code and return chunks using the AST."""</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="p">[</span><span class="n">text</span><span class="p">]}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">tree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="s2">"utf-8"</span><span class="p">))</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="ow">not</span> <span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="o">.</span><span class="n">children</span>
            <span class="ow">or</span> <span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="o">.</span><span class="n">children</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">type</span> <span class="o">!=</span> <span class="s2">"ERROR"</span>
        <span class="p">):</span>
            <span class="n">chunks</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">chunk</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chunk_node</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">root_node</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
            <span class="p">]</span>
            <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span>
                <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">:</span> <span class="n">chunks</span><span class="p">},</span>
            <span class="p">)</span>

            <span class="k">return</span> <span class="n">chunks</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Could not parse code with language </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">language</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/)[Next Hierarchical](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)
