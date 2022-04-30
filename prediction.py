import numpy as np
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.nn as nn

class Predictor(object):
    #This is the function we will use to train a model with given dataset.
    def train(self,size,inputs,targets):
        model = nn.Linear(3, 2)                                         #We declare a linear model with 3 inputs and 2 outputs
        trainingDS = TensorDataset(inputs, targets)                     #We take our input and target tensors and create a dataset
        batch_size = 5                                                  #This is the amount of training data to go through at each iteration
        trainingDL = DataLoader(trainingDS, batch_size, shuffle=True)   #We create the loader for the data and enable shuffle for randomized distribution
        loss_func = F.mse_loss                                          #As our loss function we will use mean squared error function
        opt = torch.optim.SGD(model.parameters(), lr=1e-5)              #This is the gradient descent function from torch library, initially I choose an arbitrary learning rate
        for epoch in range(size):
            for xb, yb in trainingDL:
                prediction = model(xb)                                  #We use our model to get a prediction
                loss = loss_func(prediction, yb)                        #We calculate how bad the prediction is via loss function
                loss.backward()                                         #This computes the gradients 
                opt.step()                                              #And this uses the gradients to update the weights and biases
                opt.zero_grad()                                         #We need to zero the current gradient information in order to calculate new ones in nex iteration
        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, size, loss.item()))
        return model                                                    #After we trained for the specifed time we return the trained model

    def getdata(self,filename):                                         #
        with open(str(filename),'rb') as file:
            inputs = np.load(file)
            targets = np.load(file)
        inputs = inputs.astype(np.float32)
        targets = targets.astype(np.float32)
        inputs = np.delete(inputs, 0, 0)
        targets = np.delete(targets, 0, 0)
        print(inputs.shape)
        print(targets.shape)
        inputs = torch.from_numpy(inputs)
        targets = torch.from_numpy(targets)
        return inputs, targets

predictor = Predictor()
inputs, targets = predictor.getdata("batch.npy")




model = predictor.train(100,inputs,targets)
while True:
    print("Predict the outcome of game for: ")
    agro = np.float32(input("Enemy aggresiveness: "))
    health = np.float32(input("Player health: "))
    power = np.float32(input("Player power: "))
    testing = np.array([agro,health,power])
    testing = torch.from_numpy(testing)
    #testing = torch.tensor([agro, health, power], dtype='float32')
    print(model(testing))
    


