Title: Snscrape twitter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/snscrape_twitter/

Markdown Content:
Snscrape twitter - LlamaIndex


SnscrapeTwitterReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/snscrape_twitter/#llama_index.readers.snscrape_twitter.SnscrapeTwitterReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

SnscrapeTwitter reader. Reads data from a twitter profile.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `username` | `str` | 
Twitter Username.



 | _required_ |
| `num_tweets` | `int` | 

Number of tweets to fetch.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-snscrape-twitter/llama_index/readers/snscrape_twitter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SnscrapeTwitterReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""SnscrapeTwitter reader. Reads data from a twitter profile.</span>

<span class="sd">    Args:</span>
<span class="sd">        username (str): Twitter Username.</span>
<span class="sd">        num_tweets (int): Number of tweets to fetch.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize SnscrapeTwitter reader."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num_tweets</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from a twitter profile.</span>

<span class="sd">        Args:</span>
<span class="sd">            username (str): Twitter Username.</span>
<span class="sd">            num_tweets (int): Number of tweets to fetch.</span>


<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">snscrape.modules.twitter</span> <span class="k">as</span> <span class="nn">sntwitter</span>

        <span class="n">attributes_container</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">tweet</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span>
            <span class="n">sntwitter</span><span class="o">.</span><span class="n">TwitterSearchScraper</span><span class="p">(</span><span class="sa">f</span><span class="s2">"from:</span><span class="si">{</span><span class="n">username</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span><span class="o">.</span><span class="n">get_items</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;</span> <span class="n">num_tweets</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="n">attributes_container</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tweet</span><span class="o">.</span><span class="n">rawContent</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">attributes_container</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"username"</span><span class="p">:</span> <span class="n">username</span><span class="p">})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/snscrape_twitter/#llama_index.readers.snscrape_twitter.SnscrapeTwitterReader.load_data "Permanent link")

```
load_data(username: str, num_tweets: int) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from a twitter profile.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `username` | `str` | 
Twitter Username.



 | _required_ |
| `num_tweets` | `int` | 

Number of tweets to fetch.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-snscrape-twitter/llama_index/readers/snscrape_twitter/base.py`

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
<span class="normal">39</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num_tweets</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from a twitter profile.</span>

<span class="sd">    Args:</span>
<span class="sd">        username (str): Twitter Username.</span>
<span class="sd">        num_tweets (int): Number of tweets to fetch.</span>


<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">snscrape.modules.twitter</span> <span class="k">as</span> <span class="nn">sntwitter</span>

    <span class="n">attributes_container</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">tweet</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span>
        <span class="n">sntwitter</span><span class="o">.</span><span class="n">TwitterSearchScraper</span><span class="p">(</span><span class="sa">f</span><span class="s2">"from:</span><span class="si">{</span><span class="n">username</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span><span class="o">.</span><span class="n">get_items</span><span class="p">()</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;</span> <span class="n">num_tweets</span><span class="p">:</span>
            <span class="k">break</span>
        <span class="n">attributes_container</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tweet</span><span class="o">.</span><span class="n">rawContent</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">attributes_container</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"username"</span><span class="p">:</span> <span class="n">username</span><span class="p">})]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Snowflake](https://docs.llamaindex.ai/en/stable/api_reference/readers/snowflake/)[Next Spotify](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/)
