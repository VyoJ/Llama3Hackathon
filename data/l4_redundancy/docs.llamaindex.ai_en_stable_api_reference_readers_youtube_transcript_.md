Title: Youtube transcript - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/

Markdown Content:
Youtube transcript - LlamaIndex


YoutubeTranscriptReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/#llama_index.readers.youtube_transcript.YoutubeTranscriptReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Youtube Transcript reader.

Source code in `llama-index-integrations/readers/llama-index-readers-youtube-transcript/llama_index/readers/youtube_transcript/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">YoutubeTranscriptReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Youtube Transcript reader."""</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the name identifier of the class."""</span>
        <span class="k">return</span> <span class="s2">"YoutubeTranscriptReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">ytlinks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">languages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"en"</span><span class="p">],</span>
        <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            pages (List[str]): List of youtube links \</span>
<span class="sd">                for which transcripts are to be read.</span>

<span class="sd">        """</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">link</span> <span class="ow">in</span> <span class="n">ytlinks</span><span class="p">:</span>
            <span class="n">video_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_video_id</span><span class="p">(</span><span class="n">link</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">video_id</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Supplied url </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2"> is not a supported youtube URL."</span>
                    <span class="s2">"Supported formats include:"</span>
                    <span class="s2">"  youtube.com/watch?v=</span><span class="se">\\</span><span class="s2">{video_id</span><span class="se">\\</span><span class="s2">} "</span>
                    <span class="s2">"(with or without 'www.')</span><span class="se">\n</span><span class="s2">"</span>
                    <span class="s2">"  youtube.com/embed?v=</span><span class="se">\\</span><span class="s2">{video_id</span><span class="se">\\</span><span class="s2">} "</span>
                    <span class="s2">"(with or without 'www.')</span><span class="se">\n</span><span class="s2">"</span>
                    <span class="s2">"  youtu.be/{video_id</span><span class="se">\\</span><span class="s2">} (never includes www subdomain)"</span>
                <span class="p">)</span>
            <span class="n">transcript_chunks</span> <span class="o">=</span> <span class="n">YouTubeTranscriptApi</span><span class="o">.</span><span class="n">get_transcript</span><span class="p">(</span>
                <span class="n">video_id</span><span class="p">,</span> <span class="n">languages</span><span class="o">=</span><span class="n">languages</span>
            <span class="p">)</span>
            <span class="n">chunk_text</span> <span class="o">=</span> <span class="p">[</span><span class="n">chunk</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">transcript_chunks</span><span class="p">]</span>
            <span class="n">transcript</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">chunk_text</span><span class="p">)</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">video_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"video_id"</span><span class="p">:</span> <span class="n">video_id</span><span class="p">}</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_extract_video_id</span><span class="p">(</span><span class="n">yt_link</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">pattern</span> <span class="ow">in</span> <span class="n">YOUTUBE_URL_PATTERNS</span><span class="p">:</span>
            <span class="n">match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="n">yt_link</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">match</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>

        <span class="c1"># return None if no match is found</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/#llama_index.readers.youtube_transcript.YoutubeTranscriptReader.class_name "Permanent link")

```
class_name() -> str
```

Get the name identifier of the class.

Source code in `llama-index-integrations/readers/llama-index-readers-youtube-transcript/llama_index/readers/youtube_transcript/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the name identifier of the class."""</span>
    <span class="k">return</span> <span class="s2">"YoutubeTranscriptReader"</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/#llama_index.readers.youtube_transcript.YoutubeTranscriptReader.load_data "Permanent link")

```
load_data(ytlinks: List[str], languages: Optional[List[str]] = ['en'], **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pages` | `List[str]` | 
List of youtube links for which transcripts are to be read.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-youtube-transcript/llama_index/readers/youtube_transcript/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
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
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">ytlinks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="n">languages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"en"</span><span class="p">],</span>
    <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        pages (List[str]): List of youtube links \</span>
<span class="sd">            for which transcripts are to be read.</span>

<span class="sd">    """</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">link</span> <span class="ow">in</span> <span class="n">ytlinks</span><span class="p">:</span>
        <span class="n">video_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_video_id</span><span class="p">(</span><span class="n">link</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">video_id</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Supplied url </span><span class="si">{</span><span class="n">link</span><span class="si">}</span><span class="s2"> is not a supported youtube URL."</span>
                <span class="s2">"Supported formats include:"</span>
                <span class="s2">"  youtube.com/watch?v=</span><span class="se">\\</span><span class="s2">{video_id</span><span class="se">\\</span><span class="s2">} "</span>
                <span class="s2">"(with or without 'www.')</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"  youtube.com/embed?v=</span><span class="se">\\</span><span class="s2">{video_id</span><span class="se">\\</span><span class="s2">} "</span>
                <span class="s2">"(with or without 'www.')</span><span class="se">\n</span><span class="s2">"</span>
                <span class="s2">"  youtu.be/{video_id</span><span class="se">\\</span><span class="s2">} (never includes www subdomain)"</span>
            <span class="p">)</span>
        <span class="n">transcript_chunks</span> <span class="o">=</span> <span class="n">YouTubeTranscriptApi</span><span class="o">.</span><span class="n">get_transcript</span><span class="p">(</span>
            <span class="n">video_id</span><span class="p">,</span> <span class="n">languages</span><span class="o">=</span><span class="n">languages</span>
        <span class="p">)</span>
        <span class="n">chunk_text</span> <span class="o">=</span> <span class="p">[</span><span class="n">chunk</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">transcript_chunks</span><span class="p">]</span>
        <span class="n">transcript</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">chunk_text</span><span class="p">)</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">video_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"video_id"</span><span class="p">:</span> <span class="n">video_id</span><span class="p">}</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Youtube metadata](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_metadata/)[Next Zendesk](https://docs.llamaindex.ai/en/stable/api_reference/readers/zendesk/)
