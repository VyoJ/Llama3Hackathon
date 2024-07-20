Title: Github - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/github/

Markdown Content:
Github - LlamaIndex


GitHubRepositoryCollaboratorsReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/#llama_index.readers.github.GitHubRepositoryCollaboratorsReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

GitHub repository collaborators reader.

Retrieves the list of collaborators of a GitHub repository and returns a list of documents.

**Examples:**

```
>>> reader = GitHubRepositoryCollaboratorsReader("owner", "repo")
>>> colabs = reader.load_data()
>>> print(colabs)
```

Source code in `llama-index-integrations/readers/llama-index-readers-github/llama_index/readers/github/collaborators/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
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
<span class="normal">165</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GitHubRepositoryCollaboratorsReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    GitHub repository collaborators reader.</span>

<span class="sd">    Retrieves the list of collaborators of a GitHub repository and returns a list of documents.</span>

<span class="sd">    Examples:</span>
<span class="sd">        &gt;&gt;&gt; reader = GitHubRepositoryCollaboratorsReader("owner", "repo")</span>
<span class="sd">        &gt;&gt;&gt; colabs = reader.load_data()</span>
<span class="sd">        &gt;&gt;&gt; print(colabs)</span>

<span class="sd">    """</span>

    <span class="k">class</span> <span class="nc">FilterType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Filter type.</span>

<span class="sd">        Used to determine whether the filter is inclusive or exclusive.</span>
<span class="sd">        """</span>

        <span class="n">EXCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>
        <span class="n">INCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">github_client</span><span class="p">:</span> <span class="n">BaseGitHubCollaboratorsClient</span><span class="p">,</span>
        <span class="n">owner</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">repo</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize params.</span>

<span class="sd">        Args:</span>
<span class="sd">            - github_client (BaseGitHubCollaboratorsClient): GitHub client.</span>
<span class="sd">            - owner (str): Owner of the repository.</span>
<span class="sd">            - repo (str): Name of the repository.</span>
<span class="sd">            - verbose (bool): Whether to print verbose messages.</span>

<span class="sd">        Raises:</span>
<span class="sd">            - `ValueError`: If the github_token is not provided and</span>
<span class="sd">                the GITHUB_TOKEN environment variable is not set.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span> <span class="o">=</span> <span class="n">owner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span> <span class="o">=</span> <span class="n">repo</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="c1"># Set up the event loop</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_running_loop</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span><span class="p">:</span>
            <span class="c1"># If there is no running loop, create a new one</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span> <span class="o">=</span> <span class="n">github_client</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        GitHub repository collaborators reader.</span>

<span class="sd">        Retrieves the list of collaborators in a GitHub repository and converts them to documents.</span>

<span class="sd">        Each collaborator is converted to a document by doing the following:</span>

<span class="sd">            - The text of the document is the login.</span>
<span class="sd">            - The title of the document is also the login.</span>
<span class="sd">            - The extra_info of the document is a dictionary with the following keys:</span>
<span class="sd">                - login: str, the login of the user</span>
<span class="sd">                - type: str, the type of user e.g. "User"</span>
<span class="sd">                - site_admin: bool, whether the user has admin permissions</span>
<span class="sd">                - role_name: str, e.g. "admin"</span>
<span class="sd">                - name: str, the name of the user, if available</span>
<span class="sd">                - email: str, the email of the user, if available</span>
<span class="sd">                - permissions: str, the permissions of the user, if available</span>


<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">page</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="c1"># Loop until there are no more collaborators</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">collaborators</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="o">.</span><span class="n">get_collaborators</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="n">page</span><span class="o">=</span><span class="n">page</span>
                <span class="p">)</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">collaborators</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="s2">"No more collaborators found, stopping"</span><span class="p">)</span>

            <span class="k">break</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"Found </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">collaborators</span><span class="p">)</span><span class="si">}</span><span class="s2"> collaborators in the repo page </span><span class="si">{</span><span class="n">page</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">page</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">collab</span> <span class="ow">in</span> <span class="n">collaborators</span><span class="p">:</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"login"</span><span class="p">:</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"login"</span><span class="p">],</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                <span class="s2">"site_admin"</span><span class="p">:</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"site_admin"</span><span class="p">],</span>
                <span class="s2">"role_name"</span><span class="p">:</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"role_name"</span><span class="p">],</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="n">collab</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="o">=</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">collab</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"email"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"email"</span><span class="p">]</span> <span class="o">=</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"email"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">collab</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"permissions"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"permissions"</span><span class="p">]</span> <span class="o">=</span> <span class="n">collab</span><span class="p">[</span><span class="s2">"permissions"</span><span class="p">]</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">doc_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">collab</span><span class="p">[</span><span class="s2">"login"</span><span class="p">]),</span>
                <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">collab</span><span class="p">[</span><span class="s2">"login"</span><span class="p">]),</span>  <span class="c1"># unsure for this</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"Resulted in </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2"> documents"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

GitHubRepositoryIssuesReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/#llama_index.readers.github.GitHubRepositoryIssuesReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

GitHub repository issues reader.

Retrieves the list of issues of a GitHub repository and returns a list of documents.

**Examples:**

```
>>> reader = GitHubRepositoryIssuesReader("owner", "repo")
>>> issues = reader.load_data()
>>> print(issues)
```

Source code in `llama-index-integrations/readers/llama-index-readers-github/llama_index/readers/github/issues/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 43</span>
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
<span class="normal">211</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GitHubRepositoryIssuesReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    GitHub repository issues reader.</span>

