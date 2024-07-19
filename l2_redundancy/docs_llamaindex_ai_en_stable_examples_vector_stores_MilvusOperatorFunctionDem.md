Title: MilvusOperatorFunctionDemo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/

Markdown Content:
MilvusOperatorFunctionDemo - LlamaIndex


       

How to use FilterOperatorFunctions for advanced scalar querying and complex query joins in Milvus[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#how-to-use-filteroperatorfunctions-for-advanced-scalar-querying-and-complex-query-joins-in-milvus)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The goal of this guide is to walk through the basics of how to utilize the LlamaIndex FilterOperatorFunctions to leverage the power of Milvus's advanced query cabability against hosted vector databases. For context on how these work, see Milvus's documentation:

1.  [Basic operators](https://docs.zilliz.com/docs/get-and-scalar-query#basic-operators)
2.  [JSON filtering](https://docs.zilliz.com/docs/use-json-fields)
3.  [Array filtering](https://docs.zilliz.com/docs/use-array-fields)

This guide assumes a few things:

1.  You have a provisioned Milvus collection loaded into and hosted on a vector database
2.  You are running this example locally and have access to environment variables

### Install Milvus and LlamaIndex dependencies[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#install-milvus-and-llamaindex-dependencies)

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-milvus

%pip install llama-index-vector-stores-milvus

In \[ \]:

Copied!

! pip install llama\-index

! pip install llama-index

### Build reused code[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#build-reused-code)

*   constants
*   function to demonstrate outputs

In \[ \]:

Copied!

from llama\_index.core.schema import QueryBundle

top\_k \= 5
key \= "product\_codes"

def retrieve\_and\_print\_results(retriever):
    query\_result \= retriever.retrieve(
        QueryBundle(
            query\_str\="Explain non-refoulement.", embedding\=\[0.0\] \* 3072
        )
    )
    for node in query\_result:
        print(
            f"node id\_: {node.id\_}\\nmetadata: \\n\\tchapter id: {node.metadata\['chapter\_id'\]}\\n\\t{key}: {node.metadata\[key\]}\\n"
        )

from llama\_index.core.schema import QueryBundle top\_k = 5 key = "product\_codes" def retrieve\_and\_print\_results(retriever): query\_result = retriever.retrieve( QueryBundle( query\_str="Explain non-refoulement.", embedding=\[0.0\] \* 3072 ) ) for node in query\_result: print( f"node id\_: {node.id\_}\\nmetadata: \\n\\tchapter id: {node.metadata\['chapter\_id'\]}\\n\\t{key}: {node.metadata\[key\]}\\n" )

### Load .env variables and build the VectorStore/Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#load-env-variables-and-build-the-vectorstoreindex)

Provide the path to the variables if necessary (i.e. if running in a forked local repository)

*   If you'd rather provide the uri, token and collection info manually, do that in the next step and ignore the load\_dotenv

In \[ \]:

Copied!

from dotenv import load\_dotenv

load\_dotenv("/path/to/your/.env")

from dotenv import load\_dotenv load\_dotenv("/path/to/your/.env")

In \[ \]:

Copied!

import os
from llama\_index.vector\_stores.milvus import MilvusVectorStore
from llama\_index.core import VectorStoreIndex

vector\_store \= MilvusVectorStore(
    overwrite\=False,
    uri\=os.getenv("MILVUS\_URI", "xxx"),
    token\=os.getenv("MILVUS\_TOKEN", "yyy"),
    collection\_name\=os.getenv("MILVUS\_COLLECTION", "zzz"),
)

index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)

import os from llama\_index.vector\_stores.milvus import MilvusVectorStore from llama\_index.core import VectorStoreIndex vector\_store = MilvusVectorStore( overwrite=False, uri=os.getenv("MILVUS\_URI", "xxx"), token=os.getenv("MILVUS\_TOKEN", "yyy"), collection\_name=os.getenv("MILVUS\_COLLECTION", "zzz"), ) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store)

### Run Queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#run-queries)

#### Using a FilterOperatorFunction[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#using-a-filteroperatorfunction)

Assume that there is a metadata field called "product\_codes" that contains an array of strings detailing certain product information. To filter the vector results down to only those tagged with "code4", use the `ARRAY_CONTAINS` function

Build the `ScalarMetadataFilter` and `ScalarMetadataFilters` objects

In \[ \]:

Copied!

from llama\_index.vector\_stores.milvus.utils import (
    ScalarMetadataFilters,
    ScalarMetadataFilter,
    FilterOperatorFunction,
)

array\_contains\_scalar\_filter \= ScalarMetadataFilter(
    key\=key, value\="code4", operator\=FilterOperatorFunction.ARRAY\_CONTAINS
)

scalar\_filters \= ScalarMetadataFilters(filters\=\[array\_contains\_scalar\_filter\])

retriever \= index.as\_retriever(
    vector\_store\_kwargs\={"milvus\_scalar\_filters": scalar\_filters.to\_dict()},
    similarity\_top\_k\=top\_k,
)

retrieve\_and\_print\_results(retriever)

from llama\_index.vector\_stores.milvus.utils import ( ScalarMetadataFilters, ScalarMetadataFilter, FilterOperatorFunction, ) array\_contains\_scalar\_filter = ScalarMetadataFilter( key=key, value="code4", operator=FilterOperatorFunction.ARRAY\_CONTAINS ) scalar\_filters = ScalarMetadataFilters(filters=\[array\_contains\_scalar\_filter\]) retriever = index.as\_retriever( vector\_store\_kwargs={"milvus\_scalar\_filters": scalar\_filters.to\_dict()}, similarity\_top\_k=top\_k, ) retrieve\_and\_print\_results(retriever)

#### Execute the query and print the relevant information[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#execute-the-query-and-print-the-relevant-information)

`ARRAY_CONTAINS(product_codes, "code4")`

Example output:

*   Only contains nodes with metadata that matches the ARRAY\_CONTAINS restriction

```
node id_: c_142236555_s_291254779-291254817
metadata: 
	chapter id: 142236555
	product_codes: ['code2', 'code9', 'code5', 'code4', 'code6']

node id_: c_440696406_s_440696822-440696847
metadata: 
	chapter id: 440696406
	product_codes: ['code3', 'code2', 'code1', 'code4', 'code9', 'code5']

node id_: c_440700190_s_440700206-440700218 
metadata: 
	chapter id: 440700190
	product_codes: ['code9', 'code7', 'code4', 'code2', 'code6']

node id_: c_440763876_s_440763935-440763942
metadata: 
	chapter id: 440763876
	product_codes: ['code4', 'code8', 'code10']

node id_: c_440885466_s_440885620-440885631
metadata: 
	chapter id: 440885466
	product_codes: ['code9', 'code5', 'code2', 'code4', 'code1']
```

#### Run a query using the FilterOperator.NIN enum to exclude some previous results[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#run-a-query-using-the-filteroperatornin-enum-to-exclude-some-previous-results)

`chapter_id not in [440885466, 440763876]`

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    MetadataFilters,
    MetadataFilter,
    FilterOperator,
)

not\_in\_metadata\_filter \= MetadataFilter(
    key\="chapter\_id", value\=\[440885466, 440763876\], operator\=FilterOperator.NIN
)

metadata\_filters \= MetadataFilters(filters\=\[not\_in\_metadata\_filter\])

retriever \= index.as\_retriever(
    filters\=metadata\_filters, similarity\_top\_k\=top\_k
)

retrieve\_and\_print\_results(retriever)

from llama\_index.core.vector\_stores import ( MetadataFilters, MetadataFilter, FilterOperator, ) not\_in\_metadata\_filter = MetadataFilter( key="chapter\_id", value=\[440885466, 440763876\], operator=FilterOperator.NIN ) metadata\_filters = MetadataFilters(filters=\[not\_in\_metadata\_filter\]) retriever = index.as\_retriever( filters=metadata\_filters, similarity\_top\_k=top\_k ) retrieve\_and\_print\_results(retriever)

Example output:

*   Doesn't contain chapter ids 440885466 or 440763876
*   Contains results with product codes we would've excluded in the first query

```
node id_: c_440769025_s_440769040-440769053
metadata: 
	chapter id: 440769025
	product_codes: ['code3']

node id_: c_441155692_s_441155856-441155752
metadata: 
	chapter id: 441155692
	product_codes: ['code9', 'code1']

node id_: c_142236555_s_291254779-291254817
metadata: 
	chapter id: 142236555
	product_codes: ['code2', 'code9', 'code5', 'code4', 'code6']

node id_: c_441156096_s_441156098-441156102
metadata: 
	chapter id: 441156096
	product_codes: ['code3', 'code8', 'code5']

node id_: c_444354779_s_444354787-444354792
metadata: 
	chapter id: 444354779
	product_codes: ['code3', 'code5', 'code10', 'code1']
```

#### Combine the two query conditions into a single query call[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/#combine-the-two-query-conditions-into-a-single-query-call)

`ARRAY_CONTAINS(product_codes, "code4") and chapter_id not in [440885466, 440763876]`

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    filters\=metadata\_filters,
    vector\_store\_kwargs\={"milvus\_scalar\_filters": scalar\_filters.to\_dict()},
    similarity\_top\_k\=top\_k,
)

retrieve\_and\_print\_results(retriever)

retriever = index.as\_retriever( filters=metadata\_filters, vector\_store\_kwargs={"milvus\_scalar\_filters": scalar\_filters.to\_dict()}, similarity\_top\_k=top\_k, ) retrieve\_and\_print\_results(retriever)

Example output:

*   Doesn't contain chapter ids 440885466 or 440763876
*   Only contains results that match the ARRAY\_CONTAINS restriction

```
node id_: c_142236555_s_291254779-291254817
metadata: 
	chapter id: 142236555
	product_codes['code2', 'code9', 'code5', 'code4', 'code6']

node id_: c_361386932_s_361386982-361387025
metadata: 
	chapter id: 361386932
	product_codes['code4']

node id_: c_361386932_s_361387000-361387179
metadata: 
	chapter id: 361386932
	product_codes['code4']

node id_: c_361386932_s_361387026-361387053
metadata: 
	chapter id: 361386932
	product_codes['code4']

node id_: c_361384286_s_361384359-361384367
metadata: 
	chapter id: 361384286
	product_codes['code4', 'code2', 'code9']
```

Back to top

[Previous Milvus Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)[Next MongoDBAtlasVectorSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)
