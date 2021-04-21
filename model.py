# https://www.python-engineer.com/courses/pytorchbeginner/17-saving-and-loading/
import torch
import torch.nn as nn

# Enter the desired model, this is an example model
class Model(nn.Module):
    def __init__(self, n_input_features):
        super(Model, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

# Edit the parameters for the model
model = Model(n_input_features=6)

# Enter the name of the file to which you will save the model. We need the model source code.
# Make sure to use .pth as the extension as that is the convention for pytorch.
FILE = "model.pth"
torch.save(model, FILE)
model = torch.load(PATH)
model.eval()

########################################################################################
# use this in case we want to save the state of the model.
# torch.save(model.state_dict(), PATH)
# model.load_state_dict(torch.load(PATH))
# model.eval()