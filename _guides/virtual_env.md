---
layout: page
title: "Using Virtual Environments"
guideno: 1
---

## Motivation

The idea behind virtual environments is to ensure that different projects don't have conflicting dependencies. For example, if one project you're working on uses some package A at version 1.0, but another project you're working on uses package A at version 2.0 (which is not backwards compatible), then you would need to remove and re-install package A every time you switched projects. With virtual environments, you simply need to switch virtual environments instead!

Virtual environments not only help us manage packages but also Python versions when used in conjunction with a Python version manager like `pyenv`.

## Installation (if using `pyenv`)

If you're using macOS, you can install virtualenv for pyenv using brew:

```bash
brew install pyenv-virtualenv
```

Then add the following line to your `.bashrc` or equivalent and then restart your shell.

```bash
eval "$(pyenv virtualenv-init -)"
```

Otherwise, you should follow the instructions listed on the [pyenv-virtualenv repo](https://github.com/pyenv/pyenv-virtualenv?tab=readme-ov-file#installation).

## Using Virtual Environments

To create a venv, first find a place to put it. Typically, this will be within the folder of the project you're working on. To create a venv, run the following command:

```bash
pyenv virtualenv <venv_name>
```

After creating a virtual environment, you'll need to activate it. Do so by running this command:

```bash
pyenv activate <venv_name>
```

This will effectively make it seem like you have a fresh new Python installation with basically no packages. Try running `pip list` and you'll probably only see two things: `pip` itself and `setuptools`. Your terminal might also tell you which virtual environment you're currently working in, e.g. somewhere within the prompt. Mine looks like this:

```bash
my_cool_venv ❯
```

You can also run `pyenv virtualenvs` to see a list of virtualenvs. If one is active, it will have an asterisk next to its name.

Finally, once you're done using a virtual environment, you'll need to deactivate it. Simply run the command:

```bash
pyenv deactivate
```

and you should no longer see that you are in the virtual environment.

There's more advanced usage you can setup, such as automatically activating environments based on the directory you're in. If you're interested, take a look at the [pyenv-virtualenv repo](https://github.com/pyenv/pyenv-virtualenv?tab=readme-ov-file#usage).