Title: Azure devops - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/

Markdown Content:
Azure devops - LlamaIndex


AzureDevopsReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/#llama_index.readers.azure_devops.AzureDevopsReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

A loader class for Azure DevOps repositories. This class provides methods to authenticate with Azure DevOps, access repositories, and retrieve file content.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `access_token` | `str` | 
The personal access token for Azure DevOps.



 |
| `organization_name` | `str` | 

The name of the organization in Azure DevOps.



 |
| `project_name` | `str` | 

The name of the project in Azure DevOps.



 |
| `repo` | `str` | 

The name of the repository in the project.



 |
| `organization_url` | `str` | 

The URL to the organization in Azure DevOps.



 |
| `git_client` |  | 

The Git client for interacting with Azure DevOps.



 |
| `repository_id` |  | 

The ID of the repository in Azure DevOps.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azure-devops/llama_index/readers/azure_devops/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  6</span>
<span class="normal">  7</span>
<span class="normal">  8</span>
<span class="normal">  9</span>
<span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
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
<span class="normal">182</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureDevopsReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A loader class for Azure DevOps repositories. This class provides methods to authenticate with Azure DevOps,</span>
<span class="sd">    access repositories, and retrieve file content.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        access_token (str): The personal access token for Azure DevOps.</span>
<span class="sd">        organization_name (str): The name of the organization in Azure DevOps.</span>
<span class="sd">        project_name (str): The name of the project in Azure DevOps.</span>
<span class="sd">        repo (str): The name of the repository in the project.</span>
<span class="sd">        organization_url (str): The URL to the organization in Azure DevOps.</span>
<span class="sd">        git_client: The Git client for interacting with Azure DevOps.</span>
<span class="sd">        repository_id: The ID of the repository in Azure DevOps.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">access_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">organization_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">project_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">repo</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">file_filter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes the AzureDevopsLoader with the necessary details to interact with an Azure DevOps repository.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            access_token (str): The personal access token for Azure DevOps.</span>
<span class="sd">            organization_name (str): The name of the organization in Azure DevOps.</span>
<span class="sd">            project_name (str): The name of the project in Azure DevOps.</span>
<span class="sd">            repo (str): The name of the repository in the project.</span>
<span class="sd">            file_filter(callable): A function that can be used as file filter ex: `lambda file_path: file_path.endswith(".py")`</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span> <span class="o">=</span> <span class="n">access_token</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">project_name</span> <span class="o">=</span> <span class="n">project_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">repo</span> <span class="o">=</span> <span class="n">repo</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">organization_url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://dev.azure.com/</span><span class="si">{</span><span class="n">organization_name</span><span class="si">}</span><span class="s2">/"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_filter</span> <span class="o">=</span> <span class="n">file_filter</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">git_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_git_client</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">repository_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_repository_id</span><span class="p">(</span><span class="n">repo_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repo</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">create_git_client</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Creates and returns a Git client for interacting with Azure DevOps.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The Git client object for Azure DevOps.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">azure.devops.connection</span> <span class="kn">import</span> <span class="n">Connection</span>
            <span class="kn">from</span> <span class="nn">msrest.authentication</span> <span class="kn">import</span> <span class="n">BasicAuthentication</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install azure-devops to use the AzureDevopsLoader. "</span>
                <span class="s2">"You can do so by running `pip install azure-devops`."</span>
            <span class="p">)</span>
        <span class="n">credentials</span> <span class="o">=</span> <span class="n">BasicAuthentication</span><span class="p">(</span><span class="s2">""</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">)</span>
        <span class="n">connection</span> <span class="o">=</span> <span class="n">Connection</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">organization_url</span><span class="p">,</span> <span class="n">creds</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">connection</span><span class="o">.</span><span class="n">clients</span><span class="o">.</span><span class="n">get_git_client</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_get_repository_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">repo_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves the repository ID for a given repository name.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            repo_name (str): The name of the repository.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The ID of the repository.</span>
<span class="sd">        """</span>
        <span class="n">repositories</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">git_client</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">next</span><span class="p">((</span><span class="n">repo</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">repo</span> <span class="ow">in</span> <span class="n">repositories</span> <span class="k">if</span> <span class="n">repo</span><span class="o">.</span><span class="n">name</span> <span class="o"></span> <span class="s2">"blob"</span><span class="p">)</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_file_content_by_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves the content of a file by its path in the repository.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            path (str): The path of the file in the repository.</span>
<span class="sd">            version_descriptor (Optional): The version descriptor to specify a version or branch.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The content of the file as a string.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">stream</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">git_client</span><span class="o">.</span><span class="n">get_item_text</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repository_id</span><span class="p">,</span>
                <span class="n">path</span><span class="o">=</span><span class="n">path</span><span class="p">,</span>
                <span class="n">project</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="p">,</span>
                <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">file_content</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="c1"># Iterate over the generator object</span>
            <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">stream</span><span class="p">:</span>
                <span class="c1"># Assuming the content is encoded in UTF-8, decode each chunk and append to the file_content string</span>
                <span class="n">file_content</span> <span class="o">+=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">file_content</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"failed loading </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">folder</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span> <span class="n">branch</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Loads the documents from a specified folder and branch in the repository.</span>

<span class="sd">        Parameters:</span>
<span class="sd">            folder (Optional[str]): The folder to load documents from, defaults to root.</span>
<span class="sd">            branch (Optional[str]): The branch to load documents from.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A list of Document objects representing the loaded documents.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">version_descriptor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_version_descriptor</span><span class="p">(</span><span class="n">branch</span><span class="o">=</span><span class="n">branch</span><span class="p">)</span>
        <span class="n">files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_file_paths</span><span class="p">(</span>
            <span class="n">folder</span><span class="o">=</span><span class="n">folder</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
            <span class="n">path</span> <span class="o">=</span> <span class="n">file</span><span class="p">[</span><span class="s2">"path"</span><span class="p">]</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_file_content_by_path</span><span class="p">(</span>
                <span class="n">path</span><span class="o">=</span><span class="n">path</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">content</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="s2">"path"</span><span class="p">:</span> <span class="n">path</span><span class="p">,</span>
                    <span class="s2">"extension"</span><span class="p">:</span> <span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"."</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                    <span class="s2">"source"</span><span class="p">:</span> <span class="n">file</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                <span class="p">}</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### create\_git\_client [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/#llama_index.readers.azure_devops.AzureDevopsReader.create_git_client "Permanent link")

```
create_git_client()
```

Creates and returns a Git client for interacting with Azure DevOps.

**Returns:**

| Type | Description |
| --- | --- |
|  | 
The Git client object for Azure DevOps.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azure-devops/llama_index/readers/azure_devops/base.py`

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
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_git_client</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Creates and returns a Git client for interacting with Azure DevOps.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The Git client object for Azure DevOps.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">azure.devops.connection</span> <span class="kn">import</span> <span class="n">Connection</span>
        <span class="kn">from</span> <span class="nn">msrest.authentication</span> <span class="kn">import</span> <span class="n">BasicAuthentication</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install azure-devops to use the AzureDevopsLoader. "</span>
            <span class="s2">"You can do so by running `pip install azure-devops`."</span>
        <span class="p">)</span>
    <span class="n">credentials</span> <span class="o">=</span> <span class="n">BasicAuthentication</span><span class="p">(</span><span class="s2">""</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">access_token</span><span class="p">)</span>
    <span class="n">connection</span> <span class="o">=</span> <span class="n">Connection</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">organization_url</span><span class="p">,</span> <span class="n">creds</span><span class="o">=</span><span class="n">credentials</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">connection</span><span class="o">.</span><span class="n">clients</span><span class="o">.</span><span class="n">get_git_client</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_file\_paths [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/#llama_index.readers.azure_devops.AzureDevopsReader.get_file_paths "Permanent link")

```
get_file_paths(folder: str = '/', version_descriptor=None) -> List[Dict]
```

Retrieves the paths of all files within a given folder in the repository.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `folder` | `str` | 
The folder to retrieve file paths from, defaults to root.



 | `'/'` |
| `version_descriptor` | `Optional` | 

The version descriptor to specify a version or branch.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[Dict]` | 
A list of paths of the files.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azure-devops/llama_index/readers/azure_devops/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
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
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_file_paths</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">folder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieves the paths of all files within a given folder in the repository.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        folder (str): The folder to retrieve file paths from, defaults to root.</span>
<span class="sd">        version_descriptor (Optional): The version descriptor to specify a version or branch.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A list of paths of the files.</span>
<span class="sd">    """</span>
    <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">git_client</span><span class="o">.</span><span class="n">get_items</span><span class="p">(</span>
        <span class="n">repository_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repository_id</span><span class="p">,</span>
        <span class="n">project</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="p">,</span>
        <span class="n">scope_path</span><span class="o">=</span><span class="n">folder</span><span class="p">,</span>
        <span class="n">recursion_level</span><span class="o">=</span><span class="s2">"Full"</span><span class="p">,</span>
        <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="p">{</span><span class="s2">"path"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">path</span><span class="p">,</span> <span class="s2">"url"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">url</span><span class="p">}</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">file_filter</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">file_filter</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">path</span><span class="p">))</span>
        <span class="ow">and</span> <span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">git_object_type</span> <span class="o">==</span> <span class="s2">"blob"</span><span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_file\_content\_by\_path [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/#llama_index.readers.azure_devops.AzureDevopsReader.get_file_content_by_path "Permanent link")

```
get_file_content_by_path(path: str, version_descriptor=None)
```

Retrieves the content of a file by its path in the repository.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str` | 
The path of the file in the repository.



 | _required_ |
| `version_descriptor` | `Optional` | 

The version descriptor to specify a version or branch.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
|  | 
The content of the file as a string.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azure-devops/llama_index/readers/azure_devops/base.py`

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
<span class="normal">152</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_file_content_by_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Retrieves the content of a file by its path in the repository.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        path (str): The path of the file in the repository.</span>
<span class="sd">        version_descriptor (Optional): The version descriptor to specify a version or branch.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The content of the file as a string.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">stream</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">git_client</span><span class="o">.</span><span class="n">get_item_text</span><span class="p">(</span>
            <span class="n">repository_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">repository_id</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="n">path</span><span class="p">,</span>
            <span class="n">project</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">project_name</span><span class="p">,</span>
            <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">file_content</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="c1"># Iterate over the generator object</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">stream</span><span class="p">:</span>
            <span class="c1"># Assuming the content is encoded in UTF-8, decode each chunk and append to the file_content string</span>
            <span class="n">file_content</span> <span class="o">+=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">file_content</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"failed loading </span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/#llama_index.readers.azure_devops.AzureDevopsReader.load_data "Permanent link")

```
load_data(folder: Optional[str] = '/', branch: Optional[str] = None)
```

Loads the documents from a specified folder and branch in the repository.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `folder` | `Optional[str]` | 
The folder to load documents from, defaults to root.



 | `'/'` |
| `branch` | `Optional[str]` | 

The branch to load documents from.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
|  | 
A list of Document objects representing the loaded documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-azure-devops/llama_index/readers/azure_devops/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">154</span>
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
<span class="normal">182</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">folder</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span> <span class="n">branch</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Loads the documents from a specified folder and branch in the repository.</span>

<span class="sd">    Parameters:</span>
<span class="sd">        folder (Optional[str]): The folder to load documents from, defaults to root.</span>
<span class="sd">        branch (Optional[str]): The branch to load documents from.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A list of Document objects representing the loaded documents.</span>
<span class="sd">    """</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">version_descriptor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_version_descriptor</span><span class="p">(</span><span class="n">branch</span><span class="o">=</span><span class="n">branch</span><span class="p">)</span>
    <span class="n">files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_file_paths</span><span class="p">(</span>
        <span class="n">folder</span><span class="o">=</span><span class="n">folder</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span>
    <span class="p">)</span>
    <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
        <span class="n">path</span> <span class="o">=</span> <span class="n">file</span><span class="p">[</span><span class="s2">"path"</span><span class="p">]</span>
        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_file_content_by_path</span><span class="p">(</span>
            <span class="n">path</span><span class="o">=</span><span class="n">path</span><span class="p">,</span> <span class="n">version_descriptor</span><span class="o">=</span><span class="n">version_descriptor</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">content</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"path"</span><span class="p">:</span> <span class="n">path</span><span class="p">,</span>
                <span class="s2">"extension"</span><span class="p">:</span> <span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"."</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                <span class="s2">"source"</span><span class="p">:</span> <span class="n">file</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
            <span class="p">}</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azstorage blob](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/)[Next Bagel](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/)
