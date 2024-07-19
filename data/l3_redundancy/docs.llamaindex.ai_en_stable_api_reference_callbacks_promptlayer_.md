Title: Promptlayer - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/

Markdown Content:
Promptlayer - LlamaIndex


PromptLayerHandler [#](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/#llama_index.callbacks.promptlayer.PromptLayerHandler "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseCallbackHandler](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base_handler.BaseCallbackHandler "llama_index.core.callbacks.base_handler.BaseCallbackHandler")`

Callback handler for sending to promptlayer.com.

Source code in `llama-index-integrations/callbacks/llama-index-callbacks-promptlayer/llama_index/callbacks/promptlayer/base.py`

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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PromptLayerHandler</span><span class="p">(</span><span class="n">BaseCallbackHandler</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Callback handler for sending to promptlayer.com."""</span>

    <span class="n">pl_tags</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>
    <span class="n">return_pl_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pl_tags</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="n">return_pl_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">promptlayer.utils</span> <span class="kn">import</span> <span class="n">get_api_key</span><span class="p">,</span> <span class="n">promptlayer_api_request</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_promptlayer_api_request</span> <span class="o">=</span> <span class="n">promptlayer_api_request</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_promptlayer_api_key</span> <span class="o">=</span> <span class="n">get_api_key</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install PromptLAyer with `pip install promptlayer`"</span>
            <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pl_tags</span> <span class="o">=</span> <span class="n">pl_tags</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">return_pl_id</span> <span class="o">=</span> <span class="n">return_pl_id</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">event_starts_to_ignore</span><span class="o">=</span><span class="p">[],</span> <span class="n">event_ends_to_ignore</span><span class="o">=</span><span class="p">[])</span>

    <span class="k">def</span> <span class="nf">start_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>

    <span class="k">def</span> <span class="nf">end_trace</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">trace_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">trace_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span>

    <span class="n">event_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">add_event</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"kwargs"</span><span class="p">:</span> <span class="n">kwargs</span><span class="p">,</span>
            <span class="s2">"request_start_time"</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">timestamp</span><span class="p">(),</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">get_event</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">event_map</span><span class="p">[</span><span class="n">event_id</span><span class="p">]</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">on_event_start</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">parent_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">event_type</span> <span class="o">==</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span> <span class="ow">and</span> <span class="n">payload</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">add_event</span><span class="p">(</span>
                <span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">,</span> <span class="o">**</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">SERIALIZED</span><span class="p">,</span> <span class="p">{})</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">event_id</span>

    <span class="k">def</span> <span class="nf">on_event_end</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">event_type</span><span class="p">:</span> <span class="n">CBEventType</span><span class="p">,</span>
        <span class="n">payload</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">event_type</span> <span class="o">!=</span> <span class="n">CBEventType</span><span class="o">.</span><span class="n">LLM</span> <span class="ow">or</span> <span class="n">payload</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span>
        <span class="n">request_end_time</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">timestamp</span><span class="p">()</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">PROMPT</span><span class="p">))</span>
        <span class="n">completion</span> <span class="o">=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">COMPLETION</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">)</span>
        <span class="n">function_name</span> <span class="o">=</span> <span class="n">PROMPT_LAYER_CHAT_FUNCTION_NAME</span>
        <span class="n">event_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_event</span><span class="p">(</span><span class="n">event_id</span><span class="o">=</span><span class="n">event_id</span><span class="p">)</span>
        <span class="n">resp</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>
        <span class="n">extra_args</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">messages</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">MESSAGES</span><span class="p">,</span> <span class="p">[]))</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">resp</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span>

            <span class="n">usage_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">usage</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">raw</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"usage"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">usage</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                    <span class="n">usage_dict</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="s2">"prompt_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"prompt_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
                        <span class="s2">"completion_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"completion_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
                        <span class="s2">"total_tokens"</span><span class="p">:</span> <span class="n">usage</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"total_tokens"</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
                    <span class="p">}</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">usage</span><span class="p">,</span> <span class="n">BaseModel</span><span class="p">):</span>
                    <span class="n">usage_dict</span> <span class="o">=</span> <span class="n">usage</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="k">pass</span>

            <span class="n">extra_args</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"messages"</span><span class="p">:</span> <span class="p">[</span><span class="n">message</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">],</span>
                <span class="s2">"usage"</span><span class="p">:</span> <span class="n">usage_dict</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="c1">## promptlayer needs tool_calls toplevel.</span>
            <span class="k">if</span> <span class="s2">"tool_calls"</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">:</span>
                <span class="n">resp</span><span class="p">[</span><span class="s2">"tool_calls"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">tool_call</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span>
                    <span class="k">for</span> <span class="n">tool_call</span> <span class="ow">in</span> <span class="n">resp</span><span class="p">[</span><span class="s2">"additional_kwargs"</span><span class="p">][</span><span class="s2">"tool_calls"</span><span class="p">]</span>
                <span class="p">]</span>
                <span class="k">del</span> <span class="n">resp</span><span class="p">[</span><span class="s2">"additional_kwargs"</span><span class="p">][</span><span class="s2">"tool_calls"</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">completion</span><span class="p">:</span>
            <span class="n">function_name</span> <span class="o">=</span> <span class="n">PROMPT_LAYER_COMPLETION_FUNCTION_NAME</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">completion</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">resp</span><span class="p">:</span>
            <span class="n">_pl_request_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_promptlayer_api_request</span><span class="p">(</span>
                <span class="n">function_name</span><span class="p">,</span>
                <span class="s2">"openai"</span><span class="p">,</span>
                <span class="p">[</span><span class="n">prompt</span><span class="p">],</span>
                <span class="p">{</span>
                    <span class="o">**</span><span class="n">extra_args</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">event_data</span><span class="p">[</span><span class="s2">"kwargs"</span><span class="p">],</span>
                <span class="p">},</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">pl_tags</span><span class="p">,</span>
                <span class="p">[</span><span class="n">resp</span><span class="p">],</span>
                <span class="n">event_data</span><span class="p">[</span><span class="s2">"request_start_time"</span><span class="p">],</span>
                <span class="n">request_end_time</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_promptlayer_api_key</span><span class="p">,</span>
                <span class="n">return_pl_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">return_pl_id</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openinference](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/)[Next Token counter](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/)
