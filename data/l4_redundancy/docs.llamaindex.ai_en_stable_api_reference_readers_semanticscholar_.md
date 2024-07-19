Title: Semanticscholar - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/

Markdown Content:
Semanticscholar - LlamaIndex


SemanticScholarReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

A class to read and process data from Semantic Scholar API ...

#### Methods:[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader--methods "Permanent link")

**init**(): Instantiate the SemanticScholar object

load\_data(query: str, limit: int = 10, returned\_fields: list = \["title", "abstract", "venue", "year", "paperId", "citationCount", "openAccessPdf", "authors"\]) -> list: Loads data from Semantic Scholar based on the query and returned\_fields

Source code in `llama-index-integrations/readers/llama-index-readers-semanticscholar/llama_index/readers/semanticscholar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 10</span>
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
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SemanticScholarReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A class to read and process data from Semantic Scholar API</span>
<span class="sd">    ...</span>

<span class="sd">    Methods:</span>
<span class="sd">    -------</span>
<span class="sd">    __init__():</span>
<span class="sd">       Instantiate the SemanticScholar object</span>

<span class="sd">    load_data(query: str, limit: int = 10, returned_fields: list = ["title", "abstract", "venue", "year", "paperId", "citationCount", "openAccessPdf", "authors"]) -&gt; list:</span>
<span class="sd">        Loads data from Semantic Scholar based on the query and returned_fields</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">base_dir</span><span class="o">=</span><span class="s2">"pdfs"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Instantiate the SemanticScholar object.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">arxiv</span>

        <span class="kn">from</span> <span class="nn">semanticscholar</span> <span class="kn">import</span> <span class="n">SemanticScholar</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">arxiv</span> <span class="o">=</span> <span class="n">arxiv</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span> <span class="o">=</span> <span class="n">base_dir</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">s2</span> <span class="o">=</span> <span class="n">SemanticScholar</span><span class="p">(</span><span class="n">timeout</span><span class="p">,</span> <span class="n">api_key</span><span class="p">)</span>
        <span class="c1"># check for base dir</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_clear_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        delete the .citation* folder.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">shutil</span>

        <span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="s2">"./.citation*"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_download_pdf</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">paper_id</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">base_dir</span><span class="o">=</span><span class="s2">"pdfs"</span><span class="p">):</span>
        <span class="n">logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">()</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"User-Agent"</span><span class="p">:</span> <span class="p">(</span>
                <span class="s2">"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"</span>
                <span class="s2">" like Gecko) Chrome/58.0.3029.110 Safari/537.3"</span>
            <span class="p">)</span>
        <span class="p">}</span>
        <span class="c1"># Making a GET request</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="n">content_type</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s2">"Content-Type"</span><span class="p">]</span>

        <span class="c1"># As long as the content-type is application/pdf, this will download the file</span>
        <span class="k">if</span> <span class="s2">"application/pdf"</span> <span class="ow">in</span> <span class="n">content_type</span><span class="p">:</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">base_dir</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
            <span class="n">file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">base_dir</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">paper_id</span><span class="si">}</span><span class="s2">.pdf"</span><span class="p">)</span>
            <span class="c1"># check if the file already exists</span>
            <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">file_path</span><span class="p">):</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">file_path</span><span class="si">}</span><span class="s2"> already exists"</span><span class="p">)</span>
                <span class="k">return</span> <span class="n">file_path</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">iter_content</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="mi">1024</span><span class="p">):</span>
                    <span class="k">if</span> <span class="n">chunk</span><span class="p">:</span>
                        <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Downloaded pdf from </span><span class="si">{</span><span class="n">url</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">file_path</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">url</span><span class="si">}</span><span class="s2"> was not downloaded: protected"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">_get_full_text_docs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="kn">from</span> <span class="nn">PyPDF2</span> <span class="kn">import</span> <span class="n">PdfReader</span>

<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Gets the full text of the documents from Semantic Scholar</span>

<span class="sd">        Parameters</span>
<span class="sd">        ----------</span>
<span class="sd">        documents: list</span>
<span class="sd">            The list of Document object that contains the search results</span>

<span class="sd">        Returns</span>
<span class="sd">        -------</span>
<span class="sd">        list</span>
<span class="sd">            The list of Document object that contains the search results with full text</span>

<span class="sd">        Raises</span>
<span class="sd">        ------</span>
<span class="sd">        Exception</span>
<span class="sd">            If there is an error while getting the full text</span>

<span class="sd">        """</span>
        <span class="n">full_text_docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">paper</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">paper</span><span class="o">.</span><span class="n">extra_info</span>
            <span class="n">url</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"openAccessPdf"</span><span class="p">]</span>
            <span class="n">externalIds</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"externalIds"</span><span class="p">]</span>
            <span class="n">paper_id</span> <span class="o">=</span> <span class="n">metadata</span><span class="p">[</span><span class="s2">"paperId"</span><span class="p">]</span>
            <span class="n">file_path</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="n">persist_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">paper_id</span><span class="si">}</span><span class="s2">.pdf"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">url</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">):</span>
                <span class="c1"># Download the document first</span>
                <span class="n">file_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_pdf</span><span class="p">(</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"paperId"</span><span class="p">],</span> <span class="n">url</span><span class="p">,</span> <span class="n">persist_dir</span><span class="p">)</span>

            <span class="k">if</span> <span class="p">(</span>
                <span class="ow">not</span> <span class="n">url</span>
                <span class="ow">and</span> <span class="n">externalIds</span>
                <span class="ow">and</span> <span class="s2">"ArXiv"</span> <span class="ow">in</span> <span class="n">externalIds</span>
                <span class="ow">and</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
            <span class="p">):</span>
                <span class="c1"># download the pdf from arxiv</span>
                <span class="n">file_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_pdf_from_arxiv</span><span class="p">(</span>
                    <span class="n">paper_id</span><span class="p">,</span> <span class="n">externalIds</span><span class="p">[</span><span class="s2">"ArXiv"</span><span class="p">]</span>
                <span class="p">)</span>

            <span class="c1"># Then, check if it's a valid PDF. If it's not, skip to the next document.</span>
            <span class="k">if</span> <span class="n">file_path</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">pdf</span> <span class="o">=</span> <span class="n">PdfReader</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">))</span>
                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                    <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Failed to read pdf with exception: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">. Skipping document..."</span>
                    <span class="p">)</span>
                    <span class="k">continue</span>

                <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">:</span>
                    <span class="n">text</span> <span class="o">+=</span> <span class="n">page</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span>
                <span class="n">full_text_docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">full_text_docs</span>

    <span class="k">def</span> <span class="nf">_download_pdf_from_arxiv</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">paper_id</span><span class="p">,</span> <span class="n">arxiv_id</span><span class="p">):</span>
        <span class="n">paper</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">arxiv</span><span class="o">.</span><span class="n">Search</span><span class="p">(</span><span class="n">id_list</span><span class="o">=</span><span class="p">[</span><span class="n">arxiv_id</span><span class="p">],</span> <span class="n">max_results</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">results</span><span class="p">())</span>
        <span class="n">paper</span><span class="o">.</span><span class="n">download_pdf</span><span class="p">(</span><span class="n">dirpath</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">paper_id</span> <span class="o">+</span> <span class="s2">".pdf"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">base_dir</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">paper_id</span><span class="si">}</span><span class="s2">.pdf"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">,</span>
        <span class="n">full_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">returned_fields</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">"title"</span><span class="p">,</span>
            <span class="s2">"abstract"</span><span class="p">,</span>
            <span class="s2">"venue"</span><span class="p">,</span>
            <span class="s2">"year"</span><span class="p">,</span>
            <span class="s2">"paperId"</span><span class="p">,</span>
            <span class="s2">"citationCount"</span><span class="p">,</span>
            <span class="s2">"openAccessPdf"</span><span class="p">,</span>
            <span class="s2">"authors"</span><span class="p">,</span>
            <span class="s2">"externalIds"</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Loads data from Semantic Scholar based on the entered query and returned_fields.</span>

<span class="sd">        Parameters</span>
<span class="sd">        ----------</span>
<span class="sd">        query: str</span>
<span class="sd">            The search query for the paper</span>
<span class="sd">        limit: int, optional</span>
<span class="sd">            The number of maximum results returned (default is 10)</span>
<span class="sd">        returned_fields: list, optional</span>
<span class="sd">            The list of fields to be returned from the search</span>

<span class="sd">        Returns:</span>
<span class="sd">        -------</span>
<span class="sd">        list</span>
<span class="sd">            The list of Document object that contains the search results</span>

<span class="sd">        Raises:</span>
<span class="sd">        ------</span>
<span class="sd">        Exception</span>
<span class="sd">            If there is an error while performing the search</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">s2</span><span class="o">.</span><span class="n">search_paper</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">returned_fields</span><span class="p">)</span>
        <span class="k">except</span> <span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">HTTPError</span><span class="p">,</span> <span class="n">requests</span><span class="o">.</span><span class="n">ConnectionError</span><span class="p">,</span> <span class="n">requests</span><span class="o">.</span><span class="n">Timeout</span><span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="s2">"Failed to fetch data from Semantic Scholar with exception: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">e</span>
            <span class="p">)</span>
            <span class="k">raise</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An unexpected error occurred: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
            <span class="k">raise</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[:</span><span class="n">limit</span><span class="p">]:</span>
            <span class="n">openAccessPdf</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"openAccessPdf"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">abstract</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"abstract"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">title</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"title"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="c1"># concat title and abstract</span>
            <span class="k">if</span> <span class="n">abstract</span> <span class="ow">and</span> <span class="n">title</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">abstract</span>
            <span class="k">elif</span> <span class="ow">not</span> <span class="n">abstract</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">title</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
                <span class="s2">"venue"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"venue"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"year"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"year"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"paperId"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"paperId"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"citationCount"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"citationCount"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="s2">"openAccessPdf"</span><span class="p">:</span> <span class="n">openAccessPdf</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"url"</span><span class="p">)</span> <span class="k">if</span> <span class="n">openAccessPdf</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
                <span class="s2">"authors"</span><span class="p">:</span> <span class="p">[</span><span class="n">author</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="k">for</span> <span class="n">author</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"authors"</span><span class="p">,</span> <span class="p">[])],</span>
                <span class="s2">"externalIds"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"externalIds"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
            <span class="p">}</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="k">if</span> <span class="n">full_text</span><span class="p">:</span>
            <span class="n">full_text_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_full_text_docs</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">full_text_documents</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader.load_data "Permanent link")

```
load_data(query, limit, full_text=False, returned_fields=['title', 'abstract', 'venue', 'year', 'paperId', 'citationCount', 'openAccessPdf', 'authors', 'externalIds']) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads data from Semantic Scholar based on the entered query and returned\_fields.

