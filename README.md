# Docker


## Que es docker y por que lo usamos?

Docker es un software nos permite empaquetar nuestras aplicaciones de manera aislada con todas sus dependencias mediante contenedores de linux

Esto nos  permite distruibuir las aplicaciones de manera muy sencilla ya que son autosuficientes y se pueden ejecutar en cualquier tipo de maquina que tenga docker



## Como funciona docker Docker client server architecture

![docker-client-server](https://docs.docker.com/engine/images/architecture.svg)

Si vemos la version de docker nos dara la version del engine y del cliente

```    
docker version

    Client: Docker Engine - Community
    Version:           20.10.16
    API version:       1.41
    Go version:        go1.17.10
    Git commit:        aa7e414
    Built:             Thu May 12 09:17:23 2022
    OS/Arch:           linux/amd64
    Context:           default
    Experimental:      true

    Server: Docker Engine - Community
    Engine:
    Version:          20.10.16
    API version:      1.41 (minimum version 1.12)
    Go version:       go1.17.10
    Git commit:       f756502
    Built:            Thu May 12 09:15:28 2022
    OS/Arch:          linux/amd64
    Experimental:     false
    containerd:
    Version:          1.6.4
    GitCommit:        212e8b6fa2f44b9c21b2798135fc6fb7c53efc16
    runc:
    Version:          1.1.1
    GitCommit:        v1.1.1-0-g52de29d
    docker-init:
    Version:          0.19.0
    GitCommit:        de40ad0
```

con este comando podemos ver el estado del daemon
```
systemctl status docker.socket
```

Un problema tipico es que el daemon este parado
```
$ docker ps
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

## Docker images

Las imagenes de docker son un sistema de ficheros con instrucciones sobre como ejecutar un contenedor.
Podriamos ver las imagenes como las clases en programacion orientada a objetos, de una clase podemos crear instancias como de una imagen podemos crear contenedores.
Ademas las imagenes son extendibles se puede crear una imagen con otra como base algo similar a la herencia

## Docker containers

Los contendores son una imagen en ejecución, podemos ejecutar muchos contenedores de la misma imagen

## Dockerfile

Es un archivo de texto que contiene instrucciones para crear una imagen

### Commandos

-   **FROM** Imagen de la cual partimos "heredamos"
-   **COPY** Copiar un archivo o carpeta a la imagen
-   **RUN** Comandos que se ejecutan **cuando contruyes la imagen**
-   **CMD** Comandos que se ejecutan **cuando ejecutas el contenedor** facilmente sobreescribible
-   **ENTRYPOINT** Comando que se ejecuta **cuando ejecutas el contenedor** mas dificilmente sobreescribible

## Docker registries

Son lugares en los cuales podemos almacenar imagenes docker

![plot](./resources/docker.svg)


# TODO
#### Guardar imagen en tar y vice versa
### Docker images layers
## Dockerfiles
## Docker registries
## Containers

### container vs process

#### Definicion de runtime de un contenedor
a container is a sandbox for a process to isolate them
si miro los procesos desde un contenedor solo veo los suyos como es esto posible? por que tiene su propio namespace


si miro los procesos de la maquina host vere los procesos del conetenedor

`docker run -d ubuntu sleep infinity`
syntax `docker run {image} {command}`
https://www.youtube.com/watch?v=EnJ7qX9fkcU
https://www.youtube.com/watch?v=cjXI-yxqGTI
https://devopscube.com/keep-docker-container-running/
normalmente los hay un proceso por contenedor y ese proceso esta ligado al ciclo de vida del contenedor si inicias un contenedor inicias ese proceso y cuando ese proceso muere el contenedor tambien

ejemplo `docker run ubuntu sleep 20`

pero pueden haber mas procesos

`docker run --name sleep_container ubuntu sleep infinity`
`docker exec sleep_container sleep infinity`
`docker top sleep_container`

to run a process in the background `command &`

`docker run ubuntu sleep infinity &;sleep infinity &`
no hay dos processos # TODO

un contenedor esta empaquetado con todas sus dependencias lo cual es algo bastante unico e importante 

#### Container image
La base de todas las imagenes es scratch
que es un sistema de ficheros vacios

luego podemos tener por encima un sistema operativo como ubuntu debian busybox etc...

a binary representation a bunch of bits in the file sistem

Dockerfile the ubuntu
https://github.com/tianon/docker-brew-ubuntu-core/blob/fbca80af7960ffcca085d509c20f53ced1697ade/jammy/Dockerfiledebian

Dockerfile de debian
https://github.com/debuerreotype/docker-debian-artifacts/blob/337f494fae12a1db13a003cea38e74f43d312ee6/bookworm/Dockerfile
`nota: el comando ADD desempaqueta ese tar`
`nota: si quieres ver el dockerfile de una imagen de dockerhub haz click en los tags`


encima de ese sistema operativo podemos tener ciertas librerias de sistema/ lenguajes de programacion

python dockerfile

https://github.com/docker-library/buildpack-deps/blob/84e7e46026131a108a6480e5ed2969e8acf2d4e2/debian/bookworm/curl/Dockerfile
https://github.com/docker-library/python/blob/56cea612ab370f3d05b29e97466d418a0f07e463/3.10/bullseye/Dockerfile

y encima de esa imagen con librerias/ lenguajes de programacion podemos tener nuestra applicacion

son como snapshots de discos como cuando haces algo en una maquina virtual y lo guardas

##### TODO create a docker image of my ubuntu


### How do we build images Dockerfile

FROM es como la herencia

cada capa del dockerfile es como un layer

Podemos crear imagenes con el Dockerfile y con contenedores

podemos crear un contenedor de una imagen 
y podemos crear una imagen de un contenedor `docker commit`

#### linux process namespace

Namespaces are a feature of the Linux kernel that partitions kernel resources such that one set of processes sees one set of resources while another set of processes sees a different set of resources. The feature works by having the same namespace for a set of resources and processes, but those namespaces refer to distinct resources. Resources may exist in multiple spaces. Examples of such resources are process IDs, hostnames, user IDs, file names, and some names associated with network access, and interprocess communication. 

### docker container vs virtual machine
Son distintas formas de virtualizar

Las maquinas virtuales son virtualizacion hardware
machine isolation

Los contendores son virtualizacion a nivel de sistema operativo
process isolation

# TODO add image

#### SO namespace
#### cgroups



Los cgroups o grupos de control, son una característica del kernel Linux que permite que los procesos se organicen en grupos jerárquicos con el fin de limitar y monitorear el uso de varios tipos de recursos. Con cgroups cada proceso corre en su propio espacio del kernel y de la memoria. Cuando se tienen la necesidad, un administrador puede configurar fácilmente un cgroup para limitar los recursos que puede utilizar un proceso.

En concreto cgroups nos permite:

    Establecer límites de recursos: Se pueden asignar límites de recursos como CPU, memoria, I/O,  etc. a cada cgroup
    Realizar funciones de auditoría: Se puede medir el uso de los recursos de cada  cgroup
    Priorizar recursos: Se puede dar mayor proporción de algunos recursos a determinados grupos de control
    Etiquetar el tráfico de red con un identificador de clase para controlar el tráfico de red
    Congelar grupos de procesos, sus puntos de control y reinicio


#### Que es un kernel
Buscar que kernel tenemos `uname -r`
All kernel files are on the boot folder

`docker run -it --entrypoint /bin/sh ubuntu`
`ls boot`
esta vacio
`uname -r`
`5.13.0-41-generic`

 # TODO es el de mi maquina?
`docker run -it --entrypoint /bin/sh debian`
`uname -r`
`5.13.0-41-generic`

`docker run -it --entrypoint /bin/sh alpine`
`uname -r`
`5.13.0-41-generic`

`docker run -it --entrypoint /bin/sh vcatechnology/linux-mint`
`uname -r`
`5.13.0-41-generic`

`docker run -it --entrypoint /bin/sh ubuntu:14.04`
`uname -r`
`5.13.0-41-generic`

# Ubuntu22.04 VM

`uname -r`
`5.15.0-39-generic`


`docker run -it --entrypoint /bin/sh ubuntu`
`uname -r`
`5.13.0-41-generic`



No puedes ejecutar contenedores de windows en linux
No puedes ejecutar contenedores de linux en windows directamente, windows los ejecuta en hyper-v una maquina virtual o en wsl2

Is a program of the operating system to access and interact with hardware
cada sistema operativo tiene su propio kernel


docker top
docker inspect
## Usual workflow

## SCOPE introducir conceptos basicos crear imagen basica ejecturarla y pushearla a un registry

## Ventajas Inconvenientes
https://devopscube.com/run-docker-in-docker/#:~:text=To%20run%20docker%20inside%20docker,sock%20as%20a%20volume.&text=Just%20a%20word%20of%20caution,privileges%20over%20your%20docker%20daemon.


docker exec -it dind-test /bin/sh


### CMD vs ENTRYPOINT


### VOLUME


#TODO definir socket

```
curl -X GET --unix-socket /var/run/docker.sock http://localhost/images/json
```