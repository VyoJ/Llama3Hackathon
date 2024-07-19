Title: Finance - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/

Markdown Content:
Finance - LlamaIndex


FinanceAgentToolSpec [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseToolSpec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/#llama_index.core.tools.tool_spec.base.BaseToolSpec "llama_index.core.tools.tool_spec.base.BaseToolSpec")`

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  9</span>
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
<span class="normal">167</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FinanceAgentToolSpec</span><span class="p">(</span><span class="n">BaseToolSpec</span><span class="p">):</span>
    <span class="n">spec_functions</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s2">"find_similar_companies"</span><span class="p">,</span>
        <span class="s2">"get_earnings_history"</span><span class="p">,</span>
        <span class="s2">"get_stocks_with_upcoming_earnings"</span><span class="p">,</span>
        <span class="s2">"get_current_gainer_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_loser_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_undervalued_growth_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_technology_growth_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_most_traded_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_undervalued_large_cap_stocks"</span><span class="p">,</span>
        <span class="s2">"get_current_aggressive_small_cap_stocks"</span><span class="p">,</span>
        <span class="s2">"get_trending_finance_news"</span><span class="p">,</span>
        <span class="s2">"get_google_trending_searches"</span><span class="p">,</span>
        <span class="s2">"get_google_trends_for_query"</span><span class="p">,</span>
        <span class="s2">"get_latest_news_for_stock"</span><span class="p">,</span>
        <span class="s2">"get_current_stock_price_info"</span><span class="p">,</span>
    <span class="p">]</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">polygon_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">finnhub_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">alpha_vantage_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">newsapi_api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"ALPHA_VANTAGE"</span><span class="p">:</span> <span class="n">alpha_vantage_api_key</span><span class="p">,</span>
            <span class="s2">"POLYGON"</span><span class="p">:</span> <span class="n">polygon_api_key</span><span class="p">,</span>
            <span class="s2">"FINNHUB"</span><span class="p">:</span> <span class="n">finnhub_api_key</span><span class="p">,</span>
            <span class="s2">"NEWSAPI"</span><span class="p">:</span> <span class="n">newsapi_api_key</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">find_similar_companies</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Given a stock's ticker symbol, returns a list of similar companies."""</span>
        <span class="k">return</span> <span class="n">comparisons</span><span class="o">.</span><span class="n">find_similar_companies</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">symbol</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_earnings_history</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Given a stock's ticker symbol, returns a dataframe storing actual and estimated earnings over past K quarterly reports."""</span>
        <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_earnings_history</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">symbol</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_latest_earning_estimate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Given a stock's ticker symbol, returns it's earnings estimate for the upcoming quarterly report."""</span>
        <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_latest_earning_estimate</span><span class="p">(</span><span class="n">symbol</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_stocks_with_upcoming_earnings</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">num_days_from_now</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">only_sp500</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a pandas dataframe containing all stocks which are announcing earnings in upcoming days.</span>

<span class="sd">        Arguments:</span>
<span class="sd">         num_days_from_now: only returns stocks which announcing earnings from today's date to num_days_from_now.</span>
<span class="sd">         only_sp500: only returns sp500 stocks.</span>

<span class="sd">        """</span>
        <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">end_date</span> <span class="o">=</span> <span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span> <span class="o">+</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">num_days_from_now</span><span class="p">))</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_upcoming_earnings</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span>
            <span class="n">start_date</span><span class="o">=</span><span class="n">start_date</span><span class="p">,</span>
            <span class="n">end_date</span><span class="o">=</span><span class="n">end_date</span><span class="p">,</span>
            <span class="n">country</span><span class="o">=</span><span class="s2">"USD"</span><span class="p">,</span>
            <span class="n">only_sp500</span><span class="o">=</span><span class="n">only_sp500</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_current_gainer_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return US stocks which are classified as day gainers as per Yahoo Finance.</span>

<span class="sd">        A US stock is classified as day gainer if %change in price &gt; 3, price &gt;=5, volume &gt; 15_000</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_gainer_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_loser_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns US stocks which are classified as day losers as per Yahoo Finance.</span>

<span class="sd">        A US stock is classified as day loser if %change in price &lt; -2.5, price &gt;=5, volume &gt; 20_000</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_loser_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_undervalued_growth_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get list of undervalued growth stocks in US market as per Yahoo Finance.</span>

<span class="sd">        A stock with Price to Earnings ratio between 0-20, Price / Earnings to Growth &lt; 1</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_undervalued_growth_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_technology_growth_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a data frame of growth stocks in technology sector in US market.</span>

<span class="sd">        If a stocks's quarterly revenue growth YoY% &gt; 25%.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_technology_growth_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_most_traded_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a dataframe storing stocks which were traded the most in current market.</span>

<span class="sd">        Stocks are ordered in decreasing order of activity i.e stock traded the most on top.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_most_traded_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_undervalued_large_cap_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a dataframe storing US market large cap stocks with P/E &lt; 20."""</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_undervalued_large_cap_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_current_aggressive_small_cap_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns a dataframe storing US market small cap stocks with 1 yr % change in earnings per share &gt; 25."""</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_aggressive_small_cap_stocks</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_trending_finance_news</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Returns a list of top 10 trending news in financial market as per seekingalpha."""</span>
        <span class="n">trends</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_topk_trending_news</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">t</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">trends</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_google_trending_searches</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Returns trending searches in US as per google trends.</span>

<span class="sd">        If unable to find any trends, returns None.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_google_trending_searches</span><span class="p">(</span><span class="n">region</span><span class="o">=</span><span class="s2">"united_states"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_google_trends_for_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Finds google search trends for a given query in United States.</span>

<span class="sd">        Returns None if unable to find any trends.</span>

<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_google_trends_for_query</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="s2">"united_states"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_latest_news_for_stock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stock_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Given a stock_id representing the name of a company or the stock ticker symbol, Returns a list of news published related to top business articles in US in last 7 days from now."""</span>
        <span class="n">articles</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_latest_news_for_stock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">stock_id</span><span class="o">=</span><span class="n">stock_id</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">a</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">articles</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_current_stock_price_info</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">stock_ticker_symbol</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Given a stock's ticker symbol, returns current price information of the stock.</span>

<span class="sd">        Returns None if the provided stock ticker symbol is invalid.</span>
<span class="sd">        """</span>
        <span class="n">price_info</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_stock_price_info</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">stock_ticker_symbol</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">price_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="s2">"Current Price"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"c"</span><span class="p">],</span>
                <span class="s2">"High Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"h"</span><span class="p">],</span>
                <span class="s2">"Low Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"l"</span><span class="p">],</span>
                <span class="s2">"Open Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"o"</span><span class="p">],</span>
                <span class="s2">"Percentage change"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"dp"</span><span class="p">],</span>
            <span class="p">}</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### find\_similar\_companies [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.find_similar_companies "Permanent link")

