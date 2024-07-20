Title: Opendal - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/

Markdown Content:
Opendal - LlamaIndex


OpendalAzblobReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalAzblobReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any Azblob file or directory.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/azblob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpendalAzblobReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any Azblob file or directory."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">container</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Azblob container, along with credentials if needed.</span>

<span class="sd">        If key is not set, the entire bucket (filtered by prefix) is parsed.</span>

<span class="sd">        Args:</span>
<span class="sd">        container (str): the name of your azblob bucket</span>
<span class="sd">        path (str): the path of the data. If none is provided,</span>
<span class="sd">            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.</span>
<span class="sd">        endpoint Optional[str]: the endpoint of the azblob service.</span>
<span class="sd">        account_name (Optional[str]): provide azblob access key directly.</span>
<span class="sd">        account_key (Optional[str]): provide azblob access key directly.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. See `SimpleDirectoryReader` for more details.</span>

<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>

        <span class="c1"># opendal service related config.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">options</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"container"</span><span class="p">:</span> <span class="n">container</span><span class="p">,</span>
            <span class="s2">"endpoint"</span><span class="p">:</span> <span class="n">endpoint</span><span class="p">,</span>
            <span class="s2">"account_name"</span><span class="p">:</span> <span class="n">account_name</span><span class="p">,</span>
            <span class="s2">"account_key"</span><span class="p">:</span> <span class="n">account_key</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
        <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
            <span class="n">scheme</span><span class="o">=</span><span class="s2">"azblob"</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalAzblobReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file(s) from OpenDAL.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/azblob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
    <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
        <span class="n">scheme</span><span class="o">=</span><span class="s2">"azblob"</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

OpendalGcsReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalGcsReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any Gcs file or directory.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/gcs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpendalGcsReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any Gcs file or directory."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">bucket</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">credentials</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize Gcs container, along with credentials if needed.</span>

<span class="sd">        If key is not set, the entire bucket (filtered by prefix) is parsed.</span>

<span class="sd">        Args:</span>
<span class="sd">        bucket (str): the name of your gcs bucket</span>
<span class="sd">        path (str): the path of the data. If none is provided,</span>
<span class="sd">            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.</span>
<span class="sd">        endpoint Optional[str]: the endpoint of the azblob service.</span>
<span class="sd">        credentials (Optional[str]): provide credential string for GCS OAuth2 directly.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. See `SimpleDirectoryReader` for more details.</span>

<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>

        <span class="c1"># opendal service related config.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">options</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"bucket"</span><span class="p">:</span> <span class="n">bucket</span><span class="p">,</span>
            <span class="s2">"endpoint"</span><span class="p">:</span> <span class="n">endpoint</span><span class="p">,</span>
            <span class="s2">"credentials"</span><span class="p">:</span> <span class="n">credentials</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
        <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
            <span class="n">scheme</span><span class="o">=</span><span class="s2">"gcs"</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalGcsReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file(s) from OpenDAL.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/gcs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
    <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
        <span class="n">scheme</span><span class="o">=</span><span class="s2">"gcs"</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

OpendalReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any opendal operator.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
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
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpendalReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any opendal operator."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">scheme</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize opendal operator, along with credentials if needed.</span>


<span class="sd">        Args:</span>
<span class="sd">        scheme (str): the scheme of the service</span>
<span class="sd">        path (str): the path of the data. If none is provided,</span>
<span class="sd">            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. See `SimpleDirectoryReader` for more details.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">opendal</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">op</span> <span class="o">=</span> <span class="n">opendal</span><span class="o">.</span><span class="n">AsyncOperator</span><span class="p">(</span><span class="n">scheme</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"/"</span><span class="p">):</span>
                <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">download_file_from_opendal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">download_dir_from_opendal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">))</span>

            <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">,</span> <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">)</span>

            <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file(s) from OpenDAL.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
    <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"/"</span><span class="p">):</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">download_file_from_opendal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">download_dir_from_opendal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">))</span>

        <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">,</span> <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

OpendalS3Reader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalS3Reader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General reader for any S3 file or directory.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/s3/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OpendalS3Reader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General reader for any S3 file or directory."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">bucket</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/"</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">access_key_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">secret_access_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize S3 bucket and key, along with credentials if needed.</span>

<span class="sd">        If key is not set, the entire bucket (filtered by prefix) is parsed.</span>

<span class="sd">        Args:</span>
<span class="sd">        bucket (str): the name of your S3 bucket</span>
<span class="sd">        path (str): the path of the data. If none is provided,</span>
<span class="sd">            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.</span>
<span class="sd">        endpoint Optional[str]: the endpoint of the S3 service.</span>
<span class="sd">        region: Optional[str]: the region of the S3 service.</span>
<span class="sd">        access_key_id (Optional[str]): provide AWS access key directly.</span>
<span class="sd">        secret_access_key (Optional[str]): provide AWS access key directly.</span>
<span class="sd">        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. See `SimpleDirectoryReader` for more details.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span> <span class="o">=</span> <span class="n">file_extractor</span>

        <span class="c1"># opendal service related config.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">options</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"access_key"</span><span class="p">:</span> <span class="n">access_key_id</span><span class="p">,</span>
            <span class="s2">"secret_key"</span><span class="p">:</span> <span class="n">secret_access_key</span><span class="p">,</span>
            <span class="s2">"endpoint"</span><span class="p">:</span> <span class="n">endpoint</span><span class="p">,</span>
            <span class="s2">"region"</span><span class="p">:</span> <span class="n">region</span><span class="p">,</span>
            <span class="s2">"bucket"</span><span class="p">:</span> <span class="n">bucket</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
        <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
            <span class="n">scheme</span><span class="o">=</span><span class="s2">"s3"</span><span class="p">,</span>
            <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
            <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/#llama_index.readers.opendal.OpendalS3Reader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file(s) from OpenDAL.

Source code in `llama-index-integrations/readers/llama-index-readers-opendal/llama_index/readers/opendal/s3/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file(s) from OpenDAL."""</span>
    <span class="n">loader</span> <span class="o">=</span> <span class="n">OpendalReader</span><span class="p">(</span>
        <span class="n">scheme</span><span class="o">=</span><span class="s2">"s3"</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span>
        <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Openapi](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/)[Next Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/)
