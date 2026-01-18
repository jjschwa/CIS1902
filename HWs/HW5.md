---
layout: page
title: HW5 - LLM Coding Assistant
nav_exclude: true
---

# HW5 - LLM Coding Assistant
__Due Date:__

(Right click and “Save Link As…”)

[llm_coder.zip](../HWs/llm_coder.zip)

# LLM Coding Assistant

In this assignment, we'll be building an AI coding assistant! Download the provided zip file and extract it. You should see a folder with some files. You will only need to modify `server.py` for this assignment, but you will need to refer to `generate.py` to understand how to generate LLM responses.

Overall, this homework does not involve much, but setup, downloading the model, and debugging may take quite some time. Get started early, otherwise we won't be able to help you with strange errors!

| File | Description |
|---|---|
| `requirements.txt` | A list of Python package requirements. |
| `generate.py` | This is an example of how to generate a response from DeepSeek's Coder LLM. |
| `templates/chat.html` | A provided HTML file that displays a very basic chat template. |
| `server.py` | An empty file where you will be working! |

## Setup

### Packages

It's highly recommended to use a *Python virtual environment* (venv) for this assignment. Otherwise, you may run into some trouble during setup. Follow the guide posted on the website to get setup. Once you've got virtual environments installed, create one for this homework and activate it.

```bash
pyenv virtualenv llm_coder
pyenv activate llm_coder
```

Install the required packages to run the model:

```shell
pip install -r requirements.txt
```

Next, you will need to install `huggingface_hub`. Huggingface is an open source community that builds tools for training and evaluating AI models.

```shell
pip install --upgrade huggingface_hub
```

If all goes well, you should be able to have the LLM generate responses by simply running the python script below. The first time you run this, it will need to download the entire DeepSeek model from HuggingFace, so it may take a couple of minutes. While we're using the smallest version of the coding model DeepSeek provides, it's still over 3gb! Once the model is downloaded, it still takes a bit of time to generate a response. For my laptop, it took about 10-15 seconds for each query.

````shell
❯ python generate.py
...
Sure, here is a simple implementation of the Quick Sort algorithm in Python:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Test the function
print(quicksort([3,6,8,10,1,2,1]))
# Output: [1, 1, 2, 3, 6, 8, 10]
```

This algorithm works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.
````

## Tasks

We've got our LLM downloaded and ready to use, so now let's actually create a website where users can interact with our model. Your goal is to fill in `server.py` to create a Flask webserver that has two endpoints. We will do this in two parts. First, we'll create a class to help us interact with the LLM, and then we will implement the Flask server.

### LLMCoder

Implement a class `LLMCoder` to help manage our LLM. Specifically, the init function should load the tokenizer and model. Then, there should be a `generate()` method that takes a prompt as input and returns the model’s response.

### Flask Endpoints

Implement the following two endpoints.

* `/` Homepage: this should render the provided `chat.html` page. It should only serve the HTTP `GET` method. Take a look at Flask’s [template documentation](https://flask.palletsprojects.com/en/stable/tutorial/templates/) for guidance.
* `/generate` Generate: this will generate text based on the prompt given. It is called when you click on the "Submit" button (the code for this is in chat.html if you wish to examine it).
  * It should be a `POST` endpoint that expects a JSON blob. Return a 400 if the body given is not JSON.
  * The JSON blob will contain a single key called `query` which contains the prompt. If the JSON blob is not properly formatted, return a 400.
  * Pass the prompt to the LLM model and generate a response. Return the response as plain text.

  If you’ve implemented it properly, you should see the website render the response!