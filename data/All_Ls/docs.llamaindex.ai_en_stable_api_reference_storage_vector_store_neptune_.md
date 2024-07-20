Title: Neptune - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/

Markdown Content:
Neptune - LlamaIndex


NeptuneAnalyticsVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/#llama_index.vector_stores.neptune.NeptuneAnalyticsVectorStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neptune/llama_index/vector_stores/neptune/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
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
<span class="normal">246</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NeptuneAnalyticsVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">graph_identifier</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">text_node_property</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">retrieval_query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">graph_identifier</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">credentials_profile_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Chunk"</span><span class="p">,</span>
        <span class="n">text_node_property</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">retrieval_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Neptune Analytics graph wrapper instance."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">graph_identifier</span><span class="o">=</span><span class="n">graph_identifier</span><span class="p">,</span>
            <span class="n">embedding_dimension</span><span class="o">=</span><span class="n">embedding_dimension</span><span class="p">,</span>
            <span class="n">node_label</span><span class="o">=</span><span class="n">node_label</span><span class="p">,</span>
            <span class="n">text_node_property</span><span class="o">=</span><span class="n">text_node_property</span><span class="p">,</span>
            <span class="n">hybrid_search</span><span class="o">=</span><span class="n">hybrid_search</span><span class="p">,</span>
            <span class="n">retrieval_query</span><span class="o">=</span><span class="n">retrieval_query</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">boto3</span>

                <span class="k">if</span> <span class="n">credentials_profile_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">(</span><span class="n">profile_name</span><span class="o">=</span><span class="n">credentials_profile_name</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="c1"># use default credentials</span>
                    <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>

                <span class="k">if</span> <span class="n">region_name</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>
                        <span class="s2">"neptune-graph"</span><span class="p">,</span> <span class="n">region_name</span><span class="o">=</span><span class="n">region_name</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">client</span><span class="p">(</span><span class="s2">"neptune-graph"</span><span class="p">)</span>

        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ModuleNotFoundError</span><span class="p">(</span>
                <span class="s2">"Could not import boto3 python package. "</span>
                <span class="s2">"Please install it with `pip install boto3`."</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span> <span class="o"></span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span>
            <span class="p">):</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Vector search index dimension for Neptune Analytics graph does not match the provided value."</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Vector search index does not exist for the Neptune Analytics graph."</span>
            <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"NeptuneAnalyticsVectorStore"</span>

    <span class="k">def</span> <span class="nf">database_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This method sends a query to the Neptune Analytics graph</span>