<span class="sd">    Retrieves the list of issues of a GitHub repository and returns a list of documents.</span>

<span class="sd">    Examples:</span>
<span class="sd">        &gt;&gt;&gt; reader = GitHubRepositoryIssuesReader("owner", "repo")</span>
<span class="sd">        &gt;&gt;&gt; issues = reader.load_data()</span>
<span class="sd">        &gt;&gt;&gt; print(issues)</span>

<span class="sd">    """</span>

    <span class="k">class</span> <span class="nc">IssueState</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Issue type.</span>

<span class="sd">        Used to decide what issues to retrieve.</span>

<span class="sd">        Attributes:</span>
<span class="sd">            - OPEN: Just open issues. This is the default.</span>
<span class="sd">            - CLOSED: Just closed issues.</span>
<span class="sd">            - ALL: All issues, open and closed.</span>
<span class="sd">        """</span>

        <span class="n">OPEN</span> <span class="o">=</span> <span class="s2">"open"</span>
        <span class="n">CLOSED</span> <span class="o">=</span> <span class="s2">"closed"</span>
        <span class="n">ALL</span> <span class="o">=</span> <span class="s2">"all"</span>

    <span class="k">class</span> <span class="nc">FilterType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Filter type.</span>

<span class="sd">        Used to determine whether the filter is inclusive or exclusive.</span>
<span class="sd">        """</span>

        <span class="n">EXCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>
        <span class="n">INCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">github_client</span><span class="p">:</span> <span class="n">BaseGitHubIssuesClient</span><span class="p">,</span>
        <span class="n">owner</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">repo</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize params.</span>

<span class="sd">        Args:</span>
<span class="sd">            - github_client (BaseGitHubIssuesClient): GitHub client.</span>
<span class="sd">            - owner (str): Owner of the repository.</span>
<span class="sd">            - repo (str): Name of the repository.</span>
<span class="sd">            - verbose (bool): Whether to print verbose messages.</span>

<span class="sd">        Raises:</span>
<span class="sd">            - `ValueError`: If the github_token is not provided and</span>
<span class="sd">                the GITHUB_TOKEN environment variable is not set.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span> <span class="o">=</span> <span class="n">owner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span> <span class="o">=</span> <span class="n">repo</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="c1"># Set up the event loop</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_running_loop</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span><span class="p">:</span>
            <span class="c1"># If there is no running loop, create a new one</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span> <span class="o">=</span> <span class="n">github_client</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IssueState</span><span class="p">]</span> <span class="o">=</span> <span class="n">IssueState</span><span class="o">.</span><span class="n">OPEN</span><span class="p">,</span>
        <span class="n">labelFilters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">FilterType</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load issues from a repository and converts them to documents.</span>

<span class="sd">        Each issue is converted to a document by doing the following:</span>

<span class="sd">        - The text of the document is the concatenation of the title and the body of the issue.</span>
<span class="sd">        - The title of the document is the title of the issue.</span>
<span class="sd">        - The doc_id of the document is the issue number.</span>
<span class="sd">        - The extra_info of the document is a dictionary with the following keys:</span>
<span class="sd">            - state: State of the issue.</span>
<span class="sd">            - created_at: Date when the issue was created.</span>
<span class="sd">            - closed_at: Date when the issue was closed. Only present if the issue is closed.</span>
<span class="sd">            - url: URL of the issue.</span>
<span class="sd">            - assignee: Login of the user assigned to the issue. Only present if the issue is assigned.</span>
<span class="sd">        - The embedding of the document is None.</span>
<span class="sd">        - The doc_hash of the document is None.</span>

<span class="sd">        Args:</span>
<span class="sd">            - state (IssueState): State of the issues to retrieve. Default is IssueState.OPEN.</span>
<span class="sd">            - labelFilters: an optional list of filters to apply to the issue list based on labels.</span>

<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">page</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="c1"># Loop until there are no more issues</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">issues</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="o">.</span><span class="n">get_issues</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">page</span><span class="o">=</span><span class="n">page</span>
                <span class="p">)</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">issues</span><span class="p">)</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">FilterType</span><span class="o">.</span><span class="n">INCLUDE</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">labels</span>
            <span class="k">elif</span> <span class="n">filterType</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="s2">"No more issues found, stopping"</span><span class="p">)</span>

            <span class="k">break</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"Found </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">issues</span><span class="p">)</span><span class="si">}</span><span class="s2"> issues in the repo page </span><span class="si">{</span><span class="n">page</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="n">page</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">filterCount</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">issue</span> <span class="ow">in</span> <span class="n">issues</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_must_include</span><span class="p">(</span><span class="n">labelFilters</span><span class="p">,</span> <span class="n">issue</span><span class="p">):</span>
                <span class="n">filterCount</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">continue</span>
            <span class="n">title</span> <span class="o">=</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"body"</span><span class="p">]</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">doc_id</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">issue</span><span class="p">[</span><span class="s2">"number"</span><span class="p">]),</span>
                <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">title</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">body</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"state"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"state"</span><span class="p">],</span>
                <span class="s2">"created_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"created_at"</span><span class="p">],</span>
                <span class="c1"># url is the API URL</span>
                <span class="s2">"url"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                <span class="c1"># source is the HTML URL, more convenient for humans</span>
                <span class="s2">"source"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"html_url"</span><span class="p">],</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"closed_at"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"closed_at"</span><span class="p">]</span> <span class="o">=</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"closed_at"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"assignee"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"assignee"</span><span class="p">]</span> <span class="o">=</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"assignee"</span><span class="p">][</span><span class="s2">"login"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">extra_info</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">label</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]]</span>
            <span class="n">document</span><span class="o">.</span><span class="n">extra_info</span> <span class="o">=</span> <span class="n">extra_info</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"Resulted in </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span><span class="si">}</span><span class="s2"> documents"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">labelFilters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"Filtered out </span><span class="si">{</span><span class="n">filterCount</span><span class="si">}</span><span class="s2"> issues"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

GithubRepositoryReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/#llama_index.readers.github.GithubRepositoryReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Github repository reader.

Retrieves the contents of a Github repository and returns a list of documents. The documents are either the contents of the files in the repository or the text extracted from the files using the parser.

**Examples:**

```
>>> client = github_client = GithubClient(
...    github_token=os.environ["GITHUB_TOKEN"],
...    verbose=True
... )
>>> reader = GithubRepositoryReader(
...    github_client=github_client,
...    owner="run-llama",
...    repo="llama_index",
... )
>>> branch_documents = reader.load_data(branch="branch")
>>> commit_documents = reader.load_data(commit_sha="commit_sha")
```

Source code in `llama-index-integrations/readers/llama-index-readers-github/llama_index/readers/github/repository/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
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
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
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
<span class="normal">541</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GithubRepositoryReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Github repository reader.</span>

<span class="sd">    Retrieves the contents of a Github repository and returns a list of documents.</span>
<span class="sd">    The documents are either the contents of the files in the repository or the text</span>
<span class="sd">    extracted from the files using the parser.</span>

<span class="sd">    Examples:</span>
<span class="sd">        &gt;&gt;&gt; client = github_client = GithubClient(</span>
<span class="sd">        ...    github_token=os.environ["GITHUB_TOKEN"],</span>
<span class="sd">        ...    verbose=True</span>
<span class="sd">        ... )</span>
<span class="sd">        &gt;&gt;&gt; reader = GithubRepositoryReader(</span>
<span class="sd">        ...    github_client=github_client,</span>
<span class="sd">        ...    owner="run-llama",</span>
<span class="sd">        ...    repo="llama_index",</span>
<span class="sd">        ... )</span>
<span class="sd">        &gt;&gt;&gt; branch_documents = reader.load_data(branch="branch")</span>
<span class="sd">        &gt;&gt;&gt; commit_documents = reader.load_data(commit_sha="commit_sha")</span>

<span class="sd">    """</span>

    <span class="k">class</span> <span class="nc">FilterType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Filter type.</span>

