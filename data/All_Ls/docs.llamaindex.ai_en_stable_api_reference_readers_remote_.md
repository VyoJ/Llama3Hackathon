Title: Remote - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/

Markdown Content:
Remote - LlamaIndex


Init file.

RemoteReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/#llama_index.readers.remote.RemoteReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any remote page or file.

Source code in `llama-index-integrations/readers/llama-index-readers-remote/llama_index/readers/remote/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
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
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RemoteReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any remote page or file."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_is_youtube_video</span><span class="p">(</span><span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="c1"># TODO create more global method for detecting all types</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Returns True if the given URL is a video on YouTube, False otherwise.</span>
<span class="sd">        """</span>
        <span class="c1"># Regular expression pattern to match YouTube video URLs</span>
        <span class="n">youtube_pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?([^\s&amp;]+)"</span>

        <span class="c1"># Match the pattern against the URL</span>
        <span class="n">match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">youtube_pattern</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>

        <span class="c1"># If there's a match, it's a YouTube video URL</span>
        <span class="k">if</span> <span class="n">match</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">True</span>

        <span class="c1"># Otherwise, it's not a YouTube video URL</span>
        <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse whatever is at the URL."""</span>
        <span class="kn">import</span> <span class="nn">tempfile</span>
        <span class="kn">from</span> <span class="nn">urllib.parse</span> <span class="kn">import</span> <span class="n">urlparse</span>
        <span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">Request</span><span class="p">,</span> <span class="n">urlopen</span>

        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Source"</span><span class="p">:</span> <span class="n">url</span><span class="p">}</span>

        <span class="n">req</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"User-Agent"</span><span class="p">:</span> <span class="s2">"Magic Browser"</span><span class="p">})</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span>
        <span class="n">url_type</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">info</span><span class="p">()</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">url_type</span> <span class="o"></span> <span class="s2">"text/plain"</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8-sig"</span><span class="p">))</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">result</span><span class="p">])</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)]</span>
        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_youtube_video</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
            <span class="n">youtube_reader</span> <span class="o">=</span> <span class="n">YoutubeTranscriptReader</span><span class="p">()</span>
            <span class="c1"># TODO should we have another language, like english / french?</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="n">youtube_reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">([</span><span class="n">url</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">suffix</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">urlparse</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">suffix</span>
            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
                <span class="n">filepath</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">temp_dir</span><span class="si">}</span><span class="s2">/temp</span><span class="si">{</span><span class="n">suffix</span><span class="si">}</span><span class="s2">"</span>
                <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">output</span><span class="p">:</span>
                    <span class="n">output</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
                <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
                    <span class="n">temp_dir</span><span class="p">,</span>
                    <span class="n">file_metadata</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="n">extra_info</span><span class="p">),</span>
                    <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">documents</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/#llama_index.readers.remote.RemoteReader.load_data "Permanent link")

```
load_data(url: str) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse whatever is at the URL.

Source code in `llama-index-integrations/readers/llama-index-readers-remote/llama_index/readers/remote/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">50</span>
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
<span class="normal">81</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse whatever is at the URL."""</span>
    <span class="kn">import</span> <span class="nn">tempfile</span>
    <span class="kn">from</span> <span class="nn">urllib.parse</span> <span class="kn">import</span> <span class="n">urlparse</span>
    <span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">Request</span><span class="p">,</span> <span class="n">urlopen</span>

    <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Source"</span><span class="p">:</span> <span class="n">url</span><span class="p">}</span>

    <span class="n">req</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="s2">"User-Agent"</span><span class="p">:</span> <span class="s2">"Magic Browser"</span><span class="p">})</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span>
    <span class="n">url_type</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">info</span><span class="p">()</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span>
    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">url_type</span> <span class="o"></span> <span class="s2">"text/plain"</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8-sig"</span><span class="p">))</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">result</span><span class="p">])</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)]</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_youtube_video</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
        <span class="n">youtube_reader</span> <span class="o">=</span> <span class="n">YoutubeTranscriptReader</span><span class="p">()</span>
        <span class="c1"># TODO should we have another language, like english / french?</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="n">youtube_reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">([</span><span class="n">url</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">suffix</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">urlparse</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">suffix</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="n">filepath</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">temp_dir</span><span class="si">}</span><span class="s2">/temp</span><span class="si">{</span><span class="n">suffix</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">output</span><span class="p">:</span>
                <span class="n">output</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
            <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
                <span class="n">temp_dir</span><span class="p">,</span>
                <span class="n">file_metadata</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="n">extra_info</span><span class="p">),</span>
                <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Reddit](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/)[Next Remote depth](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote_depth/)
