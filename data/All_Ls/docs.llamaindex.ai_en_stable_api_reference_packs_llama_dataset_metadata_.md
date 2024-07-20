Title: Llama dataset metadata - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/

Markdown Content:
Llama dataset metadata - LlamaIndex


LlamaDatasetMetadataPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/#llama_index.packs.llama_dataset_metadata.LlamaDatasetMetadataPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

A llamapack for creating and saving the necessary metadata files for submitting a llamadataset: card.json and README.md.

Source code in `llama-index-packs/llama-index-packs-llama-dataset-metadata/llama_index/packs/llama_dataset_metadata/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
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
<span class="normal">248</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LlamaDatasetMetadataPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A llamapack for creating and saving the necessary metadata files for</span>
<span class="sd">    submitting a llamadataset: card.json and README.md.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">BaseIndex</span><span class="p">,</span>
        <span class="n">benchmark_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
        <span class="n">rag_dataset</span><span class="p">:</span> <span class="s2">"LabelledRagDataset"</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">baseline_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">source_urls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">code_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Main usage for a llamapack. This will build the card.json and README.md</span>
<span class="sd">        and save them to local disk.</span>

<span class="sd">        Args:</span>
<span class="sd">            index (BaseIndex): the index from which query_engine is derived and</span>
<span class="sd">                used in the rag evaluation.</span>
<span class="sd">            benchmark_df (pd.DataFrame): the benchmark dataframe after using</span>
<span class="sd">                RagEvaluatorPack</span>
<span class="sd">            rag_dataset (LabelledRagDataset): the LabelledRagDataset used for</span>
<span class="sd">                evaluations</span>
<span class="sd">            name (str): The name of the new dataset e.g., "Paul Graham Essay Dataset"</span>
<span class="sd">            baseline_name (str): The name of the baseline e.g., "llamaindex"</span>
<span class="sd">            description (str): The description of the new dataset.</span>
<span class="sd">            source_urls (Optional[List[str]], optional): _description_. Defaults to None.</span>
<span class="sd">            code_url (Optional[str], optional): _description_. Defaults to None.</span>
<span class="sd">        """</span>
        <span class="n">readme_obj</span> <span class="o">=</span> <span class="n">Readme</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
        <span class="n">card_obj</span> <span class="o">=</span> <span class="n">DatasetCard</span><span class="o">.</span><span class="n">from_rag_evaluation</span><span class="p">(</span>
            <span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span>
            <span class="n">benchmark_df</span><span class="o">=</span><span class="n">benchmark_df</span><span class="p">,</span>
            <span class="n">rag_dataset</span><span class="o">=</span><span class="n">rag_dataset</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
            <span class="n">baseline_name</span><span class="o">=</span><span class="n">baseline_name</span><span class="p">,</span>
            <span class="n">source_urls</span><span class="o">=</span><span class="n">source_urls</span><span class="p">,</span>
            <span class="n">code_url</span><span class="o">=</span><span class="n">code_url</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># save card.json</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"card.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">card_obj</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span> <span class="n">f</span><span class="p">)</span>

        <span class="c1"># save README.md</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"README.md"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">readme_obj</span><span class="o">.</span><span class="n">create_readme</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/#llama_index.packs.llama_dataset_metadata.LlamaDatasetMetadataPack.run "Permanent link")

```
run(index: [BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex"), benchmark_df: DataFrame, rag_dataset: [LabelledRagDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataset "llama_index.core.llama_dataset.LabelledRagDataset"), name: str, description: str, baseline_name: str, source_urls: Optional[List[str]] = None, code_url: Optional[str] = None)
```

Main usage for a llamapack. This will build the card.json and README.md and save them to local disk.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `[BaseIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/#llama_index.core.indices.base.BaseIndex "llama_index.core.indices.base.BaseIndex")` | 
the index from which query\_engine is derived and used in the rag evaluation.



 | _required_ |
| `benchmark_df` | `DataFrame` | 

the benchmark dataframe after using RagEvaluatorPack



 | _required_ |
| `rag_dataset` | `[LabelledRagDataset](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/#llama_index.core.llama_dataset.LabelledRagDataset "llama_index.core.llama_dataset.LabelledRagDataset")` | 

the LabelledRagDataset used for evaluations



 | _required_ |
| `name` | `str` | 

The name of the new dataset e.g., "Paul Graham Essay Dataset"



 | _required_ |
| `baseline_name` | `str` | 

The name of the baseline e.g., "llamaindex"



 | _required_ |
| `description` | `str` | 

The description of the new dataset.



 | _required_ |
| `source_urls` | `Optional[List[str]]` | 

_description_. Defaults to None.



 | `None` |
| `code_url` | `Optional[str]` | 

_description_. Defaults to None.



 | `None` |

Source code in `llama-index-packs/llama-index-packs-llama-dataset-metadata/llama_index/packs/llama_dataset_metadata/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">203</span>
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
<span class="normal">248</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">index</span><span class="p">:</span> <span class="n">BaseIndex</span><span class="p">,</span>
    <span class="n">benchmark_df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
    <span class="n">rag_dataset</span><span class="p">:</span> <span class="s2">"LabelledRagDataset"</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">baseline_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">source_urls</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">code_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Main usage for a llamapack. This will build the card.json and README.md</span>
<span class="sd">    and save them to local disk.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (BaseIndex): the index from which query_engine is derived and</span>
<span class="sd">            used in the rag evaluation.</span>
<span class="sd">        benchmark_df (pd.DataFrame): the benchmark dataframe after using</span>
<span class="sd">            RagEvaluatorPack</span>
<span class="sd">        rag_dataset (LabelledRagDataset): the LabelledRagDataset used for</span>
<span class="sd">            evaluations</span>
<span class="sd">        name (str): The name of the new dataset e.g., "Paul Graham Essay Dataset"</span>
<span class="sd">        baseline_name (str): The name of the baseline e.g., "llamaindex"</span>
<span class="sd">        description (str): The description of the new dataset.</span>
<span class="sd">        source_urls (Optional[List[str]], optional): _description_. Defaults to None.</span>
<span class="sd">        code_url (Optional[str], optional): _description_. Defaults to None.</span>
<span class="sd">    """</span>
    <span class="n">readme_obj</span> <span class="o">=</span> <span class="n">Readme</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
    <span class="n">card_obj</span> <span class="o">=</span> <span class="n">DatasetCard</span><span class="o">.</span><span class="n">from_rag_evaluation</span><span class="p">(</span>
        <span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span>
        <span class="n">benchmark_df</span><span class="o">=</span><span class="n">benchmark_df</span><span class="p">,</span>
        <span class="n">rag_dataset</span><span class="o">=</span><span class="n">rag_dataset</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="n">description</span><span class="p">,</span>
        <span class="n">baseline_name</span><span class="o">=</span><span class="n">baseline_name</span><span class="p">,</span>
        <span class="n">source_urls</span><span class="o">=</span><span class="n">source_urls</span><span class="p">,</span>
        <span class="n">code_url</span><span class="o">=</span><span class="n">code_url</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="c1"># save card.json</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"card.json"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">card_obj</span><span class="o">.</span><span class="n">dict</span><span class="p">(</span><span class="n">by_alias</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span> <span class="n">f</span><span class="p">)</span>

    <span class="c1"># save README.md</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"README.md"</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">readme_obj</span><span class="o">.</span><span class="n">create_readme</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Koda retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/koda_retriever/)[Next Llama guard moderator](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/)
