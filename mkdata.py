import glob
import json
import os
import random

labels = ["dokujo-tsushin", "it-life-hack", "kaden-channel", "livedoor-homme", "movie-enter", "peachy", "smax", "sports-watch", "topic-news"]

deta = []

for label in labels:
    dir_path = os.path.join("data/livedoor_news/text", label)
    for file_path in sorted(glob.glob(os.path.join(dir_path, "*.txt"))):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            test = "".join(text.split("\n")[2:])

        deta.append({
            "text": text,
            "label": label
        })

random.seed(1)
random.shuffle(deta)

split_data = {}
eval_size = int(len(deta) * 0.1)
split_data["test"] = deta[:eval_size]
split_data["validation"] = deta[eval_size:eval_size*2]
split_data["train"] = deta[eval_size*2:]

for fold in ("train", "validation", "test"):
    out_file = os.path.join("data/livedoor_news/", "livedoor_news_{}.jsonl".format(fold))
    with open (out_file, "w", encoding="utf-8") as f:
        for item in split_data[fold]:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")



