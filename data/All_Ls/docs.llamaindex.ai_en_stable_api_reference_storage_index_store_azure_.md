Title: Azure - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/

Markdown Content:
Azure - LlamaIndex


AzureIndexStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVIndexStore`

Azure Table Index store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `azure_kvstore` | `[AzureKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore "llama_index.storage.kvstore.azure.AzureKVStore")` | 
Azure key-value store



 | _required_ |
| `namespace` | `str` | 

namespace for the index store



 | `None` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-azure/llama_index/storage/index_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  8</span>
<span class="normal">  9</span>
<span class="normal"> 10</span>
<span class="normal"> 11</span>
<span class="normal"> 12</span>
<span class="normal"> 13</span>
<span class="normal"> 14</span>
<span class="normal"> 15</span>
<span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureIndexStore</span><span class="p">(</span><span class="n">KVIndexStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure Table Index store.</span>

<span class="sd">    Args:</span>
<span class="sd">        azure_kvstore (AzureKVStore): Azure key-value store</span>
<span class="sd">        namespace (str): namespace for the index store</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">azure_kvstore</span><span class="p">:</span> <span class="n">AzureKVStore</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a MongoIndexStore."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load an AzureIndexStore from an Azure connection string.</span>

<span class="sd">        Args:</span>
<span class="sd">            connection_string (str): Azure connection string</span>
<span class="sd">            namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">            service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">        """</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
            <span class="n">connection_string</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load an AzureIndexStore from an account name and key.</span>

<span class="sd">        Args:</span>
<span class="sd">            account_name (str): Azure Storage Account Name</span>
<span class="sd">            account_key (str): Azure Storage Account Key</span>
<span class="sd">            namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">            service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">        """</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_account_and_key</span><span class="p">(</span>
            <span class="n">account_name</span><span class="p">,</span> <span class="n">account_key</span><span class="p">,</span> <span class="n">endpoint</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load an AzureIndexStore from a SAS token.</span>

<span class="sd">        Args:</span>
<span class="sd">            endpoint (str): Azure Table service endpoint</span>
<span class="sd">            sas_token (str): Shared Access Signature token</span>
<span class="sd">            namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">            service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">        """</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_sas_token</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span> <span class="n">sas_token</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
        <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load an AzureIndexStore from an AAD token.</span>

<span class="sd">        Args:</span>
<span class="sd">            endpoint (str): Azure Table service endpoint</span>
<span class="sd">            namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">            service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">        """</span>
        <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_aad_token</span><span class="p">(</span>
            <span class="n">endpoint</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_connection\_string `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore.from_connection_string "Permanent link")

```
from_connection_string(connection_string: str, namespace: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None) -> [AzureIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore "llama_index.storage.index_store.azure.base.AzureIndexStore")
```

Load an AzureIndexStore from an Azure connection string.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `connection_string` | `str` | 
Azure connection string



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace for the AzureIndexStore



 | `None` |
| `service_mode` | `ServiceMode` | 

CosmosDB or Azure Table service mode



 | `STORAGE` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-azure/llama_index/storage/index_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">24</span>
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
<span class="normal">42</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_connection_string</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load an AzureIndexStore from an Azure connection string.</span>

<span class="sd">    Args:</span>
<span class="sd">        connection_string (str): Azure connection string</span>
<span class="sd">        namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">        service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">    """</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
        <span class="n">connection_string</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_account\_and\_key `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore.from_account_and_key "Permanent link")

```
from_account_and_key(account_name: str, account_key: str, namespace: Optional[str] = None, endpoint: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None) -> [AzureIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore "llama_index.storage.index_store.azure.base.AzureIndexStore")
```

Load an AzureIndexStore from an account name and key.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `account_name` | `str` | 
Azure Storage Account Name



 | _required_ |
| `account_key` | `str` | 

Azure Storage Account Key



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace for the AzureIndexStore



 | `None` |
| `service_mode` | `ServiceMode` | 

CosmosDB or Azure Table service mode



 | `STORAGE` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-azure/llama_index/storage/index_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">44</span>
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
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_account_and_key</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">account_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">account_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load an AzureIndexStore from an account name and key.</span>

<span class="sd">    Args:</span>
<span class="sd">        account_name (str): Azure Storage Account Name</span>
<span class="sd">        account_key (str): Azure Storage Account Key</span>
<span class="sd">        namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">        service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">    """</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_account_and_key</span><span class="p">(</span>
        <span class="n">account_name</span><span class="p">,</span> <span class="n">account_key</span><span class="p">,</span> <span class="n">endpoint</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_sas\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore.from_sas_token "Permanent link")

```
from_sas_token(endpoint: str, sas_token: str, namespace: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None) -> [AzureIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore "llama_index.storage.index_store.azure.base.AzureIndexStore")
```

Load an AzureIndexStore from a SAS token.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `endpoint` | `str` | 
Azure Table service endpoint



 | _required_ |
| `sas_token` | `str` | 

Shared Access Signature token



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace for the AzureIndexStore



 | `None` |
| `service_mode` | `ServiceMode` | 

CosmosDB or Azure Table service mode



 | `STORAGE` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-azure/llama_index/storage/index_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">67</span>
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
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_sas_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">sas_token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load an AzureIndexStore from a SAS token.</span>

<span class="sd">    Args:</span>
<span class="sd">        endpoint (str): Azure Table service endpoint</span>
<span class="sd">        sas_token (str): Shared Access Signature token</span>
<span class="sd">        namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">        service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">    """</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_sas_token</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span> <span class="n">sas_token</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_aad\_token `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore.from_aad_token "Permanent link")

```
from_aad_token(endpoint: str, namespace: Optional[str] = None, service_mode: ServiceMode = ServiceMode.STORAGE, partition_key: Optional[str] = None) -> [AzureIndexStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/#llama_index.storage.index_store.azure.AzureIndexStore "llama_index.storage.index_store.azure.base.AzureIndexStore")
```

Load an AzureIndexStore from an AAD token.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `endpoint` | `str` | 
Azure Table service endpoint



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace for the AzureIndexStore



 | `None` |
| `service_mode` | `ServiceMode` | 

CosmosDB or Azure Table service mode



 | `STORAGE` |

Source code in `llama-index-integrations/storage/index_store/llama-index-storage-index-store-azure/llama_index/storage/index_store/azure/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 89</span>
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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_aad_token</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_mode</span><span class="p">:</span> <span class="n">ServiceMode</span> <span class="o">=</span> <span class="n">ServiceMode</span><span class="o">.</span><span class="n">STORAGE</span><span class="p">,</span>
    <span class="n">partition_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"AzureIndexStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load an AzureIndexStore from an AAD token.</span>

<span class="sd">    Args:</span>
<span class="sd">        endpoint (str): Azure Table service endpoint</span>
<span class="sd">        namespace (Optional[str]): namespace for the AzureIndexStore</span>
<span class="sd">        service_mode (ServiceMode): CosmosDB or Azure Table service mode</span>
<span class="sd">    """</span>
    <span class="n">azure_kvstore</span> <span class="o">=</span> <span class="n">AzureKVStore</span><span class="o">.</span><span class="n">from_aad_token</span><span class="p">(</span>
        <span class="n">endpoint</span><span class="p">,</span> <span class="n">service_mode</span><span class="p">,</span> <span class="n">partition_key</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">azure_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tidb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/tidb/)[Next Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/)
