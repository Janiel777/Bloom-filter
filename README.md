## Bloom Filter
Este proyecto es una implementación de un filtro de Bloom en Python. Un filtro de Bloom es una estructura de datos probabilística utilizada para verificar si un elemento pertenece a un conjunto. En lugar de almacenar todos los elementos en el conjunto, el filtro de Bloom utiliza varias funciones hash para mapear los elementos a un conjunto de posiciones en un bit array. Luego, para verificar si un elemento pertenece al conjunto, se aplican las mismas funciones hash a ese elemento y se comprueba si todos los bits correspondientes en el bit array están encendidos. Si todos los bits están encendidos, es probable que el elemento pertenezca al conjunto; de lo contrario, se puede decir con certeza que el elemento no está en el conjunto. Se dice que "es probale" que este en el conjunto por eso de que pueden ocurrir colisiones en el que dos elementos produscan las mismas posiciones en el bit array.

Este proyecto implementa un filtro de Bloom que utiliza múltiples funciones hash, lo que mejora su precisión en la detección de elementos en el conjunto y reduce la probabilidad de falsos positivos. El número de funciones hash utilizadas depende del tamaño del conjunto y la tasa de error aceptable.

La tasa de error aceptable se utiliza para determinar el tamaño del bit array utilizado para el filtro de Bloom, y por lo tanto, el número de funciones hash necesarias. Cuando se crea una instancia de la clase BloomFilter, se especifica el tamaño esperado del conjunto y la tasa de error aceptable. El tamaño del bit array se calcula a partir de estos valores, y el número de funciones hash se calcula automáticamente en función del tamaño del bit array. La taza de error aceptable es la probabilidad con la que cocurran los falsos positivos.

La clase BloomFilter utiliza una implementación personalizada de un bit array, representado como una cadena de bits almacenada en una variable de tipo str. Esta implementación permite un manejo eficiente de los bits individuales del bit array. La clase BitArray define métodos para establecer y obtener bits en una posición específica en la cadena de bits.

### Uso
Para utilizar este filtro de Bloom en tu propio proyecto, simplemente agrega el archivo bloom_filter.py a tu proyecto y crea una instancia de la clase BloomFilter. Luego, puedes agregar elementos al filtro utilizando el método add y verificar si un elemento está presente utilizando el método contains.

```python
from bloom_filter import BloomFilter

bf = BloomFilter(1000, 0.01)
bf.add("ejemplo")
bf.add("otro ejemplo")

if bf.contains("ejemplo"):
      print("El elemento 'ejemplo' está en el filtro.")
else:
      print("El elemento 'ejemplo' no está en el filtro.")
```

En este ejemplo, se crea un filtro de Bloom con una capacidad para 1000 elementos y una tasa de error aceptable del 1%. Se agregan dos elementos al filtro, y luego se verifica si el elemento "ejemplo" está presente. Si está presente, se imprime un mensaje indicando que el elemento se encuentra en el filtro; de lo contrario, se imprime un mensaje indicando que no está en el filtro.

### Contribuciones
Si encuentras algún error o tienes alguna sugerencia de mejora, ¡no dudes en contribuir al proyecto!
