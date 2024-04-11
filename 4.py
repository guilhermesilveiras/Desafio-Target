class Lampada:
    def __init__(self):
        self.acesa = False
        self.quente = False

class Interruptor:
    def __init__(self, lampada):
        self.lampada = lampada

    def ligar(self):
        self.lampada.acesa = True

    def desligar(self):
        if self.lampada.acesa:
            self.lampada.quente = True
        self.lampada.acesa = False

lampada1 = Lampada()
lampada2 = Lampada()
lampada3 = Lampada()
interruptor1 = Interruptor(lampada1)
interruptor2 = Interruptor(lampada2)
interruptor3 = Interruptor(lampada3)

interruptor1.ligar()
interruptor1.desligar()


interruptor2.ligar()

# descobrindo qual interruptor liga qual lâmpada a partir da temperatura!! :)
if lampada1.quente:
    print("O primeiro interruptor controla a primeira lâmpada.")
elif lampada1.acesa:
    print("O primeiro interruptor controla a segunda lâmpada.")
else:
    print("O primeiro interruptor controla a terceira lâmpada.")

if lampada2.quente:
    print("O segundo interruptor controla a primeira lâmpada.")
elif lampada2.acesa:
    print("O segundo interruptor controla a segunda lâmpada.")
else:
    print("O segundo interruptor controla a terceira lâmpada.")

if lampada3.quente:
    print("O terceiro interruptor controla a primeira lâmpada.")
elif lampada3.acesa:
    print("O terceiro interruptor controla a segunda lâmpada.")
else:
    print("O terceiro interruptor controla a terceira lâmpada.")