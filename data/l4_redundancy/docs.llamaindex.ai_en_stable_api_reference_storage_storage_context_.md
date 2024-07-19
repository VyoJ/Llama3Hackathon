Title: Storage context - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/

Markdown Content:
Storage context - LlamaIndex


StorageContext `dataclass` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Storage context.

The storage context container is a utility container for storing nodes, indices, and vectors. It contains the following: - docstore: BaseDocumentStore - index\_store: BaseIndexStore - vector\_store: BasePydanticVectorStore - graph\_store: GraphStore - property\_graph\_store: PropertyGraphStore (lazily initialized)

Source code in `llama-index-core/llama_index/core/storage/storage_context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 51</span>
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
<span class="normal">270</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">StorageContext</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Storage context.</span>

<span class="sd">    The storage context container is a utility container for storing nodes,</span>
<span class="sd">    indices, and vectors. It contains the following:</span>
<span class="sd">    - docstore: BaseDocumentStore</span>
<span class="sd">    - index_store: BaseIndexStore</span>
<span class="sd">    - vector_store: BasePydanticVectorStore</span>
<span class="sd">    - graph_store: GraphStore</span>
<span class="sd">    - property_graph_store: PropertyGraphStore (lazily initialized)</span>

<span class="sd">    """</span>

    <span class="n">docstore</span><span class="p">:</span> <span class="n">BaseDocumentStore</span>
    <span class="n">index_store</span><span class="p">:</span> <span class="n">BaseIndexStore</span>
    <span class="n">vector_stores</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePydanticVectorStore</span><span class="p">]</span>
    <span class="n">graph_store</span><span class="p">:</span> <span class="n">GraphStore</span>
    <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PropertyGraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">docstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseDocumentStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseIndexStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">image_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">vector_stores</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePydanticVectorStore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PropertyGraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StorageContext"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a StorageContext from defaults.</span>

<span class="sd">        Args:</span>
<span class="sd">            docstore (Optional[BaseDocumentStore]): document store</span>
<span class="sd">            index_store (Optional[BaseIndexStore]): index store</span>
<span class="sd">            vector_store (Optional[BasePydanticVectorStore]): vector store</span>
<span class="sd">            graph_store (Optional[GraphStore]): graph store</span>
<span class="sd">            image_store (Optional[BasePydanticVectorStore]): image store</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">persist_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">docstore</span> <span class="o">=</span> <span class="n">docstore</span> <span class="ow">or</span> <span class="n">SimpleDocumentStore</span><span class="p">()</span>
            <span class="n">index_store</span> <span class="o">=</span> <span class="n">index_store</span> <span class="ow">or</span> <span class="n">SimpleIndexStore</span><span class="p">()</span>
            <span class="n">graph_store</span> <span class="o">=</span> <span class="n">graph_store</span> <span class="ow">or</span> <span class="n">SimpleGraphStore</span><span class="p">()</span>
            <span class="n">image_store</span> <span class="o">=</span> <span class="n">image_store</span> <span class="ow">or</span> <span class="n">SimpleVectorStore</span><span class="p">()</span>

            <span class="k">if</span> <span class="n">vector_store</span><span class="p">:</span>
                <span class="n">vector_stores</span> <span class="o">=</span> <span class="p">{</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">vector_store</span><span class="p">}</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">vector_stores</span> <span class="ow">or</span> <span class="p">{</span>
                    <span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">SimpleVectorStore</span><span class="p">()</span>
                <span class="p">}</span>
            <span class="k">if</span> <span class="n">image_store</span><span class="p">:</span>
                <span class="c1"># append image store to vector stores</span>
                <span class="n">vector_stores</span><span class="p">[</span><span class="n">IMAGE_VECTOR_STORE_NAMESPACE</span><span class="p">]</span> <span class="o">=</span> <span class="n">image_store</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">docstore</span> <span class="o">=</span> <span class="n">docstore</span> <span class="ow">or</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
                <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>
            <span class="n">index_store</span> <span class="o">=</span> <span class="n">index_store</span> <span class="ow">or</span> <span class="n">SimpleIndexStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
                <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>
            <span class="n">graph_store</span> <span class="o">=</span> <span class="n">graph_store</span> <span class="ow">or</span> <span class="n">SimpleGraphStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
                <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">property_graph_store</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">property_graph_store</span>
                    <span class="ow">or</span> <span class="n">SimplePropertyGraphStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">FileNotFoundError</span><span class="p">:</span>
                <span class="n">property_graph_store</span> <span class="o">=</span> <span class="kc">None</span>

            <span class="k">if</span> <span class="n">vector_store</span><span class="p">:</span>
                <span class="n">vector_stores</span> <span class="o">=</span> <span class="p">{</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">vector_store</span><span class="p">}</span>
            <span class="k">elif</span> <span class="n">vector_stores</span><span class="p">:</span>
                <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">vector_stores</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">SimpleVectorStore</span><span class="o">.</span><span class="n">from_namespaced_persist_dir</span><span class="p">(</span>
                    <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
                <span class="p">)</span>
            <span class="k">if</span> <span class="n">image_store</span><span class="p">:</span>
                <span class="c1"># append image store to vector stores</span>
                <span class="n">vector_stores</span><span class="p">[</span><span class="n">IMAGE_VECTOR_STORE_NAMESPACE</span><span class="p">]</span> <span class="o">=</span> <span class="n">image_store</span>  <span class="c1"># type: ignore</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">,</span>
            <span class="n">index_store</span><span class="o">=</span><span class="n">index_store</span><span class="p">,</span>
            <span class="n">vector_stores</span><span class="o">=</span><span class="n">vector_stores</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
            <span class="n">graph_store</span><span class="o">=</span><span class="n">graph_store</span><span class="p">,</span>
            <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">PathLike</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">docstore_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
        <span class="n">index_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">INDEX_STORE_FNAME</span><span class="p">,</span>
        <span class="n">vector_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">VECTOR_STORE_FNAME</span><span class="p">,</span>
        <span class="n">image_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">IMAGE_STORE_FNAME</span><span class="p">,</span>
        <span class="n">graph_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">GRAPH_STORE_FNAME</span><span class="p">,</span>
        <span class="n">pg_graph_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PG_FNAME</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the storage context.</span>

<span class="sd">        Args:</span>
<span class="sd">            persist_dir (str): directory to persist the storage context</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">persist_dir</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>  <span class="c1"># NOTE: doesn't support Windows here</span>
            <span class="n">docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_fname</span><span class="p">)</span>
            <span class="n">index_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">index_store_fname</span><span class="p">)</span>
            <span class="n">graph_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">graph_store_fname</span><span class="p">)</span>
            <span class="n">pg_graph_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">pg_graph_store_fname</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">persist_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
            <span class="n">docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">docstore_fname</span><span class="p">)</span>
            <span class="n">index_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">index_store_fname</span><span class="p">)</span>
            <span class="n">graph_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">graph_store_fname</span><span class="p">)</span>
            <span class="n">pg_graph_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">pg_graph_store_fname</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">docstore_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">index_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">graph_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">pg_graph_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

        <span class="c1"># save each vector store under it's namespace</span>
        <span class="k">for</span> <span class="n">vector_store_name</span><span class="p">,</span> <span class="n">vector_store</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">vector_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span>
                    <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">),</span>
                    <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">vector_store_name</span><span class="si">}{</span><span class="n">NAMESPACE_SEP</span><span class="si">}{</span><span class="n">vector_store_fname</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">vector_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span>
                    <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
                    <span class="o">/</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">vector_store_name</span><span class="si">}{</span><span class="n">NAMESPACE_SEP</span><span class="si">}{</span><span class="n">vector_store_fname</span><span class="si">}</span><span class="s2">"</span>
                <span class="p">)</span>

            <span class="n">vector_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">vector_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="n">all_simple</span> <span class="o">=</span> <span class="p">(</span>
            <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="p">,</span> <span class="n">SimpleDocumentStore</span><span class="p">)</span>
            <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_store</span><span class="p">,</span> <span class="n">SimpleIndexStore</span><span class="p">)</span>
            <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="p">,</span> <span class="n">SimpleGraphStore</span><span class="p">)</span>
            <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span> <span class="p">(</span><span class="n">SimplePropertyGraphStore</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">))</span>
            <span class="p">)</span>
            <span class="ow">and</span> <span class="nb">all</span><span class="p">(</span>
                <span class="nb">isinstance</span><span class="p">(</span><span class="n">vs</span><span class="p">,</span> <span class="n">SimpleVectorStore</span><span class="p">)</span> <span class="k">for</span> <span class="n">vs</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="o">.</span><span class="n">values</span><span class="p">()</span>
            <span class="p">)</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">all_simple</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"to_dict only available when using simple doc/index/vector stores"</span>
            <span class="p">)</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="p">,</span> <span class="n">SimpleDocumentStore</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">index_store</span><span class="p">,</span> <span class="n">SimpleIndexStore</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="p">,</span> <span class="n">SimpleGraphStore</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">,</span> <span class="p">(</span><span class="n">SimplePropertyGraphStore</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">))</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="n">VECTOR_STORE_KEY</span><span class="p">:</span> <span class="p">{</span>
                <span class="n">key</span><span class="p">:</span> <span class="n">vector_store</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
                <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">vector_store</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">vector_store</span><span class="p">,</span> <span class="n">SimpleVectorStore</span><span class="p">)</span>
            <span class="p">},</span>
            <span class="n">DOC_STORE_KEY</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(),</span>
            <span class="n">INDEX_STORE_KEY</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(),</span>
            <span class="n">GRAPH_STORE_KEY</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">to_dict</span><span class="p">(),</span>
            <span class="n">PG_STORE_KEY</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span>
            <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">save_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StorageContext"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a StorageContext from dict."""</span>
        <span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">DOC_STORE_KEY</span><span class="p">])</span>
        <span class="n">index_store</span> <span class="o">=</span> <span class="n">SimpleIndexStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">INDEX_STORE_KEY</span><span class="p">])</span>
        <span class="n">graph_store</span> <span class="o">=</span> <span class="n">SimpleGraphStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">GRAPH_STORE_KEY</span><span class="p">])</span>
        <span class="n">property_graph_store</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">SimplePropertyGraphStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">PG_STORE_KEY</span><span class="p">])</span>
            <span class="k">if</span> <span class="n">save_dict</span><span class="p">[</span><span class="n">PG_STORE_KEY</span><span class="p">]</span>
            <span class="k">else</span> <span class="kc">None</span>
        <span class="p">)</span>

        <span class="n">vector_stores</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">vector_store_dict</span> <span class="ow">in</span> <span class="n">save_dict</span><span class="p">[</span><span class="n">VECTOR_STORE_KEY</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">vector_stores</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">SimpleVectorStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">vector_store_dict</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">,</span>
            <span class="n">index_store</span><span class="o">=</span><span class="n">index_store</span><span class="p">,</span>
            <span class="n">vector_stores</span><span class="o">=</span><span class="n">vector_stores</span><span class="p">,</span>
            <span class="n">graph_store</span><span class="o">=</span><span class="n">graph_store</span><span class="p">,</span>
            <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">vector_store</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BasePydanticVectorStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Backwrds compatibility for vector_store property."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="p">[</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">add_vector_store</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">vector_store</span><span class="p">:</span> <span class="n">BasePydanticVectorStore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add a vector store to the storage context."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="p">[</span><span class="n">namespace</span><span class="p">]</span> <span class="o">=</span> <span class="n">vector_store</span>
</code></pre></div></td></tr></tbody></table>

### vector\_store `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext.vector_store "Permanent link")

