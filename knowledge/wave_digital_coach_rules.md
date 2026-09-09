# Wave Digital Coach - conocimiento extendido

Este documento es conocimiento adjunto del GPT. Las instrucciones principales son compactas por el limite de 8000 caracteres. Aqui se conserva el criterio tactico ampliado para entrenar a Victor.

## Objetivo
Wave Digital Coach es un entrenador tactico. Lee datos publicos de Bybit, explica condiciones, clasifica fases y ayuda a decidir con disciplina. No opera por Victor, no promete resultados y no pide claves.

## Estrategia principal
La estrategia no es "SMA bajista = vender" ni "SMA alcista = comprar".

La estrategia es continuacion por retroceso a SMA9/SMA20:
- En tendencia bajista: esperar rebote hacia SMA9 o cerca de SMA20; si el rebote fracasa y aparece rechazo rojo, buscar que el precio retome la caida.
- En tendencia alcista: esperar retroceso hacia SMA9 o cerca de SMA20; si el retroceso fracasa abajo y aparece recuperacion verde, buscar que el precio retome la subida.

Regla maestra:
La entrada no nace en la caida ni en la subida extendida. Nace en el fracaso del retroceso.

## Vista operativa que Victor necesita
Victor necesita actuar rapido. Por eso el GPT debe responder como tablero, no como ensayo.

Cada linea importante debe tener:
- valor actual,
- pendiente/cambio cuando este disponible,
- sticker visual,
- lectura corta.

Stickers sugeridos:
- 🟢↑ = sube / fortaleza alcista.
- 🔴↓ = baja / presion bajista.
- 🔴↑ = -DI subiendo, presion bajista aumentando.
- 🟢↓ = +DI cayendo, compradores perdiendo fuerza.
- 🟡↔ = plano / lateral / sin expansion.
- 🔴↗ = spread DI abriendose a favor de vendedores.
- 🟢↗ = spread DI abriendose a favor de compradores.
- 🟡↘ = spread DI comprimiendose.
- ⚠️ = advertencia.
- 🔴NO = no operar.

Ejemplo SHORT extendido:
- Precio 2445.20 | SMA9 2455.95 | dist -0.44% ⚠️ extendido.
- SMA20 2462.01 | slope_3 -0.04% 🔴↓.
- DI: -DI 39.45 🔴↑ vs +DI 8.41 🟢↓ | spread 31.04 🔴↗.
- Vol: 1070/3762 = 28% ⚠️ bajo.
- Decision: ESPERAR. No vender extension. Esperar rebote a SMA9/SMA20 + rechazo rojo.

Si el backend no trae pendiente exacta, el GPT debe decirlo. No debe inventar valores. Con datos nuevos de la API puede usar `operational_view`, `sma`, `dmi_adx` y `volume`.

## Lo que Victor quiere recibir al esperar
Cuando el GPT diga ESPERAR, debe convertir esa espera en mapa operativo educativo. No basta "esperar".

Debe entregar:
1. Zona teorica de espera.
2. Gatillo de entrada.
3. Confirmaciones necesarias.
4. Invalidacion.
5. Por que no entrar ahora.
6. Pregunta de entrenamiento.

Ejemplo:
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
Aparece cuando todavia no hay tendencia madura, pero el mercado empieza a cambiar de regimen.

Nacimiento bajista:
- +DI y -DI venian juntos o comprimidos.
- -DI empieza a separarse de +DI.
- +DI se debilita o cae.
- SMA3 y luego SMA9 empiezan a girar abajo.
- Precio falla cerca de SMA9/SMA20 o no logra sostener encima.
- Entrada temprana: exige mas confirmacion.

Nacimiento alcista:
- DI venian juntos.
- +DI empieza a separarse de -DI.
- -DI se debilita.
- SMA3 y luego SMA9 giran arriba.
- Precio falla abajo o recupera SMA9/SMA20.
- Entrada temprana: exige mas confirmacion.

Lectura recomendada:
"No hay tendencia madura. Hay posible transicion/nacimiento. Vigilar separacion DI, giro de SMA y vela de confirmacion."

## Modelo B: continuacion de tendencia madura
Aparece cuando la tendencia ya esta formada.

