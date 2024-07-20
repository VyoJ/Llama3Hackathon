Title: Google - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/

Markdown Content:
Google - LlamaIndex


GoogleTextSynthesizer [#](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/#llama_index.response_synthesizers.google.GoogleTextSynthesizer "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseSynthesizer](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/#llama_index.core.response_synthesizers.base.BaseSynthesizer "llama_index.core.response_synthesizers.base.BaseSynthesizer")`

Google's Attributed Question and Answering service.

Given a user's query and a list of passages, Google's server will return a response that is grounded to the provided list of passages. It will not base the response on parametric memory.

Source code in `llama-index-integrations/response_synthesizers/llama-index-response-synthesizers-google/llama_index/response_synthesizers/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 44</span>
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
<span class="normal">255</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleTextSynthesizer</span><span class="p">(</span><span class="n">BaseSynthesizer</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google's Attributed Question and Answering service.</span>

<span class="sd">    Given a user's query and a list of passages, Google's server will return</span>
<span class="sd">    a response that is grounded to the provided list of passages. It will not</span>
<span class="sd">    base the response on parametric memory.</span>
<span class="sd">    """</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">_temperature</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">_answer_style</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">_safety_setting</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span>
        <span class="n">answer_style</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">safety_setting</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create a new Google AQA.</span>

<span class="sd">        Prefer to use the factory `from_defaults` instead for type safety.</span>
<span class="sd">        See `from_defaults` for more documentation.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">MockLLM</span><span class="p">(),</span>
            <span class="n">output_cls</span><span class="o">=</span><span class="n">SynthesizedResponse</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">build_generative_service</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_temperature</span> <span class="o">=</span> <span class="n">temperature</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_answer_style</span> <span class="o">=</span> <span class="n">answer_style</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_safety_setting</span> <span class="o">=</span> <span class="n">safety_setting</span>

    <span class="c1"># Type safe factory that is only available if Google is installed.</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.7</span><span class="p">,</span>
        <span class="n">answer_style</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">safety_setting</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"genai.SafetySetting"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GoogleTextSynthesizer"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Google AQA.</span>

<span class="sd">        Example:</span>
<span class="sd">          responder = GoogleTextSynthesizer.create(</span>
<span class="sd">              temperature=0.7,</span>
<span class="sd">              answer_style=AnswerStyle.ABSTRACTIVE,</span>
<span class="sd">              safety_setting=[</span>
<span class="sd">                  SafetySetting(</span>
<span class="sd">                      category=HARM_CATEGORY_SEXUALLY_EXPLICIT,</span>
<span class="sd">                      threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,</span>
<span class="sd">                  ),</span>
<span class="sd">              ]</span>
<span class="sd">          )</span>

<span class="sd">        Args:</span>
<span class="sd">          temperature: 0.0 to 1.0.</span>
<span class="sd">          answer_style: See `google.ai.generativelanguage.GenerateAnswerRequest.AnswerStyle`</span>
<span class="sd">            The default is ABSTRACTIVE (1).</span>
<span class="sd">          safety_setting: See `google.ai.generativelanguage.SafetySetting`.</span>

<span class="sd">        Returns:</span>
<span class="sd">          an instance of GoogleTextSynthesizer.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">answer_style</span><span class="o">=</span><span class="n">answer_style</span><span class="p">,</span>
            <span class="n">safety_setting</span><span class="o">=</span><span class="n">safety_setting</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SynthesizedResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a grounded response on provided passages.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_str: The user's question.</span>
<span class="sd">            text_chunks: A list of passages that should be used to answer the</span>
<span class="sd">                question.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A `SynthesizedResponse` object.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

            <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">GenerativeServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">generate_answer</span><span class="p">(</span>
            <span class="n">prompt</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">passages</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">text_chunks</span><span class="p">),</span>
            <span class="n">answer_style</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_answer_style</span><span class="p">,</span>
            <span class="n">safety_settings</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_safety_setting</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_temperature</span><span class="p">,</span>
            <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">SynthesizedResponse</span><span class="p">(</span>
            <span class="n">answer</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">answer</span><span class="p">,</span>
            <span class="n">attributed_passages</span><span class="o">=</span><span class="p">[</span>
                <span class="n">passage</span><span class="o">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">passage</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">attributed_passages</span>
            <span class="p">],</span>
            <span class="n">answerable_probability</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">answerable_probability</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_chunks</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TEXT_TYPE</span><span class="p">:</span>
        <span class="c1"># TODO: Implement a true async version.</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_response</span><span class="p">(</span><span class="n">query_str</span><span class="p">,</span> <span class="n">text_chunks</span><span class="p">,</span> <span class="o">**</span><span class="n">response_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">synthesize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query</span><span class="p">:</span> <span class="n">QueryTextType</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">additional_source_nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">response_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a grounded response based on provided passages.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Response's `source_nodes` will begin with a list of attributed</span>
<span class="sd">            passages. These passages are the ones that were used to construct</span>
<span class="sd">            the grounded response. These passages will always have no score,</span>
<span class="sd">            the only way to mark them as attributed passages. Then, the list</span>
<span class="sd">            will follow with the originally provided passages, which will have</span>
<span class="sd">            a score from the retrieval.</span>

<span class="sd">            Response's `metadata` may also have have an entry with key</span>
<span class="sd">            `answerable_probability`, which is the model's estimate of the</span>
<span class="sd">            probability that its answer is correct and grounded in the input</span>
<span class="sd">            passages.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="s2">"Empty Response"</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callback_manager</span><span class="o">.</span><span class="n">event</span><span class="p">(</span>
        <span class="n">CBEventType</span><span class="o">.</span><span class="n">SYNTHESIZE</span><span class="p">,</span> <span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">QUERY_STR</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">}</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">event</span><span class="p">:</span>
        <span class="n">internal_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_response</span><span class="p">(</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">text_chunks</span><span class="o">=</span><span class="p">[</span>
                <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">LLM</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span>
            <span class="p">],</span>
            <span class="o">**</span><span class="n">response_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">additional_source_nodes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">additional_source_nodes</span> <span class="ow">or</span> <span class="p">[])</span>

        <span class="n">external_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prepare_external_response</span><span class="p">(</span>
            <span class="n">internal_response</span><span class="p">,</span> <span class="n">nodes</span> <span class="o">+</span> <span class="n">additional_source_nodes</span>
        <span class="p">)</span>

        <span class="n">event</span><span class="o">.</span><span class="n">on_end</span><span class="p">(</span><span class="n">payload</span><span class="o">=</span><span class="p">{</span><span class="n">EventPayload</span><span class="o">.</span><span class="n">RESPONSE</span><span class="p">:</span> <span class="n">external_response</span><span class="p">})</span>

    <span class="k">return</span> <span class="n">external_response</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Generation](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/)
