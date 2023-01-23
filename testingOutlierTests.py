import pickle
from pprint import pprint
# load the array from the binary file
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

print(len(data))
pprint(data[3])
