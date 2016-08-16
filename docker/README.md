# Example use of envopt in a Dockerfile

Use `docker-compose` to see how different options interact with each other.

```bash
docker-compose up && dockerc-compose down --rmi local
```

Output:

```
...
Creating network "docker_default" with the default driver
Creating docker_envopt_0_1
Creating docker_envopt_1_1
Attaching to docker_envopt_0_1, docker_envopt_1_1
envopt_0_1  | --option-a :: I started life in the Dockerfile
envopt_0_1  | --option-b :: I also started life in the Dockerfile
envopt_0_1  | --option-c :: I am a hardcoded default in myscript.py
envopt_0_1  | --option-d :: None
envopt_1_1  | --option-a :: I started life in the Dockerfile
envopt_1_1  | --option-b :: I was passed at runtime and overrode the ENV variable
envopt_1_1  | --option-c :: I am a hardcoded default in myscript.py
envopt_1_1  | --option-d :: I was passed at runtime and did not override anything
docker_envopt_0_1 exited with code 0
docker_envopt_1_1 exited with code 0
```
