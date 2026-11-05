

from componente import Componente
from robot import Robot


def registra_robot(robot_prodotti: list[Robot], robot: Robot) -> None:

    if any(r.codice.lower() == robot.codice.lower() for r in robot_prodotti):
        raise ValueError(
            f"Robot con codice '{robot.codice}' già registrato nel sistema."
        )
    robot_prodotti.append(robot)


def cerca_robot(robot_prodotti: list[Robot], codice: str) -> Robot | None:
    """Cerca un robot per codice ignorando maiuscole e minuscole."""
    for r in robot_prodotti:
        if r.codice.lower() == codice.lower():
            return r
    return None


def riepilogo_robot(nome_azienda: str, robot_prodotti: list[Robot]) -> None:
    print(f" RIEPILOGO PRODUZIONE: {nome_azienda.upper()}")

    if not robot_prodotti:
        print("Nessun robot registrato.")
        return

    for r in robot_prodotti:
        print(
            f" ID: {r.codice:<8} | Modello: {r.modello:<15} | Applicazione:"
            f" {r.applicazione:<12} | Stato: {r.stato:<15} | Peso"
            f" Componenti: {r.peso_componenti():.2f}/{r.peso_massimo_componenti_kg:.2f}"
            f" kg ({len(r.componenti)} installati)"
        )
    print("=" * 42)


if __name__ == "__main__":
    robot_prodotti: list[Robot] = []

    print("1. CREAZIONE E REGISTRAZIONE ROBOT")
    r1 = Robot("ROB-01", "Carrier-X100", "magazzino", 50.0, "in produzione")
    r2 = Robot("ROB-02", "Assist-V2", "assistenza", 30.0, "in collaudo")
    r3 = Robot("ROB-03", "HeavyLift-9000", "magazzino", 120.0, "pronto")
    r4 = Robot("ROB-04", "Sorter-Mini", "magazzino", 20.0, "in produzione")

    registra_robot(robot_prodotti, r1)
    registra_robot(robot_prodotti, r2)
    registra_robot(robot_prodotti, r3)
    registra_robot(robot_prodotti, r4)

    print("2. INSTALLAZIONE COMPONENTI DIFFERENZIATI")
    r1.aggiungi_componente(Componente("CMP-01", "Braccio Articolato A1", 15.5))
    r1.aggiungi_componente(Componente("CMP-02", "Sensore LIDAR 3D", 2.1))

    r2.aggiungi_componente(Componente("CMP-03", "Modulo Telecamera HD", 0.8))
    r2.aggiungi_componente(
        Componente("CMP-04", "Ruota Motrice Omnidirezionale", 8.4)
    )

    r3.aggiungi_componente(Componente("CMP-05", "Pinza Idraulica", 45.0))
    r3.aggiungi_componente(
        Componente("CMP-06", "Batteria ad Alta Capacità", 35.0)
    )

    r4.aggiungi_componente(
        Componente("CMP-07", "Nastro Trasportatore Compatto", 12.0)
    )
    r4.aggiungi_componente(Componente("CMP-08", "Sensore ad Ultrasuoni", 0.5))

    # Stampa del riepilogo
    riepilogo_robot("Physical AI Corp", robot_prodotti)

    print("\n3. TEST RICERCHE ROBOT ED ELEMENTI INESISTENTI")
    esito_r1 = cerca_robot(robot_prodotti, "rob-01")  # Test case-insensitivity
    print(
        f"Ricerca 'rob-01' (Esistente): Trovato ->"
        f" {esito_r1.modello if esito_r1 else 'Non trovato'}"
    )

    esito_rx = cerca_robot(robot_prodotti, "ROB-99")
    print(
        f"Ricerca 'ROB-99' (Inesistente): Trovato ->"
        f" {esito_rx.modello if esito_rx else 'Non trovato'}"
    )

    esito_cx = r1.cerca_componente("CMP-999")
    print(f"Ricerca componente 'CMP-999' su ROB-01: {esito_cx}")

    print("\n 4. TEST GESTIONE ECCEZIONI (TRY / EXCEPT)")
    # Tentativo A: registrazione robot duplicato
    try:
        registra_robot(
            robot_prodotti,
            Robot("ROB-01", "Duplicato", "magazzino", 50.0, "in produzione"),
        )
    except ValueError as err:
        print(f"[ECCEZIONE INTERCETTATA  Robot Duplicato]: {err}")

    # Tentativo B: aggiunta componente duplicato nel medesimo robot
    try:
        r1.aggiungi_componente(Componente("CMP-01", "Sensore Duplicato", 1.0))
    except ValueError as err:
        print(f"[ECCEZIONE INTERCETTATA Componente Duplicato]: {err}")

    # Tentativo C: superamento del peso massimo consentito
    try:
        r1.aggiungi_componente(Componente("CMP-99", "Payload Eccessivo", 100.0))
    except ValueError as err:
        print(f"[ECCEZIONE INTERCETTATA - Peso Eccessivo]: {err}")

    print("\n 5. TEST RIMOZIONE COMPONENTE ED ESPRESSIONE FILTRO")
    print("Ricerca iniziale CMP-03 su ROB-02:", r2.cerca_componente("CMP-03"))
    comp_rimosso = r2.rimuovi_componente("CMP-03")
    print(f"Componente rimosso con successo: {comp_rimosso}")
    print("Verifica ricerca post-rimozione:", r2.cerca_componente("CMP-03"))

    leggeri_r3 = r3.componenti_sotto_peso(40.0)
    print(
        f"\nComponenti con peso <= 40 kg su ROB-03 (filtrati con List"
        f" Comprehension): {leggeri_r3}"
    )


