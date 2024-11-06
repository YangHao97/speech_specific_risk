# Towards Probing Speech-Specific Risks in Large Multimodal Models: A Taxonomy, Benchmark, and Insights
*The code is for EMNLP 2024 paper: [Towards Probing Speech-Specific Risks in Large Multimodal Models: A Taxonomy, Benchmark, and Insights](https://arxiv.org/abs/2406.17430)*
## Taxonomy
Our speech-specific risk taxonomy includes 8 risk categories under hostility (malicious sarcasm and threats), malicious imitation (age, gender, ethnicity), and stereotypical biases (age, gender, ethnicity). 


<div align="center">
<img src="https://github.com/YangHao97/speech_specific_risk/blob/main/resources/taxonomy.png" width="50%">
</div>

## Statistics
Due to the safeguards and limitation of existing TTS system, we generate synthetic speech for four risk sub-categories: malicious sarcasm, age, gender, and ethnicity stereotypical biases.


<div align="center">
<img src="https://github.com/YangHao97/speech_specific_risk/blob/main/resources/statistics.png" width="50%">
</div>

## Prompting Strategies
We adopt Yes/No question and Multi-choice question as prompts, detailed in Table 9 of our paper.
## Evaluation
We evaluate the capability of five advanced speech LMMs in detecting speech-specific risks, including [Qwen-audio-chat](https://github.com/QwenLM/Qwen-Audio), [SALMONN-7B/13B](https://github.com/bytedance/SALMONN), [WavLLM](https://github.com/microsoft/SpeechT5/tree/main/WavLLM), and [Gemini-1.5-Pro](https://gemini.google.com/). Please deploy models/APIs based on the corresponding offical instructions.
## Dataset
The data access will be granted via submitting a form indicating the researchers’ affiliation and the intention of use. [Access the dataset](https://docs.google.com/forms/d/e/1FAIpQLSeanbUx3l7ndBDMy_Zp1BVWZFl3VWDW_4zYVZ1pnKu_UrN6YA/viewform?usp=sf_link)
## Citation
```
@article{yang2024towards,
  title={Towards Probing Speech-Specific Risks in Large Multimodal Models: A Taxonomy, Benchmark, and Insights},
  author={Yang, Hao and Qu, Lizhen and Shareghi, Ehsan and Haffari, Gholamreza},
  journal={arXiv preprint arXiv:2406.17430},
  year={2024}
}
```
