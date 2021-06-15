import matplotlib.pyplot as plt
import pickle

def load_data():
    data = {}
    
    for char in 'abcdef':
        file = open(f'data/{char}.pkl', 'rb')
        raw = pickle.load(file)
        data[char] = raw
        
    return data

def visualize(data):
    rows, columns = 2, 3
    
    keys = list(data.keys())
    
    fig, axes = plt.subplots(rows,columns, figsize=(20,10))
    
    for idx in range(len(keys)):
        row, col = idx//columns, idx%columns
        axes[row, col].hist(data[keys[idx]], ec='black', bins=15)
        axes[row, col].set_title(keys[idx].upper(), fontsize=20)
        
def multiple_choice():
    data = load_data()
    visualize(data)
    
    