Title: Weather - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/

Markdown Content:
Weather - LlamaIndex


WeatherReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/#llama_index.readers.weather.WeatherReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Weather Reader.

Reads the forecast & current weather of any location using OpenWeatherMap's free API.

Check 'https://openweathermap.org/appid' on how to generate a free OpenWeatherMap API, It's free.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `token` | `str` | 
bearer\_token that you get from OWM API.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-weather/llama_index/readers/weather/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
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
<span class="normal">90</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">WeatherReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Weather Reader.</span>

<span class="sd">    Reads the forecast &amp; current weather of any location using OpenWeatherMap's free API.</span>

<span class="sd">    Check 'https://openweathermap.org/appid' \</span>
<span class="sd">        on how to generate a free OpenWeatherMap API, It's free.</span>

<span class="sd">    Args:</span>
<span class="sd">        token (str): bearer_token that you get from OWM API.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">token</span> <span class="o">=</span> <span class="n">token</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">places</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load weather data for the given locations.</span>
<span class="sd">        OWM's One Call API provides the following weather data for any geographical coordinate:</span>
<span class="sd">        - Current weather</span>
<span class="sd">        - Hourly forecast for 48 hours</span>
<span class="sd">        - Daily forecast for 7 days.</span>

<span class="sd">        Args:</span>
<span class="sd">            places (List[str]) - places you want the weather data for.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pyowm</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"install pyowm using `pip install pyowm`"</span><span class="p">)</span>

        <span class="n">owm</span> <span class="o">=</span> <span class="n">pyowm</span><span class="o">.</span><span class="n">OWM</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">token</span><span class="p">)</span>
        <span class="n">mgr</span> <span class="o">=</span> <span class="n">owm</span><span class="o">.</span><span class="n">weather_manager</span><span class="p">()</span>

        <span class="n">reg</span> <span class="o">=</span> <span class="n">owm</span><span class="o">.</span><span class="n">city_id_registry</span><span class="p">()</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">place</span> <span class="ow">in</span> <span class="n">places</span><span class="p">:</span>
            <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">list_of_locations</span> <span class="o">=</span> <span class="n">reg</span><span class="o">.</span><span class="n">locations_for</span><span class="p">(</span><span class="n">city_name</span><span class="o">=</span><span class="n">place</span><span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">city</span> <span class="o">=</span> <span class="n">list_of_locations</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Unable to find </span><span class="si">{</span><span class="n">place</span><span class="si">}</span><span class="s2">, try checking the spelling and try again"</span>
                <span class="p">)</span>
            <span class="n">lat</span> <span class="o">=</span> <span class="n">city</span><span class="o">.</span><span class="n">lat</span>
            <span class="n">lon</span> <span class="o">=</span> <span class="n">city</span><span class="o">.</span><span class="n">lon</span>

            <span class="n">res</span> <span class="o">=</span> <span class="n">mgr</span><span class="o">.</span><span class="n">one_call</span><span class="p">(</span><span class="n">lat</span><span class="o">=</span><span class="n">lat</span><span class="p">,</span> <span class="n">lon</span><span class="o">=</span><span class="n">lon</span><span class="p">)</span>

            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"latitude"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lat</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"longitude"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lon</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"timezone"</span><span class="p">]</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">timezone</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"location"</span><span class="p">]</span> <span class="o">=</span> <span class="n">place</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"current weather"</span><span class="p">]</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">current</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_daily</span><span class="p">:</span>
                <span class="n">info_dict</span><span class="p">[</span><span class="s2">"daily forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_daily</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_hourly</span><span class="p">:</span>
                <span class="n">info_dict</span><span class="p">[</span><span class="s2">"hourly forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_hourly</span>
                <span class="p">]</span>
            <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_minutely</span><span class="p">:</span>
                <span class="n">info_dict</span><span class="p">[</span><span class="s2">"minutely forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_minutely</span>
                <span class="p">]</span>
            <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">national_weather_alerts</span><span class="p">:</span>
                <span class="n">info_dict</span><span class="p">[</span><span class="s2">"national weather alerts"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">national_weather_alerts</span>
                <span class="p">]</span>

            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">info_dict</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/#llama_index.readers.weather.WeatherReader.load_data "Permanent link")

```
load_data(places: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load weather data for the given locations. OWM's One Call API provides the following weather data for any geographical coordinate: - Current weather - Hourly forecast for 48 hours - Daily forecast for 7 days.

Source code in `llama-index-integrations/readers/llama-index-readers-weather/llama_index/readers/weather/base.py`

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
<span class="normal">90</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">places</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load weather data for the given locations.</span>
<span class="sd">    OWM's One Call API provides the following weather data for any geographical coordinate:</span>
<span class="sd">    - Current weather</span>
<span class="sd">    - Hourly forecast for 48 hours</span>
<span class="sd">    - Daily forecast for 7 days.</span>

<span class="sd">    Args:</span>
<span class="sd">        places (List[str]) - places you want the weather data for.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">pyowm</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"install pyowm using `pip install pyowm`"</span><span class="p">)</span>

    <span class="n">owm</span> <span class="o">=</span> <span class="n">pyowm</span><span class="o">.</span><span class="n">OWM</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">token</span><span class="p">)</span>
    <span class="n">mgr</span> <span class="o">=</span> <span class="n">owm</span><span class="o">.</span><span class="n">weather_manager</span><span class="p">()</span>

    <span class="n">reg</span> <span class="o">=</span> <span class="n">owm</span><span class="o">.</span><span class="n">city_id_registry</span><span class="p">()</span>

    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">place</span> <span class="ow">in</span> <span class="n">places</span><span class="p">:</span>
        <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">list_of_locations</span> <span class="o">=</span> <span class="n">reg</span><span class="o">.</span><span class="n">locations_for</span><span class="p">(</span><span class="n">city_name</span><span class="o">=</span><span class="n">place</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">city</span> <span class="o">=</span> <span class="n">list_of_locations</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Unable to find </span><span class="si">{</span><span class="n">place</span><span class="si">}</span><span class="s2">, try checking the spelling and try again"</span>
            <span class="p">)</span>
        <span class="n">lat</span> <span class="o">=</span> <span class="n">city</span><span class="o">.</span><span class="n">lat</span>
        <span class="n">lon</span> <span class="o">=</span> <span class="n">city</span><span class="o">.</span><span class="n">lon</span>

        <span class="n">res</span> <span class="o">=</span> <span class="n">mgr</span><span class="o">.</span><span class="n">one_call</span><span class="p">(</span><span class="n">lat</span><span class="o">=</span><span class="n">lat</span><span class="p">,</span> <span class="n">lon</span><span class="o">=</span><span class="n">lon</span><span class="p">)</span>

        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"latitude"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lat</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"longitude"</span><span class="p">]</span> <span class="o">=</span> <span class="n">lon</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"timezone"</span><span class="p">]</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">timezone</span>
        <span class="n">info_dict</span><span class="p">[</span><span class="s2">"location"</span><span class="p">]</span> <span class="o">=</span> <span class="n">place</span>
        <span class="n">info_dict</span><span class="p">[</span><span class="s2">"current weather"</span><span class="p">]</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">current</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_daily</span><span class="p">:</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"daily forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_daily</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_hourly</span><span class="p">:</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"hourly forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_hourly</span>
            <span class="p">]</span>
        <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_minutely</span><span class="p">:</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"minutely forecast"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">forecast_minutely</span>
            <span class="p">]</span>
        <span class="k">if</span> <span class="n">res</span><span class="o">.</span><span class="n">national_weather_alerts</span><span class="p">:</span>
            <span class="n">info_dict</span><span class="p">[</span><span class="s2">"national weather alerts"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">i</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">res</span><span class="o">.</span><span class="n">national_weather_alerts</span>
            <span class="p">]</span>

        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">info_dict</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Upstage](https://docs.llamaindex.ai/en/stable/api_reference/readers/upstage/)[Next Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/)
