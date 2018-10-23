# MNIST Tensorflow
Basic image classification using tensorflow and its estimator API

## File Contents
* `digits.py`: Code for loading the dataset
* `EDA.ipynb`: Brief exploration and verification of the dataset
* `CNN.ipynb`: Basic CNN model for image classification based on VGG
* `CNN-RES.ipynb`: VGG based CNN model with shortcut connections
* `CNN-DA.ipynb`: Basic CNN model for image classification based on VGG with data augmentation
* `CNN-RES-DA.ipynb`: VGG based CNN model with shortcut connections with data augmentation
* `requirements.txt`: Pip requirements file to install all dependencies to run the code

## Running the Code
1. Clone the repository using `git clone https://github.com/baluyotraf/mnist-tensorflow.git`
2. Download a dataset. The dataset must follow the format similar to `https://www.kaggle.com/c/digit-recognizer/data`
3. Install all the dependencies from the `requirements.txt file`. This can be done using `pip install -r requirements.txt`
4. On the repository directory run the jupyter notebook. Use the command `jupyter notebook`
5. Open and notebooks, modify the paths, and run them as desired.
6. Open tensorboard to view the results while training the models. Running `tensorboard --logdir /path/to/modeldir --host localhost` will allow you to view tensorboard on `http://localhost:6006`.

## Results

The models were run on a dataset with 10000 images. 8000 images is used for training, 1000 for development and 1000 for testing. Here are the results

| Model | Minimum Dev Loss | Test Loss | Test Precision | Test Recall | Test F1 Score | Test Accuracy |
| ---------- | - | - | - | - | - | - |
| CNN        | 0.122868 | 0.146851 | 0.970223 | 0.970 | 0.969903 | 97.0% |
| CNN-DA     | 0.106950 | 0.092053 | 0.970262 | 0.969 | 0.969220 | 96.9% |
| CNN-RES    | 0.174696 | 0.160997 | 0.959430 | 0.959 | 0.958955 | 95.9% |
| CNN-RES-DA | 0.068687 | 0.080314 | 0.978308 | 0.978 | 0.978017 | 97.8% |

The data augmentation was not able to improve the accuracy but it was able to reduce the test loss. This means that the certainty of the predictions went up. Also the development and the test datasets has closer result with the augmented data. From that we can say that the generalization of the model when it comes to unseen dataset increased.

The CNN-RES model did not do better than the normal CNN model. This is due to the tendency of the model to overfit during training. However when the augmented data with high generalization was used with the CNN-RES model, higher accuracy and lower losses was achieved. This is due the reduction of the overfitting. 
