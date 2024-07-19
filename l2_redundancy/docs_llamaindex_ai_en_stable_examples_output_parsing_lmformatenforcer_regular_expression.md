Title: LM Format Enforcer Regular Expression Generation

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_regular_expressions/

Markdown Content:
LM Format Enforcer Regular Expression Generation - LlamaIndex


Generate structured data with [**lm-format-enforcer**](https://github.com/noamgat/lm-format-enforcer) via LlamaIndex.

With lm-format-enforcer, you can guarantee the output structure is correct by _forcing_ the LLM to output desired tokens.  
This is especialy helpful when you are using lower-capacity model (e.g. the current open source models), which otherwise would struggle to generate valid output that fits the desired output schema.

[lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) supports regular expressions and JSON Schema, this demo focuses on regular expressions. For JSON Schema + Pydantic, see the [sample Pydantic program notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/output_parsing/lmformatenforcer_pydantic_program.ipynb).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-llama\-cpp

%pip install llama-index-llms-llama-cpp

In \[ \]:

Copied!

!pip install llama\-index lm\-format\-enforcer llama\-cpp\-python

!pip install llama-index lm-format-enforcer llama-cpp-python

In \[ \]:

Copied!

import lmformatenforcer
import re

from llama\_index.core.prompts.lmformatenforcer\_utils import (
    activate\_lm\_format\_enforcer,
    build\_lm\_format\_enforcer\_function,
)

import lmformatenforcer import re from llama\_index.core.prompts.lmformatenforcer\_utils import ( activate\_lm\_format\_enforcer, build\_lm\_format\_enforcer\_function, )

Define output format

In \[ \]:

Copied!

regex \= r'"Hello, my name is (?P<name>\[a-zA-Z\]\*)\\. I was born in (?P<hometown>\[a-zA-Z\]\*). Nice to meet you!"'

regex = r'"Hello, my name is (?P\[a-zA-Z\]\*)\\. I was born in (?P\[a-zA-Z\]\*). Nice to meet you!"'

Create the model. We use `LlamaCPP` as the LLM in this demo, but `HuggingFaceLLM` is also supported.

In \[ \]:

Copied!

from llama\_index.llms.llama\_cpp import LlamaCPP

llm \= LlamaCPP()

from llama\_index.llms.llama\_cpp import LlamaCPP llm = LlamaCPP()

llama\_model\_loader: loaded meta data with 19 key-value pairs and 363 tensors from /mnt/wsl/PHYSICALDRIVE1p3/llama\_index/models/llama-2-13b-chat.Q4\_0.gguf (version GGUF V2 (latest))
llama\_model\_loader: - tensor    0:                token\_embd.weight q4\_0     \[  5120, 32000,     1,     1 \]
llama\_model\_loader: - tensor    1:           blk.0.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor    2:            blk.0.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor    3:            blk.0.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor    4:              blk.0.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor    5:            blk.0.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor    6:              blk.0.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor    7:         blk.0.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor    8:              blk.0.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor    9:              blk.0.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   10:           blk.1.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   11:            blk.1.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   12:            blk.1.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   13:              blk.1.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   14:            blk.1.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   15:              blk.1.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   16:         blk.1.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   17:              blk.1.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   18:              blk.1.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   19:          blk.10.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   20:           blk.10.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   21:           blk.10.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   22:             blk.10.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   23:           blk.10.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   24:             blk.10.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   25:        blk.10.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   26:             blk.10.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   27:             blk.10.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   28:          blk.11.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   29:           blk.11.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   30:           blk.11.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   31:             blk.11.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   32:           blk.11.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   33:             blk.11.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   34:        blk.11.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   35:             blk.11.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   36:             blk.11.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   37:          blk.12.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   38:           blk.12.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   39:           blk.12.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   40:             blk.12.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   41:           blk.12.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   42:             blk.12.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   43:        blk.12.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   44:             blk.12.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   45:             blk.12.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   46:          blk.13.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   47:           blk.13.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   48:           blk.13.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   49:             blk.13.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   50:           blk.13.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   51:             blk.13.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   52:        blk.13.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   53:             blk.13.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   54:             blk.13.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   55:          blk.14.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   56:           blk.14.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   57:           blk.14.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   58:             blk.14.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   59:           blk.14.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   60:             blk.14.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   61:        blk.14.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   62:             blk.14.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   63:             blk.14.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   64:             blk.15.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   65:             blk.15.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   66:           blk.2.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   67:            blk.2.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   68:            blk.2.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   69:              blk.2.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   70:            blk.2.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   71:              blk.2.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   72:         blk.2.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   73:              blk.2.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   74:              blk.2.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   75:           blk.3.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   76:            blk.3.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   77:            blk.3.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   78:              blk.3.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   79:            blk.3.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   80:              blk.3.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   81:         blk.3.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   82:              blk.3.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   83:              blk.3.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   84:           blk.4.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   85:            blk.4.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   86:            blk.4.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   87:              blk.4.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   88:            blk.4.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   89:              blk.4.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   90:         blk.4.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   91:              blk.4.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   92:              blk.4.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   93:           blk.5.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   94:            blk.5.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor   95:            blk.5.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   96:              blk.5.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor   97:            blk.5.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor   98:              blk.5.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor   99:         blk.5.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  100:              blk.5.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  101:              blk.5.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  102:           blk.6.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  103:            blk.6.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  104:            blk.6.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  105:              blk.6.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  106:            blk.6.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  107:              blk.6.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  108:         blk.6.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  109:              blk.6.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  110:              blk.6.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  111:           blk.7.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  112:            blk.7.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  113:            blk.7.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  114:              blk.7.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  115:            blk.7.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  116:              blk.7.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  117:         blk.7.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  118:              blk.7.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  119:              blk.7.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  120:           blk.8.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  121:            blk.8.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  122:            blk.8.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  123:              blk.8.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  124:            blk.8.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  125:              blk.8.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  126:         blk.8.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  127:              blk.8.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  128:              blk.8.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  129:           blk.9.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  130:            blk.9.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  131:            blk.9.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  132:              blk.9.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  133:            blk.9.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  134:              blk.9.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  135:         blk.9.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  136:              blk.9.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  137:              blk.9.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  138:          blk.15.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  139:           blk.15.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  140:           blk.15.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  141:             blk.15.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  142:           blk.15.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  143:        blk.15.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  144:             blk.15.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  145:          blk.16.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  146:           blk.16.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  147:           blk.16.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  148:             blk.16.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  149:           blk.16.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  150:             blk.16.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  151:        blk.16.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  152:             blk.16.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  153:             blk.16.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  154:          blk.17.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  155:           blk.17.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  156:           blk.17.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  157:             blk.17.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  158:           blk.17.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  159:             blk.17.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  160:        blk.17.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  161:             blk.17.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  162:             blk.17.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  163:          blk.18.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  164:           blk.18.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  165:           blk.18.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  166:             blk.18.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  167:           blk.18.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  168:             blk.18.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  169:        blk.18.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  170:             blk.18.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  171:             blk.18.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  172:          blk.19.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  173:           blk.19.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  174:           blk.19.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  175:             blk.19.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  176:           blk.19.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  177:             blk.19.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  178:        blk.19.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  179:             blk.19.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  180:             blk.19.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  181:          blk.20.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  182:           blk.20.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  183:           blk.20.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  184:             blk.20.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  185:           blk.20.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  186:             blk.20.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  187:        blk.20.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  188:             blk.20.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  189:             blk.20.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  190:          blk.21.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  191:           blk.21.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  192:           blk.21.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  193:             blk.21.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  194:           blk.21.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  195:             blk.21.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  196:        blk.21.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  197:             blk.21.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  198:             blk.21.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  199:          blk.22.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  200:           blk.22.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  201:           blk.22.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  202:             blk.22.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  203:           blk.22.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  204:             blk.22.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  205:        blk.22.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  206:             blk.22.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  207:             blk.22.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  208:          blk.23.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  209:           blk.23.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  210:           blk.23.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  211:             blk.23.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  212:           blk.23.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  213:             blk.23.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  214:        blk.23.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  215:             blk.23.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  216:             blk.23.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  217:          blk.24.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  218:           blk.24.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  219:           blk.24.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  220:             blk.24.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  221:           blk.24.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  222:             blk.24.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  223:        blk.24.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  224:             blk.24.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  225:             blk.24.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  226:          blk.25.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  227:           blk.25.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  228:           blk.25.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  229:             blk.25.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  230:           blk.25.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  231:             blk.25.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  232:        blk.25.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  233:             blk.25.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  234:             blk.25.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  235:          blk.26.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  236:           blk.26.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  237:           blk.26.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  238:             blk.26.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  239:           blk.26.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  240:             blk.26.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  241:        blk.26.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  242:             blk.26.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  243:             blk.26.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  244:          blk.27.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  245:           blk.27.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  246:           blk.27.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  247:             blk.27.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  248:           blk.27.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  249:             blk.27.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  250:        blk.27.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  251:             blk.27.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  252:             blk.27.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  253:          blk.28.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  254:           blk.28.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  255:           blk.28.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  256:             blk.28.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  257:           blk.28.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  258:             blk.28.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  259:        blk.28.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  260:             blk.28.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  261:             blk.28.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  262:          blk.29.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  263:           blk.29.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  264:           blk.29.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  265:             blk.29.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  266:           blk.29.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  267:             blk.29.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  268:        blk.29.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  269:             blk.29.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  270:             blk.29.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  271:           blk.30.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  272:             blk.30.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  273:             blk.30.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  274:        blk.30.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  275:             blk.30.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  276:             blk.30.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  277:                    output.weight q6\_K     \[  5120, 32000,     1,     1 \]
llama\_model\_loader: - tensor  278:          blk.30.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  279:           blk.30.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  280:           blk.30.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  281:          blk.31.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  282:           blk.31.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  283:           blk.31.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  284:             blk.31.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  285:           blk.31.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  286:             blk.31.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  287:        blk.31.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  288:             blk.31.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  289:             blk.31.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  290:          blk.32.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  291:           blk.32.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  292:           blk.32.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  293:             blk.32.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  294:           blk.32.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  295:             blk.32.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  296:        blk.32.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  297:             blk.32.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  298:             blk.32.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  299:          blk.33.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  300:           blk.33.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  301:           blk.33.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  302:             blk.33.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  303:           blk.33.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  304:             blk.33.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  305:        blk.33.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  306:             blk.33.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  307:             blk.33.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  308:          blk.34.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  309:           blk.34.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  310:           blk.34.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  311:             blk.34.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  312:           blk.34.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  313:             blk.34.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  314:        blk.34.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  315:             blk.34.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  316:             blk.34.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  317:          blk.35.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  318:           blk.35.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  319:           blk.35.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  320:             blk.35.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  321:           blk.35.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  322:             blk.35.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  323:        blk.35.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  324:             blk.35.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  325:             blk.35.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  326:          blk.36.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  327:           blk.36.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  328:           blk.36.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  329:             blk.36.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  330:           blk.36.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  331:             blk.36.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  332:        blk.36.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  333:             blk.36.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  334:             blk.36.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  335:          blk.37.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  336:           blk.37.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  337:           blk.37.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  338:             blk.37.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  339:           blk.37.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  340:             blk.37.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  341:        blk.37.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  342:             blk.37.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  343:             blk.37.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  344:          blk.38.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  345:           blk.38.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  346:           blk.38.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  347:             blk.38.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  348:           blk.38.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  349:             blk.38.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  350:        blk.38.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  351:             blk.38.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  352:             blk.38.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  353:          blk.39.attn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  354:           blk.39.ffn\_down.weight q4\_0     \[ 13824,  5120,     1,     1 \]
llama\_model\_loader: - tensor  355:           blk.39.ffn\_gate.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  356:             blk.39.ffn\_up.weight q4\_0     \[  5120, 13824,     1,     1 \]
llama\_model\_loader: - tensor  357:           blk.39.ffn\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - tensor  358:             blk.39.attn\_k.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  359:        blk.39.attn\_output.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  360:             blk.39.attn\_q.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  361:             blk.39.attn\_v.weight q4\_0     \[  5120,  5120,     1,     1 \]
llama\_model\_loader: - tensor  362:               output\_norm.weight f32      \[  5120,     1,     1,     1 \]
llama\_model\_loader: - kv   0:                       general.architecture str     
llama\_model\_loader: - kv   1:                               general.name str     
llama\_model\_loader: - kv   2:                       llama.context\_length u32     
llama\_model\_loader: - kv   3:                     llama.embedding\_length u32     
llama\_model\_loader: - kv   4:                          llama.block\_count u32     
llama\_model\_loader: - kv   5:                  llama.feed\_forward\_length u32     
llama\_model\_loader: - kv   6:                 llama.rope.dimension\_count u32     
llama\_model\_loader: - kv   7:                 llama.attention.head\_count u32     
llama\_model\_loader: - kv   8:              llama.attention.head\_count\_kv u32     
llama\_model\_loader: - kv   9:     llama.attention.layer\_norm\_rms\_epsilon f32     
llama\_model\_loader: - kv  10:                          general.file\_type u32     
llama\_model\_loader: - kv  11:                       tokenizer.ggml.model str     
llama\_model\_loader: - kv  12:                      tokenizer.ggml.tokens arr     
llama\_model\_loader: - kv  13:                      tokenizer.ggml.scores arr     
llama\_model\_loader: - kv  14:                  tokenizer.ggml.token\_type arr     
llama\_model\_loader: - kv  15:                tokenizer.ggml.bos\_token\_id u32     
llama\_model\_loader: - kv  16:                tokenizer.ggml.eos\_token\_id u32     
llama\_model\_loader: - kv  17:            tokenizer.ggml.unknown\_token\_id u32     
llama\_model\_loader: - kv  18:               general.quantization\_version u32     
llama\_model\_loader: - type  f32:   81 tensors
llama\_model\_loader: - type q4\_0:  281 tensors
llama\_model\_loader: - type q6\_K:    1 tensors
llm\_load\_print\_meta: format           = GGUF V2 (latest)
llm\_load\_print\_meta: arch             = llama
llm\_load\_print\_meta: vocab type       = SPM
llm\_load\_print\_meta: n\_vocab          = 32000
llm\_load\_print\_meta: n\_merges         = 0
llm\_load\_print\_meta: n\_ctx\_train      = 4096
llm\_load\_print\_meta: n\_embd           = 5120
llm\_load\_print\_meta: n\_head           = 40
llm\_load\_print\_meta: n\_head\_kv        = 40
llm\_load\_print\_meta: n\_layer          = 40
llm\_load\_print\_meta: n\_rot            = 128
llm\_load\_print\_meta: n\_gqa            = 1
llm\_load\_print\_meta: f\_norm\_eps       = 0.0e+00
llm\_load\_print\_meta: f\_norm\_rms\_eps   = 1.0e-05
llm\_load\_print\_meta: n\_ff             = 13824
llm\_load\_print\_meta: freq\_base\_train  = 10000.0
llm\_load\_print\_meta: freq\_scale\_train = 1
llm\_load\_print\_meta: model type       = 13B
llm\_load\_print\_meta: model ftype      = mostly Q4\_0
llm\_load\_print\_meta: model params     = 13.02 B
llm\_load\_print\_meta: model size       = 6.86 GiB (4.53 BPW) 
llm\_load\_print\_meta: general.name   = LLaMA v2
llm\_load\_print\_meta: BOS token = 1 '<s>'
llm\_load\_print\_meta: EOS token = 2 '</s>'
llm\_load\_print\_meta: UNK token = 0 '<unk>'
llm\_load\_print\_meta: LF token  = 13 '<0x0A>'
llm\_load\_tensors: ggml ctx size =    0.12 MB
llm\_load\_tensors: mem required  = 7024.01 MB
...................................................................................................
llama\_new\_context\_with\_model: n\_ctx      = 3900
llama\_new\_context\_with\_model: freq\_base  = 10000.0
llama\_new\_context\_with\_model: freq\_scale = 1
llama\_new\_context\_with\_model: kv self size  = 3046.88 MB
llama\_new\_context\_with\_model: compute buffer total size = 348.18 MB
AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512\_VBMI = 0 | AVX512\_VNNI = 0 | FMA = 1 | NEON = 0 | ARM\_FMA = 0 | F16C = 1 | FP16\_VA = 0 | WASM\_SIMD = 0 | BLAS = 0 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | 

Activate the format enforcer and run the LLM get structured output in the desired regular expression format. As long as we are inside the `with activate_lm_format_enforcer(...)` block, the LLM will output the desired format.

If we would have used `lmformatenforcer.JsonSchemaParser` and a JSON schema, we would have gotten JSON output instead.

In \[ \]:

Copied!

regex\_parser \= lmformatenforcer.RegexParser(regex)
lm\_format\_enforcer\_fn \= build\_lm\_format\_enforcer\_function(llm, regex\_parser)
with activate\_lm\_format\_enforcer(llm, lm\_format\_enforcer\_fn):
    output \= llm.complete(
        "Here is a way to present myself, if my name was John and I born in Boston: "
    )

regex\_parser = lmformatenforcer.RegexParser(regex) lm\_format\_enforcer\_fn = build\_lm\_format\_enforcer\_function(llm, regex\_parser) with activate\_lm\_format\_enforcer(llm, lm\_format\_enforcer\_fn): output = llm.complete( "Here is a way to present myself, if my name was John and I born in Boston: " )

llama\_print\_timings:        load time =  2709.44 ms
llama\_print\_timings:      sample time =     7.26 ms /    22 runs   (    0.33 ms per token,  3031.56 tokens per second)
llama\_print\_timings: prompt eval time =  2709.40 ms /    21 tokens (  129.02 ms per token,     7.75 tokens per second)
llama\_print\_timings:        eval time =  3047.28 ms /    21 runs   (  145.11 ms per token,     6.89 tokens per second)
llama\_print\_timings:       total time =  5965.41 ms

The output is a string, according to the regular expression, which we can parse and extract parameters from.

In \[ \]:

Copied!

print(output)
print(re.match(regex, output.text).groupdict())

print(output) print(re.match(regex, output.text).groupdict())

"Hello, my name is John. I was born in Boston, Nice to meet you!"
{'name': 'John', 'hometown': 'Boston'}

Back to top

[Previous LM Format Enforcer Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_pydantic_program/)[Next OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)

Hi, how can I help you?

🦙
