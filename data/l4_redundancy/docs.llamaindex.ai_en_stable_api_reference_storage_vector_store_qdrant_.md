Title: Qdrant - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/

Markdown Content:
Qdrant - LlamaIndex


QdrantVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/#llama_index.vector_stores.qdrant.QdrantVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Qdrant Vector Store.

In this vector store, embeddings and docs are stored within a Qdrant collection.

During query time, the index uses Qdrant to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `collection_name` | `str` | 
(str): name of the Qdrant collection



 | _required_ |
| `client` | `Optional[Any]` | 

QdrantClient instance from `qdrant-client` package



 | `None` |
| `aclient` | `Optional[Any]` | 

AsyncQdrantClient instance from `qdrant-client` package



 | `None` |
| `url` | `Optional[str]` | 

url of the Qdrant instance



 | `None` |
| `api_key` | `Optional[str]` | 

API key for authenticating with Qdrant



 | `None` |
| `batch_size` | `int` | 

number of points to upload in a single request to Qdrant. Defaults to 64



 | `64` |
| `parallel` | `int` | 

number of parallel processes to use during upload. Defaults to 1



 | `1` |
| `max_retries` | `int` | 

maximum number of retries in case of a failure. Defaults to 3



 | `3` |
| `client_kwargs` | `Optional[dict]` | 

additional kwargs for QdrantClient and AsyncQdrantClient



 | `None` |
| `enable_hybrid` | `bool` | 

whether to enable hybrid search using dense and sparse vectors



 | `False` |
| `fastembed_sparse_model` | `Optional[str]` | 

name of the FastEmbed sparse model to use, if any



 | `None` |
| `sparse_doc_fn` | `Optional[SparseEncoderCallable]` | 

function to encode sparse vectors



 | `None` |
| `sparse_query_fn` | `Optional[SparseEncoderCallable]` | 

function to encode sparse queries



 | `None` |
| `hybrid_fusion_fn` | `Optional[HybridFusionCallable]` | 

function to fuse hybrid search results



 | `None` |
| `index_doc_id` | `bool` | 

whether to create a payload index for the document ID. Defaults to True



 | `True` |

**Examples:**

`pip install llama-index-vector-stores-qdrant`