<span class="sd">        Used to determine whether the filter is inclusive or exclusive.</span>

<span class="sd">        Attributes:</span>
<span class="sd">            - EXCLUDE: Exclude the files in the directories or with the extensions.</span>
<span class="sd">            - INCLUDE: Include only the files in the directories or with the extensions.</span>
<span class="sd">        """</span>

        <span class="n">EXCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>
        <span class="n">INCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">github_client</span><span class="p">:</span> <span class="n">BaseGithubClient</span><span class="p">,</span>
        <span class="n">owner</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">repo</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">use_parser</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">concurrent_requests</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">filter_directories</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">FilterType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filter_file_extensions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">FilterType</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize params.</span>

<span class="sd">        Args:</span>
<span class="sd">            - github_client (BaseGithubClient): Github client.</span>
<span class="sd">            - owner (str): Owner of the repository.</span>
<span class="sd">            - repo (str): Name of the repository.</span>
<span class="sd">            - use_parser (bool): Whether to use the parser to extract</span>
<span class="sd">                the text from the files.</span>
<span class="sd">            - verbose (bool): Whether to print verbose messages.</span>
<span class="sd">            - concurrent_requests (int): Number of concurrent requests to</span>
<span class="sd">                make to the Github API.</span>
<span class="sd">            - timeout (int or None): Timeout for the requests to the Github API. Default is 5.</span>
<span class="sd">            - retries (int): Number of retries for requests made to the Github API. Default is 0.</span>
<span class="sd">            - filter_directories (Optional[Tuple[List[str], FilterType]]): Tuple</span>
<span class="sd">                containing a list of directories and a FilterType. If the FilterType</span>
<span class="sd">                is INCLUDE, only the files in the directories in the list will be</span>
<span class="sd">                included. If the FilterType is EXCLUDE, the files in the directories</span>
<span class="sd">                in the list will be excluded.</span>
<span class="sd">            - filter_file_extensions (Optional[Tuple[List[str], FilterType]]): Tuple</span>
<span class="sd">                containing a list of file extensions and a FilterType. If the</span>
<span class="sd">                FilterType is INCLUDE, only the files with the extensions in the list</span>
<span class="sd">                will be included. If the FilterType is EXCLUDE, the files with the</span>
<span class="sd">                extensions in the list will be excluded.</span>

<span class="sd">        Raises:</span>
<span class="sd">            - `ValueError`: If the github_token is not provided and</span>
<span class="sd">                the GITHUB_TOKEN environment variable is not set.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span> <span class="o">=</span> <span class="n">owner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span> <span class="o">=</span> <span class="n">repo</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_use_parser</span> <span class="o">=</span> <span class="n">use_parser</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concurrent_requests</span> <span class="o">=</span> <span class="n">concurrent_requests</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span> <span class="o">=</span> <span class="n">timeout</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_retries</span> <span class="o">=</span> <span class="n">retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_filter_directories</span> <span class="o">=</span> <span class="n">filter_directories</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_filter_file_extensions</span> <span class="o">=</span> <span class="n">filter_file_extensions</span>

        <span class="c1"># Set up the event loop</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_running_loop</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">RuntimeError</span><span class="p">:</span>
            <span class="c1"># If there is no running loop, create a new one</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span> <span class="o">=</span> <span class="n">github_client</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_file_readers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_supported_suffix</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">DEFAULT_FILE_READER_CLS</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">_check_filter_directories</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tree_obj_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Check if a tree object should be allowed based on the directories.</span>

<span class="sd">        :param `tree_obj_path`: path of the tree object i.e. 'llama_index/readers'</span>

<span class="sd">        :return: True if the tree object should be allowed, False otherwise</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_directories</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">True</span>
        <span class="n">filter_directories</span><span class="p">,</span> <span class="n">filter_type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_directories</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"Checking </span><span class="si">{</span><span class="n">tree_obj_path</span><span class="si">}</span><span class="s2"> whether to </span><span class="si">{</span><span class="n">filter_type</span><span class="si">}</span><span class="s2"> it"</span>
            <span class="o">+</span> <span class="sa">f</span><span class="s2">" based on the filter directories: </span><span class="si">{</span><span class="n">filter_directories</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">filter_type</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">FilterType</span><span class="o">.</span><span class="n">INCLUDE</span><span class="p">:</span>
            <span class="n">print_if_verbose</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                <span class="sa">f</span><span class="s2">"Checking if </span><span class="si">{</span><span class="n">tree_obj_path</span><span class="si">}</span><span class="s2"> is a subdirectory of any of the filter"</span>
                <span class="s2">" directories"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="nb">any</span><span class="p">(</span>
                <span class="n">tree_obj_path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>
                <span class="ow">or</span> <span class="n">directory</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">tree_obj_path</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">directory</span> <span class="ow">in</span> <span class="n">filter_directories</span>
            <span class="p">)</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Unknown filter type: </span><span class="si">{</span><span class="n">filter_type</span><span class="si">}</span><span class="s2">. "</span>
            <span class="s2">"Please use either 'INCLUDE' or 'EXCLUDE'."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_check_filter_file_extensions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tree_obj_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Check if a tree object should be allowed based on the file extensions.</span>

<span class="sd">        :param `tree_obj_path`: path of the tree object i.e. 'llama_index/indices'</span>

<span class="sd">        :return: True if the tree object should be allowed, False otherwise</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_file_extensions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">True</span>
        <span class="n">filter_file_extensions</span><span class="p">,</span> <span class="n">filter_type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_file_extensions</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"Checking </span><span class="si">{</span><span class="n">tree_obj_path</span><span class="si">}</span><span class="s2"> whether to </span><span class="si">{</span><span class="n">filter_type</span><span class="si">}</span><span class="s2"> it"</span>
            <span class="o">+</span> <span class="sa">f</span><span class="s2">" based on the filter file extensions: </span><span class="si">{</span><span class="n">filter_file_extensions</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">filter_type</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">FilterType</span><span class="o">.</span><span class="n">INCLUDE</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">get_file_extension</span><span class="p">(</span><span class="n">tree_obj_path</span><span class="p">)</span> <span class="ow">in</span> <span class="n">filter_file_extensions</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Unknown filter type: </span><span class="si">{</span><span class="n">filter_type</span><span class="si">}</span><span class="s2">. "</span>
            <span class="s2">"Please use either 'INCLUDE' or 'EXCLUDE'."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_allow_tree_obj</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tree_obj_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">tree_obj_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Check if a tree object should be allowed.</span>

<span class="sd">        :param `tree_obj_path`: path of the tree object</span>

<span class="sd">        :return: True if the tree object should be allowed, False otherwise</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_directories</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">tree_obj_type</span> <span class="o"></span> <span class="s2">"blob"</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_check_filter_directories</span><span class="p">(</span>
                <span class="n">tree_obj_path</span>
            <span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_check_filter_file_extensions</span><span class="p">(</span><span class="n">tree_obj_path</span><span class="p">)</span>

        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_load_data_from_commit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">commit_sha</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from a commit.</span>

<span class="sd">        Loads github repository data from a specific commit sha.</span>

<span class="sd">        :param `commit`: commit sha</span>

<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="n">commit_response</span><span class="p">:</span> <span class="n">GitCommitResponseModel</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="o">.</span><span class="n">get_commit</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="n">commit_sha</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">tree_sha</span> <span class="o">=</span> <span class="n">commit_response</span><span class="o">.</span><span class="n">commit</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">sha</span>
        <span class="n">blobs_and_paths</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_recurse_tree</span><span class="p">(</span><span class="n">tree_sha</span><span class="p">))</span>

        <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">blobs_and_paths</span><span class="p">)</span><span class="si">}</span><span class="s2"> blobs"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_generate_documents</span><span class="p">(</span><span class="n">blobs_and_paths</span><span class="o">=</span><span class="n">blobs_and_paths</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">commit_sha</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_load_data_from_branch</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">branch</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from a branch.</span>

<span class="sd">        Loads github repository data from a specific branch.</span>

<span class="sd">        :param `branch`: branch name</span>

<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="n">branch_data</span><span class="p">:</span> <span class="n">GitBranchResponseModel</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="o">.</span><span class="n">get_branch</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="n">branch</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="n">tree_sha</span> <span class="o">=</span> <span class="n">branch_data</span><span class="o">.</span><span class="n">commit</span><span class="o">.</span><span class="n">commit</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">sha</span>
        <span class="n">blobs_and_paths</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_recurse_tree</span><span class="p">(</span><span class="n">tree_sha</span><span class="p">))</span>

        <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">blobs_and_paths</span><span class="p">)</span><span class="si">}</span><span class="s2"> blobs"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_generate_documents</span><span class="p">(</span><span class="n">blobs_and_paths</span><span class="o">=</span><span class="n">blobs_and_paths</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">branch</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">commit_sha</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">branch</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load data from a commit or a branch.</span>

<span class="sd">        Loads github repository data from a specific commit sha or a branch.</span>

<span class="sd">        :param `commit`: commit sha</span>
<span class="sd">        :param `branch`: branch name</span>

<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">branch</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You can only specify one of commit or branch."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">branch</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must specify one of commit or branch."</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_from_commit</span><span class="p">(</span><span class="n">commit_sha</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">branch</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_from_branch</span><span class="p">(</span><span class="n">branch</span><span class="p">)</span>

        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must specify one of commit or branch."</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_recurse_tree</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tree_sha</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">current_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">current_depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">max_depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Recursively get all blob tree objects in a tree.</span>

<span class="sd">        And construct their full path relative to the root of the repository.</span>
<span class="sd">        (see GitTreeResponseModel.GitTreeObject in</span>
<span class="sd">            github_api_client.py for more information)</span>

<span class="sd">        :param `tree_sha`: sha of the tree to recurse</span>
<span class="sd">        :param `current_path`: current path of the tree</span>
<span class="sd">        :param `current_depth`: current depth of the tree</span>
<span class="sd">        :return: list of tuples of</span>
<span class="sd">            (tree object, file's full path relative to the root of the repo)</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">max_depth</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span> <span class="ow">and</span> <span class="n">current_depth</span> <span class="o">&gt;</span> <span class="n">max_depth</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="n">blobs_and_full_paths</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">GitTreeResponseModel</span><span class="o">.</span><span class="n">GitTreeObject</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"current path: </span><span class="si">{</span><span class="n">current_path</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">tree_data</span><span class="p">:</span> <span class="n">GitTreeResponseModel</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="o">.</span><span class="n">get_tree</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="n">tree_sha</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_timeout</span>
        <span class="p">)</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"tree data: </span><span class="si">{</span><span class="n">tree_data</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"processing tree </span><span class="si">{</span><span class="n">tree_sha</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">tree_obj</span> <span class="ow">in</span> <span class="n">tree_data</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span>
            <span class="n">file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">tree_obj</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_allow_tree_obj</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">tree_obj</span><span class="o">.</span><span class="n">type</span><span class="p">):</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                    <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"ignoring </span><span class="si">{</span><span class="n">tree_obj</span><span class="o">.</span><span class="n">path</span><span class="si">}</span><span class="s2"> due to filter"</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">continue</span>

            <span class="n">print_if_verbose</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"tree object: </span><span class="si">{</span><span class="n">tree_obj</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="n">tree_obj</span><span class="o">.</span><span class="n">type</span> <span class="o"></span> <span class="s2">"blob"</span><span class="p">:</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                    <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"found blob </span><span class="si">{</span><span class="n">tree_obj</span><span class="o">.</span><span class="n">path</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="n">blobs_and_full_paths</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">tree_obj</span><span class="p">,</span> <span class="n">file_path</span><span class="p">))</span>

            <span class="n">print_if_verbose</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">current_depth</span> <span class="o">+</span> <span class="sa">f</span><span class="s2">"blob and full paths: </span><span class="si">{</span><span class="n">blobs_and_full_paths</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">blobs_and_full_paths</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_generate_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">blobs_and_paths</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">GitTreeResponseModel</span><span class="o">.</span><span class="n">GitTreeObject</span><span class="p">,</span> <span class="nb">str</span><span class="p">]],</span>
        <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Generate documents from a list of blobs and their full paths.</span>

<span class="sd">        :param `blobs_and_paths`: list of tuples of</span>
<span class="sd">            (tree object, file's full path in the repo relative to the root of the repo)</span>
<span class="sd">        :param `id`: the branch name or commit sha used when loading the repo</span>
<span class="sd">        :return: list of documents</span>
<span class="sd">        """</span>
        <span class="n">buffered_iterator</span> <span class="o">=</span> <span class="n">BufferedGitBlobDataIterator</span><span class="p">(</span>
            <span class="n">blobs_and_paths</span><span class="o">=</span><span class="n">blobs_and_paths</span><span class="p">,</span>
            <span class="n">github_client</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_github_client</span><span class="p">,</span>
            <span class="n">owner</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span>
            <span class="n">repo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span>
            <span class="n">loop</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span>
            <span class="n">buffer_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_concurrent_requests</span><span class="p">,</span>  <span class="c1"># TODO: make this configurable</span>
            <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">blob_data</span><span class="p">,</span> <span class="n">full_path</span> <span class="ow">in</span> <span class="n">buffered_iterator</span><span class="p">:</span>
            <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"generating document for </span><span class="si">{</span><span class="n">full_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">assert</span> <span class="p">(</span>
                <span class="n">blob_data</span><span class="o">.</span><span class="n">encoding</span> <span class="o">==</span> <span class="s2">"base64"</span>
            <span class="p">),</span> <span class="sa">f</span><span class="s2">"blob encoding </span><span class="si">{</span><span class="n">blob_data</span><span class="o">.</span><span class="n">encoding</span><span class="si">}</span><span class="s2"> not supported"</span>
            <span class="n">decoded_bytes</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">decoded_bytes</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">blob_data</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
                <span class="k">del</span> <span class="n">blob_data</span><span class="o">.</span><span class="n">content</span>
            <span class="k">except</span> <span class="n">binascii</span><span class="o">.</span><span class="n">Error</span><span class="p">:</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"could not decode </span><span class="si">{</span><span class="n">full_path</span><span class="si">}</span><span class="s2"> as base64"</span>
                <span class="p">)</span>
                <span class="k">continue</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_use_parser</span><span class="p">:</span>
                <span class="n">document</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_supported_file</span><span class="p">(</span>
                    <span class="n">file_path</span><span class="o">=</span><span class="n">full_path</span><span class="p">,</span>
                    <span class="n">file_content</span><span class="o">=</span><span class="n">decoded_bytes</span><span class="p">,</span>
                    <span class="n">tree_sha</span><span class="o">=</span><span class="n">blob_data</span><span class="o">.</span><span class="n">sha</span><span class="p">,</span>
                    <span class="n">tree_path</span><span class="o">=</span><span class="n">full_path</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">if</span> <span class="n">document</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>
                    <span class="k">continue</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                    <span class="sa">f</span><span class="s2">"could not parse </span><span class="si">{</span><span class="n">full_path</span><span class="si">}</span><span class="s2"> as a supported file type"</span>
                    <span class="o">+</span> <span class="s2">" - falling back to decoding as utf-8 raw text"</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">decoded_bytes</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"decoded_bytes is None"</span><span class="p">)</span>
                <span class="n">decoded_text</span> <span class="o">=</span> <span class="n">decoded_bytes</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"could not decode </span><span class="si">{</span><span class="n">full_path</span><span class="si">}</span><span class="s2"> as utf-8"</span>
                <span class="p">)</span>
                <span class="k">continue</span>
            <span class="n">print_if_verbose</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                <span class="sa">f</span><span class="s2">"got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">decoded_text</span><span class="p">)</span><span class="si">}</span><span class="s2"> characters"</span>
                <span class="o">+</span> <span class="sa">f</span><span class="s2">"- adding to documents - </span><span class="si">{</span><span class="n">full_path</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="s2">"https://github.com/"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_owner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_repo</span><span class="p">,</span> <span class="s2">"blob/"</span><span class="p">,</span> <span class="nb">id</span><span class="p">,</span> <span class="n">full_path</span>
            <span class="p">)</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">decoded_text</span><span class="p">,</span>
                <span class="n">doc_id</span><span class="o">=</span><span class="n">blob_data</span><span class="o">.</span><span class="n">sha</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">full_path</span><span class="p">,</span>
                    <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">full_path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                    <span class="s2">"url"</span><span class="p">:</span> <span class="n">url</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">_parse_supported_file</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">file_content</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span>
        <span class="n">tree_sha</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tree_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Parse a file if it is supported by a parser.</span>

