# aghpb_parser
This is a parser of [Anime-Girls-Holding-Programming-Books](https://github.com/cat-milk/Anime-Girls-Holding-Programming-Books) repository.  

## Usage  
1. Run `git clone https://github.com/synalice/aghpb_parser.git`
2. Run `cd aghpb_parser`
3. Run `poetry install` _(or install dependencies from pyproject.toml yourself. The ones you need are under [tool.poetry.dependencies])_.
4. Run the programm  
5. You should have gotten a message in the console that Uvicorn server is running

Now you can search for `localhost:8000/anime-girls/<programming language>`.  
Instead of `<programming language>` enter something of your choice. If everything was done right, you should have gotten JSON response with multiple _(of few, if there are not a lot of results)_ links to images.
