Title: Imdb review - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/

Markdown Content:
Imdb review - LlamaIndex


IMDBReviews [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/#llama_index.readers.imdb_review.IMDBReviews "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Source code in `llama-index-integrations/readers/llama-index-readers-imdb-review/llama_index/readers/imdb_review/base.py`

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
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IMDBReviews</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">movie_name_year</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">webdriver_engine</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"google"</span><span class="p">,</span>
        <span class="n">generate_csv</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">multithreading</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_workers</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">reviews_folder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"movie_reviews"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Get the IMDB reviews of a movie.</span>

<span class="sd">        Args:</span>
<span class="sd">            movie_name_year (str): movie name alongwith year</span>
<span class="sd">            webdriver_engine (str, optional): webdriver engine to use. Defaults to "google".</span>
<span class="sd">            generate_csv (bool, optional): whether to generate csv. Defaults to False.</span>
<span class="sd">            multithreading (bool, optional): whether to use multithreading. Defaults to False.</span>
<span class="sd">            max_workers (int, optional): number of workers if you are using multithreading. Defaults to 0.</span>
<span class="sd">        """</span>
        <span class="k">assert</span> <span class="n">webdriver_engine</span> <span class="ow">in</span> <span class="p">[</span>
            <span class="s2">"google"</span><span class="p">,</span>
            <span class="s2">"edge"</span><span class="p">,</span>
            <span class="s2">"firefox"</span><span class="p">,</span>
        <span class="p">],</span> <span class="s2">"The webdriver should be in ['google','edge','firefox']"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">movie_name_year</span> <span class="o">=</span> <span class="n">movie_name_year</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">webdriver_engine</span> <span class="o">=</span> <span class="n">webdriver_engine</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">generate_csv</span> <span class="o">=</span> <span class="n">generate_csv</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">multithreading</span> <span class="o">=</span> <span class="n">multithreading</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_workers</span> <span class="o">=</span> <span class="n">max_workers</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reviews_folder</span> <span class="o">=</span> <span class="n">reviews_folder</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Scrapes the data from the IMDB website movie reviews.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: document object in llama index with date and rating as extra information</span>
<span class="sd">        """</span>
        <span class="p">(</span>
            <span class="n">reviews_date</span><span class="p">,</span>
            <span class="n">reviews_title</span><span class="p">,</span>
            <span class="n">reviews_comment</span><span class="p">,</span>
            <span class="n">reviews_rating</span><span class="p">,</span>
            <span class="n">reviews_link</span><span class="p">,</span>
            <span class="n">review_helpful</span><span class="p">,</span>
            <span class="n">review_total_votes</span><span class="p">,</span>
            <span class="n">review_if_spoiler</span><span class="p">,</span>
        <span class="p">)</span> <span class="o">=</span> <span class="n">main_scraper</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">movie_name_year</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">webdriver_engine</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">generate_csv</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">multithreading</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">max_workers</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">reviews_folder</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">all_docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">reviews_date</span><span class="p">)):</span>
            <span class="n">all_docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">reviews_title</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">reviews_comment</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"date"</span><span class="p">:</span> <span class="n">reviews_date</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                        <span class="s2">"rating"</span><span class="p">:</span> <span class="n">reviews_rating</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                        <span class="s2">"link"</span><span class="p">:</span> <span class="n">reviews_link</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                        <span class="s2">"found_helpful_votes"</span><span class="p">:</span> <span class="n">review_helpful</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                        <span class="s2">"total_votes"</span><span class="p">:</span> <span class="n">review_total_votes</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                        <span class="s2">"spolier"</span><span class="p">:</span> <span class="n">review_if_spoiler</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">all_docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/#llama_index.readers.imdb_review.IMDBReviews.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Scrapes the data from the IMDB website movie reviews.

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: document object in llama index with date and rating as extra information



 |

Source code in `llama-index-integrations/readers/llama-index-readers-imdb-review/llama_index/readers/imdb_review/base.py`

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
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Scrapes the data from the IMDB website movie reviews.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: document object in llama index with date and rating as extra information</span>
<span class="sd">    """</span>
    <span class="p">(</span>
        <span class="n">reviews_date</span><span class="p">,</span>
        <span class="n">reviews_title</span><span class="p">,</span>
        <span class="n">reviews_comment</span><span class="p">,</span>
        <span class="n">reviews_rating</span><span class="p">,</span>
        <span class="n">reviews_link</span><span class="p">,</span>
        <span class="n">review_helpful</span><span class="p">,</span>
        <span class="n">review_total_votes</span><span class="p">,</span>
        <span class="n">review_if_spoiler</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">=</span> <span class="n">main_scraper</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">movie_name_year</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">webdriver_engine</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">generate_csv</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">multithreading</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_workers</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reviews_folder</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">all_docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">reviews_date</span><span class="p">)):</span>
        <span class="n">all_docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">reviews_title</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">reviews_comment</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"date"</span><span class="p">:</span> <span class="n">reviews_date</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="s2">"rating"</span><span class="p">:</span> <span class="n">reviews_rating</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="s2">"link"</span><span class="p">:</span> <span class="n">reviews_link</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="s2">"found_helpful_votes"</span><span class="p">:</span> <span class="n">review_helpful</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="s2">"total_votes"</span><span class="p">:</span> <span class="n">review_total_votes</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                    <span class="s2">"spolier"</span><span class="p">:</span> <span class="n">review_if_spoiler</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">all_docs</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Iceberg](https://docs.llamaindex.ai/en/stable/api_reference/readers/iceberg/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/readers/)
