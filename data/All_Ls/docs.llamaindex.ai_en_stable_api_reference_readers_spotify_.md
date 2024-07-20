Title: Spotify - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/

Markdown Content:
Spotify - LlamaIndex


SpotifyReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/#llama_index.readers.spotify.SpotifyReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Spotify Reader.

Read a user's saved albums, tracks, or playlists from Spotify.

Source code in `llama-index-integrations/readers/llama-index-readers-spotify/llama_index/readers/spotify/base.py`

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
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SpotifyReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Spotify Reader.</span>

<span class="sd">    Read a user's saved albums, tracks, or playlists from Spotify.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"albums"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from a user's Spotify account.</span>

<span class="sd">        Args:</span>
<span class="sd">            collections (Optional[str]): "albums", "tracks", or "playlists"</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">spotipy</span>
        <span class="kn">from</span> <span class="nn">spotipy.oauth2</span> <span class="kn">import</span> <span class="n">SpotifyOAuth</span>

        <span class="n">scope</span> <span class="o">=</span> <span class="s2">"user-library-read"</span>
        <span class="n">sp</span> <span class="o">=</span> <span class="n">spotipy</span><span class="o">.</span><span class="n">Spotify</span><span class="p">(</span><span class="n">auth_manager</span><span class="o">=</span><span class="n">SpotifyOAuth</span><span class="p">(</span><span class="n">scope</span><span class="o">=</span><span class="n">scope</span><span class="p">))</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">collection</span> <span class="o"></span> <span class="s2">"tracks"</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">sp</span><span class="o">.</span><span class="n">current_user_saved_tracks</span><span class="p">()</span>
            <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
                <span class="n">track</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"track"</span><span class="p">]</span>
                <span class="n">track_name</span> <span class="o">=</span> <span class="n">track</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
                <span class="n">artist_name</span> <span class="o">=</span> <span class="n">track</span><span class="p">[</span><span class="s2">"artists"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
                <span class="n">artist_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Track </span><span class="si">{</span><span class="n">track_name</span><span class="si">}</span><span class="s2"> by Artist </span><span class="si">{</span><span class="n">artist_name</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">artist_string</span><span class="p">))</span>
        <span class="k">elif</span> <span class="n">collection</span> <span class="o"></span> <span class="s2">"albums"</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">sp</span><span class="o">.</span><span class="n">current_user_saved_albums</span><span class="p">()</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
            <span class="n">album</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"album"</span><span class="p">]</span>
            <span class="n">album_name</span> <span class="o">=</span> <span class="n">album</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="n">artist_name</span> <span class="o">=</span> <span class="n">album</span><span class="p">[</span><span class="s2">"artists"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="n">album_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Album </span><span class="si">{</span><span class="n">album_name</span><span class="si">}</span><span class="s2"> by Artist </span><span class="si">{</span><span class="n">artist_name</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">album_string</span><span class="p">))</span>
    <span class="k">elif</span> <span class="n">collection</span> <span class="o"></span> <span class="s2">"playlists"</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">sp</span><span class="o">.</span><span class="n">current_user_playlists</span><span class="p">()</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
            <span class="n">playlist_name</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="n">owner_name</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s2">"owner"</span><span class="p">][</span><span class="s2">"display_name"</span><span class="p">]</span>
            <span class="n">playlist_string</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Playlist </span><span class="si">{</span><span class="n">playlist_name</span><span class="si">}</span><span class="s2"> created by </span><span class="si">{</span><span class="n">owner_name</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">playlist_string</span><span class="p">))</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Invalid collection parameter value. Allowed values are 'albums',"</span>
            <span class="s2">" 'tracks', or 'playlists'."</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Snscrape twitter](https://docs.llamaindex.ai/en/stable/api_reference/readers/snscrape_twitter/)[Next Stackoverflow](https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/)
