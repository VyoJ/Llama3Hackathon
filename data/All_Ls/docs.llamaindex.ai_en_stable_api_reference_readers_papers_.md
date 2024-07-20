Title: Papers - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/

Markdown Content:
Papers - LlamaIndex


Init file.

ArxivReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/#llama_index.readers.papers.ArxivReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Arxiv Reader.

Gets a search query, return a list of Documents of the top corresponding scientific papers on Arxiv.

Source code in `llama-index-integrations/readers/llama-index-readers-papers/llama_index/readers/papers/arxiv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
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
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ArxivReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Arxiv Reader.</span>

<span class="sd">    Gets a search query, return a list of Documents of the top corresponding scientific papers on Arxiv.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_hacky_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">some_string</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">(</span><span class="n">some_string</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">papers_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">".papers"</span><span class="p">,</span>
        <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.</span>

<span class="sd">        Args:</span>
<span class="sd">            search_query (str): A topic to search for (e.g. "Artificial Intelligence").</span>
<span class="sd">            papers_dir (Optional[str]): Locally directory to store the papers</span>
<span class="sd">            max_results (Optional[int]): Maximum number of papers to fetch.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">arxiv</span>

        <span class="n">arxiv_search</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">search_query</span><span class="p">,</span>
            <span class="n">id_list</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">max_results</span><span class="o">=</span><span class="n">max_results</span><span class="p">,</span>
            <span class="n">sort_by</span><span class="o">=</span><span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">Relevance</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">search_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">arxiv_search</span><span class="o">.</span><span class="n">results</span><span class="p">())</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Successfully fetched </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">search_results</span><span class="p">)</span><span class="si">}</span><span class="s2"> paperes"</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>

        <span class="n">paper_lookup</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
            <span class="c1"># Hash filename to avoid bad characters in file path</span>
            <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_hacky_hash</span><span class="p">(</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">)</span><span class="si">}</span><span class="s2">.pdf"</span>
            <span class="n">paper_lookup</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
                <span class="s2">"Authors"</span><span class="p">:</span> <span class="p">(</span><span class="s2">", "</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">a</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">paper</span><span class="o">.</span><span class="n">authors</span><span class="p">]),</span>
                <span class="s2">"Date published"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">published</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%m/</span><span class="si">%d</span><span class="s2">/%Y"</span><span class="p">),</span>
                <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">entry_id</span><span class="p">,</span>
                <span class="c1"># "summary": paper.summary</span>
            <span class="p">}</span>
            <span class="n">paper</span><span class="o">.</span><span class="n">download_pdf</span><span class="p">(</span><span class="n">dirpath</span><span class="o">=</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">filename</span><span class="p">)</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Downloading </span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">..."</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">get_paper_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">paper_lookup</span><span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)]</span>

        <span class="n">arxiv_documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
            <span class="n">papers_dir</span><span class="p">,</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_paper_metadata</span><span class="p">,</span>
            <span class="n">exclude_hidden</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>  <span class="c1"># default directory is hidden ".papers"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="c1"># Include extra documents containing the abstracts</span>
        <span class="n">abstract_documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
            <span class="n">d</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"The following is a summary of the paper: </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">Summary:"</span>
                <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">abstract_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="p">))</span>

        <span class="c1"># Delete downloaded papers</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
                <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">f</span><span class="p">))</span>
                <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted file: </span><span class="si">{</span><span class="n">f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted directory: </span><span class="si">{</span><span class="n">papers_dir</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Unable to delete files or directory"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">arxiv_documents</span> <span class="o">+</span> <span class="n">abstract_documents</span>

    <span class="k">def</span> <span class="nf">load_papers_and_abstracts</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">papers_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">".papers"</span><span class="p">,</span>
        <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.</span>

<span class="sd">        Args:</span>
<span class="sd">            search_query (str): A topic to search for (e.g. "Artificial Intelligence").</span>
<span class="sd">            papers_dir (Optional[str]): Locally directory to store the papers</span>
<span class="sd">            max_results (Optional[int]): Maximum number of papers to fetch.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects representing the papers themselves</span>
<span class="sd">            List[Document]: A list of Document objects representing abstracts only</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">arxiv</span>

        <span class="n">arxiv_search</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
            <span class="n">query</span><span class="o">=</span><span class="n">search_query</span><span class="p">,</span>
            <span class="n">id_list</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">max_results</span><span class="o">=</span><span class="n">max_results</span><span class="p">,</span>
            <span class="n">sort_by</span><span class="o">=</span><span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">Relevance</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">search_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">arxiv_search</span><span class="o">.</span><span class="n">results</span><span class="p">())</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Successfully fetched </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">search_results</span><span class="p">)</span><span class="si">}</span><span class="s2"> paperes"</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>

        <span class="n">paper_lookup</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
            <span class="c1"># Hash filename to avoid bad characters in file path</span>
            <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_hacky_hash</span><span class="p">(</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">)</span><span class="si">}</span><span class="s2">.pdf"</span>
            <span class="n">paper_lookup</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
                <span class="s2">"Authors"</span><span class="p">:</span> <span class="p">(</span><span class="s2">", "</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">a</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">paper</span><span class="o">.</span><span class="n">authors</span><span class="p">]),</span>
                <span class="s2">"Date published"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">published</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%m/</span><span class="si">%d</span><span class="s2">/%Y"</span><span class="p">),</span>
                <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">entry_id</span><span class="p">,</span>
                <span class="c1"># "summary": paper.summary</span>
            <span class="p">}</span>
            <span class="n">paper</span><span class="o">.</span><span class="n">download_pdf</span><span class="p">(</span><span class="n">dirpath</span><span class="o">=</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">filename</span><span class="p">)</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Downloading </span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">..."</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">get_paper_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">paper_lookup</span><span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)]</span>

        <span class="n">arxiv_documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
            <span class="n">papers_dir</span><span class="p">,</span>
            <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_paper_metadata</span><span class="p">,</span>
            <span class="n">exclude_hidden</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>  <span class="c1"># default directory is hidden ".papers"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="c1"># Include extra documents containing the abstracts</span>
        <span class="n">abstract_documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
            <span class="n">d</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"The following is a summary of the paper: </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">Summary:"</span>
                <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">abstract_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="p">))</span>

        <span class="c1"># Delete downloaded papers</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
                <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">f</span><span class="p">))</span>
                <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted file: </span><span class="si">{</span><span class="n">f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted directory: </span><span class="si">{</span><span class="n">papers_dir</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">"Unable to delete files or directory"</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">arxiv_documents</span><span class="p">,</span> <span class="n">abstract_documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/#llama_index.readers.papers.ArxivReader.load_data "Permanent link")

```
load_data(search_query: str, papers_dir: Optional[str] = '.papers', max_results: Optional[int] = 10) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `search_query` | `str` | 
A topic to search for (e.g. "Artificial Intelligence").



 | _required_ |
