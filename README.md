# Docker


## Que es docker y por que lo usamos?

Docker nos permite empaquetar nuestras aplicaciones de manera aislada con todas sus dependencias

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

Los contendores son una imagen en ejecución podemos ejecutar muchos contenedores de la misma imagen

## Dockerfile

Es un archivo de texto que contiene instrucciones para crear una imagen

## Docker registries

Son lugares en los cuales podemos almacenar imagenes docker

![plot](./resources/docker.svg)