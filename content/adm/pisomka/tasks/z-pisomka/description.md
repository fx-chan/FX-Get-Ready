**4 príklady, 100 minút.** Každý príklad má 25 bodov, rozdelených rovnomerne medzi jeho časti.

### Príklad 1 — transformácie
Zobrazenie $f$ v rovine vznikne v tomto poradí: **(1)** reflexia podľa priamky $y = 2x$, **(2)** posunutie o $(3, -1)$,
**(3)** rotácia o $90^\circ$ proti smeru hodinových ručičiek okolo bodu $(1, 2)$.

### Príklad 2 — vlastné čísla
$$\mathbf{A} = \begin{bmatrix}3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3\end{bmatrix}$$
Mocninová metóda s maximálnym škálovaním: $\mathbf{x}_k = \mathbf{A}\mathbf{x}_{k-1} / \max(\mathbf{A}\mathbf{x}_{k-1})$, kde $\max$ je najväčšia absolútna hodnota zložky. Odhad čísla: Rayleighov podiel $\dfrac{\mathbf{A}\mathbf{x}\cdot\mathbf{x}}{\mathbf{x}\cdot\mathbf{x}}$. Štart $\mathbf{x}_0 = (1, 0, 0)$, dve iterácie.

### Príklad 3 — determinant
$$\mathbf{B} = \begin{bmatrix}2 & 0 & 0 & 3 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 & 2 & 0 \\ 0 & 0 & 3 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 2 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 2\end{bmatrix}$$ $$\mathbf{C}(x) = \begin{bmatrix}x & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 & 0 & 0 & 1 \\ 1 & 0 & x & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & x & 0 \\ 0 & 0 & 0 & 0 & 3 & 0 & 0 \\ 0 & x & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 2 & 0 & 1\end{bmatrix}$$

### Príklad 4 — LU rozklad
$$\mathbf{A} = \begin{bmatrix}2 & 1 & -1 \\ 4 & 5 & 1 \\ -2 & 3 & 7\end{bmatrix},\quad \mathbf{b} = (3, 13, 11),\qquad \mathbf{D}(t) = \begin{bmatrix}2 & 1 & -1 \\ 4 & t & 1 \\ -2 & 3 & t\end{bmatrix}$$
