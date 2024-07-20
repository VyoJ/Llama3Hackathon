Title: Azure openai - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/

Markdown Content:
Azure openai - LlamaIndex


AzureOpenAIMultiModal [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/#llama_index.multi_modal_llms.azure_openai.AzureOpenAIMultiModal "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[OpenAIMultiModal](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/#llama_index.multi_modal_llms.openai.OpenAIMultiModal "llama_index.multi_modal_llms.openai.OpenAIMultiModal")`

Azure OpenAI.

To use this, you must first deploy a model on Azure OpenAI. Unlike OpenAI, you need to specify a `engine` parameter to identify your deployment (called "model deployment name" in Azure portal).

*   model: Name of the model (e.g. `text-davinci-003`) This in only used to decide completion vs. chat endpoint.
*   engine: This will correspond to the custom name you chose for your deployment when you deployed a model.

You must have the following environment variables set: - `OPENAI_API_VERSION`: set this to `2023-05-15` This may change in the future. - `AZURE_OPENAI_ENDPOINT`: your endpoint should look like the following https://YOUR\_RESOURCE\_NAME.openai.azure.com/ - `AZURE_OPENAI_API_KEY`: your API key if the api type is `azure`

More information can be found herehttps://learn.microsoft.com/en-us/azure/cognitive-services/openai/quickstart?tabs=command-line&pivots=programming-language-python

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-azure-openai/llama_index/multi_modal_llms/azure_openai/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
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
<span class="normal">158</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureOpenAIMultiModal</span><span class="p">(</span><span class="n">OpenAIMultiModal</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Azure OpenAI.</span>

<span class="sd">    To use this, you must first deploy a model on Azure OpenAI.</span>
<span class="sd">    Unlike OpenAI, you need to specify a `engine` parameter to identify</span>
<span class="sd">    your deployment (called "model deployment name" in Azure portal).</span>

<span class="sd">    - model: Name of the model (e.g. `text-davinci-003`)</span>
<span class="sd">        This in only used to decide completion vs. chat endpoint.</span>
<span class="sd">    - engine: This will correspond to the custom name you chose</span>
<span class="sd">        for your deployment when you deployed a model.</span>

<span class="sd">    You must have the following environment variables set:</span>
<span class="sd">    - `OPENAI_API_VERSION`: set this to `2023-05-15`</span>
<span class="sd">        This may change in the future.</span>
<span class="sd">    - `AZURE_OPENAI_ENDPOINT`: your endpoint should look like the following</span>
<span class="sd">        https://YOUR_RESOURCE_NAME.openai.azure.com/</span>
<span class="sd">    - `AZURE_OPENAI_API_KEY`: your API key if the api type is `azure`</span>

<span class="sd">    More information can be found here:</span>
<span class="sd">        https://learn.microsoft.com/en-us/azure/cognitive-services/openai/quickstart?tabs=command-line&amp;pivots=programming-language-python</span>
<span class="sd">    """</span>

    <span class="n">engine</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The name of the deployed azure engine."</span><span class="p">)</span>
    <span class="n">azure_endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The Azure endpoint to use."</span>
    <span class="p">)</span>
    <span class="n">azure_deployment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The Azure deployment to use."</span>
    <span class="p">)</span>
    <span class="n">use_azure_ad</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Indicates if Microsoft Entra ID (former Azure AD) is used for token authentication"</span>
    <span class="p">)</span>

    <span class="n">_azure_ad_token</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span>
        <span class="n">engine</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">DEFAULT_TEMPERATURE</span><span class="p">,</span>
        <span class="n">max_new_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">300</span><span class="p">,</span>
        <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_window</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_CONTEXT_WINDOW</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">60.0</span><span class="p">,</span>
        <span class="n">image_detail</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"low"</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_base</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_version</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># azure specific</span>
        <span class="n">azure_endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">azure_deployment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">use_azure_ad</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="c1"># aliases for engine</span>
        <span class="n">deployment_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deployment_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deployment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">messages_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">completion_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">default_headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">httpx</span><span class="o">.</span><span class="n">Client</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">engine</span> <span class="o">=</span> <span class="n">resolve_from_aliases</span><span class="p">(</span>
            <span class="n">engine</span><span class="p">,</span> <span class="n">deployment_name</span><span class="p">,</span> <span class="n">deployment_id</span><span class="p">,</span> <span class="n">deployment</span><span class="p">,</span> <span class="n">azure_deployment</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">engine</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must specify an `engine` parameter."</span><span class="p">)</span>

        <span class="n">azure_endpoint</span> <span class="o">=</span> <span class="n">get_from_param_or_env</span><span class="p">(</span>
            <span class="s2">"azure_endpoint"</span><span class="p">,</span> <span class="n">azure_endpoint</span><span class="p">,</span> <span class="s2">"AZURE_OPENAI_ENDPOINT"</span><span class="p">,</span> <span class="s2">""</span>
        <span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">engine</span><span class="o">=</span><span class="n">engine</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">max_new_tokens</span><span class="o">=</span><span class="n">max_new_tokens</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">additional_kwargs</span><span class="p">,</span>
            <span class="n">context_window</span><span class="o">=</span><span class="n">context_window</span><span class="p">,</span>
            <span class="n">max_retries</span><span class="o">=</span><span class="n">max_retries</span><span class="p">,</span>
            <span class="n">timeout</span><span class="o">=</span><span class="n">timeout</span><span class="p">,</span>
            <span class="n">image_detail</span><span class="o">=</span><span class="n">image_detail</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">api_base</span><span class="o">=</span><span class="n">api_base</span><span class="p">,</span>
            <span class="n">api_version</span><span class="o">=</span><span class="n">api_version</span><span class="p">,</span>
            <span class="n">messages_to_prompt</span><span class="o">=</span><span class="n">messages_to_prompt</span><span class="p">,</span>
            <span class="n">completion_to_prompt</span><span class="o">=</span><span class="n">completion_to_prompt</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">azure_endpoint</span><span class="o">=</span><span class="n">azure_endpoint</span><span class="p">,</span>
            <span class="n">azure_deployment</span><span class="o">=</span><span class="n">azure_deployment</span><span class="p">,</span>
            <span class="n">use_azure_ad</span><span class="o">=</span><span class="n">use_azure_ad</span><span class="p">,</span>
            <span class="n">default_headers</span><span class="o">=</span><span class="n">default_headers</span><span class="p">,</span>
            <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_clients</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">SyncAzureOpenAI</span><span class="p">,</span> <span class="n">AsyncAzureOpenAI</span><span class="p">]:</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">SyncAzureOpenAI</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_credential_kwargs</span><span class="p">())</span>
        <span class="n">aclient</span> <span class="o">=</span> <span class="n">AsyncAzureOpenAI</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_credential_kwargs</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">client</span><span class="p">,</span> <span class="n">aclient</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"azure_openai_multi_modal_llm"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Multi Modal LLM metadata."""</span>
        <span class="k">return</span> <span class="n">MultiModalLLMMetadata</span><span class="p">(</span>
            <span class="n">num_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_new_tokens</span> <span class="ow">or</span> <span class="n">DEFAULT_NUM_OUTPUTS</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">engine</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_credential_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_azure_ad</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_azure_ad_token</span> <span class="o">=</span> <span class="n">refresh_openai_azuread_token</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_azure_ad_token</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_azure_ad_token</span><span class="o">.</span><span class="n">token</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"api_key"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="ow">or</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"max_retries"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span><span class="p">,</span>
            <span class="s2">"azure_endpoint"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">azure_endpoint</span><span class="p">,</span>
            <span class="s2">"azure_deployment"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">azure_deployment</span><span class="p">,</span>
            <span class="s2">"api_version"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_version</span><span class="p">,</span>
            <span class="s2">"default_headers"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_headers</span><span class="p">,</span>
            <span class="s2">"http_client"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_http_client</span><span class="p">,</span>
            <span class="s2">"timeout"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_model_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">model_kwargs</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_get_model_kwargs</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">model_kwargs</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">engine</span>
        <span class="k">return</span> <span class="n">model_kwargs</span>
</code></pre></div></td></tr></tbody></table>

### metadata `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/#llama_index.multi_modal_llms.azure_openai.AzureOpenAIMultiModal.metadata "Permanent link")

```
metadata: MultiModalLLMMetadata
```

Multi Modal LLM metadata.

Back to top

[Previous Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/anthropic/)[Next Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/dashscope/)
