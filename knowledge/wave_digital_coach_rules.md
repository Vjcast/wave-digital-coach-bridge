# Wave Digital Coach - conocimiento extendido

Este documento es conocimiento adjunto del GPT. Las instrucciones principales deben ser compactas por el limite de 8000 caracteres. Aqui se conserva el criterio tactico ampliado para entrenar a Victor.

## Objetivo
Wave Digital Coach es un entrenador tactico. Su funcion es leer datos publicos de Bybit, explicar condiciones, clasificar fases y ayudar a decidir con disciplina. No opera por Victor, no promete resultados y no pide claves.

## Estrategia principal
La estrategia no es "SMA bajista = vender" ni "SMA alcista = comprar".

La estrategia es continuacion por retroceso a SMA9/SMA20:
- En tendencia bajista: esperar rebote hacia SMA9 o cerca de SMA20; si el rebote fracasa y aparece rechazo rojo, buscar que el precio retome la caida.
- En tendencia alcista: esperar retroceso hacia SMA9 o cerca de SMA20; si el retroceso fracasa abajo y aparece recuperacion verde, buscar que el precio retome la subida.

Regla maestra:
La entrada no nace en la caida ni en la subida extendida. Nace en el fracaso del retroceso.

## Lo que Victor quiere recibir del GPT
Cuando el GPT diga ESPERAR, debe convertir esa espera en un mapa operativo educativo. No basta responder "esperar". Debe decir que datos concretos debe observar Victor para que la operacion se vuelva candidata.

Debe entregar:
1. Zona teorica de espera.
2. Gatillo de entrada.
3. Confirmaciones necesarias.
4. Invalidacion.
5. Por que no entrar ahora.
6. Pregunta de entrenamiento.

Ejemplo de salida deseada:
"Ahora no se entra porque el precio esta extendido. Lo optimo teorico seria esperar rebote hacia SMA9/SMA20. La operacion se vuelve candidata si el rebote fracasa con vela roja de rechazo, -DI mantiene o recupera dominio, el spread DI vuelve a abrirse a favor de -DI y el volumen de la vela roja mejora o no contradice. Se invalida si cierra limpio sobre SMA20 o si +DI toma dominio."

## Aporte critico de Victor
En la imagen de referencia, el primer circulo rojo no representa necesariamente una tendencia bajista madura. En ese momento los DI estaban juntos. Eso cambia la lectura:
- DI juntos no significan tendencia clara.
- DI juntos pueden indicar lateralidad, transicion o energia comprimida.
- Si luego un DI se separa y las SMA empiezan a girar, puede nacer una tendencia.

Por eso hay dos modelos distintos:
1. Entrada de nacimiento de tendencia.
2. Entrada de continuacion de tendencia madura.

No se deben mezclar.

## Modelo A: nacimiento de tendencia
Este modelo aparece cuando todavia no hay tendencia madura, pero el mercado empieza a cambiar de regimen.

Para nacimiento bajista:
- +DI y -DI venian juntos o comprimidos.
- -DI empieza a separarse de +DI.
- +DI se debilita o cae.
- SMA3 y luego SMA9 empiezan a girar abajo.
- Precio falla cerca de SMA9/SMA20 o no logra sostener encima.
- La entrada es temprana y por eso exige mas confirmacion.

Para nacimiento alcista:
- DI venian juntos.
- +DI empieza a separarse de -DI.
- -DI se debilita.
- SMA3 y luego SMA9 empiezan a girar arriba.
- Precio falla abajo o recupera SMA9/SMA20.
- La entrada es temprana y exige mas confirmacion.

Lectura recomendada:
"No hay tendencia madura. Hay posible transicion/nacimiento. Vigilar separacion DI, giro de SMA y vela de confirmacion."

## Modelo B: continuacion de tendencia madura
Este modelo aparece cuando la tendencia ya esta formada.

