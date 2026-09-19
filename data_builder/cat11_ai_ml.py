CATEGORY = "Artificial Intelligence & Machine Learning Basics"

QUESTIONS = [
    # Easy (10)
    {
        "difficulty": "Easy",
        "question": "What is Supervised Learning in machine learning?",
        "options": ["Training models on labeled datasets containing known input-output pairs", "Training models without any human supervision or labels", "Rewarding an agent via trial and error in game environments", "Clustering unorganized text documents"],
        "answer": "Training models on labeled datasets containing known input-output pairs",
        "explanation": "Supervised learning algorithms learn a mapping function from input variables (X) to labeled target outputs (Y)."
    },
    {
        "difficulty": "Easy",
        "question": "What is Unsupervised Learning?",
        "options": ["Discovering hidden patterns, clusters, or intrinsic structures in unlabeled data without target outputs", "Learning with manually labeled ground truth", "Training neural networks on labeled image datasets", "Compiling code without errors"],
        "answer": "Discovering hidden patterns, clusters, or intrinsic structures in unlabeled data without target outputs",
        "explanation": "Unsupervised learning infers underlying representations from data without supervisor feedback or target labels (e.g. K-Means clustering)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the primary objective of Classification in machine learning?",
        "options": ["Predicting discrete categorical class labels for given inputs", "Predicting continuous numeric values", "Compressing image file size", "Sorting numbers in ascending order"],
        "answer": "Predicting discrete categorical class labels for given inputs",
        "explanation": "Classification predicts discrete class labels (e.g., spam vs non-spam, disease diagnosis)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the primary objective of Regression in machine learning?",
        "options": ["Predicting continuous numerical target values (e.g., house price, temperature)", "Classifying images into categories", "Grouping customers into clusters", "Translating languages"],
        "answer": "Predicting continuous numerical target values (e.g., house price, temperature)",
        "explanation": "Regression models predict continuous quantitative outcomes based on independent predictor variables."
    },
    {
        "difficulty": "Easy",
        "question": "What is Overfitting in machine learning models?",
        "options": ["When a model learns training data noise and details too closely, performing well on training set but poorly on unseen test data", "When a model is too simple to capture patterns", "When training runs out of GPU RAM", "When dataset has zero features"],
        "answer": "When a model learns training data noise and details too closely, performing well on training set but poorly on unseen test data",
        "explanation": "Overfitting occurs when a complex model captures idiosyncrasies and noise in the training set, sacrificing generalizability."
    },
    {
        "difficulty": "Easy",
        "question": "What is Underfitting?",
        "options": ["When a model is too simple to capture the underlying trend in data, performing poorly on both training and test sets", "When a model achieves 100% test accuracy", "When training data is too clean", "When neural network has too many layers"],
        "answer": "When a model is too simple to capture the underlying trend in data, performing poorly on both training and test sets",
        "explanation": "Underfitting happens when a model lacks capacity or training iterations to learn the data patterns."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithm is a popular unsupervised clustering method that partitions N observations into K clusters?",
        "options": ["K-Means Clustering", "Linear Regression", "Logistic Regression", "Decision Tree Classifier"],
        "answer": "K-Means Clustering",
        "explanation": "K-Means iteratively partitions data points into K clusters by minimizing the distance between points and cluster centroids."
    },
    {
        "difficulty": "Easy",
        "question": "What does an Artificial Neural Network (ANN) take inspiration from?",
        "options": ["Biological neural networks of interconnected neurons in human brains", "Computer motherboard circuitry", "Relational database tables", "File system hierarchies"],
        "answer": "Biological neural networks of interconnected neurons in human brains",
        "explanation": "ANNs are inspired by biological neurons transmitting signals across weighted synaptical connections."
    },
    {
        "difficulty": "Easy",
        "question": "What is the purpose of an Activation Function in neural network nodes?",
        "options": ["Introducing non-linearity to allow networks to learn complex relationships beyond linear combinations", "Cooling down GPU processors", "Preventing matrix multiplication", "Converting floats to integers"],
        "answer": "Introducing non-linearity to allow networks to learn complex relationships beyond linear combinations",
        "explanation": "Non-linear activation functions (like ReLU, Sigmoid, Tanh) enable multi-layer networks to approximate arbitrary complex functions."
    },
    {
        "difficulty": "Easy",
        "question": "What is Reinforcement Learning (RL)?",
        "options": ["An area of ML where an agent learns optimal decision policies through reward signals received from interacting with an environment", "Supervised classification using labels", "Clustering customer data", "Static heuristic rule systems"],
        "answer": "An area of ML where an agent learns optimal decision policies through reward signals received from interacting with an environment",
        "explanation": "In RL, an agent takes actions in an environment to maximize cumulative scalar rewards via trial-and-error exploration."
    },

    # Medium (10)
    {
        "difficulty": "Medium",
        "question": "What is the Bias-Variance Tradeoff in machine learning?",
        "options": ["High bias causes underfitting (erroneous assumptions); high variance causes overfitting (sensitivity to small training fluctuations)", "High bias increases model complexity", "Variance is reduced by increasing model parameters", "Bias and variance always sum to 1"],
        "answer": "High bias causes underfitting (erroneous assumptions); high variance causes overfitting (sensitivity to small training fluctuations)",
        "explanation": "Expected prediction error decomposes into Bias^2 + Variance + Irreducible Error, requiring balance between simplicity and flexibility."
    },
    {
        "difficulty": "Medium",
        "question": "What is Backpropagation in Deep Learning?",
        "options": ["An algorithm calculating the gradient of the loss function with respect to each network weight using the calculus Chain Rule, propagating errors backward", "Restarting network training from epoch 1", "Reversing dataset rows", "Pruning dead neurons"],
        "answer": "An algorithm calculating the gradient of the loss function with respect to each network weight using the calculus Chain Rule, propagating errors backward",
        "explanation": "Backpropagation computes error gradients from output to input layers via chain rule to update weights via Gradient Descent."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Precision and Recall in binary classification evaluation?",
        "options": ["Precision = TP / (TP + FP) (accuracy of positive predictions); Recall = TP / (TP + FN) (proportion of actual positives identified)", "Precision measures negative classes only", "Recall = TP / (TP + FP)", "Precision and Recall are identical metrics"],
        "answer": "Precision = TP / (TP + FP) (accuracy of positive predictions); Recall = TP / (TP + FN) (proportion of actual positives identified)",
        "explanation": "Precision evaluates how many selected items are relevant; Recall evaluates how many relevant items were selected."
    },
    {
        "difficulty": "Medium",
        "question": "What does the F1-Score measure?",
        "options": ["The Harmonic Mean of Precision and Recall", "The arithmetic mean of accuracy and loss", "The time taken to train an epoch", "The ratio of true negatives to false positives"],
        "answer": "The Harmonic Mean of Precision and Recall",
        "explanation": "F1-Score is calculated as `2 * (Precision * Recall) / (Precision + Recall)`, balancing precision and recall on imbalanced data."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of Regularization techniques (L1 Lasso and L2 Ridge) in machine learning?",
        "options": ["Penalizing large model weights in the loss function to prevent overfitting and improve generalization", "Accelerating gradient descent step size", "Normalizing image pixels to [0, 1]", "Imputing missing column values"],
        "answer": "Penalizing large model weights in the loss function to prevent overfitting and improve generalization",
        "explanation": "L1 (Lasso) and L2 (Ridge) add penalty terms to the loss function, constraining weight magnitudes to prevent overfitting."
    },
    {
        "difficulty": "Medium",
        "question": "Why is the Rectified Linear Unit (ReLU) function `f(x) = max(0, x)` widely preferred in hidden layers over Sigmoid?",
        "options": ["It is computationally efficient to evaluate and mitigates the vanishing gradient problem for positive activations", "It bounds all values strictly between 0 and 1", "It is differentiable at all points including x=0", "It completely eliminates dead neurons"],
        "answer": "It is computationally efficient to evaluate and mitigates the vanishing gradient problem for positive activations",
        "explanation": "ReLU has a constant derivative of 1 for positive inputs, avoiding gradient saturation that slows deep networks using Sigmoid/Tanh."
    },
    {
        "difficulty": "Medium",
        "question": "What is the primary architecture used for Computer Vision and image processing tasks?",
        "options": ["Convolutional Neural Networks (CNN)", "Recurrent Neural Networks (RNN)", "Linear Support Vector Machines", "Naive Bayes Classifiers"],
        "answer": "Convolutional Neural Networks (CNN)",
        "explanation": "CNNs use convolutional filter kernels and pooling layers to extract spatial hierarchies of visual features efficiently."
    },
    {
        "difficulty": "Medium",
        "question": "What is K-Fold Cross-Validation?",
        "options": ["Splitting data into K subsets, training on K-1 folds and testing on the remaining fold iteratively K times to assess model robustness", "Training K separate models in parallel on same data", "Repeating training for K epochs", "Clustering data into K groups"],
        "answer": "Splitting data into K subsets, training on K-1 folds and testing on the remaining fold iteratively K times to assess model robustness",
        "explanation": "K-fold cross-validation evaluates model stability and reduces data partitioning bias by averaging test performance across all K splits."
    },
    {
        "difficulty": "Medium",
        "question": "What does Principal Component Analysis (PCA) do?",
        "options": ["Reduces dimensionality of data by finding orthogonal axes (principal components) that maximize data variance", "Classifies text documents into topics", "Normalizes database tables to 3NF", "Predicts time-series values"],
        "answer": "Reduces dimensionality of data by finding orthogonal axes (principal components) that maximize data variance",
        "explanation": "PCA performs linear dimensionality reduction by projecting correlated features onto principal eigenvectors of the covariance matrix."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Bagging (e.g., Random Forest) and Boosting (e.g., XGBoost)?",
        "options": ["Bagging trains independent base models in parallel on bootstrap samples; Boosting trains models sequentially, focusing on errors of previous models", "Boosting trains models in parallel with no dependencies", "Bagging is only for regression; Boosting is only for classification", "Bagging increases model bias"],
        "answer": "Bagging trains independent base models in parallel on bootstrap samples; Boosting trains models sequentially, focusing on errors of previous models",
        "explanation": "Bagging reduces variance by averaging independent trees; Boosting reduces bias by iteratively fitting learners to residual errors."
    },

    # Hard (5)
    {
        "difficulty": "Hard",
        "question": "What is the Self-Attention mechanism in Transformer architectures (e.g., Vaswani et al. 'Attention Is All You Need')?",
        "options": ["Computing dynamic interaction weights between all token pairs in a sequence using Query, Key, and Value matrix projections (`Softmax(QK^T / sqrt(d_k))V`)", "A method for pruning neural network weights", "Recurrent cell transitions over time steps", "A loss function for GAN discriminators"],
        "answer": "Computing dynamic interaction weights between all token pairs in a sequence using Query, Key, and Value matrix projections (`Softmax(QK^T / sqrt(d_k))V`)",
        "explanation": "Self-attention computes relational weights across all positions in parallel via scaled dot-product attention of Query, Key, and Value vectors."
    },
    {
        "difficulty": "Hard",
        "question": "What causes the Vanishing / Exploding Gradient problem in deep Recurrent Neural Networks (RNNs) and how do LSTMs address it?",
        "options": ["Repeated matrix multiplications across long time steps cause gradients to decay to zero or blow up; LSTMs introduce constant error carousels via internal Cell States and gating units (Input, Forget, Output)", "Overfitting on small vocabularies", "High learning rates in Adam optimizer", "Incompatible GPU drivers"],
        "answer": "Repeated matrix multiplications across long time steps cause gradients to decay to zero or blow up; LSTMs introduce constant error carousels via internal Cell States and gating units (Input, Forget, Output)",
        "explanation": "LSTMs use additive linear cell state highways regulated by Forget, Input, and Output gates to let gradient signals flow back across long sequence steps."
    },
    {
        "difficulty": "Hard",
        "question": "In Generative Adversarial Networks (GANs), what is the minimax game formulated between the Generator (G) and Discriminator (D)?",
        "options": ["Generator tries to generate synthetic samples that fool Discriminator; Discriminator tries to distinguish real training samples from fake samples (`min_G max_D V(D, G)`)", "Both networks cooperate to minimize mean squared error", "Discriminator generates images while Generator labels them", "A game played between two RL agents"],
        "answer": "Generator tries to generate synthetic samples that fool Discriminator; Discriminator tries to distinguish real training samples from fake samples (`min_G max_D V(D, G)`)",
        "explanation": "GANs set up a zero-sum game where G creates realistic samples to maximize D's error while D trains as a binary classifier to detect fakes."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of Batch Normalization in deep neural networks?",
        "options": ["Normalizing layer inputs across mini-batches to zero mean and unit variance, smoothing the optimization landscape and accelerating training convergence", "Compressing weights to 8-bit integers", "Splitting batches across CPU cores", "Sorting training data by label"],
        "answer": "Normalizing layer inputs across mini-batches to zero mean and unit variance, smoothing the optimization landscape and accelerating training convergence",
        "explanation": "Batch Normalization stabilizes intermediate activation distributions across mini-batches, allowing higher learning rates and reducing sensitivity to initialization."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Contrastive Loss and Cross-Entropy Loss in self-supervised representation learning?",
        "options": ["Contrastive Loss pulls representations of augmented views of the same sample together while pushing representations of different samples apart in embedding space", "Contrastive loss is used only for linear regression", "Cross-entropy requires unlabeled data exclusively", "They produce identical gradient vectors"],
        "answer": "Contrastive Loss pulls representations of augmented views of the same sample together while pushing representations of different samples apart in embedding space",
        "explanation": "Self-supervised frameworks (like SimCLR, CLIP) use contrastive loss (e.g. InfoNCE) to learn semantic feature embeddings without explicit manual ground-truth labels."
    }
]
