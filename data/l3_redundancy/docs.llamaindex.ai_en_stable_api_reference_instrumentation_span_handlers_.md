Title: Span handlers - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/

Markdown Content:
Span handlers - LlamaIndex


BaseSpanHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`, `Generic[T]`

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
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
<span class="normal">157</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseSpanHandler</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">T</span><span class="p">]):</span>
    <span class="n">open_spans</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Dictionary of open spans."</span>
    <span class="p">)</span>
    <span class="n">completed_spans</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"List of completed spans."</span>
    <span class="p">)</span>
    <span class="n">dropped_spans</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"List of completed spans."</span>
    <span class="p">)</span>
    <span class="n">current_span_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="p">{},</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Id of current spans in a given thread."</span>
    <span class="p">)</span>
    <span class="n">_lock</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">threading</span><span class="o">.</span><span class="n">Lock</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">open_spans</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="n">completed_spans</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
        <span class="n">dropped_spans</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
        <span class="n">current_span_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">open_spans</span><span class="o">=</span><span class="n">open_spans</span><span class="p">,</span>
            <span class="n">completed_spans</span><span class="o">=</span><span class="n">completed_spans</span><span class="p">,</span>
            <span class="n">dropped_spans</span><span class="o">=</span><span class="n">dropped_spans</span><span class="p">,</span>
            <span class="n">current_span_ids</span><span class="o">=</span><span class="n">current_span_ids</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"BaseSpanHandler"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">threading</span><span class="o">.</span><span class="n">Lock</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Lock</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lock</span>

    <span class="k">def</span> <span class="nf">span_enter</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for entering a span."""</span>
        <span class="k">if</span> <span class="n">id_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">:</span>
            <span class="k">pass</span>  <span class="c1"># should probably raise an error here</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_span</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span>
                <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span>
                <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span>
                <span class="n">parent_span_id</span><span class="o">=</span><span class="n">parent_id</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
                <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span> <span class="o">=</span> <span class="n">span</span>

    <span class="k">def</span> <span class="nf">span_exit</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for exiting a span."""</span>
        <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare_to_exit_span</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span> <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">span_drop</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for dropping a span i.e. early exit."""</span>
        <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare_to_drop_span</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span> <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span> <span class="n">err</span><span class="o">=</span><span class="n">err</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">new_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parent_span_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create a span.</span>

<span class="sd">        Subclasses of BaseSpanHandler should create the respective span type T</span>
<span class="sd">        and return it. Only NullSpanHandler should return a None here.</span>
<span class="sd">        """</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">prepare_to_exit_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Logic for preparing to exit a span.</span>

<span class="sd">        Subclasses of BaseSpanHandler should return back the specific span T</span>
<span class="sd">        that is to be exited. If None is returned, then the span won't actually</span>
<span class="sd">        be exited.</span>
<span class="sd">        """</span>
        <span class="o">...</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">prepare_to_drop_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Logic for preparing to drop a span.</span>

<span class="sd">        Subclasses of BaseSpanHandler should return back the specific span T</span>
<span class="sd">        that is to be dropped. If None is returned, then the span won't actually</span>
<span class="sd">        be dropped.</span>
<span class="sd">        """</span>
        <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### class\_name [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.class_name "Permanent link")

```
class_name() -> str
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"BaseSpanHandler"</span>
</code></pre></div></td></tr></tbody></table>

### span\_enter [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.span_enter "Permanent link")

```
span_enter(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, parent_id: Optional[str] = None, **kwargs: Any) -> None
```

Logic for entering a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
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
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">span_enter</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for entering a span."""</span>
    <span class="k">if</span> <span class="n">id_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">:</span>
        <span class="k">pass</span>  <span class="c1"># should probably raise an error here</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_span</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span>
            <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span>
            <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span>
            <span class="n">parent_span_id</span><span class="o">=</span><span class="n">parent_id</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span> <span class="o">=</span> <span class="n">span</span>
</code></pre></div></td></tr></tbody></table>

### span\_exit [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.span_exit "Permanent link")

```
span_exit(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, result: Optional[Any] = None, **kwargs: Any) -> None
```