```
find_similar_companies(symbol: str) -> List[str]
```

Given a stock's ticker symbol, returns a list of similar companies.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">find_similar_companies</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Given a stock's ticker symbol, returns a list of similar companies."""</span>
    <span class="k">return</span> <span class="n">comparisons</span><span class="o">.</span><span class="n">find_similar_companies</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">symbol</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_earnings\_history [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_earnings_history "Permanent link")

```
get_earnings_history(symbol: str) -> DataFrame
```

Given a stock's ticker symbol, returns a dataframe storing actual and estimated earnings over past K quarterly reports.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_earnings_history</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Given a stock's ticker symbol, returns a dataframe storing actual and estimated earnings over past K quarterly reports."""</span>
    <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_earnings_history</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">symbol</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_latest\_earning\_estimate [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_latest_earning_estimate "Permanent link")

```
get_latest_earning_estimate(symbol: str) -> float
```

Given a stock's ticker symbol, returns it's earnings estimate for the upcoming quarterly report.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_latest_earning_estimate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Given a stock's ticker symbol, returns it's earnings estimate for the upcoming quarterly report."""</span>
    <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_latest_earning_estimate</span><span class="p">(</span><span class="n">symbol</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_stocks\_with\_upcoming\_earnings [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_stocks_with_upcoming_earnings "Permanent link")

```
get_stocks_with_upcoming_earnings(num_days_from_now: int, only_sp500: bool) -> DataFrame
```

Returns a pandas dataframe containing all stocks which are announcing earnings in upcoming days.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `num_days_from_now` | `int` | 
only returns stocks which announcing earnings from today's date to num\_days\_from\_now.



 | _required_ |
| `only_sp500` | `bool` | 

only returns sp500 stocks.



 | _required_ |

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
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
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_stocks_with_upcoming_earnings</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">num_days_from_now</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">only_sp500</span><span class="p">:</span> <span class="nb">bool</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a pandas dataframe containing all stocks which are announcing earnings in upcoming days.</span>

<span class="sd">    Arguments:</span>
<span class="sd">     num_days_from_now: only returns stocks which announcing earnings from today's date to num_days_from_now.</span>
<span class="sd">     only_sp500: only returns sp500 stocks.</span>

<span class="sd">    """</span>
    <span class="n">start_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">end_date</span> <span class="o">=</span> <span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span> <span class="o">+</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">num_days_from_now</span><span class="p">))</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">"%Y-%m-</span><span class="si">%d</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">earnings</span><span class="o">.</span><span class="n">get_upcoming_earnings</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span>
        <span class="n">start_date</span><span class="o">=</span><span class="n">start_date</span><span class="p">,</span>
        <span class="n">end_date</span><span class="o">=</span><span class="n">end_date</span><span class="p">,</span>
        <span class="n">country</span><span class="o">=</span><span class="s2">"USD"</span><span class="p">,</span>
        <span class="n">only_sp500</span><span class="o">=</span><span class="n">only_sp500</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_gainer\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_gainer_stocks "Permanent link")

