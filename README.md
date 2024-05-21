# Git bisect demonstrator repository

This repository is used as a demonstrator repository for git bisect.

## Preparation

Before running below examples, please do the following:

```
./get-bisect-scripts.sh
```

This is required because bisect scripts cannot be in the repository
itself - unless they are present on all commits under consideration.

## Run the "application"

You can run the provided application with:

```
python app.py
```

## Bisecting the repository

Your goal is to find the commit that introduced the obvious math issue:

```
git bisect start
git bisect good v1
git bisect bad HEAD
git bisect run ./test.sh
git bisect reset
```

Alternatively, try `python perf.py` instead of `./test.sh`. 

## License

This repository is provided under the CC-0 license.