```
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore

client = qdrant_client.QdrantClient()

vector_store = QdrantVectorStore(
    collection_name="example_collection", client=client
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-qdrant/llama_index/vector_stores/qdrant/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">  61</span>
<span class="normal">  62</span>
<span class="normal">  63</span>
<span class="normal">  64</span>
<span class="normal">  65</span>
<span class="normal">  66</span>
<span class="normal">  67</span>
<span class="normal">  68</span>
<span class="normal">  69</span>
<span class="normal">  70</span>
<span class="normal">  71</span>
<span class="normal">  72</span>
<span class="normal">  73</span>
<span class="normal">  74</span>
<span class="normal">  75</span>
<span class="normal">  76</span>
<span class="normal">  77</span>
<span class="normal">  78</span>
<span class="normal">  79</span>
<span class="normal">  80</span>
<span class="normal">  81</span>
<span class="normal">  82</span>
<span class="normal">  83</span>
<span class="normal">  84</span>
<span class="normal">  85</span>
<span class="normal">  86</span>
<span class="normal">  87</span>
<span class="normal">  88</span>
<span class="normal">  89</span>
<span class="normal">  90</span>
<span class="normal">  91</span>
<span class="normal">  92</span>
<span class="normal">  93</span>
<span class="normal">  94</span>
<span class="normal">  95</span>
<span class="normal">  96</span>
<span class="normal">  97</span>
<span class="normal">  98</span>
<span class="normal">  99</span>
<span class="normal"> 100</span>
<span class="normal"> 101</span>
<span class="normal"> 102</span>
<span class="normal"> 103</span>
<span class="normal"> 104</span>
<span class="normal"> 105</span>
<span class="normal"> 106</span>
<span class="normal"> 107</span>
<span class="normal"> 108</span>
<span class="normal"> 109</span>
<span class="normal"> 110</span>
<span class="normal"> 111</span>
<span class="normal"> 112</span>
<span class="normal"> 113</span>
<span class="normal"> 114</span>
<span class="normal"> 115</span>
<span class="normal"> 116</span>
<span class="normal"> 117</span>
<span class="normal"> 118</span>
<span class="normal"> 119</span>
<span class="normal"> 120</span>
<span class="normal"> 121</span>
<span class="normal"> 122</span>
<span class="normal"> 123</span>
<span class="normal"> 124</span>
<span class="normal"> 125</span>
<span class="normal"> 126</span>
<span class="normal"> 127</span>
<span class="normal"> 128</span>
<span class="normal"> 129</span>
<span class="normal"> 130</span>
<span class="normal"> 131</span>
<span class="normal"> 132</span>
<span class="normal"> 133</span>
<span class="normal"> 134</span>
<span class="normal"> 135</span>
<span class="normal"> 136</span>
<span class="normal"> 137</span>
<span class="normal"> 138</span>
<span class="normal"> 139</span>
<span class="normal"> 140</span>
<span class="normal"> 141</span>
<span class="normal"> 142</span>
<span class="normal"> 143</span>
<span class="normal"> 144</span>
<span class="normal"> 145</span>
<span class="normal"> 146</span>
<span class="normal"> 147</span>
<span class="normal"> 148</span>
<span class="normal"> 149</span>
<span class="normal"> 150</span>
<span class="normal"> 151</span>
<span class="normal"> 152</span>
<span class="normal"> 153</span>
<span class="normal"> 154</span>
<span class="normal"> 155</span>
<span class="normal"> 156</span>
<span class="normal"> 157</span>
<span class="normal"> 158</span>
<span class="normal"> 159</span>
<span class="normal"> 160</span>
<span class="normal"> 161</span>
<span class="normal"> 162</span>
<span class="normal"> 163</span>
<span class="normal"> 164</span>
<span class="normal"> 165</span>
<span class="normal"> 166</span>
<span class="normal"> 167</span>
<span class="normal"> 168</span>
<span class="normal"> 169</span>
<span class="normal"> 170</span>
<span class="normal"> 171</span>
<span class="normal"> 172</span>
<span class="normal"> 173</span>
<span class="normal"> 174</span>
<span class="normal"> 175</span>
<span class="normal"> 176</span>
<span class="normal"> 177</span>
<span class="normal"> 178</span>
<span class="normal"> 179</span>
<span class="normal"> 180</span>
<span class="normal"> 181</span>
<span class="normal"> 182</span>
<span class="normal"> 183</span>
<span class="normal"> 184</span>
<span class="normal"> 185</span>
<span class="normal"> 186</span>
<span class="normal"> 187</span>
<span class="normal"> 188</span>
<span class="normal"> 189</span>
<span class="normal"> 190</span>
<span class="normal"> 191</span>
<span class="normal"> 192</span>
<span class="normal"> 193</span>
<span class="normal"> 194</span>
<span class="normal"> 195</span>
<span class="normal"> 196</span>
<span class="normal"> 197</span>
<span class="normal"> 198</span>
<span class="normal"> 199</span>
<span class="normal"> 200</span>
<span class="normal"> 201</span>
<span class="normal"> 202</span>
<span class="normal"> 203</span>
<span class="normal"> 204</span>
<span class="normal"> 205</span>
<span class="normal"> 206</span>
<span class="normal"> 207</span>
<span class="normal"> 208</span>
<span class="normal"> 209</span>
<span class="normal"> 210</span>
<span class="normal"> 211</span>
<span class="normal"> 212</span>
<span class="normal"> 213</span>
<span class="normal"> 214</span>
<span class="normal"> 215</span>
<span class="normal"> 216</span>
<span class="normal"> 217</span>
<span class="normal"> 218</span>
<span class="normal"> 219</span>
<span class="normal"> 220</span>
<span class="normal"> 221</span>
<span class="normal"> 222</span>
<span class="normal"> 223</span>
<span class="normal"> 224</span>
<span class="normal"> 225</span>
<span class="normal"> 226</span>
<span class="normal"> 227</span>
<span class="normal"> 228</span>
<span class="normal"> 229</span>
<span class="normal"> 230</span>
<span class="normal"> 231</span>
<span class="normal"> 232</span>
<span class="normal"> 233</span>
<span class="normal"> 234</span>
<span class="normal"> 235</span>
<span class="normal"> 236</span>
<span class="normal"> 237</span>
<span class="normal"> 238</span>
<span class="normal"> 239</span>
<span class="normal"> 240</span>
<span class="normal"> 241</span>
<span class="normal"> 242</span>
<span class="normal"> 243</span>
<span class="normal"> 244</span>
<span class="normal"> 245</span>
<span class="normal"> 246</span>
<span class="normal"> 247</span>
<span class="normal"> 248</span>
<span class="normal"> 249</span>
<span class="normal"> 250</span>
<span class="normal"> 251</span>
<span class="normal"> 252</span>
<span class="normal"> 253</span>
<span class="normal"> 254</span>
<span class="normal"> 255</span>
<span class="normal"> 256</span>
<span class="normal"> 257</span>
<span class="normal"> 258</span>
<span class="normal"> 259</span>
<span class="normal"> 260</span>
<span class="normal"> 261</span>
<span class="normal"> 262</span>
<span class="normal"> 263</span>
<span class="normal"> 264</span>
<span class="normal"> 265</span>
<span class="normal"> 266</span>
<span class="normal"> 267</span>
<span class="normal"> 268</span>
<span class="normal"> 269</span>
<span class="normal"> 270</span>
<span class="normal"> 271</span>
<span class="normal"> 272</span>
<span class="normal"> 273</span>
<span class="normal"> 274</span>
<span class="normal"> 275</span>
<span class="normal"> 276</span>
<span class="normal"> 277</span>
<span class="normal"> 278</span>
<span class="normal"> 279</span>
<span class="normal"> 280</span>
<span class="normal"> 281</span>
<span class="normal"> 282</span>
<span class="normal"> 283</span>
<span class="normal"> 284</span>
<span class="normal"> 285</span>
<span class="normal"> 286</span>
<span class="normal"> 287</span>
<span class="normal"> 288</span>
<span class="normal"> 289</span>
<span class="normal"> 290</span>
<span class="normal"> 291</span>
<span class="normal"> 292</span>
<span class="normal"> 293</span>
<span class="normal"> 294</span>
<span class="normal"> 295</span>
<span class="normal"> 296</span>
<span class="normal"> 297</span>
<span class="normal"> 298</span>
<span class="normal"> 299</span>
<span class="normal"> 300</span>
<span class="normal"> 301</span>
<span class="normal"> 302</span>
<span class="normal"> 303</span>
<span class="normal"> 304</span>
<span class="normal"> 305</span>
<span class="normal"> 306</span>
<span class="normal"> 307</span>
<span class="normal"> 308</span>
<span class="normal"> 309</span>
<span class="normal"> 310</span>
<span class="normal"> 311</span>
<span class="normal"> 312</span>
<span class="normal"> 313</span>
<span class="normal"> 314</span>
<span class="normal"> 315</span>
<span class="normal"> 316</span>
<span class="normal"> 317</span>
<span class="normal"> 318</span>
<span class="normal"> 319</span>
<span class="normal"> 320</span>
<span class="normal"> 321</span>
<span class="normal"> 322</span>
<span class="normal"> 323</span>
<span class="normal"> 324</span>
<span class="normal"> 325</span>
<span class="normal"> 326</span>
<span class="normal"> 327</span>
<span class="normal"> 328</span>
<span class="normal"> 329</span>
<span class="normal"> 330</span>
<span class="normal"> 331</span>
<span class="normal"> 332</span>
<span class="normal"> 333</span>
<span class="normal"> 334</span>
<span class="normal"> 335</span>
<span class="normal"> 336</span>
<span class="normal"> 337</span>
<span class="normal"> 338</span>
<span class="normal"> 339</span>
<span class="normal"> 340</span>
<span class="normal"> 341</span>
<span class="normal"> 342</span>
<span class="normal"> 343</span>
<span class="normal"> 344</span>
<span class="normal"> 345</span>
<span class="normal"> 346</span>
<span class="normal"> 347</span>
<span class="normal"> 348</span>
<span class="normal"> 349</span>
<span class="normal"> 350</span>
<span class="normal"> 351</span>
<span class="normal"> 352</span>
<span class="normal"> 353</span>
<span class="normal"> 354</span>
<span class="normal"> 355</span>
<span class="normal"> 356</span>
<span class="normal"> 357</span>
<span class="normal"> 358</span>
<span class="normal"> 359</span>
<span class="normal"> 360</span>
<span class="normal"> 361</span>
<span class="normal"> 362</span>
<span class="normal"> 363</span>
<span class="normal"> 364</span>
<span class="normal"> 365</span>
<span class="normal"> 366</span>
<span class="normal"> 367</span>
<span class="normal"> 368</span>
<span class="normal"> 369</span>
<span class="normal"> 370</span>
<span class="normal"> 371</span>
<span class="normal"> 372</span>
<span class="normal"> 373</span>
<span class="normal"> 374</span>
<span class="normal"> 375</span>
<span class="normal"> 376</span>
<span class="normal"> 377</span>
<span class="normal"> 378</span>
<span class="normal"> 379</span>
<span class="normal"> 380</span>
<span class="normal"> 381</span>
<span class="normal"> 382</span>
<span class="normal"> 383</span>
<span class="normal"> 384</span>
<span class="normal"> 385</span>
<span class="normal"> 386</span>
<span class="normal"> 387</span>
<span class="normal"> 388</span>
<span class="normal"> 389</span>
<span class="normal"> 390</span>
<span class="normal"> 391</span>
<span class="normal"> 392</span>
<span class="normal"> 393</span>
<span class="normal"> 394</span>
<span class="normal"> 395</span>
<span class="normal"> 396</span>
<span class="normal"> 397</span>
<span class="normal"> 398</span>
<span class="normal"> 399</span>
<span class="normal"> 400</span>
<span class="normal"> 401</span>
<span class="normal"> 402</span>
<span class="normal"> 403</span>
<span class="normal"> 404</span>
<span class="normal"> 405</span>
<span class="normal"> 406</span>
<span class="normal"> 407</span>
<span class="normal"> 408</span>
<span class="normal"> 409</span>
<span class="normal"> 410</span>
<span class="normal"> 411</span>
<span class="normal"> 412</span>
<span class="normal"> 413</span>
<span class="normal"> 414</span>
<span class="normal"> 415</span>
<span class="normal"> 416</span>
<span class="normal"> 417</span>
<span class="normal"> 418</span>
<span class="normal"> 419</span>
<span class="normal"> 420</span>
<span class="normal"> 421</span>
<span class="normal"> 422</span>
<span class="normal"> 423</span>
<span class="normal"> 424</span>
<span class="normal"> 425</span>
<span class="normal"> 426</span>
<span class="normal"> 427</span>
<span class="normal"> 428</span>
<span class="normal"> 429</span>
<span class="normal"> 430</span>
<span class="normal"> 431</span>
<span class="normal"> 432</span>
<span class="normal"> 433</span>
<span class="normal"> 434</span>
<span class="normal"> 435</span>
<span class="normal"> 436</span>
<span class="normal"> 437</span>
<span class="normal"> 438</span>
<span class="normal"> 439</span>
<span class="normal"> 440</span>
<span class="normal"> 441</span>
<span class="normal"> 442</span>
<span class="normal"> 443</span>
<span class="normal"> 444</span>
<span class="normal"> 445</span>
<span class="normal"> 446</span>
<span class="normal"> 447</span>
<span class="normal"> 448</span>
<span class="normal"> 449</span>
<span class="normal"> 450</span>
<span class="normal"> 451</span>
<span class="normal"> 452</span>
<span class="normal"> 453</span>
<span class="normal"> 454</span>
<span class="normal"> 455</span>
<span class="normal"> 456</span>
<span class="normal"> 457</span>
<span class="normal"> 458</span>
<span class="normal"> 459</span>
<span class="normal"> 460</span>
<span class="normal"> 461</span>
<span class="normal"> 462</span>
<span class="normal"> 463</span>
<span class="normal"> 464</span>
<span class="normal"> 465</span>
<span class="normal"> 466</span>
<span class="normal"> 467</span>
<span class="normal"> 468</span>
<span class="normal"> 469</span>
<span class="normal"> 470</span>
<span class="normal"> 471</span>
<span class="normal"> 472</span>
<span class="normal"> 473</span>
<span class="normal"> 474</span>
<span class="normal"> 475</span>
<span class="normal"> 476</span>
<span class="normal"> 477</span>
<span class="normal"> 478</span>
<span class="normal"> 479</span>
<span class="normal"> 480</span>
<span class="normal"> 481</span>
<span class="normal"> 482</span>
<span class="normal"> 483</span>
<span class="normal"> 484</span>
<span class="normal"> 485</span>
<span class="normal"> 486</span>
<span class="normal"> 487</span>
<span class="normal"> 488</span>
<span class="normal"> 489</span>
<span class="normal"> 490</span>
<span class="normal"> 491</span>
<span class="normal"> 492</span>
<span class="normal"> 493</span>
<span class="normal"> 494</span>
<span class="normal"> 495</span>
<span class="normal"> 496</span>
<span class="normal"> 497</span>
<span class="normal"> 498</span>
<span class="normal"> 499</span>
<span class="normal"> 500</span>
<span class="normal"> 501</span>
<span class="normal"> 502</span>
<span class="normal"> 503</span>
<span class="normal"> 504</span>
<span class="normal"> 505</span>
<span class="normal"> 506</span>
<span class="normal"> 507</span>
<span class="normal"> 508</span>
<span class="normal"> 509</span>
<span class="normal"> 510</span>
<span class="normal"> 511</span>
<span class="normal"> 512</span>
<span class="normal"> 513</span>
<span class="normal"> 514</span>
<span class="normal"> 515</span>
<span class="normal"> 516</span>
<span class="normal"> 517</span>
<span class="normal"> 518</span>
<span class="normal"> 519</span>
<span class="normal"> 520</span>
<span class="normal"> 521</span>
<span class="normal"> 522</span>
<span class="normal"> 523</span>
<span class="normal"> 524</span>
<span class="normal"> 525</span>
<span class="normal"> 526</span>
<span class="normal"> 527</span>
<span class="normal"> 528</span>
<span class="normal"> 529</span>
<span class="normal"> 530</span>
<span class="normal"> 531</span>
<span class="normal"> 532</span>
<span class="normal"> 533</span>
<span class="normal"> 534</span>
<span class="normal"> 535</span>
<span class="normal"> 536</span>
<span class="normal"> 537</span>
<span class="normal"> 538</span>
<span class="normal"> 539</span>
<span class="normal"> 540</span>
<span class="normal"> 541</span>
<span class="normal"> 542</span>
<span class="normal"> 543</span>
<span class="normal"> 544</span>
<span class="normal"> 545</span>
<span class="normal"> 546</span>
<span class="normal"> 547</span>
<span class="normal"> 548</span>
<span class="normal"> 549</span>
<span class="normal"> 550</span>
<span class="normal"> 551</span>
<span class="normal"> 552</span>
<span class="normal"> 553</span>
<span class="normal"> 554</span>
<span class="normal"> 555</span>
<span class="normal"> 556</span>
<span class="normal"> 557</span>
<span class="normal"> 558</span>
<span class="normal"> 559</span>
<span class="normal"> 560</span>
<span class="normal"> 561</span>
<span class="normal"> 562</span>
<span class="normal"> 563</span>
<span class="normal"> 564</span>
<span class="normal"> 565</span>
<span class="normal"> 566</span>
<span class="normal"> 567</span>
<span class="normal"> 568</span>
<span class="normal"> 569</span>
<span class="normal"> 570</span>
<span class="normal"> 571</span>
<span class="normal"> 572</span>
<span class="normal"> 573</span>
<span class="normal"> 574</span>
<span class="normal"> 575</span>
<span class="normal"> 576</span>
<span class="normal"> 577</span>
<span class="normal"> 578</span>
<span class="normal"> 579</span>
<span class="normal"> 580</span>
<span class="normal"> 581</span>
<span class="normal"> 582</span>
<span class="normal"> 583</span>
<span class="normal"> 584</span>
<span class="normal"> 585</span>
<span class="normal"> 586</span>
<span class="normal"> 587</span>
<span class="normal"> 588</span>
<span class="normal"> 589</span>
<span class="normal"> 590</span>
<span class="normal"> 591</span>
<span class="normal"> 592</span>
<span class="normal"> 593</span>
<span class="normal"> 594</span>
<span class="normal"> 595</span>
<span class="normal"> 596</span>
<span class="normal"> 597</span>
<span class="normal"> 598</span>
<span class="normal"> 599</span>
<span class="normal"> 600</span>
<span class="normal"> 601</span>
<span class="normal"> 602</span>
<span class="normal"> 603</span>
<span class="normal"> 604</span>
<span class="normal"> 605</span>
<span class="normal"> 606</span>
<span class="normal"> 607</span>
<span class="normal"> 608</span>
<span class="normal"> 609</span>
<span class="normal"> 610</span>
<span class="normal"> 611</span>
<span class="normal"> 612</span>
<span class="normal"> 613</span>
<span class="normal"> 614</span>
<span class="normal"> 615</span>
<span class="normal"> 616</span>
<span class="normal"> 617</span>
<span class="normal"> 618</span>
<span class="normal"> 619</span>
<span class="normal"> 620</span>
<span class="normal"> 621</span>
<span class="normal"> 622</span>
<span class="normal"> 623</span>
<span class="normal"> 624</span>
<span class="normal"> 625</span>
<span class="normal"> 626</span>
<span class="normal"> 627</span>
<span class="normal"> 628</span>
<span class="normal"> 629</span>
<span class="normal"> 630</span>
<span class="normal"> 631</span>
<span class="normal"> 632</span>
<span class="normal"> 633</span>
<span class="normal"> 634</span>
<span class="normal"> 635</span>
<span class="normal"> 636</span>
<span class="normal"> 637</span>
<span class="normal"> 638</span>
<span class="normal"> 639</span>
<span class="normal"> 640</span>
<span class="normal"> 641</span>
<span class="normal"> 642</span>
<span class="normal"> 643</span>
<span class="normal"> 644</span>
<span class="normal"> 645</span>
<span class="normal"> 646</span>
<span class="normal"> 647</span>
<span class="normal"> 648</span>
<span class="normal"> 649</span>
<span class="normal"> 650</span>
<span class="normal"> 651</span>
<span class="normal"> 652</span>
<span class="normal"> 653</span>
<span class="normal"> 654</span>
<span class="normal"> 655</span>
<span class="normal"> 656</span>
<span class="normal"> 657</span>
<span class="normal"> 658</span>
<span class="normal"> 659</span>
<span class="normal"> 660</span>
<span class="normal"> 661</span>
<span class="normal"> 662</span>
<span class="normal"> 663</span>
<span class="normal"> 664</span>
<span class="normal"> 665</span>
<span class="normal"> 666</span>
<span class="normal"> 667</span>
<span class="normal"> 668</span>
<span class="normal"> 669</span>
<span class="normal"> 670</span>
<span class="normal"> 671</span>
<span class="normal"> 672</span>
<span class="normal"> 673</span>
<span class="normal"> 674</span>
<span class="normal"> 675</span>
<span class="normal"> 676</span>
<span class="normal"> 677</span>
<span class="normal"> 678</span>
<span class="normal"> 679</span>
<span class="normal"> 680</span>
<span class="normal"> 681</span>
<span class="normal"> 682</span>
<span class="normal"> 683</span>
<span class="normal"> 684</span>
<span class="normal"> 685</span>
<span class="normal"> 686</span>
<span class="normal"> 687</span>
<span class="normal"> 688</span>
<span class="normal"> 689</span>
<span class="normal"> 690</span>
<span class="normal"> 691</span>
<span class="normal"> 692</span>
<span class="normal"> 693</span>
<span class="normal"> 694</span>
<span class="normal"> 695</span>
<span class="normal"> 696</span>
<span class="normal"> 697</span>
<span class="normal"> 698</span>
<span class="normal"> 699</span>
<span class="normal"> 700</span>
<span class="normal"> 701</span>
<span class="normal"> 702</span>
<span class="normal"> 703</span>
<span class="normal"> 704</span>
<span class="normal"> 705</span>
<span class="normal"> 706</span>
<span class="normal"> 707</span>
<span class="normal"> 708</span>
<span class="normal"> 709</span>
<span class="normal"> 710</span>
<span class="normal"> 711</span>
<span class="normal"> 712</span>
<span class="normal"> 713</span>
<span class="normal"> 714</span>
<span class="normal"> 715</span>
<span class="normal"> 716</span>
<span class="normal"> 717</span>
<span class="normal"> 718</span>
<span class="normal"> 719</span>
<span class="normal"> 720</span>
<span class="normal"> 721</span>
<span class="normal"> 722</span>
<span class="normal"> 723</span>
<span class="normal"> 724</span>
<span class="normal"> 725</span>
<span class="normal"> 726</span>
<span class="normal"> 727</span>
<span class="normal"> 728</span>
<span class="normal"> 729</span>
<span class="normal"> 730</span>
<span class="normal"> 731</span>
<span class="normal"> 732</span>
<span class="normal"> 733</span>
<span class="normal"> 734</span>
<span class="normal"> 735</span>
<span class="normal"> 736</span>
<span class="normal"> 737</span>
<span class="normal"> 738</span>
<span class="normal"> 739</span>
<span class="normal"> 740</span>
<span class="normal"> 741</span>
<span class="normal"> 742</span>
<span class="normal"> 743</span>
<span class="normal"> 744</span>
<span class="normal"> 745</span>
<span class="normal"> 746</span>
<span class="normal"> 747</span>
<span class="normal"> 748</span>
<span class="normal"> 749</span>
<span class="normal"> 750</span>
<span class="normal"> 751</span>
<span class="normal"> 752</span>
<span class="normal"> 753</span>
<span class="normal"> 754</span>
<span class="normal"> 755</span>
<span class="normal"> 756</span>
<span class="normal"> 757</span>
<span class="normal"> 758</span>
<span class="normal"> 759</span>
<span class="normal"> 760</span>
<span class="normal"> 761</span>
<span class="normal"> 762</span>
<span class="normal"> 763</span>
<span class="normal"> 764</span>
<span class="normal"> 765</span>
<span class="normal"> 766</span>
<span class="normal"> 767</span>
<span class="normal"> 768</span>
<span class="normal"> 769</span>
<span class="normal"> 770</span>
<span class="normal"> 771</span>
<span class="normal"> 772</span>
<span class="normal"> 773</span>
<span class="normal"> 774</span>
<span class="normal"> 775</span>
<span class="normal"> 776</span>
<span class="normal"> 777</span>
<span class="normal"> 778</span>
<span class="normal"> 779</span>
<span class="normal"> 780</span>
<span class="normal"> 781</span>
<span class="normal"> 782</span>
<span class="normal"> 783</span>
<span class="normal"> 784</span>
<span class="normal"> 785</span>
<span class="normal"> 786</span>
<span class="normal"> 787</span>
<span class="normal"> 788</span>
<span class="normal"> 789</span>
<span class="normal"> 790</span>
<span class="normal"> 791</span>
<span class="normal"> 792</span>
<span class="normal"> 793</span>
<span class="normal"> 794</span>
<span class="normal"> 795</span>
<span class="normal"> 796</span>
<span class="normal"> 797</span>
<span class="normal"> 798</span>
<span class="normal"> 799</span>
<span class="normal"> 800</span>
<span class="normal"> 801</span>
<span class="normal"> 802</span>
<span class="normal"> 803</span>
<span class="normal"> 804</span>
<span class="normal"> 805</span>
<span class="normal"> 806</span>
<span class="normal"> 807</span>
<span class="normal"> 808</span>
<span class="normal"> 809</span>
<span class="normal"> 810</span>
<span class="normal"> 811</span>
<span class="normal"> 812</span>
<span class="normal"> 813</span>
<span class="normal"> 814</span>
<span class="normal"> 815</span>
<span class="normal"> 816</span>
<span class="normal"> 817</span>
<span class="normal"> 818</span>
<span class="normal"> 819</span>
<span class="normal"> 820</span>
<span class="normal"> 821</span>
<span class="normal"> 822</span>
<span class="normal"> 823</span>
<span class="normal"> 824</span>
<span class="normal"> 825</span>
<span class="normal"> 826</span>
<span class="normal"> 827</span>
<span class="normal"> 828</span>
<span class="normal"> 829</span>
<span class="normal"> 830</span>
<span class="normal"> 831</span>
<span class="normal"> 832</span>
<span class="normal"> 833</span>
<span class="normal"> 834</span>
<span class="normal"> 835</span>
<span class="normal"> 836</span>
<span class="normal"> 837</span>
<span class="normal"> 838</span>
<span class="normal"> 839</span>
<span class="normal"> 840</span>
<span class="normal"> 841</span>
<span class="normal"> 842</span>
<span class="normal"> 843</span>
<span class="normal"> 844</span>
<span class="normal"> 845</span>
<span class="normal"> 846</span>
<span class="normal"> 847</span>
<span class="normal"> 848</span>
<span class="normal"> 849</span>
<span class="normal"> 850</span>
<span class="normal"> 851</span>
<span class="normal"> 852</span>
<span class="normal"> 853</span>
<span class="normal"> 854</span>
<span class="normal"> 855</span>
<span class="normal"> 856</span>
<span class="normal"> 857</span>
<span class="normal"> 858</span>
<span class="normal"> 859</span>
<span class="normal"> 860</span>
<span class="normal"> 861</span>
<span class="normal"> 862</span>
<span class="normal"> 863</span>
<span class="normal"> 864</span>
<span class="normal"> 865</span>
<span class="normal"> 866</span>
<span class="normal"> 867</span>
<span class="normal"> 868</span>
<span class="normal"> 869</span>
<span class="normal"> 870</span>
<span class="normal"> 871</span>
<span class="normal"> 872</span>
<span class="normal"> 873</span>
<span class="normal"> 874</span>
<span class="normal"> 875</span>
<span class="normal"> 876</span>
<span class="normal"> 877</span>
<span class="normal"> 878</span>
<span class="normal"> 879</span>
<span class="normal"> 880</span>
<span class="normal"> 881</span>
<span class="normal"> 882</span>
<span class="normal"> 883</span>
<span class="normal"> 884</span>
<span class="normal"> 885</span>
<span class="normal"> 886</span>
<span class="normal"> 887</span>
<span class="normal"> 888</span>
<span class="normal"> 889</span>
<span class="normal"> 890</span>
<span class="normal"> 891</span>
<span class="normal"> 892</span>
<span class="normal"> 893</span>
<span class="normal"> 894</span>
<span class="normal"> 895</span>
<span class="normal"> 896</span>
<span class="normal"> 897</span>
<span class="normal"> 898</span>
<span class="normal"> 899</span>
<span class="normal"> 900</span>
<span class="normal"> 901</span>
<span class="normal"> 902</span>
<span class="normal"> 903</span>
<span class="normal"> 904</span>
<span class="normal"> 905</span>
<span class="normal"> 906</span>
<span class="normal"> 907</span>
<span class="normal"> 908</span>
<span class="normal"> 909</span>
<span class="normal"> 910</span>
<span class="normal"> 911</span>
<span class="normal"> 912</span>
<span class="normal"> 913</span>
<span class="normal"> 914</span>
<span class="normal"> 915</span>
<span class="normal"> 916</span>
<span class="normal"> 917</span>
<span class="normal"> 918</span>
<span class="normal"> 919</span>
<span class="normal"> 920</span>
<span class="normal"> 921</span>
<span class="normal"> 922</span>
<span class="normal"> 923</span>
<span class="normal"> 924</span>
<span class="normal"> 925</span>
<span class="normal"> 926</span>
<span class="normal"> 927</span>
<span class="normal"> 928</span>
<span class="normal"> 929</span>
<span class="normal"> 930</span>
<span class="normal"> 931</span>
<span class="normal"> 932</span>
<span class="normal"> 933</span>
<span class="normal"> 934</span>
<span class="normal"> 935</span>
<span class="normal"> 936</span>
<span class="normal"> 937</span>
<span class="normal"> 938</span>
<span class="normal"> 939</span>
<span class="normal"> 940</span>
<span class="normal"> 941</span>
<span class="normal"> 942</span>
<span class="normal"> 943</span>
<span class="normal"> 944</span>
<span class="normal"> 945</span>
<span class="normal"> 946</span>
<span class="normal"> 947</span>
<span class="normal"> 948</span>
<span class="normal"> 949</span>
<span class="normal"> 950</span>
<span class="normal"> 951</span>
<span class="normal"> 952</span>
<span class="normal"> 953</span>
<span class="normal"> 954</span>
<span class="normal"> 955</span>
<span class="normal"> 956</span>
<span class="normal"> 957</span>
<span class="normal"> 958</span>
<span class="normal"> 959</span>
<span class="normal"> 960</span>
<span class="normal"> 961</span>
<span class="normal"> 962</span>
<span class="normal"> 963</span>
<span class="normal"> 964</span>
<span class="normal"> 965</span>
<span class="normal"> 966</span>
<span class="normal"> 967</span>
<span class="normal"> 968</span>
<span class="normal"> 969</span>
<span class="normal"> 970</span>
<span class="normal"> 971</span>
<span class="normal"> 972</span>
<span class="normal"> 973</span>
<span class="normal"> 974</span>
<span class="normal"> 975</span>
<span class="normal"> 976</span>
<span class="normal"> 977</span>
<span class="normal"> 978</span>
<span class="normal"> 979</span>
<span class="normal"> 980</span>
<span class="normal"> 981</span>
<span class="normal"> 982</span>
<span class="normal"> 983</span>
<span class="normal"> 984</span>
<span class="normal"> 985</span>
<span class="normal"> 986</span>
<span class="normal"> 987</span>
<span class="normal"> 988</span>
<span class="normal"> 989</span>
<span class="normal"> 990</span>
<span class="normal"> 991</span>
<span class="normal"> 992</span>
<span class="normal"> 993</span>
<span class="normal"> 994</span>
<span class="normal"> 995</span>
<span class="normal"> 996</span>
<span class="normal"> 997</span>
<span class="normal"> 998</span>
<span class="normal"> 999</span>
<span class="normal">1000</span>
<span class="normal">1001</span>
<span class="normal">1002</span>
<span class="normal">1003</span>
<span class="normal">1004</span>
<span class="normal">1005</span>
<span class="normal">1006</span>
<span class="normal">1007</span>
<span class="normal">1008</span>
<span class="normal">1009</span>
<span class="normal">1010</span>
<span class="normal">1011</span>
<span class="normal">1012</span>
<span class="normal">1013</span>
<span class="normal">1014</span>
<span class="normal">1015</span>
<span class="normal">1016</span>
<span class="normal">1017</span>
<span class="normal">1018</span>
<span class="normal">1019</span>
<span class="normal">1020</span>
<span class="normal">1021</span>
<span class="normal">1022</span>
<span class="normal">1023</span>
<span class="normal">1024</span>
<span class="normal">1025</span>
<span class="normal">1026</span>
<span class="normal">1027</span>
<span class="normal">1028</span>
<span class="normal">1029</span>
<span class="normal">1030</span>
<span class="normal">1031</span>
<span class="normal">1032</span>
<span class="normal">1033</span>
<span class="normal">1034</span>
<span class="normal">1035</span>
<span class="normal">1036</span>
<span class="normal">1037</span>
<span class="normal">1038</span>
<span class="normal">1039</span>
<span class="normal">1040</span>
<span class="normal">1041</span>
<span class="normal">1042</span>
<span class="normal">1043</span>
<span class="normal">1044</span>
<span class="normal">1045</span>
<span class="normal">1046</span>
<span class="normal">1047</span>
<span class="normal">1048</span>
<span class="normal">1049</span>
<span class="normal">1050</span>
<span class="normal">1051</span>
<span class="normal">1052</span>
<span class="normal">1053</span>
<span class="normal">1054</span>
<span class="normal">1055</span>
<span class="normal">1056</span>
<span class="normal">1057</span>
<span class="normal">1058</span>
<span class="normal">1059</span>
<span class="normal">1060</span>
<span class="normal">1061</span>
<span class="normal">1062</span>
<span class="normal">1063</span>
<span class="normal">1064</span>
<span class="normal">1065</span>
<span class="normal">1066</span>
<span class="normal">1067</span>
<span class="normal">1068</span>
<span class="normal">1069</span>
<span class="normal">1070</span>
<span class="normal">1071</span>
<span class="normal">1072</span>
<span class="normal">1073</span>
<span class="normal">1074</span>
<span class="normal">1075</span>
<span class="normal">1076</span>
<span class="normal">1077</span>
<span class="normal">1078</span>
<span class="normal">1079</span>
<span class="normal">1080</span>
<span class="normal">1081</span>
<span class="normal">1082</span>
<span class="normal">1083</span>
<span class="normal">1084</span>
<span class="normal">1085</span>
<span class="normal">1086</span>
<span class="normal">1087</span>
<span class="normal">1088</span>
<span class="normal">1089</span>
<span class="normal">1090</span>
<span class="normal">1091</span>
<span class="normal">1092</span>
<span class="normal">1093</span>
<span class="normal">1094</span>
<span class="normal">1095</span>
<span class="normal">1096</span>
<span class="normal">1097</span>
<span class="normal">1098</span>
<span class="normal">1099</span>
<span class="normal">1100</span>
<span class="normal">1101</span>
<span class="normal">1102</span>
<span class="normal">1103</span>
<span class="normal">1104</span>
<span class="normal">1105</span>
<span class="normal">1106</span>
<span class="normal">1107</span>
<span class="normal">1108</span>
<span class="normal">1109</span>
<span class="normal">1110</span>
<span class="normal">1111</span>
<span class="normal">1112</span>
<span class="normal">1113</span>
<span class="normal">1114</span>
<span class="normal">1115</span>
<span class="normal">1116</span>
<span class="normal">1117</span>
<span class="normal">1118</span>
<span class="normal">1119</span>
<span class="normal">1120</span>
<span class="normal">1121</span>
<span class="normal">1122</span>
<span class="normal">1123</span>
<span class="normal">1124</span>
<span class="normal">1125</span>
<span class="normal">1126</span>
<span class="normal">1127</span>
<span class="normal">1128</span>
<span class="normal">1129</span>
<span class="normal">1130</span>
<span class="normal">1131</span>
<span class="normal">1132</span>
<span class="normal">1133</span>
<span class="normal">1134</span>
<span class="normal">1135</span>
<span class="normal">1136</span>
<span class="normal">1137</span>
<span class="normal">1138</span>
<span class="normal">1139</span>
<span class="normal">1140</span>
<span class="normal">1141</span>
<span class="normal">1142</span>
<span class="normal">1143</span>
<span class="normal">1144</span>
<span class="normal">1145</span>
<span class="normal">1146</span>
<span class="normal">1147</span>
<span class="normal">1148</span>
<span class="normal">1149</span>
<span class="normal">1150</span>
<span class="normal">1151</span>
<span class="normal">1152</span>
<span class="normal">1153</span>
<span class="normal">1154</span>
<span class="normal">1155</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QdrantVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Qdrant Vector Store.</span>

<span class="sd">    In this vector store, embeddings and docs are stored within a</span>
<span class="sd">    Qdrant collection.</span>

<span class="sd">    During query time, the index uses Qdrant to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        collection_name: (str): name of the Qdrant collection</span>
<span class="sd">        client (Optional[Any]): QdrantClient instance from `qdrant-client` package</span>
<span class="sd">        aclient (Optional[Any]): AsyncQdrantClient instance from `qdrant-client` package</span>
<span class="sd">        url (Optional[str]): url of the Qdrant instance</span>
<span class="sd">        api_key (Optional[str]): API key for authenticating with Qdrant</span>
<span class="sd">        batch_size (int): number of points to upload in a single request to Qdrant. Defaults to 64</span>
<span class="sd">        parallel (int): number of parallel processes to use during upload. Defaults to 1</span>
<span class="sd">        max_retries (int): maximum number of retries in case of a failure. Defaults to 3</span>
<span class="sd">        client_kwargs (Optional[dict]): additional kwargs for QdrantClient and AsyncQdrantClient</span>
<span class="sd">        enable_hybrid (bool): whether to enable hybrid search using dense and sparse vectors</span>
<span class="sd">        fastembed_sparse_model (Optional[str]): name of the FastEmbed sparse model to use, if any</span>
<span class="sd">        sparse_doc_fn (Optional[SparseEncoderCallable]): function to encode sparse vectors</span>
<span class="sd">        sparse_query_fn (Optional[SparseEncoderCallable]): function to encode sparse queries</span>
<span class="sd">        hybrid_fusion_fn (Optional[HybridFusionCallable]): function to fuse hybrid search results</span>
<span class="sd">        index_doc_id (bool): whether to create a payload index for the document ID. Defaults to True</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-qdrant`</span>

