<img src="data/Diagrams/steganography_logo.png" width="900">

## Implementing Steganography from scratch using Python

[![flake8](https://img.shields.io/badge/flake8-passing-brightgreen)](https://github.com/italoPontes/Steganography)


This repository presents a robust implementation of steganography techniques designed specifically for embedding sensitive information within images using the Python programming language. In an era characterized by pervasive cybersecurity threats, safeguarding personal data, such as family photographs, from potential unauthorized access is of utmost importance.

Consider the following scenario: you possess a directory on your computer containing treasured family photographs, and you seek to shield them from unauthorized viewing.

Traditional approaches entail certain limitations:

- __Conventional Storage__: Placing images in easily accessible directories on your computer renders them susceptible to discovery by malicious actors.

- __Encryption__: Applying password-based encryption to images may inadvertently draw attention to their presence, piquing the curiosity of adversaries and potentially inviting further attempts to breach security measures.

- __Steganographic Solution__: Utilizing steganography presents a discreet alternative. By embedding important images within seemingly innocuous ones, such as images resembling movie covers, the likelihood of detection by adversaries is significantly diminished. Moreover, augmenting this approach with additional encryption, bolstered by passwords, enhances the security of the steganographically concealed images.

In essence, this repository offers a comprehensive toolkit for leveraging steganography in image data to enhance privacy and confidentiality in digital environments. Through its clear and concise documentation and illustrative examples, users gain insights into implementing and utilizing steganographic techniques effectively for safeguarding sensitive information.

# Quick install

For a quick installation, follow these simple steps:

1. Clone this repository to your local environment.
```
git clone https://github.com/italoPontes/Steganography/
```

2. Navigate to the project directory.
```
cd Steganography
```

3. Run the command `pip install -r requirements.txt` to install all the necessary dependencies listed in the `requirements.txt` file.

```
pip install -r requirements.txt
```

4. Once the installation is complete, you're ready to start.

# How to use?

## Encode

```
python how-to-use.py encode
-secret_image data/secret-image.jpg
-cover_image data/Monalisa.png
-output_image data/steganography-image.png
```

<img src="data/Diagrams/encode-example.png" alt="Encode Demonstration">


## Decode

```
python how-to-use.py decode
-steganography_image data/steganography-image.png
-secret_image data/retrieved.png
```

<img src="data/Diagrams/decode-example.png" alt="Decode Demonstration">


# Who am I?

I am Ítalo de Pontes Oliveira, Master's in Computer Vision and Data Scientist.

<img src="data/Italo.jpeg" alt="Italo de Pontes Oliveira" width="40%">

<a href="https://www.linkedin.com/in/italo-de-pontes/">
<img src="data/logos/Linkedin-logo.png" width="100">
</a>

[Link](https://docs.google.com/document/d/1Wz_oqnyiWBoPQqESW-rKTz4bCPeYhu4qduBa3W660JA/edit?usp=sharing) to my CV (on-line version).

[Link](data/My-cv-Italo-de-Pontes-Oliveira.pdf) to my CV (PDF version), perhaps outdate.