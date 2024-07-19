Title: Llama debug - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/

Markdown Content:
Llama debug - LlamaIndex


LlamaDebugHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PythonicallyPrintingBaseHandler`

Callback handler that keeps track of debug info.

NOTE: this is a beta feature. The usage within our codebase, and the interface may change.

This handler simply keeps track of event starts/ends, separated by event types. You can use this callback handler to keep track of and debug events.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_starts_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 
list of event types to ignore when tracking event starts.



 | `None` |
| `event_ends_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

list of event types to ignore when tracking event ends.



 | `None` |

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

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
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LlamaDebugHandler</span><span class="p">(</span><span class="n">PythonicallyPrintingBaseHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback handler that keeps track of debug info.</span>

<span class="sd">    NOTE: this is a beta feature. The usage within our codebase, and the interface</span>
<span class="sd">    may change.</span>

<span class="sd">    This handler simply keeps track of event starts/ends, separated by event types.</span>
<span class="sd">    You can use this callback handler to keep track of and debug events.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_starts_to_ignore (Optional[List[CBEventType]]): list of event types to</span>
<span class="sd">            ignore when tracking event starts.</span>
<span class="sd">        event_ends_to_ignore (Optional[List[CBEventType]]): list of event types to</span>
<span class="sd">            ignore when tracking event ends.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_starts_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_ends_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">print_trace_on_end</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">logger</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the llama debug handler."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">print_trace_on_end</span> <span class="o">=</span> <span class="n">print_trace_on_end</span>
        <span class="n">event_starts_to_ignore</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">event_starts_to_ignore</span> <span class="k">if</span> <span class="n">event_starts_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>
        <span class="n">event_ends_to_ignore</span> <span class="o">=</span> <span class="n">event_ends_to_ignore</span> <span class="k">if</span> <span class="n">event_ends_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="n">event_starts_to_ignore</span><span class="p">,</span>
            <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="n">event_ends_to_ignore</span><span class="p">,</span>
            <span class="n">logger</span><span class="o">=</span><span class="n">logger</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Store event start data by event type.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>
<span class="sd">            parent_id (str): parent event id.</span>

<span class="sd">        """</span>
        <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">event_type</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">event</span><span class="o">.</span><span class="n">id_</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Store event end data by event type.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>

<span class="sd">        """</span>
        <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">event_type</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_events</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all events for a specific event type."""</span>
        <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event_type</span><span class="p">]</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span>

    <span class="k">def</span> <span class="nf">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">events</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Helper function to pair events according to their ID."""</span>
        <span class="n">event_pairs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
            <span class="n">event_pairs</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span>
            <span class="n">event_pairs</span><span class="o">.</span><span class="n">values</span><span class="p">(),</span>
            <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">TIMESTAMP_FORMAT</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_time_stats_from_event_pairs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EventStats</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Calculate time-based stats for a set of event pairs."""</span>
        <span class="n">total_secs</span> <span class="o">=</span> <span class="mf">0.0</span>
        <span class="k">for</span> <span class="n">event_pair</span> <span class="ow">in</span> <span class="n">event_pairs</span><span class="p">:</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">TIMESTAMP_FORMAT</span><span class="p">)</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span><span class="n">event_pair</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">TIMESTAMP_FORMAT</span><span class="p">)</span>
            <span class="n">total_secs</span> <span class="o">+=</span> <span class="p">(</span><span class="n">end_time</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span>

        <span class="k">return</span> <span class="n">EventStats</span><span class="p">(</span>
            <span class="n">total_secs</span><span class="o">=</span><span class="n">total_secs</span><span class="p">,</span>
            <span class="n">average_secs</span><span class="o">=</span><span class="n">total_secs</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">event_pairs</span><span class="p">),</span>
            <span class="n">total_count</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">event_pairs</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_event_pairs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Pair events by ID, either all events or a specific type."""</span>
        <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event_type</span><span class="p">])</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_llm_inputs_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get the exact LLM inputs and outputs."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">get_event_time_info</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">event_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EventStats</span><span class="p">:</span>
        <span class="n">event_pairs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_event_pairs</span><span class="p">(</span><span class="n">event_type</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_time_stats_from_event_pairs</span><span class="p">(</span><span class="n">event_pairs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">flush_event_logs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Clear all events from memory."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Launch a trace."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="o">=</span> <span class="n">trace_id</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Shutdown the current trace."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">trace_map</span> <span class="ow">or</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">print_trace_on_end</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">print_trace_map</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_print_trace_map</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cur_event_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">level</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Recursively print trace map to terminal for debugging."""</span>
        <span class="n">event_pair</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">cur_event_id</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">event_pair</span><span class="p">:</span>
            <span class="n">time_stats</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_time_stats_from_event_pairs</span><span class="p">([</span><span class="n">event_pair</span><span class="p">])</span>
            <span class="n">indent</span> <span class="o">=</span> <span class="s2">" "</span> <span class="o">*</span> <span class="n">level</span> <span class="o">*</span> <span class="mi">2</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">indent</span><span class="si">}</span><span class="s2">|_</span><span class="si">{</span><span class="n">event_pair</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">event_type</span><span class="si">}</span><span class="s2"> -&gt; </span><span class="si">{</span><span class="n">time_stats</span><span class="o">.</span><span class="n">total_secs</span><span class="si">}</span><span class="s2"> seconds"</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">child_event_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span><span class="p">[</span><span class="n">cur_event_id</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">child_event_id</span> <span class="ow">in</span> <span class="n">child_event_ids</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_print_trace_map</span><span class="p">(</span><span class="n">child_event_id</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">level</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">print_trace_map</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Print simple trace map to terminal for debugging of the most recent trace."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="s2">"*"</span> <span class="o">*</span> <span class="mi">10</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Trace: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_print_trace_map</span><span class="p">(</span><span class="n">BASE_TRACE_EVENT</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="s2">"*"</span> <span class="o">*</span> <span class="mi">10</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">event_pairs_by_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">events_pairs_by_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">sequential_events</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_start [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.on_event_start "Permanent link")

```
on_event_start(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', parent_id: str = '', **kwargs: Any) -> str
```

Store event start data by event type.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_type` | `[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")` | 
event type to store.



 | _required_ |
| `payload` | `Optional[Dict[str, Any]]` | 

payload to store.



 | `None` |
| `event_id` | `str` | 

event id to store.



 | `''` |
| `parent_id` | `str` | 

parent event id.



 | `''` |

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
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
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Store event start data by event type.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>
<span class="sd">        parent_id (str): parent event id.</span>

<span class="sd">    """</span>
    <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">event_type</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">event</span><span class="o">.</span><span class="n">id_</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_end [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.on_event_end "Permanent link")

```
on_event_end(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', **kwargs: Any) -> None
```

Store event end data by event type.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event_type` | `[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")` | 
event type to store.



 | _required_ |
| `payload` | `Optional[Dict[str, Any]]` | 

payload to store.



 | `None` |
| `event_id` | `str` | 

event id to store.



 | `''` |

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 81</span>
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
<span class="normal">100</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Store event end data by event type.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>

<span class="sd">    """</span>
    <span class="n">event</span> <span class="o">=</span> <span class="n">CBEvent</span><span class="p">(</span><span class="n">event_type</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">event_type</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">id_</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_events [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.get_events "Permanent link")

```
get_events(event_type: Optional[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")] = None) -> List[[CBEvent](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEvent "llama_index.core.callbacks.schema.CBEvent")]
```

Get all events for a specific event type.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_events</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all events for a specific event type."""</span>
    <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event_type</span><span class="p">]</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span>
</code></pre></div></td></tr></tbody></table>

### get\_event\_pairs [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.get_event_pairs "Permanent link")

```
get_event_pairs(event_type: Optional[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")] = None) -> List[List[[CBEvent](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEvent "llama_index.core.callbacks.schema.CBEvent")]]
```

Pair events by ID, either all events or a specific type.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_event_pairs</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">event_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Pair events by ID, either all events or a specific type."""</span>
    <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">event_type</span><span class="p">])</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_llm\_inputs\_outputs [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.get_llm_inputs_outputs "Permanent link")

```
get_llm_inputs_outputs() -> List[List[[CBEvent](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEvent "llama_index.core.callbacks.schema.CBEvent")]]
```

Get the exact LLM inputs and outputs.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_llm_inputs_outputs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEvent</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Get the exact LLM inputs and outputs."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_pairs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span><span class="p">[</span><span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### flush\_event\_logs [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.flush_event_logs "Permanent link")

```
flush_event_logs() -> None
```

Clear all events from memory.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">flush_event_logs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Clear all events from memory."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_type</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_event_pairs_by_id</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_sequential_events</span> <span class="o">=</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

### start\_trace [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.start_trace "Permanent link")

```
start_trace(trace_id: Optional[str] = None) -> None
```

Launch a trace.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Launch a trace."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span> <span class="o">=</span> <span class="n">trace_id</span>
</code></pre></div></td></tr></tbody></table>

### end\_trace [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.end_trace "Permanent link")

```
end_trace(trace_id: Optional[str] = None, trace_map: Optional[Dict[str, List[str]]] = None) -> None
```

Shutdown the current trace.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Shutdown the current trace."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_trace_map</span> <span class="o">=</span> <span class="n">trace_map</span> <span class="ow">or</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">print_trace_on_end</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">print_trace_map</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### print\_trace\_map [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/#llama_index.core.callbacks.llama_debug.LlamaDebugHandler.print_trace_map "Permanent link")

```
print_trace_map() -> None
```

Print simple trace map to terminal for debugging of the most recent trace.

Source code in `llama-index-core/llama_index/core/callbacks/llama_debug.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">print_trace_map</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Print simple trace map to terminal for debugging of the most recent trace."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="s2">"*"</span> <span class="o">*</span> <span class="mi">10</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Trace: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_cur_trace_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_print_trace_map</span><span class="p">(</span><span class="n">BASE_TRACE_EVENT</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_print</span><span class="p">(</span><span class="s2">"*"</span> <span class="o">*</span> <span class="mi">10</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Langfuse](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/langfuse/)[Next Openinference](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/)
