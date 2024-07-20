Title: Dynamodb - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/

Markdown Content:
Dynamodb - LlamaIndex


DynamoDBKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

DynamoDB Key-Value store. Stores key-value pairs in a DynamoDB Table. The DynamoDB Table must have both a hash key and a range key, and their types must be string.

You can specify a custom URL for DynamoDB by setting the `DYNAMODB_URL` environment variable. This is useful if you're using a local instance of DynamoDB for development or testing. If `DYNAMODB_URL` is not set, the application will use the default AWS DynamoDB service.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `table` | `Any` | 
DynamoDB Table Service Resource



 | _required_ |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
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
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DynamoDBKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DynamoDB Key-Value store.</span>
<span class="sd">    Stores key-value pairs in a DynamoDB Table.</span>
<span class="sd">    The DynamoDB Table must have both a hash key and a range key,</span>
<span class="sd">        and their types must be string.</span>

<span class="sd">    You can specify a custom URL for DynamoDB by setting the `DYNAMODB_URL`</span>
<span class="sd">    environment variable. This is useful if you're using a local instance of</span>
<span class="sd">    DynamoDB for development or testing. If `DYNAMODB_URL` is not set, the</span>
<span class="sd">    application will use the default AWS DynamoDB service.</span>

<span class="sd">    Args:</span>
<span class="sd">        table (Any): DynamoDB Table Service Resource</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init a DynamoDBKVStore."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table</span> <span class="o">=</span> <span class="n">table</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_boto3_key</span> <span class="o">=</span> <span class="n">Key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span> <span class="o">=</span> <span class="n">parse_schema</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBKVStore</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a DynamoDBKVStore from a DynamoDB table name.</span>

<span class="sd">        Args:</span>
<span class="sd">            table_name (str): DynamoDB table name</span>
<span class="sd">        """</span>
        <span class="c1"># Get the DynamoDB URL from environment variable</span>
        <span class="n">dynamodb_url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DYNAMODB_URL"</span><span class="p">)</span>

        <span class="c1"># Create a session</span>
        <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>

        <span class="c1"># If the DynamoDB URL is set, use it as the endpoint URL</span>
        <span class="k">if</span> <span class="n">dynamodb_url</span><span class="p">:</span>
            <span class="n">ddb</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">resource</span><span class="p">(</span><span class="s2">"dynamodb"</span><span class="p">,</span> <span class="n">endpoint_url</span><span class="o">=</span><span class="n">dynamodb_url</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Otherwise, let boto3 use its default configuration</span>
            <span class="n">ddb</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">resource</span><span class="p">(</span><span class="s2">"dynamodb"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">table</span><span class="o">=</span><span class="n">ddb</span><span class="o">.</span><span class="n">Table</span><span class="p">(</span><span class="n">table_name</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">item</span> <span class="o">=</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">convert_float_to_decimal</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">val</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
        <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">]</span> <span class="o">=</span> <span class="n">collection</span>
        <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">]</span> <span class="o">=</span> <span class="n">key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">put_item</span><span class="p">(</span><span class="n">Item</span><span class="o">=</span><span class="n">item</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            val (dict): value</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">get_item</span><span class="p">(</span>
            <span class="n">Key</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">:</span> <span class="n">key</span><span class="p">}</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">item</span> <span class="o">:=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Item"</span><span class="p">))</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="n">k</span><span class="p">:</span> <span class="n">convert_decimal_to_int_or_float</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">item</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">k</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">}</span>
            <span class="p">}</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">result</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">last_evaluated_key</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">is_first</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="k">while</span> <span class="n">last_evaluated_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">is_first</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
                <span class="n">is_first</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="n">option</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"KeyConditionExpression"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_boto3_key</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">)</span><span class="o">.</span><span class="n">eq</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="n">last_evaluated_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">option</span><span class="p">[</span><span class="s2">"ExclusiveStartKey"</span><span class="p">]</span> <span class="o">=</span> <span class="n">last_evaluated_key</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">**</span><span class="n">option</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Items"</span><span class="p">,</span> <span class="p">[]):</span>
                <span class="n">item</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">)</span>
                <span class="n">key</span> <span class="o">=</span> <span class="n">item</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">)</span>
                <span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="n">k</span><span class="p">:</span> <span class="n">convert_decimal_to_int_or_float</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">item</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="p">}</span>
            <span class="n">last_evaluated_key</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"LastEvaluatedKey"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">delete_item</span><span class="p">(</span>
            <span class="n">Key</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">:</span> <span class="n">key</span><span class="p">},</span>
            <span class="n">ReturnValues</span><span class="o">=</span><span class="s2">"ALL_OLD"</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="p">(</span><span class="n">item</span> <span class="o">:=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Attributes"</span><span class="p">))</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">        Args:</span>
<span class="sd">            key (str): key</span>
<span class="sd">            collection (str): collection name</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### from\_table\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.from_table_name "Permanent link")

```
from_table_name(table_name: str) -> [DynamoDBKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore "llama_index.storage.kvstore.dynamodb.base.DynamoDBKVStore")
```

Load a DynamoDBKVStore from a DynamoDB table name.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `table_name` | `str` | 
DynamoDB table name



 | _required_ |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">75</span>
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
<span class="normal">94</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_table_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">table_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">DynamoDBKVStore</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a DynamoDBKVStore from a DynamoDB table name.</span>

<span class="sd">    Args:</span>
<span class="sd">        table_name (str): DynamoDB table name</span>
<span class="sd">    """</span>
    <span class="c1"># Get the DynamoDB URL from environment variable</span>
    <span class="n">dynamodb_url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s2">"DYNAMODB_URL"</span><span class="p">)</span>

    <span class="c1"># Create a session</span>
    <span class="n">session</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span>

    <span class="c1"># If the DynamoDB URL is set, use it as the endpoint URL</span>
    <span class="k">if</span> <span class="n">dynamodb_url</span><span class="p">:</span>
        <span class="n">ddb</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">resource</span><span class="p">(</span><span class="s2">"dynamodb"</span><span class="p">,</span> <span class="n">endpoint_url</span><span class="o">=</span><span class="n">dynamodb_url</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># Otherwise, let boto3 use its default configuration</span>
        <span class="n">ddb</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">resource</span><span class="p">(</span><span class="s2">"dynamodb"</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">table</span><span class="o">=</span><span class="n">ddb</span><span class="o">.</span><span class="n">Table</span><span class="p">(</span><span class="n">table_name</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.put "Permanent link")

