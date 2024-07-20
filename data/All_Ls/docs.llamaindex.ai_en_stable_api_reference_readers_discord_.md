Title: Discord - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/

Markdown Content:
Discord - LlamaIndex


DiscordReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/#llama_index.readers.discord.DiscordReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Discord reader.

Reads conversations from channels.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `discord_token` | `Optional[str]` | 
Discord token. If not provided, we assume the environment variable `DISCORD_TOKEN` is set.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-discord/llama_index/readers/discord/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 88</span>
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
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DiscordReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Discord reader.</span>

<span class="sd">    Reads conversations from channels.</span>

<span class="sd">    Args:</span>
<span class="sd">        discord_token (Optional[str]): Discord token. If not provided, we</span>
<span class="sd">            assume the environment variable `DISCORD_TOKEN` is set.</span>

<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">discord_token</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">discord_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">discord</span>  <span class="c1"># noqa: F401</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`discord.py` package not found, please run `pip install discord.py`"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">discord_token</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">discord_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"DISCORD_TOKEN"</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">discord_token</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify `discord_token` or set environment "</span>
                    <span class="s2">"variable `DISCORD_TOKEN`."</span>
                <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">discord_token</span><span class="o">=</span><span class="n">discord_token</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the name identifier of the class."""</span>
        <span class="k">return</span> <span class="s2">"DiscordReader"</span>

    <span class="k">def</span> <span class="nf">_read_channel</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">channel_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">oldest_first</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Read channel."""</span>
        <span class="k">return</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="n">read_channel</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">discord_token</span><span class="p">,</span> <span class="n">channel_id</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">oldest_first</span><span class="o">=</span><span class="n">oldest_first</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">channel_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span>
        <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">oldest_first</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            channel_ids (List[int]): List of channel ids to read.</span>
<span class="sd">            limit (Optional[int]): Maximum number of messages to read.</span>
<span class="sd">            oldest_first (bool): Whether to read oldest messages first.</span>
<span class="sd">                Defaults to `True`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>

<span class="sd">        """</span>
        <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">channel_id</span> <span class="ow">in</span> <span class="n">channel_ids</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">channel_id</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Channel id </span><span class="si">{</span><span class="n">channel_id</span><span class="si">}</span><span class="s2"> must be an integer, "</span>
                    <span class="sa">f</span><span class="s2">"not </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">channel_id</span><span class="p">)</span><span class="si">}</span><span class="s2">."</span>
                <span class="p">)</span>
            <span class="n">channel_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_channel</span><span class="p">(</span>
                <span class="n">channel_id</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">oldest_first</span><span class="o">=</span><span class="n">oldest_first</span>
            <span class="p">)</span>
            <span class="n">results</span> <span class="o">+=</span> <span class="n">channel_documents</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/#llama_index.readers.discord.DiscordReader.class_name "Permanent link")

```
class_name() -> str
```

Get the name identifier of the class.

Source code in `llama-index-integrations/readers/llama-index-readers-discord/llama_index/readers/discord/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the name identifier of the class."""</span>
    <span class="k">return</span> <span class="s2">"DiscordReader"</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/#llama_index.readers.discord.DiscordReader.load_data "Permanent link")

```
load_data(channel_ids: List[int], limit: Optional[int] = None, oldest_first: bool = True) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `channel_ids` | `List[int]` | 
List of channel ids to read.



 | _required_ |
| `limit` | `Optional[int]` | 

Maximum number of messages to read.



 | `None` |
| `oldest_first` | `bool` | 

Whether to read oldest messages first. Defaults to `True`.



 | `True` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-discord/llama_index/readers/discord/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">channel_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span>
    <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">oldest_first</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        channel_ids (List[int]): List of channel ids to read.</span>
<span class="sd">        limit (Optional[int]): Maximum number of messages to read.</span>
<span class="sd">        oldest_first (bool): Whether to read oldest messages first.</span>
<span class="sd">            Defaults to `True`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>
    <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">channel_id</span> <span class="ow">in</span> <span class="n">channel_ids</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">channel_id</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Channel id </span><span class="si">{</span><span class="n">channel_id</span><span class="si">}</span><span class="s2"> must be an integer, "</span>
                <span class="sa">f</span><span class="s2">"not </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">channel_id</span><span class="p">)</span><span class="si">}</span><span class="s2">."</span>
            <span class="p">)</span>
        <span class="n">channel_documents</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_channel</span><span class="p">(</span>
            <span class="n">channel_id</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">oldest_first</span><span class="o">=</span><span class="n">oldest_first</span>
        <span class="p">)</span>
        <span class="n">results</span> <span class="o">+=</span> <span class="n">channel_documents</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/readers/deeplake/)[Next Docstring walker](https://docs.llamaindex.ai/en/stable/api_reference/readers/docstring_walker/)
