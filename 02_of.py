import rx

rx.of('Hola', 'Adios').subscribe(on_next=lambda v: print(f'Recibido: {v}'))