```
get_current_gainer_stocks() -> DataFrame
```

Return US stocks which are classified as day gainers as per Yahoo Finance.

A US stock is classified as day gainer if %change in price > 3, price >=5, volume > 15\_000

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_gainer_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return US stocks which are classified as day gainers as per Yahoo Finance.</span>

<span class="sd">    A US stock is classified as day gainer if %change in price &gt; 3, price &gt;=5, volume &gt; 15_000</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_gainer_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_loser\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_loser_stocks "Permanent link")

```
get_current_loser_stocks() -> DataFrame
```

Returns US stocks which are classified as day losers as per Yahoo Finance.

A US stock is classified as day loser if %change in price < -2.5, price >=5, volume > 20\_000

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_loser_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns US stocks which are classified as day losers as per Yahoo Finance.</span>

<span class="sd">    A US stock is classified as day loser if %change in price &lt; -2.5, price &gt;=5, volume &gt; 20_000</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_loser_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_undervalued\_growth\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_undervalued_growth_stocks "Permanent link")

```
get_current_undervalued_growth_stocks() -> DataFrame
```

Get list of undervalued growth stocks in US market as per Yahoo Finance.

A stock with Price to Earnings ratio between 0-20, Price / Earnings to Growth < 1

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_undervalued_growth_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get list of undervalued growth stocks in US market as per Yahoo Finance.</span>

<span class="sd">    A stock with Price to Earnings ratio between 0-20, Price / Earnings to Growth &lt; 1</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_undervalued_growth_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_technology\_growth\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_technology_growth_stocks "Permanent link")

```
get_current_technology_growth_stocks() -> DataFrame
```

Returns a data frame of growth stocks in technology sector in US market.

If a stocks's quarterly revenue growth YoY% > 25%.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_technology_growth_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a data frame of growth stocks in technology sector in US market.</span>

<span class="sd">    If a stocks's quarterly revenue growth YoY% &gt; 25%.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_technology_growth_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_most\_traded\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_most_traded_stocks "Permanent link")

```
get_current_most_traded_stocks() -> DataFrame
```

Returns a dataframe storing stocks which were traded the most in current market.

Stocks are ordered in decreasing order of activity i.e stock traded the most on top.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_most_traded_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a dataframe storing stocks which were traded the most in current market.</span>

<span class="sd">    Stocks are ordered in decreasing order of activity i.e stock traded the most on top.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_most_traded_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_undervalued\_large\_cap\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_undervalued_large_cap_stocks "Permanent link")

```
get_current_undervalued_large_cap_stocks() -> DataFrame
```

