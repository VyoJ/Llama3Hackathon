Title: Google - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/google/

Markdown Content:
Google - LlamaIndex


GmailReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GmailReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`, `BaseModel`

Gmail reader.

Reads emails

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `max_results` | `int` | 
Defaults to 10.



 | _required_ |
| `query` | `str` | 

Gmail query. Defaults to None.



 | _required_ |
| `service` | `Any` | 

Gmail service. Defaults to None.



 | _required_ |
| `results_per_page` | `Optional[int]` | 

Max number of results per page. Defaults to 10.



 | _required_ |
| `use_iterative_parser` | `bool` | 

Use iterative parser. Defaults to False.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
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
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GmailReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">,</span> <span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Gmail reader.</span>

<span class="sd">    Reads emails</span>

<span class="sd">    Args:</span>
<span class="sd">        max_results (int): Defaults to 10.</span>
<span class="sd">        query (str): Gmail query. Defaults to None.</span>
<span class="sd">        service (Any): Gmail service. Defaults to None.</span>
<span class="sd">        results_per_page (Optional[int]): Max number of results per page. Defaults to 10.</span>
<span class="sd">        use_iterative_parser (bool): Use iterative parser. Defaults to False.</span>
<span class="sd">    """</span>

    <span class="n">query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">use_iterative_parser</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">max_results</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span>
    <span class="n">service</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">results_per_page</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load emails from the user's account."""</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"gmail"</span><span class="p">,</span> <span class="s2">"v1"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

        <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_messages</span><span class="p">()</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"body"</span><span class="p">)</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="n">message</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_get_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get valid user credentials from storage.</span>

<span class="sd">        The file token.json stores the user's access and refresh tokens, and is</span>
<span class="sd">        created automatically when the authorization flow completes for the first</span>
<span class="sd">        time.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Credentials, the obtained credential.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="kn">from</span> <span class="nn">google_auth_oauthlib.flow</span> <span class="kn">import</span> <span class="n">InstalledAppFlow</span>

        <span class="kn">from</span> <span class="nn">google.auth.transport.requests</span> <span class="kn">import</span> <span class="n">Request</span>
        <span class="kn">from</span> <span class="nn">google.oauth2.credentials</span> <span class="kn">import</span> <span class="n">Credentials</span>

        <span class="n">creds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">):</span>
            <span class="n">creds</span> <span class="o">=</span> <span class="n">Credentials</span><span class="o">.</span><span class="n">from_authorized_user_file</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="n">SCOPES</span><span class="p">)</span>
        <span class="c1"># If there are no (valid) credentials available, let the user log in.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">creds</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">creds</span><span class="o">.</span><span class="n">valid</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">creds</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">expired</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">refresh_token</span><span class="p">:</span>
                <span class="n">creds</span><span class="o">.</span><span class="n">refresh</span><span class="p">(</span><span class="n">Request</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">flow</span> <span class="o">=</span> <span class="n">InstalledAppFlow</span><span class="o">.</span><span class="n">from_client_secrets_file</span><span class="p">(</span>
                    <span class="s2">"credentials.json"</span><span class="p">,</span> <span class="n">SCOPES</span>
                <span class="p">)</span>
                <span class="n">creds</span> <span class="o">=</span> <span class="n">flow</span><span class="o">.</span><span class="n">run_local_server</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
            <span class="c1"># Save the credentials for the next run</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">token</span><span class="p">:</span>
                <span class="n">token</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">creds</span><span class="o">.</span><span class="n">to_json</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">creds</span>

    <span class="k">def</span> <span class="nf">search_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span>

        <span class="n">max_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_results</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">results_per_page</span><span class="p">:</span>
            <span class="n">max_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results_per_page</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">messages</span><span class="p">()</span>
            <span class="o">.</span><span class="n">list</span><span class="p">(</span><span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="n">q</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">maxResults</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">max_results</span><span class="p">))</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">messages</span> <span class="o">=</span> <span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"messages"</span><span class="p">,</span> <span class="p">[])</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_results</span><span class="p">:</span>
            <span class="c1"># paginate if there are more results</span>
            <span class="k">while</span> <span class="s2">"nextPageToken"</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
                <span class="n">page_token</span> <span class="o">=</span> <span class="n">results</span><span class="p">[</span><span class="s2">"nextPageToken"</span><span class="p">]</span>
                <span class="n">results</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
                    <span class="o">.</span><span class="n">messages</span><span class="p">()</span>
                    <span class="o">.</span><span class="n">list</span><span class="p">(</span>
                        <span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span>
                        <span class="n">q</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                        <span class="n">pageToken</span><span class="o">=</span><span class="n">page_token</span><span class="p">,</span>
                        <span class="n">maxResults</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">max_results</span><span class="p">),</span>
                    <span class="p">)</span>
                    <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
                <span class="p">)</span>
                <span class="n">messages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">results</span><span class="p">[</span><span class="s2">"messages"</span><span class="p">])</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_results</span><span class="p">:</span>
                    <span class="k">break</span>

        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
                <span class="n">message_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_message_data</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">message_data</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message_data</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Can't get message data"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">result</span>

    <span class="k">def</span> <span class="nf">get_message_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
        <span class="n">message_id</span> <span class="o">=</span> <span class="n">message</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
        <span class="n">message_data</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">users</span><span class="p">()</span>
            <span class="o">.</span><span class="n">messages</span><span class="p">()</span>
            <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">format</span><span class="o">=</span><span class="s2">"raw"</span><span class="p">,</span> <span class="n">userId</span><span class="o">=</span><span class="s2">"me"</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">message_id</span><span class="p">)</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_iterative_parser</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body_iterative</span><span class="p">(</span><span class="n">message_data</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body</span><span class="p">(</span><span class="n">message_data</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">body</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="c1"># https://developers.google.com/gmail/api/reference/rest/v1/users.messages</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"id"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
            <span class="s2">"threadId"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"threadId"</span><span class="p">],</span>
            <span class="s2">"snippet"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"snippet"</span><span class="p">],</span>
            <span class="s2">"internalDate"</span><span class="p">:</span> <span class="n">message_data</span><span class="p">[</span><span class="s2">"internalDate"</span><span class="p">],</span>
            <span class="s2">"body"</span><span class="p">:</span> <span class="n">body</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">extract_message_body_iterative</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">message_from_bytes</span><span class="p">(</span><span class="n">body</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">message</span>

        <span class="n">body_text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="n">mime_msg</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span> <span class="o"></span> <span class="s2">"multipart"</span><span class="p">:</span>
            <span class="n">msg_parts</span> <span class="o">=</span> <span class="n">mime_msg</span><span class="o">.</span><span class="n">get_payload</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">msg_part</span> <span class="ow">in</span> <span class="n">msg_parts</span><span class="p">:</span>
                <span class="n">body_text</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">extract_message_body_iterative</span><span class="p">(</span><span class="n">msg_part</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">body_text</span>

    <span class="k">def</span> <span class="nf">extract_message_body</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"raw"</span><span class="p">]</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="n">mime_msg</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">message_from_bytes</span><span class="p">(</span><span class="n">body</span><span class="p">)</span>

            <span class="c1"># If the message body contains HTML, parse it with BeautifulSoup</span>
            <span class="k">if</span> <span class="s2">"text/html"</span> <span class="ow">in</span> <span class="n">mime_msg</span><span class="p">:</span>
                <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">body</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
                <span class="n">body</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
            <span class="k">return</span> <span class="n">body</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Can't parse message body"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GmailReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load emails from the user's account.

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/gmail/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
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
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load emails from the user's account."""</span>
    <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

    <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"gmail"</span><span class="p">,</span> <span class="s2">"v1"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

    <span class="n">messages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">search_messages</span><span class="p">()</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"body"</span><span class="p">)</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="n">message</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

GoogleCalendarReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleCalendarReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Google Calendar reader.

Reads events from Google Calendar

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/calendar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 27</span>
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
<span class="normal">135</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleCalendarReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Calendar reader.</span>

<span class="sd">    Reads events from Google Calendar</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
        <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from user's calendar.</span>

<span class="sd">        Args:</span>
<span class="sd">            number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">            start_date (Optional[Union[str, datetime.date]]): the start date to return events from. Defaults to today.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

        <span class="n">start_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">combine</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">min</span><span class="p">)</span>
        <span class="n">start_datetime_utc</span> <span class="o">=</span> <span class="n">start_datetime</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">Z"</span><span class="p">)</span>

        <span class="n">events_result</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span>
            <span class="o">.</span><span class="n">list</span><span class="p">(</span>
                <span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span>
                <span class="n">timeMin</span><span class="o">=</span><span class="n">start_datetime_utc</span><span class="p">,</span>
                <span class="n">maxResults</span><span class="o">=</span><span class="n">number_of_results</span><span class="p">,</span>
                <span class="n">singleEvents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">orderBy</span><span class="o">=</span><span class="s2">"startTime"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="n">events</span> <span class="o">=</span> <span class="n">events_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"items"</span><span class="p">,</span> <span class="p">[])</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">]:</span>
                <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

            <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">]:</span>
                <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

            <span class="n">event_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Status: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'status'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Summary: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'summary'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Start time: </span><span class="si">{</span><span class="n">start_time</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"End time: </span><span class="si">{</span><span class="n">end_time</span><span class="si">}</span><span class="s2">, "</span>

            <span class="n">organizer</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"organizer"</span><span class="p">,</span> <span class="p">{})</span>
            <span class="n">display_name</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"displayName"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
            <span class="n">email</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"email"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">display_name</span> <span class="o">!=</span> <span class="s2">"N/A"</span><span class="p">:</span>
                <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">)"</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">event_string</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_get_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get valid user credentials from storage.</span>

<span class="sd">        The file token.json stores the user's access and refresh tokens, and is</span>
<span class="sd">        created automatically when the authorization flow completes for the first</span>
<span class="sd">        time.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Credentials, the obtained credential.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">google_auth_oauthlib.flow</span> <span class="kn">import</span> <span class="n">InstalledAppFlow</span>

        <span class="kn">from</span> <span class="nn">google.auth.transport.requests</span> <span class="kn">import</span> <span class="n">Request</span>
        <span class="kn">from</span> <span class="nn">google.oauth2.credentials</span> <span class="kn">import</span> <span class="n">Credentials</span>

        <span class="n">creds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">):</span>
            <span class="n">creds</span> <span class="o">=</span> <span class="n">Credentials</span><span class="o">.</span><span class="n">from_authorized_user_file</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="n">SCOPES</span><span class="p">)</span>
        <span class="c1"># If there are no (valid) credentials available, let the user log in.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">creds</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">creds</span><span class="o">.</span><span class="n">valid</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">creds</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">expired</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">refresh_token</span><span class="p">:</span>
                <span class="n">creds</span><span class="o">.</span><span class="n">refresh</span><span class="p">(</span><span class="n">Request</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">flow</span> <span class="o">=</span> <span class="n">InstalledAppFlow</span><span class="o">.</span><span class="n">from_client_secrets_file</span><span class="p">(</span>
                    <span class="s2">"credentials.json"</span><span class="p">,</span> <span class="n">SCOPES</span>
                <span class="p">)</span>
                <span class="n">creds</span> <span class="o">=</span> <span class="n">flow</span><span class="o">.</span><span class="n">run_local_server</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
            <span class="c1"># Save the credentials for the next run</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">token</span><span class="p">:</span>
                <span class="n">token</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">creds</span><span class="o">.</span><span class="n">to_json</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">creds</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleCalendarReader.load_data "Permanent link")

```
load_data(number_of_results: Optional[int] = 100, start_date: Optional[Union[str, date]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from user's calendar.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `number_of_results` | `Optional[int]` | 
the number of events to return. Defaults to 100.



 | `100` |
| `start_date` | `Optional[Union[str, date]]` | 

the start date to return events from. Defaults to today.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/calendar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 34</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from user's calendar.</span>

<span class="sd">    Args:</span>
<span class="sd">        number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">        start_date (Optional[Union[str, datetime.date]]): the start date to return events from. Defaults to today.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

    <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
    <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"calendar"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

    <span class="n">start_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">combine</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">min</span><span class="p">)</span>
    <span class="n">start_datetime_utc</span> <span class="o">=</span> <span class="n">start_datetime</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">T%H:%M:%S.</span><span class="si">%f</span><span class="s2">Z"</span><span class="p">)</span>

    <span class="n">events_result</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">service</span><span class="o">.</span><span class="n">events</span><span class="p">()</span>
        <span class="o">.</span><span class="n">list</span><span class="p">(</span>
            <span class="n">calendarId</span><span class="o">=</span><span class="s2">"primary"</span><span class="p">,</span>
            <span class="n">timeMin</span><span class="o">=</span><span class="n">start_datetime_utc</span><span class="p">,</span>
            <span class="n">maxResults</span><span class="o">=</span><span class="n">number_of_results</span><span class="p">,</span>
            <span class="n">singleEvents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">orderBy</span><span class="o">=</span><span class="s2">"startTime"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
    <span class="p">)</span>

    <span class="n">events</span> <span class="o">=</span> <span class="n">events_result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"items"</span><span class="p">,</span> <span class="p">[])</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">]:</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"start"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

        <span class="k">if</span> <span class="s2">"dateTime"</span> <span class="ow">in</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">]:</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"dateTime"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">event</span><span class="p">[</span><span class="s2">"end"</span><span class="p">][</span><span class="s2">"date"</span><span class="p">]</span>

        <span class="n">event_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Status: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'status'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Summary: </span><span class="si">{</span><span class="n">event</span><span class="p">[</span><span class="s1">'summary'</span><span class="p">]</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Start time: </span><span class="si">{</span><span class="n">start_time</span><span class="si">}</span><span class="s2">, "</span>
        <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"End time: </span><span class="si">{</span><span class="n">end_time</span><span class="si">}</span><span class="s2">, "</span>

        <span class="n">organizer</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"organizer"</span><span class="p">,</span> <span class="p">{})</span>
        <span class="n">display_name</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"displayName"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
        <span class="n">email</span> <span class="o">=</span> <span class="n">organizer</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"email"</span><span class="p">,</span> <span class="s2">"N/A"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">display_name</span> <span class="o">!=</span> <span class="s2">"N/A"</span><span class="p">:</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">)"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">event_string</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"Organizer: </span><span class="si">{</span><span class="n">email</span><span class="si">}</span><span class="s2">"</span>

        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">event_string</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

GoogleChatReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleChatReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Google Chat Reader.

Reads messages from Google Chat

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/chat/base.py`

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
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleChatReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Chat Reader.</span>

<span class="sd">    Reads messages from Google Chat</span>
<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Gets name identifier of class."""</span>
        <span class="k">return</span> <span class="s2">"GoogleChatReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">space_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">num_messages</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">after</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">before</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">order_asc</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Loads documents from Google Chat.</span>

<span class="sd">        Args:</span>
<span class="sd">            space_name (List[str]): List of Space ID names found at top of URL (without the "space/").</span>
<span class="sd">            num_messages (int, optional): Number of messages to load (may exceed this number). If -1, then loads all messages. Defaults to -1.</span>
<span class="sd">            after (datetime, optional): Only search for messages after this datetime (UTC). Defaults to None.</span>
<span class="sd">            before (datetime, optional): Only search for messages before this datetime (UTC). Defaults to None.</span>
<span class="sd">            order_asc (bool, optional): If messages should be ordered by ascending time order. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of document objects</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>

        <span class="c1"># get credentials and create chat service</span>
        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"chat"</span><span class="p">,</span> <span class="s2">"v1"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Credentials successfully obtained."</span><span class="p">)</span>

        <span class="n">res</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">space_name</span> <span class="ow">in</span> <span class="n">space_names</span><span class="p">:</span>
            <span class="n">all_msgs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_msgs</span><span class="p">(</span>
                <span class="n">service</span><span class="p">,</span> <span class="n">space_name</span><span class="p">,</span> <span class="n">num_messages</span><span class="p">,</span> <span class="n">after</span><span class="p">,</span> <span class="n">before</span><span class="p">,</span> <span class="n">order_asc</span>
            <span class="p">)</span>  <span class="c1"># gets raw API output in list of dict</span>
            <span class="n">msgs_sorted</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sort_msgs</span><span class="p">(</span>
                <span class="n">space_name</span><span class="p">,</span> <span class="n">all_msgs</span>
            <span class="p">)</span>  <span class="c1"># puts messages into list of Document objects</span>
            <span class="n">res</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">msgs_sorted</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Successfully retrieved messages from </span><span class="si">{</span><span class="n">space_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">res</span>

    <span class="k">def</span> <span class="nf">_sort_msgs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">space_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">all_msgs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Sorts messages from space and puts them into Document.</span>

<span class="sd">        Args:</span>
<span class="sd">            space_name (str): Space ID</span>
<span class="sd">            all_msgs (List[Dict[str, Any]]): All messages</span>
<span class="sd">            order_asc (bool): If ordered by ascending order</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: Document with messages</span>
<span class="sd">        """</span>
        <span class="n">res</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">id_to_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_id_to_text</span><span class="p">(</span>
            <span class="n">all_msgs</span>
        <span class="p">)</span>  <span class="c1"># maps message ID to text (useful for retrieving info about quote replies)</span>
        <span class="n">thread_msg_cnt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_thread_msg_cnt</span><span class="p">(</span>
            <span class="n">all_msgs</span>
        <span class="p">)</span>  <span class="c1"># gets message count in each thread</span>
        <span class="k">for</span> <span class="n">msg</span> <span class="ow">in</span> <span class="n">all_msgs</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">any</span><span class="p">(</span>
                <span class="n">i</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">msg</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="p">(</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">,</span> <span class="s2">"thread"</span><span class="p">,</span> <span class="s2">"sender"</span><span class="p">,</span> <span class="s2">"createTime"</span><span class="p">)</span>
            <span class="p">):</span>
                <span class="c1"># invalid message</span>
                <span class="k">continue</span>

            <span class="k">if</span> <span class="s2">"name"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"thread"</span><span class="p">]</span> <span class="ow">or</span> <span class="s2">"name"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"sender"</span><span class="p">]:</span>
                <span class="c1"># invalid message</span>
                <span class="k">continue</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"space_id"</span><span class="p">:</span> <span class="n">space_name</span><span class="p">,</span>
                <span class="s2">"sender_id"</span><span class="p">:</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"sender"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">],</span>
                <span class="s2">"timestamp"</span><span class="p">:</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"createTime"</span><span class="p">],</span>
            <span class="p">}</span>

            <span class="k">if</span> <span class="p">(</span>
                <span class="s2">"quotedMessageMetadata"</span> <span class="ow">in</span> <span class="n">msg</span>
                <span class="ow">and</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"quotedMessageMetadata"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">id_to_text</span>
            <span class="p">):</span>
                <span class="c1"># metadata for a quote reply</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"quoted_msg"</span><span class="p">]</span> <span class="o">=</span> <span class="n">id_to_text</span><span class="p">[</span>
                    <span class="n">msg</span><span class="p">[</span><span class="s2">"quotedMessageMetadata"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
                <span class="p">]</span>

            <span class="c1"># adds metadata for threads</span>
            <span class="c1"># all threads with a message count of 1 gets counted as the "main thread"</span>
            <span class="n">thread_id</span> <span class="o">=</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"thread"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">thread_msg_cnt</span><span class="p">[</span><span class="n">thread_id</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"thread_id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">thread_id</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"thread_id"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"Main Thread"</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">id_</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">text</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>
            <span class="n">res</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">res</span>

    <span class="k">def</span> <span class="nf">_id_to_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">all_msgs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Maps message ID to text, used for quote replies.</span>

<span class="sd">        Args:</span>
<span class="sd">            all_msgs (List[Dict[str, Any]]): All messages</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, str]: Map message ID -&gt; message text</span>
<span class="sd">        """</span>
        <span class="n">res</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">for</span> <span class="n">msg</span> <span class="ow">in</span> <span class="n">all_msgs</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">msg</span> <span class="ow">or</span> <span class="s2">"name"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">msg</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">res</span><span class="p">[</span><span class="n">msg</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">res</span>

    <span class="k">def</span> <span class="nf">_get_thread_msg_cnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">all_msgs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Gets message count for each thread ID.</span>

<span class="sd">        Args:</span>
<span class="sd">            all_msgs (List[Dict[str, Any]]): All messages</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, int]: Maps thread ID -&gt; count of messages that were in that thread</span>
<span class="sd">        """</span>
        <span class="c1"># maps thread ID -&gt; count</span>
        <span class="n">threads_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">msg</span> <span class="ow">in</span> <span class="n">all_msgs</span><span class="p">:</span>
            <span class="n">thread_name</span> <span class="o">=</span> <span class="n">msg</span><span class="p">[</span><span class="s2">"thread"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">thread_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">threads_dict</span><span class="p">:</span>
                <span class="c1"># add thread name to dict</span>
                <span class="n">threads_dict</span><span class="p">[</span><span class="n">thread_name</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">threads_dict</span><span class="p">[</span><span class="n">thread_name</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="k">return</span> <span class="n">threads_dict</span>

    <span class="k">def</span> <span class="nf">_get_msgs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">service</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">space_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_messages</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">after</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">before</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">order_asc</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Puts raw API output of chat messages from one space into a list.</span>

<span class="sd">        Args:</span>
<span class="sd">            service (Any): Google Chat API service object</span>
<span class="sd">            space_name (str): Space ID name found at top of URL (without the "space/").</span>
<span class="sd">            num_messages (int, optional): Number of messages to load (may exceed this number). If -1, then loads all messages. Defaults to -1.</span>
<span class="sd">            after (datetime, optional): Only search for messages after this datetime (UTC). Defaults to None.</span>
<span class="sd">            before (datetime, optional): Only search for messages before this datetime (UTC). Defaults to None.</span>
<span class="sd">            order_asc (bool, optional): If messages should be ordered by ascending time order. Defaults to True.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Dict[str, Any]]: List of message objects</span>
<span class="sd">        """</span>
        <span class="n">all_msgs</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># API parameters</span>
        <span class="n">parent</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"spaces/</span><span class="si">{</span><span class="n">space_name</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">page_token</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">filter_str</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="n">after</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">offset_str</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">if</span> <span class="n">after</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">offset_str</span> <span class="o">=</span> <span class="s2">"+00:00"</span>
            <span class="n">filter_str</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">'createTime &gt; "</span><span class="si">{</span><span class="n">after</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(</span><span class="s2">"T"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">offset_str</span><span class="si">}</span><span class="s1">" AND '</span>
        <span class="k">if</span> <span class="n">before</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">offset_str</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">if</span> <span class="n">before</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">offset_str</span> <span class="o">=</span> <span class="s2">"+00:00"</span>
            <span class="n">filter_str</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">'createTime &lt; "</span><span class="si">{</span><span class="n">before</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(</span><span class="s2">"T"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">offset_str</span><span class="si">}</span><span class="s1">" AND '</span>
        <span class="n">filter_str</span> <span class="o">=</span> <span class="n">filter_str</span><span class="p">[:</span><span class="o">-</span><span class="mi">4</span><span class="p">]</span>
        <span class="n">order_by</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"createTime </span><span class="si">{</span><span class="s1">'ASC'</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">order_asc</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s1">'DESC'</span><span class="si">}</span><span class="s2">"</span>

        <span class="c1"># Get all messages from space</span>
        <span class="k">while</span> <span class="n">num_messages</span> <span class="o"></span> <span class="s2">"TITLE"</span><span class="p">:</span>
                <span class="n">level</span> <span class="o">=</span> <span class="mi">0</span>
                <span class="n">heading_key</span> <span class="o">=</span> <span class="s2">"title"</span>
            <span class="k">elif</span> <span class="n">style_type</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"HEADING_"</span><span class="p">):</span>
                <span class="n">level</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">style_type</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"_"</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>
                <span class="k">if</span> <span class="n">level</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">split_on_heading_level</span><span class="p">:</span>
                    <span class="k">return</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>

                <span class="n">heading_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Header </span><span class="si">{</span><span class="n">level</span><span class="si">}</span><span class="s2">"</span>

        <span class="k">return</span> <span class="n">level</span><span class="p">,</span> <span class="n">heading_key</span><span class="p">,</span> <span class="n">heading_id</span>

    <span class="k">def</span> <span class="nf">_generate_doc_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">metadata</span><span class="p">:</span> <span class="nb">dict</span><span class="p">):</span>
        <span class="k">if</span> <span class="s2">"heading_id"</span> <span class="ow">in</span> <span class="n">metadata</span><span class="p">:</span>
            <span class="n">heading_id</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"heading_id"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">heading_id</span> <span class="o">=</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">ascii_letters</span> <span class="o">+</span> <span class="n">string</span><span class="o">.</span><span class="n">digits</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">8</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">metadata</span><span class="p">[</span><span class="s1">'document_id'</span><span class="p">]</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">heading_id</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">_structural_elements_to_docs</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">doc_metadata</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Recurse through a list of Structural Elements.</span>

<span class="sd">        Split documents on heading if split_on_heading_level is set.</span>

<span class="sd">        Args:</span>
<span class="sd">            elements: a list of Structural Elements.</span>
<span class="sd">        """</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">current_heading_level</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">split_on_heading_level</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="n">doc_metadata</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">elements</span><span class="p">:</span>
            <span class="n">element_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_structural_elements</span><span class="p">([</span><span class="n">value</span><span class="p">])</span>

            <span class="n">level</span><span class="p">,</span> <span class="n">heading_key</span><span class="p">,</span> <span class="n">heading_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_determine_heading_level</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">level</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">level</span> <span class="o"></span> <span class="n">folder_mime_type</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">drive_id</span><span class="p">:</span>
                            <span class="n">fileids_meta</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                                <span class="bp">self</span><span class="o">.</span><span class="n">_get_fileids_meta</span><span class="p">(</span>
                                    <span class="n">drive_id</span><span class="o">=</span><span class="n">drive_id</span><span class="p">,</span>
                                    <span class="n">folder_id</span><span class="o">=</span><span class="n">item</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                                    <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
                                    <span class="n">query_string</span><span class="o">=</span><span class="n">query_string</span><span class="p">,</span>
                                <span class="p">)</span>
                            <span class="p">)</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">fileids_meta</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                                <span class="bp">self</span><span class="o">.</span><span class="n">_get_fileids_meta</span><span class="p">(</span>
                                    <span class="n">folder_id</span><span class="o">=</span><span class="n">item</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                                    <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
                                    <span class="n">query_string</span><span class="o">=</span><span class="n">query_string</span><span class="p">,</span>
                                <span class="p">)</span>
                            <span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="c1"># Check if file doesn't belong to a Shared Drive. "owners" doesn't exist in a Shared Drive</span>
                        <span class="n">is_shared_drive</span> <span class="o">=</span> <span class="s2">"driveId"</span> <span class="ow">in</span> <span class="n">item</span>
                        <span class="n">author</span> <span class="o">=</span> <span class="p">(</span>
                            <span class="n">item</span><span class="p">[</span><span class="s2">"owners"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">"displayName"</span><span class="p">]</span>
                            <span class="k">if</span> <span class="ow">not</span> <span class="n">is_shared_drive</span>
                            <span class="k">else</span> <span class="s2">"Shared Drive"</span>
                        <span class="p">)</span>

                        <span class="n">fileids_meta</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="p">(</span>
                                <span class="n">item</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                                <span class="n">author</span><span class="p">,</span>
                                <span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                                <span class="n">item</span><span class="p">[</span><span class="s2">"mimeType"</span><span class="p">],</span>
                                <span class="n">item</span><span class="p">[</span><span class="s2">"createdTime"</span><span class="p">],</span>
                                <span class="n">item</span><span class="p">[</span><span class="s2">"modifiedTime"</span><span class="p">],</span>
                            <span class="p">)</span>
                        <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Get the file details</span>
                <span class="n">file</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">service</span><span class="o">.</span><span class="n">files</span><span class="p">()</span>
                    <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">fileId</span><span class="o">=</span><span class="n">file_id</span><span class="p">,</span> <span class="n">supportsAllDrives</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="s2">"*"</span><span class="p">)</span>
                    <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
                <span class="p">)</span>
                <span class="c1"># Get metadata of the file</span>
                <span class="c1"># Check if file doesn't belong to a Shared Drive. "owners" doesn't exist in a Shared Drive</span>
                <span class="n">is_shared_drive</span> <span class="o">=</span> <span class="s2">"driveId"</span> <span class="ow">in</span> <span class="n">file</span>
                <span class="n">author</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">file</span><span class="p">[</span><span class="s2">"owners"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">"displayName"</span><span class="p">]</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="n">is_shared_drive</span>
                    <span class="k">else</span> <span class="s2">"Shared Drive"</span>
                <span class="p">)</span>

                <span class="n">fileids_meta</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="p">(</span>
                        <span class="n">file</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                        <span class="n">author</span><span class="p">,</span>
                        <span class="n">file</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                        <span class="n">file</span><span class="p">[</span><span class="s2">"mimeType"</span><span class="p">],</span>
                        <span class="n">file</span><span class="p">[</span><span class="s2">"createdTime"</span><span class="p">],</span>
                        <span class="n">file</span><span class="p">[</span><span class="s2">"modifiedTime"</span><span class="p">],</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">return</span> <span class="n">fileids_meta</span>

        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"An error occurred while getting fileids metadata: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_download_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fileid</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">filename</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Download the file with fileid and filename</span>
<span class="sd">        Args:</span>
<span class="sd">            fileid: file id of the file in google drive</span>
<span class="sd">            filename: filename with which it will be downloaded</span>
<span class="sd">        Returns:</span>
<span class="sd">            The downloaded filename, which which may have a new extension.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span>

        <span class="kn">from</span> <span class="nn">googleapiclient.discovery</span> <span class="kn">import</span> <span class="n">build</span>
        <span class="kn">from</span> <span class="nn">googleapiclient.http</span> <span class="kn">import</span> <span class="n">MediaIoBaseDownload</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># Get file details</span>
            <span class="n">service</span> <span class="o">=</span> <span class="n">build</span><span class="p">(</span><span class="s2">"drive"</span><span class="p">,</span> <span class="s2">"v3"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_creds</span><span class="p">)</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">files</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">fileId</span><span class="o">=</span><span class="n">fileid</span><span class="p">,</span> <span class="n">supportsAllDrives</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>

            <span class="k">if</span> <span class="n">file</span><span class="p">[</span><span class="s2">"mimeType"</span><span class="p">]</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mimetypes</span><span class="p">:</span>
                <span class="n">download_mimetype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mimetypes</span><span class="p">[</span><span class="n">file</span><span class="p">[</span><span class="s2">"mimeType"</span><span class="p">]][</span><span class="s2">"mimetype"</span><span class="p">]</span>
                <span class="n">download_extension</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_mimetypes</span><span class="p">[</span><span class="n">file</span><span class="p">[</span><span class="s2">"mimeType"</span><span class="p">]][</span><span class="s2">"extension"</span><span class="p">]</span>
                <span class="n">new_file_name</span> <span class="o">=</span> <span class="n">filename</span> <span class="o">+</span> <span class="n">download_extension</span>

                <span class="c1"># Download and convert file</span>
                <span class="n">request</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">files</span><span class="p">()</span><span class="o">.</span><span class="n">export_media</span><span class="p">(</span>
                    <span class="n">fileId</span><span class="o">=</span><span class="n">fileid</span><span class="p">,</span> <span class="n">mimeType</span><span class="o">=</span><span class="n">download_mimetype</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">new_file_name</span> <span class="o">=</span> <span class="n">filename</span>

                <span class="c1"># Download file without conversion</span>
                <span class="n">request</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">files</span><span class="p">()</span><span class="o">.</span><span class="n">get_media</span><span class="p">(</span><span class="n">fileId</span><span class="o">=</span><span class="n">fileid</span><span class="p">)</span>

            <span class="c1"># Download file data</span>
            <span class="n">file_data</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">()</span>
            <span class="n">downloader</span> <span class="o">=</span> <span class="n">MediaIoBaseDownload</span><span class="p">(</span><span class="n">file_data</span><span class="p">,</span> <span class="n">request</span><span class="p">)</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>

            <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span><span class="p">:</span>
                <span class="n">status</span><span class="p">,</span> <span class="n">done</span> <span class="o">=</span> <span class="n">downloader</span><span class="o">.</span><span class="n">next_chunk</span><span class="p">()</span>

            <span class="c1"># Save the downloaded file</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">new_file_name</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">file_data</span><span class="o">.</span><span class="n">getvalue</span><span class="p">())</span>

            <span class="k">return</span> <span class="n">new_file_name</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"An error occurred while downloading file: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_data_fileids_meta</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fileids_meta</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from fileids metadata</span>
<span class="sd">        Args:</span>
<span class="sd">            fileids_meta: metadata of fileids in google drive.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Lis[Document]: List of Document of data present in fileids.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>

                <span class="k">def</span> <span class="nf">get_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
                    <span class="k">return</span> <span class="n">metadata</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span>

                <span class="n">temp_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">)</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>

                <span class="k">for</span> <span class="n">fileid_meta</span> <span class="ow">in</span> <span class="n">fileids_meta</span><span class="p">:</span>
                    <span class="c1"># Download files and name them with their fileid</span>
                    <span class="n">fileid</span> <span class="o">=</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                    <span class="n">filepath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">,</span> <span class="n">fileid</span><span class="p">)</span>
                    <span class="n">final_filepath</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_file</span><span class="p">(</span><span class="n">fileid</span><span class="p">,</span> <span class="n">filepath</span><span class="p">)</span>

                    <span class="c1"># Add metadata of the file to metadata dictionary</span>
                    <span class="n">metadata</span><span class="p">[</span><span class="n">final_filepath</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="s2">"file id"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                        <span class="s2">"author"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
                        <span class="s2">"file name"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
                        <span class="s2">"mime type"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span>
                        <span class="s2">"created at"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">4</span><span class="p">],</span>
                        <span class="s2">"modified at"</span><span class="p">:</span> <span class="n">fileid_meta</span><span class="p">[</span><span class="mi">5</span><span class="p">],</span>
                    <span class="p">}</span>
                <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
                    <span class="n">temp_dir</span><span class="p">,</span>
                    <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
                    <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_metadata</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">documents</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
                <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
                    <span class="n">doc</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file id"</span><span class="p">,</span> <span class="n">doc</span><span class="o">.</span><span class="n">id_</span><span class="p">)</span>

            <span class="k">return</span> <span class="n">documents</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"An error occurred while loading data from fileids meta: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_from_file_ids</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">file_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
        <span class="n">query_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from file ids</span>
<span class="sd">        Args:</span>
<span class="sd">            file_ids: File ids of the files in google drive.</span>
<span class="sd">            mime_types: The mimeTypes you want to allow e.g.: "application/vnd.google-apps.document"</span>
<span class="sd">            query_string: List of query strings to filter the documents, e.g. "name contains 'test'".</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: List of Documents of text.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">fileids_meta</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">file_id</span> <span class="ow">in</span> <span class="n">file_ids</span><span class="p">:</span>
                <span class="n">fileids_meta</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_get_fileids_meta</span><span class="p">(</span>
                        <span class="n">drive_id</span><span class="o">=</span><span class="n">drive_id</span><span class="p">,</span>
                        <span class="n">file_id</span><span class="o">=</span><span class="n">file_id</span><span class="p">,</span>
                        <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
                        <span class="n">query_string</span><span class="o">=</span><span class="n">query_string</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_fileids_meta</span><span class="p">(</span><span class="n">fileids_meta</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"An error occurred while loading with fileid: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_from_folder</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">folder_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
        <span class="n">query_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from folder_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            drive_id: Drive id of the shared drive in google drive.</span>
<span class="sd">            folder_id: folder id of the folder in google drive.</span>
<span class="sd">            mime_types: The mimeTypes you want to allow e.g.: "application/vnd.google-apps.document"</span>
<span class="sd">            query_string: A more generic query string to filter the documents, e.g. "name contains 'test'".</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: List of Documents of text.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">fileids_meta</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_fileids_meta</span><span class="p">(</span>
                <span class="n">drive_id</span><span class="o">=</span><span class="n">drive_id</span><span class="p">,</span>
                <span class="n">folder_id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">,</span>
                <span class="n">mime_types</span><span class="o">=</span><span class="n">mime_types</span><span class="p">,</span>
                <span class="n">query_string</span><span class="o">=</span><span class="n">query_string</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_fileids_meta</span><span class="p">(</span><span class="n">fileids_meta</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"An error occurred while loading from folder: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">exc_info</span><span class="o">=</span><span class="kc">True</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>  <span class="c1"># Deprecated</span>
        <span class="n">query_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the folder id or file ids.</span>

<span class="sd">        Args:</span>
<span class="sd">            drive_id: Drive id of the shared drive in google drive.</span>
<span class="sd">            folder_id: Folder id of the folder in google drive.</span>
<span class="sd">            file_ids: File ids of the files in google drive.</span>
<span class="sd">            mime_types: The mimeTypes you want to allow e.g.: "application/vnd.google-apps.document"</span>
<span class="sd">            query_string: A more generic query string to filter the documents, e.g. "name contains 'test'".</span>
<span class="sd">                It gives more flexibility to filter the documents. More info: https://developers.google.com/drive/api/v3/search-files</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_creds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>

        <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
        <span class="k">if</span> <span class="n">drive_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">drive_id</span>
        <span class="k">if</span> <span class="n">folder_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">folder_id</span>
        <span class="k">if</span> <span class="n">file_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">file_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_ids</span>
        <span class="k">if</span> <span class="n">query_string</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_string</span>

        <span class="k">if</span> <span class="n">folder_id</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_from_folder</span><span class="p">(</span><span class="n">drive_id</span><span class="p">,</span> <span class="n">folder_id</span><span class="p">,</span> <span class="n">mime_types</span><span class="p">,</span> <span class="n">query_string</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">file_ids</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_from_file_ids</span><span class="p">(</span>
                <span class="n">drive_id</span><span class="p">,</span> <span class="n">file_ids</span><span class="p">,</span> <span class="n">mime_types</span><span class="p">,</span> <span class="n">query_string</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Either 'folder_id' or 'file_ids' must be provided."</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleDriveReader.load_data "Permanent link")

```
load_data(drive_id: Optional[str] = None, folder_id: Optional[str] = None, file_ids: Optional[List[str]] = None, mime_types: Optional[List[str]] = None, query_string: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the folder id or file ids.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `drive_id` | `Optional[str]` | 
Drive id of the shared drive in google drive.



 | `None` |
| `folder_id` | `Optional[str]` | 

Folder id of the folder in google drive.



 | `None` |
| `file_ids` | `Optional[List[str]]` | 

File ids of the files in google drive.



 | `None` |
| `mime_types` | `Optional[List[str]]` | 

The mimeTypes you want to allow e.g.: "application/vnd.google-apps.document"



 | `None` |
| `query_string` | `Optional[str]` | 

A more generic query string to filter the documents, e.g. "name contains 'test'". It gives more flexibility to filter the documents. More info: https://developers.google.com/drive/api/v3/search-files



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/drive/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">drive_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">folder_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">file_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mime_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>  <span class="c1"># Deprecated</span>
    <span class="n">query_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the folder id or file ids.</span>

<span class="sd">    Args:</span>
<span class="sd">        drive_id: Drive id of the shared drive in google drive.</span>
<span class="sd">        folder_id: Folder id of the folder in google drive.</span>
<span class="sd">        file_ids: File ids of the files in google drive.</span>
<span class="sd">        mime_types: The mimeTypes you want to allow e.g.: "application/vnd.google-apps.document"</span>
<span class="sd">        query_string: A more generic query string to filter the documents, e.g. "name contains 'test'".</span>
<span class="sd">            It gives more flexibility to filter the documents. More info: https://developers.google.com/drive/api/v3/search-files</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_creds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>

    <span class="c1"># If no arguments are provided to load_data, default to the object attributes</span>
    <span class="k">if</span> <span class="n">drive_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">drive_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">drive_id</span>
    <span class="k">if</span> <span class="n">folder_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">folder_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">folder_id</span>
    <span class="k">if</span> <span class="n">file_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">file_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_ids</span>
    <span class="k">if</span> <span class="n">query_string</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">query_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_string</span>

    <span class="k">if</span> <span class="n">folder_id</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_from_folder</span><span class="p">(</span><span class="n">drive_id</span><span class="p">,</span> <span class="n">folder_id</span><span class="p">,</span> <span class="n">mime_types</span><span class="p">,</span> <span class="n">query_string</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">file_ids</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_from_file_ids</span><span class="p">(</span>
            <span class="n">drive_id</span><span class="p">,</span> <span class="n">file_ids</span><span class="p">,</span> <span class="n">mime_types</span><span class="p">,</span> <span class="n">query_string</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">"Either 'folder_id' or 'file_ids' must be provided."</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[]</span>
</code></pre></div></td></tr></tbody></table>

GoogleKeepReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleKeepReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Google Keep reader.

Reads notes from Google Keep

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/keep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
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
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
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
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleKeepReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Keep reader.</span>

<span class="sd">    Reads notes from Google Keep</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the document_ids.</span>

<span class="sd">        Args:</span>
<span class="sd">            document_ids (List[str]): a list of note ids.</span>
<span class="sd">        """</span>
        <span class="n">keep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keep</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">document_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "document_ids" in `load_kwargs`.'</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">note_id</span> <span class="ow">in</span> <span class="n">document_ids</span><span class="p">:</span>
            <span class="n">note</span> <span class="o">=</span> <span class="n">keep</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">note_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">note</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Note with id </span><span class="si">{</span><span class="n">note_id</span><span class="si">}</span><span class="s2"> not found."</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Title: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="s2">Content: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"note_id"</span><span class="p">:</span> <span class="n">note_id</span><span class="p">}))</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">load_all_notes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load all notes from Google Keep."""</span>
        <span class="n">keep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keep</span><span class="p">()</span>

        <span class="n">notes</span> <span class="o">=</span> <span class="n">keep</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">note</span> <span class="ow">in</span> <span class="n">notes</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Title: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="s2">Content: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"note_id"</span><span class="p">:</span> <span class="n">note</span><span class="o">.</span><span class="n">id</span><span class="p">}))</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_get_keep</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">gkeepapi</span>

<span class="w">        </span><span class="sd">"""Get a Google Keep object with login."""</span>
        <span class="c1"># Read username and password from keep_credentials.json</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"keep_credentials.json"</span><span class="p">):</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"keep_credentials.json"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">credentials</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">"Failed to load keep_credentials.json."</span><span class="p">)</span>

        <span class="n">keep</span> <span class="o">=</span> <span class="n">gkeepapi</span><span class="o">.</span><span class="n">Keep</span><span class="p">()</span>

        <span class="n">success</span> <span class="o">=</span> <span class="n">keep</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">credentials</span><span class="p">[</span><span class="s2">"username"</span><span class="p">],</span> <span class="n">credentials</span><span class="p">[</span><span class="s2">"password"</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">success</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">"Failed to login to Google Keep."</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">keep</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleKeepReader.load_data "Permanent link")

```
load_data(document_ids: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the document\_ids.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `document_ids` | `List[str]` | 
a list of note ids.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/keep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
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
<span class="normal">36</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the document_ids.</span>

<span class="sd">    Args:</span>
<span class="sd">        document_ids (List[str]): a list of note ids.</span>
<span class="sd">    """</span>
    <span class="n">keep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keep</span><span class="p">()</span>

    <span class="k">if</span> <span class="n">document_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "document_ids" in `load_kwargs`.'</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">note_id</span> <span class="ow">in</span> <span class="n">document_ids</span><span class="p">:</span>
        <span class="n">note</span> <span class="o">=</span> <span class="n">keep</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">note_id</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">note</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Note with id </span><span class="si">{</span><span class="n">note_id</span><span class="si">}</span><span class="s2"> not found."</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Title: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="s2">Content: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"note_id"</span><span class="p">:</span> <span class="n">note_id</span><span class="p">}))</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_all\_notes [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleKeepReader.load_all_notes "Permanent link")

```
load_all_notes() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load all notes from Google Keep.

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/keep/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_all_notes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load all notes from Google Keep."""</span>
    <span class="n">keep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_keep</span><span class="p">()</span>

    <span class="n">notes</span> <span class="o">=</span> <span class="n">keep</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">note</span> <span class="ow">in</span> <span class="n">notes</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Title: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="s2">Content: </span><span class="si">{</span><span class="n">note</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"note_id"</span><span class="p">:</span> <span class="n">note</span><span class="o">.</span><span class="n">id</span><span class="p">}))</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

GoogleMapsTextSearchReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleMapsTextSearchReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/maps/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 34</span>
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
<span class="normal">140</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleMapsTextSearchReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"GOOGLE_MAPS_API_KEY"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"API key must be provided or set in the environment variables as 'GOOGLE_MAPS_API_KEY'"</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_NUMBER_OF_RESULTS</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Google Maps.</span>

<span class="sd">        Args:</span>
<span class="sd">            text (str): the text to search for.</span>
<span class="sd">            number_of_results (Optional[int]): the number of results to return. Defaults to 20.</span>
<span class="sd">        """</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_text_request</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">MAX_RESULTS_PER_PAGE</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="s2">"nextPageToken"</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">next_page_token</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"nextPageToken"</span><span class="p">]</span>
            <span class="n">places</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"places"</span><span class="p">,</span> <span class="p">[])</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">places</span><span class="p">)</span> <span class="o"></span> <span class="n">number_of_results</span><span class="p">:</span>
                    <span class="k">return</span> <span class="n">documents</span>

                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">place</span><span class="o">.</span><span class="n">dict</span><span class="p">()))</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_text_request</span><span class="p">(</span>
                <span class="n">text</span><span class="p">,</span> <span class="n">MAX_RESULTS_PER_PAGE</span><span class="p">,</span> <span class="n">next_page_token</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data lazily from Google Maps."""</span>
        <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_search_text_request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">number_of_results</span><span class="p">,</span> <span class="n">next_page_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Send a request to the Google Maps Places API to search for text.</span>

<span class="sd">        Args:</span>
<span class="sd">            text (str): the text to search for.</span>
<span class="sd">            number_of_results (int): the number of results to return.</span>
<span class="sd">            next_page_token (Optional[str]): the next page token to get the next page of results.</span>
<span class="sd">        """</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"X-Goog-Api-Key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="s2">"X-Goog-FieldMask"</span><span class="p">:</span> <span class="n">FIELD_MASK</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"textQuery"</span><span class="p">:</span> <span class="n">text</span><span class="p">,</span>
                <span class="s2">"pageSize"</span><span class="p">:</span> <span class="n">number_of_results</span><span class="p">,</span>
                <span class="s2">"pageToken"</span><span class="p">:</span> <span class="n">next_page_token</span><span class="p">,</span>
            <span class="p">}</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">SEARCH_TEXT_BASE_URL</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">payload</span><span class="p">)</span>
        <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleMapsTextSearchReader.load_data "Permanent link")

