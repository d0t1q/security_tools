find . -name ".git" -type d | sed 's/\/.git//' |  xargs -P10 -I{} git -C {} pull origin master
