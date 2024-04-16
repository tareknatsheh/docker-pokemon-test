## Docker example: Pokemon

### Prerequisites
Docker desktop
(You don't even need to have python installed in your machine)

### Quick start
1. Go to the terminal and navigate to the project root
2. Run this: `docker build -t test-pokemon .`
3. After the image build is finished, run the image by executing this:
`docker run -d -p 8000:8000 --name pokemon test-pokemon`

That's it!
If everything worked as expected, you'll be able to explore the API at this enpoint:
`http://localhost:8000/api/getpokemon?name=<pokemon name>`

Replace `<pokemon name>` with the name of the pokemon you want to get data about.
For example try this:

`http://localhost:8000/api/getpokemon?name=pikachu`

## Note
Go and open Docker Desktop.
You'll be able to see the running containers and the available images.
You can run/stop/delete as you like using Docker Desktop if you don't want to bother with the command line commands.