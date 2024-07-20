Title: Gemini - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/

Markdown Content:
Gemini - LlamaIndex


GeminiMultiModal [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/#llama_index.multi_modal_llms.gemini.GeminiMultiModal "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MultiModalLLM](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "llama_index.core.multi_modal_llms.MultiModalLLM")`

Gemini multimodal.

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-gemini/llama_index/multi_modal_llms/gemini/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 47</span>
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
<span class="normal">252</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GeminiMultiModal</span><span class="p">(</span><span class="n">MultiModalLLM</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Gemini multimodal."""</span>

    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">GEMINI_MM_MODELS</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">description</span><span class="o">=</span><span class="s2">"The Gemini model to use."</span>
    <span class="p">)</span>
    <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_TEMPERATURE</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The temperature to use during generation."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
        <span class="n">lte</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">max_tokens</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_NUM_OUTPUTS</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The number of tokens to generate."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">generate_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Kwargs for generation."</span>
    <span class="p">)</span>

    <span class="n">_model</span><span class="p">:</span> <span class="s2">"genai.GenerativeModel"</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_model_meta</span><span class="p">:</span> <span class="s2">"genai.types.Model"</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">GEMINI_MM_MODELS</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">DEFAULT_TEMPERATURE</span><span class="p">,</span>
        <span class="n">max_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">generation_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s2">"genai.types.GenerationConfigDict"</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">safety_settings</span><span class="p">:</span> <span class="s2">"genai.types.SafetySettingOptions"</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_base</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transport</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">generate_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Creates a new Gemini model interface."""</span>
        <span class="c1"># API keys are optional. The API can be authorised via OAuth (detected</span>
        <span class="c1"># environmentally) or by the GOOGLE_API_KEY environment variable.</span>
        <span class="n">config_params</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"api_key"</span><span class="p">:</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"GOOGLE_API_KEY"</span><span class="p">),</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">api_base</span><span class="p">:</span>
            <span class="n">config_params</span><span class="p">[</span><span class="s2">"client_options"</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"api_endpoint"</span><span class="p">:</span> <span class="n">api_base</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">transport</span><span class="p">:</span>
            <span class="n">config_params</span><span class="p">[</span><span class="s2">"transport"</span><span class="p">]</span> <span class="o">=</span> <span class="n">transport</span>
        <span class="c1"># transport: A string, one of: [`rest`, `grpc`, `grpc_asyncio`].</span>
        <span class="n">genai</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span><span class="o">**</span><span class="n">config_params</span><span class="p">)</span>

        <span class="n">base_gen_config</span> <span class="o">=</span> <span class="n">generation_config</span> <span class="k">if</span> <span class="n">generation_config</span> <span class="k">else</span> <span class="p">{}</span>
        <span class="c1"># Explicitly passed args take precedence over the generation_config.</span>
        <span class="n">final_gen_config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"temperature"</span><span class="p">:</span> <span class="n">temperature</span><span class="p">}</span> <span class="o">|</span> <span class="n">base_gen_config</span>

        <span class="c1"># Check whether the Gemini Model is supported or not</span>
        <span class="k">if</span> <span class="n">model_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">GEMINI_MM_MODELS</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Invalid model </span><span class="si">{</span><span class="n">model_name</span><span class="si">}</span><span class="s2">. "</span>
                <span class="sa">f</span><span class="s2">"Available models are: </span><span class="si">{</span><span class="n">GEMINI_MM_MODELS</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_model</span> <span class="o">=</span> <span class="n">genai</span><span class="o">.</span><span class="n">GenerativeModel</span><span class="p">(</span>
            <span class="n">model_name</span><span class="o">=</span><span class="n">model_name</span><span class="p">,</span>
            <span class="n">generation_config</span><span class="o">=</span><span class="n">final_gen_config</span><span class="p">,</span>
            <span class="n">safety_settings</span><span class="o">=</span><span class="n">safety_settings</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_model_meta</span> <span class="o">=</span> <span class="n">genai</span><span class="o">.</span><span class="n">get_model</span><span class="p">(</span><span class="n">model_name</span><span class="p">)</span>

        <span class="n">supported_methods</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_meta</span><span class="o">.</span><span class="n">supported_generation_methods</span>
        <span class="k">if</span> <span class="s2">"generateContent"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">supported_methods</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Model </span><span class="si">{</span><span class="n">model_name</span><span class="si">}</span><span class="s2"> does not support content generation, only "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">supported_methods</span><span class="si">}</span><span class="s2">."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">max_tokens</span><span class="p">:</span>
            <span class="n">max_tokens</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_meta</span><span class="o">.</span><span class="n">output_token_limit</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">max_tokens</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">max_tokens</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_meta</span><span class="o">.</span><span class="n">output_token_limit</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">model_name</span><span class="o">=</span><span class="n">model_name</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">max_tokens</span><span class="o">=</span><span class="n">max_tokens</span><span class="p">,</span>
            <span class="n">generate_kwargs</span><span class="o">=</span><span class="n">generate_kwargs</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"Gemini_MultiModal_LLM"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
        <span class="n">total_tokens</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_meta</span><span class="o">.</span><span class="n">input_token_limit</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_tokens</span>
        <span class="k">return</span> <span class="n">MultiModalLLMMetadata</span><span class="p">(</span>
            <span class="n">context_window</span><span class="o">=</span><span class="n">total_tokens</span><span class="p">,</span>
            <span class="n">num_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">max_tokens</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">images</span> <span class="o">=</span> <span class="p">[</span><span class="n">PIL</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">resolve_image</span><span class="p">())</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">image_documents</span><span class="p">]</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">generate_content</span><span class="p">([</span><span class="n">prompt</span><span class="p">,</span> <span class="o">*</span><span class="n">images</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">completion_from_gemini_response</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
        <span class="n">images</span> <span class="o">=</span> <span class="p">[</span><span class="n">PIL</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">resolve_image</span><span class="p">())</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">image_documents</span><span class="p">]</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">generate_content</span><span class="p">([</span><span class="n">prompt</span><span class="p">,</span> <span class="o">*</span><span class="n">images</span><span class="p">],</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">yield from</span> <span class="nb">map</span><span class="p">(</span><span class="n">completion_from_gemini_response</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="o">*</span><span class="n">history</span><span class="p">,</span> <span class="n">next_msg</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">chat_message_to_gemini</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
        <span class="n">chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">start_chat</span><span class="p">(</span><span class="n">history</span><span class="o">=</span><span class="n">history</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="o">.</span><span class="n">send_message</span><span class="p">(</span><span class="n">next_msg</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">chat_from_gemini_response</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
        <span class="o">*</span><span class="n">history</span><span class="p">,</span> <span class="n">next_msg</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">chat_message_to_gemini</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
        <span class="n">chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">start_chat</span><span class="p">(</span><span class="n">history</span><span class="o">=</span><span class="n">history</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="o">.</span><span class="n">send_message</span><span class="p">(</span><span class="n">next_msg</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
                <span class="n">top_candidate</span> <span class="o">=</span> <span class="n">r</span><span class="o">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">top_candidate</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span>
                <span class="n">role</span> <span class="o">=</span> <span class="n">ROLES_FROM_GEMINI</span><span class="p">[</span><span class="n">top_candidate</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">role</span><span class="p">]</span>
                <span class="n">raw</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="o">**</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">top_candidate</span><span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="n">top_candidate</span><span class="p">)),</span>
                    <span class="o">**</span><span class="p">(</span>
                        <span class="nb">type</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">prompt_feedback</span><span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">prompt_feedback</span><span class="p">)</span>
                    <span class="p">),</span>
                <span class="p">}</span>
                <span class="n">content</span> <span class="o">+=</span> <span class="n">content_delta</span>
                <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
                    <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">),</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">raw</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="n">images</span> <span class="o">=</span> <span class="p">[</span><span class="n">PIL</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">resolve_image</span><span class="p">())</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">image_documents</span><span class="p">]</span>
        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">generate_content_async</span><span class="p">([</span><span class="n">prompt</span><span class="p">,</span> <span class="o">*</span><span class="n">images</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">completion_from_gemini_response</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
        <span class="n">images</span> <span class="o">=</span> <span class="p">[</span><span class="n">PIL</span><span class="o">.</span><span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">doc</span><span class="o">.</span><span class="n">resolve_image</span><span class="p">())</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">image_documents</span><span class="p">]</span>
        <span class="n">ait</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">generate_content_async</span><span class="p">(</span>
            <span class="p">[</span><span class="n">prompt</span><span class="p">,</span> <span class="o">*</span><span class="n">images</span><span class="p">],</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">comp</span> <span class="ow">in</span> <span class="n">ait</span><span class="p">:</span>
                <span class="k">yield</span> <span class="n">completion_from_gemini_response</span><span class="p">(</span><span class="n">comp</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="o">*</span><span class="n">history</span><span class="p">,</span> <span class="n">next_msg</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">chat_message_to_gemini</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
        <span class="n">chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">start_chat</span><span class="p">(</span><span class="n">history</span><span class="o">=</span><span class="n">history</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">chat</span><span class="o">.</span><span class="n">send_message_async</span><span class="p">(</span><span class="n">next_msg</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">chat_from_gemini_response</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
        <span class="o">*</span><span class="n">history</span><span class="p">,</span> <span class="n">next_msg</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">chat_message_to_gemini</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
        <span class="n">chat</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model</span><span class="o">.</span><span class="n">start_chat</span><span class="p">(</span><span class="n">history</span><span class="o">=</span><span class="n">history</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">chat</span><span class="o">.</span><span class="n">send_message_async</span><span class="p">(</span><span class="n">next_msg</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">async</span> <span class="k">def</span> <span class="nf">gen</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
                <span class="n">top_candidate</span> <span class="o">=</span> <span class="n">r</span><span class="o">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">content_delta</span> <span class="o">=</span> <span class="n">top_candidate</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span>
                <span class="n">role</span> <span class="o">=</span> <span class="n">ROLES_FROM_GEMINI</span><span class="p">[</span><span class="n">top_candidate</span><span class="o">.</span><span class="n">content</span><span class="o">.</span><span class="n">role</span><span class="p">]</span>
                <span class="n">raw</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="o">**</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">top_candidate</span><span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="n">top_candidate</span><span class="p">)),</span>
                    <span class="o">**</span><span class="p">(</span>
                        <span class="nb">type</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">prompt_feedback</span><span class="p">)</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">prompt_feedback</span><span class="p">)</span>
                    <span class="p">),</span>
                <span class="p">}</span>
                <span class="n">content</span> <span class="o">+=</span> <span class="n">content_delta</span>
                <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
                    <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="n">role</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">),</span>
                    <span class="n">delta</span><span class="o">=</span><span class="n">content_delta</span><span class="p">,</span>
                    <span class="n">raw</span><span class="o">=</span><span class="n">raw</span><span class="p">,</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">gen</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/dashscope/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/)
