Title: Dashscope - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/agent/dashscope/

Markdown Content:
Dashscope - LlamaIndex


DashScopeAgent [#](https://docs.llamaindex.ai/en/stable/api_reference/agent/dashscope/#llama_index.agent.dashscope.DashScopeAgent "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseAgent](https://docs.llamaindex.ai/en/stable/api_reference/agent/#llama_index.core.agent.types.BaseAgent "llama_index.core.agent.types.BaseAgent")`

DashScope agent simple wrapper for Alibaba cloud bailian high-level agent api.

Source code in `llama-index-integrations/agent/llama-index-agent-dashscope/llama_index/agent/dashscope/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 20</span>
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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DashScopeAgent</span><span class="p">(</span><span class="n">BaseAgent</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    DashScope agent simple wrapper for Alibaba cloud bailian high-level agent api.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">app_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">chat_session</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">workspace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params.</span>

<span class="sd">        Args:</span>
<span class="sd">            app_id (str): id of Alibaba cloud bailian application</span>
<span class="sd">            chat_session (bool): When need to keep chat session, defaults to True.</span>
<span class="sd">            workspace(str, `optional`): Workspace of Alibaba cloud bailian</span>
<span class="sd">            api_key (str, optional): The api api_key, can be None,</span>
<span class="sd">                if None, will get from ENV DASHSCOPE_API_KEY.</span>
<span class="sd">            verbose: Output verbose info or not.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">app_id</span> <span class="o">=</span> <span class="n">app_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">chat_session</span> <span class="o">=</span> <span class="n">chat_session</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">workspace</span> <span class="o">=</span> <span class="n">workspace</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chat</span><span class="p">(</span><span class="n">message</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AgentChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"achat not implemented"</span><span class="p">)</span>

    <span class="nd">@trace_method</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chat</span><span class="p">(</span><span class="n">message</span><span class="o">=</span><span class="n">message</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamingAgentChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"astream_chat not implemented"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">chat_history</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"chat_history not implemented"</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">get_session_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span>

    <span class="k">def</span> <span class="nf">_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">message</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">stream</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">chat_history</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">AgentChatResponse</span><span class="p">,</span> <span class="n">StreamingAgentChatResponse</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Call app completion service.</span>

<span class="sd">        Args:</span>
<span class="sd">            message (str): Message for chatting with LLM.</span>
<span class="sd">            chat_history (List[ChatMessage], `optional`): The user provided chat history. Defaults to None.</span>

<span class="sd">            **kwargs:</span>
<span class="sd">                session_id(str, `optional`): Session if for multiple rounds call.</span>
<span class="sd">                biz_params(dict, `optional`): The extra parameters for flow or plugin.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ValueError: The request failed with http code and message.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Union[AgentChatResponse, StreamingAgentChatResponse]</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">stream</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"stream"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">chat_session</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"session_id"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">Application</span><span class="o">.</span><span class="n">call</span><span class="p">(</span>
            <span class="n">app_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">app_id</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
            <span class="n">history</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">workspace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">workspace</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">stream</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">StreamingAgentChatResponse</span><span class="p">(</span>
                <span class="n">chat_stream</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">from_dashscope_response</span><span class="p">(</span><span class="n">rsp</span><span class="p">)</span> <span class="k">for</span> <span class="n">rsp</span> <span class="ow">in</span> <span class="n">response</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="n">HTTPStatus</span><span class="o">.</span><span class="n">OK</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Chat failed with status: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">, request id: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">request_id</span><span class="si">}</span><span class="s2">, "</span>
                    <span class="sa">f</span><span class="s2">"code: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">code</span><span class="si">}</span><span class="s2">, message: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">"Got chat response: </span><span class="si">%s</span><span class="s2">"</span> <span class="o">%</span> <span class="n">response</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">session_id</span>

            <span class="k">return</span> <span class="n">AgentChatResponse</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">from_dashscope_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">ApplicationResponse</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="n">HTTPStatus</span><span class="o">.</span><span class="n">OK</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Chat failed with status: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">, request id: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">request_id</span><span class="si">}</span><span class="s2">, "</span>
                <span class="sa">f</span><span class="s2">"code: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">code</span><span class="si">}</span><span class="s2">, message: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">message</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="ow">and</span> <span class="n">response</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">finish_reason</span> <span class="o">==</span> <span class="s2">"stop"</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Got final chat response: </span><span class="si">%s</span><span class="s2">"</span> <span class="o">%</span> <span class="n">response</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_session_id</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">session_id</span>

        <span class="k">return</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="o">.</span><span class="n">ASSISTANT</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">text</span>
            <span class="p">)</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Coa](https://docs.llamaindex.ai/en/stable/api_reference/agent/coa/)[Next Core Agent Classes](https://docs.llamaindex.ai/en/stable/api_reference/agent/)