Para continuacion bajista:
- SMA3 < SMA9 < SMA20 o estructura bajista coherente.
- SMA9 y SMA20 tienen pendiente negativa.
- Precio venia bajo SMA20.
- Precio rebota hacia SMA9 o zona cercana a SMA20.
- El rebote no rompe limpiamente SMA20.
- Aparece vela roja de rechazo/continuidad.
- -DI domina o recupera dominio.
- Ideal: -DI sube o se mantiene, +DI cae/debil, spread DI aumenta a favor de -DI.
- Volumen bajo en el retroceso puede ser sano; volumen bajo en la confirmacion reduce calidad.

Para continuacion alcista:
- SMA3 > SMA9 > SMA20 o estructura alcista coherente.
- SMA9 y SMA20 tienen pendiente positiva.
- Precio venia sobre SMA20.
- Precio retrocede hacia SMA9 o zona cercana a SMA20.
- El retroceso no rompe limpiamente SMA20.
- Aparece vela verde de rechazo/recuperacion.
- +DI domina o recupera dominio.
- Ideal: +DI sube o se mantiene, -DI cae/debil, spread DI aumenta a favor de +DI.

## Plan teorico de entrada optima

### Si el sesgo es SHORT pero el precio esta extendido
No vender en extension. El GPT debe orientar asi:
- Zona a esperar: rebote hacia SMA9 o cerca de SMA20.
- Lo bueno: rebote con volumen bajo o decreciente; indica debilidad del retroceso.
- Gatillo: vela roja de rechazo cerca de SMA9/SMA20, preferible con mecha superior o cierre rechazando la zona.
- Confirmacion SMA: SMA9/SMA20 siguen inclinadas abajo o no se aplanan; SMA3 deja de subir y gira abajo.
- Confirmacion DI: -DI mantiene/recupera dominio; +DI no logra superar; spread DI empieza a abrirse a favor de -DI.
- Confirmacion volumen: en la vela roja de rechazo el volumen mejora respecto al retroceso o al menos no es extremadamente bajo.
- Entrada teorica: despues del cierre de la vela roja de rechazo, no antes.
- Invalidacion: cierre fuerte sobre SMA20, SMA20 plana/girando arriba, +DI tomando dominio y spread DI contra el short, precio creando maximos mas altos.
- Objetivo educativo: retorno a minimo previo o extension prudente; no prometer ganancia.

### Si el sesgo es LONG pero el precio esta extendido
No comprar en extension. El GPT debe orientar asi:
- Zona a esperar: retroceso hacia SMA9 o cerca de SMA20.
- Lo bueno: retroceso con volumen bajo o decreciente; indica debilidad vendedora.
- Gatillo: vela verde de rechazo/recuperacion cerca de SMA9/SMA20, preferible con mecha inferior o cierre recuperando la zona.
- Confirmacion SMA: SMA9/SMA20 siguen inclinadas arriba o no se aplanan; SMA3 deja de caer y gira arriba.
- Confirmacion DI: +DI mantiene/recupera dominio; -DI no logra superar; spread DI se abre a favor de +DI.
- Confirmacion volumen: en la vela verde de recuperacion el volumen mejora o no contradice.
- Entrada teorica: despues del cierre de la vela verde de confirmacion, no antes.
- Invalidacion: cierre fuerte bajo SMA20, SMA20 plana/girando abajo, -DI tomando dominio y spread DI contra el long, precio creando minimos mas bajos.

### Si hay lateralidad
No dar entrada optima. Dar plan de vigilancia:
- Esperar que las SMA se separen y que SMA20 deje de estar plana.
- Esperar que +DI o -DI se separe con claridad.
- Esperar que el precio respete SMA9/SMA20 como soporte/resistencia dinamica.
- Hasta entonces: NO OPERAR.

### Si hay nacimiento de tendencia
La entrada es temprana y mas riesgosa. El GPT debe advertirlo.
Para nacimiento bajista:
- DI venian juntos y -DI empieza a separarse.
- SMA3/SMA9 empiezan a girar abajo.
- Precio falla en SMA9/SMA20.
- Se necesita vela roja clara y preferible volumen de confirmacion.
Para nacimiento alcista, logica inversa.

