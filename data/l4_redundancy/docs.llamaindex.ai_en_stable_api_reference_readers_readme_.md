Title: Readme - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/readme/

Markdown Content:
Readme - LlamaIndex


ReadmeReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/readme/#llama_index.readers.readme.ReadmeReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Readme reader. Reads data from a Readme.com docs.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_key` | `str` | 
Readme.com API Key



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-readme/llama_index/readers/readme/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
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
<span class="normal">154</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ReadmeReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Readme reader. Reads data from a Readme.com docs.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key (str): Readme.com API Key</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Readme reader."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">api_key</span><span class="si">}</span><span class="s2">:"</span><span class="p">,</span> <span class="s2">"utf-8"</span><span class="p">))</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"accept"</span><span class="p">:</span> <span class="s2">"*/*"</span><span class="p">,</span>
            <span class="s2">"authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Basic </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the docs (pages).</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_docs</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"body_html"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">body</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">body</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"id"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                <span class="s2">"slug"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"slug"</span><span class="p">],</span>
                <span class="s2">"updated_at"</span><span class="p">:</span> <span class="n">doc</span><span class="p">[</span><span class="s2">"updatedAt"</span><span class="p">],</span>
            <span class="p">}</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">body</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">get_all_docs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves all documents, along with their information, categorized by categories.</span>

<span class="sd">        Returns:</span>
<span class="sd">            list: A list containing dictionaries with document information.</span>
<span class="sd">        """</span>
        <span class="n">categories</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_categories</span><span class="p">()</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">category</span> <span class="ow">in</span> <span class="n">categories</span><span class="p">:</span>
            <span class="n">category_docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_docs_in_category</span><span class="p">(</span><span class="n">category</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"slug"</span><span class="p">))</span>
            <span class="n">documents_slugs</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">category_doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"slug"</span><span class="p">)</span> <span class="k">for</span> <span class="n">category_doc</span> <span class="ow">in</span> <span class="n">category_docs</span>
            <span class="p">]</span>
            <span class="k">for</span> <span class="n">document_slug</span> <span class="ow">in</span> <span class="n">documents_slugs</span><span class="p">:</span>
                <span class="n">doc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_document_info</span><span class="p">(</span><span class="n">document_slug</span><span class="p">)</span>
                <span class="n">doc</span><span class="p">[</span><span class="s2">"category_name"</span><span class="p">]</span> <span class="o">=</span> <span class="n">category</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">get_docs_in_category</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">category_slug</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves documents belonging to a specific category.</span>

<span class="sd">        Args:</span>
<span class="sd">            category_slug (str): The slug of the category.</span>

<span class="sd">        Returns:</span>
<span class="sd">            list: A list containing dictionaries with document information.</span>
<span class="sd">        """</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://dash.readme.com/api/v1/categories/</span><span class="si">{</span><span class="n">category_slug</span><span class="si">}</span><span class="s2">/docs"</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="c1"># Filter documents hidden=False</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">doc</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">doc</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"hidden"</span><span class="p">,</span> <span class="kc">True</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">get_document_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document_slug</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves information about a specific document.</span>

<span class="sd">        Args:</span>
<span class="sd">            document_slug (str): The slug of the document.</span>

<span class="sd">        Returns:</span>
<span class="sd">            dict: A dictionary containing document information.</span>
<span class="sd">        """</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://dash.readme.com/api/v1/docs/</span><span class="si">{</span><span class="n">document_slug</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_categories_page</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">params</span><span class="p">,</span> <span class="n">page</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Sends a GET request to a specific page of categories.</span>

<span class="sd">        Args:</span>
<span class="sd">            params (dict): Parameters of the request, such as perPage and others.</span>
<span class="sd">            page (int): The number of the page to be retrieved.</span>

<span class="sd">        Returns:</span>
<span class="sd">            tuple: A tuple containing the total number of items and the retrieved categories.</span>
<span class="sd">        """</span>
        <span class="n">url</span> <span class="o">=</span> <span class="s2">"https://dash.readme.com/api/v1/categories"</span>
        <span class="n">params</span><span class="p">[</span><span class="s2">"page"</span><span class="p">]</span> <span class="o">=</span> <span class="n">page</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">)</span>
        <span class="c1"># total counts and categories</span>
        <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">headers</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"x-total-count"</span><span class="p">,</span> <span class="mi">0</span><span class="p">)),</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_all_categories</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Retrieves all categories from the API.</span>

<span class="sd">        Returns:</span>
<span class="sd">            list: A list containing all categories with type "guide".</span>
<span class="sd">        """</span>
        <span class="n">perPage</span> <span class="o">=</span> <span class="mi">100</span>
        <span class="n">page</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"perPage"</span><span class="p">:</span> <span class="n">perPage</span><span class="p">,</span>
            <span class="s2">"page"</span><span class="p">:</span> <span class="n">page</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">total_count</span><span class="p">,</span> <span class="n">categories</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_categories_page</span><span class="p">(</span><span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">,</span> <span class="n">page</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="n">remaining_pages</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">ceil</span><span class="p">(</span><span class="n">total_count</span> <span class="o">/</span> <span class="n">perPage</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">remaining_pages</span> <span class="o">+</span> <span class="mi">2</span><span class="p">):</span>
            <span class="n">categories</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_categories_page</span><span class="p">(</span><span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">,</span> <span class="n">page</span><span class="o">=</span><span class="n">i</span><span class="p">))</span>

        <span class="c1"># Include just categories with type: "guide"</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">category</span> <span class="k">for</span> <span class="n">category</span> <span class="ow">in</span> <span class="n">categories</span> <span class="k">if</span> <span class="n">category</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"type"</span><span class="p">)</span> <span class="o"></span> <span class="s2">"guide"</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Rayyan](https://docs.llamaindex.ai/en/stable/api_reference/readers/rayyan/)[Next Readwise](https://docs.llamaindex.ai/en/stable/api_reference/readers/readwise/)
