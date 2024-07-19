Title: Firestore - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/

Markdown Content:
Firestore - LlamaIndex


FirestoreReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/#llama_index.readers.firestore.FirestoreReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Simple Firestore reader.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `project_id` | `str` | 
The Google Cloud Project ID.



 | _required_ |
| `*args` | `Optional[Any]` | 

Additional arguments.



 | `()` |
| `**kwargs` | `Optional[Any]` | 

Additional keyword arguments.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `FirestoreReader` |  | 
A FirestoreReader object.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-firestore/llama_index/readers/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
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
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FirestoreReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Firestore reader.</span>

<span class="sd">    Args:</span>
<span class="sd">        project_id (str): The Google Cloud Project ID.</span>
<span class="sd">        *args (Optional[Any]): Additional arguments.</span>
<span class="sd">        **kwargs (Optional[Any]): Additional keyword arguments.</span>

<span class="sd">    Returns:</span>
<span class="sd">        FirestoreReader: A FirestoreReader object.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_FIRESTORE_DATABASE</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">google.cloud</span> <span class="kn">import</span> <span class="n">firestore</span>
            <span class="kn">from</span> <span class="nn">google.cloud.firestore_v1.services.firestore.transports.base</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">DEFAULT_CLIENT_INFO</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">IMPORT_ERROR_MSG</span><span class="p">)</span>

        <span class="n">client_info</span> <span class="o">=</span> <span class="n">DEFAULT_CLIENT_INFO</span>
        <span class="n">client_info</span><span class="o">.</span><span class="n">user_agent</span> <span class="o">=</span> <span class="n">USER_AGENT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="n">firestore</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span>
            <span class="n">project</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span> <span class="n">database</span><span class="o">=</span><span class="n">database_id</span><span class="p">,</span> <span class="n">client_info</span><span class="o">=</span><span class="n">client_info</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from a Firestore collection, returning a list of Documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): The name of the Firestore collection to read from.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: A list of Document objects.</span>
<span class="sd">        """</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">col_ref</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">col_ref</span><span class="o">.</span><span class="n">stream</span><span class="p">():</span>
            <span class="n">doc_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc_str</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_document</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a single document from Firestore.</span>

<span class="sd">        Args:</span>
<span class="sd">            document_url (str): The absolute path to the Firestore document to read.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: A Document object.</span>
<span class="sd">        """</span>
        <span class="n">parts</span> <span class="o">=</span> <span class="n">document_url</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">parts</span><span class="p">)</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Invalid document URL: </span><span class="si">{</span><span class="n">document_url</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">ref</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">parts</span><span class="p">)):</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">ref</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="n">parts</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">ref</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">document</span><span class="p">(</span><span class="n">parts</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>

    <span class="n">doc</span> <span class="o">=</span> <span class="n">ref</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">doc</span><span class="o">.</span><span class="n">exists</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"No such document: </span><span class="si">{</span><span class="n">document_url</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">doc_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
    <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">doc_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)[Next Gcs](https://docs.llamaindex.ai/en/stable/api_reference/readers/gcs/)
