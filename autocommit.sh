#!/bin/zsh

git pull --rebase

git add --all
git commit -am "change file $*"
gpv

