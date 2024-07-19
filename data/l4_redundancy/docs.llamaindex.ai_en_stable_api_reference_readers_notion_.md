Title: Notion - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/

Markdown Content:
Notion - LlamaIndex


NotionPageReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`

Notion Page reader.

Reads a set of Notion pages.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `integration_token` | `str` | 
Notion integration token.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
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
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NotionPageReader</span><span class="p">(</span><span class="n">BasePydanticReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Notion Page reader.</span>

<span class="sd">    Reads a set of Notion pages.</span>

<span class="sd">    Args:</span>
<span class="sd">        integration_token (str): Notion integration token.</span>

<span class="sd">    """</span>

    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">token</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">headers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">integration_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="k">if</span> <span class="n">integration_token</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">integration_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="n">INTEGRATION_TOKEN_NAME</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">integration_token</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Must specify `integration_token` or set environment "</span>
                    <span class="s2">"variable `NOTION_INTEGRATION_TOKEN`."</span>
                <span class="p">)</span>

        <span class="n">token</span> <span class="o">=</span> <span class="n">integration_token</span>
        <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"Authorization"</span><span class="p">:</span> <span class="s2">"Bearer "</span> <span class="o">+</span> <span class="n">token</span><span class="p">,</span>
            <span class="s2">"Content-Type"</span><span class="p">:</span> <span class="s2">"application/json"</span><span class="p">,</span>
            <span class="s2">"Notion-Version"</span><span class="p">:</span> <span class="s2">"2022-06-28"</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">token</span><span class="o">=</span><span class="n">token</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the name identifier of the class."""</span>
        <span class="k">return</span> <span class="s2">"NotionPageReader"</span>

    <span class="k">def</span> <span class="nf">_read_block</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">num_tabs</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Read a block."""</span>
        <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="n">result_lines_arr</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">cur_block_id</span> <span class="o">=</span> <span class="n">block_id</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span><span class="p">:</span>
            <span class="n">block_url</span> <span class="o">=</span> <span class="n">BLOCK_CHILD_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">block_id</span><span class="o">=</span><span class="n">cur_block_id</span><span class="p">)</span>
            <span class="n">query_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
                <span class="s2">"GET"</span><span class="p">,</span> <span class="n">block_url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span>
            <span class="p">)</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
                <span class="n">result_type</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span>
                <span class="n">result_obj</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="n">result_type</span><span class="p">]</span>

                <span class="n">cur_result_text_arr</span> <span class="o">=</span> <span class="p">[]</span>
                <span class="k">if</span> <span class="s2">"rich_text"</span> <span class="ow">in</span> <span class="n">result_obj</span><span class="p">:</span>
                    <span class="k">for</span> <span class="n">rich_text</span> <span class="ow">in</span> <span class="n">result_obj</span><span class="p">[</span><span class="s2">"rich_text"</span><span class="p">]:</span>
                        <span class="c1"># skip if doesn't have text object</span>
                        <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">in</span> <span class="n">rich_text</span><span class="p">:</span>
                            <span class="n">text</span> <span class="o">=</span> <span class="n">rich_text</span><span class="p">[</span><span class="s2">"text"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">]</span>
                            <span class="n">prefix</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\t</span><span class="s2">"</span> <span class="o">*</span> <span class="n">num_tabs</span>
                            <span class="n">cur_result_text_arr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">prefix</span> <span class="o">+</span> <span class="n">text</span><span class="p">)</span>

                <span class="n">result_block_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
                <span class="n">has_children</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"has_children"</span><span class="p">]</span>
                <span class="k">if</span> <span class="n">has_children</span><span class="p">:</span>
                    <span class="n">children_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_block</span><span class="p">(</span>
                        <span class="n">result_block_id</span><span class="p">,</span> <span class="n">num_tabs</span><span class="o">=</span><span class="n">num_tabs</span> <span class="o">+</span> <span class="mi">1</span>
                    <span class="p">)</span>
                    <span class="n">cur_result_text_arr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">children_text</span><span class="p">)</span>

                <span class="n">cur_result_text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">cur_result_text_arr</span><span class="p">)</span>
                <span class="n">result_lines_arr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">cur_result_text</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">break</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">cur_block_id</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span>

        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">result_lines_arr</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_request_with_retry</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">method</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">headers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">json</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">requests</span><span class="o">.</span><span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Make a request with retry and rate limit handling."""</span>
        <span class="n">max_retries</span> <span class="o">=</span> <span class="mi">5</span>
        <span class="n">backoff_factor</span> <span class="o">=</span> <span class="mi">1</span>

        <span class="k">for</span> <span class="n">attempt</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">max_retries</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">method</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">json</span><span class="p">)</span>
                <span class="n">response</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
                <span class="k">return</span> <span class="n">response</span>
            <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">HTTPError</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">==</span> <span class="mi">429</span><span class="p">:</span>
                    <span class="c1"># Rate limit exceeded</span>
                    <span class="n">retry_after</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">headers</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Retry-After"</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
                    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">backoff_factor</span> <span class="o">*</span> <span class="p">(</span><span class="mi">2</span><span class="o">**</span><span class="n">attempt</span><span class="p">)</span> <span class="o">+</span> <span class="n">retry_after</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">HTTPError</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"Request failed: </span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>
            <span class="k">except</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RequestException</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">requests</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">RequestException</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Request failed: </span><span class="si">{</span><span class="n">err</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Maximum retries exceeded"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">read_page</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Read a page."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_block</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">query_database</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">database_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_size"</span><span class="p">:</span> <span class="mi">100</span><span class="p">}</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all the pages from a Notion database."""</span>
        <span class="n">pages</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
            <span class="s2">"POST"</span><span class="p">,</span>
            <span class="n">DATABASE_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">),</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

        <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"results"</span><span class="p">))</span>

        <span class="k">while</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"has_more"</span><span class="p">):</span>
            <span class="n">query_dict</span><span class="p">[</span><span class="s2">"start_cursor"</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"next_cursor"</span><span class="p">)</span>
            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
                <span class="s2">"POST"</span><span class="p">,</span>
                <span class="n">DATABASE_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">),</span>
                <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
                <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"results"</span><span class="p">))</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">page</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Search Notion page given a text query."""</span>
        <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="n">next_cursor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">page_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span><span class="p">:</span>
            <span class="n">query_dict</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="n">next_cursor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">query_dict</span><span class="p">[</span><span class="s2">"start_cursor"</span><span class="p">]</span> <span class="o">=</span> <span class="n">next_cursor</span>
            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
                <span class="s2">"POST"</span><span class="p">,</span> <span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span>
            <span class="p">)</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
                <span class="n">page_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
                <span class="n">page_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="k">break</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">next_cursor</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">page_ids</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">page_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="n">database_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            page_ids (List[str]): List of page ids to load.</span>
<span class="sd">            database_ids Optional (List[str]): List database ids from which to load page ids.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">page_ids</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">database_ids</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify either `page_ids` or `database_ids`."</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">database_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">database_id</span> <span class="ow">in</span> <span class="n">database_ids</span><span class="p">:</span>
                <span class="c1"># get all the pages in the database</span>
                <span class="n">page_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_database</span><span class="p">(</span><span class="n">database_id</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
                    <span class="n">page_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_page</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>
                    <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Document</span><span class="p">(</span>
                            <span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"page_id"</span><span class="p">:</span> <span class="n">page_id</span><span class="p">}</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
                <span class="n">page_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_page</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"page_id"</span><span class="p">:</span> <span class="n">page_id</span><span class="p">}</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">list_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""List all databases in the Notion workspace."""</span>
        <span class="n">query_dict</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filter"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"property"</span><span class="p">:</span> <span class="s2">"object"</span><span class="p">,</span> <span class="s2">"value"</span><span class="p">:</span> <span class="s2">"database"</span><span class="p">}}</span>
        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
            <span class="s2">"POST"</span><span class="p">,</span> <span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span>
        <span class="p">)</span>
        <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">db</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="k">for</span> <span class="n">db</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]]</span>
</code></pre></div></td></tr></tbody></table>

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.class_name "Permanent link")

```
class_name() -> str
```

Get the name identifier of the class.

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the name identifier of the class."""</span>
    <span class="k">return</span> <span class="s2">"NotionPageReader"</span>
</code></pre></div></td></tr></tbody></table>

### read\_page [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.read_page "Permanent link")

```
read_page(page_id: str) -> str
```

Read a page.

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">read_page</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">page_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Read a page."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_read_block</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query\_database [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.query_database "Permanent link")

```
query_database(database_id: str, query_dict: Dict[str, Any] = {'page_size': 100}) -> List[str]
```

Get all the pages from a Notion database.

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

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
<span class="normal">164</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query_database</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">database_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_size"</span><span class="p">:</span> <span class="mi">100</span><span class="p">}</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all the pages from a Notion database."""</span>
    <span class="n">pages</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
        <span class="s2">"POST"</span><span class="p">,</span>
        <span class="n">DATABASE_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">),</span>
        <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
        <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>

    <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"results"</span><span class="p">))</span>

    <span class="k">while</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"has_more"</span><span class="p">):</span>
        <span class="n">query_dict</span><span class="p">[</span><span class="s2">"start_cursor"</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"next_cursor"</span><span class="p">)</span>
        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
            <span class="s2">"POST"</span><span class="p">,</span>
            <span class="n">DATABASE_URL_TMPL</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">database_id</span><span class="o">=</span><span class="n">database_id</span><span class="p">),</span>
            <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">pages</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"results"</span><span class="p">))</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">page</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">pages</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### search [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.search "Permanent link")

```
search(query: str) -> List[str]
```

Search Notion page given a text query.

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Search Notion page given a text query."""</span>
    <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">next_cursor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">page_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span><span class="p">:</span>
        <span class="n">query_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">query</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">next_cursor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_dict</span><span class="p">[</span><span class="s2">"start_cursor"</span><span class="p">]</span> <span class="o">=</span> <span class="n">next_cursor</span>
        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
            <span class="s2">"POST"</span><span class="p">,</span> <span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span>
        <span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]:</span>
            <span class="n">page_id</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span>
            <span class="n">page_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="k">break</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">next_cursor</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s2">"next_cursor"</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">page_ids</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.load_data "Permanent link")

```
load_data(page_ids: List[str] = [], database_ids: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `page_ids` | `List[str]` | 
List of page ids to load.



 | `[]` |
| `database_ids` | `Optional (List[str]` | 

List database ids from which to load page ids.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">page_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="n">database_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        page_ids (List[str]): List of page ids to load.</span>
<span class="sd">        database_ids Optional (List[str]): List database ids from which to load page ids.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">page_ids</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">database_ids</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Must specify either `page_ids` or `database_ids`."</span><span class="p">)</span>
    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">database_ids</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">database_id</span> <span class="ow">in</span> <span class="n">database_ids</span><span class="p">:</span>
            <span class="c1"># get all the pages in the database</span>
            <span class="n">page_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_database</span><span class="p">(</span><span class="n">database_id</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
                <span class="n">page_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_page</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"page_id"</span><span class="p">:</span> <span class="n">page_id</span><span class="p">}</span>
                    <span class="p">)</span>
                <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">page_id</span> <span class="ow">in</span> <span class="n">page_ids</span><span class="p">:</span>
            <span class="n">page_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_page</span><span class="p">(</span><span class="n">page_id</span><span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">id_</span><span class="o">=</span><span class="n">page_id</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="p">{</span><span class="s2">"page_id"</span><span class="p">:</span> <span class="n">page_id</span><span class="p">}</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### list\_databases [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/#llama_index.readers.notion.NotionPageReader.list_databases "Permanent link")

```
list_databases() -> List[str]
```

List all databases in the Notion workspace.

Source code in `llama-index-integrations/readers/llama-index-readers-notion/llama_index/readers/notion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""List all databases in the Notion workspace."""</span>
    <span class="n">query_dict</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filter"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"property"</span><span class="p">:</span> <span class="s2">"object"</span><span class="p">,</span> <span class="s2">"value"</span><span class="p">:</span> <span class="s2">"database"</span><span class="p">}}</span>
    <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_with_retry</span><span class="p">(</span>
        <span class="s2">"POST"</span><span class="p">,</span> <span class="n">SEARCH_URL</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">,</span> <span class="n">json</span><span class="o">=</span><span class="n">query_dict</span>
    <span class="p">)</span>
    <span class="n">res</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">res</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">db</span><span class="p">[</span><span class="s2">"id"</span><span class="p">]</span> <span class="k">for</span> <span class="n">db</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s2">"results"</span><span class="p">]]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Myscale](https://docs.llamaindex.ai/en/stable/api_reference/readers/myscale/)[Next Nougat ocr](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/)
