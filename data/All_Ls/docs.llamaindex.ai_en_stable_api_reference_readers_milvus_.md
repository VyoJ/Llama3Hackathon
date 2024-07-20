Title: Milvus - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/

Markdown Content:
Milvus - LlamaIndex


MilvusReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/#llama_index.readers.milvus.MilvusReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Milvus reader.

Source code in `llama-index-integrations/readers/llama-index-readers-milvus/llama_index/readers/milvus/base.py`

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
<span class="normal">142</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MilvusReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Milvus reader."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"localhost"</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">19530</span><span class="p">,</span>
        <span class="n">user</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">use_secure</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"`pymilvus` package not found, please run `pip install pymilvus`"</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pymilvus</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="kn">from</span> <span class="nn">pymilvus</span> <span class="kn">import</span> <span class="n">MilvusException</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">host</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">port</span> <span class="o">=</span> <span class="n">port</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">user</span> <span class="o">=</span> <span class="n">user</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">password</span> <span class="o">=</span> <span class="n">password</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_secure</span> <span class="o">=</span> <span class="n">use_secure</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">default_search_params</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"IVF_FLAT"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"nprobe"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"IVF_SQ8"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"nprobe"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"IVF_PQ"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"nprobe"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"HNSW"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"ef"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"RHNSW_FLAT"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"ef"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"RHNSW_SQ"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"ef"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"RHNSW_PQ"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"ef"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"IVF_HNSW"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"nprobe"</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span> <span class="s2">"ef"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"ANNOY"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"search_k"</span><span class="p">:</span> <span class="mi">10</span><span class="p">}},</span>
            <span class="s2">"AUTOINDEX"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"metric_type"</span><span class="p">:</span> <span class="s2">"IP"</span><span class="p">,</span> <span class="s2">"params"</span><span class="p">:</span> <span class="p">{}},</span>
        <span class="p">}</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_create_connection_alias</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">MilvusException</span><span class="p">:</span>
            <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">expr</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">search_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Milvus.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection_name (str): Name of the Milvus collection.</span>
<span class="sd">            query_vector (List[float]): Query vector.</span>
<span class="sd">            limit (int): Number of results to return.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">pymilvus</span> <span class="kn">import</span> <span class="n">Collection</span><span class="p">,</span> <span class="n">MilvusException</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="o">=</span> <span class="n">Collection</span><span class="p">(</span><span class="n">collection_name</span><span class="p">,</span> <span class="n">using</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">alias</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">MilvusException</span><span class="p">:</span>
            <span class="k">raise</span>

        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">load</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">MilvusException</span><span class="p">:</span>
            <span class="k">raise</span>
        <span class="k">if</span> <span class="n">search_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">search_params</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_search_params</span><span class="p">()</span>

        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="p">[</span><span class="n">query_vector</span><span class="p">],</span>
            <span class="s2">"embedding"</span><span class="p">,</span>
            <span class="n">param</span><span class="o">=</span><span class="n">search_params</span><span class="p">,</span>
            <span class="n">expr</span><span class="o">=</span><span class="n">expr</span><span class="p">,</span>
            <span class="n">output_fields</span><span class="o">=</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">],</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># TODO: In future append embedding when more efficient</span>
        <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">),</span>
                <span class="n">text</span><span class="o">=</span><span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text"</span><span class="p">),</span>
            <span class="p">)</span>

            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">_create_connection_alias</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">pymilvus</span> <span class="kn">import</span> <span class="n">connections</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">alias</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="c1"># Attempt to reuse an open connection</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">connections</span><span class="o">.</span><span class="n">list_connections</span><span class="p">():</span>
            <span class="n">addr</span> <span class="o">=</span> <span class="n">connections</span><span class="o">.</span><span class="n">get_connection_addr</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
                <span class="ow">and</span> <span class="p">(</span><span class="s2">"address"</span> <span class="ow">in</span> <span class="n">addr</span><span class="p">)</span>
                <span class="ow">and</span> <span class="p">(</span><span class="n">addr</span><span class="p">[</span><span class="s2">"address"</span><span class="p">]</span> <span class="o">==</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">alias</span> <span class="o">=</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                <span class="k">break</span>

        <span class="c1"># Connect to the Milvus instance using the passed in Environment variables</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">alias</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">alias</span> <span class="o">=</span> <span class="n">uuid4</span><span class="p">()</span><span class="o">.</span><span class="n">hex</span>
            <span class="n">connections</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span>
                <span class="n">alias</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">alias</span><span class="p">,</span>
                <span class="n">host</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">,</span>
                <span class="n">port</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="p">,</span>
                <span class="n">user</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">user</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
                <span class="n">password</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">password</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
                <span class="n">secure</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">use_secure</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_search_params</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">indexes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">_index_params</span>
        <span class="n">search_params</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_search_params</span><span class="p">[</span><span class="n">index</span><span class="p">[</span><span class="s2">"index_type"</span><span class="p">]]</span>
        <span class="n">search_params</span><span class="p">[</span><span class="s2">"metric_type"</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span><span class="p">[</span><span class="s2">"metric_type"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">search_params</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/#llama_index.readers.milvus.MilvusReader.load_data "Permanent link")

```
load_data(query_vector: List[float], collection_name: str, expr: Any = None, search_params: Optional[dict] = None, limit: int = 10) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Milvus.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
Name of the Milvus collection.



 | _required_ |
| `query_vector` | `List[float]` | 

Query vector.



 | _required_ |
| `limit` | `int` | 

Number of results to return.



 | `10` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-milvus/llama_index/readers/milvus/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 56</span>
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
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">query_vector</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span>
    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">expr</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">search_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Milvus.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name (str): Name of the Milvus collection.</span>
<span class="sd">        query_vector (List[float]): Query vector.</span>
<span class="sd">        limit (int): Number of results to return.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">pymilvus</span> <span class="kn">import</span> <span class="n">Collection</span><span class="p">,</span> <span class="n">MilvusException</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="o">=</span> <span class="n">Collection</span><span class="p">(</span><span class="n">collection_name</span><span class="p">,</span> <span class="n">using</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">alias</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">MilvusException</span><span class="p">:</span>
        <span class="k">raise</span>

    <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">load</span><span class="p">()</span>
    <span class="k">except</span> <span class="n">MilvusException</span><span class="p">:</span>
        <span class="k">raise</span>
    <span class="k">if</span> <span class="n">search_params</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">search_params</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_search_params</span><span class="p">()</span>

    <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">collection</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
        <span class="p">[</span><span class="n">query_vector</span><span class="p">],</span>
        <span class="s2">"embedding"</span><span class="p">,</span>
        <span class="n">param</span><span class="o">=</span><span class="n">search_params</span><span class="p">,</span>
        <span class="n">expr</span><span class="o">=</span><span class="n">expr</span><span class="p">,</span>
        <span class="n">output_fields</span><span class="o">=</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">],</span>
        <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># TODO: In future append embedding when more efficient</span>
    <span class="k">for</span> <span class="n">hit</span> <span class="ow">in</span> <span class="n">res</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
        <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"doc_id"</span><span class="p">),</span>
            <span class="n">text</span><span class="o">=</span><span class="n">hit</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text"</span><span class="p">),</span>
        <span class="p">)</span>

        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Microsoft sharepoint](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/)[Next Minio](https://docs.llamaindex.ai/en/stable/api_reference/readers/minio/)
