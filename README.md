### OBJETIVO ###
Descubrir puertos abiertos en un HOST.



### ESTRUCTURA DEL REPO ###
dev -> Herramienta de ayuda para configurar el ambiente de desarrollo.
build -> Herramienta de ayuda para la construcción del paquete ejecutable.
deploy -> Herramienta de ayuda para el despliegue del paquete ejecutable en la plataforma destino.

doc -> Documentación.
doc/tst -> Documentación de los casos de uso.
src -> Componentes funcionales necesarios para el proyecto (Códigos, recursos de configuración, recursos multimedia, otros).
tst -> Componentes para ejecutar pruebas.

dump/lib -> Copia (o enlace con verificación de integridad) de cada una de las librerías utilizadas.



### Getting started ###
Nota: Revisar información más detallada en la documentación.

CASO DE USO MÁS COMÚN - Descubrir puertos comunes
1. Indicar el HOST mediante la IPv4.
2. Para el escaneo de puertos: Indicar con la letra   d   que se realizará escaneo de puertos comunes.
3. Esperar a que aparezca la leyenda "Escaneo completado".
4. Fin del caso de uso.

CASO DE USO MÁS COMÚN - Descubrir puertos indicados en la tarea (1 al 200)
1. Indicar el HOST mediante la IPv4.
2. Para el escaneo de puertos: Indicar con la palabra   tarea   que se realizará escaneo de puertos 1 al 200.
3. Esperar a que aparezca la leyenda "Escaneo completado".
4. Fin del caso de uso.
