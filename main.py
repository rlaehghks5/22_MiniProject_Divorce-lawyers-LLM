from fastapi import FastAPI
from pydantic import BaseModel
# from llm_model import SimpleLLM
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from peft import get_peft_config, get_peft_model, LoraConfig, TaskType, PeftModel, PeftConfig
from utils.prompter import Prompter

app = FastAPI()

print('tokenizer')
tokenizer = AutoTokenizer.from_pretrained("LDCC/LDCC-SOLAR-10.7B", trust_remote_code=True)
# print(tokenizer.es)
print('model')
model = AutoModelForCausalLM.from_pretrained(
    "LDCC/LDCC-SOLAR-10.7B",
    device_map="auto",
    return_dict=True,
    torch_dtype=torch.float16,
)

print('model_2')
peft_model_id = 'DoHwan9672/SOLAR10.7B-Divorce-Lawyers-LLM-PEFT'
model = PeftModel.from_pretrained(model, peft_model_id).to('cuda', non_blocking=True)

print('load done')
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompter = Prompter("kullm")

def infer(instruction="", input_text=""):
    prompt = prompter.generate_prompt(instruction, input_text)
    print('prompt:\n', prompt)
    output = pipe(prompt, max_length=1024, temperature=0.8, do_sample=True, eos_token_id=32000, top_p=0.7, top_k=80, truncation=True)
    s = output[0]["generated_text"]
    result = prompter.get_response(s)

    return result

class TextRequest(BaseModel):
    text: str
    
@app.post("/generate_text/")
async def generate_text(request: TextRequest):
    print("request.text: ",request.text)
    input_text = request.text

    result = infer(instruction=input_text)

    # Postprocess the output_tensor (convert numerical representation to text)
    # For example, convert token IDs back to text using tokenizer

    return {"generated_text": result}
