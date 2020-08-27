1.1 OS Packages

$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update

1.2 Using Pyenv

$ PROJECT=https://github.com/pyenv/pyenv-installer \
  PATH=raw/master/bin/pyenv-installer \
  curl -L $PROJECT/PATH | bash

$ git clone https://github.com/pyenv/pyenv-installer
$ cd pyenv-installer
$ bash pyenv-installer

export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ pyenv install <version>

$ pyenv global 3.7.0

$ pyenv local 3.7.0


