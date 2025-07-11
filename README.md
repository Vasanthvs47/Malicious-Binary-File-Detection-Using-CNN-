MALICIOUS BINARY EXECUTABLE FILE DETECTION USING COMPUTER VISION

Malware malicious software designed to compromise the confidentiality, integrity, or availability of computer systems continues to escalate in frequency and sophistication, posing severe risks to individuals, enterprises, and critical infrastructure. Traditional signature‐based and heuristic detection methods struggle against polymorphic and zero‐day threats, driving the cybersecurity community to explore machine learning (ML) and, more recently, computer vision (CV) techniques for more resilient detection mechanisms.

In the CV‐based approach, raw binary files are interpreted as images by mapping each byte (0–255) to a grayscale pixel intensity, enabling convolutional neural networks (CNNs) to automatically learn hierarchical visual features indicative of malicious patterns. This “binary visualization” strategy was first popularized by Nataraj et al., who demonstrated that simple CNNs could effectively classify malware into multiple families based on their image representations. More recent studies have fine‐tuned state‐of‐the‐art architectures such as EfficientNet, ResNet, and Inception variants to achieve classification accuracies above 95% on large‐scale malware image benchmarks.
Building on this paradigm, our project—Malicious Binary File Detection Using Computer Vision—implements a binary classifier that distinguishes malicious executables from benign software by:
1. Binary‑to‑Image Conversion
Transforming each executable into an 8‑bit grayscale image, resized to 255×255 pixels.
2. Dataset Utilization
Leveraging the Balanced Malware Image Dataset from Kaggle, which provides over 24 000 labeled malware images across multiple families,
supplemented with an equal number of benign images converted via the same pipeline.
3. Model Fine‑Tuning
Adapting a pre‑trained Inception‑V3 network in TensorFlow/ Keras, training with the Adam optimizer for 4 epochs and a batch size of 32.