```
put(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 96</span>
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
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">item</span> <span class="o">=</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">convert_float_to_decimal</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">val</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
    <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">]</span> <span class="o">=</span> <span class="n">collection</span>
    <span class="n">item</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">]</span> <span class="o">=</span> <span class="n">key</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">put_item</span><span class="p">(</span><span class="n">Item</span><span class="o">=</span><span class="n">item</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.aput "Permanent link")

```
aput(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `val` | `dict` | 

value



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        val (dict): value</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.get "Permanent link")

```
get(key: str, collection: str = DEFAULT_COLLECTION) -> dict | None
```

Get a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">121</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">get_item</span><span class="p">(</span>
        <span class="n">Key</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">:</span> <span class="n">key</span><span class="p">}</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">item</span> <span class="o">:=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Item"</span><span class="p">))</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">k</span><span class="p">:</span> <span class="n">convert_decimal_to_int_or_float</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">item</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">k</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">}</span>
        <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.aget "Permanent link")

```
aget(key: str, collection: str = DEFAULT_COLLECTION) -> dict | None
```

Get a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.get_all "Permanent link")

```
get_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">149</span>
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
<span class="normal">174</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">last_evaluated_key</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">is_first</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="k">while</span> <span class="n">last_evaluated_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">is_first</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
            <span class="n">is_first</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="n">option</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"KeyConditionExpression"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_boto3_key</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">)</span><span class="o">.</span><span class="n">eq</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">last_evaluated_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">option</span><span class="p">[</span><span class="s2">"ExclusiveStartKey"</span><span class="p">]</span> <span class="o">=</span> <span class="n">last_evaluated_key</span>
        <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">**</span><span class="n">option</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Items"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="n">item</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">)</span>
            <span class="n">key</span> <span class="o">=</span> <span class="n">item</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">)</span>
            <span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
                <span class="n">k</span><span class="p">:</span> <span class="n">convert_decimal_to_int_or_float</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">item</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="p">}</span>
        <span class="n">last_evaluated_key</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"LastEvaluatedKey"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">result</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.aget_all "Permanent link")

```
aget_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection` | `str` | 
collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.delete "Permanent link")

```
delete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">184</span>
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
<span class="normal">199</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table</span><span class="o">.</span><span class="n">delete_item</span><span class="p">(</span>
        <span class="n">Key</span><span class="o">=</span><span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_key_hash</span><span class="p">:</span> <span class="n">collection</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_key_range</span><span class="p">:</span> <span class="n">key</span><span class="p">},</span>
        <span class="n">ReturnValues</span><span class="o">=</span><span class="s2">"ALL_OLD"</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="k">if</span> <span class="p">(</span><span class="n">item</span> <span class="o">:=</span> <span class="n">resp</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Attributes"</span><span class="p">))</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/#llama_index.storage.kvstore.dynamodb.DynamoDBKVStore.adelete "Permanent link")

```
adelete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | 
key



 | _required_ |
| `collection` | `str` | 

collection name



 | `DEFAULT_COLLECTION` |

Source code in `llama-index-integrations/storage/kvstore/llama-index-storage-kvstore-dynamodb/llama_index/storage/kvstore/dynamodb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store.</span>

<span class="sd">    Args:</span>
<span class="sd">        key (str): key</span>
<span class="sd">        collection (str): collection name</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/)[Next Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/)
