#!/bin/zsh

# add files first
git add --all
git commit -am "change file $*"

# pull code using rebase mode
git pull --rebase

# push code
git push
