Title: Microsoft outlook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/

Markdown Content:
Microsoft outlook - LlamaIndex


OutlookLocalCalendarReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/#llama_index.readers.microsoft_outlook.OutlookLocalCalendarReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Outlook local calendar reader for Windows. Reads events from local copy of Outlook calendar.

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-outlook/llama_index/readers/microsoft_outlook/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
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
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OutlookLocalCalendarReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Outlook local calendar reader for Windows.</span>
<span class="sd">    Reads events from local copy of Outlook calendar.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
        <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">more_attributes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from user's local calendar.</span>

<span class="sd">        Args:</span>
<span class="sd">            number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">            start_date (Optional[Union[str, datetime.date]]): the start date to return events from. Defaults to today.</span>
<span class="sd">            end_date (Optional[Union[str, datetime.date]]): the last date (inclusive) to return events from. Defaults to 2199-01-01.</span>
<span class="sd">            more_attributes (Optional[ List[str]]): additional attributes to be retrieved from calendar entries. Non-existnat attributes are ignored.</span>

<span class="sd">        Returns a list of documents sutitable for indexing by llam_index. Always returns Start, End, Subject, Location, and Organizer</span>
<span class="sd">        attributes and optionally returns additional attributes specified in the more_attributes parameter.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">platform</span><span class="o">.</span><span class="n">system</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="s2">"windows"</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="n">attributes</span> <span class="o">=</span> <span class="p">[</span>
            <span class="s2">"Start"</span><span class="p">,</span>
            <span class="s2">"End"</span><span class="p">,</span>
            <span class="s2">"Subject"</span><span class="p">,</span>
            <span class="s2">"Location"</span><span class="p">,</span>
            <span class="s2">"Organizer"</span><span class="p">,</span>
        <span class="p">]</span>  <span class="c1"># base attributes to return</span>
        <span class="k">if</span> <span class="n">more_attributes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># if the user has specified more attributes</span>
            <span class="n">attributes</span> <span class="o">+=</span> <span class="n">more_attributes</span>
        <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

        <span class="c1"># Initialize the Outlook application</span>
        <span class="n">winstuff</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="s2">"win32com.client"</span><span class="p">)</span>
        <span class="n">outlook</span> <span class="o">=</span> <span class="n">winstuff</span><span class="o">.</span><span class="n">Dispatch</span><span class="p">(</span><span class="s2">"Outlook.Application"</span><span class="p">)</span><span class="o">.</span><span class="n">GetNamespace</span><span class="p">(</span><span class="s2">"MAPI"</span><span class="p">)</span>

        <span class="c1"># Get the Calendar folder</span>
        <span class="n">calendar_folder</span> <span class="o">=</span> <span class="n">outlook</span><span class="o">.</span><span class="n">GetDefaultFolder</span><span class="p">(</span><span class="mi">9</span><span class="p">)</span>

        <span class="c1"># Retrieve calendar items</span>
        <span class="n">events</span> <span class="o">=</span> <span class="n">calendar_folder</span><span class="o">.</span><span class="n">Items</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>
        <span class="n">events</span><span class="o">.</span><span class="n">Sort</span><span class="p">(</span><span class="s2">"[Start]"</span><span class="p">)</span>  <span class="c1"># Sort items by start time</span>
        <span class="n">numberReturned</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
            <span class="n">converted_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">(</span>
                <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">day</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">converted_date</span> <span class="o">&gt;</span> <span class="n">start_date</span><span class="p">:</span>  <span class="c1"># if past start date</span>
                <span class="n">numberReturned</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">eventstring</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="k">for</span> <span class="n">attribute</span> <span class="ow">in</span> <span class="n">attributes</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">attribute</span><span class="p">):</span>
                        <span class="n">eventstring</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">attribute</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="nb">getattr</span><span class="p">(</span><span class="n">event</span><span class="p">,</span><span class="n">attribute</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">eventstring</span><span class="p">))</span>
            <span class="k">if</span> <span class="n">numberReturned</span> <span class="o">&gt;=</span> <span class="n">number_of_results</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/#llama_index.readers.microsoft_outlook.OutlookLocalCalendarReader.load_data "Permanent link")