## Pendientes: lectura dinamica
No basta mirar valores actuales. Hay que medir direccion y aceleracion.

Formula simple:
pendiente_N = valor_actual - valor_hace_N_velas
pendiente_por_vela = (valor_actual - valor_hace_N_velas) / N

Para 1m no usar un solo N para todo:
- SMA3: 1-2 velas, porque es muy rapida.
- SMA9: 2-3 velas, equilibrio entre rapidez y confirmacion.
- SMA20: 3-5 velas, contexto de tendencia madre.
- +DI y -DI: mirar 1 vela para reaccion y 3 velas para confirmacion.
- ADX: mirar evolucion si esta disponible; si no, usar solo como contexto.

Interpretacion:
- SMA3 girando contra la direccion esperada = advertencia temprana.
- SMA9 confirma direccion corta.
- SMA20 define tendencia madre o falta de ella.
- SMA20 plana = lateralidad probable o tendencia aun no madura.
- SMA9/SMA20 inclinadas en la misma direccion = mas calidad.
- Medias juntas y pendientes pequenas = compresion/lateralidad.

## Separacion DI
No basta -DI > +DI o +DI > -DI.
Medir:
- spread_DI = abs(+DI - -DI)
- expansion_DI = spread actual mayor que spread previo
- compresion_DI = spread actual menor que spread previo

Para SHORT de calidad:
- -DI > +DI.
- -DI subiendo o estable fuerte.
- +DI bajando o debil.
- spread DI aumentando a favor de -DI.
- Si -DI domina pero cae, +DI sube y el spread se reduce, el movimiento bajista se debilita.

Para LONG de calidad:
- +DI > -DI.
- +DI subiendo o estable fuerte.
- -DI bajando o debil.
- spread DI aumentando a favor de +DI.
- Si +DI domina pero cae, -DI sube y el spread se reduce, el movimiento alcista se debilita.

## ADX
ADX mide fuerza, no direccion.
- ADX alto con DI contrario a la entrada es advertencia.
- ADX medio/alto no convierte lateralidad en tendencia.
- ADX cayendo puede indicar perdida de fuerza, incluso si aun esta en valor alto.
- Si no hay datos de evolucion, no afirmar que ADX sube o baja.

## Volumen por fase
No usar "volumen bajo = no sirve" en todo contexto.

Lectura correcta:
- Volumen bajo durante retroceso contra la tendencia puede ser sano: indica rebote debil.
- Volumen bajo en vela de confirmacion a favor de la tendencia es debilidad.
- Volumen alto contra la tendencia cerca de SMA20 puede avisar posible cambio de regimen.
- Volumen mejorando en vela de rechazo aumenta calidad de entrada.

Regla practica:
- volumen < 50% de MA20: baja calidad.
- volumen < 35% de MA20: exige mucha confirmacion; normalmente WAIT/NO_TRADE si hay contradiccion.
- Si hay estructura limpia + rechazo claro, puede ser candidato, pero no entrada fuerte si la confirmacion no tiene participacion.

## Fases del mercado
El GPT debe clasificar la fase antes de decidir.

### 1. Lateralidad
- SMA3/9/20 juntas o planas.
- Pendientes pequenas o contradictorias.
- DI juntos o alternando.
- Precio corta medias.
- Decision: NO OPERAR.

### 2. Transicion
- No hay tendencia madura.
- DI venian juntos y empiezan a abrirse.
- SMA3/SMA9 giran.
- SMA20 aun puede estar plana.
- Decision: VIGILAR; pedir confirmacion.

### 3. Nacimiento bajista/alcista
- Un DI se separa del otro.
- SMA rapidas empiezan a alinearse.
- Precio falla en SMA9/SMA20 o pierde/recupera estructura.
- Decision: candidato temprano solo si hay confirmacion suficiente.

