#!/bin/sh
docker build -t template .
mkdir -p $HOME/bin
grep -qxF 'export "PATH=$PATH:$HOME/bin"' ~/.bash_profile || echo 'export "PATH=$PATH:$HOME/bin"' >> ~/.bash_profile
install -m 0755 template-wrapper $HOME/bin/template
