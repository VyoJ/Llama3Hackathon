Title: Guru - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/

Markdown Content:
Guru - LlamaIndex


GuruReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/#llama_index.readers.guru.GuruReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Guru cards / collections reader.

Source code in `llama-index-integrations/readers/llama-index-readers-guru/llama_index/readers/guru/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
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
<span class="normal">156</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GuruReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Guru cards / collections reader."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">guru_username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize GuruReader.</span>

<span class="sd">        Args:</span>
<span class="sd">            guru_username: Guru username.</span>
<span class="sd">            api_token: Guru API token. This can be personal API keys or collection based API keys. Note this is not the same as your password.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">guru_username</span> <span class="o">=</span> <span class="n">guru_username</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_token</span> <span class="o">=</span> <span class="n">api_token</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">guru_auth</span> <span class="o">=</span> <span class="n">HTTPBasicAuth</span><span class="p">(</span><span class="n">guru_username</span><span class="p">,</span> <span class="n">api_token</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">card_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Guru.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_ids: List of collection ids to load from. Only pass in card_ids or collection_ids, not both.</span>
<span class="sd">            card_ids: List of card ids to load from. Only pass in card_ids or collection_ids, not both.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>

<span class="sd">        """</span>
        <span class="k">assert</span> <span class="p">(</span><span class="n">collection_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="n">card_ids</span> <span class="ow">is</span> <span class="kc">None</span>
        <span class="p">),</span> <span class="s2">"Only pass in card_ids or collection_ids, not both."</span>
        <span class="k">assert</span> <span class="p">(</span><span class="n">collection_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="n">card_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">),</span> <span class="s2">"Pass in card_ids or collection_ids."</span>

        <span class="k">if</span> <span class="n">collection_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">card_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_card_ids_from_collection_ids</span><span class="p">(</span><span class="n">collection_ids</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_card_info</span><span class="p">(</span><span class="n">card_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">card_id</span> <span class="ow">in</span> <span class="n">card_ids</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_get_card_ids_from_collection_ids</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get card ids from collection ids."""</span>
        <span class="n">all_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">collection_id</span> <span class="ow">in</span> <span class="n">collection_ids</span><span class="p">:</span>
            <span class="n">card_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_card_ids_from_collection_id</span><span class="p">(</span><span class="n">collection_id</span><span class="p">)</span>
            <span class="n">all_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">card_ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">all_ids</span>

    <span class="k">def</span> <span class="nf">_get_card_ids_from_collection_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">records</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">next_page</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="n">initial_url</span> <span class="o">=</span> <span class="s2">"https://api.getguru.com/api/v1/search/cardmgr?queryType=cards"</span>

        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">initial_url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">guru_auth</span><span class="p">)</span>
        <span class="n">records</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">())</span>

        <span class="k">while</span> <span class="n">next_page</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">url</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s2">"Link"</span><span class="p">]</span>
                <span class="n">url_pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"&lt;(.*?)&gt;"</span>
                <span class="n">url_match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">url_pattern</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>
                <span class="n">url</span> <span class="o">=</span> <span class="n">url_match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="n">next_page</span> <span class="o">=</span> <span class="kc">False</span>
                <span class="k">break</span>

            <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">guru_auth</span><span class="p">)</span>
            <span class="n">records</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">())</span>

        <span class="n">cards</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="o">.</span><span class="n">from_records</span><span class="p">(</span><span class="n">records</span><span class="p">)</span>
        <span class="n">df_normalized</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">json_normalize</span><span class="p">(</span><span class="n">cards</span><span class="p">[</span><span class="s2">"collection"</span><span class="p">])</span>
        <span class="n">df_normalized</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"collection_"</span> <span class="o">+</span> <span class="n">col</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">df_normalized</span><span class="o">.</span><span class="n">columns</span><span class="p">]</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">cards</span><span class="p">,</span> <span class="n">df_normalized</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">collection_id</span> <span class="o"></span> <span class="mi">200</span><span class="p">:</span>
            <span class="n">title</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"preferredPhrase"</span><span class="p">]</span>
            <span class="n">html</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"content"</span><span class="p">]</span>  <span class="c1"># i think this needs to be loaded</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clean_html</span><span class="p">(</span><span class="n">html</span><span class="p">)</span>
            <span class="n">collection</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"collection"</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"title"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span>
                <span class="s2">"collection"</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span>
                <span class="s2">"card_id"</span><span class="p">:</span> <span class="n">card_id</span><span class="p">,</span>
                <span class="s2">"guru_link"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_guru_link</span><span class="p">(</span><span class="n">card_id</span><span class="p">),</span>
            <span class="p">}</span>

            <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Could not get card info for </span><span class="si">{</span><span class="n">card_id</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_clean_html</span><span class="p">(</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Cleans HTML content by fetching its text representation using BeautifulSoup.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">text</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">""</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">with</span> <span class="n">warnings</span><span class="o">.</span><span class="n">catch_warnings</span><span class="p">():</span>
                <span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s2">"ignore"</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">UserWarning</span><span class="p">)</span>
                <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>
                <span class="k">return</span> <span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>

        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_guru_link</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">card_id</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        takes a guru "ExternalId" from meta data and returns the link to the guru card.</span>
<span class="sd">        """</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"https://api.getguru.com/api/v1/cards/</span><span class="si">{</span><span class="n">card_id</span><span class="si">}</span><span class="s2">/extended"</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"accept"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">guru_auth</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">==</span> <span class="mi">200</span><span class="p">:</span>
            <span class="n">slug</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()[</span><span class="s2">"slug"</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Guru link doesn't exist: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="k">return</span> <span class="sa">f</span><span class="s2">"https://app.getguru.com/card/</span><span class="si">{</span><span class="n">slug</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/#llama_index.readers.guru.GuruReader.load_data "Permanent link")

```
load_data(collection_ids: Optional[List[str]] = None, card_ids: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Guru.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_ids` | `Optional[List[str]]` | 
List of collection ids to load from. Only pass in card\_ids or collection\_ids, not both.



 | `None` |
| `card_ids` | `Optional[List[str]]` | 

List of card ids to load from. Only pass in card\_ids or collection\_ids, not both.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-guru/llama_index/readers/guru/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
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
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">collection_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">card_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Guru.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_ids: List of collection ids to load from. Only pass in card_ids or collection_ids, not both.</span>
<span class="sd">        card_ids: List of card ids to load from. Only pass in card_ids or collection_ids, not both.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">collection_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
        <span class="n">card_ids</span> <span class="ow">is</span> <span class="kc">None</span>
    <span class="p">),</span> <span class="s2">"Only pass in card_ids or collection_ids, not both."</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">collection_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
        <span class="n">card_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">),</span> <span class="s2">"Pass in card_ids or collection_ids."</span>

    <span class="k">if</span> <span class="n">collection_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">card_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_card_ids_from_collection_ids</span><span class="p">(</span><span class="n">collection_ids</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_card_info</span><span class="p">(</span><span class="n">card_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">card_id</span> <span class="ow">in</span> <span class="n">card_ids</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Graphql](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/)[Next Hatena blog](https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/)
