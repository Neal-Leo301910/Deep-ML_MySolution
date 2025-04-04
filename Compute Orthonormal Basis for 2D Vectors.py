'''
Implement a function that computes an orthonormal basis for the subspace spanned by a list of 2D vectors using the Gram-Schmidt process. 
The function should take a list of 2D vectors and a tolerance value (tol) to determine linear independence, 
returning a list of orthonormal vectors (unit length and orthogonal to each other) that span the same subspace. 
This is a fundamental concept in linear algebra with applications in machine learning, such as feature orthogonalization.
'''

import numpy as np
def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    
    orth_vec = []
    
    if len(vectors) == 1:
        return orth_vec
    
    v_i_norm = 1 / np.linalg.norm(vectors,axis=1)
    u_i = np.array(vectors) * np.array(v_i_norm)[:, np.newaxis]

    
    orth_vec.append(u_i[0])
    
    for k in range(1,len(vectors)):
        v_k = vectors[k]
        sum_proj = np.zeros_like(vectors[0],dtype=float)

        for i in range(k):
            sum_proj += proj_ui_vk(u_i[i],v_k)
            
        w_k = v_k - sum_proj
        w_k_norm = np.linalg.norm(w_k)

        if w_k_norm > tol:
            u_k = w_k / w_k_norm
            orth_vec.append(u_k)
                    


    return [np.round(vec, decimals=4) for vec in orth_vec]

def proj_ui_vk(vector_a: list[list[float]],vector_b: list[list[float]]) -> list[np.ndarray]:
    
    
    return np.dot(vector_b,vector_a) * vector_a
