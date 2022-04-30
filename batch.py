import numpy as np
#I use this to collect all the results from the games played, and concatenate them into one numpy array, which is then also saved as a file
A =  np.array([[0,0,0]])
B = np.array([[0,0]])

for i in range(100):
    name = 'iteration' + str(i) + '.npy'
    with open(name, 'rb') as f:
        a = np.load(f)
        b = np.load(f)
        A = np.concatenate((A,a))
        B = np.concatenate((B,b))
        
print(A,B)

txt = "batch.npy"
with open(txt, 'wb') as f:
    np.save(f,A) 
    np.save(f, B)