```
vector_store: [BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")
```

Backwrds compatibility for vector\_store property.

### from\_defaults `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext.from_defaults "Permanent link")

```
from_defaults(docstore: Optional[[BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.types.BaseDocumentStore")] = None, index_store: Optional[[BaseIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/#llama_index.core.storage.index_store.types.BaseIndexStore "llama_index.core.storage.index_store.types.BaseIndexStore")] = None, vector_store: Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")] = None, image_store: Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")] = None, vector_stores: Optional[Dict[str, [BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")]] = None, graph_store: Optional[[GraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "llama_index.core.graph_stores.types.GraphStore")] = None, property_graph_store: Optional[PropertyGraphStore] = None, persist_dir: Optional[str] = None, fs: Optional[AbstractFileSystem] = None) -> [StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")
```

Create a StorageContext from defaults.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `docstore` | `Optional[[BaseDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/#llama_index.core.storage.docstore.types.BaseDocumentStore "llama_index.core.storage.docstore.types.BaseDocumentStore")]` | 
document store



 | `None` |
| `index_store` | `Optional[[BaseIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/#llama_index.core.storage.index_store.types.BaseIndexStore "llama_index.core.storage.index_store.types.BaseIndexStore")]` | 

index store



 | `None` |
| `vector_store` | `Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")]` | 

