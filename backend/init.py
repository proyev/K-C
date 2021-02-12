from fitbert import FitBert

# This file does nothing except instantiate a Fitbert Model, to prompt the fitbert package to install the necessary model files
# This should happen at compile time, rather than at startup time

if __name__ == '__main__':
    fb = FitBert(model_name="bert-large-uncased", disable_gpu=True)