
from componente import Componente


class Robot:
    def __init__(self,codice: str,modello: str,applicazione: str,peso_massimo_componenti_kg: float,stato: str,) -> None:
        self.codice: str = codice
        self.modello: str = modello
        self.applicazione: str = applicazione
        self.peso_massimo_componenti_kg: float = peso_massimo_componenti_kg
        self.stato: str = stato
        self.componenti: list[Componente] = []

    def aggiungi_componente(self, componente: Componente) -> None:
       
        if any(c.codice == componente.codice for c in self.componenti):
            raise ValueError(
                f"Componente con codice '{componente.codice}' già presente nel"
                f" robot '{self.codice}'."
            )

        if (
            self.peso_componenti() + componente.peso_kg
            > self.peso_massimo_componenti_kg
        ):
            raise ValueError(
                f"Impossibile aggiungere '{componente.nome}'"
                f" ({componente.peso_kg} kg): supera il limite massimo di"
                f" {self.peso_massimo_componenti_kg} kg. Peso attuale:"
                f" {self.peso_componenti()} kg."
            )

        self.componenti.append(componente)

    def peso_componenti(self) -> float:
                return sum(c.peso_kg for c in self.componenti)

    def cerca_componente(self, codice: str) -> Componente | None:
        for c in self.componenti:
            if c.codice.lower() == codice.lower():
                return c
        return None

    def rimuovi_componente(self, codice: str) -> Componente | None:
        comp = self.cerca_componente(codice)
        if comp:
            self.componenti.remove(comp)
            return comp
        return None

    def componenti_sotto_peso(self, peso_massimo: float) -> list[Componente]:

        return [c for c in self.componenti if c.peso_kg <= peso_massimo]

    def __repr__(self) -> str:
        return (
            f"Robot(codice='{self.codice}', modello='{self.modello}', "
            f"stato='{self.stato}', n_componenti={len(self.componenti)})"
        )