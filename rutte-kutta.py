#!/usr/bin/env wolframscript

RKODE[G_, x0_, f0_, dx_, NS_] := Module[{k1, k2, retvals, index, xn, fn},
  retvals = Table[{0.0, 0.0}, {i, 1, NS}];
  xn = x0;
  fn = f0;
  retvals[[1]] = {x0, f0};
  For[index = 2, index <= NS, index = index + 1,
    k1 = dx * G[xn, fn];
    k2 = dx * G[xn + dx/2, fn + k1/2];
    fn = fn + k2;
    xn = xn + dx;
    retvals[[index]] = {xn, fn};
  ];
  Return[retvals];
]

f[t_, x_] := -2*x*t;

resultados = RKODE[f, 0.0, 2.0, 0.5, 100];

(* Solución analítica para comparar: x(t) = 2*e^(-t^2) *)
analitica = Table[{t, 2.0*Exp[-t^2]}, {t, 0.0, 50.0, 0.5}];

(* Gráfica *)
grafica = ListLinePlot[
  {resultados, analitica},
  PlotStyle -> {{Blue, Thick}, {Red, Dashed, Thick}},
  Mesh -> All,
  MeshStyle -> {Blue, Red},
  AxesLabel -> {"Tiempo (t)", "x(t)"},
  PlotLabel -> "Solucion usando Runge-Kutta Midpoint",
  PlotLegends -> {"RK2 Midpoint", "Analitica: 2*exp(-t^2)"},
  AspectRatio -> 0.6
];

Export["rk2_grafica.png", grafica];

(* Tabla *)
Print["Tabla de resultados (primeros 5 valores):"];
Print[TableForm[
  Take[resultados, 5],
  TableHeadings -> {None, {"Tiempo (t)", "x(t)"}}
]];

Print["Listo! Guardado como rk2_grafica.png"];
