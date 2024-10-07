class Table:
    def __init__(self, id_table, num_table, capacite):
        self.id_table = id_table
        self.num_table = num_table
        self.capacite = capacite

    def assigner_table(self):
        print(f"La table {self.num_table} est assignée.")

    def liberer_table(self):
        print(f"La table {self.num_table} est libérée.")