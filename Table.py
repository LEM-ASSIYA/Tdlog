class Table:
    def __init__(self, id_table, capacite):
        self.id_table = id_table
        self.capacite = capacite

    def assigner_table(self):
        print(f"La table {self.id_table} est assignée.")

    def liberer_table(self):
        print(f"La table {self.id_table} est libérée.")