vector store



 | `None` |
| `graph_store` | `Optional[[GraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "llama_index.core.graph_stores.types.GraphStore")]` | 

graph store



 | `None` |
| `image_store` | `Optional[[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")]` | 

image store



 | `None` |

Source code in `llama-index-core/llama_index/core/storage/storage_context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 71</span>
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
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_defaults</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">docstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseDocumentStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">index_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseIndexStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">vector_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">image_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">vector_stores</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePydanticVectorStore</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">property_graph_store</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PropertyGraphStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StorageContext"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a StorageContext from defaults.</span>

<span class="sd">    Args:</span>
<span class="sd">        docstore (Optional[BaseDocumentStore]): document store</span>
<span class="sd">        index_store (Optional[BaseIndexStore]): index store</span>
<span class="sd">        vector_store (Optional[BasePydanticVectorStore]): vector store</span>
<span class="sd">        graph_store (Optional[GraphStore]): graph store</span>
<span class="sd">        image_store (Optional[BasePydanticVectorStore]): image store</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">persist_dir</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">docstore</span> <span class="o">=</span> <span class="n">docstore</span> <span class="ow">or</span> <span class="n">SimpleDocumentStore</span><span class="p">()</span>
        <span class="n">index_store</span> <span class="o">=</span> <span class="n">index_store</span> <span class="ow">or</span> <span class="n">SimpleIndexStore</span><span class="p">()</span>
        <span class="n">graph_store</span> <span class="o">=</span> <span class="n">graph_store</span> <span class="ow">or</span> <span class="n">SimpleGraphStore</span><span class="p">()</span>
        <span class="n">image_store</span> <span class="o">=</span> <span class="n">image_store</span> <span class="ow">or</span> <span class="n">SimpleVectorStore</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">vector_store</span><span class="p">:</span>
            <span class="n">vector_stores</span> <span class="o">=</span> <span class="p">{</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">vector_store</span><span class="p">}</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">vector_stores</span> <span class="ow">or</span> <span class="p">{</span>
                <span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">SimpleVectorStore</span><span class="p">()</span>
            <span class="p">}</span>
        <span class="k">if</span> <span class="n">image_store</span><span class="p">:</span>
            <span class="c1"># append image store to vector stores</span>
            <span class="n">vector_stores</span><span class="p">[</span><span class="n">IMAGE_VECTOR_STORE_NAMESPACE</span><span class="p">]</span> <span class="o">=</span> <span class="n">image_store</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">docstore</span> <span class="o">=</span> <span class="n">docstore</span> <span class="ow">or</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
            <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
        <span class="p">)</span>
        <span class="n">index_store</span> <span class="o">=</span> <span class="n">index_store</span> <span class="ow">or</span> <span class="n">SimpleIndexStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
            <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
        <span class="p">)</span>
        <span class="n">graph_store</span> <span class="o">=</span> <span class="n">graph_store</span> <span class="ow">or</span> <span class="n">SimpleGraphStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span>
            <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
        <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">property_graph_store</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">property_graph_store</span>
                <span class="ow">or</span> <span class="n">SimplePropertyGraphStore</span><span class="o">.</span><span class="n">from_persist_dir</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">FileNotFoundError</span><span class="p">:</span>
            <span class="n">property_graph_store</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="n">vector_store</span><span class="p">:</span>
            <span class="n">vector_stores</span> <span class="o">=</span> <span class="p">{</span><span class="n">DEFAULT_VECTOR_STORE</span><span class="p">:</span> <span class="n">vector_store</span><span class="p">}</span>
        <span class="k">elif</span> <span class="n">vector_stores</span><span class="p">:</span>
            <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">vector_stores</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">vector_stores</span> <span class="o">=</span> <span class="n">SimpleVectorStore</span><span class="o">.</span><span class="n">from_namespaced_persist_dir</span><span class="p">(</span>
                <span class="n">persist_dir</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">image_store</span><span class="p">:</span>
            <span class="c1"># append image store to vector stores</span>
            <span class="n">vector_stores</span><span class="p">[</span><span class="n">IMAGE_VECTOR_STORE_NAMESPACE</span><span class="p">]</span> <span class="o">=</span> <span class="n">image_store</span>  <span class="c1"># type: ignore</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">,</span>
        <span class="n">index_store</span><span class="o">=</span><span class="n">index_store</span><span class="p">,</span>
        <span class="n">vector_stores</span><span class="o">=</span><span class="n">vector_stores</span><span class="p">,</span>  <span class="c1"># type: ignore</span>
        <span class="n">graph_store</span><span class="o">=</span><span class="n">graph_store</span><span class="p">,</span>
        <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext.persist "Permanent link")

```
persist(persist_dir: Union[str, PathLike] = DEFAULT_PERSIST_DIR, docstore_fname: str = DOCSTORE_FNAME, index_store_fname: str = INDEX_STORE_FNAME, vector_store_fname: str = VECTOR_STORE_FNAME, image_store_fname: str = IMAGE_STORE_FNAME, graph_store_fname: str = GRAPH_STORE_FNAME, pg_graph_store_fname: str = PG_FNAME, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the storage context.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `persist_dir` | `str` | 
directory to persist the storage context



 | `DEFAULT_PERSIST_DIR` |

Source code in `llama-index-core/llama_index/core/storage/storage_context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
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
<span class="normal">197</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">PathLike</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
    <span class="n">docstore_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DOCSTORE_FNAME</span><span class="p">,</span>
    <span class="n">index_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">INDEX_STORE_FNAME</span><span class="p">,</span>
    <span class="n">vector_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">VECTOR_STORE_FNAME</span><span class="p">,</span>
    <span class="n">image_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">IMAGE_STORE_FNAME</span><span class="p">,</span>
    <span class="n">graph_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">GRAPH_STORE_FNAME</span><span class="p">,</span>
    <span class="n">pg_graph_store_fname</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PG_FNAME</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the storage context.</span>

<span class="sd">    Args:</span>
<span class="sd">        persist_dir (str): directory to persist the storage context</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">persist_dir</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>  <span class="c1"># NOTE: doesn't support Windows here</span>
        <span class="n">docstore_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">docstore_fname</span><span class="p">)</span>
        <span class="n">index_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">index_store_fname</span><span class="p">)</span>
        <span class="n">graph_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">graph_store_fname</span><span class="p">)</span>
        <span class="n">pg_graph_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">pg_graph_store_fname</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">persist_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
        <span class="n">docstore_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">docstore_fname</span><span class="p">)</span>
        <span class="n">index_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">index_store_fname</span><span class="p">)</span>
        <span class="n">graph_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">graph_store_fname</span><span class="p">)</span>
        <span class="n">pg_graph_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span> <span class="o">/</span> <span class="n">pg_graph_store_fname</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">docstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">docstore_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">index_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">graph_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">graph_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">property_graph_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">pg_graph_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="c1"># save each vector store under it's namespace</span>
    <span class="k">for</span> <span class="n">vector_store_name</span><span class="p">,</span> <span class="n">vector_store</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">vector_store_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">),</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">vector_store_name</span><span class="si">}{</span><span class="n">NAMESPACE_SEP</span><span class="si">}{</span><span class="n">vector_store_fname</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">vector_store_path</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span>
                <span class="n">Path</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">)</span>
                <span class="o">/</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">vector_store_name</span><span class="si">}{</span><span class="n">NAMESPACE_SEP</span><span class="si">}{</span><span class="n">vector_store_fname</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="n">vector_store</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="o">=</span><span class="n">vector_store_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_dict `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext.from_dict "Permanent link")

