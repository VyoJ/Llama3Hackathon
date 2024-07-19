Title: Azstorage blob - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/

Markdown Content:
Azstorage blob - LlamaIndex


AzStorageBlobReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/#llama_index.readers.azstorage_blob.AzStorageBlobReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BasePydanticReader "llama_index.core.readers.base.BasePydanticReader")`, `ResourcesReaderMixin`, `FileSystemReaderMixin`

General reader for any Azure Storage Blob file or directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `container_name` | `str` | 
name of the container for the blob.



 | _required_ |
| `blob` | `Optional[str]` | 

name of the file to download. If none specified this loader will iterate through list of blobs in the container.



 | _required_ |
| `name_starts_with` | `Optional[str]` | 

filter the list of blobs to download to only those whose names begin with the specified string.



 | _required_ |
| `include` |  | 

(Union\[str, List\[str\], None\]): Specifies one or more additional datasets to include in the response. Options include: 'snapshots', 'metadata', 'uncommittedblobs', 'copy', 'deleted', 'deletedwithversions', 'tags', 'versions', 'immutabilitypolicy', 'legalhold'.



 | _required_ |
| `file_extractor` | `Optional[Dict[str, Union[str, [BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")]]]` | 

A mapping of file extension to a BaseReader class that specifies how to convert that file to text. See `SimpleDirectoryReader` for more details, or call this path `llama_index.readers.file.base.DEFAULT_FILE_READER_CLS`.



 | _required_ |
| `connection_string` | `str` | 

A connection string which can be found under a storage account's "Access keys" security tab. This parameter



 | _required_ |
| `account_url` | `str` | 

URI to the storage account, may include SAS token.



 | _required_ |
| `credential` | `Union[str, Dict[str, str], AzureNamedKeyCredential, AzureSasCredential, TokenCredential, None] = None` | 

