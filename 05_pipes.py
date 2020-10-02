from rx import of, operators

of('Hola', 'Adios').pipe(
    operators.map(lambda s: s.upper()),
    operators.map(lambda s: f'En mayusculas: {s}')
).subscribe(lambda v: print(f'Recibido: {v}'))
