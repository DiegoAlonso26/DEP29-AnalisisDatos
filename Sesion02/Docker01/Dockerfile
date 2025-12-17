# Referenciar una imagen Base de Python - Ubuntu
FROM  ubuntu:20.04

# evitar que el SO retire alguna instalacion manual
ENV DEBIAN_FRONTEND=noninteractive

# actualizaciones de sistemas e instalacion de paquetes
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget && \
    apt-get clean

# Instalar el jupyet
RUN pip3 install --upgrade pip && \
    pip3 install notebook==6.5.6

# definir el directorio de trabajo
WORKDIR /workspace

# Crear el directorio donde guardaremos las configuraciones de los usuarios jupyter
RUN mkdir -p /root/.jupyter

# Configuraciones Basicas
# deshabilitar la aut por token y contraseña
# Evitar que se habra el navegador de forma automatica
# permitir el uso como root
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py

# Exponer el puerto 8888
EXPOSE 8888

# Comando por defecto
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]