import base64
import time
from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1", timeout=300.0)

#def encode_image_to_base64(image_path: str) -> str:
#    mime_type = "image/png" if image_path.endswith(".png") else "image/jpeg"
#    with open(image_path, "rb") as f:
#        encoded = base64.b64encode(f.read()).decode("utf-8")
#    return f"data:{mime_type};base64,{encoded}"
#
#image_data_uri = encode_image_to_base64("sample_image.png")
#
#start_time = time.perf_counter()
#response = client.chat.completions.create(
#    model="deepseek-ocr",
#    messages=[
#        {
#            "role": "user",
#            "content": [
#                {"type": "text", "text": "<image>\n<|grounding|>Convert the document to markdown."},
#                {"type": "image_url", "image_url": {"url": image_data_uri}},
#            ],
#        }
#    ],
#    max_tokens=4096,
#    temperature=0.0,
#    extra_body={
#        "skip_special_tokens": False,
#        "vllm_xargs": {
#            "ngram_size": 30,
#            "window_size": 90,
#            "whitelist_token_ids": [128821, 128822],
#        },
#    },
#)
#latency = time.perf_counter() - start_time
#print(f"⚡ Inferred on T4 in {latency:.2f}s!")
#print(response.choices[0].message.content)

import base64
import time
from openai import OpenAI

# Keep base_url matching your working port-forward
client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1", timeout=300.0)

def encode_image_to_base64(image_path: str) -> str:
    mime_type = "image/png" if image_path.endswith(".png") else "image/jpeg"
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

image_data_uri = encode_image_to_base64("week3_vllm_deployment/sample_image.png")

print("🚀 Sending request to vLLM...")
start_time = time.perf_counter()

response = client.chat.completions.create(
    model="deepseek-ocr",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "<image>\n<|grounding|>Convert the document to markdown."},
                {"type": "image_url", "image_url": {"url": image_data_uri}},
            ],
        }
    ],
    max_tokens=2048,
    temperature=0.0,
    # REMOVED: extra_body with the aggressive ngram_size constraints
)

latency = time.perf_counter() - start_time
print(f"⚡ Inferred in {latency:.2f}s!")
print(response.choices[0].message.content)