| `papers_dir` | `Optional[str]` | 

Locally directory to store the papers



 | `'.papers'` |
| `max_results` | `Optional[int]` | 

Maximum number of papers to fetch.



 | `10` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of Document objects.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-papers/llama_index/readers/papers/arxiv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">28</span>
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
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span>
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">papers_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">".papers"</span><span class="p">,</span>
    <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.</span>

<span class="sd">    Args:</span>
<span class="sd">        search_query (str): A topic to search for (e.g. "Artificial Intelligence").</span>
<span class="sd">        papers_dir (Optional[str]): Locally directory to store the papers</span>
<span class="sd">        max_results (Optional[int]): Maximum number of papers to fetch.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of Document objects.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">arxiv</span>

    <span class="n">arxiv_search</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">search_query</span><span class="p">,</span>
        <span class="n">id_list</span><span class="o">=</span><span class="p">[],</span>
        <span class="n">max_results</span><span class="o">=</span><span class="n">max_results</span><span class="p">,</span>
        <span class="n">sort_by</span><span class="o">=</span><span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">Relevance</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">search_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">arxiv_search</span><span class="o">.</span><span class="n">results</span><span class="p">())</span>
    <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Successfully fetched </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">search_results</span><span class="p">)</span><span class="si">}</span><span class="s2"> paperes"</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
        <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>

    <span class="n">paper_lookup</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
        <span class="c1"># Hash filename to avoid bad characters in file path</span>
        <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_hacky_hash</span><span class="p">(</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">)</span><span class="si">}</span><span class="s2">.pdf"</span>
        <span class="n">paper_lookup</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
            <span class="s2">"Authors"</span><span class="p">:</span> <span class="p">(</span><span class="s2">", "</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">a</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">paper</span><span class="o">.</span><span class="n">authors</span><span class="p">]),</span>
            <span class="s2">"Date published"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">published</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%m/</span><span class="si">%d</span><span class="s2">/%Y"</span><span class="p">),</span>
            <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">entry_id</span><span class="p">,</span>
            <span class="c1"># "summary": paper.summary</span>
        <span class="p">}</span>
        <span class="n">paper</span><span class="o">.</span><span class="n">download_pdf</span><span class="p">(</span><span class="n">dirpath</span><span class="o">=</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">filename</span><span class="p">)</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Downloading </span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">..."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_paper_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">paper_lookup</span><span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)]</span>

    <span class="n">arxiv_documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
        <span class="n">papers_dir</span><span class="p">,</span>
        <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_paper_metadata</span><span class="p">,</span>
        <span class="n">exclude_hidden</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>  <span class="c1"># default directory is hidden ".papers"</span>
    <span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
    <span class="c1"># Include extra documents containing the abstracts</span>
    <span class="n">abstract_documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
        <span class="n">d</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"The following is a summary of the paper: </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">Summary:"</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="n">abstract_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="p">))</span>

    <span class="c1"># Delete downloaded papers</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">f</span><span class="p">))</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted file: </span><span class="si">{</span><span class="n">f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted directory: </span><span class="si">{</span><span class="n">papers_dir</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Unable to delete files or directory"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">arxiv_documents</span> <span class="o">+</span> <span class="n">abstract_documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_papers\_and\_abstracts [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/#llama_index.readers.papers.ArxivReader.load_papers_and_abstracts "Permanent link")