```
load_data(text: str, number_of_results: Optional[int] = DEFAULT_NUMBER_OF_RESULTS) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Google Maps.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text` | `str` | 
the text to search for.



 | _required_ |
| `number_of_results` | `Optional[int]` | 

the number of results to return. Defaults to 20.



 | `DEFAULT_NUMBER_OF_RESULTS` |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/maps/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 45</span>
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
<span class="normal">109</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_NUMBER_OF_RESULTS</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Google Maps.</span>

<span class="sd">    Args:</span>
<span class="sd">        text (str): the text to search for.</span>
<span class="sd">        number_of_results (Optional[int]): the number of results to return. Defaults to 20.</span>
<span class="sd">    """</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_text_request</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">MAX_RESULTS_PER_PAGE</span><span class="p">)</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="s2">"nextPageToken"</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="n">next_page_token</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"nextPageToken"</span><span class="p">]</span>
        <span class="n">places</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"places"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">places</span><span class="p">)</span> <span class="o"></span> <span class="n">number_of_results</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">documents</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">document_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">place</span><span class="o">.</span><span class="n">dict</span><span class="p">()))</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_search_text_request</span><span class="p">(</span>
            <span class="n">text</span><span class="p">,</span> <span class="n">MAX_RESULTS_PER_PAGE</span><span class="p">,</span> <span class="n">next_page_token</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### lazy\_load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleMapsTextSearchReader.lazy_load_data "Permanent link")

```
lazy_load_data(*args: Any, **load_kwargs: Any) -> Iterable[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data lazily from Google Maps.

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/maps/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">lazy_load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data lazily from Google Maps."""</span>
    <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">load_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

GoogleSheetsReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleSheetsReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Google Sheets reader.

Reads a sheet as TSV from Google Sheets

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/sheets/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 35</span>
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
<span class="normal">197</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleSheetsReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google Sheets reader.</span>

<span class="sd">    Reads a sheet as TSV from Google Sheets</span>

<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">google</span>  <span class="c1"># noqa</span>
            <span class="kn">import</span> <span class="nn">google_auth_oauthlib</span>  <span class="c1"># noqa</span>
            <span class="kn">import</span> <span class="nn">googleapiclient</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`google_auth_oauthlib`, `googleapiclient` and `google` "</span>
                <span class="s2">"must be installed to use the GoogleSheetsReader.</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"Please run `pip install --upgrade google-api-python-client "</span>
                <span class="s2">"google-auth-httplib2 google-auth-oauthlib`."</span>
            <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"GoogleSheetsReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            spreadsheet_ids (List[str]): a list of document ids.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">spreadsheet_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "spreadsheet_ids" in `load_kwargs`.'</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">spreadsheet_id</span> <span class="ow">in</span> <span class="n">spreadsheet_ids</span><span class="p">:</span>
            <span class="n">sheet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sheet</span><span class="p">(</span><span class="n">spreadsheet_id</span><span class="p">)</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">sheet</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"spreadsheet_id"</span><span class="p">:</span> <span class="n">spreadsheet_id</span><span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">load_data_in_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            spreadsheet_ids (List[str]): a list of document ids.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">spreadsheet_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "spreadsheet_ids" in `load_kwargs`.'</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">spreadsheet_id</span> <span class="ow">in</span> <span class="n">spreadsheet_ids</span><span class="p">:</span>
            <span class="n">dataframes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sheet_in_pandas</span><span class="p">(</span><span class="n">spreadsheet_id</span><span class="p">)</span>
            <span class="n">results</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">dataframes</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_load_sheet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a sheet from Google Sheets.</span>

