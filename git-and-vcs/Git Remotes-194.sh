## 1. Git remotes ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making changes to cloned repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. The master branch ##

/home/dq/chatbot$ git branch

## 4. Pushing changes to the remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing individual commits ##

/home/dq/chatbot$ git show $HASH -q

## 6. Commits and the working directory ##

/home/dq/chatbot$ git --no-pager diff $HASH2 $HASH

## 7. Switching to a specific commit ##

/home/dq/chatbot$ git reset --hard $HASH

## 8. Pulling from a remote repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the most recent commit ##

/home/dq/chatbot$ git reset --hard HEAD~1