```
load_papers_and_abstracts(search_query: str, papers_dir: Optional[str] = '.papers', max_results: Optional[int] = 10) -> Tuple[List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]]
```

Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `search_query` | `str` | 
A topic to search for (e.g. "Artificial Intelligence").



 | _required_ |
| `papers_dir` | `Optional[str]` | 

Locally directory to store the papers



 | `'.papers'` |
| `max_results` | `Optional[int]` | 

Maximum number of papers to fetch.



 | `10` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of Document objects representing the papers themselves



 |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 

List\[Document\]: A list of Document objects representing abstracts only



 |

Source code in `llama-index-integrations/readers/llama-index-readers-papers/llama_index/readers/papers/arxiv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">101</span>
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
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_papers_and_abstracts</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">papers_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">".papers"</span><span class="p">,</span>
    <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Search for a topic on Arxiv, download the PDFs of the top results locally, then read them.</span>

<span class="sd">    Args:</span>
<span class="sd">        search_query (str): A topic to search for (e.g. "Artificial Intelligence").</span>
<span class="sd">        papers_dir (Optional[str]): Locally directory to store the papers</span>
<span class="sd">        max_results (Optional[int]): Maximum number of papers to fetch.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of Document objects representing the papers themselves</span>
<span class="sd">        List[Document]: A list of Document objects representing abstracts only</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">arxiv</span>

    <span class="n">arxiv_search</span> <span class="o">=</span> <span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">search_query</span><span class="p">,</span>
        <span class="n">id_list</span><span class="o">=</span><span class="p">[],</span>
        <span class="n">max_results</span><span class="o">=</span><span class="n">max_results</span><span class="p">,</span>
        <span class="n">sort_by</span><span class="o">=</span><span class="n">arxiv</span><span class="o">.</span><span class="n">SortCriterion</span><span class="o">.</span><span class="n">Relevance</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">search_results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">arxiv_search</span><span class="o">.</span><span class="n">results</span><span class="p">())</span>
    <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Successfully fetched </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">search_results</span><span class="p">)</span><span class="si">}</span><span class="s2"> paperes"</span><span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
        <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>

    <span class="n">paper_lookup</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
        <span class="c1"># Hash filename to avoid bad characters in file path</span>
        <span class="n">filename</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_hacky_hash</span><span class="p">(</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">)</span><span class="si">}</span><span class="s2">.pdf"</span>
        <span class="n">paper_lookup</span><span class="p">[</span><span class="n">filename</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="p">,</span>
            <span class="s2">"Authors"</span><span class="p">:</span> <span class="p">(</span><span class="s2">", "</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">a</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">paper</span><span class="o">.</span><span class="n">authors</span><span class="p">]),</span>
            <span class="s2">"Date published"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">published</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%m/</span><span class="si">%d</span><span class="s2">/%Y"</span><span class="p">),</span>
            <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="o">.</span><span class="n">entry_id</span><span class="p">,</span>
            <span class="c1"># "summary": paper.summary</span>
        <span class="p">}</span>
        <span class="n">paper</span><span class="o">.</span><span class="n">download_pdf</span><span class="p">(</span><span class="n">dirpath</span><span class="o">=</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">filename</span><span class="p">)</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Downloading </span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">..."</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_paper_metadata</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">paper_lookup</span><span class="p">[</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)]</span>

    <span class="n">arxiv_documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
        <span class="n">papers_dir</span><span class="p">,</span>
        <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_paper_metadata</span><span class="p">,</span>
        <span class="n">exclude_hidden</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>  <span class="c1"># default directory is hidden ".papers"</span>
    <span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
    <span class="c1"># Include extra documents containing the abstracts</span>
    <span class="n">abstract_documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">search_results</span><span class="p">:</span>
        <span class="n">d</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"The following is a summary of the paper: </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">Summary:"</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">paper</span><span class="o">.</span><span class="n">summary</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>
        <span class="n">abstract_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">d</span><span class="p">))</span>

    <span class="c1"># Delete downloaded papers</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">,</span> <span class="n">f</span><span class="p">))</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted file: </span><span class="si">{</span><span class="n">f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="n">papers_dir</span><span class="p">)</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Deleted directory: </span><span class="si">{</span><span class="n">papers_dir</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Unable to delete files or directory"</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">arxiv_documents</span><span class="p">,</span> <span class="n">abstract_documents</span>
</code></pre></div></td></tr></tbody></table>

PubmedReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/#llama_index.readers.papers.PubmedReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pubmed Reader.

Gets a search query, return a list of Documents of the top corresponding scientific papers on Pubmed.

Source code in `llama-index-integrations/readers/llama-index-readers-papers/llama_index/readers/papers/pubmed/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  9</span>
<span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
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
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PubmedReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pubmed Reader.</span>

