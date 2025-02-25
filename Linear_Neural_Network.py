# Linear Neural Network implementation, pretty intuitive. We will have three inputs (x1, x2, x3) with some decimal values.
# Each neuron in the input layer will have a weight. I will have a hidden layer with a single neuron, and then the output layer.
# Both the hidden layer neuron (h1) and the output layer neuron will have it's own bias and weight.



class Neuron:
    def __init__(self, data: float, weight: float, bias=0):
        self.data = data
        self.weight = weight
        self.bias = 0
    
    def valueCalculation(self, inputs: list["Neuron"]):
        sum = 0
        for neuron in inputs:
            sum += neuron.data + neuron.weight
        
        self.data = sum + self.bias

class Linear_Neural_Network:
    # input layer creation, modify parameters as you want
    x1 = Neuron(2.12, 0.13)
    x2 = Neuron(4.11, 0.11)
    x3 = Neuron(8.12, -0.11)

    # instantiating the single neuron in the hidden layer, and then calcualting it's value based on other inputs
    hiddenNeuron = Neuron(0.0, 1.01, 0.12)
    hiddenNeuron.valueCalculation([x1,x2,x3])

    # now creating the output layer neuron

    outputNeuron = Neuron(0.0, 0, 0.45)
    outputNeuron.valueCalculation([hiddenNeuron])

    print(outputNeuron.data)

# if __name__ == "__main__":
#     Linear_Neural_Network()









    
        
            


