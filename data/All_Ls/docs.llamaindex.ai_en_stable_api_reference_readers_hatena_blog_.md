Title: Hatena blog - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/

Markdown Content:
Hatena blog - LlamaIndex


HatenaBlogReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/#llama_index.readers.hatena_blog.HatenaBlogReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Hatena Blog reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `root_endpoint` | `str` | 
AtomPub root endpoint.



 | _required_ |
| `api_key` | `str` | 

AtomPub API Key



 | _required_ |
| `username` | `str` | 

Hatena ID



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-hatena-blog/llama_index/readers/hatena_blog/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
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
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HatenaBlogReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hatena Blog reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        root_endpoint (str): AtomPub root endpoint.</span>
<span class="sd">        api_key (str): AtomPub API Key</span>
<span class="sd">        username (str): Hatena ID</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">root_endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Hatena Blog reader."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">root_endpoint</span> <span class="o">=</span> <span class="n">root_endpoint</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">username</span> <span class="o">=</span> <span class="n">username</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">articles</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_articles</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">articles</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">a</span><span class="o">.</span><span class="n">content</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">a</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
                        <span class="s2">"published"</span><span class="p">:</span> <span class="n">a</span><span class="o">.</span><span class="n">published</span><span class="p">,</span>
                        <span class="s2">"url"</span><span class="p">:</span> <span class="n">a</span><span class="o">.</span><span class="n">url</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">get_all_articles</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Article</span><span class="p">]:</span>
        <span class="n">articles</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Article</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">page_url</span> <span class="o">=</span> <span class="n">ATOM_PUB_ENTRY_URL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">root_endpoint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">root_endpoint</span><span class="p">)</span>

        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_articles</span><span class="p">(</span><span class="n">page_url</span><span class="p">)</span>
            <span class="n">articles</span> <span class="o">+=</span> <span class="n">res</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"articles"</span><span class="p">)</span>
            <span class="n">page_url</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"next_page"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">page_url</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">articles</span>

    <span class="k">def</span> <span class="nf">get_articles</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">requests</span>
        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>
        <span class="kn">from</span> <span class="nn">requests.auth</span> <span class="kn">import</span> <span class="n">HTTPBasicAuth</span>

        <span class="n">articles</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Article</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">next_page</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="n">res</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="n">HTTPBasicAuth</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">username</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">))</span>
        <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">res</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="s2">"xml"</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">soup</span><span class="o">.</span><span class="n">find_all</span><span class="p">(</span><span class="s2">"entry"</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">entry</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"app:control"</span><span class="p">)</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"app:draft"</span><span class="p">)</span><span class="o">.</span><span class="n">string</span> <span class="o"></span> <span class="s2">"text/html"</span><span class="p">:</span>
                <span class="n">article</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">entry</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span><span class="o">.</span><span class="n">string</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
                    <span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
                    <span class="o">.</span><span class="n">strip</span><span class="p">()</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">article</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">entry</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span><span class="o">.</span><span class="n">string</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="n">articles</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">article</span><span class="p">)</span>

        <span class="nb">next</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">"link"</span><span class="p">,</span> <span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="s2">"rel"</span><span class="p">:</span> <span class="s2">"next"</span><span class="p">})</span>
        <span class="k">if</span> <span class="nb">next</span><span class="p">:</span>
            <span class="n">next_page</span> <span class="o">=</span> <span class="nb">next</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"href"</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span><span class="s2">"articles"</span><span class="p">:</span> <span class="n">articles</span><span class="p">,</span> <span class="s2">"next_page"</span><span class="p">:</span> <span class="n">next_page</span><span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Guru](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/)[Next Hive](https://docs.llamaindex.ai/en/stable/api_reference/readers/hive/)
