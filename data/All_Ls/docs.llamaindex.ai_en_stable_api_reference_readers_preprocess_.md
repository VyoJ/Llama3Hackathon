Title: Preprocess - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/

Markdown Content:
Preprocess - LlamaIndex


PreprocessReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/#llama_index.readers.preprocess.PreprocessReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Source code in `llama-index-integrations/readers/llama-index-readers-preprocess/llama_index/readers/preprocess/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
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
<span class="normal">157</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PreprocessReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">api_key</span> <span class="o"></span> <span class="s2">"filepath"</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_filepath</span> <span class="o">=</span> <span class="n">value</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_preprocess</span><span class="o">.</span><span class="n">set_filepath</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">key</span> <span class="o"></span> <span class="s2">"OK"</span> <span class="ow">and</span> <span class="n">pp_response</span><span class="o">.</span><span class="n">success</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_process_id</span> <span class="o">=</span> <span class="n">pp_response</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s2">"process"</span><span class="p">][</span><span class="s2">"id"</span><span class="p">]</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_preprocess</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status</span> <span class="o"></span> <span class="s2">"OK"</span> <span class="ow">and</span> <span class="n">response</span><span class="o">.</span><span class="n">success</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_filepath</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s2">"info"</span><span class="p">][</span><span class="s2">"file"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_chunks</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s2">"chunks"</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pebblo](https://docs.llamaindex.ai/en/stable/api_reference/readers/pebblo/)[Next Psychic](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/)
