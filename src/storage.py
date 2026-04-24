import os
import json

class JSONStorage:
    @staticmethod
    def save(data, filename):
        '''Salvar os dados num arquivo JSON'''
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            #metodo para serializar uma string em python para uma string em json
    @staticmethod
    def load(filename):
        '''carregar os dados e retornar none se não existir'''
        if not os.path.exists(filename):
            return None
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