<span class="sd">        ```python</span>
<span class="sd">        import qdrant_client</span>
<span class="sd">        from llama_index.vector_stores.qdrant import QdrantVectorStore</span>

<span class="sd">        client = qdrant_client.QdrantClient()</span>

<span class="sd">        vector_store = QdrantVectorStore(</span>
<span class="sd">            collection_name="example_collection", client=client</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">parallel</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">client_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>
    <span class="n">enable_hybrid</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">index_doc_id</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">fastembed_sparse_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">qdrant_client</span><span class="o">.</span><span class="n">QdrantClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_aclient</span><span class="p">:</span> <span class="n">qdrant_client</span><span class="o">.</span><span class="n">AsyncQdrantClient</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection_initialized</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_sparse_doc_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_sparse_query_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_hybrid_fusion_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">HybridFusionCallable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_dense_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">rest</span><span class="o">.</span><span class="n">VectorParams</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_sparse_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">rest</span><span class="o">.</span><span class="n">SparseVectorParams</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aclient</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">64</span><span class="p">,</span>
        <span class="n">parallel</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">client_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">dense_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">rest</span><span class="o">.</span><span class="n">VectorParams</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sparse_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">rest</span><span class="o">.</span><span class="n">SparseVectorParams</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">enable_hybrid</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">fastembed_sparse_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sparse_doc_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sparse_query_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">hybrid_fusion_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">HybridFusionCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_doc_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">client</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">and</span> <span class="n">aclient</span> <span class="ow">is</span> <span class="kc">None</span>
            <span class="ow">and</span> <span class="p">(</span><span class="n">url</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">collection_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span>
        <span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Must provide either a QdrantClient instance or a url and api_key."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">client</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">aclient</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">client_kwargs</span> <span class="o">=</span> <span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">qdrant_client</span><span class="o">.</span><span class="n">QdrantClient</span><span class="p">(</span>
                <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="o">**</span><span class="n">client_kwargs</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="o">=</span> <span class="n">qdrant_client</span><span class="o">.</span><span class="n">AsyncQdrantClient</span><span class="p">(</span>
                <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="o">**</span><span class="n">client_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">aclient</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                    <span class="s2">"Both client and aclient are provided. If using `:memory:` "</span>
                    <span class="s2">"mode, the data between clients is not synced."</span>
                <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span> <span class="o">=</span> <span class="n">aclient</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection_initialized</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection_exists</span><span class="p">(</span><span class="n">collection_name</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1">#  need to do lazy init for async clients</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection_initialized</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="c1"># setup hybrid search if enabled</span>
        <span class="k">if</span> <span class="n">enable_hybrid</span> <span class="ow">or</span> <span class="n">fastembed_sparse_model</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">enable_hybrid</span> <span class="o">=</span> <span class="kc">True</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_doc_fn</span> <span class="o">=</span> <span class="n">sparse_doc_fn</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_default_sparse_doc_encoder</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="p">,</span> <span class="n">fastembed_sparse_model</span><span class="o">=</span><span class="n">fastembed_sparse_model</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_query_fn</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">sparse_query_fn</span>
                <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_default_sparse_query_encoder</span><span class="p">(</span>
                    <span class="n">collection_name</span><span class="p">,</span> <span class="n">fastembed_sparse_model</span><span class="o">=</span><span class="n">fastembed_sparse_model</span>
                <span class="p">)</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="o">=</span> <span class="n">hybrid_fusion_fn</span> <span class="ow">or</span> <span class="n">cast</span><span class="p">(</span>
                <span class="n">HybridFusionCallable</span><span class="p">,</span> <span class="n">relative_score_fusion</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_config</span> <span class="o">=</span> <span class="n">sparse_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_dense_config</span> <span class="o">=</span> <span class="n">dense_config</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">parallel</span><span class="o">=</span><span class="n">parallel</span><span class="p">,</span>
            <span class="n">max_retries</span><span class="o">=</span><span class="n">max_retries</span><span class="p">,</span>
            <span class="n">client_kwargs</span><span class="o">=</span><span class="n">client_kwargs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">enable_hybrid</span><span class="o">=</span><span class="n">enable_hybrid</span><span class="p">,</span>
            <span class="n">index_doc_id</span><span class="o">=</span><span class="n">index_doc_id</span><span class="p">,</span>
            <span class="n">fastembed_sparse_model</span><span class="o">=</span><span class="n">fastembed_sparse_model</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"QdrantVectorStore"</span>

    <span class="k">def</span> <span class="nf">set_query_functions</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">sparse_doc_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sparse_query_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SparseEncoderCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">hybrid_fusion_fn</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">HybridFusionCallable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_doc_fn</span> <span class="o">=</span> <span class="n">sparse_doc_fn</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_query_fn</span> <span class="o">=</span> <span class="n">sparse_query_fn</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="o">=</span> <span class="n">hybrid_fusion_fn</span>

    <span class="k">def</span> <span class="nf">_build_points</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="n">sparse_vector_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">points</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
            <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">vectors</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">sparse_vectors</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">sparse_indices</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">payloads</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_doc_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">sparse_indices</span><span class="p">,</span> <span class="n">sparse_vectors</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_doc_fn</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span>
                        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_batch</span>
                    <span class="p">],</span>
                <span class="p">)</span>

            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">node_batch</span><span class="p">):</span>
                <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">)</span>
                <span class="n">node_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
                    <span class="k">if</span> <span class="p">(</span>
                        <span class="nb">len</span><span class="p">(</span><span class="n">sparse_vectors</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
                        <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">sparse_indices</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
                        <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">sparse_vectors</span><span class="p">)</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Hybrid search is not enabled. Please build the query with "</span>
                <span class="s2">"`enable_hybrid=True` in the constructor."</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="mi">2</span>
            <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

            <span class="c1"># flatten the response</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
                <span class="c1"># NOTE: only for hybrid search (0 for sparse search, 1 for dense search)</span>
                <span class="n">alpha</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">or</span> <span class="mf">0.5</span><span class="p">,</span>
                <span class="c1"># NOTE: use hybrid_top_k if provided, otherwise use similarity_top_k</span>
                <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Hybrid search is not enabled. Please build the query with "</span>
                <span class="s2">"`enable_hybrid=True` in the constructor."</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="mi">2</span>
            <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

            <span class="c1"># flatten the response</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
                <span class="n">alpha</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">or</span> <span class="mf">0.5</span><span class="p">,</span>
                <span class="c1"># NOTE: use hybrid_top_k if provided, otherwise use similarity_top_k</span>
                <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">EQ</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span>
                    <span class="n">conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">FieldCondition</span><span class="p">(</span>
                            <span class="n">key</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span>
                            <span class="nb">range</span><span class="o">=</span><span class="n">Range</span><span class="p">(</span>
                                <span class="n">gte</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
                                <span class="n">lte</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
                            <span class="p">),</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">FieldCondition</span><span class="p">(</span>
                            <span class="n">key</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span>
                            <span class="n">match</span><span class="o">=</span><span class="n">MatchValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">),</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
            <span class="k">elif</span> <span class="n">subfilter</span><span class="o">.</span><span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">GT</span><span class="p">:</span>
                <span class="n">conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">FieldCondition</span><span class="p">(</span>
                        <span class="n">key</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span>
                        <span class="nb">range</span><span class="o">=</span><span class="n">Range</span><span class="p">(</span><span class="n">gt</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">subfilter</span><span class="o">.</span><span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">LTE</span><span class="p">:</span>
                <span class="n">conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">FieldCondition</span><span class="p">(</span>
                        <span class="n">key</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span>
                        <span class="nb">range</span><span class="o">=</span><span class="n">Range</span><span class="p">(</span><span class="n">lte</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">subfilter</span><span class="o">.</span><span class="n">operator</span> <span class="o"></span> <span class="n">FilterOperator</span><span class="o">.</span><span class="n">NE</span><span class="p">:</span>
                <span class="n">conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">FieldCondition</span><span class="p">(</span>
                        <span class="n">key</span><span class="o">=</span><span class="n">subfilter</span><span class="o">.</span><span class="n">key</span><span class="p">,</span>
                        <span class="n">match</span><span class="o">=</span><span class="n">MatchExcept</span><span class="p">(</span><span class="o">**</span><span class="p">{</span><span class="s2">"except"</span><span class="p">:</span> <span class="p">[</span><span class="n">subfilter</span><span class="o">.</span><span class="n">value</span><span class="p">]}),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">subfilter</span><span class="o">.</span><span class="n">operator</span> <span class="o"></span> <span class="n">FilterCondition</span><span class="o">.</span><span class="n">AND</span><span class="p">:</span>
            <span class="nb">filter</span><span class="o">.</span><span class="n">must</span> <span class="o">=</span> <span class="n">conditions</span>
        <span class="k">elif</span> <span class="n">filters</span><span class="o">.</span><span class="n">condition</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Hybrid search is not enabled. Please build the query with "</span>
            <span class="s2">"`enable_hybrid=True` in the constructor."</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="mi">2</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="c1"># flatten the response</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
            <span class="c1"># NOTE: only for hybrid search (0 for sparse search, 1 for dense search)</span>
            <span class="n">alpha</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">or</span> <span class="mf">0.5</span><span class="p">,</span>
            <span class="c1"># NOTE: use hybrid_top_k if provided, otherwise use similarity_top_k</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
            <span class="s2">"Hybrid search is not enabled. Please build the query with "</span>
            <span class="s2">"`enable_hybrid=True` in the constructor."</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="mi">2</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

        <span class="c1"># flatten the response</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hybrid_fusion_fn</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
            <span class="n">alpha</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">or</span> <span class="mf">0.5</span><span class="p">,</span>
            <span class="c1"># NOTE: use hybrid_top_k if provided, otherwise use similarity_top_k</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">hybrid_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o">==</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">SPARSE</span>
        <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span>
        <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_query_fn</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="n">sparse_indices</span><span class="p">,</span> <span class="n">sparse_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_query_fn</span><span class="p">(</span>
            <span class="p">[</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">sparse_top_k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">sparse_top_k</span> <span class="ow">or</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

        <span class="n">sparse_response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">search_batch</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">requests</span><span class="o">=</span><span class="p">[</span>
                <span class="n">rest</span><span class="o">.</span><span class="n">SearchRequest</span><span class="p">(</span>
                    <span class="n">vector</span><span class="o">=</span><span class="n">rest</span><span class="o">.</span><span class="n">NamedSparseVector</span><span class="p">(</span>
                        <span class="c1"># Dynamically switch between the old and new sparse vector name</span>
                        <span class="n">name</span><span class="o">=</span><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">asparse_vector_name</span><span class="p">(),</span>
                        <span class="n">vector</span><span class="o">=</span><span class="n">rest</span><span class="o">.</span><span class="n">SparseVector</span><span class="p">(</span>
                            <span class="n">indices</span><span class="o">=</span><span class="n">sparse_indices</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                            <span class="n">values</span><span class="o">=</span><span class="n">sparse_embedding</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
                        <span class="p">),</span>
                    <span class="p">),</span>
                    <span class="n">limit</span><span class="o">=</span><span class="n">sparse_top_k</span><span class="p">,</span>
                    <span class="nb">filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span>
                    <span class="n">with_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">sparse_response</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">enable_hybrid</span><span class="p">:</span>
        <span class="c1"># search for dense vectors only</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">search_batch</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">requests</span><span class="o">=</span><span class="p">[</span>
                <span class="n">rest</span><span class="o">.</span><span class="n">SearchRequest</span><span class="p">(</span>
                    <span class="n">vector</span><span class="o">=</span><span class="n">rest</span><span class="o">.</span><span class="n">NamedVector</span><span class="p">(</span>
                        <span class="n">name</span><span class="o">=</span><span class="n">DENSE_VECTOR_NAME</span><span class="p">,</span>
                        <span class="n">vector</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                    <span class="nb">filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span>
                    <span class="n">with_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">response</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aclient</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">query_vector</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">query_filter</span><span class="o">=</span><span class="n">query_filter</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_to_query_result</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### parse\_to\_query\_result [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/#llama_index.vector_stores.qdrant.QdrantVectorStore.parse_to_query_result "Permanent link")

```
parse_to_query_result(response: List[Any]) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Convert vector store response to VectorStoreQueryResult.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `response` | `List[Any]` | 
List\[Any\]: List of results returned from the vector store.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-qdrant/llama_index/vector_stores/qdrant/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">945</span>
<span class="normal">946</span>
<span class="normal">947</span>
<span class="normal">948</span>
<span class="normal">949</span>
<span class="normal">950</span>
<span class="normal">951</span>
<span class="normal">952</span>
<span class="normal">953</span>
<span class="normal">954</span>
<span class="normal">955</span>
<span class="normal">956</span>
<span class="normal">957</span>
<span class="normal">958</span>
<span class="normal">959</span>
<span class="normal">960</span>
<span class="normal">961</span>
<span class="normal">962</span>
<span class="normal">963</span>
<span class="normal">964</span>
<span class="normal">965</span>
<span class="normal">966</span>
<span class="normal">967</span>
<span class="normal">968</span>
<span class="normal">969</span>
<span class="normal">970</span>
<span class="normal">971</span>
<span class="normal">972</span>
<span class="normal">973</span>
<span class="normal">974</span>
<span class="normal">975</span>
<span class="normal">976</span>
<span class="normal">977</span>
<span class="normal">978</span>
<span class="normal">979</span>
<span class="normal">980</span>
<span class="normal">981</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse_to_query_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Convert vector store response to VectorStoreQueryResult.</span>

<span class="sd">    Args:</span>
<span class="sd">        response: List[Any]: List of results returned from the vector store.</span>
<span class="sd">    """</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="n">payload</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Payload</span><span class="p">,</span> <span class="n">point</span><span class="o">.</span><span class="n">payload</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">payload</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                <span class="n">payload</span>
            <span class="p">)</span>

            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">id_</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">id</span><span class="p">),</span>
                <span class="n">text</span><span class="o">=</span><span class="n">payload</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"text"</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">id</span><span class="p">))</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
            <span class="c1"># certain requests do not return a score</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mf">1.0</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/)[Next Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/redis/)
