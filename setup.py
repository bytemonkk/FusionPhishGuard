from setuptools import setup, find_packages

setup(
    name="FusionPhishGuard",
    version="1.0.0",
    author="Yashwanth Yallavula, Panigrahi Srikanth, Manoj Kumar Sunkara, Vishwanath Tangella",
    description="Attention-Enhanced Multi-Branch Framework for Intelligent Phishing Detection on Mobile and Web Platforms",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "transformers",
        "sentence-transformers",
        "scikit-learn",
        "numpy",
        "pandas",
        "matplotlib",
        "tqdm",
        "gensim",
        "pyyaml"
    ],
    python_requires=">=3.10",
    license="MIT",
    keywords=[
        "phishing-detection",
        "cybersecurity",
        "deep-learning",
        "transformers",
        "llm",
        "attention-mechanism",
        "bilstm",
        "pytorch",
        "url-analysis",
        "machine-learning"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)