Logic for exiting a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">span_exit</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for exiting a span."""</span>
    <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare_to_exit_span</span><span class="p">(</span>
        <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span> <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### span\_drop [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.span_drop "Permanent link")

```
span_drop(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, err: Optional[BaseException] = None, **kwargs: Any) -> None
```

Logic for dropping a span i.e. early exit.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">span_drop</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for dropping a span i.e. early exit."""</span>
    <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare_to_drop_span</span><span class="p">(</span>
        <span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">bound_args</span><span class="o">=</span><span class="n">bound_args</span><span class="p">,</span> <span class="n">instance</span><span class="o">=</span><span class="n">instance</span><span class="p">,</span> <span class="n">err</span><span class="o">=</span><span class="n">err</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">span</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### new\_span `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.new_span "Permanent link")

```
new_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, parent_span_id: Optional[str] = None, **kwargs: Any) -> Optional[T]
```

Create a span.

Subclasses of BaseSpanHandler should create the respective span type T and return it. Only NullSpanHandler should return a None here.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">new_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">parent_span_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Create a span.</span>

<span class="sd">    Subclasses of BaseSpanHandler should create the respective span type T</span>
<span class="sd">    and return it. Only NullSpanHandler should return a None here.</span>
<span class="sd">    """</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### prepare\_to\_exit\_span `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.prepare_to_exit_span "Permanent link")

```
prepare_to_exit_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, result: Optional[Any] = None, **kwargs: Any) -> Optional[T]
```

Logic for preparing to exit a span.

Subclasses of BaseSpanHandler should return back the specific span T that is to be exited. If None is returned, then the span won't actually be exited.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">125</span>
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
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">prepare_to_exit_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Logic for preparing to exit a span.</span>

<span class="sd">    Subclasses of BaseSpanHandler should return back the specific span T</span>
<span class="sd">    that is to be exited. If None is returned, then the span won't actually</span>
<span class="sd">    be exited.</span>
<span class="sd">    """</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

### prepare\_to\_drop\_span `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler.prepare_to_drop_span "Permanent link")

```
prepare_to_drop_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, err: Optional[BaseException] = None, **kwargs: Any) -> Optional[T]
```

Logic for preparing to drop a span.

Subclasses of BaseSpanHandler should return back the specific span T that is to be dropped. If None is returned, then the span won't actually be dropped.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">142</span>
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
<span class="normal">157</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">prepare_to_drop_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">T</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Logic for preparing to drop a span.</span>

<span class="sd">    Subclasses of BaseSpanHandler should return back the specific span T</span>
<span class="sd">    that is to be dropped. If None is returned, then the span won't actually</span>
<span class="sd">    be dropped.</span>
<span class="sd">    """</span>
    <span class="o">...</span>
</code></pre></div></td></tr></tbody></table>

SimpleSpanHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseSpanHandler](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler "llama_index.core.instrumentation.span_handlers.base.BaseSpanHandler")[SimpleSpan]`

Span Handler that manages SimpleSpan's.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 13</span>
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
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleSpanHandler</span><span class="p">(</span><span class="n">BaseSpanHandler</span><span class="p">[</span><span class="n">SimpleSpan</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Span Handler that manages SimpleSpan's."""</span>

    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Class name."""</span>
        <span class="k">return</span> <span class="s2">"SimpleSpanHandler"</span>

    <span class="k">def</span> <span class="nf">new_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parent_span_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a span."""</span>
        <span class="k">return</span> <span class="n">SimpleSpan</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_span_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">prepare_to_exit_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for preparing to drop a span."""</span>
        <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
        <span class="n">span</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SimpleSpan</span><span class="p">,</span> <span class="n">span</span><span class="p">)</span>
        <span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
        <span class="n">span</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="o">-</span> <span class="n">span</span><span class="o">.</span><span class="n">start_time</span><span class="p">)</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">completed_spans</span> <span class="o">+=</span> <span class="p">[</span><span class="n">span</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">span</span>

    <span class="k">def</span> <span class="nf">prepare_to_drop_span</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
        <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Logic for droppping a span."""</span>
        <span class="k">if</span> <span class="n">id_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
                <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
                <span class="n">span</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"error"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">)}</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">dropped_spans</span> <span class="o">+=</span> <span class="p">[</span><span class="n">span</span><span class="p">]</span>
            <span class="k">return</span> <span class="n">span</span>

        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_get_parents</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SimpleSpan</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Helper method to get all parent/root spans."""</span>
        <span class="n">all_spans</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">completed_spans</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">dropped_spans</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">all_spans</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">parent_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_build_tree_by_parent</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">:</span> <span class="n">SimpleSpan</span><span class="p">,</span> <span class="n">acc</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SimpleSpan</span><span class="p">],</span> <span class="n">spans</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">SimpleSpan</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">SimpleSpan</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Builds the tree by parent root."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">spans</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">acc</span>

        <span class="n">children</span> <span class="o">=</span> <span class="p">[</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">spans</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">parent_id</span> <span class="o"></span> <span class="n">s</span><span class="o">.</span><span class="n">parent_id</span> <span class="k">for</span> <span class="n">ns</span> <span class="ow">in</span> <span class="n">all_spans</span><span class="p">):</span>
                <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Parent with id </span><span class="si">{</span><span class="n">s</span><span class="o">.</span><span class="n">parent_id</span><span class="si">}</span><span class="s2"> missing from spans"</span><span class="p">)</span>
                <span class="n">s</span><span class="o">.</span><span class="n">parent_id</span> <span class="o">+=</span> <span class="s2">"-MISSING"</span>
                <span class="n">all_spans</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">SimpleSpan</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">parent_id</span><span class="p">,</span> <span class="n">parent_id</span><span class="o">=</span><span class="kc">None</span><span class="p">))</span>

        <span class="n">parents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_parents</span><span class="p">()</span>
        <span class="n">span_groups</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">parents</span><span class="p">:</span>
            <span class="n">this_span_group</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_tree_by_parent</span><span class="p">(</span>
                <span class="n">parent</span><span class="o">=</span><span class="n">p</span><span class="p">,</span> <span class="n">acc</span><span class="o">=</span><span class="p">[</span><span class="n">p</span><span class="p">],</span> <span class="n">spans</span><span class="o">=</span><span class="p">[</span><span class="n">s</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">all_spans</span> <span class="k">if</span> <span class="n">s</span> <span class="o">!=</span> <span class="n">p</span><span class="p">]</span>
            <span class="p">)</span>
            <span class="n">sorted_span_group</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">this_span_group</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">start_time</span><span class="p">)</span>
            <span class="n">span_groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sorted_span_group</span><span class="p">)</span>

        <span class="n">trees</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">tree</span> <span class="o">=</span> <span class="n">Tree</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">grp</span> <span class="ow">in</span> <span class="n">span_groups</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">grp</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">span</span><span class="o">.</span><span class="n">parent_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="c1"># complete old tree unless its empty (i.e., start of loop)</span>
                    <span class="k">if</span> <span class="n">tree</span><span class="o">.</span><span class="n">all_nodes</span><span class="p">():</span>
                        <span class="n">trees</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>
                        <span class="c1"># start new tree</span>
                        <span class="n">tree</span> <span class="o">=</span> <span class="n">Tree</span><span class="p">()</span>

                <span class="n">tree</span><span class="o">.</span><span class="n">create_node</span><span class="p">(</span>
                    <span class="n">tag</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">span</span><span class="o">.</span><span class="n">id_</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">span</span><span class="o">.</span><span class="n">duration</span><span class="si">}</span><span class="s2">)"</span><span class="p">,</span>
                    <span class="n">identifier</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">id_</span><span class="p">,</span>
                    <span class="n">parent</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">parent_id</span><span class="p">,</span>
                    <span class="n">data</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">start_time</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="n">trees</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">trees</span>

    <span class="k">def</span> <span class="nf">print_trace_trees</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Method for viewing trace trees."""</span>
        <span class="n">trees</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_trace_trees</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">tree</span> <span class="ow">in</span> <span class="n">trees</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">stdout</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sorting</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">node</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">data</span><span class="p">))</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### class\_name [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler.class_name "Permanent link")

```
class_name() -> str
```

Class name.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Class name."""</span>
    <span class="k">return</span> <span class="s2">"SimpleSpanHandler"</span>
