import json
import os
import pickle

# Part A
def read_json(file_path):
    file = open(file_path)
    return file

# print(read_json('/Users/laffertythomas/dev/PyParts/PyPart9/data/super_smash_bros/link.json'))

# Part B
def read_all_json_files(dir_path:str) -> list:
    os.chdir(dir_path)
    json_files = [read_json(pos_json) for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
    return json_files

# print(read_all_json_files('/Users/laffertythomas/dev/PyParts/PyPart9/data/super_smash_bros'))
    # file_content = list()
    # os.chdir(dir_path)
    # for root, dirs, files in os.walk("data", topdown=True):
    #     for name in files:
    #         file_content.append(json.loads(read_json(name)))
    # return file_content
#
# read_all_json_files('/Users/laffertythomas/dev/PyParts/PyPart9/data/super_smash_bros')

def write_pickle(file_path):
    # file_content = str(open(file_path,))
    output_file = open('super_smash_characters.pickle', 'wb')
    pickle.dump(file_path, output_file)

    # output_list = json.loads(read_json(file_path))

    # print(type(output_list))
# write_pickle('/Users/laffertythomas/dev/PyParts/PyPart9/data/super_smash_bros')
    # pickle.dump(output_list, output_file)
    # super_smash_characters.pickle.close()
    # output_file.close()
#
# write_pickle('/Users/laffertythomas/dev/PyPart9/data/super_smash_bros/')

# write_pickle('/Users/laffertythomas/dev/PyParts/PyPart9/data/super_smash_bros')

def load_pickle(file_path):
    input_file = open(file_path,'rb')
    data = pickle.load(input_file, fix_imports=True)
    input_file.close()
    print(data)

# load_pickle('/Users/laffertythomas/dev/PyParts/PyPart9/super_smash_characters.pickle')