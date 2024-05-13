FROM mcr.microsoft.com/devcontainers/anaconda:0-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends build-essential gdb

RUN apt-get install -y cmake zip

RUN apt-get install -y valgrind

RUN apt-get install -y python3 python3-dev python3-pip python3-setuptools python3-pytest

RUN mkdir /gtest

RUN cd /gtest/ && wget https://github.com/google/googletest/archive/main.zip && unzip main.zip && cmake -DCMAKE_CXX_STANDARD=14 ./googletest-main/ && make && make install

RUN pip3 install cython

RUN apt-get install -y clang-format

RUN pip3 install numpy jupyter matplotlib

RUN apt-get install -y gsl-bin libgsl-dbg libgsl-dev libgslcblas0

RUN pip3 install flask

RUN pip3 install --upgrade watchdog