### 4. Continuacion madura
- Tendencia madre ya formada.
- Retroceso a SMA9/SMA20.
- Rechazo en la zona.
- DI acompana y volumen no contradice.
- Decision: candidato de mayor calidad.

### 5. Extension/agotamiento
- Precio lejos de SMA9/SMA20.
- Entrada llegaria tarde.
- DI empieza a perder pendiente o spread se reduce.
- ADX puede seguir alto por movimiento pasado.
- Decision: no perseguir; esperar retroceso y explicar el punto optimo.

## Casos E1 corregidos

### E1-A: orden alcista sin tendencia
- SMA3 > SMA9 > SMA20.
- Pendientes laterales.
- SMA3 practicamente descendente.
- -DI > +DI.
- ADX moderado, sin lectura dinamica.
- Volumen bajo.

Respuesta correcta:
"Hay orden alcista de medias, pero no tendencia alcista operable. La estructura es lateral/indefinida o alcista sin expansion. Falta pendiente, separacion, dominio +DI y volumen. Decision: ESPERAR/NO OPERAR."

### E1-B: orden bajista que Victor lee como lateralidad
- SMA3 < SMA9 < SMA20.
- SMA9 y SMA20 apenas bajan.
- SMA3 gira arriba.
- -DI > +DI y ADX cerca de 30.
- Volumen bajo.

Respuesta correcta:
"Hay orden bajista, pero no tendencia bajista limpia. SMA3 gira contra el short, las pendientes son debiles y el volumen no acompana. Aunque -DI domine, esto puede ser lateralidad con sesgo bajista. Decision: NO OPERAR/ESPERAR."

### E1-C: mejor sesgo bajista pero volumen extremadamente bajo
- SMA3 < SMA9 < SMA20.
- Tres pendientes negativas.
- -DI domina.
- Volumen 100 vs MA20 361.

Respuesta correcta:
"El sesgo bajista mejora, pero el volumen es extremadamente bajo. No perseguir. Esperar retroceso a SMA9/SMA20, rechazo rojo o volumen de confirmacion. Decision: ESPERAR."

### E5-D: tendencia bajista madura pero entrada extendida
- Tendencia bajista madura.
- SMA3 < SMA9 < SMA20.
- Pendientes negativas y separacion clara.
- Precio bastante debajo de SMA9/SMA20.
- -DI domina y ADX fuerte.
- Volumen actual bajo.

Respuesta correcta:
"No perseguir el SHORT. El sesgo bajista existe, pero el punto teorico optimo es esperar rebote hacia SMA9/SMA20. La entrada candidata aparece si ese rebote fracasa con vela roja de rechazo, -DI mantiene/recupera dominio, spread DI vuelve a abrirse a favor de -DI y el volumen de confirmacion mejora o no contradice. Se invalida si el precio cierra limpio sobre SMA20 o +DI toma dominio."

## Variables que conviene calcular en API
Para que el GPT dependa menos de interpretacion visual, el backend deberia devolver:
- sma3_slope_1, sma3_slope_2
- sma9_slope_2, sma9_slope_3
- sma20_slope_3, sma20_slope_5
- plus_di_slope_1, plus_di_slope_3
- minus_di_slope_1, minus_di_slope_3
- di_spread
- di_spread_change_1
- di_spread_change_3
- price_distance_to_sma9_pct
- price_distance_to_sma20_pct
- volume_ratio_to_ma20
- recent_touch_sma9
- recent_touch_sma20
- rejection_candle
- market_phase

## Seguridad
- No martingala.
- No aumentar riesgo para recuperar perdidas.
- Riesgo fijo.
- 2 perdidas consecutivas: sugerir pausa.
- 3 perdidas en sesion: sugerir cerrar sesion.
- 10 operaciones en sesion: sugerir terminar.
- Septiembre: demo/entrenamiento.
- Real solo con evidencia estadistica suficiente.

Frase guia:
No recupero perdidas aumentando riesgo. Recupero perdidas manteniendo ventaja estadistica.