<span class="sd">        :param `file_path`: path of the file in the repo</span>
<span class="sd">        :param `file_content`: content of the file</span>
<span class="sd">        :return: Document if the file is supported by a parser, None otherwise</span>
<span class="sd">        """</span>
        <span class="n">file_extension</span> <span class="o">=</span> <span class="n">get_file_extension</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_supported_suffix</span><span class="p">:</span>
            <span class="c1"># skip</span>
            <span class="k">return</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_file_readers</span><span class="p">:</span>
            <span class="c1"># initialize reader</span>
            <span class="n">cls_</span> <span class="o">=</span> <span class="n">DEFAULT_FILE_READER_CLS</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_file_readers</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span> <span class="o">=</span> <span class="n">cls_</span><span class="p">()</span>

        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_file_readers</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span>

        <span class="n">print_if_verbose</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
            <span class="sa">f</span><span class="s2">"parsing </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">"</span>
            <span class="o">+</span> <span class="sa">f</span><span class="s2">"as </span><span class="si">{</span><span class="n">file_extension</span><span class="si">}</span><span class="s2"> with "</span>
            <span class="o">+</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">reader</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">tmpdirname</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">(</span>
                <span class="nb">dir</span><span class="o">=</span><span class="n">tmpdirname</span><span class="p">,</span>
                <span class="n">suffix</span><span class="o">=</span><span class="sa">f</span><span class="s2">".</span><span class="si">{</span><span class="n">file_extension</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="n">mode</span><span class="o">=</span><span class="s2">"w+b"</span><span class="p">,</span>
                <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span> <span class="k">as</span> <span class="n">tmpfile</span><span class="p">:</span>
                <span class="n">print_if_verbose</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                    <span class="s2">"created a temporary file"</span>
                    <span class="o">+</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">tmpfile</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2"> for parsing </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">tmpfile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">file_content</span><span class="p">)</span>
                <span class="n">tmpfile</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
                <span class="n">tmpfile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">docs</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">pathlib</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span><span class="n">tmpfile</span><span class="o">.</span><span class="n">name</span><span class="p">))</span>
                    <span class="n">parsed_file</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">doc</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">])</span>
                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">print_if_verbose</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"error while parsing </span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                        <span class="s2">"Error while parsing "</span>
                        <span class="o">+</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> with "</span>
                        <span class="o">+</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">reader</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">:</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>
                    <span class="n">parsed_file</span> <span class="o">=</span> <span class="kc">None</span>
                <span class="k">finally</span><span class="p">:</span>
                    <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">tmpfile</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">parsed_file</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">return</span> <span class="kc">None</span>
                <span class="k">return</span> <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">parsed_file</span><span class="p">,</span>
                    <span class="n">doc_id</span><span class="o">=</span><span class="n">tree_sha</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"file_path"</span><span class="p">:</span> <span class="n">file_path</span><span class="p">,</span>
                        <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">tree_path</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### FilterType [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/#llama_index.readers.github.GithubRepositoryReader.FilterType "Permanent link")

Bases: `Enum`

Filter type.

Used to determine whether the filter is inclusive or exclusive.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `-` | `EXCLUDE` | 
Exclude the files in the directories or with the extensions.



 |
| `-` | `INCLUDE` | 

Include only the files in the directories or with the extensions.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-github/llama_index/readers/github/repository/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">64</span>
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
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FilterType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Filter type.</span>

<span class="sd">    Used to determine whether the filter is inclusive or exclusive.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        - EXCLUDE: Exclude the files in the directories or with the extensions.</span>
<span class="sd">        - INCLUDE: Include only the files in the directories or with the extensions.</span>
<span class="sd">    """</span>

    <span class="n">EXCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>
    <span class="n">INCLUDE</span> <span class="o">=</span> <span class="n">enum</span><span class="o">.</span><span class="n">auto</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/#llama_index.readers.github.GithubRepositoryReader.load_data "Permanent link")

```
load_data(commit_sha: Optional[str] = None, branch: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from a commit or a branch.

Loads github repository data from a specific commit sha or a branch.

:param `commit`: commit sha :param `branch`: branch name

:return: list of documents

Source code in `llama-index-integrations/readers/llama-index-readers-github/llama_index/readers/github/repository/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">commit_sha</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">branch</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load data from a commit or a branch.</span>

<span class="sd">    Loads github repository data from a specific commit sha or a branch.</span>

<span class="sd">    :param `commit`: commit sha</span>
<span class="sd">    :param `branch`: branch name</span>

<span class="sd">    :return: list of documents</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">branch</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You can only specify one of commit or branch."</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">branch</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must specify one of commit or branch."</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">commit_sha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_from_commit</span><span class="p">(</span><span class="n">commit_sha</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">branch</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_data_from_branch</span><span class="p">(</span><span class="n">branch</span><span class="p">)</span>

    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must specify one of commit or branch."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Genius](https://docs.llamaindex.ai/en/stable/api_reference/readers/genius/)[Next Google](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/)
