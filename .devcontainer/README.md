This is the folder that builds the codespace environment.

The build command goes like:

    docker build --platform linux/amd64,linux/arm64 -f .devcontainer/Dockerfile -t swen-230-p3 .

Then it needs to be tagged like so:

    docker tag swen-230-p3 us.gcr.io/gcpdrive-sjstest/sw230-p3:2

and then pushed

    docker push us.gcr.io/gcpdrive-sjstest/sw230-p3:2

