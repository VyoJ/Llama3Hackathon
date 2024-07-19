Title: String iterable - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/

Markdown Content:
String iterable - LlamaIndex


StringIterableReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/#llama_index.readers.string_iterable.StringIterableReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

String Iterable Reader.

Gets a list of documents, given an iterable (e.g. list) of strings.

Example.. code-block:: python

```
from llama_index import TreeIndex
from llama_index.readers import StringIterableReader

documents = StringIterableReader().load_data(
    texts=["I went to the store", "I bought an apple"]
)
index = TreeIndex.from_documents(documents)
query_engine = index.as_query_engine()
query_engine.query("what did I buy?")

# response should be something like "You bought an apple."
```
Source code in `llama-index-integrations/readers/llama-index-readers-string-iterable/llama_index/readers/string_iterable/base.py`

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
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">StringIterableReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""String Iterable Reader.</span>

<span class="sd">    Gets a list of documents, given an iterable (e.g. list) of strings.</span>

<span class="sd">    Example:</span>
<span class="sd">        .. code-block:: python</span>

<span class="sd">            from llama_index import TreeIndex</span>
<span class="sd">            from llama_index.readers import StringIterableReader</span>

<span class="sd">            documents = StringIterableReader().load_data(</span>
<span class="sd">                texts=["I went to the store", "I bought an apple"]</span>
<span class="sd">            )</span>
<span class="sd">            index = TreeIndex.from_documents(documents)</span>
<span class="sd">            query_engine = index.as_query_engine()</span>
<span class="sd">            query_engine.query("what did I buy?")</span>

<span class="sd">            # response should be something like "You bought an apple."</span>
<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"StringIterableReader"</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load the data."""</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">texts</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/#llama_index.readers.string_iterable.StringIterableReader.load_data "Permanent link")

```
load_data(texts: List[str]) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load the data.

Source code in `llama-index-integrations/readers/llama-index-readers-string-iterable/llama_index/readers/string_iterable/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">texts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load the data."""</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">texts</span><span class="p">:</span>
        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Steamship](https://docs.llamaindex.ai/en/stable/api_reference/readers/steamship/)[Next Stripe docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/stripe_docs/)
