Title: Requests - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/

Markdown Content:
Requests - LlamaIndex


RequestsToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/#llama_index.tools.requests.RequestsToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Requests Tool.

Source code in `llama-index-integrations/tools/llama-index-tools-requests/llama_index/tools/requests/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
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
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RequestsToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Requests Tool."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"get_request"</span><span class="p">,</span> <span class="s2">"post_request"</span><span class="p">,</span> <span class="s2">"patch_request"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">domain_headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">domain_headers</span> <span class="o">=</span> <span class="n">domain_headers</span>

    <span class="k">def</span> <span class="nf">get_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this to GET content from a website.</span>

<span class="sd">        Args:</span>
<span class="sd">            url ([str]): The url to make the get request against</span>
<span class="sd">            params (Optional[dict]): the parameters to provide with the get request</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">post_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this to POST content to a website.</span>

<span class="sd">        Args:</span>
<span class="sd">            url ([str]): The url to make the get request against</span>
<span class="sd">            data (Optional[dict]): the key-value pairs to provide with the get request</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">json</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">patch_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Use this to PATCH content to a website.</span>

<span class="sd">        Args:</span>
<span class="sd">            url ([str]): The url to make the get request against</span>
<span class="sd">            data (Optional[dict]): the key-value pairs to provide with the get request</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

        <span class="n">requests</span><span class="o">.</span><span class="n">patch</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">json</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_valid_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">parsed</span> <span class="o">=</span> <span class="n">urlparse</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">parsed</span><span class="o">.</span><span class="n">scheme</span> <span class="ow">and</span> <span class="n">parsed</span><span class="o">.</span><span class="n">hostname</span>

    <span class="k">def</span> <span class="nf">_get_domain</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">urlparse</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">hostname</span>

    <span class="k">def</span> <span class="nf">_get_headers_for_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">domain_headers</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_domain</span><span class="p">(</span><span class="n">url</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### get\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/#llama_index.tools.requests.RequestsToolSpec.get_request "Permanent link")

```
get_request(url: str, params: Optional[dict] = {})
```

Use this to GET content from a website.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `[str]` | 
The url to make the get request against



 | _required_ |
| `params` | `Optional[dict]` | 

the parameters to provide with the get request



 | `{}` |

Source code in `llama-index-integrations/tools/llama-index-tools-requests/llama_index/tools/requests/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
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
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this to GET content from a website.</span>

<span class="sd">    Args:</span>
<span class="sd">        url ([str]): The url to make the get request against</span>
<span class="sd">        params (Optional[dict]): the parameters to provide with the get request</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

    <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### post\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/#llama_index.tools.requests.RequestsToolSpec.post_request "Permanent link")

```
post_request(url: str, data: Optional[dict] = {})
```

Use this to POST content to a website.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `[str]` | 
The url to make the get request against



 | _required_ |
| `data` | `Optional[dict]` | 

the key-value pairs to provide with the get request



 | `{}` |

Source code in `llama-index-integrations/tools/llama-index-tools-requests/llama_index/tools/requests/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
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
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">post_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this to POST content to a website.</span>

<span class="sd">    Args:</span>
<span class="sd">        url ([str]): The url to make the get request against</span>
<span class="sd">        data (Optional[dict]): the key-value pairs to provide with the get request</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

    <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">json</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### patch\_request [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/#llama_index.tools.requests.RequestsToolSpec.patch_request "Permanent link")

```
patch_request(url: str, data: Optional[dict] = {})
```

Use this to PATCH content to a website.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `url` | `[str]` | 
The url to make the get request against



 | _required_ |
| `data` | `Optional[dict]` | 

the key-value pairs to provide with the get request



 | `{}` |

Source code in `llama-index-integrations/tools/llama-index-tools-requests/llama_index/tools/requests/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
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
<span class="normal">67</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">patch_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Use this to PATCH content to a website.</span>

<span class="sd">    Args:</span>
<span class="sd">        url ([str]): The url to make the get request against</span>
<span class="sd">        data (Optional[dict]): the key-value pairs to provide with the get request</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_valid_url</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">INVALID_URL_PROMPT</span>

    <span class="n">requests</span><span class="o">.</span><span class="n">patch</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_headers_for_url</span><span class="p">(</span><span class="n">url</span><span class="p">),</span> <span class="n">json</span><span class="o">=</span><span class="n">data</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Query plan](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/)[Next Retriever](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/)
