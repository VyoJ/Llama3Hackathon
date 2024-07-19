Title: OpenVINO LLMs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/openvino/

Markdown Content:
OpenVINO LLMs - LlamaIndex


[OpenVINO™](https://github.com/openvinotoolkit/openvino) is an open-source toolkit for optimizing and deploying AI inference. OpenVINO™ Runtime can enable running the same model optimized across various hardware [devices](https://github.com/openvinotoolkit/openvino?tab=readme-ov-file#supported-hardware-matrix). Accelerate your deep learning performance across use cases like: language + LLMs, computer vision, automatic speech recognition, and more.

OpenVINO models can be run locally through `OpenVINOLLM` entitiy wrapped by LlamaIndex :

In the below line, we install the packages necessary for this demo:

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openvino transformers huggingface\_hub

%pip install llama-index-llms-openvino transformers huggingface\_hub

Now that we're set up, let's play around:

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.llms.openvino import OpenVINOLLM

from llama\_index.llms.openvino import OpenVINOLLM

In \[ \]:

Copied!

def messages\_to\_prompt(messages):
    prompt \= ""
    for message in messages:
        if message.role \ "user":
            prompt += f"<|user|>\\n{message.content}</s>\\n"
        elif message.role \ "system": prompt += f"<|system|>\\n{message.content}\\n" elif message.role  "assistant": prompt += f"<|assistant|>\\n{message.content}\\n" # ensure we start with a system prompt, insert blank if needed if not prompt.startswith("<|system|>\\n"): prompt = "<|system|>\\n\\n" + prompt # add final assistant prompt prompt = prompt + "<|assistant|>\\n" return prompt def completion\_to\_prompt(completion): return f"<|system|>\\n\\n<|user|>\\n{completion}\\n<|assistant|>\\n"

### Model Loading[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/#model-loading)

Models can be loaded by specifying the model parameters using the `OpenVINOLLM` method.

If you have an Intel GPU, you can specify `device_map="gpu"` to run inference on it.

In \[ \]:

Copied!

ov\_config \= {
    "PERFORMANCE\_HINT": "LATENCY",
    "NUM\_STREAMS": "1",
    "CACHE\_DIR": "",
}

ov\_llm \= OpenVINOLLM(
    model\_name\="HuggingFaceH4/zephyr-7b-beta",
    tokenizer\_name\="HuggingFaceH4/zephyr-7b-beta",
    context\_window\=3900,
    max\_new\_tokens\=256,
    model\_kwargs\={"ov\_config": ov\_config},
    generate\_kwargs\={"temperature": 0.7, "top\_k": 50, "top\_p": 0.95},
    messages\_to\_prompt\=messages\_to\_prompt,
    completion\_to\_prompt\=completion\_to\_prompt,
    device\_map\="cpu",
)

ov\_config = { "PERFORMANCE\_HINT": "LATENCY", "NUM\_STREAMS": "1", "CACHE\_DIR": "", } ov\_llm = OpenVINOLLM( model\_name="HuggingFaceH4/zephyr-7b-beta", tokenizer\_name="HuggingFaceH4/zephyr-7b-beta", context\_window=3900, max\_new\_tokens=256, model\_kwargs={"ov\_config": ov\_config}, generate\_kwargs={"temperature": 0.7, "top\_k": 50, "top\_p": 0.95}, messages\_to\_prompt=messages\_to\_prompt, completion\_to\_prompt=completion\_to\_prompt, device\_map="cpu", )

In \[ \]:

Copied!

response \= ov\_llm.complete("What is the meaning of life?")
print(str(response))

response = ov\_llm.complete("What is the meaning of life?") print(str(response))

### Inference with local OpenVINO model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/#inference-with-local-openvino-model)

It is possible to [export your model](https://github.com/huggingface/optimum-intel?tab=readme-ov-file#export) to the OpenVINO IR format with the CLI, and load the model from local folder.

In \[ \]:

Copied!

!optimum\-cli export openvino \--model HuggingFaceH4/zephyr\-7b\-beta ov\_model\_dir

!optimum-cli export openvino --model HuggingFaceH4/zephyr-7b-beta ov\_model\_dir

It is recommended to apply 8 or 4-bit weight quantization to reduce inference latency and model footprint using `--weight-format`:

In \[ \]:

Copied!

!optimum\-cli export openvino \--model HuggingFaceH4/zephyr\-7b\-beta \--weight\-format int8 ov\_model\_dir

!optimum-cli export openvino --model HuggingFaceH4/zephyr-7b-beta --weight-format int8 ov\_model\_dir

In \[ \]:

Copied!

!optimum\-cli export openvino \--model HuggingFaceH4/zephyr\-7b\-beta \--weight\-format int4 ov\_model\_dir

!optimum-cli export openvino --model HuggingFaceH4/zephyr-7b-beta --weight-format int4 ov\_model\_dir

In \[ \]:

Copied!

ov\_llm \= OpenVINOLLM(
    model\_name\="ov\_model\_dir",
    tokenizer\_name\="ov\_model\_dir",
    context\_window\=3900,
    max\_new\_tokens\=256,
    model\_kwargs\={"ov\_config": ov\_config},
    generate\_kwargs\={"temperature": 0.7, "top\_k": 50, "top\_p": 0.95},
    messages\_to\_prompt\=messages\_to\_prompt,
    completion\_to\_prompt\=completion\_to\_prompt,
    device\_map\="gpu",
)

ov\_llm = OpenVINOLLM( model\_name="ov\_model\_dir", tokenizer\_name="ov\_model\_dir", context\_window=3900, max\_new\_tokens=256, model\_kwargs={"ov\_config": ov\_config}, generate\_kwargs={"temperature": 0.7, "top\_k": 50, "top\_p": 0.95}, messages\_to\_prompt=messages\_to\_prompt, completion\_to\_prompt=completion\_to\_prompt, device\_map="gpu", )

You can get additional inference speed improvement with Dynamic Quantization of activations and KV-cache quantization. These options can be enabled with `ov_config` as follows:

In \[ \]:

Copied!

ov\_config \= {
    "KV\_CACHE\_PRECISION": "u8",
    "DYNAMIC\_QUANTIZATION\_GROUP\_SIZE": "32",
    "PERFORMANCE\_HINT": "LATENCY",
    "NUM\_STREAMS": "1",
    "CACHE\_DIR": "",
}

ov\_config = { "KV\_CACHE\_PRECISION": "u8", "DYNAMIC\_QUANTIZATION\_GROUP\_SIZE": "32", "PERFORMANCE\_HINT": "LATENCY", "NUM\_STREAMS": "1", "CACHE\_DIR": "", }

### Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/#streaming)

Using `stream_complete` endpoint

In \[ \]:

Copied!

response \= ov\_llm.stream\_complete("Who is Paul Graham?")
for r in response:
    print(r.delta, end\="")

response = ov\_llm.stream\_complete("Who is Paul Graham?") for r in response: print(r.delta, end="")

Using `stream_chat` endpoint

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= ov\_llm.stream\_chat(messages)

for r in resp:
    print(r.delta, end\="")

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = ov\_llm.stream\_chat(messages) for r in resp: print(r.delta, end="")

For more information refer to:

*   [OpenVINO LLM guide](https://docs.openvino.ai/2024/learn-openvino/llm_inference_guide.html).
    
*   [OpenVINO Documentation](https://docs.openvino.ai/2024/home.html).
    
*   [OpenVINO Get Started Guide](https://www.intel.com/content/www/us/en/content-details/819067/openvino-get-started-guide.html).
    
*   [RAG example with LlamaIndex](https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/llm-rag-llamaindex).
    

Back to top

[Previous OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)[Next Optimum Intel LLMs optimized with IPEX backend](https://docs.llamaindex.ai/en/stable/examples/llm/optimum_intel/)

Hi, how can I help you?

🦙
