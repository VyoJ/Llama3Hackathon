Title: Telegram - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/

Markdown Content:
Telegram - LlamaIndex


TelegramReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/#llama_index.readers.telegram.TelegramReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Telegram posts/chat messages/comments reader.

Read posts/chat messages/comments from Telegram channels or chats.

Before working with Telegram’s API, you need to get your own API ID and hash:

```
1. Login to your Telegram account with the phone number of the developer account to use.
2. Click under API Development tools.
3. A Create new application window will appear. Fill in your application details.            There is no need to enter any URL,            and only the first two fields (App title and Short name) can currently be changed later.
4. Click on Create application at the end.            Remember that your API hash is secret and Telegram won’t let you revoke it.            Don’t post it anywhere!
```

This API ID and hash is the one used by your application, not your phone number. You can use this API ID and hash with any phone number.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `session_name` | `str` | 
The file name of the session file to be used if a string is given (it may be a full path), or the Session instance to be used otherwise.



 | _required_ |
| `api_id` | `int` | 

The API ID you obtained from https://my.telegram.org.



 | _required_ |
| `api_hash` | `str` | 

The API hash you obtained from https://my.telegram.org.



 | _required_ |
| `phone_number` | `str` | 

The phone to which the code will be sent.



 | _required_ |

Source code in `llama-index-integrations/readers/llama-index-readers-telegram/llama_index/readers/telegram/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 12</span>
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
<span class="normal">148</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">TelegramReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Telegram posts/chat messages/comments reader.</span>

<span class="sd">    Read posts/chat messages/comments from Telegram channels or chats.</span>

<span class="sd">    Before working with Telegram’s API, you need to get your own API ID and hash:</span>

<span class="sd">        1. Login to your Telegram account with the phone number of the developer account to use.</span>
<span class="sd">        2. Click under API Development tools.</span>
<span class="sd">        3. A Create new application window will appear. Fill in your application details.\</span>
<span class="sd">            There is no need to enter any URL,\</span>
<span class="sd">            and only the first two fields (App title and Short name) can currently be changed later.</span>
<span class="sd">        4. Click on Create application at the end.\</span>
<span class="sd">            Remember that your API hash is secret and Telegram won’t let you revoke it.\</span>
<span class="sd">            Don’t post it anywhere!</span>

<span class="sd">    This API ID and hash is the one used by your application, not your phone number.\</span>
<span class="sd">        You can use this API ID and hash with any phone number.</span>

<span class="sd">    Args:</span>
<span class="sd">        session_name (str): The file name of the session file to be used\</span>
<span class="sd">            if a string is given (it may be a full path),\</span>
<span class="sd">            or the Session instance to be used otherwise.</span>
<span class="sd">        api_id (int): The API ID you obtained from https://my.telegram.org.</span>
<span class="sd">        api_hash (str): The API hash you obtained from https://my.telegram.org.</span>
<span class="sd">        phone_number (str): The phone to which the code will be sent.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">session_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">api_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">api_hash</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">phone_number</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with parameters."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">session_name</span> <span class="o">=</span> <span class="n">session_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_id</span> <span class="o">=</span> <span class="n">api_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">api_hash</span> <span class="o">=</span> <span class="n">api_hash</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">phone_number</span> <span class="o">=</span> <span class="n">phone_number</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
        <span class="n">asyncio</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">post_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load posts/chat messages/comments from Telegram channels or chats.</span>

<span class="sd">        Since Telethon is an asynchronous library,\</span>
<span class="sd">            you need to await coroutine functions to have them run\</span>
<span class="sd">            (or otherwise, run the loop until they are complete)</span>

<span class="sd">        Args:</span>
<span class="sd">            entity_name (str): The entity from whom to retrieve the message history.</span>
<span class="sd">            post_id (int): If set to a post ID, \</span>
<span class="sd">                the comments that reply to this ID will be returned.\</span>
<span class="sd">                Else will get posts/chat messages.</span>
<span class="sd">            limit (int): Number of messages to be retrieved.</span>
<span class="sd">            start_date (datetime.datetime): Start date of the time period.</span>
<span class="sd">            end_date (datetime.datetime): End date of the time period.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_load_data</span><span class="p">(</span>
                <span class="n">entity_name</span><span class="o">=</span><span class="n">entity_name</span><span class="p">,</span>
                <span class="n">post_id</span><span class="o">=</span><span class="n">post_id</span><span class="p">,</span>
                <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                <span class="n">start_date</span><span class="o">=</span><span class="n">start_date</span><span class="p">,</span>
                <span class="n">end_date</span><span class="o">=</span><span class="n">end_date</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">post_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">end_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load posts/chat messages/comments from Telegram channels or chats.</span>

<span class="sd">        Args:</span>
<span class="sd">            entity_name (str): The entity from whom to retrieve the message history.</span>
<span class="sd">            post_id (int): If set to a post ID, \</span>
<span class="sd">                the comments that reply to this ID will be returned.\</span>
<span class="sd">                Else will get posts/chat messages.</span>
<span class="sd">            limit (int): Number of messages to be retrieved.</span>
<span class="sd">            start_date (datetime.datetime): Start date of the time period.</span>
<span class="sd">            end_date (datetime.datetime): End date of the time period.</span>

<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">telethon</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">telethon</span><span class="o">.</span><span class="n">TelegramClient</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">session_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">api_hash</span><span class="p">)</span>
        <span class="k">await</span> <span class="n">client</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">phone</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">phone_number</span><span class="p">)</span>

        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">client</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">end_date</span> <span class="ow">and</span> <span class="n">start_date</span><span class="p">:</span>
                <span class="c1"># Asynchronously iterate over messages in between start_date and end_date</span>
                <span class="k">async</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">client</span><span class="o">.</span><span class="n">iter_messages</span><span class="p">(</span>
                    <span class="n">entity_name</span><span class="p">,</span>
                    <span class="n">reply_to</span><span class="o">=</span><span class="n">post_id</span><span class="p">,</span>
                    <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                    <span class="n">offset_date</span><span class="o">=</span><span class="n">end_date</span><span class="p">,</span>
                <span class="p">):</span>
                    <span class="k">if</span> <span class="n">message</span><span class="o">.</span><span class="n">date</span> <span class="o">&lt;</span> <span class="n">start_date</span><span class="p">:</span>
                        <span class="k">break</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="n">message</span><span class="o">.</span><span class="n">text</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">:</span>
                        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_remove_links</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">text</span><span class="p">)))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Asynchronously iterate over messages</span>
                <span class="k">async</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">client</span><span class="o">.</span><span class="n">iter_messages</span><span class="p">(</span>
                    <span class="n">entity_name</span><span class="p">,</span>
                    <span class="n">reply_to</span><span class="o">=</span><span class="n">post_id</span><span class="p">,</span>
                    <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
                <span class="p">):</span>
                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="n">message</span><span class="o">.</span><span class="n">text</span> <span class="o">!=</span> <span class="s2">""</span><span class="p">:</span>
                        <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_remove_links</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">text</span><span class="p">)))</span>
        <span class="k">return</span> <span class="n">results</span>

    <span class="k">def</span> <span class="nf">_remove_links</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Removes all URLs from a given string, leaving only the base domain name."""</span>

        <span class="k">def</span> <span class="nf">replace_match</span><span class="p">(</span><span class="n">match</span><span class="p">):</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">text</span> <span class="k">if</span> <span class="n">text</span> <span class="k">else</span> <span class="s2">""</span>

        <span class="n">url_pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"https?://(?:www\.)?((?!www\.).)+?"</span>
        <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">url_pattern</span><span class="p">,</span> <span class="n">replace_match</span><span class="p">,</span> <span class="n">string</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/#llama_index.readers.telegram.TelegramReader.load_data "Permanent link")

```
load_data(entity_name: str, post_id: Optional[int] = None, limit: Optional[int] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load posts/chat messages/comments from Telegram channels or chats.

Since Telethon is an asynchronous library, you need to await coroutine functions to have them run (or otherwise, run the loop until they are complete)

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `entity_name` | `str` | 
The entity from whom to retrieve the message history.



 | _required_ |
| `post_id` | `int` | 

If set to a post ID, the comments that reply to this ID will be returned. Else will get posts/chat messages.



 | `None` |
| `limit` | `int` | 

Number of messages to be retrieved.



 | `None` |
| `start_date` | `datetime` | 

Start date of the time period.



 | `None` |
| `end_date` | `datetime` | 

End date of the time period.



 | `None` |

Source code in `llama-index-integrations/readers/llama-index-readers-telegram/llama_index/readers/telegram/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">post_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">start_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">end_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load posts/chat messages/comments from Telegram channels or chats.</span>

<span class="sd">    Since Telethon is an asynchronous library,\</span>
<span class="sd">        you need to await coroutine functions to have them run\</span>
<span class="sd">        (or otherwise, run the loop until they are complete)</span>

<span class="sd">    Args:</span>
<span class="sd">        entity_name (str): The entity from whom to retrieve the message history.</span>
<span class="sd">        post_id (int): If set to a post ID, \</span>
<span class="sd">            the comments that reply to this ID will be returned.\</span>
<span class="sd">            Else will get posts/chat messages.</span>
<span class="sd">        limit (int): Number of messages to be retrieved.</span>
<span class="sd">        start_date (datetime.datetime): Start date of the time period.</span>
<span class="sd">        end_date (datetime.datetime): End date of the time period.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_load_data</span><span class="p">(</span>
            <span class="n">entity_name</span><span class="o">=</span><span class="n">entity_name</span><span class="p">,</span>
            <span class="n">post_id</span><span class="o">=</span><span class="n">post_id</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">start_date</span><span class="o">=</span><span class="n">start_date</span><span class="p">,</span>
            <span class="n">end_date</span><span class="o">=</span><span class="n">end_date</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Structured data](https://docs.llamaindex.ai/en/stable/api_reference/readers/structured_data/)[Next Toggl](https://docs.llamaindex.ai/en/stable/api_reference/readers/toggl/)
