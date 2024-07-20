Title: Maps - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/

Markdown Content:
Maps - LlamaIndex


OpenMap [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/#llama_index.readers.maps.OpenMap "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

OpenMap Reader.

Get the map Features from the overpass api(osm) for the given location/area

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `if` | `you not sure about the search_tag and tag_values visit https` | 
//taginfo.openstreetmap.org/tags



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-maps/llama_index/readers/maps/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 14</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpenMap</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""OpenMap Reader.</span>

<span class="sd">    Get the map Features from the overpass api(osm) for the given location/area</span>


<span class="sd">    Args:</span>
<span class="sd">        localarea(str) -  Area or location you are searching for</span>
<span class="sd">        tag_values(str) -  filter for the give area</span>
<span class="sd">        search_tag(str)  - Tag that you are looking for</span>

<span class="sd">        if you not sure about the search_tag and tag_values visit https://taginfo.openstreetmap.org/tags</span>

<span class="sd">        remove_keys(list) - list of keys that need to be removed from the response</span>
<span class="sd">                            by default  following keys will be removed ['nodes','geometry','members']</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_get_user</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># choose from all lowercase letter</span>
        <span class="n">letters</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">ascii_lowercase</span>
        <span class="k">return</span> <span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">letters</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">_get_latlon</span><span class="p">(</span><span class="n">locarea</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">user_agent</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">geopy.geocoders</span> <span class="kn">import</span> <span class="n">Nominatim</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"install geopy using `pip3 install geopy`"</span><span class="p">)</span>

        <span class="n">geolocator</span> <span class="o">=</span> <span class="n">Nominatim</span><span class="p">(</span><span class="n">user_agent</span><span class="o">=</span><span class="n">user_agent</span><span class="p">)</span>
        <span class="n">location</span> <span class="o">=</span> <span class="n">geolocator</span><span class="o">.</span><span class="n">geocode</span><span class="p">(</span><span class="n">locarea</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">location</span><span class="o">.</span><span class="n">latitude</span><span class="p">,</span> <span class="n">location</span><span class="o">.</span><span class="n">longitude</span><span class="p">)</span> <span class="k">if</span> <span class="n">location</span> <span class="k">else</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">localarea</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">search_tag</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"amenity"</span><span class="p">,</span>
        <span class="n">remove_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="s2">"geometry"</span><span class="p">,</span> <span class="s2">"members"</span><span class="p">],</span>
        <span class="n">tag_only</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">tag_values</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">""</span><span class="p">],</span>
        <span class="n">local_area_buffer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2000</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This loader will bring you the all the node values from the open street maps for the given location.</span>

<span class="sd">        Args:</span>
<span class="sd">        localarea(str) -  Area or location you are searching for</span>
<span class="sd">        search_tag(str)  - Tag that you are looking for</span>
<span class="sd">        if you not sure about the search_tag and tag_values visit https://taginfo.openstreetmap.org/tags</span>

<span class="sd">        remove_keys(list) - list of keys that need to be removed from the response</span>
<span class="sd">                            by default it those keys will be removed ['nodes','geometry','members']</span>

