# Low-code model tuning in PyCaret - a python-based package.

![Logo.jpeg](Logo.jpeg)

## About this package

This newly created light weight solution that will invoke the python class that contains the core logic of low-code machine-learning library to evaluate the best model for your solutions. This application developed using pandas & other useful libraries. This project is for the advanced Python developer & Data Science Newbi's.


## How to use this package

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the Model Tuning-App:

```bash
python trainPYCARETModel.py
```

Please find the some of the important dependent package -

```
numpy==1.24.2
pandas==1.5.3
python-dateutil==2.8.2
pycaret==3.0.0

```

Install the requirements:

```

Run the Model Testing-App:

```bash
python testPYCARETModel.py
```

Note that the debug indicator is set to "Y". This will generate logs. If you change this to 'N'. No logs will be generated. However, the process will be faster.

## Screenshots

![demo.GIF](demo.GIF)

## Resources

- To view the complete demo with sound, check out our [YouTube Page](https://youtu.be/jhcAQDJLQrQ).
- To view the more on PyCaret, check out this [PyCaret Official PyPi Page](https://pypi.org/project/pycaret/3.0.0/).
