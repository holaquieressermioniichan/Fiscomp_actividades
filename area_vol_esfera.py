(* Número de puntos *)
nPuntos = 100000;  (* Más puntos = más precisión *)
radio = 1;

puntosDentro = 0;

(* Generamos puntos aleatorios dentro de un cubo [-r,r]^3 *)
Do[
  x = RandomReal[{-radio, radio}];
  y = RandomReal[{-radio, radio}];
  z = RandomReal[{-radio, radio}];

  If[x^2 + y^2 + z^2 <= radio^2,
    puntosDentro++
  ];

, {nPuntos}];

(* Volumen del cubo: (2r)^3 *)
volumenCubo = (2 radio)^3;

(* Volumen aproximado de la esfera *)
volumenAprox = (puntosDentro/nPuntos) * volumenCubo;

volumenReal = (4/3) Pi radio^3;

Print["Simulación Monte Carlo (n = ", nPuntos, ")"];
Print["--------------------------------------------"];
Print["Puntos dentro: ", puntosDentro];
Print["Volumen aproximado: ", N[volumenAprox, 6]];
Print["Volumen real:	   ", N[volumenReal, 6]];
Print["Error volumen:	   ", N[Abs[volumenAprox - volumenReal], 6]];

Print[""];

(* Área superficial de la esfera (fórmula exacta) *)
areaReal = 4 Pi radio^2;

Print["Área superficial (exacta): ", N[areaReal, 6]];