```
load_data(number_of_results: Optional[int] = 100, start_date: Optional[Union[str, date]] = None, end_date: Optional[Union[str, date]] = None, more_attributes: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from user's local calendar.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `number_of_results` | `Optional[int]` | 
the number of events to return. Defaults to 100.



 | `100` |
| `start_date` | `Optional[Union[str, date]]` | 

the start date to return events from. Defaults to today.



 | `None` |
| `end_date` | `Optional[Union[str, date]]` | 

the last date (inclusive) to return events from. Defaults to 2199-01-01.



 | `None` |
| `more_attributes` | `Optional[List[str]]` | 

additional attributes to be retrieved from calendar entries. Non-existnat attributes are ignored.



 | `None` |

Returns a list of documents sutitable for indexing by llam\_index. Always returns Start, End, Subject, Location, and Organizer attributes and optionally returns additional attributes specified in the more\_attributes parameter.

Source code in `llama-index-integrations/readers/llama-index-readers-microsoft-outlook/llama_index/readers/microsoft_outlook/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
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
    <span class="n">number_of_results</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">100</span><span class="p">,</span>
    <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">more_attributes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from user's local calendar.</span>

<span class="sd">    Args:</span>
<span class="sd">        number_of_results (Optional[int]): the number of events to return. Defaults to 100.</span>
<span class="sd">        start_date (Optional[Union[str, datetime.date]]): the start date to return events from. Defaults to today.</span>
<span class="sd">        end_date (Optional[Union[str, datetime.date]]): the last date (inclusive) to return events from. Defaults to 2199-01-01.</span>
<span class="sd">        more_attributes (Optional[ List[str]]): additional attributes to be retrieved from calendar entries. Non-existnat attributes are ignored.</span>

<span class="sd">    Returns a list of documents sutitable for indexing by llam_index. Always returns Start, End, Subject, Location, and Organizer</span>
<span class="sd">    attributes and optionally returns additional attributes specified in the more_attributes parameter.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">platform</span><span class="o">.</span><span class="n">system</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="s2">"windows"</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>
    <span class="n">attributes</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s2">"Start"</span><span class="p">,</span>
        <span class="s2">"End"</span><span class="p">,</span>
        <span class="s2">"Subject"</span><span class="p">,</span>
        <span class="s2">"Location"</span><span class="p">,</span>
        <span class="s2">"Organizer"</span><span class="p">,</span>
    <span class="p">]</span>  <span class="c1"># base attributes to return</span>
    <span class="k">if</span> <span class="n">more_attributes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>  <span class="c1"># if the user has specified more attributes</span>
        <span class="n">attributes</span> <span class="o">+=</span> <span class="n">more_attributes</span>
    <span class="k">if</span> <span class="n">start_date</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">start_date</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="o">.</span><span class="n">fromisoformat</span><span class="p">(</span><span class="n">start_date</span><span class="p">)</span>

    <span class="c1"># Initialize the Outlook application</span>
    <span class="n">winstuff</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="s2">"win32com.client"</span><span class="p">)</span>
    <span class="n">outlook</span> <span class="o">=</span> <span class="n">winstuff</span><span class="o">.</span><span class="n">Dispatch</span><span class="p">(</span><span class="s2">"Outlook.Application"</span><span class="p">)</span><span class="o">.</span><span class="n">GetNamespace</span><span class="p">(</span><span class="s2">"MAPI"</span><span class="p">)</span>

    <span class="c1"># Get the Calendar folder</span>
    <span class="n">calendar_folder</span> <span class="o">=</span> <span class="n">outlook</span><span class="o">.</span><span class="n">GetDefaultFolder</span><span class="p">(</span><span class="mi">9</span><span class="p">)</span>

    <span class="c1"># Retrieve calendar items</span>
    <span class="n">events</span> <span class="o">=</span> <span class="n">calendar_folder</span><span class="o">.</span><span class="n">Items</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">events</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[]</span>
    <span class="n">events</span><span class="o">.</span><span class="n">Sort</span><span class="p">(</span><span class="s2">"[Start]"</span><span class="p">)</span>  <span class="c1"># Sort items by start time</span>
    <span class="n">numberReturned</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
        <span class="n">converted_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">(</span>
            <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">Start</span><span class="o">.</span><span class="n">day</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">converted_date</span> <span class="o">&gt;</span> <span class="n">start_date</span><span class="p">:</span>  <span class="c1"># if past start date</span>
            <span class="n">numberReturned</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">eventstring</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">attribute</span> <span class="ow">in</span> <span class="n">attributes</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">attribute</span><span class="p">):</span>
                    <span class="n">eventstring</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">attribute</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="nb">getattr</span><span class="p">(</span><span class="n">event</span><span class="p">,</span><span class="n">attribute</span><span class="p">)</span><span class="si">}</span><span class="s2">, "</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">eventstring</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">numberReturned</span> <span class="o">&gt;=</span> <span class="n">number_of_results</span><span class="p">:</span>
            <span class="k">break</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Microsoft onedrive](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/)[Next Microsoft sharepoint](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/)