<span class="sd">        tag_only(bool) - if True it  return the nodes which has tags if False returns all the nodes</span>
<span class="sd">        tag_values(str) -  filter for the give area</span>
<span class="sd">        local_area_buffer(int) - range that you wish to cover (Default 2000(2km))</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">osmxtract</span> <span class="kn">import</span> <span class="n">location</span><span class="p">,</span> <span class="n">overpass</span>
            <span class="kn">from</span> <span class="nn">osmxtract.errors</span> <span class="kn">import</span> <span class="n">OverpassBadRequest</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"install osmxtract using `pip3 install osmxtract`"</span><span class="p">)</span>

        <span class="n">null_list</span> <span class="o">=</span> <span class="p">[</span><span class="s2">""</span><span class="p">,</span> <span class="s2">"null"</span><span class="p">,</span> <span class="s2">"none"</span><span class="p">,</span> <span class="kc">None</span><span class="p">]</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">local_area</span> <span class="o">=</span> <span class="n">localarea</span>

        <span class="k">if</span> <span class="n">local_area</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="ow">in</span> <span class="n">null_list</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"The Area should not be null"</span><span class="p">)</span>

        <span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_user</span><span class="p">()</span>
        <span class="n">lat</span><span class="p">,</span> <span class="n">lon</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_latlon</span><span class="p">(</span><span class="n">local_area</span><span class="p">,</span> <span class="n">user</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">bounds</span> <span class="o">=</span> <span class="n">location</span><span class="o">.</span><span class="n">from_buffer</span><span class="p">(</span><span class="n">lat</span><span class="p">,</span> <span class="n">lon</span><span class="p">,</span> <span class="n">buffer_size</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">local_area_buffer</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"Please give valid location name or check for spelling"</span><span class="p">)</span>

        <span class="c1"># overpass query generation and execution</span>
        <span class="n">tag_values</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">tag_values</span><span class="p">]</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">overpass</span><span class="o">.</span><span class="n">ql_query</span><span class="p">(</span>
            <span class="n">bounds</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="n">search_tag</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span> <span class="n">values</span><span class="o">=</span><span class="n">tag_values</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">500</span>
        <span class="p">)</span>

        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"overpass_query"</span><span class="p">]</span> <span class="o">=</span> <span class="n">query</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">overpass</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

        <span class="k">except</span> <span class="n">OverpassBadRequest</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Error while executing the Query </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> please check the Args"</span>
            <span class="p">)</span>

        <span class="n">res</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"elements"</span><span class="p">]</span>

        <span class="n">_meta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="k">del</span> <span class="n">_meta</span><span class="p">[</span><span class="s2">"elements"</span><span class="p">]</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"overpass_meta"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">_meta</span><span class="p">)</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"lat"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lat</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"lon"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lon</span>
        <span class="c1"># filtering for only the tag values</span>
        <span class="n">filtered</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span> <span class="k">if</span> <span class="s2">"tags"</span> <span class="ow">in</span> <span class="n">i</span><span class="p">]</span> <span class="k">if</span> <span class="n">tag_only</span> <span class="k">else</span> <span class="n">res</span>

        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">remove_keys</span><span class="p">:</span>
            <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">filtered</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">filtered</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">filtered</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">res</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/#llama_index.readers.maps.OpenMap.load_data "Permanent link")

```
load_data(localarea: str, search_tag: Optional[str] = 'amenity', remove_keys: Optional[List] = ['nodes', 'geometry', 'members'], tag_only: Optional[bool] = True, tag_values: Optional[List] = [''], local_area_buffer: Optional[int] = 2000) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

This loader will bring you the all the node values from the open street maps for the given location.

Args: localarea(str) - Area or location you are searching for search\_tag(str) - Tag that you are looking for if you not sure about the search\_tag and tag\_values visit https://taginfo.openstreetmap.org/tags

remove\_keys(list) - list of keys that need to be removed from the response by default it those keys will be removed \['nodes','geometry','members'\]

tag\_only(bool) - if True it return the nodes which has tags if False returns all the nodes tag\_values(str) - filter for the give area local\_area\_buffer(int) - range that you wish to cover (Default 2000(2km))

Source code in `llama-index-integrations/readers/llama-index-readers-maps/llama_index/readers/maps/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 53</span>
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
<span class="normal">127</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">localarea</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">search_tag</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"amenity"</span><span class="p">,</span>
    <span class="n">remove_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="s2">"geometry"</span><span class="p">,</span> <span class="s2">"members"</span><span class="p">],</span>
    <span class="n">tag_only</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">tag_values</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s2">""</span><span class="p">],</span>
    <span class="n">local_area_buffer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2000</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This loader will bring you the all the node values from the open street maps for the given location.</span>

<span class="sd">    Args:</span>
<span class="sd">    localarea(str) -  Area or location you are searching for</span>
<span class="sd">    search_tag(str)  - Tag that you are looking for</span>
<span class="sd">    if you not sure about the search_tag and tag_values visit https://taginfo.openstreetmap.org/tags</span>

