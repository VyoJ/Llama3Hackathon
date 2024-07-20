Title: Chatgpt plugin - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/

Markdown Content:
Chatgpt plugin - LlamaIndex


init.py.

ChatGPTPluginToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/#llama_index.tools.chatgpt_plugin.ChatGPTPluginToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

ChatGPT Plugin Tool.

This tool leverages the OpenAPI tool spec to automatically load ChatGPT plugins from a manifest file. You should also provide the Requests tool spec to allow the Agent to make calls to the OpenAPI endpoints To use endpoints with authorization, use the Requests tool spec with the authorization headers

Source code in `llama-index-integrations/tools/llama-index-tools-chatgpt-plugin/llama_index/tools/chatgpt_plugin/base.py`

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
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChatGPTPluginToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ChatGPT Plugin Tool.</span>

<span class="sd">    This tool leverages the OpenAPI tool spec to automatically load ChatGPT</span>
<span class="sd">    plugins from a manifest file.</span>
<span class="sd">    You should also provide the Requests tool spec to allow the Agent to make calls to the OpenAPI endpoints</span>
<span class="sd">    To use endpoints with authorization, use the Requests tool spec with the authorization headers</span>
<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"load_openapi_spec"</span><span class="p">,</span> <span class="s2">"describe_plugin"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">manifest</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">manifest_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="kn">import</span> <span class="nn">yaml</span>

        <span class="k">if</span> <span class="n">manifest</span> <span class="ow">and</span> <span class="n">manifest_url</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You cannot provide both a manifest and a manifest_url"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">manifest</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">elif</span> <span class="n">manifest_url</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">manifest_url</span><span class="p">)</span><span class="o">.</span><span class="n">text</span>
            <span class="n">manifest</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"You must provide either a manifest or a manifest_url"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">manifest</span><span class="p">[</span><span class="s2">"api"</span><span class="p">][</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">"openapi"</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s1">'API type must be "openapi", not "</span><span class="si">{</span><span class="n">manifest</span><span class="p">[</span><span class="s2">"api"</span><span class="p">][</span><span class="s2">"type"</span><span class="p">]</span><span class="si">}</span><span class="s1">"'</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">manifest</span><span class="p">[</span><span class="s2">"auth"</span><span class="p">][</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">!=</span> <span class="s2">"none"</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Authentication cannot be supported for ChatGPT plugins"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">openapi</span> <span class="o">=</span> <span class="n">OpenAPIToolSpec</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">manifest</span><span class="p">[</span><span class="s2">"api"</span><span class="p">][</span><span class="s2">"url"</span><span class="p">])</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">plugin_description</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            'human_description': </span><span class="si">{</span><span class="n">manifest</span><span class="p">[</span><span class="s1">'description_for_human'</span><span class="p">]</span><span class="si">}</span>
<span class="s2">            'model_description': </span><span class="si">{</span><span class="n">manifest</span><span class="p">[</span><span class="s1">'description_for_model'</span><span class="p">]</span><span class="si">}</span>
<span class="s2">        """</span>

    <span class="k">def</span> <span class="nf">load_openapi_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.</span>

<span class="sd">        Here's a step-by-step guide to assist you in answering questions:</span>

<span class="sd">        1. Determine the base URL required for making the request</span>

<span class="sd">        2. Identify the relevant paths necessary to address the question</span>

<span class="sd">        3. Find the required parameters for making the request</span>

<span class="sd">        4. Perform the necessary requests to obtain the answer</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: A List of Document objects describing the OpenAPI spec</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">openapi</span><span class="o">.</span><span class="n">load_openapi_spec</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">describe_plugin</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">plugin_description</span>
</code></pre></div></td></tr></tbody></table>

### load\_openapi\_spec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/#llama_index.tools.chatgpt_plugin.ChatGPTPluginToolSpec.load_openapi_spec "Permanent link")

```
load_openapi_spec() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.

Here's a step-by-step guide to assist you in answering questions:

1.  Determine the base URL required for making the request
    
2.  Identify the relevant paths necessary to address the question
    
3.  Find the required parameters for making the request
    
4.  Perform the necessary requests to obtain the answer
    

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `Document` | `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
A List of Document objects describing the OpenAPI spec



 |

Source code in `llama-index-integrations/tools/llama-index-tools-chatgpt-plugin/llama_index/tools/chatgpt_plugin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
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
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_openapi_spec</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    You are an AI agent specifically designed to retrieve information by making web requests to an API based on an OpenAPI specification.</span>

<span class="sd">    Here's a step-by-step guide to assist you in answering questions:</span>

<span class="sd">    1. Determine the base URL required for making the request</span>

<span class="sd">    2. Identify the relevant paths necessary to address the question</span>

<span class="sd">    3. Find the required parameters for making the request</span>

<span class="sd">    4. Perform the necessary requests to obtain the answer</span>

<span class="sd">    Returns:</span>
<span class="sd">        Document: A List of Document objects describing the OpenAPI spec</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">openapi</span><span class="o">.</span><span class="n">load_openapi_spec</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/tools/cassandra/)[Next Code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/)
