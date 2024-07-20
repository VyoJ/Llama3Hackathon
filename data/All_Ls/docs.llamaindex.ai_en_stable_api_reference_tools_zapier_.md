Title: Zapier - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/

Markdown Content:
Zapier - LlamaIndex


Init file.

ZapierToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/#llama_index.tools.zapier.ZapierToolSpec "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Zapier tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-zapier/llama_index/tools/zapier/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
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
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ZapierToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Zapier tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">oauth_access_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"x-api-key"</span><span class="p">:</span> <span class="n">api_key</span><span class="p">}</span>
        <span class="k">elif</span> <span class="n">oauth_access_token</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_headers</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"Authorization"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"Bearer </span><span class="si">{</span><span class="n">oauth_access_token</span><span class="si">}</span><span class="s2">"</span><span class="p">}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must provide either api_key or oauth_access_token"</span><span class="p">)</span>

        <span class="c1"># Get the exposed actions from Zapier</span>
        <span class="n">actions</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list_actions</span><span class="p">())</span>
        <span class="k">if</span> <span class="s2">"results"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"No Zapier actions exposed, visit https://nla.zapier.com/dev/actions/"</span>
                <span class="s2">" to expose actions."</span>
            <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">actions</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]</span>

        <span class="c1"># Register the actions as Tools</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">params</span> <span class="o">=</span> <span class="n">action</span><span class="p">[</span><span class="s2">"params"</span><span class="p">]</span>

            <span class="k">def</span> <span class="nf">function_action</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">action</span><span class="p">[</span><span class="s2">"id"</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">natural_language_query</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

            <span class="n">action_name</span> <span class="o">=</span> <span class="n">action</span><span class="p">[</span><span class="s2">"description"</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">": "</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">" "</span><span class="p">,</span> <span class="s2">"_"</span><span class="p">)</span>
            <span class="n">function_action</span><span class="o">.</span><span class="vm">__name__</span> <span class="o">=</span> <span class="n">action_name</span>
            <span class="n">function_action</span><span class="o">.</span><span class="vm">__doc__</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">                This is a Zapier Natural Language Action function wrapper.</span>

<span class="s2">                The 'instructions' key is REQUIRED for all function calls.</span>
<span class="s2">                The instructions key is a natural language string describing the action to be taken</span>
<span class="s2">                The following are all of the valid arguments you can provide: </span><span class="si">{</span><span class="n">params</span><span class="si">}</span>

<span class="s2">                Ignore the id field, it is provided for you.</span>
<span class="s2">                If the returned error field is not null, interpret the error and try to fix it. Otherwise, inform the user of how they might fix it.</span>
<span class="s2">            """</span>
            <span class="nb">setattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action_name</span><span class="p">,</span> <span class="n">function_action</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">spec_functions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">action_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">list_actions</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s2">"https://nla.zapier.com/api/v1/dynamic/exposed/"</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">text</span>

    <span class="k">def</span> <span class="nf">natural_language_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span>
            <span class="n">ACTION_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">action_id</span><span class="o">=</span><span class="nb">id</span><span class="p">),</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_headers</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">kwargs</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">text</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Yelp](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/)[Next Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/)
