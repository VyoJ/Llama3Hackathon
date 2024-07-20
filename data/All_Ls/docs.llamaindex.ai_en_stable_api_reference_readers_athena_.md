Title: Athena - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/

Markdown Content:
Athena - LlamaIndex


AthenaReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/#llama_index.readers.athena.AthenaReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Athena reader.

Follow AWS best practices for security. AWS discourages hardcoding credentials in code. We recommend that you use IAM roles instead of IAM user credentials. If you must use credentials, do not embed them in your code. Instead, store them in environment variables or in a separate configuration file.

Source code in `llama-index-integrations/readers/llama-index-readers-athena/llama_index/readers/athena/base.py`

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
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AthenaReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Athena reader.</span>

<span class="sd">    Follow AWS best practices for security.</span>
<span class="sd">    AWS discourages hardcoding credentials in code.</span>
<span class="sd">    We recommend that you use IAM roles instead of IAM user credentials.</span>
<span class="sd">    If you must use credentials, do not embed them in your code.</span>
<span class="sd">    Instead, store them in environment variables or in a separate configuration file.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>

    <span class="k">def</span> <span class="nf">create_athena_engine</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">aws_access_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_secret_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_region</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">s3_staging_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">workgroup</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Args:</span>
<span class="sd">        aws_access_key is the AWS access key from aws credential</span>
<span class="sd">        aws_secret_key is the AWS secret key from aws credential</span>
<span class="sd">        aws_region is the AWS region</span>
<span class="sd">        s3_staging_dir is the S3 staging (result bucket) directory</span>
<span class="sd">        database is the Athena database name</span>
<span class="sd">        workgroup is the Athena workgroup name.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">aws_access_key</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">aws_secret_key</span><span class="p">:</span>
            <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
                <span class="s2">"awsathena+rest://:@athena.</span><span class="si">{region_name}</span><span class="s2">.amazonaws.com:443/"</span>
                <span class="s2">"</span><span class="si">{database}</span><span class="s2">?s3_staging_dir=</span><span class="si">{s3_staging_dir}</span><span class="s2">?work_group=</span><span class="si">{workgroup}</span><span class="s2">"</span>
            <span class="p">)</span>

            <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span>
                <span class="n">conn_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                    <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
                    <span class="n">s3_staging_dir</span><span class="o">=</span><span class="n">s3_staging_dir</span><span class="p">,</span>
                    <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
                    <span class="n">workgroup</span><span class="o">=</span><span class="n">workgroup</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
                <span class="s2">"aws_access_key and aws_secret_key are set. We recommend to use IAM role instead."</span>
            <span class="p">)</span>
            <span class="n">boto3</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>
                <span class="s2">"athena"</span><span class="p">,</span>
                <span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key</span><span class="p">,</span>
                <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_key</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
                <span class="s2">"awsathena+rest://:@athena.</span><span class="si">{region_name}</span><span class="s2">.amazonaws.com:443/"</span>
                <span class="s2">"</span><span class="si">{database}</span><span class="s2">?s3_staging_dir=</span><span class="si">{s3_staging_dir}</span><span class="s2">?work_group=</span><span class="si">{workgroup}</span><span class="s2">"</span>
            <span class="p">)</span>

            <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span>
                <span class="n">conn_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                    <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
                    <span class="n">s3_staging_dir</span><span class="o">=</span><span class="n">s3_staging_dir</span><span class="p">,</span>
                    <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
                    <span class="n">workgroup</span><span class="o">=</span><span class="n">workgroup</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">engine</span>
</code></pre></div></td></tr></tbody></table>

### create\_athena\_engine [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/#llama_index.readers.athena.AthenaReader.create_athena_engine "Permanent link")

```
create_athena_engine(aws_access_key: Optional[str] = None, aws_secret_key: Optional[str] = None, aws_region: str = None, s3_staging_dir: str = None, database: str = None, workgroup: str = None)
```

Args: aws\_access\_key is the AWS access key from aws credential aws\_secret\_key is the AWS secret key from aws credential aws\_region is the AWS region s3\_staging\_dir is the S3 staging (result bucket) directory database is the Athena database name workgroup is the Athena workgroup name.

Source code in `llama-index-integrations/readers/llama-index-readers-athena/llama_index/readers/athena/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">26</span>
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
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_athena_engine</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">aws_access_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_secret_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_region</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">s3_staging_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">workgroup</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Args:</span>
<span class="sd">    aws_access_key is the AWS access key from aws credential</span>
<span class="sd">    aws_secret_key is the AWS secret key from aws credential</span>
<span class="sd">    aws_region is the AWS region</span>
<span class="sd">    s3_staging_dir is the S3 staging (result bucket) directory</span>
<span class="sd">    database is the Athena database name</span>
<span class="sd">    workgroup is the Athena workgroup name.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">aws_access_key</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">aws_secret_key</span><span class="p">:</span>
        <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"awsathena+rest://:@athena.</span><span class="si">{region_name}</span><span class="s2">.amazonaws.com:443/"</span>
            <span class="s2">"</span><span class="si">{database}</span><span class="s2">?s3_staging_dir=</span><span class="si">{s3_staging_dir}</span><span class="s2">?work_group=</span><span class="si">{workgroup}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span>
            <span class="n">conn_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
                <span class="n">s3_staging_dir</span><span class="o">=</span><span class="n">s3_staging_dir</span><span class="p">,</span>
                <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
                <span class="n">workgroup</span><span class="o">=</span><span class="n">workgroup</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
            <span class="s2">"aws_access_key and aws_secret_key are set. We recommend to use IAM role instead."</span>
        <span class="p">)</span>
        <span class="n">boto3</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>
            <span class="s2">"athena"</span><span class="p">,</span>
            <span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key</span><span class="p">,</span>
            <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_key</span><span class="p">,</span>
            <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">conn_str</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"awsathena+rest://:@athena.</span><span class="si">{region_name}</span><span class="s2">.amazonaws.com:443/"</span>
            <span class="s2">"</span><span class="si">{database}</span><span class="s2">?s3_staging_dir=</span><span class="si">{s3_staging_dir}</span><span class="s2">?work_group=</span><span class="si">{workgroup}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">engine</span> <span class="o">=</span> <span class="n">create_engine</span><span class="p">(</span>
            <span class="n">conn_str</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">region_name</span><span class="o">=</span><span class="n">aws_region</span><span class="p">,</span>
                <span class="n">s3_staging_dir</span><span class="o">=</span><span class="n">s3_staging_dir</span><span class="p">,</span>
                <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
                <span class="n">workgroup</span><span class="o">=</span><span class="n">workgroup</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">engine</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Astra db](https://docs.llamaindex.ai/en/stable/api_reference/readers/astra_db/)[Next Awadb](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/)
