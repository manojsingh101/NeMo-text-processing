
import nemo_text_processing
import os, json, sys, logging, time

logging.basicConfig(level=logging.DEBUG)

# create inverse text normalization instance
from nemo_text_processing.inverse_text_normalization.inverse_normalize import InverseNormalizer
inverse_normalizer = InverseNormalizer(lang='en', cache_dir= 'cache', overwrite_cache=False)

# spoken = 'twenty second february nineteen twenty' #sys.argv[1]
# un_normalized = inverse_normalizer.inverse_normalize(spoken, verbose=True)
# print(un_normalized)

stt_test_fpath = sys.argv[1]

with open(stt_test_fpath, 'r') as test_file :
    j_obj = json.load(test_file)
    lines = [line['input'].lower().strip() for line in j_obj ]
    t1 = time.time()
    for line in lines:
            un_normalized_line = inverse_normalizer.inverse_normalize(line, verbose=False)
            print(f"input : {line}")
            print(f"output : {un_normalized_line}\n")
    t2 = time.time()
    print(f'time taken = {t2-t1}')
