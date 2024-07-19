Title: Ollama - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/

Markdown Content:
Ollama - LlamaIndex


OllamaMultiModal [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[MultiModalLLM](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/#llama_index.core.multi_modal_llms.base.MultiModalLLM "llama_index.core.multi_modal_llms.MultiModalLLM")`

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-ollama/llama_index/multi_modal_llms/ollama/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 52</span>
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
<span class="normal">221</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">OllamaMultiModal</span><span class="p">(</span><span class="n">MultiModalLLM</span><span class="p">):</span>
    <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="s2">"http://localhost:11434"</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Base url the model is hosted under."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">model</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">"The MultiModal Ollama model to use."</span><span class="p">)</span>
    <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="mf">0.75</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The temperature to use for sampling."</span><span class="p">,</span>
        <span class="n">gte</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
        <span class="n">lte</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">context_window</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_CONTEXT_WINDOW</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The maximum number of context tokens for the model."</span><span class="p">,</span>
        <span class="n">gt</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">request_timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"The timeout for making http request to Ollama API server"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">additional_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Additional model parameters for the Ollama API."</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">_client</span><span class="p">:</span> <span class="n">Client</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params and ollama client."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">request_timeout</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"Ollama_multi_modal_llm"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MultiModalLLMMetadata</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""LLM metadata."""</span>
        <span class="k">return</span> <span class="n">MultiModalLLMMetadata</span><span class="p">(</span>
            <span class="n">context_window</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">context_window</span><span class="p">,</span>
            <span class="n">num_output</span><span class="o">=</span><span class="n">DEFAULT_NUM_OUTPUTS</span><span class="p">,</span>
            <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
            <span class="n">is_chat_model</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>  <span class="c1"># Ollama supports chat API for all models</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">_model_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">base_kwargs</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"temperature"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">temperature</span><span class="p">,</span>
            <span class="s2">"num_ctx"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_window</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="o">**</span><span class="n">base_kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">additional_kwargs</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">chat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Chat."""</span>
        <span class="n">ollama_messages</span> <span class="o">=</span> <span class="n">_messages_to_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="n">messages</span><span class="o">=</span><span class="n">ollama_messages</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">],</span>
                <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"role"</span><span class="p">]),</span>
                <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
            <span class="p">),</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">],</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Stream chat."""</span>
        <span class="n">ollama_messages</span> <span class="o">=</span> <span class="n">_messages_to_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="n">messages</span><span class="o">=</span><span class="n">ollama_messages</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"done"</span> <span class="ow">in</span> <span class="n">chunk</span> <span class="ow">and</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"done"</span><span class="p">]:</span>
                <span class="k">break</span>
            <span class="n">message</span> <span class="o">=</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"message"</span><span class="p">]</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
            <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
                <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                    <span class="n">content</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"role"</span><span class="p">]),</span>
                    <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span>
                        <span class="n">message</span><span class="p">,</span> <span class="p">(</span><span class="s2">"content"</span><span class="p">,</span> <span class="s2">"role"</span><span class="p">)</span>
                    <span class="p">),</span>
                <span class="p">),</span>
                <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
                <span class="n">raw</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
                <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
        <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Complete."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
            <span class="n">images</span><span class="o">=</span><span class="n">image_documents_to_base64</span><span class="p">(</span><span class="n">image_documents</span><span class="p">),</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">options</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">CompletionResponse</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"response"</span><span class="p">],</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"response"</span><span class="p">,)),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
        <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Stream complete."""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
            <span class="n">images</span><span class="o">=</span><span class="n">image_documents_to_base64</span><span class="p">(</span><span class="n">image_documents</span><span class="p">),</span>
            <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">options</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"done"</span> <span class="ow">in</span> <span class="n">chunk</span> <span class="ow">and</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"done"</span><span class="p">]:</span>
                <span class="k">break</span>
            <span class="n">delta</span> <span class="o">=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"response"</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
            <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk</span><span class="p">[</span><span class="s2">"response"</span><span class="p">]),</span>
                <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
                <span class="n">raw</span><span class="o">=</span><span class="n">chunk</span><span class="p">,</span>
                <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="p">(</span><span class="s2">"response"</span><span class="p">,)),</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">acomplete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Ollama does not support async completion."</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">achat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Ollama does not support async chat."</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseAsyncGen</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Ollama does not support async streaming completion."</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">astream_chat</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseAsyncGen</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Ollama does not support async streaming chat."</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### metadata `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal.metadata "Permanent link")

```
metadata: MultiModalLLMMetadata
```

LLM metadata.

### chat [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal.chat "Permanent link")

```
chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponse
```

Chat.

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-ollama/llama_index/multi_modal_llms/ollama/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">108</span>
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
<span class="normal">122</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">chat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Chat."""</span>
    <span class="n">ollama_messages</span> <span class="o">=</span> <span class="n">_messages_to_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
        <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="n">messages</span><span class="o">=</span><span class="n">ollama_messages</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">ChatResponse</span><span class="p">(</span>
        <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
            <span class="n">content</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"content"</span><span class="p">],</span>
            <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">][</span><span class="s2">"role"</span><span class="p">]),</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
        <span class="p">),</span>
        <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"message"</span><span class="p">],</span>
        <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### stream\_chat [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal.stream_chat "Permanent link")

