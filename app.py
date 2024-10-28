import tkinter as tk 
from tkinter import messagebox

class JuegoTresEnRaya:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tres en Raya")
        self.botones = [[None, None, None] for _ in range(3)]
        self.jugador_actual = "X"
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(3):
            for columna in range(3):
                self.botones[fila][columna] = tk.Button(
                    self.ventana, 
                    text="", 
                    font=('normal', 40), 
                    width=5, 
                    height=2, 
                    command=lambda f=fila, c=columna: self.boton_clic(f, c)
                )
                self.botones[fila][columna].grid(row=fila, column=columna)

    def boton_clic(self, fila, columna):
        if self.botones[fila][columna]["text"] == "":
            self.botones[fila][columna]["text"] = self.jugador_actual

            if self.verificar_ganador():
                messagebox.showinfo("¡Fin del juego!", f"¡El jugador {self.jugador_actual} es el ganador!")
                self.reiniciar_juego()
            elif self.verificar_empate():
                messagebox.showinfo("¡Fin del juego!", "¡Es un empate!")
                self.reiniciar_juego()
            else:
                self.cambiar_jugador()

    def verificar_ganador(self):
        for i in range(3):
            if self.verificar_linea(self.botones[i][0], self.botones[i][1], self.botones[i][2]) or \
               self.verificar_linea(self.botones[0][i], self.botones[1][i], self.botones[2][i]):
                return True
        return self.verificar_linea(self.botones[0][0], self.botones[1][1], self.botones[2][2]) or \
               self.verificar_linea(self.botones[0][2], self.botones[1][1], self.botones[2][0])

    def verificar_linea(self, a, b, c):
        return a["text"] == b["text"] == c["text"] != ""

    def verificar_empate(self):
        return all(self.botones[fila][columna]["text"] != "" for fila in range(3) for columna in range(3))

    def cambiar_jugador(self):
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def reiniciar_juego(self):
        self.jugador_actual = "X"
        for fila in range(3):
            for columna in range(3):
                self.botones[fila][columna]["text"] = ""

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = JuegoTresEnRaya()
    juego.iniciar()