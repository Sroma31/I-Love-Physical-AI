


class Componente:


    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:

        if peso_kg < 0:
            raise ValueError("Il peso del componente non può essere negativo.")

        self.codice: str = codice
        self.nome: str = nome
        self.peso_kg: float = peso_kg

    def __repr__(self) -> str:
        return (
            f"Componente(codice='{self.codice}', nome='{self.nome}', "
            f"peso_kg={self.peso_kg})"
        )