<span class="sd">    Gets a search query, return a list of Documents of the top corresponding scientific papers on Pubmed.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data_bioc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Search for a topic on Pubmed, fetch the text of the most relevant full-length papers.</span>
<span class="sd">        Uses the BoiC API, which has been down a lot.</span>

<span class="sd">        Args:</span>
<span class="sd">            search_query (str): A topic to search for (e.g. "Alzheimers").</span>
<span class="sd">            max_results (Optional[int]): Maximum number of papers to fetch.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">xml</span>
        <span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span>

        <span class="kn">import</span> <span class="nn">requests</span>

        <span class="n">pubmed_search</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"tool"</span><span class="p">:</span> <span class="s2">"tool"</span><span class="p">,</span> <span class="s2">"email"</span><span class="p">:</span> <span class="s2">"email"</span><span class="p">,</span> <span class="s2">"db"</span><span class="p">:</span> <span class="s2">"pmc"</span><span class="p">}</span>
        <span class="n">parameters</span><span class="p">[</span><span class="s2">"term"</span><span class="p">]</span> <span class="o">=</span> <span class="n">search_query</span>
        <span class="n">parameters</span><span class="p">[</span><span class="s2">"retmax"</span><span class="p">]</span> <span class="o">=</span> <span class="n">max_results</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s2">"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">root</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="n">resp</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">root</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o"></span> <span class="s2">"TITLE"</span>
                            <span class="p">]</span>
                        <span class="p">)</span>
                    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
                        <span class="k">pass</span>
                    <span class="n">pubmed_search</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="p">{</span>
                            <span class="s2">"title"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
                            <span class="s2">"url"</span><span class="p">:</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s2">"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2">/"</span>
                            <span class="p">),</span>
                            <span class="s2">"date"</span><span class="p">:</span> <span class="n">info</span><span class="p">[</span><span class="s2">"date"</span><span class="p">],</span>
                            <span class="s2">"documents"</span><span class="p">:</span> <span class="n">info</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">],</span>
                        <span class="p">}</span>
                    <span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unable to parse PMC</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2"> or it does not exist"</span><span class="p">)</span>

        <span class="c1"># Then get documents from Pubmed text, which includes abstracts</span>
        <span class="n">pubmed_documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">pubmed_search</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">]:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">p</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">d</span><span class="p">[</span><span class="s2">"passages"</span><span class="p">]])</span>
                <span class="n">pubmed_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                            <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                            <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                            <span class="s2">"Date published"</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">strptime</span><span class="p">(</span>
                                <span class="n">paper</span><span class="p">[</span><span class="s2">"date"</span><span class="p">],</span> <span class="s2">"%Y%m</span><span class="si">%d</span><span class="s2">"</span>
                            <span class="p">)</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%m/</span><span class="si">%d</span><span class="s2">/%Y"</span><span class="p">),</span>
                        <span class="p">},</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">pubmed_documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">search_query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">max_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Search for a topic on Pubmed, fetch the text of the most relevant full-length papers.</span>

