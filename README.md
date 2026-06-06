# DATA-PIPELINE-DEVELOPMENT

"COMPANY": CODTECH IT SOLUTIONS

"NAME": MAYERA HABEEB

"INTERN ID": CITS262

"DOMAIN": DATA SCIENCE

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTHOSH



"TASK-DESCRIPTION": This task involved building and training a deep learning neural network to classify handwritten digit images. The model was trained on the MNIST dataset, which is one of the most well-known benchmark datasets in machine learning, and achieved a test accuracy of 96.87%.

Tools and Libraries Used
The model was built using PyTorch, a leading deep learning framework widely used in both research and industry. Additional libraries included Torchvision for loading and transforming the MNIST dataset, and Matplotlib for generating visualizations. The script was written in a plain Python file (image_classifier.py) and run via the Windows Command Prompt.

Platform
The project was developed on a Windows machine. PyTorch was chosen over TensorFlow due to compatibility with Python 3.14, which TensorFlow does not yet support. The model was trained entirely on the local CPU.

Dataset
The MNIST dataset consists of 70,000 grayscale images of handwritten digits (0–9), each 28x28 pixels in size. 60,000 images were used for training and 10,000 for testing. The dataset was downloaded automatically using Torchvision's built-in datasets module.

Model Architecture
The neural network was built using PyTorch's nn.Sequential module and consisted of an input Flatten layer to convert 2D images into 1D vectors, a fully connected Linear layer with 128 neurons and ReLU activation, a second Linear layer with 64 neurons and ReLU activation, and a final output Linear layer with 10 neurons corresponding to digits 0–9.

Training
The model was trained for 5 epochs using the Adam optimiser and CrossEntropyLoss. The training loss dropped steadily from 0.4095 in epoch 1 to 0.0998 in epoch 5, demonstrating that the model was learning effectively.

Application and Real-World Relevance
Image classification is used in a huge range of real-world applications including medical imaging, document scanning, postal code recognition, and security systems. The techniques used here — convolutional-style networks, backpropagation, and optimisation — form the foundation of modern computer vision systems.
