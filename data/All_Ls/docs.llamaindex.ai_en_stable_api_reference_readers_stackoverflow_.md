Title: Stackoverflow - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/

Markdown Content:
Stackoverflow - LlamaIndex


StackoverflowReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/#llama_index.readers.stackoverflow.StackoverflowReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Source code in `llama-index-integrations/readers/llama-index-readers-stackoverflow/llama_index/readers/stackoverflow/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 83</span>
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
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StackoverflowReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">team_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">cache_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"STACKOVERFLOW_PAT"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_team_name</span> <span class="o">=</span> <span class="n">team_name</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"STACKOVERFLOW_TEAM_NAME"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_last_index_time</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># TODO</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span> <span class="o">=</span> <span class="n">cache_dir</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span><span class="p">:</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">page</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">doc_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"posts"</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">50</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">has_more</span> <span class="o">=</span> <span class="kc">True</span>

        <span class="k">while</span> <span class="n">has_more</span><span class="p">:</span>
            <span class="n">url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_url</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">doc_type</span><span class="p">)</span>
            <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"X-API-Access-Token"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">}</span>
            <span class="n">fp</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">doc_type</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">page</span><span class="si">}</span><span class="s2">.json"</span><span class="p">)</span>
            <span class="n">response</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
                        <span class="n">response</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">response</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">rate_limited_get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="p">)</span>
                <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span><span class="p">:</span>
                    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span>
                        <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_cache_dir</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">doc_type</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">page</span><span class="si">}</span><span class="s2">.json"</span><span class="p">),</span> <span class="s2">"w"</span>
                    <span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
                    <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Wrote </span><span class="si">{</span><span class="n">fp</span><span class="si">}</span><span class="s2"> to cache"</span><span class="p">)</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="n">has_more</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"has_more"</span><span class="p">]</span>
            <span class="n">items</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"items"</span><span class="p">]</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Fetched </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">items</span><span class="p">)</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">doc_type</span><span class="si">}</span><span class="s2"> from Stack Overflow"</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">item_dict</span> <span class="ow">in</span> <span class="n">items</span><span class="p">:</span>
                <span class="n">owner_fields</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">if</span> <span class="s2">"owner"</span> <span class="ow">in</span> <span class="n">item_dict</span><span class="p">:</span>
                    <span class="n">owner_fields</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="sa">f</span><span class="s2">"owner_</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">"</span><span class="p">:</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">item_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"owner"</span><span class="p">)</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                    <span class="p">}</span>
                <span class="k">if</span> <span class="s2">"title"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">item_dict</span><span class="p">:</span>
                    <span class="n">item_dict</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="o">=</span> <span class="n">item_dict</span><span class="p">[</span><span class="s2">"link"</span><span class="p">]</span>
                <span class="n">post</span> <span class="o">=</span> <span class="n">StackOverflowPost</span><span class="p">(</span><span class="o">**</span><span class="n">item_dict</span><span class="p">,</span> <span class="o">**</span><span class="n">owner_fields</span><span class="p">)</span>
                <span class="c1"># TODO: filter out old posts</span>
                <span class="c1"># last_modified = datetime.fromtimestamp(post.last_edit_date or post.last_activity_date)</span>
                <span class="c1"># if last_modified &lt; self._last_index_time:</span>
                <span class="c1">#     return data</span>

                <span class="n">post_document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">post</span><span class="o">.</span><span class="n">body_markdown</span><span class="p">,</span>
                    <span class="n">doc_id</span><span class="o">=</span><span class="n">post</span><span class="o">.</span><span class="n">post_id</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
                        <span class="s2">"author"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">owner_display_name</span><span class="p">,</span>
                        <span class="s2">"timestamp"</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">post</span><span class="o">.</span><span class="n">creation_date</span><span class="p">),</span>
                        <span class="s2">"location"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">link</span><span class="p">,</span>
                        <span class="s2">"url"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">link</span><span class="p">,</span>
                        <span class="s2">"author_image_url"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">owner_profile_image</span><span class="p">,</span>
                        <span class="s2">"type"</span><span class="p">:</span> <span class="n">post</span><span class="o">.</span><span class="n">post_type</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
                <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">post_document</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">has_more</span><span class="p">:</span>
                <span class="n">page</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="k">return</span> <span class="n">data</span>

    <span class="k">def</span> <span class="nf">build_url</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">doc_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">team_fragment</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;team=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_team_name</span><span class="si">}</span><span class="s2">"</span>
        <span class="c1"># not sure if this filter is shared globally, or only to a particular team</span>
        <span class="n">filter_fragment</span> <span class="o">=</span> <span class="s2">"&amp;filter=!nOedRLbqzB"</span>
        <span class="n">page_fragment</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"&amp;page=</span><span class="si">{</span><span class="n">page</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"https://api.stackoverflowteams.com/2.3/</span><span class="si">{</span><span class="n">doc_type</span><span class="si">}</span><span class="s2">?</span><span class="si">{</span><span class="n">team_fragment</span><span class="si">}{</span><span class="n">filter_fragment</span><span class="si">}{</span><span class="n">page_fragment</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Spotify](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/)[Next Steamship](https://docs.llamaindex.ai/en/stable/api_reference/readers/steamship/)
