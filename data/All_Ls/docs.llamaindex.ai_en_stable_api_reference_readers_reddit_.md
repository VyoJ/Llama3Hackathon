Title: Reddit - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/

Markdown Content:
Reddit - LlamaIndex


RedditReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/#llama_index.readers.reddit.RedditReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Subreddit post and top-level comments reader for Reddit.

Source code in `llama-index-integrations/readers/llama-index-readers-reddit/llama_index/readers/reddit/base.py`

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
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RedditReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Subreddit post and top-level comments reader for Reddit.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">subreddits</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">search_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">post_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Load text from relevant posts and top-level comments in subreddit(s), given keyword(s) for search.</span>

<span class="sd">        Args:</span>
<span class="sd">            subreddits (List[str]): List of subreddits you'd like to read from</span>
<span class="sd">            search_keys (List[str]): List of keywords you'd like to use to search from subreddit(s)</span>
<span class="sd">            post_limit (Optional[int]): Maximum number of posts per subreddit you'd like to read from, defaults to 10</span>

<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">os</span>

        <span class="kn">import</span> <span class="nn">praw</span>
        <span class="kn">from</span> <span class="nn">praw.models</span> <span class="kn">import</span> <span class="n">MoreComments</span>

        <span class="n">reddit</span> <span class="o">=</span> <span class="n">praw</span><span class="o">.</span><span class="n">Reddit</span><span class="p">(</span>
            <span class="n">client_id</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_CLIENT_ID"</span><span class="p">),</span>
            <span class="n">client_secret</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_CLIENT_SECRET"</span><span class="p">),</span>
            <span class="n">user_agent</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_USER_AGENT"</span><span class="p">),</span>
            <span class="n">username</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_USERNAME"</span><span class="p">),</span>
            <span class="n">password</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_PASSWORD"</span><span class="p">),</span>
        <span class="p">)</span>

        <span class="n">posts</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">sr</span> <span class="ow">in</span> <span class="n">subreddits</span><span class="p">:</span>
            <span class="n">ml_subreddit</span> <span class="o">=</span> <span class="n">reddit</span><span class="o">.</span><span class="n">subreddit</span><span class="p">(</span><span class="n">sr</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">kw</span> <span class="ow">in</span> <span class="n">search_keys</span><span class="p">:</span>
                <span class="n">relevant_posts</span> <span class="o">=</span> <span class="n">ml_subreddit</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">kw</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">post_limit</span><span class="p">)</span>

                <span class="k">for</span> <span class="n">post</span> <span class="ow">in</span> <span class="n">relevant_posts</span><span class="p">:</span>
                    <span class="n">posts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">post</span><span class="o">.</span><span class="n">selftext</span><span class="p">))</span>
                    <span class="k">for</span> <span class="n">top_level_comment</span> <span class="ow">in</span> <span class="n">post</span><span class="o">.</span><span class="n">comments</span><span class="p">:</span>
                        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">top_level_comment</span><span class="p">,</span> <span class="n">MoreComments</span><span class="p">):</span>
                            <span class="k">continue</span>
                        <span class="n">posts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">top_level_comment</span><span class="o">.</span><span class="n">body</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">posts</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/#llama_index.readers.reddit.RedditReader.load_data "Permanent link")

```
load_data(subreddits: List[str], search_keys: List[str], post_limit: Optional[int] = [10]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load text from relevant posts and top-level comments in subreddit(s), given keyword(s) for search.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `subreddits` | `List[str]` | 
List of subreddits you'd like to read from



 | _required_ |
| `search_keys` | `List[str]` | 

List of keywords you'd like to use to search from subreddit(s)



 | _required_ |
| `post_limit` | `Optional[int]` | 

Maximum number of posts per subreddit you'd like to read from, defaults to 10



 | `[10]` |

Source code in `llama-index-integrations/readers/llama-index-readers-reddit/llama_index/readers/reddit/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
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
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">subreddits</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">search_keys</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">post_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Load text from relevant posts and top-level comments in subreddit(s), given keyword(s) for search.</span>

<span class="sd">    Args:</span>
<span class="sd">        subreddits (List[str]): List of subreddits you'd like to read from</span>
<span class="sd">        search_keys (List[str]): List of keywords you'd like to use to search from subreddit(s)</span>
<span class="sd">        post_limit (Optional[int]): Maximum number of posts per subreddit you'd like to read from, defaults to 10</span>

<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">os</span>

    <span class="kn">import</span> <span class="nn">praw</span>
    <span class="kn">from</span> <span class="nn">praw.models</span> <span class="kn">import</span> <span class="n">MoreComments</span>

    <span class="n">reddit</span> <span class="o">=</span> <span class="n">praw</span><span class="o">.</span><span class="n">Reddit</span><span class="p">(</span>
        <span class="n">client_id</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_CLIENT_ID"</span><span class="p">),</span>
        <span class="n">client_secret</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_CLIENT_SECRET"</span><span class="p">),</span>
        <span class="n">user_agent</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_USER_AGENT"</span><span class="p">),</span>
        <span class="n">username</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_USERNAME"</span><span class="p">),</span>
        <span class="n">password</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"REDDIT_PASSWORD"</span><span class="p">),</span>
    <span class="p">)</span>

    <span class="n">posts</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">sr</span> <span class="ow">in</span> <span class="n">subreddits</span><span class="p">:</span>
        <span class="n">ml_subreddit</span> <span class="o">=</span> <span class="n">reddit</span><span class="o">.</span><span class="n">subreddit</span><span class="p">(</span><span class="n">sr</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">kw</span> <span class="ow">in</span> <span class="n">search_keys</span><span class="p">:</span>
            <span class="n">relevant_posts</span> <span class="o">=</span> <span class="n">ml_subreddit</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">kw</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">post_limit</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">post</span> <span class="ow">in</span> <span class="n">relevant_posts</span><span class="p">:</span>
                <span class="n">posts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">post</span><span class="o">.</span><span class="n">selftext</span><span class="p">))</span>
                <span class="k">for</span> <span class="n">top_level_comment</span> <span class="ow">in</span> <span class="n">post</span><span class="o">.</span><span class="n">comments</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">top_level_comment</span><span class="p">,</span> <span class="n">MoreComments</span><span class="p">):</span>
                        <span class="k">continue</span>
                    <span class="n">posts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">top_level_comment</span><span class="o">.</span><span class="n">body</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">posts</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Readwise](https://docs.llamaindex.ai/en/stable/api_reference/readers/readwise/)[Next Remote](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/)