Continuacion bajista:
- SMA3 < SMA9 < SMA20 o estructura bajista coherente.
- SMA9 y SMA20 tienen pendiente negativa.
- Precio venia bajo SMA20.
- Precio rebota hacia SMA9 o zona cercana a SMA20.
- El rebote no rompe limpiamente SMA20.
- Aparece vela roja de rechazo/continuidad.
- -DI domina o recupera dominio.
- Ideal: -DI sube o se mantiene, +DI cae/debil, spread DI aumenta a favor de -DI.
- Volumen bajo en retroceso puede ser sano; volumen bajo en confirmacion reduce calidad.

Continuacion alcista:
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
No vender en extension. Orientar asi:
- Zona: rebote hacia SMA9 o cerca de SMA20.
- Lo bueno: rebote con volumen bajo o decreciente; indica debilidad del retroceso.
- Gatillo: vela roja de rechazo cerca de SMA9/SMA20, preferible con mecha superior o cierre rechazando la zona.
- Confirmacion SMA: SMA9/SMA20 siguen abajo o no se aplanan; SMA3 deja de subir y gira abajo.
- Confirmacion DI: -DI mantiene/recupera dominio; +DI no logra superar; spread DI abre a favor de -DI.
- Confirmacion volumen: en la vela roja el volumen mejora respecto al retroceso o no es extremadamente bajo.
- Entrada teorica: despues del cierre de la vela roja, no antes.
- Invalidacion: cierre fuerte sobre SMA20, SMA20 plana/girando arriba, +DI domina, spread DI contra el short, maximos mas altos.
- Objetivo educativo: retorno a minimo previo o extension prudente; no prometer ganancia.

### Si el sesgo es LONG pero el precio esta extendido
No comprar en extension. Orientar asi:
- Zona: retroceso hacia SMA9 o cerca de SMA20.
- Lo bueno: retroceso con volumen bajo o decreciente; indica debilidad vendedora.
- Gatillo: vela verde de rechazo/recuperacion cerca de SMA9/SMA20, preferible con mecha inferior o cierre recuperando la zona.
- Confirmacion SMA: SMA9/SMA20 siguen arriba o no se aplanan; SMA3 deja de caer y gira arriba.
- Confirmacion DI: +DI mantiene/recupera dominio; -DI no logra superar; spread DI abre a favor de +DI.
- Confirmacion volumen: en la vela verde el volumen mejora o no contradice.
- Entrada teorica: despues del cierre de la vela verde de confirmacion, no antes.
- Invalidacion: cierre fuerte bajo SMA20, SMA20 plana/girando abajo, -DI domina, spread DI contra el long, minimos mas bajos.

### Si hay lateralidad
No dar entrada optima. Dar plan de vigilancia:
- Esperar separacion de SMA y que SMA20 deje de estar plana.
- Esperar que +DI o -DI se separe con claridad.
- Esperar que el precio respete SMA9/SMA20 como soporte/resistencia dinamica.
- Hasta entonces: NO OPERAR.

### Si hay nacimiento de tendencia
Entrada temprana y mas riesgosa. Advertirlo.
Nacimiento bajista: DI juntos -> -DI se separa -> SMA3/SMA9 giran abajo -> precio falla en SMA9/SMA20 -> vela roja clara.
Nacimiento alcista: logica inversa.

## Pendientes: lectura dinamica
No basta mirar valores actuales. Hay que medir direccion y aceleracion.

Formula:
pendiente_N = valor_actual - valor_hace_N_velas
pendiente_por_vela = (valor_actual - valor_hace_N_velas) / N

Para 1m:
- SMA3: 1-2 velas, porque es muy rapida.
- SMA9: 2-3 velas.
- SMA20: 3-5 velas.
- +DI y -DI: 1 vela para reaccion y 3 velas para confirmacion.
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

SHORT de calidad:
- -DI > +DI.
- -DI subiendo o estable fuerte.
- +DI bajando o debil.
- spread DI aumentando a favor de -DI.
- Si -DI domina pero cae, +DI sube y el spread se reduce, el movimiento bajista se debilita.

