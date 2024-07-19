Title: Intercom - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/

Markdown Content:
Intercom - LlamaIndex


IntercomReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/#llama_index.readers.intercom.IntercomReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Intercom reader. Reads data from a Intercom workspace.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `personal_access_token` | `str` | 
Intercom token.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-intercom/llama_index/readers/intercom/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
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
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
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
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IntercomReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Intercom reader. Reads data from a Intercom workspace.</span>

<span class="sd">    Args:</span>
<span class="sd">        personal_access_token (str): Intercom token.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">intercom_access_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Intercom reader."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">intercom_access_token</span> <span class="o">=</span> <span class="n">intercom_access_token</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the workspace.</span>

<span class="sd">        Args:</span>
<span class="sd">            workspace_id (str): Workspace ID.</span>


<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">articles</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_articles</span><span class="p">()</span>

        <span class="k">for</span> <span class="n">article</span> <span class="ow">in</span> <span class="n">articles</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">article</span><span class="p">[</span><span class="s2">"body"</span><span class="p">]</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">body</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>

            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"id"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                <span class="s2">"url"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                <span class="s2">"updated_at"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"updated_at"</span><span class="p">],</span>
            <span class="p">}</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">body</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">get_all_articles</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">articles</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">next_page</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_articles_page</span><span class="p">(</span><span class="n">next_page</span><span class="p">)</span>
            <span class="n">articles</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s2">"articles"</span><span class="p">])</span>
            <span class="n">next_page</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"next_page"</span><span class="p">]</span>

            <span class="k">if</span> <span class="n">next_page</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">articles</span>

    <span class="k">def</span> <span class="nf">get_articles_page</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">next_page</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="kn">import</span> <span class="nn">requests</span>

        <span class="k">if</span> <span class="n">next_page</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">url</span> <span class="o">=</span> <span class="s2">"https://api.intercom.io/articles"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">url</span> <span class="o">=</span> <span class="n">next_page</span>

        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Intercom-Version"</span><span class="p">:</span> <span class="s2">"2.8"</span><span class="p">,</span>
            <span class="s2">"authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">intercom_access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>

        <span class="n">response_json</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>

        <span class="n">next_page</span> <span class="o">=</span> <span class="n">response_json</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"pages"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"next"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

        <span class="n">articles</span> <span class="o">=</span> <span class="n">response_json</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"data"</span><span class="p">,</span> <span class="p">[])</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"articles"</span><span class="p">:</span> <span class="n">articles</span><span class="p">,</span> <span class="s2">"next_page"</span><span class="p">:</span> <span class="n">next_page</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/#llama_index.readers.intercom.IntercomReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the workspace.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `workspace_id` | `str` | 
Workspace ID.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-intercom/llama_index/readers/intercom/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the workspace.</span>

<span class="sd">    Args:</span>
<span class="sd">        workspace_id (str): Workspace ID.</span>


<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">articles</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_articles</span><span class="p">()</span>

    <span class="k">for</span> <span class="n">article</span> <span class="ow">in</span> <span class="n">articles</span><span class="p">:</span>
        <span class="n">body</span> <span class="o">=</span> <span class="n">article</span><span class="p">[</span><span class="s2">"body"</span><span class="p">]</span>
        <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">body</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
        <span class="n">body</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>

        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"id"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
            <span class="s2">"title"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
            <span class="s2">"url"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
            <span class="s2">"updated_at"</span><span class="p">:</span> <span class="n">article</span><span class="p">[</span><span class="s2">"updated_at"</span><span class="p">],</span>
        <span class="p">}</span>

        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">body</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/readers/)[Next Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/)
