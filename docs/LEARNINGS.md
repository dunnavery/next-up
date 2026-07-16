# Tracking my learnings from building NextUp along the way

- SQLAlchemy is an Object-Relational Mapping (ORM) library for Python, used to communicate with relational databases through Python code

- FastAPI + Uvicorn: uvicorn is an ASGI (asynchronous server gateway interface) web server implementation for Python
- FastAPI framework only defines API logic, routing, and data validation. Does not know how to natively handle raw network sockets or HTTP streams, uvicorn fills gap by acting as bridge between internet and Python code

## Docker
Tutorial

What is a container? Another process on your machine that has been isolated from all other processes on the host machine.

What is a container image? A running container uses an isolated filesystem. This custom filesystem is provided by a container image. The image contains the container's file system and everything else needed to run the application (dependencies, configuration, scripts, binaries, etc). Image contains environment variables, default command to run, and other metadata.

What is a Dockerfile? Dockerfile is a text-based script of instructions that is used to create a container image.

When a container runs, it uses various layers from an image for its filesystem
- Each container gets its own scratch space to create/update/remove files
- Any changes won't be seen in another container even if they are using the same image

Volumes provide ability to connect specific filesystem paths of the container back to the host machine
- If directory in container is mounted > changes in that directory are also seen on host machine
- If we mount same directory across container restarts, we'd see the same files
Named volume = bucket of data, docker maintains physical location on the disk and you only need to remember the name of the volume
Named volumes, used to persist data in our database, great if we simply want to store data, don't have to worry about where the data is stored

Bind mounts, also used to persist data, can control the exact mountpoint on the host. Often used to provide additional data into containers.
- E.g. can use bind mount to mount our source code into the container to let it see code changes, respond, and let use see changes right away

In general: each container should do one thing and do it well.

Containers by default run in isolation and don't know anything about other processes or containers on the same machine. We use networking to allow one container to talk to another: if two containers are on the same network, then they can talk to each other. If they aren't, they can't.

Docker Compose: tool that was developed to help define and share multi-container applications
- Create a YAML file to define the services and with a single command, spin everything up and tear everything down
- Advantage: define application stack in a file, keep it at root of project repo, and easily enable someone else to contribute to your project


## Backend Questions to Answer
1. Why do I have a Pydantic schema and a SQLAlchemy model?
2. Why shouldn't my endpoint talk directly to the database?
3. Why does FastAPI use dependency injection (`Depends`)?
4. Why do we create a close sessions per request?
