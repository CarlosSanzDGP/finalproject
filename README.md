# finalproject

Objetivo; Entrenar un modelo capaz de deducri el color de un coche. 
Objetivo2: Enseñar al programa una foto de un coche y que sea capaz de decir que modelo es. 

El objetivo 1 es parte de un proyecto más complejo que debería ser capaz de cotejar el modelo de un coche con su matrícula en una foto tomada por un radar de velocidad o un parking público. 
De esta manera el programa podría decir si el modelo y color corresponde con su matrícula, avisando en su caso de que la matrícula es falsa o robada.

1.- El primer problema, como casi siempre, es conseguir un dataset que se ajuste lo máximo posible al proyecto que queremos realizar. En este caso habíamos elegido el famoso dataset 196 de coches de stanford, competición que sigue en curso, pero sus datos, a pesar de lo tremendamente extensos, no contenían la variable color que es la primera con la que queremos trabajar. 
Dataset https://ai.stanford.edu/~jkrause/cars/car_dataset.html?fbclid=IwAR2XibtbHU_dES8CXk5llA-CpwRm18Ntji1n72gcmLVkJLtZyk0zlTVYT_I

Tras mucha búsqueda, el dataset elegido es el que provee la Huazhong University of Science and Technology, Wuhan, Hubei, China. Aprovecho aquí para agradecer el trabajo y nombrar a los autores:
Vehicle Color Recognition on an Urban Road by Feature Context. Pan chen, Xiang bai and Wenyu Liu. Intelligent Transportation Systems, IEEE Transactions on (TITS), 2014, Issue: 99, Page(s): 1-7

2.-Tras elegir el dataset decidimos utilizar 4 de los 8 colores que ofrecen por distintas razones, en un caso por la poca cantidad de variables de cada clase (fotos de coches con ese color) y en otros porque el color que presentan no es homogéneo, con lo que puede ser demasiado fácil errar. 

3.- Limpiamos los colores de elegidos de algunos valores que considero erróneos, como coches dorados en carpeta de blancos y similares.

4.- Resize y normalizar las fotos. La idea es crear una funcion que convierta cada una de las fotos en una fotos de 64 x 64 para poder trabajar con ella.

5.- Creamos 

5.- Arquitectura neuronal






