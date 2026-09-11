import janus_swi as janus

#Logica Proporcional
janus.consult('lógica proposicional', '''
conbi(and).
conbi(or).
conbi(then).
clog(v).
clog(f).
vlog(p).
vlog(q).
vlog(r).
vlog(s).
expr(X) :- clog(X).
expr(X) :- vlog(X).
expr([neg, A]) :- expr(A).
expr([A, Con, B]) :- expr(A), conbi(Con), expr(B).
''')
#p & (q -> ¬r)
list(janus.query('expr( [p, and, [q, then, [neg, r]]]).'))


#fibonacci
janus.consult('fibonacci(N, X)', '''
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, X) :- N > 1, N1 is N-1, fibonacci(N1, X1), N2 is N-2, fibonacci(N2, X2), X is X1+X2.
''')
list(janus.query('fibonacci(3, X).'))

#Juego Torres de Hanoi
janus.consult('Hanoi', '''
hanoi(1, A, _, C) :- write('Mueve del '), write(A), write(' al '), write(C), nl.
hanoi(N, A, B, C) :- N>1, M is N-1, hanoi(M, A, C, B), hanoi(1, A, B, C), hanoi(M, B, A, C).
''')
list(janus.query('hanoi(3, a, b, c).'))

#Rutas
janus.consult('rutas', '''
distancia(buenosAires, puertoMadryn, 1300).
distancia(puertoMadryn, puertoDeseado, 732).
distancia(puertoDeseado, rioGallegos, 736).
distancia(puertoDeseado, calafate, 979).
distancia(rioGallegos, calafate, 304).
distancia(calafate, chalten, 213).

kilometrosViaje(Origen, Destino, Kms):-
    distancia(Origen, Destino, Kms).
kilometrosViaje(Origen, Destino, KmsTotales):-
    distancia(Origen, PuntoIntermedio, KmsIntermedios),
    kilometrosViaje(PuntoIntermedio, Destino, KmsFinales),
    KmsTotales is KmsIntermedios + KmsFinales.

totalViaje(Origen, Destino, Kms):-kilometrosViaje(Origen, Destino, Kms).
totalViaje(Destino, Origen, Kms):-kilometrosViaje(Origen, Destino, Kms).
''')

input(list(janus.query('totalViaje(buenosAires, calafate, K).')))