<span class="sd">        Args:</span>
<span class="sd">            spreadsheet_id: the sheet id.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The sheet data.</span>
<span class="sd">        """</span>
        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">sheets_service</span> <span class="o">=</span> <span class="n">discovery</span><span class="o">.</span><span class="n">build</span><span class="p">(</span><span class="s2">"sheets"</span><span class="p">,</span> <span class="s2">"v4"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>
        <span class="n">spreadsheet_data</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sheets_service</span><span class="o">.</span><span class="n">spreadsheets</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">spreadsheetId</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="p">)</span>
        <span class="n">sheets</span> <span class="o">=</span> <span class="n">spreadsheet_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"sheets"</span><span class="p">)</span>
        <span class="n">sheet_text</span> <span class="o">=</span> <span class="s2">""</span>

        <span class="k">for</span> <span class="n">sheet</span> <span class="ow">in</span> <span class="n">sheets</span><span class="p">:</span>
            <span class="n">properties</span> <span class="o">=</span> <span class="n">sheet</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"properties"</span><span class="p">)</span>
            <span class="n">title</span> <span class="o">=</span> <span class="n">properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"title"</span><span class="p">)</span>
            <span class="n">sheet_text</span> <span class="o">+=</span> <span class="n">title</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">grid_props</span> <span class="o">=</span> <span class="n">properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gridProperties"</span><span class="p">)</span>
            <span class="n">rows</span> <span class="o">=</span> <span class="n">grid_props</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"rowCount"</span><span class="p">)</span>
            <span class="n">cols</span> <span class="o">=</span> <span class="n">grid_props</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"columnCount"</span><span class="p">)</span>
            <span class="n">range_pattern</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"R1C1:R</span><span class="si">{</span><span class="n">rows</span><span class="si">}</span><span class="s2">C</span><span class="si">{</span><span class="n">cols</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">response</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">sheets_service</span><span class="o">.</span><span class="n">spreadsheets</span><span class="p">()</span>
                <span class="o">.</span><span class="n">values</span><span class="p">()</span>
                <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">spreadsheetId</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">,</span> <span class="nb">range</span><span class="o">=</span><span class="n">range_pattern</span><span class="p">)</span>
                <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
            <span class="p">)</span>
            <span class="n">sheet_text</span> <span class="o">+=</span> <span class="p">(</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">"</span><span class="se">\t</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">)</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">,</span> <span class="p">[]))</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">sheet_text</span>

    <span class="k">def</span> <span class="nf">_load_sheet_in_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load a sheet from Google Sheets.</span>

<span class="sd">        Args:</span>
<span class="sd">            spreadsheet_id: the sheet id.</span>
<span class="sd">            sheet_name: the sheet name.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The sheet data.</span>
<span class="sd">        """</span>
        <span class="n">credentials</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_credentials</span><span class="p">()</span>
        <span class="n">sheets_service</span> <span class="o">=</span> <span class="n">discovery</span><span class="o">.</span><span class="n">build</span><span class="p">(</span><span class="s2">"sheets"</span><span class="p">,</span> <span class="s2">"v4"</span><span class="p">,</span> <span class="n">credentials</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>
        <span class="n">sheet</span> <span class="o">=</span> <span class="n">sheets_service</span><span class="o">.</span><span class="n">spreadsheets</span><span class="p">()</span>
        <span class="n">spreadsheet_data</span> <span class="o">=</span> <span class="n">sheet</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">spreadsheetId</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="n">sheets</span> <span class="o">=</span> <span class="n">spreadsheet_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"sheets"</span><span class="p">)</span>
        <span class="n">dataframes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">sheet</span> <span class="ow">in</span> <span class="n">sheets</span><span class="p">:</span>
            <span class="n">properties</span> <span class="o">=</span> <span class="n">sheet</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"properties"</span><span class="p">)</span>
            <span class="n">title</span> <span class="o">=</span> <span class="n">properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"title"</span><span class="p">)</span>
            <span class="n">grid_props</span> <span class="o">=</span> <span class="n">properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"gridProperties"</span><span class="p">)</span>
            <span class="n">rows</span> <span class="o">=</span> <span class="n">grid_props</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"rowCount"</span><span class="p">)</span>
            <span class="n">cols</span> <span class="o">=</span> <span class="n">grid_props</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"columnCount"</span><span class="p">)</span>
            <span class="n">range_pattern</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">title</span><span class="si">}</span><span class="s2">!R1C1:R</span><span class="si">{</span><span class="n">rows</span><span class="si">}</span><span class="s2">C</span><span class="si">{</span><span class="n">cols</span><span class="si">}</span><span class="s2">"</span>
            <span class="n">response</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">sheets_service</span><span class="o">.</span><span class="n">spreadsheets</span><span class="p">()</span>
                <span class="o">.</span><span class="n">values</span><span class="p">()</span>
                <span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">spreadsheetId</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">,</span> <span class="nb">range</span><span class="o">=</span><span class="n">range_pattern</span><span class="p">)</span>
                <span class="o">.</span><span class="n">execute</span><span class="p">()</span>
            <span class="p">)</span>
            <span class="n">values</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">,</span> <span class="p">[])</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">values</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"No data found in </span><span class="si">{</span><span class="n">title</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">values</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">columns</span><span class="o">=</span><span class="n">values</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                <span class="n">dataframes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">dataframes</span>

    <span class="k">def</span> <span class="nf">_get_credentials</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get valid user credentials from storage.</span>