<span class="sd">        and returns the results as a list of dictionaries.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The openCypher query to execute.</span>
<span class="sd">            params (dict, optional): Dictionary of query parameters. Defaults to {}.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Dict[str, Any]]: List of dictionaries containing the query results.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query() query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> parameters: </span><span class="si">{</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">execute_query</span><span class="p">(</span>
                <span class="n">graphIdentifier</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_identifier</span><span class="p">,</span>
                <span class="n">queryString</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
                <span class="n">parameters</span><span class="o">=</span><span class="n">params</span><span class="p">,</span>
                <span class="n">language</span><span class="o">=</span><span class="s2">"OPEN_CYPHER"</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">resp</span><span class="p">[</span><span class="s2">"payload"</span><span class="p">]</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"UTF-8"</span><span class="p">))[</span><span class="s2">"results"</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NeptuneVectorQueryException</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s2">"message"</span><span class="p">:</span> <span class="s2">"An error occurred while executing the query."</span><span class="p">,</span>
                    <span class="s2">"details"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
                <span class="p">}</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

        <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">import_query</span> <span class="o">=</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"MERGE (c:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">` </span><span class="se">{{</span><span class="s2">`~id`: $id</span><span class="se">}}</span><span class="s2">) "</span>
                <span class="s2">"SET c += $data "</span>
                <span class="s2">"WITH c "</span>
                <span class="sa">f</span><span class="s2">"CALL neptune.algo.vectors.upsert(c, </span><span class="si">{</span><span class="n">r</span><span class="o">.</span><span class="n">embedding</span><span class="si">}</span><span class="s2">) "</span>
                <span class="s2">"YIELD node "</span>
                <span class="s2">"RETURN id(node) as id"</span>
            <span class="p">)</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
                <span class="n">import_query</span><span class="p">,</span>
                <span class="n">params</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">__clean_params</span><span class="p">(</span><span class="n">r</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Nodes added"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">_get_search_index_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">hybrid</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">hybrid</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="s2">"WITH $embedding as emb "</span>
                <span class="s2">"CALL neptune.algo.vectors.topKByEmbedding(emb, {topK: "</span>
                <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
                <span class="o">+</span> <span class="s2">"}) YIELD embedding, node, score "</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">default_retrieval</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"RETURN node.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="si">}</span><span class="s2">` AS text, score, "</span>
            <span class="s2">"id(node) AS id, "</span>
            <span class="sa">f</span><span class="s2">"node AS metadata"</span>
        <span class="p">)</span>

        <span class="n">retrieval_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieval_query</span> <span class="ow">or</span> <span class="n">default_retrieval</span>
        <span class="n">read_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_get_search_index_query</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hybrid_search</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">)</span>
            <span class="o">+</span> <span class="n">retrieval_query</span>
        <span class="p">)</span>

        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">read_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">][</span><span class="s2">"~properties"</span><span class="p">])</span>
            <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]))</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"id"</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"MATCH (n:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">`) WHERE n.ref_doc_id = $id DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">__clean_params</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">record</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Convert BaseNode object to a dictionary to be imported into Neo4j."""</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span>
        <span class="nb">id</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">node_id</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">record</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="c1"># Remove redundant metadata information</span>
        <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"document_id"</span><span class="p">,</span> <span class="s2">"doc_id"</span><span class="p">]:</span>
            <span class="k">del</span> <span class="n">metadata</span><span class="p">[</span><span class="n">k</span><span class="p">]</span>
        <span class="k">return</span> <span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="nb">id</span><span class="p">,</span> <span class="s2">"data"</span><span class="p">:</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="p">:</span> <span class="n">text</span><span class="p">,</span> <span class="s2">"id"</span><span class="p">:</span> <span class="nb">id</span><span class="p">,</span> <span class="o">**</span><span class="n">metadata</span><span class="p">}}</span>
</code></pre></div></td></tr></tbody></table>

### database\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/#llama_index.vector_stores.neptune.NeptuneAnalyticsVectorStore.database_query "Permanent link")

```
database_query(query: str, params: Optional[dict] = None) -> List[Dict[str, Any]]
```

This method sends a query to the Neptune Analytics graph and returns the results as a list of dictionaries.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The openCypher query to execute.



 | _required_ |
| `params` | `dict` | 

Dictionary of query parameters. Defaults to {}.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[Dict[str, Any]]` | 
List\[Dict\[str, Any\]\]: List of dictionaries containing the query results.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neptune/llama_index/vector_stores/neptune/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
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
<span class="normal">169</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">database_query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This method sends a query to the Neptune Analytics graph</span>
<span class="sd">    and returns the results as a list of dictionaries.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The openCypher query to execute.</span>
<span class="sd">        params (dict, optional): Dictionary of query parameters. Defaults to {}.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Dict[str, Any]]: List of dictionaries containing the query results.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query() query: </span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2"> parameters: </span><span class="si">{</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">params</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">execute_query</span><span class="p">(</span>
            <span class="n">graphIdentifier</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">graph_identifier</span><span class="p">,</span>
            <span class="n">queryString</span><span class="o">=</span><span class="n">query</span><span class="p">,</span>
            <span class="n">parameters</span><span class="o">=</span><span class="n">params</span><span class="p">,</span>
            <span class="n">language</span><span class="o">=</span><span class="s2">"OPEN_CYPHER"</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">resp</span><span class="p">[</span><span class="s2">"payload"</span><span class="p">]</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"UTF-8"</span><span class="p">))[</span><span class="s2">"results"</span><span class="p">]</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">NeptuneVectorQueryException</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s2">"message"</span><span class="p">:</span> <span class="s2">"An error occurred while executing the query."</span><span class="p">,</span>
                <span class="s2">"details"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">),</span>
            <span class="p">}</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Neo4jvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/)[Next Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/)
