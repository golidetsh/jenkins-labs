TIMES=1
for i in $(eval echo "{1..$TIMES}")
do
    siege -c 1 -r 10 http://localhost:8000/docs
    siege -c 3 -r 5 http://localhost:8000/posts/2
    siege -c 2 -r 10 http://localhost:8000/posts
    sleep 5
done
