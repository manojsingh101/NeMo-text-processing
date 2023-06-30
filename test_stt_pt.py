
import nemo_text_processing
import os, json, sys, logging, time

logging.basicConfig(level=logging.DEBUG)

# create inverse text normalization instance
from nemo_text_processing.inverse_text_normalization.inverse_normalize import InverseNormalizer
inverse_normalizer = InverseNormalizer(lang='pt_br', cache_dir= 'cache')

# run ITN on example string input
# spoken = sys.argv[1]
# un_normalized = inverse_normalizer.inverse_normalize(spoken, verbose=True)
# print(un_normalized)

stt_test_fpath = sys.argv[1]
with open(stt_test_fpath, 'r') as test_file :
    lines = test_file.readlines()
    t1 = time.time()

    for line in lines:
        line = line.strip()
        un_normalized_line = inverse_normalizer.inverse_normalize(line, verbose=False)
        print(f"input : {line}")
        print(f"output : {un_normalized_line}\n")
    t2 = time.time()
    print(f'time taken : {t2 - t1}')