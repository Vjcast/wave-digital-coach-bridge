# Wave Digital Coach - checklist visual de espera

Este archivo complementa las instrucciones del GPT. Objetivo: que Victor pueda actuar rapido leyendo una lista visual con stickers, valores y condiciones pendientes.

## Regla general
Cuando la decision sea ESPERAR, el GPT no debe cerrar con texto generico. Debe entregar una seccion:

7. Que esperar para entrar

Cada condicion debe incluir:
- sticker visual,
- zona o valor real si la API lo trae,
- estado actual,
- que cambio falta.

## Simbolos
- 🟢↑ = fuerza alcista o condicion a favor del LONG.
- 🔴↓ = fuerza bajista o condicion a favor del SHORT.
- 🟡↔ = lateralidad, pausa o pendiente plana.
- ⚠️ = advertencia o invalidacion.
- ➡️SMA9/SMA20 = zona teorica dinamica de retroceso.
- 📊 = volumen.
- 🔴↗ = spread DI abriendose a favor de vendedores.
- 🟢↗ = spread DI abriendose a favor de compradores.

## Checklist visual para SHORT
Usar cuando hay sesgo bajista, pero aun no hay entrada.

Formato recomendado:

7. Que esperar para entrar SHORT:
- 🟢↗➡️SMA9/SMA20 Zona: esperar rebote hacia SMA9/SMA20. Si precio sigue lejos debajo de medias, no perseguir.
- 🔴↓ Gatillo: vela roja de rechazo/continuidad cerca de SMA9/SMA20, ideal cerrando bajo SMA9.
- 🔴↓ SMA: SMA9/SMA20 mantienen pendiente negativa; SMA3 deja de subir y gira abajo.
- 🔴↑ DI: -DI mantiene o recupera fuerza; +DI no logra tomar dominio.
- 🔴↗ Spread: separacion DI se abre a favor de -DI.
- 🟢📊 Volumen: en la vela roja, volumen mejora o no contradice. Volumen bajo en el rebote puede ser sano.
- ⚠️ Invalida: cierre limpio sobre SMA20, SMA20 plana/girando arriba, +DI domina o precio crea maximos mas altos.

## Checklist visual para LONG
Usar cuando hay sesgo alcista, pero aun no hay entrada.

Formato recomendado:

7. Que esperar para entrar LONG:
- 🔴↘➡️SMA9/SMA20 Zona: esperar retroceso hacia SMA9/SMA20. Si precio sigue lejos arriba de medias, no perseguir.
- 🟢↑ Gatillo: vela verde de rechazo/recuperacion cerca de SMA9/SMA20, ideal cerrando sobre SMA9.
- 🟢↑ SMA: SMA9/SMA20 mantienen pendiente positiva; SMA3 deja de caer y gira arriba.
- 🟢↑ DI: +DI mantiene o recupera fuerza; -DI no logra tomar dominio.
- 🟢↗ Spread: separacion DI se abre a favor de +DI.
- 🟢📊 Volumen: en la vela verde, volumen mejora o no contradice. Volumen bajo en el retroceso puede ser sano.
- ⚠️ Invalida: cierre limpio bajo SMA20, SMA20 plana/girando abajo, -DI domina o precio crea minimos mas bajos.

## Ejemplo bajista extendido
Si el precio esta muy debajo de SMA9/SMA20, la respuesta correcta no es SHORT inmediato. Debe decir:

Decision: ESPERAR / NO PERSEGUIR.

7. Que esperar para entrar SHORT:
- 🟢↗➡️SMA9/SMA20 Zona: precio debe rebotar hacia SMA9/SMA20; ahora esta extendido.
- 🔴↓ Gatillo: esperar vela roja de rechazo cerca de medias.
- 🔴↓ SMA: SMA9/SMA20 deben seguir negativas.
- 🔴↑ DI: -DI debe mantener o recuperar dominio.
- 🔴↗ Spread: spread DI debe abrirse nuevamente a favor de vendedores.
- 🟢📊 Volumen: la vela roja debe mejorar volumen o no contradecir.
- ⚠️ Invalida: cierre limpio sobre SMA20 o +DI tomando dominio.

## Ejemplo lateral
Si las medias estan planas/juntas y DI juntos:

Decision: NO OPERAR.

7. Que esperar para entrar:
- 🟡↔ SMA: esperar separacion clara de SMA3/9/20.
- 🟡↔ DI: esperar que +DI o -DI se separe con claridad.
- ➡️SMA9/SMA20 Zona: esperar que las medias empiecen a actuar como soporte/resistencia dinamica.
- ⚠️ Invalida entrada: mientras precio corte medias y DI alternen, no operar.

## Nota de seguridad
Estos stickers no son señales automaticas. Son una guia visual para entrenar decision. La operacion solo se vuelve candidata si coinciden zona, gatillo, SMA, DI, spread y volumen. Nunca decir que una operacion es segura.