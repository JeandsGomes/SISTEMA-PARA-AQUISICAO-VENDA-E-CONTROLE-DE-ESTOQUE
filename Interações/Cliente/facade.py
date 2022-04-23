from PyQt5.QtCore import QDate

class Facade:
    def __init__(self,main_telas):
        self.main_tela = main_telas

    def reseta_lines_edite_funcionario(self):
        #self.tela_cadastro.lineEdit_cadastro_nome.setText('')
        self.main_tela.tela_cadastro.cadastro_lineEdit_nome_completo.setText('')
        self.main_tela.tela_cadastro.cadastro_lineEdit_cpf.setText('')
        date = QDate(2000, 1, 1)
        self.main_tela.tela_cadastro.cadastro_lineEdit_data_nascimento.setDate(date)
        self.main_tela.tela_cadastro.cadastro_lineEdit_email.setText('')
        self.main_tela.tela_cadastro.cadastro_lineEdit_telefone.setText('')
        #self.main_tela.tela_cadastro.cadastro_lineEdit_telefone_2.setText('')
        self.main_tela.tela_cadastro.cadastro_lineEdit_senha.setText('')

    def reseta_lines_edite_cliente_cadastra(self):
        self.main_tela.tela_cadastra_cliente.lineEdit_nome_completo.setText('')
        self.main_tela.tela_cadastra_cliente.lineEdit_cpf.setText('')
        self.main_tela.tela_cadastra_cliente.lineEdit_endereco.setText('')
        self.main_tela.tela_cadastra_cliente.lineEdit_data_nascimento.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_cadastra_cliente.lineEdit_email.setText('')
        self.main_tela.tela_cadastra_cliente.lineEdit_n_telefone.setText('')

    def reseta_lines_edite_Cliente_busco(self):
        self.main_tela.tela_busca_modifica_cliente.lineEdit_cpf.setText('')
        self.main_tela.tela_busca_modifica_cliente.lineEdit_nome.setText('')
        self.main_tela.tela_busca_modifica_cliente.lineEdit_endereco.setText('')
        self.main_tela.tela_busca_modifica_cliente.lineEdit_nascimento.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_busca_modifica_cliente.lineEdit_email.setText('')
        self.main_tela.tela_busca_modifica_cliente.lineEdit_telefone.setText('')
        self.main_tela.tela_busca_modifica_cliente.lineEdit_busca_cpf.setText('')

    def reseta_lines_edite_fornecedor_cadastra(self):
        self.main_tela.tela_cadastra_fornecedor.lineEdit_razao_social.setText('')
        self.main_tela.tela_cadastra_fornecedor.lineEdit_cnpj.setText('')
        self.main_tela.tela_cadastra_fornecedor.lineEdit_nacionalidade.setText('')
        self.main_tela.tela_cadastra_fornecedor.lineEdit_endereco.setText('')
        self.main_tela.tela_cadastra_fornecedor.lineEdit_telefone.setText('')
        self.main_tela.tela_cadastra_fornecedor.lineEdit_pessoa.setText('')

    def reseta_lines_edite_fornecedor_busca(self):
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_nacionalida.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_endereco.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_telefone.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText('')
        self.main_tela.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.setText('')

    def resetar_lines_edite_produto_cadastro(self):
        self.main_tela.tela_cadastra_produto.lineEdit_n_bebida.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_nome_bebida.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_data_fabricacao.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_cadastra_produto.lineEdit_data_vencimento_2.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_cadastra_produto.lineEdit_condicoes.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_quantidade.setValue(0)
        self.main_tela.tela_cadastra_produto.lineEdit_local.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_v_compra_uni.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_re_venda_uni.setText('')
        self.main_tela.tela_cadastra_produto.lineEdit_id_forncedor.setText('')

    def resetar_lines_edite_produto_busca(self):
        self.main_tela.tela_busca_modifica_produto.lineEdit_6.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_3.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_7.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_busca_modifica_produto.lineEdit_14.setDate(QDate(2000, 1, 1))
        self.main_tela.tela_busca_modifica_produto.lineEdit_15.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_8.setValue(0)
        self.main_tela.tela_busca_modifica_produto.lineEdit_9.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_10.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_12.setText('')
        self.main_tela.tela_busca_modifica_produto.lineEdit_11.setText('')