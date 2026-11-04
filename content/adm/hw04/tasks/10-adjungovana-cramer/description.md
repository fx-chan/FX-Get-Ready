Z úvodu DÚ 04: **adjungovaná matica** $\operatorname{adj}(\mathbf{A}) = [C_{ij}]^{\top}$ (transponovaná matica kofaktorov) a
$$\mathbf{A}^{-1} = \frac{1}{\det\mathbf{A}}\operatorname{adj}(\mathbf{A}).$$
**Cramerovo pravidlo:** pre $\mathbf{Ax} = \mathbf{b}$ s $\det\mathbf{A} \ne 0$ je $x_j = \dfrac{\det\mathbf{A}_j}{\det\mathbf{A}}$, kde
$\mathbf{A}_j$ vznikne nahradením $j$-teho stĺpca vektorom $\mathbf{b}$.

$\mathbf{A} = \begin{bmatrix}1 & -2 & 3 \\ 6 & 7 & -1 \\ -3 & 1 & 4\end{bmatrix}$; sústava $\left\{\begin{aligned}x_1 + x_2 + 2x_3 &= 8 \\ -x_1 - 2x_2 + 3x_3 &= 1 \\ 3x_1 - 7x_2 + 4x_3 &= 10\end{aligned}\right.$