</code></pre></div></td></tr></tbody></table>

### new\_span [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler.new_span "Permanent link")

```
new_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, parent_span_id: Optional[str] = None, **kwargs: Any) -> SimpleSpan
```

Create a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">new_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">parent_span_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a span."""</span>
    <span class="k">return</span> <span class="n">SimpleSpan</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">id_</span><span class="p">,</span> <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_span_id</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### prepare\_to\_exit\_span [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler.prepare_to_exit_span "Permanent link")

```
prepare_to_exit_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, result: Optional[Any] = None, **kwargs: Any) -> SimpleSpan
```

Logic for preparing to drop a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">46</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">prepare_to_exit_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for preparing to drop a span."""</span>
    <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
    <span class="n">span</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">SimpleSpan</span><span class="p">,</span> <span class="n">span</span><span class="p">)</span>
    <span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
    <span class="n">span</span><span class="o">.</span><span class="n">duration</span> <span class="o">=</span> <span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="o">-</span> <span class="n">span</span><span class="o">.</span><span class="n">start_time</span><span class="p">)</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">completed_spans</span> <span class="o">+=</span> <span class="p">[</span><span class="n">span</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">span</span>
</code></pre></div></td></tr></tbody></table>

### prepare\_to\_drop\_span [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler.prepare_to_drop_span "Permanent link")

```
prepare_to_drop_span(id_: str, bound_args: BoundArguments, instance: Optional[Any] = None, err: Optional[BaseException] = None, **kwargs: Any) -> SimpleSpan
```

Logic for droppping a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">48</span>
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
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">prepare_to_drop_span</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">bound_args</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">BoundArguments</span><span class="p">,</span>
    <span class="n">instance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">err</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SimpleSpan</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Logic for droppping a span."""</span>
    <span class="k">if</span> <span class="n">id_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
            <span class="n">span</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">open_spans</span><span class="p">[</span><span class="n">id_</span><span class="p">]</span>
            <span class="n">span</span><span class="o">.</span><span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"error"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">)}</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">dropped_spans</span> <span class="o">+=</span> <span class="p">[</span><span class="n">span</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">span</span>

    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### print\_trace\_trees [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/#llama_index.core.instrumentation.span_handlers.simple.SimpleSpanHandler.print_trace_trees "Permanent link")

```
print_trace_trees() -> None
```

Method for viewing trace trees.

Source code in `llama-index-core/llama_index/core/instrumentation/span_handlers/simple.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">print_trace_trees</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Method for viewing trace trees."""</span>
    <span class="n">trees</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_trace_trees</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">tree</span> <span class="ow">in</span> <span class="n">trees</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">stdout</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sorting</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">node</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">data</span><span class="p">))</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Instrumentation](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)[Next Span types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/)
