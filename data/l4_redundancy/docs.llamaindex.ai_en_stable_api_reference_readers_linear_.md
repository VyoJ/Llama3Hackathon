Title: Linear - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/linear/

Markdown Content:
Linear - LlamaIndex


LinearReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/linear/#llama_index.readers.linear.LinearReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Linear reader. Reads data from Linear issues for the passed query.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_key` | `str` | 
Personal API token.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-linear/llama_index/readers/linear/base.py`

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
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LinearReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Linear reader. Reads data from Linear issues for the passed query.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key (str): Personal API token.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="c1"># Define the GraphQL query</span>
        <span class="n">graphql_endpoint</span> <span class="o">=</span> <span class="s2">"https://api.linear.app/graphql"</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">}</span>

        <span class="c1"># Make the GraphQL request</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">graphql_endpoint</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">payload</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="c1"># Extract relevant information</span>
        <span class="n">issues</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">team_data</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"data"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"team"</span><span class="p">,</span> <span class="p">{})</span>
        <span class="k">for</span> <span class="n">issue</span> <span class="ow">in</span> <span class="n">team_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"issues"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="n">assignee</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"assignee"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">labels</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">label_node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">label_node</span> <span class="ow">in</span> <span class="n">issue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"labels"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[])</span>
            <span class="p">]</span>
            <span class="n">project</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"project"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">state</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"state"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">creator</span> <span class="o">=</span> <span class="n">issue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"creator"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

            <span class="n">issues</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">issue</span><span class="p">[</span><span class="s1">'title'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">\n</span><span class="s2"> </span><span class="si">{</span><span class="n">issue</span><span class="p">[</span><span class="s1">'description'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">"id"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span>
                        <span class="s2">"title"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"title"</span><span class="p">],</span>
                        <span class="s2">"created_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"createdAt"</span><span class="p">],</span>
                        <span class="s2">"archived_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"archivedAt"</span><span class="p">],</span>
                        <span class="s2">"auto_archived_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"autoArchivedAt"</span><span class="p">],</span>
                        <span class="s2">"auto_closed_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"autoClosedAt"</span><span class="p">],</span>
                        <span class="s2">"branch_name"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"branchName"</span><span class="p">],</span>
                        <span class="s2">"canceled_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"canceledAt"</span><span class="p">],</span>
                        <span class="s2">"completed_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"completedAt"</span><span class="p">],</span>
                        <span class="s2">"creator"</span><span class="p">:</span> <span class="n">creator</span><span class="p">,</span>
                        <span class="s2">"due_date"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"dueDate"</span><span class="p">],</span>
                        <span class="s2">"estimate"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"estimate"</span><span class="p">],</span>
                        <span class="s2">"labels"</span><span class="p">:</span> <span class="n">labels</span><span class="p">,</span>
                        <span class="s2">"project"</span><span class="p">:</span> <span class="n">project</span><span class="p">,</span>
                        <span class="s2">"state"</span><span class="p">:</span> <span class="n">state</span><span class="p">,</span>
                        <span class="s2">"updated_at"</span><span class="p">:</span> <span class="n">issue</span><span class="p">[</span><span class="s2">"updatedAt"</span><span class="p">],</span>
                        <span class="s2">"assignee"</span><span class="p">:</span> <span class="n">assignee</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">issues</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Lilac](https://docs.llamaindex.ai/en/stable/api_reference/readers/lilac/)[Next Llama parse](https://docs.llamaindex.ai/en/stable/api_reference/readers/llama_parse/)
