Title: Searchain - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/searchain/

Markdown Content:
Searchain - LlamaIndex


SearChainPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/searchain/#llama_index.packs.searchain.SearChainPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Simple short form SearChain pack.

Source code in `llama-index-packs/llama-index-packs-searchain/llama_index/packs/searchain/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 48</span>
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
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SearChainPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple short form SearChain pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">data_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">dprtokenizer_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/dpr_reader_multi"</span><span class="p">,</span>
        <span class="n">dprmodel_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/dpr_reader_multi"</span><span class="p">,</span>
        <span class="n">crossencoder_name_or_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"/Quora_cross_encoder"</span><span class="p">,</span>
        <span class="n">device</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cuda"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">device</span> <span class="o">=</span> <span class="n">device</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">crossencoder</span> <span class="o">=</span> <span class="n">CrossEncoder</span><span class="p">(</span><span class="n">crossencoder_name_or_path</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">documents</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span><span class="n">data_path</span><span class="p">)</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">documents</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">dprtokenizer</span> <span class="o">=</span> <span class="n">DPRReaderTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">dprtokenizer_path</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dprmodel</span> <span class="o">=</span> <span class="n">DPRReader</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="n">dprmodel_path</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dprmodel</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dprmodel</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_answer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">texts</span><span class="p">,</span> <span class="n">title</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"texts:"</span> <span class="o">+</span> <span class="n">texts</span><span class="p">)</span>
        <span class="n">encoded_inputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dprtokenizer</span><span class="p">(</span>
            <span class="n">questions</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span>
            <span class="n">titles</span><span class="o">=</span><span class="p">[</span><span class="n">title</span><span class="p">],</span>
            <span class="n">texts</span><span class="o">=</span><span class="p">[</span><span class="n">texts</span><span class="p">],</span>
            <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">,</span>
            <span class="n">max_length</span><span class="o">=</span><span class="mi">510</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dprmodel</span><span class="p">(</span><span class="o">**</span><span class="n">encoded_inputs</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">device</span><span class="p">))</span>
        <span class="n">start_logits</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">start_logits</span>
        <span class="n">end_logits</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">end_logits</span>
        <span class="n">relevance_logits</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">relevance_logits</span>

        <span class="n">answer_start_index</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">start_logits</span><span class="o">.</span><span class="n">argmax</span><span class="p">()</span>
        <span class="n">answer_end_index</span> <span class="o">=</span> <span class="n">outputs</span><span class="o">.</span><span class="n">end_logits</span><span class="o">.</span><span class="n">argmax</span><span class="p">()</span>
        <span class="n">predict_answer_tokens</span> <span class="o">=</span> <span class="n">encoded_inputs</span><span class="o">.</span><span class="n">input_ids</span><span class="p">[</span>
            <span class="mi">0</span><span class="p">,</span> <span class="n">answer_start_index</span> <span class="p">:</span> <span class="n">answer_end_index</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="p">]</span>
        <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dprtokenizer</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">predict_answer_tokens</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">answer</span><span class="p">,</span> <span class="n">relevance_logits</span>

    <span class="k">def</span> <span class="nf">_ir</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">,</span> <span class="n">query_seen_list</span><span class="p">):</span>
        <span class="n">flag_contibue_label</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="n">query_list</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">message</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">query_list</span><span class="p">)):</span>
            <span class="n">query_item</span> <span class="o">=</span> <span class="n">query_list</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="k">if</span> <span class="s2">"Query"</span> <span class="ow">in</span> <span class="n">query_item</span> <span class="ow">and</span> <span class="s2">"]:"</span> <span class="ow">in</span> <span class="n">query_item</span><span class="p">:</span>
                <span class="n">temp</span> <span class="o">=</span> <span class="n">query_item</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"]"</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="n">query_type</span> <span class="o">=</span> <span class="n">temp</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">query_item</span> <span class="o">=</span> <span class="n">temp</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
                <span class="k">if</span> <span class="s2">":"</span> <span class="ow">in</span> <span class="n">query_item</span><span class="p">:</span>
                    <span class="n">query_item</span> <span class="o">=</span> <span class="n">query_item</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">_have_seen_or_not</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">crossencoder</span><span class="p">,</span> <span class="n">query_item</span><span class="p">,</span> <span class="n">query_seen_list</span><span class="p">,</span> <span class="n">query_type</span>
                <span class="p">):</span>
                    <span class="n">now_reference</span> <span class="o">=</span> <span class="p">{}</span>
                    <span class="n">query_seen_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">query_item</span><span class="p">)</span>
                    <span class="n">response</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_item</span><span class="p">))</span>

                    <span class="n">answer</span><span class="p">,</span> <span class="n">relevance_score</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_answer</span><span class="p">(</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query_item</span><span class="p">,</span> <span class="n">texts</span><span class="o">=</span><span class="s2">""</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">response</span>
                    <span class="p">)</span>
                    <span class="n">now_reference</span><span class="p">[</span><span class="s2">"query"</span><span class="p">]</span> <span class="o">=</span> <span class="n">query_item</span>
                    <span class="n">now_reference</span><span class="p">[</span><span class="s2">"answer"</span><span class="p">]</span> <span class="o">=</span> <span class="n">answer</span>
                    <span class="n">now_reference</span><span class="p">[</span><span class="s2">"reference"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response</span>
                    <span class="n">now_reference</span><span class="p">[</span><span class="s2">"ref_score"</span><span class="p">]</span> <span class="o">=</span> <span class="n">relevance_score</span>
                    <span class="n">now_reference</span><span class="p">[</span><span class="s2">"idx"</span><span class="p">]</span> <span class="o">=</span> <span class="n">response</span>

                    <span class="k">if</span> <span class="s2">"Unsolved"</span> <span class="ow">in</span> <span class="n">query_type</span><span class="p">:</span>
                        <span class="n">message</span> <span class="o">=</span> <span class="s2">"[Unsolved Query]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;[Answer]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;[Reference]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                            <span class="n">query_item</span><span class="p">,</span> <span class="n">answer</span><span class="p">,</span> <span class="n">response</span>
                        <span class="p">)</span>
                        <span class="n">flag_contibue_label</span> <span class="o">=</span> <span class="kc">True</span>
                        <span class="k">break</span>
                    <span class="k">elif</span> <span class="n">relevance_score</span> <span class="o">&gt;</span> <span class="mf">1.5</span><span class="p">:</span>
                        <span class="n">answer_start_idx</span> <span class="o">=</span> <span class="n">idx</span> <span class="o">+</span> <span class="mi">1</span>
                        <span class="n">predict_answer</span> <span class="o">=</span> <span class="s2">""</span>
                        <span class="k">while</span> <span class="n">answer_start_idx</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_list</span><span class="p">):</span>
                            <span class="k">if</span> <span class="s2">"Answer"</span> <span class="ow">in</span> <span class="n">query_list</span><span class="p">[</span><span class="n">answer_start_idx</span><span class="p">]:</span>
                                <span class="n">predict_answer</span> <span class="o">=</span> <span class="n">query_list</span><span class="p">[</span><span class="n">answer_start_idx</span><span class="p">]</span>
                                <span class="k">break</span>
                            <span class="n">answer_start_idx</span> <span class="o">+=</span> <span class="mi">1</span>
                        <span class="n">match_label</span> <span class="o">=</span> <span class="n">_match_or_not</span><span class="p">(</span>
                            <span class="n">prediction</span><span class="o">=</span><span class="n">predict_answer</span><span class="p">,</span> <span class="n">ground_truth</span><span class="o">=</span><span class="n">answer</span>
                        <span class="p">)</span>
                        <span class="k">if</span> <span class="n">match_label</span><span class="p">:</span>
                            <span class="k">continue</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">message</span> <span class="o">=</span> <span class="s2">"[Query]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;[Answer]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;[Reference]:</span><span class="si">{}</span><span class="s2">&lt;SEP&gt;"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                                <span class="n">query_item</span><span class="p">,</span> <span class="n">answer</span><span class="p">,</span> <span class="n">response</span>
                            <span class="p">)</span>
                            <span class="n">flag_contibue_label</span> <span class="o">=</span> <span class="kc">True</span>
                            <span class="k">break</span>
        <span class="k">return</span> <span class="n">message</span><span class="p">,</span> <span class="n">flag_contibue_label</span><span class="p">,</span> <span class="n">query_seen_list</span>

    <span class="k">def</span> <span class="nf">_extract</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_keys_list</span><span class="p">):</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">message_keys_list</span>
        <span class="n">idx</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">idx</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">idx</span> <span class="o">=</span> <span class="n">idx</span> <span class="o">-</span> <span class="mi">1</span>
            <span class="n">item</span> <span class="o">=</span> <span class="n">text</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">role</span> <span class="o"></span> <span class="s2">"end"</span><span class="p">:</span>
                    <span class="k">break</span>
                <span class="c1"># [Query]:xxxx&lt;SEP&gt;[Answer]:xxxx&lt;SEP&gt;[Reference]:xxxx&lt;SEP&gt;</span>
                <span class="n">feedback_list</span> <span class="o">=</span> <span class="n">feedback</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"&lt;SEP&gt;"</span><span class="p">)</span>
                <span class="k">if</span> <span class="s2">"Unsolved Query"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">feedback</span><span class="p">:</span>
                    <span class="n">new_prompt</span> <span class="o">=</span> <span class="s2">"""Reference: </span><span class="si">{}</span><span class="s2"> According to this Reference, the answer for "</span><span class="si">{}</span><span class="s2">" should be "</span><span class="si">{}</span><span class="s2">", you can change your answer based on the Reference and continue constructing the reasoning chain to give the final answer for [Question]:</span><span class="si">{}</span><span class="s2">"""</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                        <span class="n">feedback_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">feedback_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">q</span><span class="p">,</span> <span class="n">feedback_list</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">new_prompt</span> <span class="o">=</span> <span class="s2">"""Reference: </span><span class="si">{}</span><span class="s2"> According to this Reference, the answer for "</span><span class="si">{}</span><span class="s2">" should be "</span><span class="si">{}</span><span class="s2">", you can give your answer based on the Reference and continue constructing the reasoning chain to give the final answer for [Question]：</span><span class="si">{}</span><span class="s2"> """</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                        <span class="n">feedback_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">feedback_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">q</span><span class="p">,</span> <span class="n">feedback_list</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
                    <span class="p">)</span>
                <span class="n">message_keys_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="s2">"user"</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">new_prompt</span><span class="p">))</span>
            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract</span><span class="p">(</span><span class="n">message_keys_list</span><span class="p">)</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

        <span class="k">return</span> <span class="o">-</span><span class="mi">1</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Retry engine weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/retry_engine_weaviate/)[Next Secgpt](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/)