Returns a dataframe storing US market large cap stocks with P/E < 20.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_undervalued_large_cap_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a dataframe storing US market large cap stocks with P/E &lt; 20."""</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_undervalued_large_cap_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_aggressive\_small\_cap\_stocks [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_aggressive_small_cap_stocks "Permanent link")

```
get_current_aggressive_small_cap_stocks() -> DataFrame
```

Returns a dataframe storing US market small cap stocks with 1 yr % change in earnings per share > 25.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_aggressive_small_cap_stocks</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns a dataframe storing US market small cap stocks with 1 yr % change in earnings per share &gt; 25."""</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_aggressive_small_cap_stocks</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### get\_trending\_finance\_news [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_trending_finance_news "Permanent link")

```
get_trending_finance_news() -> List[str]
```

Returns a list of top 10 trending news in financial market as per seekingalpha.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_trending_finance_news</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Returns a list of top 10 trending news in financial market as per seekingalpha."""</span>
    <span class="n">trends</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_topk_trending_news</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">t</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">trends</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_google\_trending\_searches [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_google_trending_searches "Permanent link")

```
get_google_trending_searches() -> Optional[DataFrame]
```

Returns trending searches in US as per google trends.

If unable to find any trends, returns None.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_google_trending_searches</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Returns trending searches in US as per google trends.</span>

<span class="sd">    If unable to find any trends, returns None.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_google_trending_searches</span><span class="p">(</span><span class="n">region</span><span class="o">=</span><span class="s2">"united_states"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_google\_trends\_for\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_google_trends_for_query "Permanent link")

```
get_google_trends_for_query(query: str) -> Optional[DataFrame]
```

Finds google search trends for a given query in United States.

Returns None if unable to find any trends.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_google_trends_for_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Finds google search trends for a given query in United States.</span>

<span class="sd">    Returns None if unable to find any trends.</span>

<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">news</span><span class="o">.</span><span class="n">get_google_trends_for_query</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="s2">"united_states"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_latest\_news\_for\_stock [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_latest_news_for_stock "Permanent link")

```
get_latest_news_for_stock(stock_id: str) -> List[str]
```

Given a stock\_id representing the name of a company or the stock ticker symbol, Returns a list of news published related to top business articles in US in last 7 days from now.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_latest_news_for_stock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stock_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Given a stock_id representing the name of a company or the stock ticker symbol, Returns a list of news published related to top business articles in US in last 7 days from now."""</span>
    <span class="n">articles</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_latest_news_for_stock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">stock_id</span><span class="o">=</span><span class="n">stock_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">a</span><span class="p">[</span><span class="s2">"title"</span><span class="p">]</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">articles</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_current\_stock\_price\_info [#](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/#llama_index.tools.finance.FinanceAgentToolSpec.get_current_stock_price_info "Permanent link")

```
get_current_stock_price_info(stock_ticker_symbol: str) -> Optional[Dict[str, Any]]
```

Given a stock's ticker symbol, returns current price information of the stock.

Returns None if the provided stock ticker symbol is invalid.

Source code in `llama-index-integrations/tools/llama-index-tools-finance/llama_index/tools/finance/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
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
<span class="normal">167</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_current_stock_price_info</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">stock_ticker_symbol</span><span class="p">:</span> <span class="nb">str</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Given a stock's ticker symbol, returns current price information of the stock.</span>

<span class="sd">    Returns None if the provided stock ticker symbol is invalid.</span>
<span class="sd">    """</span>
    <span class="n">price_info</span> <span class="o">=</span> <span class="n">news</span><span class="o">.</span><span class="n">get_current_stock_price_info</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_api_key</span><span class="p">,</span> <span class="n">stock_ticker_symbol</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">price_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"Current Price"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"c"</span><span class="p">],</span>
            <span class="s2">"High Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"h"</span><span class="p">],</span>
            <span class="s2">"Low Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"l"</span><span class="p">],</span>
            <span class="s2">"Open Price of the day"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"o"</span><span class="p">],</span>
            <span class="s2">"Percentage change"</span><span class="p">:</span> <span class="n">price_info</span><span class="p">[</span><span class="s2">"dp"</span><span class="p">],</span>
        <span class="p">}</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Exa](https://docs.llamaindex.ai/en/stable/api_reference/tools/exa/)[Next Function](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/)
