Title: Code interpreter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/

Markdown Content:
Code interpreter - LlamaIndex


init.py.

CodeInterpreterToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/#llama_index.tools.code_interpreter.CodeInterpreterToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Code Interpreter tool spec.

WARNING: This tool provides the Agent access to the `subprocess.run` command. Arbitrary code execution is possible on the machine running this tool. This tool is not recommended to be used in a production setting, and would require heavy sandboxing or virtual machines

Source code in `llama-index-integrations/tools/llama-index-tools-code-interpreter/llama_index/tools/code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
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
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CodeInterpreterToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Code Interpreter tool spec.</span>

<span class="sd">    WARNING: This tool provides the Agent access to the `subprocess.run` command.</span>
<span class="sd">    Arbitrary code execution is possible on the machine running this tool.</span>
<span class="sd">    This tool is not recommended to be used in a production setting, and would require heavy sandboxing or virtual machines</span>

<span class="sd">    """</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"code_interpreter"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">code_interpreter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">code</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        A function to execute python code, and return the stdout and stderr.</span>

<span class="sd">        You should import any libraries that you wish to use. You have access to any libraries the user has installed.</span>

<span class="sd">        The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.</span>

<span class="sd">        You should interpret the output and errors returned from this function, and attempt to fix any problems.</span>
<span class="sd">        If you cannot fix the error, show the code to the user and ask for help</span>

<span class="sd">        It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.</span>
<span class="sd">        """</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">,</span> <span class="s2">"-c"</span><span class="p">,</span> <span class="n">code</span><span class="p">],</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"StdOut:</span><span class="se">\n</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">stdout</span><span class="si">}</span><span class="se">\n</span><span class="s2">StdErr:</span><span class="se">\n</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">stderr</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

### code\_interpreter [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/#llama_index.tools.code_interpreter.CodeInterpreterToolSpec.code_interpreter "Permanent link")

```
code_interpreter(code: str)
```

A function to execute python code, and return the stdout and stderr.

You should import any libraries that you wish to use. You have access to any libraries the user has installed.

The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.

You should interpret the output and errors returned from this function, and attempt to fix any problems. If you cannot fix the error, show the code to the user and ask for help

It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.

Source code in `llama-index-integrations/tools/llama-index-tools-code-interpreter/llama_index/tools/code_interpreter/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
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
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">code_interpreter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">code</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    A function to execute python code, and return the stdout and stderr.</span>

<span class="sd">    You should import any libraries that you wish to use. You have access to any libraries the user has installed.</span>

<span class="sd">    The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.</span>

<span class="sd">    You should interpret the output and errors returned from this function, and attempt to fix any problems.</span>
<span class="sd">    If you cannot fix the error, show the code to the user and ask for help</span>

<span class="sd">    It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.</span>
<span class="sd">    """</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">,</span> <span class="s2">"-c"</span><span class="p">,</span> <span class="n">code</span><span class="p">],</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">"StdOut:</span><span class="se">\n</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">stdout</span><span class="si">}</span><span class="se">\n</span><span class="s2">StdErr:</span><span class="se">\n</span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">stderr</span><span class="si">}</span><span class="s2">"</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/)[Next Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/tools/cogniswitch/)
