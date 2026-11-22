# Fuentes de imágenes (deck UNESR DICT 2026)

## Slide 1 — gráficas de Freddy Vega (Platzi), video "Por qué ya no existen las carreras seguras" (YouTube X3G2C15azIs)
- curvas-s-adopcion.png — recorte de /workspace/unesr/graficas/slide1/crop_t00m18s.png (00:18). Se eligió 00:18 en lugar de 00:20/00:22 porque es el mismo gráfico sin el oscurecido ni el recuadro de resaltado. Crédito en pantalla: "Adapted from Michael Felton, The New York Times".
- waffle-adopcion-ia.png — recorte de /workspace/unesr/graficas/slide1/crop_t02m20s.png (02:20). Sin crédito de terceros en pantalla → "Fuente: Freddy Vega, Platzi".

## Slide 2 — Farmatodo
- farmatodo-logo.svg — logo oficial (versión blanca del header del sitio): https://www.farmatodo.com.ve/assets/svg/logo-farmatodo2.svg (descargado 2026-11-21). Se muestra sobre el azul de marca #418FDE.
  - Alternativa azul guardada en src/: https://commons.wikimedia.org/wiki/File:Farmatodo_logo.svg (fuente declarada: farmatodo.com.ve).
- farmatodo-delivery.jpg — foto real de un repartidor de Farmatodo (EN BICICLETA con remolque, frente a una tienda Farmatodo), publicada por El Impulso (Barquisimeto) en la nota de prensa de Farmatodo del 4 jul 2020:
  - Imagen: https://cdn.elimpulso.com/media/2020/07/pulso.jpeg
  - Nota: https://www.elimpulso.com/2020/07/04/pulsoempresarial-farmatodo-expande-su-servicio-delivery-por-venezuela/
  - NO es un motorizado: no se encontró una foto real y utilizable de un motorizado de Farmatodo. Se buscó en: notas de prensa (El Universal, Digital58, La Iguana, Sumando Negocios, Sitara, Descifrado), Contrapunto (fotos de un repartidor en bici, bloqueadas por hotlink 403), Últimas Noticias (2021 "Moto-Delivery.jpg" y 2026 — sitio con captcha/502), Wikimedia Commons, Google/Bing Imágenes, y 4 comerciales oficiales de Farmatodo en YouTube (JAmDVd1Q3zI, viLf43uPChQ, 6RTGoTacwOU — Farmatodo Venezuela; hdl1yYknaJo — Farmatodo Colombia): ninguno muestra un motorizado en moto. Las únicas fotos de motorizados con Farmatodo que aparecieron son de noticias de sucesos (Maracaibo, oct 2023) y se descartaron.

## Footer — lockup "Academia Sinergia × SpaceXAI"
- Símbolo S blanco: logos/sinergia.png (mismo que /workspace/cieca-assets/03-logo-academia-sinergia-s-blanca-transparente.png). No existe en los archivos de Adonay un lockup vectorial con texto (los PNG "Academia Sinergia" son portadas con foto; Logo_sinergia_completo.png tiene un texto rojo de otra versión). El texto "Academia Sinergia" se compone en Hanken Grotesk ("Academia" en negrita + "Sinergia" regular), igual que en las portadas oficiales de Academia Sinergia.
- SpaceXAI: logos/spacexai.png (kit oficial de embajador).

## Slide 1 — v2 (2026-11-21): gráficas reconstruidas
- Curvas S: SVG vectorial inline en index.html, trazado a mano punto por punto desde el cuadro 00:18 (ejes 1900–2005, 0–100 % hogares de EE. UU.; curvas Electricidad, Refrigerador, TV a color, Internet). Crédito en slide: "Adaptado de Michael Felton, The New York Times". Valores aproximados por lectura visual (±2–3 puntos).
- Waffle: SVG inline de 50×50 = 2.500 puntos (cada uno ≈ 3,2 M personas): 2.100 nunca (84 %), 392 chatbot gratis, 7 pagan (≈0,3 %), 1 código (≈0,04 %) — misma distribución que el original (16 % = 400 puntos incluyendo pagos y código).
- curvas-s-adopcion.png y waffle-adopcion-ia.png quedan en assets/ solo como referencia; ya no se usan en el deck.

## Slide 2 — v2 (2026-11-21): nueva foto Farmatodo + disposición ramificada
- farmatodo-repartidor-2020.jpg — foto real de un repartidor de Farmatodo (en bicicleta, con morral térmico con el logo de Farmatodo), incluida en la nota de prensa de Farmatodo del 29 may 2020 ("Farmatodo expande su servicio Delivery por Venezuela"), publicada por La Iguana TV:
  - Imagen: https://www.laiguana.tv/wp-content/uploads/2020/06/WhatsApp-Image-2020-05-29-at-12.09.07-PM-696x1239.jpeg
  - Nota: https://www.laiguana.tv/articulos/753652-farmatodo-servicio-delivery-venezuela/
  - Crédito en slide: "Foto: cortesía Farmatodo, vía La Iguana TV (2020)". Sigue siendo bicicleta, no moto: no se encontró una foto pública y utilizable de un motorizado con marca Farmatodo (las que aparecen son de sucesos, Maracaibo oct 2023; la de Tuy Informa 2024 no cargó: el servidor cierra la conexión TLS).
  - farmatodo-delivery.jpg (El Impulso) queda en assets/ pero ya no se usa.
- Disposición de la cadena: inspirada en la distribución espacial del cuadro 14:28 de /workspace/unesr/inspiracion-1080p.mp4 (origen → abanico a 3 elementos apilados → convergen en uno → teléfono → entrega). Contenido e íconos propios.

## Slide 4 — v3: distribución de agentes (datos reales)
- Fuente: /home/box/agent-data/agents/*/profile.json (29 perfiles). 6 son salas/proyectos sin avatar (no agentes) → 23 agentes, igual al dato de la slide.
- Agrupación por área (roles genéricos, sin nombres): Diseño para clientes 5 · Contenido 5 · Proyectos propios 4 · Mentoría 3 · Carrera y freelance 2 · Vida y finanzas personales 2 · Embajador y comunidad 2 = 23.
- "Embajador y comunidad" = los 2 agentes explicadores (texto y video); es una asignación por criterio, ningún perfil dice "embajador".
