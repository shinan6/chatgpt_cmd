from setuptools import setup

setup(
    name='chatgpt_cmd',
    version='0.0.1',
    author='Shinan Liu',
    author_email='shinanliu@uchicago.edu',
    description='Simply a ChatGPT command line tool, which saves all chat history to .csv',
    url='https://github.com/shinan6/chatgpt_cmd',
    install_requires=[
        'openai==0.27.0',
        'setuptools==49.2.0.post20200714'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ]
)