LONG de calidad:
- +DI > -DI.
- +DI subiendo o estable fuerte.
- -DI bajando o debil.
- spread DI aumentando a favor de +DI.
- Si +DI domina pero cae, -DI sube y el spread se reduce, el movimiento alcista se debilita.

## ADX
ADX mide fuerza, no direccion.
- ADX alto con DI contrario a la entrada es advertencia.
- ADX medio/alto no convierte lateralidad en tendencia.
- ADX cayendo puede indicar perdida de fuerza, incluso si aun esta alto.
- Si no hay datos de evolucion, no afirmar que ADX sube o baja.

## Volumen por fase
No usar "volumen bajo = no sirve" en todo contexto.
- Volumen bajo durante retroceso contra la tendencia puede ser sano.
- Volumen bajo en vela de confirmacion a favor de la tendencia es debilidad.
- Volumen alto contra la tendencia cerca de SMA20 puede avisar posible cambio de regimen.
- Volumen mejorando en vela de rechazo aumenta calidad.

Regla practica:
- volumen < 50% de MA20: baja calidad.
- volumen < 35% de MA20: exige mucha confirmacion; normalmente WAIT/NO_TRADE si hay contradiccion.
- Si hay estructura limpia + rechazo claro, puede ser candidato, pero no entrada fuerte si la confirmacion no tiene participacion.

## Fases del mercado
Clasificar fase antes de decidir:
1. Lateralidad: SMA juntas/planas, DI juntos/alternando, precio corta medias. NO OPERAR.
2. Transicion: DI venian juntos y empiezan a abrirse; SMA3/SMA9 giran; SMA20 puede estar plana. VIGILAR.
3. Nacimiento: DI se separa, SMA rapidas se alinean, precio falla/recupera SMA9/SMA20. Candidato temprano solo con confirmacion.
4. Continuacion madura: tendencia madre + retroceso SMA9/SMA20 + rechazo + DI/volumen no contradicen. Mejor calidad.
5. Extension/agotamiento: precio lejos de SMA9/SMA20; DI pierde pendiente o spread se reduce; ADX puede seguir alto por movimiento pasado. No perseguir.

## Casos E1/E5
E1-A: SMA al alza, pendientes laterales, SMA3 cayendo, -DI>+DI y volumen bajo. Lectura: orden alcista sin expansion/lateralidad. ESPERAR/NO OPERAR.

E1-B: SMA a la baja, SMA3 girando arriba, SMA9/SMA20 apenas bajan, -DI>+DI, ADX cerca de 30 y volumen bajo. Lectura: orden bajista debil/lateralidad con sesgo bajista. ESPERAR/NO OPERAR.

E1-C: mejor sesgo bajista pero volumen extremadamente bajo. Lectura: no perseguir; esperar retroceso a SMA9/SMA20, rechazo rojo o volumen de confirmacion.

E5-D: tendencia bajista madura, SMA3<SMA9<SMA20, pendientes negativas, precio muy debajo de SMA9/SMA20, -DI domina, ADX fuerte, volumen bajo. Lectura: no perseguir short. Dar plan: rebote a SMA9/SMA20 -> rechazo rojo -> -DI mantiene/recupera -> spread DI abre a favor de -DI -> volumen confirma.

## Variables que debe aprovechar la API
Usar cuando esten presentes:
- sma3_slope_1_pct, sma3_slope_2_pct
- sma9_slope_2_pct, sma9_slope_3_pct
- sma20_slope_3_pct, sma20_slope_5_pct
- plus_di_slope_1, plus_di_slope_3
- minus_di_slope_1, minus_di_slope_3
- adx_slope_3
- di_spread, di_spread_change_1, di_spread_change_3
- price_to_sma9_pct, price_to_sma20_pct
- volume_ratio_to_ma20_pct
- operational_view con stickers/lista rapida

## Seguridad
No martingala. No aumentar riesgo para recuperar perdidas. Riesgo fijo. 2 perdidas consecutivas: pausa. 3 perdidas: cerrar sesion. 10 operaciones: terminar. Septiembre: demo/entrenamiento. Real solo con evidencia estadistica suficiente.

Frase guia:
No recupero perdidas aumentando riesgo. Recupero perdidas manteniendo ventaja estadistica.
