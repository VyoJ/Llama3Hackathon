Title: Replicate - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/

Markdown Content:
Replicate - LlamaIndex


ReplicateMultiModal [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/#llama_index.multi_modal_llms.replicate.ReplicateMultiModal "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MultiModalLLM](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "llama_index.core.multi_modal_llms.MultiModalLLM")`

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-replicate/llama_index/multi_modal_llms/replicate/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 35</span>
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
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ReplicateMultiModal</span><span class="p">(</span><span class="n">MultiModalLLM</span><span class="p">):</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The Multi-Modal model to use from Replicate."</span><span class="p">)</span>
    <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The temperature to use for sampling. Adjusts randomness of outputs, greater than 1 is random and 0 is deterministic."</span>
    <span class="p">)</span>
    <span class="n">max_new_tokens</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">" The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt"</span>
    <span class="p">)</span>
    <span class="n">context_window</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The maximum number of context tokens for the model."</span>
    <span class="p">)</span>
    <span class="n">prompt_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The key to use for the prompt in API calls."</span><span class="p">)</span>
    <span class="n">image_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The key to use for the image in API calls."</span><span class="p">)</span>
    <span class="n">top_p</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"When decoding text, samples from the top p percentage of most likely tokens; lower to ignore less likely tokens."</span>
    <span class="p">)</span>
    <span class="n">num_beams</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"Number of beams for beam search decoding."</span><span class="p">)</span>
    <span class="n">repetition_penalty</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Penalty for repeated words in generated text; 1 is no penalty, values greater than 1 discourage repetition, less than 1 encourage it."</span>
    <span class="p">)</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Additional kwargs for the Replicate API."</span>
    <span class="p">)</span>

    <span class="n">_messages_to_prompt</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_completion_to_prompt</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">REPLICATE_MULTI_MODAL_LLM_MODELS</span><span class="p">[</span><span class="s2">"fuyu-8b"</span><span class="p">],</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.75</span><span class="p">,</span>
        <span class="n">max_new_tokens</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">512</span><span class="p">,</span>
        <span class="n">num_input_files</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">context_window</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_CONTEXT_WINDOW</span><span class="p">,</span>
        <span class="n">prompt_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"prompt"</span><span class="p">,</span>
        <span class="n">image_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"image"</span><span class="p">,</span>
        <span class="n">repetition_penalty</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span>
        <span class="n">num_beams</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">top_p</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.9</span><span class="p">,</span>
        <span class="n">messages_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">completion_to_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_messages_to_prompt</span> <span class="o">=</span> <span class="n">messages_to_prompt</span> <span class="ow">or</span> <span class="n">generic_messages_to_prompt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_completion_to_prompt</span> <span class="o">=</span> <span class="n">completion_to_prompt</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">max_new_tokens</span><span class="o">=</span><span class="n">max_new_tokens</span><span class="p">,</span>
            <span class="n">num_input_files</span><span class="o">=</span><span class="n">num_input_files</span><span class="p">,</span>
            <span class="n">repetition_penalty</span><span class="o">=</span><span class="n">repetition_penalty</span><span class="p">,</span>
            <span class="n">num_beams</span><span class="o">=</span><span class="n">num_beams</span><span class="p">,</span>
            <span class="n">top_p</span><span class="o">=</span><span class="n">top_p</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">additional_kwargs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">context_window</span><span class="o">=</span><span class="n">context_window</span><span class="p">,</span>
            <span class="n">prompt_key</span><span class="o">=</span><span class="n">prompt_key</span><span class="p">,</span>
            <span class="n">image_key</span><span class="o">=</span><span class="n">image_key</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"replicate_multi_modal_llm"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Multi Modal LLM metadata."""</span>
        <span class="k">return</span> <span class="n">MultiModalLLMMetadata</span><span class="p">(</span>
            <span class="n">context_window</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">context_window</span><span class="p">,</span>
            <span class="n">num_output</span><span class="o">=</span><span class="n">DEFAULT_NUM_OUTPUTS</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_model_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">base_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"temperature"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">temperature</span><span class="p">,</span>
            <span class="s2">"max_length"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_window</span><span class="p">,</span>
            <span class="s2">"max_new_tokens"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_new_tokens</span><span class="p">,</span>
            <span class="s2">"num_beams"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_beams</span><span class="p">,</span>
            <span class="s2">"repetition_penalty"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">repetition_penalty</span><span class="p">,</span>
            <span class="s2">"top_p"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">top_p</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="o">**</span><span class="n">base_kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_get_multi_modal_chat_messages</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_document</span><span class="p">:</span> <span class="n">ImageDocument</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">image_document</span><span class="o">.</span><span class="n">image_path</span><span class="p">:</span>
            <span class="c1"># load local image file and pass file handler to replicate</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">return</span> <span class="p">{</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">prompt_key</span><span class="p">:</span> <span class="n">prompt</span><span class="p">,</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">image_key</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">image_document</span><span class="o">.</span><span class="n">image_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">),</span>
                    <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
                    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
                <span class="p">}</span>
            <span class="k">except</span> <span class="ne">FileNotFoundError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">FileNotFoundError</span><span class="p">(</span>
                    <span class="s2">"Could not load local image file. Please check whether the file exists"</span>
                <span class="p">)</span>
        <span class="k">elif</span> <span class="n">image_document</span><span class="o">.</span><span class="n">image_url</span><span class="p">:</span>
            <span class="c1"># load remote image url and pass file url to replicate</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">prompt_key</span><span class="p">:</span> <span class="n">prompt</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">image_key</span><span class="p">:</span> <span class="n">image_document</span><span class="o">.</span><span class="n">image_url</span><span class="p">,</span>
                <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
                <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
            <span class="p">}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">FileNotFoundError</span><span class="p">(</span>
                <span class="s2">"Could not load image file. Please check whether the file exists"</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">response_gen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">response_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">response_gen</span><span class="p">)</span>
        <span class="n">final_response</span> <span class="o">=</span> <span class="n">response_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="n">final_response</span><span class="o">.</span><span class="n">delta</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">replicate</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Could not import replicate library."</span>
                <span class="s2">"Please install replicate with `pip install replicate`"</span>
            <span class="p">)</span>

        <span class="c1"># TODO: at the current moment, only support uploading one image document</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">image_documents</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"ReplicateMultiModal currently only supports uploading one image document"</span>
                <span class="s2">"we are using the first image document for completion."</span>
            <span class="p">)</span>

        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_completion_to_prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
        <span class="n">input_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="c1"># using the first image for single image completion</span>
            <span class="n">prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">REPLICATE_MULTI_MODAL_LLM_MODELS</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Unknown model </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="si">!r}</span><span class="s2">. Please provide a valid Replicate Multi-Modal model name in:"</span>
                <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">REPLICATE_MULTI_MODAL_LLM_MODELS</span><span class="o">.</span><span class="n">values</span><span class="p">())</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="n">response_iter</span> <span class="o">=</span> <span class="n">replicate</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="nb">input</span><span class="o">=</span><span class="n">input_dict</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">delta</span> <span class="ow">in</span> <span class="n">response_iter</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
                <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="c1"># </span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">response_gen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_complete</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="n">response_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">response_gen</span><span class="p">)</span>
        <span class="n">final_response</span> <span class="o">=</span> <span class="n">response_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="n">final_response</span><span class="o">.</span><span class="n">delta</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">final_response</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">replicate</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Could not import replicate library."</span>
                <span class="s2">"Please install replicate with `pip install replicate`"</span>
            <span class="p">)</span>

        <span class="c1"># TODO: at the current moment, only support uploading one image document</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">image_documents</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"ReplicateMultiModal currently only supports uploading one image document"</span>
                <span class="s2">"we are using the first image document for completion."</span>
            <span class="p">)</span>

        <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_completion_to_prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
        <span class="n">input_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_multi_modal_chat_messages</span><span class="p">(</span>
            <span class="c1"># using the first image for single image completion</span>
            <span class="n">prompt</span><span class="p">,</span>
            <span class="n">image_documents</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">REPLICATE_MULTI_MODAL_LLM_MODELS</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Unknown model </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="si">!r}</span><span class="s2">. Please provide a valid Replicate Multi-Modal model name in:"</span>
                <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">REPLICATE_MULTI_MODAL_LLM_MODELS</span><span class="o">.</span><span class="n">values</span><span class="p">())</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="n">response_iter</span> <span class="o">=</span> <span class="n">replicate</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="nb">input</span><span class="o">=</span><span class="n">input_dict</span><span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">delta</span> <span class="ow">in</span> <span class="n">response_iter</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
                <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### metadata `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/#llama_index.multi_modal_llms.replicate.ReplicateMultiModal.metadata "Permanent link")

```
metadata: MultiModalLLMMetadata
```

Multi Modal LLM metadata.

Back to top

[Previous Openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/)[Next Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/)