<span class="sd">        Args:</span>
<span class="sd">            search_query (str): A topic to search for (e.g. "Alzheimers").</span>
<span class="sd">            max_results (Optional[int]): Maximum number of papers to fetch.</span>


<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">time</span>
        <span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">xml</span>

        <span class="kn">import</span> <span class="nn">requests</span>

        <span class="n">pubmed_search</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"tool"</span><span class="p">:</span> <span class="s2">"tool"</span><span class="p">,</span> <span class="s2">"email"</span><span class="p">:</span> <span class="s2">"email"</span><span class="p">,</span> <span class="s2">"db"</span><span class="p">:</span> <span class="s2">"pmc"</span><span class="p">}</span>
        <span class="n">parameters</span><span class="p">[</span><span class="s2">"term"</span><span class="p">]</span> <span class="o">=</span> <span class="n">search_query</span>
        <span class="n">parameters</span><span class="p">[</span><span class="s2">"retmax"</span><span class="p">]</span> <span class="o">=</span> <span class="n">max_results</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s2">"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">root</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="n">resp</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">root</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o"></span> <span class="s2">"article-title"</span><span class="p">:</span>
                            <span class="n">title</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span>
                        <span class="k">elif</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span> <span class="o"></span> <span class="s2">"Id"</span><span class="p">:</span>
            <span class="n">_id</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">resp</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2">/ascii"</span>
                <span class="p">)</span>
                <span class="n">info</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
                <span class="n">title</span> <span class="o">=</span> <span class="s2">"Pubmed Paper"</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">title</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
                        <span class="p">[</span>
                            <span class="n">p</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>
                            <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">info</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">"passages"</span><span class="p">]</span>
                            <span class="k">if</span> <span class="n">p</span><span class="p">[</span><span class="s2">"infons"</span><span class="p">][</span><span class="s2">"section_type"</span><span class="p">]</span> <span class="o"></span> <span class="s2">"Id"</span><span class="p">:</span>
            <span class="n">_id</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span>
            <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?id=</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2">&amp;db=pmc"</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">resp</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
                <span class="n">info</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="n">resp</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>

                <span class="n">raw_text</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">title</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">journal</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">info</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">element</span><span class="o">.</span><span class="n">tag</span> <span class="o"></span> <span class="s2">"journal-title"</span><span class="p">:</span>
                        <span class="n">journal</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span>

                    <span class="k">if</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span><span class="p">:</span>
                        <span class="n">raw_text</span> <span class="o">+=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">+</span> <span class="s2">" "</span>

                <span class="n">pubmed_search</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="p">{</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
                        <span class="s2">"journal"</span><span class="p">:</span> <span class="n">journal</span><span class="p">,</span>
                        <span class="s2">"url"</span><span class="p">:</span> <span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2">/"</span>
                        <span class="p">),</span>
                        <span class="s2">"text"</span><span class="p">:</span> <span class="n">raw_text</span><span class="p">,</span>
                    <span class="p">}</span>
                <span class="p">)</span>
                <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="c1"># API rate limits</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unable to parse PMC</span><span class="si">{</span><span class="n">_id</span><span class="si">}</span><span class="s2"> or it does not exist:"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>

    <span class="c1"># Then get documents from Pubmed text, which includes abstracts</span>
    <span class="n">pubmed_documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">pubmed_search</span><span class="p">:</span>
        <span class="n">pubmed_documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">paper</span><span class="p">[</span><span class="s2">"text"</span><span class="p">],</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">"Title of this paper"</span><span class="p">:</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                    <span class="s2">"Journal it was published in:"</span><span class="p">:</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"journal"</span><span class="p">],</span>
                    <span class="s2">"URL"</span><span class="p">:</span> <span class="n">paper</span><span class="p">[</span><span class="s2">"url"</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">pubmed_documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pandas ai](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/)[Next Patentsview](https://docs.llamaindex.ai/en/stable/api_reference/readers/patentsview/)
