Title: Google - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/indices/google/

Markdown Content:
Google - LlamaIndex


GoogleIndex [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseManagedIndex`

Google's Generative AI Semantic vector store with AQA.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 42</span>
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
<span class="normal">260</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleIndex</span><span class="p">(</span><span class="n">BaseManagedIndex</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google's Generative AI Semantic vector store with AQA."""</span>

    <span class="n">_store</span><span class="p">:</span> <span class="n">GoogleVectorStore</span>
    <span class="n">_index</span><span class="p">:</span> <span class="n">VectorStoreIndex</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">GoogleVectorStore</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates an instance of GoogleIndex.</span>

<span class="sd">        Prefer to use the factories `from_corpus` or `create_corpus` instead.</span>
<span class="sd">        """</span>
        <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">MockEmbedding</span><span class="p">(</span><span class="n">embed_dim</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_store</span> <span class="o">=</span> <span class="n">vector_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_vector_store</span><span class="p">(</span>
            <span class="n">vector_store</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">index_struct</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_corpus</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span> <span class="o">*</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates a GoogleIndex from an existing corpus.</span>

<span class="sd">        Args:</span>
<span class="sd">            corpus_id: ID of an existing corpus on Google's server.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An instance of GoogleIndex pointing to the specified corpus.</span>
<span class="sd">        """</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_corpus(corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">from_corpus</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">),</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">create_corpus</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">display_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Creates a GoogleIndex from a new corpus.</span>

<span class="sd">        Args:</span>
<span class="sd">            corpus_id: ID of the new corpus to be created. If not provided,</span>
<span class="sd">                Google server will provide one.</span>
<span class="sd">            display_name: Title of the new corpus. If not provided, Google</span>
<span class="sd">                server will provide one.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An instance of GoogleIndex pointing to the specified corpus.</span>
<span class="sd">        """</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_new_corpus(new_corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">, new_display_name=</span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2">)"</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span>
                <span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span>
            <span class="p">),</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build an index from a sequence of documents."""</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_documents(...)"</span><span class="p">)</span>

        <span class="n">new_display_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Corpus created on </span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span>
        <span class="n">instance</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="n">new_display_name</span><span class="p">),</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">GoogleIndex</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span>
        <span class="n">index</span><span class="o">.</span><span class="n">insert_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">instance</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">corpus_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns the corpus ID being used by this GoogleIndex."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_store</span><span class="o">.</span><span class="n">corpus_id</span>

    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Inserts a set of nodes."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">insert_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="o">**</span><span class="n">insert_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">insert_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Inserts a set of documents."""</span>
        <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Deletes a document and its nodes by using ref_doc_id."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Updates a document and its corresponding nodes."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">document</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a Retriever for this managed index."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.7</span><span class="p">,</span>
        <span class="n">answer_style</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">safety_setting</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns the AQA engine for this index.</span>

<span class="sd">        Example:</span>
<span class="sd">          query_engine = index.as_query_engine(</span>
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
<span class="sd">            temperature: 0.0 to 1.0.</span>
<span class="sd">            answer_style: See `google.ai.generativelanguage.GenerateAnswerRequest.AnswerStyle`</span>
<span class="sd">            safety_setting: See `google.ai.generativelanguage.SafetySetting`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A query engine that uses Google's AQA model. The query engine will</span>
<span class="sd">            return a `Response` object.</span>

<span class="sd">            `Response`'s `source_nodes` will begin with a list of attributed</span>
<span class="sd">            passages. These passages are the ones that were used to construct</span>
<span class="sd">            the grounded response. These passages will always have no score,</span>
<span class="sd">            the only way to mark them as attributed passages. Then, the list</span>
<span class="sd">            will follow with the originally provided passages, which will have</span>
<span class="sd">            a score from the retrieval.</span>

<span class="sd">            `Response`'s `metadata` may also have have an entry with key</span>
<span class="sd">            `answerable_probability`, which is the probability that the grounded</span>
<span class="sd">            answer is likely correct.</span>
<span class="sd">        """</span>
        <span class="c1"># NOTE: lazy import</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
            <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># Don't overwrite the caller's kwargs, which may surprise them.</span>
        <span class="n">local_kwargs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

        <span class="k">if</span> <span class="s2">"retriever"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"Ignoring user's retriever to GoogleIndex.as_query_engine, "</span>
                <span class="s2">"which uses its own retriever."</span>
            <span class="p">)</span>
            <span class="k">del</span> <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span>

        <span class="k">if</span> <span class="s2">"response_synthesizer"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"Ignoring user's response synthesizer to "</span>
                <span class="s2">"GoogleIndex.as_query_engine, which uses its own retriever."</span>
            <span class="p">)</span>
            <span class="k">del</span> <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"response_synthesizer"</span><span class="p">]</span>

        <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">local_kwargs</span><span class="p">)</span>
        <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"response_synthesizer"</span><span class="p">]</span> <span class="o">=</span> <span class="n">GoogleTextSynthesizer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
            <span class="n">answer_style</span><span class="o">=</span><span class="n">answer_style</span><span class="p">,</span>
            <span class="n">safety_setting</span><span class="o">=</span><span class="n">safety_setting</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="s2">"service_context"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">local_kwargs</span><span class="p">:</span>
            <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"service_context"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>

        <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="o">**</span><span class="n">local_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_index_from_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">IndexDict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build the index from nodes."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">_build_index_from_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### corpus\_id `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.corpus_id "Permanent link")

