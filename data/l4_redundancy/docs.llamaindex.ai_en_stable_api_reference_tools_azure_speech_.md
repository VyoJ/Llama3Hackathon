Title: Azure speech - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/

Markdown Content:
Azure speech - LlamaIndex


AzureSpeechToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/#llama_index.tools.azure_speech.AzureSpeechToolSpec "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Azure Speech tool spec.

Source code in `llama-index-integrations/tools/llama-index-tools-azure-speech/llama_index/tools/azure_speech/base.py`

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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AzureSpeechToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Azure Speech tool spec."""</span>

    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"speech_to_text"</span><span class="p">,</span> <span class="s2">"text_to_speech"</span><span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">region</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">speech_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"en-US"</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">azure.cognitiveservices.speech</span> <span class="k">as</span> <span class="nn">speechsdk</span>

<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">config</span> <span class="o">=</span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">SpeechConfig</span><span class="p">(</span><span class="n">subscription</span><span class="o">=</span><span class="n">speech_key</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="n">region</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">speech_recognition_language</span> <span class="o">=</span> <span class="n">language</span>

    <span class="k">def</span> <span class="nf">text_to_speech</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This tool accepts a natural language string and will use Azure speech services to create an</span>
<span class="sd">        audio version of the text, and play it on the users computer.</span>

<span class="sd">        Args:</span>
<span class="sd">            text (str): The text to play</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">azure.cognitiveservices.speech</span> <span class="k">as</span> <span class="nn">speechsdk</span>

        <span class="n">speech_synthesizer</span> <span class="o">=</span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">SpeechSynthesizer</span><span class="p">(</span><span class="n">speech_config</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">speech_synthesizer</span><span class="o">.</span><span class="n">speak_text</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">reason</span> <span class="o"></span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">ResultReason</span><span class="o">.</span><span class="n">Canceled</span><span class="p">:</span>
            <span class="n">cancellation_details</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">cancellation_details</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Speech synthesis canceled: </span><span class="si">{</span><span class="n">cancellation_details</span><span class="o">.</span><span class="n">reason</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">cancellation_details</span><span class="o">.</span><span class="n">reason</span> <span class="o"></span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">ResultReason</span><span class="o">.</span><span class="n">SynthesizingAudioCompleted</span><span class="p">:</span>
        <span class="n">speechsdk</span><span class="o">.</span><span class="n">AudioDataStream</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">"Audio playback complete."</span>
    <span class="k">elif</span> <span class="n">result</span><span class="o">.</span><span class="n">reason</span> <span class="o"></span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">CancellationReason</span><span class="o">.</span><span class="n">Error</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error details: </span><span class="si">{</span><span class="n">cancellation_details</span><span class="o">.</span><span class="n">error_details</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### speech\_to\_text [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/#llama_index.tools.azure_speech.AzureSpeechToolSpec.speech_to_text "Permanent link")

```
speech_to_text(filename: str) -> List[str]
```

This tool accepts a filename for a speech audio file and uses Azure to transcribe it into text.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `filename` | `str` | 
The name of the file to transcribe



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-azure-speech/llama_index/tools/azure_speech/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">71</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">speech_to_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This tool accepts a filename for a speech audio file and uses Azure to transcribe it into text.</span>

<span class="sd">    Args:</span>
<span class="sd">        filename (str): The name of the file to transcribe</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">azure.cognitiveservices.speech</span> <span class="k">as</span> <span class="nn">speechsdk</span>

    <span class="n">speech_recognizer</span> <span class="o">=</span> <span class="n">speechsdk</span><span class="o">.</span><span class="n">SpeechRecognizer</span><span class="p">(</span>
        <span class="n">speech_config</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">,</span>
        <span class="n">audio_config</span><span class="o">=</span><span class="n">speechsdk</span><span class="o">.</span><span class="n">audio</span><span class="o">.</span><span class="n">AudioConfig</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="n">filename</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transcribe</span><span class="p">(</span><span class="n">speech_recognizer</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Azure cv](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/)[Next Azure translate](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)