```
from_dict(save_dict: dict) -> [StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")
```

Create a StorageContext from dict.

Source code in `llama-index-core/llama_index/core/storage/storage_context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">237</span>
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
<span class="normal">259</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">save_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"StorageContext"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a StorageContext from dict."""</span>
    <span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">DOC_STORE_KEY</span><span class="p">])</span>
    <span class="n">index_store</span> <span class="o">=</span> <span class="n">SimpleIndexStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">INDEX_STORE_KEY</span><span class="p">])</span>
    <span class="n">graph_store</span> <span class="o">=</span> <span class="n">SimpleGraphStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">GRAPH_STORE_KEY</span><span class="p">])</span>
    <span class="n">property_graph_store</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">SimplePropertyGraphStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">[</span><span class="n">PG_STORE_KEY</span><span class="p">])</span>
        <span class="k">if</span> <span class="n">save_dict</span><span class="p">[</span><span class="n">PG_STORE_KEY</span><span class="p">]</span>
        <span class="k">else</span> <span class="kc">None</span>
    <span class="p">)</span>

    <span class="n">vector_stores</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BasePydanticVectorStore</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">vector_store_dict</span> <span class="ow">in</span> <span class="n">save_dict</span><span class="p">[</span><span class="n">VECTOR_STORE_KEY</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">vector_stores</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">SimpleVectorStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">vector_store_dict</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">,</span>
        <span class="n">index_store</span><span class="o">=</span><span class="n">index_store</span><span class="p">,</span>
        <span class="n">vector_stores</span><span class="o">=</span><span class="n">vector_stores</span><span class="p">,</span>
        <span class="n">graph_store</span><span class="o">=</span><span class="n">graph_store</span><span class="p">,</span>
        <span class="n">property_graph_store</span><span class="o">=</span><span class="n">property_graph_store</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add\_vector\_store [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext.add_vector_store "Permanent link")

```
add_vector_store(vector_store: [BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore"), namespace: str) -> None
```

Add a vector store to the storage context.

Source code in `llama-index-core/llama_index/core/storage/storage_context.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add_vector_store</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">vector_store</span><span class="p">:</span> <span class="n">BasePydanticVectorStore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add a vector store to the storage context."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">vector_stores</span><span class="p">[</span><span class="n">namespace</span><span class="p">]</span> <span class="o">=</span> <span class="n">vector_store</span>
</code></pre></div></td></tr></tbody></table>

Init file of LlamaIndex.

load\_index\_from\_storage [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.load_index_from_storage "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
load_index_from_storage(storage_context: [StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext"), index_id: Optional[str] = None, **kwargs: Any) -> [BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")
```

Load index from storage context.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `storage_context` | `[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")` | 
storage context containing docstore, index store and vector store.



 | _required_ |
| `index_id` | `Optional[str]` | 

ID of the index to load. Defaults to None, which assumes there's only a single index in the index store and load it.



 | `None` |
| `**kwargs` | `Any` | 

Additional keyword args to pass to the index constructors.



 | `{}` |

Source code in `llama-index-core/llama_index/core/indices/loading.py`

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
<span class="normal">45</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_index_from_storage</span><span class="p">(</span>
    <span class="n">storage_context</span><span class="p">:</span> <span class="n">StorageContext</span><span class="p">,</span>
    <span class="n">index_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseIndex</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load index from storage context.</span>

<span class="sd">    Args:</span>
<span class="sd">        storage_context (StorageContext): storage context containing</span>
<span class="sd">            docstore, index store and vector store.</span>
<span class="sd">        index_id (Optional[str]): ID of the index to load.</span>
<span class="sd">            Defaults to None, which assumes there's only a single index</span>
<span class="sd">            in the index store and load it.</span>
<span class="sd">        **kwargs: Additional keyword args to pass to the index constructors.</span>
<span class="sd">    """</span>
    <span class="n">index_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>
    <span class="k">if</span> <span class="n">index_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">index_ids</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">index_ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">index_id</span><span class="p">]</span>

    <span class="n">indices</span> <span class="o">=</span> <span class="n">load_indices_from_storage</span><span class="p">(</span><span class="n">storage_context</span><span class="p">,</span> <span class="n">index_ids</span><span class="o">=</span><span class="n">index_ids</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"No index in storage context, check if you specified the right persist_dir."</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Expected to load a single index, but got </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">indices</span><span class="p">)</span><span class="si">}</span><span class="s2"> instead. "</span>
            <span class="s2">"Please specify index_id."</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">indices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

load\_indices\_from\_storage [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.load_indices_from_storage "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
load_indices_from_storage(storage_context: [StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext"), index_ids: Optional[Sequence[str]] = None, **kwargs: Any) -> List[[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")]
```

Load multiple indices from storage context.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `storage_context` | `[StorageContext](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/#llama_index.core.storage.storage_context.StorageContext "llama_index.core.storage.storage_context.StorageContext")` | 
storage context containing docstore, index store and vector store.



 | _required_ |
| `index_id` | `Optional[Sequence[str]]` | 

IDs of the indices to load. Defaults to None, which loads all indices in the index store.



 | _required_ |
| `**kwargs` | `Any` | 

Additional keyword args to pass to the index constructors.



 | `{}` |

Source code in `llama-index-core/llama_index/core/indices/loading.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">48</span>
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
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_indices_from_storage</span><span class="p">(</span>
    <span class="n">storage_context</span><span class="p">:</span> <span class="n">StorageContext</span><span class="p">,</span>
    <span class="n">index_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseIndex</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load multiple indices from storage context.</span>

<span class="sd">    Args:</span>
<span class="sd">        storage_context (StorageContext): storage context containing</span>
<span class="sd">            docstore, index store and vector store.</span>
<span class="sd">        index_id (Optional[Sequence[str]]): IDs of the indices to load.</span>
<span class="sd">            Defaults to None, which loads all indices in the index store.</span>
<span class="sd">        **kwargs: Additional keyword args to pass to the index constructors.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">index_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Loading all indices."</span><span class="p">)</span>
        <span class="n">index_structs</span> <span class="o">=</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">index_structs</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Loading indices with ids: </span><span class="si">{</span><span class="n">index_ids</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">index_structs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">index_id</span> <span class="ow">in</span> <span class="n">index_ids</span><span class="p">:</span>
            <span class="n">index_struct</span> <span class="o">=</span> <span class="n">storage_context</span><span class="o">.</span><span class="n">index_store</span><span class="o">.</span><span class="n">get_index_struct</span><span class="p">(</span><span class="n">index_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">index_struct</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to load index with ID </span><span class="si">{</span><span class="n">index_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">index_structs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_struct</span><span class="p">)</span>

    <span class="n">indices</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">index_struct</span> <span class="ow">in</span> <span class="n">index_structs</span><span class="p">:</span>
        <span class="n">type_</span> <span class="o">=</span> <span class="n">index_struct</span><span class="o">.</span><span class="n">get_type</span><span class="p">()</span>
        <span class="n">index_cls</span> <span class="o">=</span> <span class="n">INDEX_STRUCT_TYPE_TO_INDEX_CLASS</span><span class="p">[</span><span class="n">type_</span><span class="p">]</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">index_cls</span><span class="p">(</span>
            <span class="n">index_struct</span><span class="o">=</span><span class="n">index_struct</span><span class="p">,</span> <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>
        <span class="n">indices</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">indices</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/)[Next Alibabacloud opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/alibabacloud_opensearch/)
