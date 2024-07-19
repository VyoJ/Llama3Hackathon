Title: Twitter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/

Markdown Content:
Twitter - LlamaIndex


TwitterTweetReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/#llama_index.readers.twitter.TwitterTweetReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Twitter tweets reader.

Read tweets of user twitter handle.

Check 'https://developer.twitter.com/en/docs/twitter-api/ getting-started/getting-access-to-the-twitter-api' on how to get access to twitter API.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bearer_token` | `str` | 
bearer\_token that you get from twitter API.



 | _required_ |
| `num_tweets` | `Optional[int]` | 

Number of tweets for each user twitter handle. Default is 100 tweets.



 | `100` |

Source code in `llama-index-integrations/readers/llama-index-readers-twitter/llama_index/readers/twitter/base.py`

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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TwitterTweetReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Twitter tweets reader.</span>

<span class="sd">    Read tweets of user twitter handle.</span>

<span class="sd">    Check 'https://developer.twitter.com/en/docs/twitter-api/\</span>
<span class="sd">        getting-started/getting-access-to-the-twitter-api' \</span>
<span class="sd">        on how to get access to twitter API.</span>

<span class="sd">    Args:</span>
<span class="sd">        bearer_token (str): bearer_token that you get from twitter API.</span>
<span class="sd">        num_tweets (Optional[int]): Number of tweets for each user twitter handle.\</span>
<span class="sd">            Default is 100 tweets.</span>
<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">bearer_token</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">num_tweets</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">bearer_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">num_tweets</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">num_tweets</span><span class="o">=</span><span class="n">num_tweets</span><span class="p">,</span>
            <span class="n">bearer_token</span><span class="o">=</span><span class="n">bearer_token</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"TwitterTweetReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">twitterhandles</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">num_tweets</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load tweets of twitter handles.</span>

<span class="sd">        Args:</span>
<span class="sd">            twitterhandles (List[str]): List of user twitter handles to read tweets.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">tweepy</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`tweepy` package not found, please run `pip install tweepy`"</span>
            <span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">tweepy</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="n">bearer_token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">bearer_token</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">username</span> <span class="ow">in</span> <span class="n">twitterhandles</span><span class="p">:</span>
            <span class="c1"># tweets = api.user_timeline(screen_name=user, count=self.num_tweets)</span>
            <span class="n">user</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="n">username</span><span class="p">)</span>
            <span class="n">tweets</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_users_tweets</span><span class="p">(</span>
                <span class="n">user</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">max_results</span><span class="o">=</span><span class="n">num_tweets</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_tweets</span>
            <span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="s2">" "</span>
            <span class="k">for</span> <span class="n">tweet</span> <span class="ow">in</span> <span class="n">tweets</span><span class="o">.</span><span class="n">data</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="o">+</span> <span class="n">tweet</span><span class="o">.</span><span class="n">text</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">username</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/#llama_index.readers.twitter.TwitterTweetReader.load_data "Permanent link")

```
load_data(twitterhandles: List[str], num_tweets: Optional[int] = None, **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load tweets of twitter handles.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `twitterhandles` | `List[str]` | 
List of user twitter handles to read tweets.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-twitter/llama_index/readers/twitter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">twitterhandles</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">num_tweets</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load tweets of twitter handles.</span>

<span class="sd">    Args:</span>
<span class="sd">        twitterhandles (List[str]): List of user twitter handles to read tweets.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">tweepy</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"`tweepy` package not found, please run `pip install tweepy`"</span>
        <span class="p">)</span>

    <span class="n">client</span> <span class="o">=</span> <span class="n">tweepy</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="n">bearer_token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">bearer_token</span><span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">username</span> <span class="ow">in</span> <span class="n">twitterhandles</span><span class="p">:</span>
        <span class="c1"># tweets = api.user_timeline(screen_name=user, count=self.num_tweets)</span>
        <span class="n">user</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="n">username</span><span class="p">)</span>
        <span class="n">tweets</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_users_tweets</span><span class="p">(</span>
            <span class="n">user</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">max_results</span><span class="o">=</span><span class="n">num_tweets</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_tweets</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="s2">" "</span>
        <span class="k">for</span> <span class="n">tweet</span> <span class="ow">in</span> <span class="n">tweets</span><span class="o">.</span><span class="n">data</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="o">+</span> <span class="n">tweet</span><span class="o">.</span><span class="n">text</span> <span class="o">+</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">username</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Trello](https://docs.llamaindex.ai/en/stable/api_reference/readers/trello/)[Next Txtai](https://docs.llamaindex.ai/en/stable/api_reference/readers/txtai/)
