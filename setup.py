# Create setup.py in root directory
# Create new file named 'setup.py' and paste this content:
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz'
        ],
    },
    author="Krishnajith Gokul",
    author_email="krishnajithgokul@gmail.com",
    description="Math quiz game",
    license="Apache License 2.0",
    keywords="math quiz game education",
    url="https://github.com/yourusername/dsss_homework_2",
    python_requires='>=3.6',
)




