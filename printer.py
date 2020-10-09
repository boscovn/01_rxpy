import rx

class Printer(rx.core.Observer):
    def on_next(self, v):
        print(f'Recibido: {v}')

    def on_completed(self):
        print("Terminado")

    def on_error(self, e):
        print(e)