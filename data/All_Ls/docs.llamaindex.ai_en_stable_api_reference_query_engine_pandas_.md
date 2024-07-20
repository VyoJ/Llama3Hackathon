Title: Pandas - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/

Markdown Content:
Pandas - LlamaIndex


PandasQueryEngine [#](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/#llama_index.experimental.query_engine.PandasQueryEngine "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseQueryEngine](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/#llama_index.core.base.base_query_engine.BaseQueryEngine "llama_index.core.base.base_query_engine.BaseQueryEngine")`

Pandas query engine.

Convert natural language to Pandas python code.

WARNING: This tool provides the Agent access to the `eval` function. Arbitrary code execution is possible on the machine running this tool. This tool is not recommended to be used in a production setting, and would require heavy sandboxing or virtual machines

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `df` | `DataFrame` | 
Pandas dataframe to use.



 | _required_ |
| `instruction_str` | `Optional[str]` | 

Instruction string to use.



 | `None` |
| `output_processor` | `Optional[Callable[[str], str]]` | 

Output processor. A callable that takes in the output string, pandas DataFrame, and any output kwargs and returns a string. eg.kwargs\["max\_colwidth"\] = \[int\] is used to set the length of text that each column can display during str(df). Set it to a higher number if there is possibly long text in the dataframe.



 | _required_ |
| `pandas_prompt` | `Optional[[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")]` | 

Pandas prompt to use.



 | `None` |
| `head` | `int` | 

Number of rows to show in the table context.



 | `5` |
| `llm` | `Optional[[LLM](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "llama_index.core.llms.llm.LLM")]` | 

Language model to use.



 | `None` |

**Examples:**

`pip install llama-index-experimental`

```
import pandas as pd
from llama_index.experimental.query_engine.pandas import PandasQueryEngine

df = pd.DataFrame(
    {
        "city": ["Toronto", "Tokyo", "Berlin"],
        "population": [2930000, 13960000, 3645000]
    }
)

query_engine = PandasQueryEngine(df=df, verbose=True)

response = query_engine.query("What is the population of Tokyo?")
```

Source code in `llama-index-experimental/llama_index/experimental/query_engine/pandas/pandas_query_engine.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 58</span>
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
<span class="normal">207</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasQueryEngine</span><span class="p">(</span><span class="n">BaseQueryEngine</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pandas query engine.</span>

<span class="sd">    Convert natural language to Pandas python code.</span>

<span class="sd">    WARNING: This tool provides the Agent access to the `eval` function.</span>
<span class="sd">    Arbitrary code execution is possible on the machine running this tool.</span>
<span class="sd">    This tool is not recommended to be used in a production setting, and would</span>
<span class="sd">    require heavy sandboxing or virtual machines</span>


<span class="sd">    Args:</span>
<span class="sd">        df (pd.DataFrame): Pandas dataframe to use.</span>
<span class="sd">        instruction_str (Optional[str]): Instruction string to use.</span>
<span class="sd">        output_processor (Optional[Callable[[str], str]]): Output processor.</span>
<span class="sd">            A callable that takes in the output string, pandas DataFrame,</span>
<span class="sd">            and any output kwargs and returns a string.</span>
<span class="sd">            eg.kwargs["max_colwidth"] = [int] is used to set the length of text</span>
<span class="sd">            that each column can display during str(df). Set it to a higher number</span>
<span class="sd">            if there is possibly long text in the dataframe.</span>
<span class="sd">        pandas_prompt (Optional[BasePromptTemplate]): Pandas prompt to use.</span>
<span class="sd">        head (int): Number of rows to show in the table context.</span>
<span class="sd">        llm (Optional[LLM]): Language model to use.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-experimental`</span>

<span class="sd">        ```python</span>
<span class="sd">        import pandas as pd</span>
<span class="sd">        from llama_index.experimental.query_engine.pandas import PandasQueryEngine</span>

<span class="sd">        df = pd.DataFrame(</span>
<span class="sd">            {</span>
<span class="sd">                "city": ["Toronto", "Tokyo", "Berlin"],</span>
<span class="sd">                "population": [2930000, 13960000, 3645000]</span>
<span class="sd">            }</span>
<span class="sd">        )</span>

<span class="sd">        query_engine = PandasQueryEngine(df=df, verbose=True)</span>

<span class="sd">        response = query_engine.query("What is the population of Tokyo?")</span>
<span class="sd">        ```</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">df</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">,</span>
        <span class="n">instruction_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">instruction_parser</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PandasInstructionParser</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">pandas_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">head</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">synthesize_response</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">response_synthesis_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BasePromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_df</span> <span class="o">=</span> <span class="n">df</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_head</span> <span class="o">=</span> <span class="n">head</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_prompt</span> <span class="o">=</span> <span class="n">pandas_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_PANDAS_PROMPT</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_instruction_str</span> <span class="o">=</span> <span class="n">instruction_str</span> <span class="ow">or</span> <span class="n">DEFAULT_INSTRUCTION_STR</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_instruction_parser</span> <span class="o">=</span> <span class="n">instruction_parser</span> <span class="ow">or</span> <span class="n">PandasInstructionParser</span><span class="p">(</span>
            <span class="n">df</span><span class="p">,</span> <span class="n">output_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_synthesize_response</span> <span class="o">=</span> <span class="n">synthesize_response</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">response_synthesis_prompt</span> <span class="ow">or</span> <span class="n">DEFAULT_RESPONSE_SYNTHESIS_PROMPT</span>
        <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span>
                <span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_prompt_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PromptMixinType</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get prompt sub-modules."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">_get_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get prompts."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"pandas_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_prompt</span><span class="p">,</span>
            <span class="s2">"response_synthesis_prompt"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">_update_prompts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prompts</span><span class="p">:</span> <span class="n">PromptDictType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Update prompts."""</span>
        <span class="k">if</span> <span class="s2">"pandas_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"pandas_prompt"</span><span class="p">]</span>
        <span class="k">if</span> <span class="s2">"response_synthesis_prompt"</span> <span class="ow">in</span> <span class="n">prompts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span> <span class="o">=</span> <span class="n">prompts</span><span class="p">[</span><span class="s2">"response_synthesis_prompt"</span><span class="p">]</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_index</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="n">PandasIndex</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PandasQueryEngine"</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"PandasIndex is deprecated. "</span>
            <span class="s2">"Directly construct PandasQueryEngine with df instead."</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">df</span><span class="o">=</span><span class="n">index</span><span class="o">.</span><span class="n">df</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">index</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get_table_context</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get table context."""</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_head</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Answer a query."""</span>
        <span class="n">context</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_table_context</span><span class="p">()</span>

        <span class="n">pandas_response_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_prompt</span><span class="p">,</span>
            <span class="n">df_str</span><span class="o">=</span><span class="n">context</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">instruction_str</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_instruction_str</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Pandas Instructions:</span><span class="se">\n</span><span class="s2">"</span> <span class="sa">f</span><span class="s2">"```</span><span class="se">\n</span><span class="si">{</span><span class="n">pandas_response_str</span><span class="si">}</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">pandas_output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instruction_parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">pandas_response_str</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span>
            <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Pandas Output: </span><span class="si">{</span><span class="n">pandas_output</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">response_metadata</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"pandas_instruction_str"</span><span class="p">:</span> <span class="n">pandas_response_str</span><span class="p">,</span>
            <span class="s2">"raw_pandas_output"</span><span class="p">:</span> <span class="n">pandas_output</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_synthesize_response</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_response_synthesis_prompt</span><span class="p">,</span>
                    <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="n">pandas_instructions</span><span class="o">=</span><span class="n">pandas_response_str</span><span class="p">,</span>
                    <span class="n">pandas_output</span><span class="o">=</span><span class="n">pandas_output</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">pandas_output</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">Response</span><span class="p">(</span><span class="n">response</span><span class="o">=</span><span class="n">response_str</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">response_metadata</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aquery</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Response</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multi step](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/)[Next Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/)