The credentials with which to authenticate. This is optional if the account URL already has a SAS token.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-azstorage-blob/llama_index/readers/azstorage_blob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 31</span>
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
<span class="normal">232</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzStorageBlobReader</span><span class="p">(</span>
    <span class="n">BasePydanticReader</span><span class="p">,</span> <span class="n">ResourcesReaderMixin</span><span class="p">,</span> <span class="n">FileSystemReaderMixin</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    General reader for any Azure Storage Blob file or directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        container_name (str): name of the container for the blob.</span>
<span class="sd">        blob (Optional[str]): name of the file to download. If none specified</span>
<span class="sd">            this loader will iterate through list of blobs in the container.</span>
<span class="sd">        name_starts_with (Optional[str]): filter the list of blobs to download</span>
<span class="sd">            to only those whose names begin with the specified string.</span>
<span class="sd">        include: (Union[str, List[str], None]): Specifies one or more additional</span>
<span class="sd">            datasets to include in the response. Options include: 'snapshots',</span>
<span class="sd">            'metadata', 'uncommittedblobs', 'copy', 'deleted',</span>
<span class="sd">            'deletedwithversions', 'tags', 'versions', 'immutabilitypolicy',</span>
<span class="sd">            'legalhold'.</span>
<span class="sd">        file_extractor (Optional[Dict[str, Union[str, BaseReader]]]): A mapping of file</span>
<span class="sd">            extension to a BaseReader class that specifies how to convert that file</span>
<span class="sd">            to text. See `SimpleDirectoryReader` for more details, or call this path ```llama_index.readers.file.base.DEFAULT_FILE_READER_CLS```.</span>
<span class="sd">        connection_string (str): A connection string which can be found under a storage account's "Access keys" security tab. This parameter</span>
<span class="sd">        can be used in place of both the account URL and credential.</span>
<span class="sd">        account_url (str): URI to the storage account, may include SAS token.</span>
<span class="sd">        credential (Union[str, Dict[str, str], AzureNamedKeyCredential, AzureSasCredential, TokenCredential, None] = None):</span>
<span class="sd">            The credentials with which to authenticate. This is optional if the account URL already has a SAS token.</span>
<span class="sd">    """</span>

    <span class="n">container_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">prefix</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="n">blob</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">name_starts_with</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">include</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">file_extractor</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseReader</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">exclude</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>
    <span class="n">connection_string</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">account_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">credential</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">is_remote</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="c1"># Not in use. As part of the TODO below. Is part of the kwargs.</span>
    <span class="c1"># self.preloaded_data_path = kwargs.get('preloaded_data_path', None)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"AzStorageBlobReader"</span>

    <span class="k">def</span> <span class="nf">_get_container_client</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_string</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ContainerClient</span><span class="o">.</span><span class="n">from_connection_string</span><span class="p">(</span>
                <span class="n">conn_str</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">connection_string</span><span class="p">,</span>
                <span class="n">container_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">container_name</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">ContainerClient</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">account_url</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">container_name</span><span class="p">,</span> <span class="n">credential</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">credential</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_download_files_and_extract_metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Download files from Azure Storage Blob and extract metadata."""</span>
        <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
        <span class="n">blob_meta</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">blob</span><span class="p">:</span>
            <span class="n">blobs_list</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">blob</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">blobs_list</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">list_blobs</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">name_starts_with</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">include</span>
            <span class="p">)</span>

        <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">blobs_list</span><span class="p">:</span>
            <span class="n">sanitized_file_name</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"/"</span><span class="p">,</span> <span class="s2">"-"</span><span class="p">)</span> <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">blob</span> <span class="k">else</span> <span class="n">obj</span>
            <span class="n">download_file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">,</span> <span class="n">sanitized_file_name</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Start download of </span><span class="si">{</span><span class="n">sanitized_file_name</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
            <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
            <span class="n">stream</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">download_blob</span><span class="p">()</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="o">=</span><span class="n">download_file_path</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">download_file</span><span class="p">:</span>
                <span class="n">stream</span><span class="o">.</span><span class="n">readinto</span><span class="p">(</span><span class="n">download_file</span><span class="p">)</span>
            <span class="n">blob_meta</span><span class="p">[</span><span class="n">sanitized_file_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">get_blob_properties</span><span class="p">()</span>
            <span class="n">end_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">sanitized_file_name</span><span class="si">}</span><span class="s2"> downloaded in </span><span class="si">{</span><span class="n">end_time</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">start_time</span><span class="si">}</span><span class="s2"> seconds."</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">blob_meta</span>

    <span class="k">def</span> <span class="nf">_extract_blob_metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="n">meta</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">file_metadata</span>

        <span class="n">creation_time</span> <span class="o">=</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"creation_time"</span><span class="p">)</span>
        <span class="n">creation_time</span> <span class="o">=</span> <span class="n">creation_time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span> <span class="k">if</span> <span class="n">creation_time</span> <span class="k">else</span> <span class="kc">None</span>

        <span class="n">last_modified</span> <span class="o">=</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"last_modified"</span><span class="p">)</span>
        <span class="n">last_modified</span> <span class="o">=</span> <span class="n">last_modified</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span> <span class="k">if</span> <span class="n">last_modified</span> <span class="k">else</span> <span class="kc">None</span>

        <span class="n">last_accessed_on</span> <span class="o">=</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"last_accessed_on"</span><span class="p">)</span>
        <span class="n">last_accessed_on</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">last_accessed_on</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span> <span class="k">if</span> <span class="n">last_accessed_on</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="p">)</span>

        <span class="n">extracted_meta</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"name"</span><span class="p">),</span>
            <span class="s2">"file_type"</span><span class="p">:</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content_settings"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"content_type"</span><span class="p">),</span>
            <span class="s2">"file_size"</span><span class="p">:</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"size"</span><span class="p">),</span>
            <span class="s2">"creation_date"</span><span class="p">:</span> <span class="n">creation_time</span><span class="p">,</span>
            <span class="s2">"last_modified_date"</span><span class="p">:</span> <span class="n">last_modified</span><span class="p">,</span>
            <span class="s2">"last_accessed_date"</span><span class="p">:</span> <span class="n">last_accessed_on</span><span class="p">,</span>
            <span class="s2">"container"</span><span class="p">:</span> <span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"container"</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="n">extracted_meta</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{})</span>
        <span class="n">extracted_meta</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">meta</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"tags"</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{})</span>

        <span class="k">return</span> <span class="n">extracted_meta</span>

    <span class="k">def</span> <span class="nf">_load_documents_with_metadata</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">files_metadata</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">temp_dir</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load documents from a directory and extract metadata."""</span>

        <span class="k">def</span> <span class="nf">get_metadata</span><span class="p">(</span><span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
            <span class="k">return</span> <span class="n">files_metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="p">{})</span>

        <span class="n">loader</span> <span class="o">=</span> <span class="n">SimpleDirectoryReader</span><span class="p">(</span>
            <span class="n">temp_dir</span><span class="p">,</span> <span class="n">file_extractor</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">file_extractor</span><span class="p">,</span> <span class="n">file_metadata</span><span class="o">=</span><span class="n">get_metadata</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">loader</span><span class="o">.</span><span class="n">load_data</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""List all the blobs in the container."""</span>
        <span class="n">blobs_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span><span class="o">.</span><span class="n">list_blobs</span><span class="p">(</span>
            <span class="n">name_starts_with</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name_starts_with</span><span class="p">,</span> <span class="n">include</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">blob</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">blob</span> <span class="ow">in</span> <span class="n">blobs_list</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_resource_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get metadata for a specific blob."""</span>
        <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
        <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span>
        <span class="n">blob_meta</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">get_blob_properties</span><span class="p">()</span>

        <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_extract_blob_metadata</span><span class="p">(</span><span class="n">blob_meta</span><span class="p">),</span>
            <span class="s2">"file_path"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">":"</span><span class="p">,</span> <span class="s2">"/"</span><span class="p">),</span>
        <span class="p">}</span>

        <span class="k">return</span> <span class="p">{</span>
            <span class="n">meta_key</span><span class="p">:</span> <span class="n">meta_value</span>
            <span class="k">for</span> <span class="n">meta_key</span><span class="p">,</span> <span class="n">meta_value</span> <span class="ow">in</span> <span class="n">info_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">meta_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_resource</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
            <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span>
            <span class="n">stream</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">download_blob</span><span class="p">()</span>
            <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
                <span class="n">download_file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="n">temp_dir</span><span class="p">,</span> <span class="n">resource_id</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"/"</span><span class="p">,</span> <span class="s2">"-"</span><span class="p">)</span>
                <span class="p">)</span>
                <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="o">=</span><span class="n">download_file_path</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">download_file</span><span class="p">:</span>
                    <span class="n">stream</span><span class="o">.</span><span class="n">readinto</span><span class="p">(</span><span class="n">download_file</span><span class="p">)</span>
                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span>
                    <span class="p">{</span><span class="n">resource_id</span><span class="p">:</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">get_blob_properties</span><span class="p">()},</span> <span class="n">temp_dir</span>
                <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Error loading resource </span><span class="si">{</span><span class="n">resource_id</span><span class="si">}</span><span class="s2"> from AzStorageBlob: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Read the content of a file from Azure Storage Blob."""</span>
        <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
        <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>
        <span class="n">stream</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">download_blob</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">stream</span><span class="o">.</span><span class="n">readall</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load file(s) from Azure Storage Blob."""</span>
        <span class="n">total_download_start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

        <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
            <span class="n">files_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_files_and_extract_metadata</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">)</span>

            <span class="n">total_download_end_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

            <span class="n">total_elapsed_time</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">ceil</span><span class="p">(</span>
                <span class="n">total_download_end_time</span> <span class="o">-</span> <span class="n">total_download_start_time</span>
            <span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Downloading completed in approximately </span><span class="si">{</span><span class="n">total_elapsed_time</span><span class="w"> </span><span class="o">//</span><span class="w"> </span><span class="mi">60</span><span class="si">}</span><span class="s2">min"</span>
                <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">total_elapsed_time</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">60</span><span class="si">}</span><span class="s2">s."</span>
            <span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Document creation starting"</span><span class="p">)</span>

            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span><span class="n">files_metadata</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### list\_resources [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/#llama_index.readers.azstorage_blob.AzStorageBlobReader.list_resources "Permanent link")

```
list_resources(*args: Any, **kwargs: Any) -> List[str]
```

List all the blobs in the container.

Source code in `llama-index-integrations/readers/llama-index-readers-azstorage-blob/llama_index/readers/azstorage_blob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">list_resources</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""List all the blobs in the container."""</span>
    <span class="n">blobs_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span><span class="o">.</span><span class="n">list_blobs</span><span class="p">(</span>
        <span class="n">name_starts_with</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name_starts_with</span><span class="p">,</span> <span class="n">include</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">blob</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">blob</span> <span class="ow">in</span> <span class="n">blobs_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_resource\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/#llama_index.readers.azstorage_blob.AzStorageBlobReader.get_resource_info "Permanent link")

```
get_resource_info(resource_id: str, **kwargs: Any) -> Dict
```

Get metadata for a specific blob.

Source code in `llama-index-integrations/readers/llama-index-readers-azstorage-blob/llama_index/readers/azstorage_blob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">168</span>
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
<span class="normal">183</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_resource_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resource_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get metadata for a specific blob."""</span>
    <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
    <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span>
    <span class="n">blob_meta</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">get_blob_properties</span><span class="p">()</span>

    <span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_extract_blob_metadata</span><span class="p">(</span><span class="n">blob_meta</span><span class="p">),</span>
        <span class="s2">"file_path"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">resource_id</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">":"</span><span class="p">,</span> <span class="s2">"/"</span><span class="p">),</span>
    <span class="p">}</span>

    <span class="k">return</span> <span class="p">{</span>
        <span class="n">meta_key</span><span class="p">:</span> <span class="n">meta_value</span>
        <span class="k">for</span> <span class="n">meta_key</span><span class="p">,</span> <span class="n">meta_value</span> <span class="ow">in</span> <span class="n">info_dict</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">meta_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### read\_file\_content [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/#llama_index.readers.azstorage_blob.AzStorageBlobReader.read_file_content "Permanent link")

```
read_file_content(input_file: Path, **kwargs) -> bytes
```

Read the content of a file from Azure Storage Blob.

Source code in `llama-index-integrations/readers/llama-index-readers-azstorage-blob/llama_index/readers/azstorage_blob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">read_file_content</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Read the content of a file from Azure Storage Blob."""</span>
    <span class="n">container_client</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_container_client</span><span class="p">()</span>
    <span class="n">blob_client</span> <span class="o">=</span> <span class="n">container_client</span><span class="o">.</span><span class="n">get_blob_client</span><span class="p">(</span><span class="n">input_file</span><span class="p">)</span>
    <span class="n">stream</span> <span class="o">=</span> <span class="n">blob_client</span><span class="o">.</span><span class="n">download_blob</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">stream</span><span class="o">.</span><span class="n">readall</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/#llama_index.readers.azstorage_blob.AzStorageBlobReader.load_data "Permanent link")

```
load_data() -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load file(s) from Azure Storage Blob.

Source code in `llama-index-integrations/readers/llama-index-readers-azstorage-blob/llama_index/readers/azstorage_blob/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">212</span>
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
<span class="normal">232</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load file(s) from Azure Storage Blob."""</span>
    <span class="n">total_download_start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

    <span class="k">with</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryDirectory</span><span class="p">()</span> <span class="k">as</span> <span class="n">temp_dir</span><span class="p">:</span>
        <span class="n">files_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_download_files_and_extract_metadata</span><span class="p">(</span><span class="n">temp_dir</span><span class="p">)</span>

        <span class="n">total_download_end_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

        <span class="n">total_elapsed_time</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">ceil</span><span class="p">(</span>
            <span class="n">total_download_end_time</span> <span class="o">-</span> <span class="n">total_download_start_time</span>
        <span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"Downloading completed in approximately </span><span class="si">{</span><span class="n">total_elapsed_time</span><span class="w"> </span><span class="o">//</span><span class="w"> </span><span class="mi">60</span><span class="si">}</span><span class="s2">min"</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">total_elapsed_time</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">60</span><span class="si">}</span><span class="s2">s."</span>
        <span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">"Document creation starting"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_load_documents_with_metadata</span><span class="p">(</span><span class="n">files_metadata</span><span class="p">,</span> <span class="n">temp_dir</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azcognitive search](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/)[Next Azure devops](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/)
