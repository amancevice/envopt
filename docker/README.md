# Example use of envopt in a Dockerfile

Use `docker-compose` to see how different options interact with each other.

```bash
docker-compose up -d > /dev/null 2>&1
docker-compose logs envopt_0
echo
docker-compose logs envopt_1
docker-compose down --rmi local > /dev/null 2>&1
```

Output:

```
Attaching to docker_envopt_0_1
envopt_0_1  | --option-a :: I started life in the Dockerfile
envopt_0_1  | --option-b :: I also started life in the Dockerfile
envopt_0_1  | --option-c :: I am a hardcoded default in myscript.py
envopt_0_1  | --option-d :: None

Attaching to docker_envopt_1_1
envopt_1_1  | --option-a :: I started life in the Dockerfile
envopt_1_1  | --option-b :: I was passed at runtime as part of the CMD
envopt_1_1  | --option-c :: I am a hardcoded default in myscript.py
envopt_1_1  | --option-d :: I was passed at runtime as an ENV variable```
