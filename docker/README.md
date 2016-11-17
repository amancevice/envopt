# Example use of envopt in a Dockerfile

See the example [Dockerfile](./Dockerfile) to illustrate the setting of `ENV` variables there.

Building this file with:

```bash
docker build -t envopt:example .
```

We can see the default help message:

```bash
docker run --rm envopt:example --help
```

```
Sample envopt script.

Usage:
    myscript.py [options]

Options:
    -a --option-a OPT  # A [default: I was set in the Dockerfile]
    -b --option-b OPT  # B [default: I was also set in the Dockerfile]
    -c --option-c OPT  # C [default: I am hardcoded in myscript.py]
    -d --option-d OPT  # D
```

We can choose to run the container with no extra configuration:

```bash
docker run --rm envopt:example
```

```
--option-a :: I was set in the Dockerfile
--option-b :: I was also set in the Dockerfile
--option-c :: I am hardcoded in myscript.py
--option-d :: None
```

Or we can pass arguments through via the `CMD` parameter of the docker command:

```bash
docker run --rm envopt:example \
  --option-b "I was overridden as part of the CMD"
```

```
--option-a :: I was set in the Dockerfile
--option-b :: I was overridden as part of the CMD
--option-c :: I am hardcoded in myscript.py
--option-d :: None
```

Or we can pass arguments through via `ENV` variables:

```bash
docker run --rm \
  --env MYSCRIPT_OPTION_D="I was set with --env MYSCRIPT_OPTION_D" \
  envopt:example
```

```
--option-a :: I was set in the Dockerfile
--option-b :: I was also set in the Dockerfile
--option-c :: I am hardcoded in myscript.py
--option-d :: I was set with --env MYSCRIPT_OPTION_D
```

We can even mix-and-match the two, but the options passed via `CMD` will always win:

```bash
docker run --rm \
  --env MYSCRIPT_OPTION_A="I was set with --env MYSCRIPT_OPTION_A" \
  --env MYSCRIPT_OPTION_B="I was set with --env MYSCRIPT_OPTION_B" \
  --env MYSCRIPT_OPTION_C="I was set with --env MYSCRIPT_OPTION_C" \
  --env MYSCRIPT_OPTION_D="I was set with --env MYSCRIPT_OPTION_D" \
  envopt:example\
    --option-d "I was overridden as part of the CMD"
```

```
--option-a :: I was set with --env MYSCRIPT_OPTION_A
--option-b :: I was set with --env MYSCRIPT_OPTION_B
--option-c :: I was set with --env MYSCRIPT_OPTION_C
--option-d :: I was overridden as part of the CMD
```
