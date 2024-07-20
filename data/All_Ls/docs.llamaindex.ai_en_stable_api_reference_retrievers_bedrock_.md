Title: Bedrock - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/

Markdown Content:
Bedrock - LlamaIndex


AmazonKnowledgeBasesRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/#llama_index.retrievers.bedrock.AmazonKnowledgeBasesRetriever "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

`Amazon Bedrock Knowledge Bases` retrieval.

See https://aws.amazon.com/bedrock/knowledge-bases for more info.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `knowledge_base_id` | `str` | 
Knowledge Base ID.



 | _required_ |
| `retrieval_config` | `Optional[Dict[str, Any]]` | 

Configuration for retrieval.



 | `None` |
| `profile_name` | `Optional[str]` | 

The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which has either access keys or role information specified. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used.



 | `None` |
| `region_name` | `Optional[str]` | 

The aws region e.g., `us-west-2`. Fallback to AWS\_DEFAULT\_REGION env variable or region specified in ~/.aws/config.



 | `None` |
| `aws_access_key_id` | `Optional[str]` | 

The aws access key id.



 | `None` |
| `aws_secret_access_key` | `Optional[str]` | 

The aws secret access key.



 | `None` |
| `aws_session_token` | `Optional[str]` | 

AWS temporary session token.



 | `None` |

Example.. code-block:: python

```
from llama_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="<knowledge-base-id>",
    retrieval_config={
        "vectorSearchConfiguration": {
            "numberOfResults": 4,
            "overrideSearchType": "SEMANTIC",
            "filter": {
                "equals": {
                    "key": "tag",
                    "value": "space"
                }
            }
        }
    },
)
```
Source code in `llama-index-integrations/retrievers/llama-index-retrievers-bedrock/llama_index/retrievers/bedrock/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
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
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
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
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span>
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AmazonKnowledgeBasesRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""`Amazon Bedrock Knowledge Bases` retrieval.</span>

<span class="sd">    See https://aws.amazon.com/bedrock/knowledge-bases for more info.</span>

<span class="sd">    Args:</span>
<span class="sd">        knowledge_base_id: Knowledge Base ID.</span>
<span class="sd">        retrieval_config: Configuration for retrieval.</span>
<span class="sd">        profile_name: The name of the profile in the ~/.aws/credentials</span>
<span class="sd">            or ~/.aws/config files, which has either access keys or role information</span>
<span class="sd">            specified. If not specified, the default credential profile or, if on an</span>
<span class="sd">            EC2 instance, credentials from IMDS will be used.</span>
<span class="sd">        region_name: The aws region e.g., `us-west-2`.</span>
<span class="sd">            Fallback to AWS_DEFAULT_REGION env variable or region specified in</span>
<span class="sd">            ~/.aws/config.</span>
<span class="sd">        aws_access_key_id: The aws access key id.</span>
<span class="sd">        aws_secret_access_key: The aws secret access key.</span>
<span class="sd">        aws_session_token: AWS temporary session token.</span>

<span class="sd">    Example:</span>
<span class="sd">        .. code-block:: python</span>

<span class="sd">            from llama_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever</span>

<span class="sd">            retriever = AmazonKnowledgeBasesRetriever(</span>
<span class="sd">                knowledge_base_id="&lt;knowledge-base-id&gt;",</span>
<span class="sd">                retrieval_config={</span>
<span class="sd">                    "vectorSearchConfiguration": {</span>
<span class="sd">                        "numberOfResults": 4,</span>
<span class="sd">                        "overrideSearchType": "SEMANTIC",</span>
<span class="sd">                        "filter": {</span>
<span class="sd">                            "equals": {</span>
<span class="sd">                                "key": "tag",</span>
<span class="sd">                                "value": "space"</span>
<span class="sd">                            }</span>
<span class="sd">                        }</span>
<span class="sd">                    }</span>
<span class="sd">                },</span>
<span class="sd">            )</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">knowledge_base_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">retrieval_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">profile_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_session_token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">get_aws_service_client</span><span class="p">(</span>
            <span class="n">service_name</span><span class="o">=</span><span class="s2">"bedrock-agent-runtime"</span><span class="p">,</span>
            <span class="n">profile_name</span><span class="o">=</span><span class="n">profile_name</span><span class="p">,</span>
            <span class="n">region_name</span><span class="o">=</span><span class="n">region_name</span><span class="p">,</span>
            <span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key_id</span><span class="p">,</span>
            <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_access_key</span><span class="p">,</span>
            <span class="n">aws_session_token</span><span class="o">=</span><span class="n">aws_session_token</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">knowledge_base_id</span> <span class="o">=</span> <span class="n">knowledge_base_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">retrieval_config</span> <span class="o">=</span> <span class="n">retrieval_config</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">callback_manager</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span>
            <span class="n">retrievalQuery</span><span class="o">=</span><span class="p">{</span><span class="s2">"text"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">strip</span><span class="p">()},</span>
            <span class="n">knowledgeBaseId</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">knowledge_base_id</span><span class="p">,</span>
            <span class="n">retrievalConfiguration</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">retrieval_config</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s2">"retrievalResults"</span><span class="p">]</span>
        <span class="n">node_with_score</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="s2">"location"</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"location"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"location"</span><span class="p">]</span>
            <span class="k">if</span> <span class="s2">"metadata"</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"sourceMetadata"</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">]</span>
            <span class="n">node_with_score</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">NodeWithScore</span><span class="p">(</span>
                    <span class="n">node</span><span class="o">=</span><span class="n">TextNode</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"content"</span><span class="p">][</span><span class="s2">"text"</span><span class="p">],</span>
                        <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">score</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="s2">"score"</span><span class="p">]</span> <span class="k">if</span> <span class="s2">"score"</span> <span class="ow">in</span> <span class="n">result</span> <span class="k">else</span> <span class="mi">0</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">node_with_score</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Auto merging](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/)[Next Bm25](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/)
