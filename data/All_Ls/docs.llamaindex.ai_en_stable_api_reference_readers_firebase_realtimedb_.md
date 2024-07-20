Title: Firebase realtimedb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/

Markdown Content:
Firebase realtimedb - LlamaIndex


FirebaseRealtimeDatabaseReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/#llama_index.readers.firebase_realtimedb.FirebaseRealtimeDatabaseReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Firebase Realtime Database reader.

Retrieves data from Firebase Realtime Database and converts it into the Document used by LlamaIndex.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `database_url` | `str` | 
Firebase Realtime Database URL.



 | _required_ |
| `service_account_key_path` | `Optional[str]` | 

Path to the service account key file.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-firebase-realtimedb/llama_index/readers/firebase_realtimedb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FirebaseRealtimeDatabaseReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Firebase Realtime Database reader.</span>

<span class="sd">    Retrieves data from Firebase Realtime Database and converts it into the Document used by LlamaIndex.</span>

<span class="sd">    Args:</span>
<span class="sd">        database_url (str): Firebase Realtime Database URL.</span>
<span class="sd">        service_account_key_path (Optional[str]): Path to the service account key file.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">database_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">service_account_key_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">firebase_admin</span>
            <span class="kn">from</span> <span class="nn">firebase_admin</span> <span class="kn">import</span> <span class="n">credentials</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`firebase_admin` package not found, please run `pip install"</span>
                <span class="s2">" firebase-admin`"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">firebase_admin</span><span class="o">.</span><span class="n">_apps</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">service_account_key_path</span><span class="p">:</span>
                <span class="n">cred</span> <span class="o">=</span> <span class="n">credentials</span><span class="o">.</span><span class="n">Certificate</span><span class="p">(</span><span class="n">service_account_key_path</span><span class="p">)</span>
                <span class="n">firebase_admin</span><span class="o">.</span><span class="n">initialize_app</span><span class="p">(</span>
                    <span class="n">cred</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s2">"databaseURL"</span><span class="p">:</span> <span class="n">database_url</span><span class="p">}</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">firebase_admin</span><span class="o">.</span><span class="n">initialize_app</span><span class="p">(</span><span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s2">"databaseURL"</span><span class="p">:</span> <span class="n">database_url</span><span class="p">})</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from Firebase Realtime Database and convert it into documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            path (str): Path to the data in the Firebase Realtime Database.</span>
<span class="sd">            field (str, Optional): Key to pick data from</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of documents.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">firebase_admin</span> <span class="kn">import</span> <span class="n">db</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`firebase_admin` package not found, please run `pip install"</span>
                <span class="s2">" firebase-admin`"</span>
            <span class="p">)</span>

        <span class="n">ref</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">reference</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
                <span class="n">entry</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
                <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="s2">"document_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
                <span class="p">}</span>
                <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Dict</span> <span class="ow">and</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">:</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="n">entry</span><span class="p">[</span><span class="n">field</span><span class="p">]</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>

                <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/#llama_index.readers.firebase_realtimedb.FirebaseRealtimeDatabaseReader.load_data "Permanent link")

```
load_data(path: str, field: Optional[str] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from Firebase Realtime Database and convert it into documents.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str` | 
Path to the data in the Firebase Realtime Database.



 | _required_ |
| `field` | `(str, Optional)` | 

Key to pick data from



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: A list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-firebase-realtimedb/llama_index/readers/firebase_realtimedb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from Firebase Realtime Database and convert it into documents.</span>

<span class="sd">    Args:</span>
<span class="sd">        path (str): Path to the data in the Firebase Realtime Database.</span>
<span class="sd">        field (str, Optional): Key to pick data from</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: A list of documents.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">firebase_admin</span> <span class="kn">import</span> <span class="n">db</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"`firebase_admin` package not found, please run `pip install"</span>
            <span class="s2">" firebase-admin`"</span>
        <span class="p">)</span>

    <span class="n">ref</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">reference</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">entry</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"document_id"</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span> <span class="ow">is</span> <span class="n">Dict</span> <span class="ow">and</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">entry</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">entry</span><span class="p">[</span><span class="n">field</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>

            <span class="n">document</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous File](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/)[Next Firestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/)