```
stream_chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponseGen
```

Stream chat.

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-ollama/llama_index/multi_modal_llms/ollama/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">124</span>
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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">stream_chat</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">messages</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ChatMessage</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ChatResponseGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Stream chat."""</span>
    <span class="n">ollama_messages</span> <span class="o">=</span> <span class="n">_messages_to_dicts</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">chat</span><span class="p">(</span>
        <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="n">messages</span><span class="o">=</span><span class="n">ollama_messages</span><span class="p">,</span> <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
    <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"done"</span> <span class="ow">in</span> <span class="n">chunk</span> <span class="ow">and</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"done"</span><span class="p">]:</span>
            <span class="k">break</span>
        <span class="n">message</span> <span class="o">=</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"message"</span><span class="p">]</span>
        <span class="n">delta</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content"</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
        <span class="k">yield</span> <span class="n">ChatResponse</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="n">ChatMessage</span><span class="p">(</span>
                <span class="n">content</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">role</span><span class="o">=</span><span class="n">MessageRole</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">"role"</span><span class="p">]),</span>
                <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span>
                    <span class="n">message</span><span class="p">,</span> <span class="p">(</span><span class="s2">"content"</span><span class="p">,</span> <span class="s2">"role"</span><span class="p">)</span>
                <span class="p">),</span>
            <span class="p">),</span>
            <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">message</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="p">(</span><span class="s2">"message"</span><span class="p">,)),</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### complete [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal.complete "Permanent link")

```
complete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], formatted: bool = False, **kwargs: Any) -> CompletionResponse
```

Complete.

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-ollama/llama_index/multi_modal_llms/ollama/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
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
<span class="normal">172</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">complete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
    <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Complete."""</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
        <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
        <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
        <span class="n">images</span><span class="o">=</span><span class="n">image_documents_to_base64</span><span class="p">(</span><span class="n">image_documents</span><span class="p">),</span>
        <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">options</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">CompletionResponse</span><span class="p">(</span>
        <span class="n">text</span><span class="o">=</span><span class="n">response</span><span class="p">[</span><span class="s2">"response"</span><span class="p">],</span>
        <span class="n">raw</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="p">(</span><span class="s2">"response"</span><span class="p">,)),</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### stream\_complete [#](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/#llama_index.multi_modal_llms.ollama.OllamaMultiModal.stream_complete "Permanent link")

```
stream_complete(prompt: str, image_documents: Sequence[[ImageDocument](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.ImageDocument "llama_index.core.schema.ImageDocument")], formatted: bool = False, **kwargs: Any) -> CompletionResponseGen
```

Stream complete.

Source code in `llama-index-integrations/multi_modal_llms/llama-index-multi-modal-llms-ollama/llama_index/multi_modal_llms/ollama/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">174</span>
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
<span class="normal">201</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">stream_complete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">image_documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ImageDocument</span><span class="p">],</span>
    <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CompletionResponseGen</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Stream complete."""</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
        <span class="n">model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">,</span>
        <span class="n">prompt</span><span class="o">=</span><span class="n">prompt</span><span class="p">,</span>
        <span class="n">images</span><span class="o">=</span><span class="n">image_documents_to_base64</span><span class="p">(</span><span class="n">image_documents</span><span class="p">),</span>
        <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">options</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_kwargs</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"done"</span> <span class="ow">in</span> <span class="n">chunk</span> <span class="ow">and</span> <span class="n">chunk</span><span class="p">[</span><span class="s2">"done"</span><span class="p">]:</span>
            <span class="k">break</span>
        <span class="n">delta</span> <span class="o">=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"response"</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">+=</span> <span class="n">delta</span>
        <span class="k">yield</span> <span class="n">CompletionResponse</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">chunk</span><span class="p">[</span><span class="s2">"response"</span><span class="p">]),</span>
            <span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span>
            <span class="n">raw</span><span class="o">=</span><span class="n">chunk</span><span class="p">,</span>
            <span class="n">additional_kwargs</span><span class="o">=</span><span class="n">get_additional_kwargs</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="p">(</span><span class="s2">"response"</span><span class="p">,)),</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/)[Next Openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/)
