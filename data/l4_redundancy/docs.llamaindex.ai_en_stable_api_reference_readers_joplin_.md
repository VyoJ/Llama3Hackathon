Title: Joplin - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/

Markdown Content:
Joplin - LlamaIndex


JoplinReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/#llama_index.readers.joplin.JoplinReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Reader that fetches notes from Joplin.

In order to use this reader, you need to have Joplin running with the Web Clipper enabled (look for "Web Clipper" in the app settings).

To get the access token, you need to go to the Web Clipper options and under "Advanced Options" you will find the access token. You may provide it as an argument or set the JOPLIN\_ACCESS\_TOKEN environment variable.

You can find more information about the Web Clipper service here: https://joplinapp.org/clipper/

Source code in `llama-index-integrations/readers/llama-index-readers-joplin/llama_index/readers/joplin/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">JoplinReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Reader that fetches notes from Joplin.</span>

<span class="sd">    In order to use this reader, you need to have Joplin running with the</span>
<span class="sd">    Web Clipper enabled (look for "Web Clipper" in the app settings).</span>

<span class="sd">    To get the access token, you need to go to the Web Clipper options and</span>
<span class="sd">    under "Advanced Options" you will find the access token. You may provide</span>
<span class="sd">    it as an argument or set the JOPLIN_ACCESS_TOKEN environment variable.</span>

<span class="sd">    You can find more information about the Web Clipper service here:</span>
<span class="sd">    https://joplinapp.org/clipper/</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">access_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">parse_markdown</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">41184</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"localhost"</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize a new instance of JoplinReader.</span>

<span class="sd">        Args:</span>
<span class="sd">            access_token (Optional[str]): The access token for Joplin's Web Clipper service.</span>
<span class="sd">                If not provided, the JOPLIN_ACCESS_TOKEN environment variable is used. Default is None.</span>
<span class="sd">            parse_markdown (bool): Whether to parse the markdown content of the notes using MarkdownReader. Default is True.</span>
<span class="sd">            port (int): The port on which Joplin's Web Clipper service is running. Default is 41184.</span>
<span class="sd">            host (str): The host on which Joplin's Web Clipper service is running. Default is "localhost".</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">parse_markdown</span> <span class="o">=</span> <span class="n">parse_markdown</span>
        <span class="k">if</span> <span class="n">parse_markdown</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">parser</span> <span class="o">=</span> <span class="n">MarkdownReader</span><span class="p">()</span>

        <span class="n">access_token</span> <span class="o">=</span> <span class="n">access_token</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_token_from_env</span><span class="p">()</span>
        <span class="n">base_url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"http://</span><span class="si">{</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s2">"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_get_note_url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/notes?token=</span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">"</span>
            <span class="s2">"&amp;fields=id,parent_id,title,body,created_time,updated_time&amp;page=</span><span class="si">{page}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_get_folder_url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/folders/</span><span class="se">{{</span><span class="s2">id</span><span class="se">}}</span><span class="s2">?token=</span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">&amp;fields=title"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_get_tag_url</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">base_url</span><span class="si">}</span><span class="s2">/notes/</span><span class="se">{{</span><span class="s2">id</span><span class="se">}}</span><span class="s2">/tags?token=</span><span class="si">{</span><span class="n">access_token</span><span class="si">}</span><span class="s2">&amp;fields=title"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_token_from_env</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"JOPLIN_ACCESS_TOKEN"</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"JOPLIN_ACCESS_TOKEN"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"You need to provide an access token to use the Joplin reader. You may"</span>
                <span class="s2">" provide it as an argument or set the JOPLIN_ACCESS_TOKEN environment"</span>
                <span class="s2">" variable."</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_notes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">has_more</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="n">page</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="k">while</span> <span class="n">has_more</span><span class="p">:</span>
            <span class="n">req_note</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_note_url</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">page</span><span class="o">=</span><span class="n">page</span><span class="p">))</span>
            <span class="k">with</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req_note</span><span class="p">)</span> <span class="k">as</span> <span class="n">response</span><span class="p">:</span>
                <span class="n">json_data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>
                <span class="k">for</span> <span class="n">note</span> <span class="ow">in</span> <span class="n">json_data</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]:</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="s2">"source"</span><span class="p">:</span> <span class="n">LINK_NOTE_TEMPLATE</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">note</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]),</span>
                        <span class="s2">"folder"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_folder</span><span class="p">(</span><span class="n">note</span><span class="p">[</span><span class="s2">"parent_id"</span><span class="p">]),</span>
                        <span class="s2">"tags"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_tags</span><span class="p">(</span><span class="n">note</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]),</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">note</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                        <span class="s2">"created_time"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_convert_date</span><span class="p">(</span><span class="n">note</span><span class="p">[</span><span class="s2">"created_time"</span><span class="p">]),</span>
                        <span class="s2">"updated_time"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_convert_date</span><span class="p">(</span><span class="n">note</span><span class="p">[</span><span class="s2">"updated_time"</span><span class="p">]),</span>
                    <span class="p">}</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_markdown</span><span class="p">:</span>
                        <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span>
                            <span class="kc">None</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">note</span><span class="p">[</span><span class="s2">"body"</span><span class="p">],</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span>
                        <span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="k">yield</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">note</span><span class="p">[</span><span class="s2">"body"</span><span class="p">],</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>

                <span class="n">has_more</span> <span class="o">=</span> <span class="n">json_data</span><span class="p">[</span><span class="s2">"has_more"</span><span class="p">]</span>
                <span class="n">page</span> <span class="o">+=</span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">_get_folder</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">folder_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">req_folder</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_folder_url</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">folder_id</span><span class="p">))</span>
        <span class="k">with</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req_folder</span><span class="p">)</span> <span class="k">as</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">json_data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>
            <span class="k">return</span> <span class="n">json_data</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">note_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">req_tag</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_tag_url</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">note_id</span><span class="p">))</span>
        <span class="k">with</span> <span class="n">urllib</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req_tag</span><span class="p">)</span> <span class="k">as</span> <span class="n">response</span><span class="p">:</span>
            <span class="n">json_data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>
            <span class="k">return</span> <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">tag</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">json_data</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]])</span>

    <span class="k">def</span> <span class="nf">_convert_date</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">date</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">date</span> <span class="o">/</span> <span class="mi">1000</span><span class="p">)</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">lazy_load</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">yield from</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_notes</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lazy_load</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Jira](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/)[Next Json](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/)