##### Parameters[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader.load_data--parameters "Permanent link")

query: str The search query for the paper limit: int, optional The number of maximum results returned (default is 10) returned\_fields: list, optional The list of fields to be returned from the search

##### Returns:[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader.load_data--returns "Permanent link")

list The list of Document object that contains the search results

##### Raises:[#](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/#llama_index.readers.semanticscholar.SemanticScholarReader.load_data--raises "Permanent link")

Exception If there is an error while performing the search

Source code in `llama-index-integrations/readers/llama-index-readers-semanticscholar/llama_index/readers/semanticscholar/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
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
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">,</span>
    <span class="n">full_text</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">returned_fields</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">"title"</span><span class="p">,</span>
        <span class="s2">"abstract"</span><span class="p">,</span>
        <span class="s2">"venue"</span><span class="p">,</span>
        <span class="s2">"year"</span><span class="p">,</span>
        <span class="s2">"paperId"</span><span class="p">,</span>
        <span class="s2">"citationCount"</span><span class="p">,</span>
        <span class="s2">"openAccessPdf"</span><span class="p">,</span>
        <span class="s2">"authors"</span><span class="p">,</span>
        <span class="s2">"externalIds"</span><span class="p">,</span>
    <span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Loads data from Semantic Scholar based on the entered query and returned_fields.</span>

<span class="sd">    Parameters</span>
<span class="sd">    ----------</span>
<span class="sd">    query: str</span>
<span class="sd">        The search query for the paper</span>
<span class="sd">    limit: int, optional</span>
<span class="sd">        The number of maximum results returned (default is 10)</span>
<span class="sd">    returned_fields: list, optional</span>
<span class="sd">        The list of fields to be returned from the search</span>

<span class="sd">    Returns:</span>
<span class="sd">    -------</span>
<span class="sd">    list</span>
<span class="sd">        The list of Document object that contains the search results</span>

<span class="sd">    Raises:</span>
<span class="sd">    ------</span>
<span class="sd">    Exception</span>
<span class="sd">        If there is an error while performing the search</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">s2</span><span class="o">.</span><span class="n">search_paper</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">returned_fields</span><span class="p">)</span>
    <span class="k">except</span> <span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">HTTPError</span><span class="p">,</span> <span class="n">requests</span><span class="o">.</span><span class="n">ConnectionError</span><span class="p">,</span> <span class="n">requests</span><span class="o">.</span><span class="n">Timeout</span><span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
            <span class="s2">"Failed to fetch data from Semantic Scholar with exception: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">e</span>
        <span class="p">)</span>
        <span class="k">raise</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">"An unexpected error occurred: </span><span class="si">%s</span><span class="s2">"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
        <span class="k">raise</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">results</span><span class="p">[:</span><span class="n">limit</span><span class="p">]:</span>
        <span class="n">openAccessPdf</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"openAccessPdf"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">abstract</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"abstract"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">title</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"title"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="c1"># concat title and abstract</span>
        <span class="k">if</span> <span class="n">abstract</span> <span class="ow">and</span> <span class="n">title</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">title</span> <span class="o">+</span> <span class="s2">" "</span> <span class="o">+</span> <span class="n">abstract</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="n">abstract</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">title</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"title"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
            <span class="s2">"venue"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"venue"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
            <span class="s2">"year"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"year"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
            <span class="s2">"paperId"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"paperId"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
            <span class="s2">"citationCount"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"citationCount"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
            <span class="s2">"openAccessPdf"</span><span class="p">:</span> <span class="n">openAccessPdf</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"url"</span><span class="p">)</span> <span class="k">if</span> <span class="n">openAccessPdf</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">"authors"</span><span class="p">:</span> <span class="p">[</span><span class="n">author</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="k">for</span> <span class="n">author</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"authors"</span><span class="p">,</span> <span class="p">[])],</span>
            <span class="s2">"externalIds"</span><span class="p">:</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="s2">"externalIds"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
        <span class="p">}</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

    <span class="k">if</span> <span class="n">full_text</span><span class="p">:</span>
        <span class="n">full_text_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_full_text_docs</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">full_text_documents</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sec filings](https://docs.llamaindex.ai/en/stable/api_reference/readers/sec_filings/)[Next Simple directory reader](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/)
