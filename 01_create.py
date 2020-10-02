import rx

def generador(o, s):
    o.on_next('Hola')
    o.on_next('Adiós')

observable = rx.create(generador)

observable.subscribe(on_next=lambda v: print(f'Recibido: {v}'))