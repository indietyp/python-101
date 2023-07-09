# Setup

```admonish warning

This section is specific to macOS. If you are using Windows, please refer to the [Windows](./00-windows.md) page.

We currently have no setup instructions for Linux, due to the large variety of distributions and package managers, 
feel free to open a PR if you want to add instructions for your distribution.

```

We will be using Python 3.11 for this course. We will be installing a host of tools to help us with our development
process.

These include:

* [homebrew](https://brew.sh/) (macOS only)
* [pyenv](https://github.com/pyenv/pyenv)
* [Python 3.11](https://www.python.org/)
* [micromamba](https://micromamba.readthedocs.io/en/latest/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [pipx](https://pypa.github.io/pipx/) (optional)
* [poetry](https://python-poetry.org/) (optional)

## Homebrew

Homebrew is a package manager for macOS. It allows us to install software that is not included in the base macOS install
or that is not available via the App Store.

It enables us to install software via the command line, and instead of having to search for a download link, we can
simply invoke the following command:

```bash
brew install <package>
```

Homebrew will then download the package and install it for us, it even takes care of dependencies and allows us to
install applications that require a GUI.

### Installing Homebrew

To install Homebrew, simply open a terminal and paste the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This will download and install Homebrew for you.

You will be asked to enter your password, as Homebrew needs to be installed in a system directory.

Once the installation is complete, you can verify that it was successful by running the following command:

```bash
brew --version
```

If an error message is displayed, please try to restart your terminal and try again.

### Installing packages with Homebrew

To install a package with Homebrew, simply run the following command:

```bash
brew install <package>
```

To update a package, run the following command:

```bash
brew upgrade <package>
```

To update all packages, run the following command:

```bash
brew upgrade
```

To uninstall a package, run the following command:

```bash
brew uninstall <package>
```

### Troubleshooting

If you encounter any issues with Homebrew, please refer to the [Troubleshooting](https://docs.brew.sh/Troubleshooting).

You can also use the `brew doctor` command to check for common issues.

## pyenv

pyenv is a tool that allows us to install and manage multiple versions of Python on our system.

This is especially useful if you are working on multiple projects that require different versions of Python, as python
versions are not backwards compatible.

### Installing pyenv

To install pyenv, simply run the following command:

```bash
brew install pyenv
```

If you are able to run the `pyenv` command, you have successfully installed pyenv, otherwise please refer to
the [Configuring the shell](#configuring-the-shell) section.

#### Configuring the shell

If you are unable to run the `pyenv` command, you will need to configure your shell to use pyenv.

> **Note:** Between macOS 10.15 and 11.0, Apple changed the default shell from bash to zsh. If you are using macOS 10.15
> or later, you will need to configure zsh instead of bash. To check which shell you are using, run the following
> command: `ps -o comm= $$`

```admonish info title="What is a shell?" collapsible=true

A shell is a program that acts as an interface between the user and the operating system.
It allows users to interact with the computer by typing commands and receiving their result.
Think of it as the "translator" between you and the computer.

When you open a terminal on your computer, you're essentially opening a shell. It provides a text-based environment
where you can run various commands to perform tasks like navigating through files and directories, running programs, managing files and more.

The shell takes the commands you type and sends them to the operating system for execution.
It then displays the results or any error messages back to you. This way, you can control the computer and perform tasks without relying solely on graphical interfaces.

Different operating systems have different types of shells.
For example, Unix-like systems like Linux and macOS typically use the Bash (**B**ourne **A**gain **Sh**ell) or Zsh (**Z** **Sh**ell).

```

Once you have added the lines to your shell configuration file, you will need to restart your terminal.

Depending on the shell you are using, you will need to add the following lines to your shell configuration file:

##### Bash

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bashrc
echo 'eval "$(pyenv init -)"' >>~/.bashrc

BASH_PROFILE=0

if [ -e ~/.bash_profile ]; then
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.bash_profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bash_profile
  echo 'eval "$(pyenv init -)"' >>~/.bash_profile
    BASH_PROFILE=1
fi

if [ -e ~/.profile ] && [ $BASH_PROFILE -eq 0 ]; then
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.profile
  echo 'eval "$(pyenv init -)"' >>~/.profile
fi
```

##### Zsh

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.zshrc
echo 'eval "$(pyenv init -)"' >>~/.zshrc

ZPROFILE=0

if [ -e ~/.zprofile ]; then
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.zprofile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.zprofile
  echo 'eval "$(pyenv init -)"' >>~/.zprofile
  ZPROFILE=1
fi

if [ -e ~/.zlogin ] && [ $ZPROFILE -eq 0 ]; then
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.zlogin
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.zlogin
  echo 'eval "$(pyenv init -)"' >>~/.zlogin
fi

```

### Installing Python with pyenv

To install Python with pyenv, simply run the following command:

```bash
pyenv install <version>
```

You can list all available versions of Python by running the following command:

```bash
pyenv install --list
```

We will install the latest version of Python 3.11, to find out the latest version, run `pyenv install --list`, then
scroll through the list until you find the latest version of Python 3.11. (simply called `3.11.X`, chose the version
where `X` is the highest number, do **not** choose versions that have `rc`, `b`, `dev`, or `a` in their name)

~~~admonish note title="Fully automatic installation" collapsible=true

You can also install Python 3.11 through the following fully automatic command:

```bash
pyenv install "$(pyenv install --list | grep -e '^[[:space:]]*3.11' | tail -n 1 | xargs)"
```

Let's break this command down:

* `pyenv install --list` lists all available versions of Python
* `| grep -e '^[[:space:]]*3.11'` take the output of the previous command and filter it to only include lines that
  start with `3.11` (including any leading whitespace)
* `| tail -n 1` take the output of the previous command and only include the last line (which is the latest version)
* `| xargs` take the output of the previous command and remove any leading or trailing whitespace

We then take the output of the previous command and use it as an argument for the `pyenv install` command.
~~~

Once the installation is complete, you can verify that it was successful by running the following command:

```bash
pyenv versions
```

This will list all installed versions of Python, you should see the version you just installed.

### Using Python with pyenv

To use a specific version of Python, simply run the following command:

```bash
pyenv global <version>
```

This will set the specified version of Python as the default version, in any new terminal window. You can verify that it
was successful by running the following command:

```bash
python --version
```

This will print the version of Python that is currently being used.

### Using Python with pyenv in VSCode

To use a specific version of Python in VSCode, you will need to install
the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Once the extension is installed, you will need to configure it to use the version of Python you want.

To do this, open the command palette (by pressing `cmd + shift + p`), then search for `Python: Select Interpreter`,
then select the version of Python you want to use. You can verify that it was successful by running the following
command in the VSCode terminal:

```bash
python --version
```

The pyenv version will be recommended by default, but you can also select other versions of Python that are installed on
your system. You can verify that you selected the correct version by looking at the path you're selecting, it should be
something like `/Users/<username>/.pyenv/versions/<version>/bin/python` or `/Users/<username>/.pyenv/shims/python3`.

## Installing micromamba

micromamba is a lightweight version of mamba, which is a lightweight version of conda. micromamba is a package manager
for Python, which allows you to install Python packages.

There are a multitude of package managers for Python, the data-science community has mostly converged on using
conda/mamba for managing Python packages, while the rest of the Python community has mostly converged on using
pip/poetry for managing Python packages.

We will be using micromamba to install Python packages, but you can also use pip/poetry if you prefer.

### Installing micromamba with Homebrew

To install micromamba with Homebrew, simply run the following command:

```bash
brew install micromamba
```

## Installing pipx

pipx is a tool that allows you to install Python packages globally, without polluting your system Python installation,
this is important because you don't want to install Python packages globally with pip, as this can cause issues with
other Python applications on your system.

### Installing pipx with Homebrew

To install pipx with Homebrew, simply run the following command:

```bash
brew install pipx
```

You can then install Python packages globally with pipx, for example:

```bash
pipx install poetry
```

## Installing poetry

poetry is a tool that allows you to manage Python packages, it is similar to pip, but it is more modern and has more
features.

### Installing poetry with Homebrew

To install poetry with Homebrew, simply run the following command:

```bash
brew install poetry
```

## Installing VSCode

VSCode is a popular code editor which we will be using for this course, if you prefer to use a different code editor,
you can skip this section, but be aware that sections in this course that are specific to VSCode will not be applicable
to you. (These sections will be clearly marked)

### Installing VSCode with Homebrew

To install VSCode with Homebrew, simply run the following command:

```bash
brew install --cask visual-studio-code
```

### Installing VSCode via the website

You can also install VSCode by downloading it from the [VSCode website](https://code.visualstudio.com/).

## Installing VSCode extensions

VSCode extensions are plugins that add additional functionality to VSCode, we will be installing a few extensions that
are useful for Python development. You can install extensions by searching for them in the VSCode extensions tab, or by
running the following command:

```bash
code --install-extension <extension>
```

### Installing the Python extension

The Python extension is the most important extension for Python development, it adds a lot of useful features to VSCode,
such as linting, debugging, and code completion. To install it, simply run the following command:

```bash
code --install-extension ms-python.python
```

> **Note:** You can also install the Python extension by searching for it in the VSCode extensions tab.


