Title: Jira - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/

Markdown Content:
Jira - LlamaIndex


JiraReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/#llama_index.readers.jira.JiraReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Jira reader. Reads data from Jira issues from passed query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `Optional` | `basic_auth` | 
{ "email": "email", "api\_token": "token", "server\_url": "server\_url"



 | _required_ |
| `Optional` | `oauth` | 

{ "cloud\_id": "cloud\_id", "api\_token": "token"



 | _required_ |
| `Optional` | `patauth` | 

{ "server\_url": "server\_url", "api\_token": "token"



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-jira/llama_index/readers/jira/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
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
<span class="normal">132</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JiraReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Jira reader. Reads data from Jira issues from passed query.</span>

<span class="sd">    Args:</span>
<span class="sd">        Optional basic_auth:{</span>
<span class="sd">            "email": "email",</span>
<span class="sd">            "api_token": "token",</span>
<span class="sd">            "server_url": "server_url"</span>
<span class="sd">        }</span>
<span class="sd">        Optional oauth:{</span>
<span class="sd">            "cloud_id": "cloud_id",</span>
<span class="sd">            "api_token": "token"</span>
<span class="sd">        }</span>
<span class="sd">        Optional patauth:{</span>
<span class="sd">            "server_url": "server_url",</span>
<span class="sd">            "api_token": "token"</span>
<span class="sd">        }</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">email</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">server_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">BasicAuth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasicAuth</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">Oauth2</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Oauth2</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">PATauth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PATauth</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">jira</span> <span class="kn">import</span> <span class="n">JIRA</span>

        <span class="k">if</span> <span class="n">email</span> <span class="ow">and</span> <span class="n">api_token</span> <span class="ow">and</span> <span class="n">server_url</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">BasicAuth</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">BasicAuth</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">BasicAuth</span><span class="p">[</span><span class="s2">"email"</span><span class="p">]</span> <span class="o">=</span> <span class="n">email</span>
            <span class="n">BasicAuth</span><span class="p">[</span><span class="s2">"api_token"</span><span class="p">]</span> <span class="o">=</span> <span class="n">api_token</span>
            <span class="n">BasicAuth</span><span class="p">[</span><span class="s2">"server_url"</span><span class="p">]</span> <span class="o">=</span> <span class="n">server_url</span>

        <span class="k">if</span> <span class="n">Oauth2</span><span class="p">:</span>
            <span class="n">options</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"server"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"https://api.atlassian.com/ex/jira/</span><span class="si">{</span><span class="n">Oauth2</span><span class="p">[</span><span class="s1">'cloud_id'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="s2">"headers"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">Oauth2</span><span class="p">[</span><span class="s1">'api_token'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">},</span>
            <span class="p">}</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">jira</span> <span class="o">=</span> <span class="n">JIRA</span><span class="p">(</span><span class="n">options</span><span class="o">=</span><span class="n">options</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">PATauth</span><span class="p">:</span>
            <span class="n">options</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"server"</span><span class="p">:</span> <span class="n">PATauth</span><span class="p">[</span><span class="s2">"server_url"</span><span class="p">],</span>
                <span class="s2">"headers"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">PATauth</span><span class="p">[</span><span class="s1">'api_token'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">},</span>
            <span class="p">}</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">jira</span> <span class="o">=</span> <span class="n">JIRA</span><span class="p">(</span><span class="n">options</span><span class="o">=</span><span class="n">options</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">jira</span> <span class="o">=</span> <span class="n">JIRA</span><span class="p">(</span>
                <span class="n">basic_auth</span><span class="o">=</span><span class="p">(</span><span class="n">BasicAuth</span><span class="p">[</span><span class="s2">"email"</span><span class="p">],</span> <span class="n">BasicAuth</span><span class="p">[</span><span class="s2">"api_token"</span><span class="p">]),</span>
                <span class="n">server</span><span class="o">=</span><span class="sa">f</span><span class="s2">"https://</span><span class="si">{</span><span class="n">BasicAuth</span><span class="p">[</span><span class="s1">'server_url'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">relevant_issues</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">jira</span><span class="o">.</span><span class="n">search_issues</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="n">issues</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">assignee</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">reporter</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">epic_key</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">epic_summary</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">epic_descripton</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">for</span> <span class="n">issue</span> <span class="ow">in</span> <span class="n">relevant_issues</span><span class="p">:</span>
            <span class="c1"># Iterates through only issues and not epics</span>
            <span class="k">if</span> <span class="s2">"parent"</span> <span class="ow">in</span> <span class="p">(</span><span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">]):</span>
                <span class="k">if</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">assignee</span><span class="p">:</span>
                    <span class="n">assignee</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">assignee</span><span class="o">.</span><span class="n">displayName</span>

                <span class="k">if</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">reporter</span><span class="p">:</span>
                    <span class="n">reporter</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">reporter</span><span class="o">.</span><span class="n">displayName</span>

                <span class="k">if</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"key"</span><span class="p">]:</span>
                    <span class="n">epic_key</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"key"</span><span class="p">]</span>

                <span class="k">if</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"summary"</span><span class="p">]:</span>
                    <span class="n">epic_summary</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"summary"</span><span class="p">]</span>

                <span class="k">if</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"status"</span><span class="p">][</span><span class="s2">"description"</span><span class="p">]:</span>
                    <span class="n">epic_descripton</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">raw</span><span class="p">[</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"parent"</span><span class="p">][</span><span class="s2">"fields"</span><span class="p">][</span><span class="s2">"status"</span><span class="p">][</span>
                        <span class="s2">"description"</span>
                    <span class="p">]</span>

            <span class="n">issues</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2"> </span><span class="se">\n</span><span class="s2"> </span><span class="si">{</span><span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">description</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"id"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">summary</span><span class="p">,</span>
                        <span class="s2">"url"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">permalink</span><span class="p">(),</span>
                        <span class="s2">"created_at"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">created</span><span class="p">,</span>
                        <span class="s2">"updated_at"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">updated</span><span class="p">,</span>
                        <span class="s2">"labels"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">labels</span><span class="p">,</span>
                        <span class="s2">"status"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">status</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                        <span class="s2">"assignee"</span><span class="p">:</span> <span class="n">assignee</span><span class="p">,</span>
                        <span class="s2">"reporter"</span><span class="p">:</span> <span class="n">reporter</span><span class="p">,</span>
                        <span class="s2">"project"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">project</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                        <span class="s2">"issue_type"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">issuetype</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                        <span class="s2">"priority"</span><span class="p">:</span> <span class="n">issue</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">priority</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                        <span class="s2">"epic_key"</span><span class="p">:</span> <span class="n">epic_key</span><span class="p">,</span>
                        <span class="s2">"epic_summary"</span><span class="p">:</span> <span class="n">epic_summary</span><span class="p">,</span>
                        <span class="s2">"epic_description"</span><span class="p">:</span> <span class="n">epic_descripton</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">issues</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/)[Next Joplin](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/)
