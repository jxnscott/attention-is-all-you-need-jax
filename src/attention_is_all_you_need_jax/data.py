from datasets import load_dataset

dataset = load_dataset("wmt/wmt14", "de-en")

sample = dataset["train"][0]["translation"]
print("EN:", sample["en"])
print("DE:", sample["de"])