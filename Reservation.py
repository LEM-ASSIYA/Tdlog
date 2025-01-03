class Reservation:
    def __init__(self, id_reservation, nom, date_reservation=None, heure_reservation=None):
        """
        Initialise une réservation.

        :param id_reservation: Identifiant unique de la réservation
        :param nom: Nom du client pour la réservation
        :param date_reservation: Date de la réservation (optionnelle)
        :param heure_reservation: Heure de la réservation (optionnelle)
        """
        self.id_reservation = id_reservation
        self.nom = nom
        self.date_reservation = date_reservation
        self.heure_reservation = heure_reservation

    def __str__(self):
        return (f"Réservation ID: {self.id_reservation}, Nom: {self.nom}, "
                f"Date: {self.date_reservation or 'Non spécifiée'}, "
                f"Heure: {self.heure_reservation or 'Non spécifiée'}")