<span class="sd">    remove_keys(list) - list of keys that need to be removed from the response</span>
<span class="sd">                        by default it those keys will be removed ['nodes','geometry','members']</span>

<span class="sd">    tag_only(bool) - if True it  return the nodes which has tags if False returns all the nodes</span>
<span class="sd">    tag_values(str) -  filter for the give area</span>
<span class="sd">    local_area_buffer(int) - range that you wish to cover (Default 2000(2km))</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">osmxtract</span> <span class="kn">import</span> <span class="n">location</span><span class="p">,</span> <span class="n">overpass</span>
        <span class="kn">from</span> <span class="nn">osmxtract.errors</span> <span class="kn">import</span> <span class="n">OverpassBadRequest</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"install osmxtract using `pip3 install osmxtract`"</span><span class="p">)</span>

    <span class="n">null_list</span> <span class="o">=</span> <span class="p">[</span><span class="s2">""</span><span class="p">,</span> <span class="s2">"null"</span><span class="p">,</span> <span class="s2">"none"</span><span class="p">,</span> <span class="kc">None</span><span class="p">]</span>
    <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">local_area</span> <span class="o">=</span> <span class="n">localarea</span>

    <span class="k">if</span> <span class="n">local_area</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="ow">in</span> <span class="n">null_list</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"The Area should not be null"</span><span class="p">)</span>

    <span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_user</span><span class="p">()</span>
    <span class="n">lat</span><span class="p">,</span> <span class="n">lon</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_latlon</span><span class="p">(</span><span class="n">local_area</span><span class="p">,</span> <span class="n">user</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">bounds</span> <span class="o">=</span> <span class="n">location</span><span class="o">.</span><span class="n">from_buffer</span><span class="p">(</span><span class="n">lat</span><span class="p">,</span> <span class="n">lon</span><span class="p">,</span> <span class="n">buffer_size</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">local_area_buffer</span><span class="p">))</span>
    <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"Please give valid location name or check for spelling"</span><span class="p">)</span>

    <span class="c1"># overpass query generation and execution</span>
    <span class="n">tag_values</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">tag_values</span><span class="p">]</span>
    <span class="n">query</span> <span class="o">=</span> <span class="n">overpass</span><span class="o">.</span><span class="n">ql_query</span><span class="p">(</span>
        <span class="n">bounds</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="n">search_tag</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span> <span class="n">values</span><span class="o">=</span><span class="n">tag_values</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">500</span>
    <span class="p">)</span>

    <span class="n">extra_info</span><span class="p">[</span><span class="s2">"overpass_query"</span><span class="p">]</span> <span class="o">=</span> <span class="n">query</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">overpass</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

    <span class="k">except</span> <span class="n">OverpassBadRequest</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Error while executing the Query </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> please check the Args"</span>
        <span class="p">)</span>

    <span class="n">res</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"elements"</span><span class="p">]</span>

    <span class="n">_meta</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    <span class="k">del</span> <span class="n">_meta</span><span class="p">[</span><span class="s2">"elements"</span><span class="p">]</span>
    <span class="n">extra_info</span><span class="p">[</span><span class="s2">"overpass_meta"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">_meta</span><span class="p">)</span>
    <span class="n">extra_info</span><span class="p">[</span><span class="s2">"lat"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lat</span>
    <span class="n">extra_info</span><span class="p">[</span><span class="s2">"lon"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lon</span>
    <span class="c1"># filtering for only the tag values</span>
    <span class="n">filtered</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span> <span class="k">if</span> <span class="s2">"tags"</span> <span class="ow">in</span> <span class="n">i</span><span class="p">]</span> <span class="k">if</span> <span class="n">tag_only</span> <span class="k">else</span> <span class="n">res</span>

    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">remove_keys</span><span class="p">:</span>
        <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">filtered</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">filtered</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">filtered</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">res</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Mangoapps guides](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangoapps_guides/)[Next Mbox](https://docs.llamaindex.ai/en/stable/api_reference/readers/mbox/)
