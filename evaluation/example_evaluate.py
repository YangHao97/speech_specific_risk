from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch
from tqdm import tqdm
import re
torch.manual_seed(1234)

def remove_non_letters(s):
    return re.sub(r'[^a-zA-Z\s]', '', s).replace(" ", "_")

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-Audio-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-Audio-Chat", device_map="cuda", trust_remote_code=True).eval()
model.generation_config.do_sample = False
model.generation_config.temperature = 0.0

############### Unsafe Audio ###############
audio_path = "your_path.../data/sarcasm/unsafe/"
fp = open("sarcasm_prompts.txt", "r")
prompt_list = fp.read().split("\n")
fp.close()

num = 1
for prompt in tqdm(prompt_list):

    fp = open("your_path.../sarcasm/unsafe/" + str(num) + ".txt", 'w')
    res_list = []

    for i in tqdm(range(1, 376)):
        query = tokenizer.from_list_format([
            {'audio': audio_path + str(i) + ".wav"},
            {'text': prompt},
        ])

        response, history = model.chat(tokenizer, query=query, history=None)
        res_list.append(response + "\n")

    for res in res_list:
        fp.write(res)
    fp.close()
    num = num + 1


############### Safe Audio ###############
audio_path = "your_path.../data/sarcasm/safe/"
fp = open("sarcasm_prompts.txt", "r")
prompt_list = fp.read().split("\n")
fp.close()

num = 1
for prompt in tqdm(prompt_list):

    fp = open("your_path.../sarcasm/safe/" + str(num) + ".txt", 'w')
    res_list = []

    for i in tqdm(range(1, 376)):
        query = tokenizer.from_list_format([
            {'audio': audio_path + str(i) + ".wav"},
            {'text': prompt},
        ])

        response, history = model.chat(tokenizer, query=query, history=None)
        res_list.append(response + "\n")

    for res in res_list:
        fp.write(res)
    fp.close()
    num = num + 1
