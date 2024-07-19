Title: Aim - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/

Markdown Content:
Aim - LlamaIndex


AimCallback [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/#llama_index.callbacks.aim.AimCallback "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`

AimCallback callback class.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `repo` |  | 
obj:`str`, optional): Aim repository path or Repo object to which Run object is bound. If skipped, default Repo is used.



 | `None` |
| `experiment_name` |  | 

obj:`str`, optional): Sets Run's `experiment` property. 'default' if not specified. Can be used later to query runs/sequences.



 | `None` |
| `system_tracking_interval` |  | 

obj:`int`, optional): Sets the tracking interval in seconds for system usage metrics (CPU, Memory, etc.). Set to `None` to disable system metrics tracking.



 | `1` |
| `log_system_params` |  | 

obj:`bool`, optional): Enable/Disable logging of system params such as installed packages, git info, environment variables, etc.



 | `True` |
| `capture_terminal_logs` |  | 

obj:`bool`, optional): Enable/Disable terminal stdout logging.



 | `True` |
| `event_starts_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

list of event types to ignore when tracking event starts.



 | `None` |
| `event_ends_to_ignore` | `Optional[List[[CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType")]]` | 

list of event types to ignore when tracking event ends.



 | `None` |

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-aim/llama_index/callbacks/aim/base.py`

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
<span class="normal">188</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AimCallback</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    AimCallback callback class.</span>

<span class="sd">    Args:</span>
<span class="sd">        repo (:obj:`str`, optional):</span>
<span class="sd">            Aim repository path or Repo object to which Run object is bound.</span>
<span class="sd">            If skipped, default Repo is used.</span>
<span class="sd">        experiment_name (:obj:`str`, optional):</span>
<span class="sd">            Sets Run's `experiment` property. 'default' if not specified.</span>
<span class="sd">            Can be used later to query runs/sequences.</span>
<span class="sd">        system_tracking_interval (:obj:`int`, optional):</span>
<span class="sd">            Sets the tracking interval in seconds for system usage</span>
<span class="sd">            metrics (CPU, Memory, etc.). Set to `None` to disable</span>
<span class="sd">            system metrics tracking.</span>
<span class="sd">        log_system_params (:obj:`bool`, optional):</span>
<span class="sd">            Enable/Disable logging of system params such as installed packages,</span>
<span class="sd">            git info, environment variables, etc.</span>
<span class="sd">        capture_terminal_logs (:obj:`bool`, optional):</span>
<span class="sd">            Enable/Disable terminal stdout logging.</span>
<span class="sd">        event_starts_to_ignore (Optional[List[CBEventType]]):</span>
<span class="sd">            list of event types to ignore when tracking event starts.</span>
<span class="sd">        event_ends_to_ignore (Optional[List[CBEventType]]):</span>
<span class="sd">            list of event types to ignore when tracking event ends.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">repo</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">experiment_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">system_tracking_interval</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">log_system_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">capture_terminal_logs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">event_starts_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_ends_to_ignore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">CBEventType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">run_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">Run</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ModuleNotFoundError</span><span class="p">(</span>
                <span class="s2">"Please install aim to use the AimCallback: 'pip install aim'"</span>
            <span class="p">)</span>

        <span class="n">event_starts_to_ignore</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">event_starts_to_ignore</span> <span class="k">if</span> <span class="n">event_starts_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>
        <span class="n">event_ends_to_ignore</span> <span class="o">=</span> <span class="n">event_ends_to_ignore</span> <span class="k">if</span> <span class="n">event_ends_to_ignore</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="n">event_starts_to_ignore</span><span class="p">,</span>
            <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="n">event_ends_to_ignore</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">repo</span> <span class="o">=</span> <span class="n">repo</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">experiment_name</span> <span class="o">=</span> <span class="n">experiment_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">system_tracking_interval</span> <span class="o">=</span> <span class="n">system_tracking_interval</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">log_system_params</span> <span class="o">=</span> <span class="n">log_system_params</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">capture_terminal_logs</span> <span class="o">=</span> <span class="n">capture_terminal_logs</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_run_hash</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">(</span><span class="n">run_params</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>
<span class="sd">            parent_id (str): parent event id.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="s2">""</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Args:</span>
<span class="sd">            event_type (CBEventType): event type to store.</span>
<span class="sd">            payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">            event_id (str): event id to store.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"AimCallback failed to init properly."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span> <span class="ow">and</span> <span class="n">payload</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span> <span class="ow">in</span> <span class="n">payload</span><span class="p">:</span>
                <span class="n">llm_input</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">])</span>
                <span class="n">llm_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">COMPLETION</span><span class="p">])</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">message</span> <span class="o">=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">,</span> <span class="p">[])</span>
                <span class="n">llm_input</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">message</span><span class="p">])</span>
                <span class="n">llm_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">])</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
                <span class="n">Text</span><span class="p">(</span><span class="n">llm_input</span><span class="p">),</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">"prompt"</span><span class="p">,</span>
                <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
                <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
            <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
                <span class="n">Text</span><span class="p">(</span><span class="n">llm_output</span><span class="p">),</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">"response"</span><span class="p">,</span>
                <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
                <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
            <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span> <span class="ow">and</span> <span class="n">payload</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">chunk_id</span><span class="p">,</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">]):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
                    <span class="n">Text</span><span class="p">(</span><span class="n">chunk</span><span class="p">),</span>
                    <span class="n">name</span><span class="o">=</span><span class="s2">"chunk"</span><span class="p">,</span>
                    <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
                    <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"chunk_id"</span><span class="p">:</span> <span class="n">chunk_id</span><span class="p">,</span> <span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
                <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">experiment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Run</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span>

    <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_hash</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run</span> <span class="o">=</span> <span class="n">Run</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_run_hash</span><span class="p">,</span>
                    <span class="n">repo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repo</span><span class="p">,</span>
                    <span class="n">system_tracking_interval</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">system_tracking_interval</span><span class="p">,</span>
                    <span class="n">log_system_params</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">log_system_params</span><span class="p">,</span>
                    <span class="n">capture_terminal_logs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">capture_terminal_logs</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run</span> <span class="o">=</span> <span class="n">Run</span><span class="p">(</span>
                    <span class="n">repo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repo</span><span class="p">,</span>
                    <span class="n">experiment</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">experiment_name</span><span class="p">,</span>
                    <span class="n">system_tracking_interval</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">system_tracking_interval</span><span class="p">,</span>
                    <span class="n">log_system_params</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">log_system_params</span><span class="p">,</span>
                    <span class="n">capture_terminal_logs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">capture_terminal_logs</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run_hash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">hash</span>

        <span class="c1"># Log config parameters</span>
        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">args</span><span class="p">[</span><span class="n">key</span><span class="p">],</span> <span class="n">strict</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Aim could not log config parameters -&gt; </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">active</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_start [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/#llama_index.callbacks.aim.AimCallback.on_event_start "Permanent link")

```
on_event_start(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', parent_id: str = '', **kwargs: Any) -> str
```

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

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-aim/llama_index/callbacks/aim/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">76</span>
<span class="normal">77</span>
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
<span class="normal">91</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>
<span class="sd">        parent_id (str): parent event id.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="s2">""</span>
</code></pre></div></td></tr></tbody></table>

### on\_event\_end [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/#llama_index.callbacks.aim.AimCallback.on_event_end "Permanent link")

```
on_event_end(event_type: [CBEventType](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.schema.CBEventType "llama_index.core.callbacks.schema.CBEventType"), payload: Optional[Dict[str, Any]] = None, event_id: str = '', **kwargs: Any) -> None
```

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

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-aim/llama_index/callbacks/aim/base.py`

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
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
    <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Args:</span>
<span class="sd">        event_type (CBEventType): event type to store.</span>
<span class="sd">        payload (Optional[Dict[str, Any]]): payload to store.</span>
<span class="sd">        event_id (str): event id to store.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"AimCallback failed to init properly."</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span> <span class="ow">and</span> <span class="n">payload</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span> <span class="ow">in</span> <span class="n">payload</span><span class="p">:</span>
            <span class="n">llm_input</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">])</span>
            <span class="n">llm_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">COMPLETION</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">message</span> <span class="o">=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">,</span> <span class="p">[])</span>
            <span class="n">llm_input</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">message</span><span class="p">])</span>
            <span class="n">llm_output</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">])</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
            <span class="n">Text</span><span class="p">(</span><span class="n">llm_input</span><span class="p">),</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"prompt"</span><span class="p">,</span>
            <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
            <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
            <span class="n">Text</span><span class="p">(</span><span class="n">llm_output</span><span class="p">),</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">"response"</span><span class="p">,</span>
            <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
            <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="k">elif</span> <span class="n">event_type</span> <span class="ow">is</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">CHUNKING</span> <span class="ow">and</span> <span class="n">payload</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">chunk_id</span><span class="p">,</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">payload</span><span class="p">[</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">CHUNKS</span><span class="p">]):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="o">.</span><span class="n">track</span><span class="p">(</span>
                <span class="n">Text</span><span class="p">(</span><span class="n">chunk</span><span class="p">),</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">"chunk"</span><span class="p">,</span>
                <span class="n">step</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_llm_response_step</span><span class="p">,</span>
                <span class="n">context</span><span class="o">=</span><span class="p">{</span><span class="s2">"chunk_id"</span><span class="p">:</span> <span class="n">chunk_id</span><span class="p">,</span> <span class="s2">"event_id"</span><span class="p">:</span> <span class="n">event_id</span><span class="p">},</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Agentops](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/agentops/)[Next Argilla](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/)
