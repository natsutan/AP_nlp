import torch
import random


random.seed(2)
torch.manual_seed(2)

# Tokenizer
from allennlp.data.tokenizers import Tokenizer
from allennlp.data.tokenizers.token_class import Token
from fugashi import Tagger