```
corpus_id: str
```

Returns the corpus ID being used by this GoogleIndex.

### from\_corpus `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.from_corpus "Permanent link")

```
from_corpus(*, corpus_id: str, **kwargs: Any) -> IndexType
```

Creates a GoogleIndex from an existing corpus.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `corpus_id` | `str` | 
ID of an existing corpus on Google's server.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `IndexType` | 
An instance of GoogleIndex pointing to the specified corpus.



 |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_corpus</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span> <span class="o">*</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Creates a GoogleIndex from an existing corpus.</span>

<span class="sd">    Args:</span>
<span class="sd">        corpus_id: ID of an existing corpus on Google's server.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An instance of GoogleIndex pointing to the specified corpus.</span>
<span class="sd">    """</span>
    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_corpus(corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">from_corpus</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">),</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create\_corpus `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.create_corpus "Permanent link")

```
create_corpus(*, corpus_id: Optional[str] = None, display_name: Optional[str] = None, **kwargs: Any) -> IndexType
```

Creates a GoogleIndex from a new corpus.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `corpus_id` | `Optional[str]` | 
ID of the new corpus to be created. If not provided, Google server will provide one.



 | `None` |
| `display_name` | `Optional[str]` | 

Title of the new corpus. If not provided, Google server will provide one.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `IndexType` | 
An instance of GoogleIndex pointing to the specified corpus.



 |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 90</span>
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
<span class="normal">117</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">create_corpus</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">display_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Creates a GoogleIndex from a new corpus.</span>

<span class="sd">    Args:</span>
<span class="sd">        corpus_id: ID of the new corpus to be created. If not provided,</span>
<span class="sd">            Google server will provide one.</span>
<span class="sd">        display_name: Title of the new corpus. If not provided, Google</span>
<span class="sd">            server will provide one.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An instance of GoogleIndex pointing to the specified corpus.</span>
<span class="sd">    """</span>
    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_new_corpus(new_corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">, new_display_name=</span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2">)"</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span>
        <span class="p">),</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_documents `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.from_documents "Permanent link")

```
from_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], storage_context: Optional[[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")] = None, show_progress: bool = False, callback_manager: Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")] = None, transformations: Optional[List[[TransformComponent](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.TransformComponent "llama_index.core.schema.TransformComponent")]] = None, service_context: Optional[ServiceContext] = None, embed_model: Optional[[BaseEmbedding](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/#llama_index.core.embeddings.BaseEmbedding "llama_index.core.base.embeddings.base.BaseEmbedding")] = None, **kwargs: Any) -> IndexType
```

Build an index from a sequence of documents.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">119</span>
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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_documents</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">IndexType</span><span class="p">],</span>
    <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
    <span class="n">storage_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">StorageContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">show_progress</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">transformations</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TransformComponent</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="c1"># deprecated</span>
    <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">IndexType</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build an index from a sequence of documents."""</span>
    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleIndex.from_documents(...)"</span><span class="p">)</span>

    <span class="n">new_display_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"Corpus created on </span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span>
    <span class="n">instance</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">vector_store</span><span class="o">=</span><span class="n">GoogleVectorStore</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="n">new_display_name</span><span class="p">),</span>
        <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
        <span class="n">show_progress</span><span class="o">=</span><span class="n">show_progress</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
        <span class="n">transformations</span><span class="o">=</span><span class="n">transformations</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">index</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">GoogleIndex</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span>
    <span class="n">index</span><span class="o">.</span><span class="n">insert_documents</span><span class="p">(</span>
        <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
        <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="n">instance</span>
</code></pre></div></td></tr></tbody></table>

### insert\_documents [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.insert_documents "Permanent link")

```
insert_documents(documents: Sequence[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")], **kwargs: Any) -> None
```

Inserts a set of documents.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">insert_documents</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">documents</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Inserts a set of documents."""</span>
    <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">document</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.delete_ref_doc "Permanent link")

```
delete_ref_doc(ref_doc_id: str, delete_from_docstore: bool = False, **delete_kwargs: Any) -> None
```

Deletes a document and its nodes by using ref\_doc\_id.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_ref_doc</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">delete_from_docstore</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Deletes a document and its nodes by using ref_doc_id."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">delete_ref_doc</span><span class="p">(</span><span class="n">ref_doc_id</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### update\_ref\_doc [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.update_ref_doc "Permanent link")

```
update_ref_doc(document: [Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document"), **update_kwargs: Any) -> None
```

Updates a document and its corresponding nodes.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">update_ref_doc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">document</span><span class="p">:</span> <span class="n">Document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Updates a document and its corresponding nodes."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">document</span><span class="o">=</span><span class="n">document</span><span class="p">,</span> <span class="o">**</span><span class="n">update_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_retriever [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.as_retriever "Permanent link")

```
as_retriever(**kwargs: Any) -> [BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.indices.base_retriever.BaseRetriever")
```

Returns a Retriever for this managed index.

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_retriever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseRetriever</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a Retriever for this managed index."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### as\_query\_engine [#](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/#llama_index.indices.managed.google.GoogleIndex.as_query_engine "Permanent link")

```
as_query_engine(llm: Optional[LLMType] = None, temperature: float = 0.7, answer_style: Any = 1, safety_setting: List[Any] = [], **kwargs: Any) -> [BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")
```

Returns the AQA engine for this index.

Examplequery\_engine = index.as\_query\_engine( temperature=0.7, answer\_style=AnswerStyle.ABSTRACTIVE, safety\_setting=\[ SafetySetting( category=HARM\_CATEGORY\_SEXUALLY\_EXPLICIT, threshold=HarmBlockThreshold.BLOCK\_LOW\_AND\_ABOVE, ), \] )

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `temperature` | `float` | 
0.0 to 1.0.



 | `0.7` |
| `answer_style` | `Any` | 

See `google.ai.generativelanguage.GenerateAnswerRequest.AnswerStyle`



 | `1` |
| `safety_setting` | `List[Any]` | 

See `google.ai.generativelanguage.SafetySetting`.



 | `[]` |

**Returns:**

| Type | Description |
| --- | --- |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 
A query engine that uses Google's AQA model. The query engine will



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

return a `Response` object.



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

`Response`'s `source_nodes` will begin with a list of attributed



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

passages. These passages are the ones that were used to construct



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

the grounded response. These passages will always have no score,



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

the only way to mark them as attributed passages. Then, the list



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

will follow with the originally provided passages, which will have



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

a score from the retrieval.



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

`Response`'s `metadata` may also have have an entry with key



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

`answerable_probability`, which is the probability that the grounded



 |
| `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.indices.query.base.BaseQueryEngine")` | 

answer is likely correct.



 |

Source code in `llama-index-integrations/indices/llama-index-indices-managed-google/llama_index/indices/managed/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">183</span>
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
<span class="normal">256</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">as_query_engine</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLMType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">temperature</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.7</span><span class="p">,</span>
    <span class="n">answer_style</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
    <span class="n">safety_setting</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseQueryEngine</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns the AQA engine for this index.</span>

<span class="sd">    Example:</span>
<span class="sd">      query_engine = index.as_query_engine(</span>
<span class="sd">          temperature=0.7,</span>
<span class="sd">          answer_style=AnswerStyle.ABSTRACTIVE,</span>
<span class="sd">          safety_setting=[</span>
<span class="sd">              SafetySetting(</span>
<span class="sd">                  category=HARM_CATEGORY_SEXUALLY_EXPLICIT,</span>
<span class="sd">                  threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,</span>
<span class="sd">              ),</span>
<span class="sd">          ]</span>
<span class="sd">      )</span>

<span class="sd">    Args:</span>
<span class="sd">        temperature: 0.0 to 1.0.</span>
<span class="sd">        answer_style: See `google.ai.generativelanguage.GenerateAnswerRequest.AnswerStyle`</span>
<span class="sd">        safety_setting: See `google.ai.generativelanguage.SafetySetting`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A query engine that uses Google's AQA model. The query engine will</span>
<span class="sd">        return a `Response` object.</span>

<span class="sd">        `Response`'s `source_nodes` will begin with a list of attributed</span>
<span class="sd">        passages. These passages are the ones that were used to construct</span>
<span class="sd">        the grounded response. These passages will always have no score,</span>
<span class="sd">        the only way to mark them as attributed passages. Then, the list</span>
<span class="sd">        will follow with the originally provided passages, which will have</span>
<span class="sd">        a score from the retrieval.</span>

<span class="sd">        `Response`'s `metadata` may also have have an entry with key</span>
<span class="sd">        `answerable_probability`, which is the probability that the grounded</span>
<span class="sd">        answer is likely correct.</span>
<span class="sd">    """</span>
    <span class="c1"># NOTE: lazy import</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.query_engine.retriever_query_engine</span> <span class="kn">import</span> <span class="p">(</span>
        <span class="n">RetrieverQueryEngine</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="c1"># Don't overwrite the caller's kwargs, which may surprise them.</span>
    <span class="n">local_kwargs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">if</span> <span class="s2">"retriever"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"Ignoring user's retriever to GoogleIndex.as_query_engine, "</span>
            <span class="s2">"which uses its own retriever."</span>
        <span class="p">)</span>
        <span class="k">del</span> <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span>

    <span class="k">if</span> <span class="s2">"response_synthesizer"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
        <span class="n">_logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"Ignoring user's response synthesizer to "</span>
            <span class="s2">"GoogleIndex.as_query_engine, which uses its own retriever."</span>
        <span class="p">)</span>
        <span class="k">del</span> <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"response_synthesizer"</span><span class="p">]</span>

    <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"retriever"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="o">**</span><span class="n">local_kwargs</span><span class="p">)</span>
    <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"response_synthesizer"</span><span class="p">]</span> <span class="o">=</span> <span class="n">GoogleTextSynthesizer</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
        <span class="n">temperature</span><span class="o">=</span><span class="n">temperature</span><span class="p">,</span>
        <span class="n">answer_style</span><span class="o">=</span><span class="n">answer_style</span><span class="p">,</span>
        <span class="n">safety_setting</span><span class="o">=</span><span class="n">safety_setting</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="s2">"service_context"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">local_kwargs</span><span class="p">:</span>
        <span class="n">local_kwargs</span><span class="p">[</span><span class="s2">"service_context"</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service_context</span>

    <span class="k">return</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="o">**</span><span class="n">local_kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Document summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/)[Next Index](https://docs.llamaindex.ai/en/stable/api_reference/indices/)
