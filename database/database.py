import pymongo

class Database:
    def __init__(self, database_name: str):
        self.connect(database_name)

    def connect(self, database_name: str):
        try:
            connection_string = "mongodb://localhost:27017/"
            self.client = pymongo.MongoClient(connection_string, tlsAllowInvalidCertificates=True)
            self.db = self.client[database_name]
            print(f"Conectado ao banco de dados '{database_name}' com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar: {e}")

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def reset_collection(self, collection_name: str, dataset: list):
        try:
            self.db.drop_collection(collection_name)
            if dataset:
                self.db[collection_name].insert_many(dataset)
            print(f"Collection '{collection_name}' resetada com sucesso!")
        except Exception as e:
            print(f"Erro ao resetar collection: {e}")
    def close(self):
        if hasattr(self, 'client') and self.client:
            self.client.close()
            print("Conexão com o MongoDB fechada com sucesso!")