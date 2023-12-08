""""AUTOR DO CÓDIGO: Marcos Vinícius Elias Neres Barreto Ferreira"""

class database:

    def __init__(self, *args):

        for colunas in args:
            exec(f'self.{colunas} = []') # ou setattr(self, colunas, [])

    def get_colunas(self, nome_coluna):
        return getattr(self, nome_coluna)

    def set_coluna(self, nome_coluna, dados):

        exec(f'self.{nome_coluna}.append("{dados}")') # ou setattr(self, nome_coluna, dados)

    def obtendo_todos_dados(self, num_id, lista_colunas):

        posi_id = None
        tamanho_lista = len(lista_colunas)
        tamanho_id = len(getattr(self, 'id'))
        all_dados = []

        for i in range(tamanho_id):
            id_atual = getattr(self, 'id')[i]

            if str(num_id) == id_atual:
                posi_id = i

        if posi_id is not None:
            for i in range(tamanho_lista):
                all_dados.append(getattr(self, lista_colunas[i])[posi_id])

        return all_dados


colunas = ['id', 'nome', 'idade']

bd = database(colunas[0], colunas[1], colunas[2]) # ou bd = database(*colunas)

# Cadastrando Marcos
bd.set_coluna('id', 1)
bd.set_coluna('nome', 'Marcos')
bd.set_coluna('idade', 20)

# Cadastrando João
bd.set_coluna('id', 2)
bd.set_coluna('nome', 'João')
bd.set_coluna('idade', 10)

print('=' * 40 + '\n' + ' ' * 15 + 'COLUNAS\n' + "=" * 40)
print(f"\nColuna ID: {bd.get_colunas('id')}\nColuna Nome: {bd.get_colunas('nome')}\nColuna Idade: {bd.get_colunas('idade')}\n")
print('=' * 40 + '\n' + ' ' * 10 + 'PESQUISA POR ID\n' + "=" * 40)
print('\nDados Marcos:', bd.obtendo_todos_dados(1, colunas), '\nDados João:', bd.obtendo_todos_dados(2, colunas))
