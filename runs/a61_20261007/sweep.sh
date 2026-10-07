cd "$(dirname "$0")"
cat verify/sweep/todo.txt | xargs -P 12 -I{} sh -c '[ -f verify/sweep/sheet_{}.jpg ] || python3 frames.py sheet {} verify/sweep/sheet_{}.jpg'