<span class="sd">        The file token.json stores the user's access and refresh tokens, and is</span>
<span class="sd">        created automatically when the authorization flow completes for the first</span>
<span class="sd">        time.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Credentials, the obtained credential.</span>
<span class="sd">        """</span>
        <span class="n">creds</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">):</span>
            <span class="n">creds</span> <span class="o">=</span> <span class="n">Credentials</span><span class="o">.</span><span class="n">from_authorized_user_file</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="n">SCOPES</span><span class="p">)</span>
        <span class="c1"># If there are no (valid) credentials available, let the user log in.</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">creds</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">creds</span><span class="o">.</span><span class="n">valid</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">creds</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">expired</span> <span class="ow">and</span> <span class="n">creds</span><span class="o">.</span><span class="n">refresh_token</span><span class="p">:</span>
                <span class="n">creds</span><span class="o">.</span><span class="n">refresh</span><span class="p">(</span><span class="n">Request</span><span class="p">())</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">flow</span> <span class="o">=</span> <span class="n">InstalledAppFlow</span><span class="o">.</span><span class="n">from_client_secrets_file</span><span class="p">(</span>
                    <span class="s2">"credentials.json"</span><span class="p">,</span> <span class="n">SCOPES</span>
                <span class="p">)</span>
                <span class="n">creds</span> <span class="o">=</span> <span class="n">flow</span><span class="o">.</span><span class="n">run_local_server</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
            <span class="c1"># Save the credentials for the next run</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"token.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">token</span><span class="p">:</span>
                <span class="n">token</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">creds</span><span class="o">.</span><span class="n">to_json</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">creds</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleSheetsReader.load_data "Permanent link")

```
load_data(spreadsheet_ids: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `spreadsheet_ids` | `List[str]` | 
a list of document ids.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/sheets/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
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
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        spreadsheet_ids (List[str]): a list of document ids.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">spreadsheet_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "spreadsheet_ids" in `load_kwargs`.'</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">spreadsheet_id</span> <span class="ow">in</span> <span class="n">spreadsheet_ids</span><span class="p">:</span>
        <span class="n">sheet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sheet</span><span class="p">(</span><span class="n">spreadsheet_id</span><span class="p">)</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">spreadsheet_id</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">sheet</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="s2">"spreadsheet_id"</span><span class="p">:</span> <span class="n">spreadsheet_id</span><span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data\_in\_pandas [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/#llama_index.readers.google.GoogleSheetsReader.load_data_in_pandas "Permanent link")

```
load_data_in_pandas(spreadsheet_ids: List[str]) -> List[DataFrame]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `spreadsheet_ids` | `List[str]` | 
a list of document ids.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/sheets/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data_in_pandas</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spreadsheet_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        spreadsheet_ids (List[str]): a list of document ids.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">spreadsheet_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Must specify a "spreadsheet_ids" in `load_kwargs`.'</span><span class="p">)</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">spreadsheet_id</span> <span class="ow">in</span> <span class="n">spreadsheet_ids</span><span class="p">:</span>
        <span class="n">dataframes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_sheet_in_pandas</span><span class="p">(</span><span class="n">spreadsheet_id</span><span class="p">)</span>
        <span class="n">results</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">dataframes</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Github](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/)[Next Gpt repo](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/)
