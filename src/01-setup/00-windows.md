# Setup - Windows

To follow this course, you will need to install a few programs. This page will guide you through the installation
process. We will be using the following programs:

* [pyenv](https://github.com/pyenv/pyenv)
* [Python 3.11](https://www.python.org/)
* [micromamba](https://micromamba.readthedocs.io/en/latest/)
* [Visual Studio Code](https://code.visualstudio.com/)

These installation instructions require you to open the powershell as an administrator.

## Installing pyenv

For more detailed explanation, please refer to the [pyenv installation instructions](.#installing-pyenv).

To install pyenv, run the following command in the powershell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

## Installing Python with pyenv

For more detailed explanation, please refer to the [Python installation instructions](.#installing-python-with-pyenv).

To install Python 3.11, run the following command in the powershell:

```powershell
pyenv install 3.11.X
```

We will install the latest version of Python 3.11. To find out the latest version, run `pyenv install --list` and look
for the latest version of Python 3.11.

## Installing micromamba

For more detailed explanation, please refer to the [micromamba installation instructions](.#installing-micromamba).

To install micromamba, run the following command in the powershell:

```powershell
Invoke-Webrequest -URI https://micro.mamba.pm/api/micromamba/win-64/latest -OutFile micromamba.tar.bz2

tar xf micromamba.tar.bz2

.\micromamba.exe --help
```

To install the latest version of micromamba, you first need to create a new directory for micromamba, here we will
create a directory called `micromamba` in the root of the `C:` drive. (You can also create the directory somewhere else,
but you will need to adjust the path in the following commands.)

```powershell
mkdir C:\micromamba
```

To then install the latest version of micromamba, run the following command in the powershell:

```powershell
$Env:MAMBA_ROOT_PREFIX="C:\micromamba"
.\micromamba.exe shell hook -s powershell | Out-String | Invoke-Expression
```

Then, initialise the powershell to recognise micromamba:

```powershell
micromamba shell init -s powershell -p C:\micromamba
```

## Installing Visual Studio Code

For more detailed explanation, please refer to
the [Visual Studio Code installation instructions](.#installing-visual-studio-code).

To install Visual Studio Code head over to the [Visual Studio Code website](https://code.visualstudio.com/) and download
the installer. Then, run the installer and follow the instructions.

