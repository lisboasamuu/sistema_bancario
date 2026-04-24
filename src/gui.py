import tkinter as tk
from tkinter import ttk, messagebox
import contextlib
import io

from .banco import Banco
from .utils import normalizar_cpf

class BancoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 Sistema Bancário")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Instância do banco (já carrega dados automaticamente)
        self.banco = Banco()

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 11), padding=5)
        self.style.configure("TLabel", font=("Arial", 11))

        # Título
        titulo = ttk.Label(root, text="Sistema Bancário do Samuca", font=("Arial", 20, "bold"))
        titulo.pack(pady=20)

        # Frame para os botões principais
        frame_botoes = ttk.Frame(root)
        frame_botoes.pack(pady=10)

        botoes = [
            ("➕ Criar Conta", self.criar_conta_ui),
            ("💰 Depositar", self.depositar_ui),
            ("💸 Sacar", self.sacar_ui),
            ("🔄 Transferir", self.transferir_ui),
            ("📊 Consultar Saldo", self.saldo_ui),
            ("📜 Ver Histórico", self.historico_ui),
            ("📋 Listar Contas", self.listar_contas_ui),
            ("🚪 Sair", self.sair)
        ]

        for texto, comando in botoes:
            btn = ttk.Button(frame_botoes, text=texto, width=25, command=comando)
            btn.pack(pady=6)

        # Rodapé
        rodape = ttk.Label(root, text="Dados salvos automaticamente", font=("Arial", 9))
        rodape.pack(side=tk.BOTTOM, pady=10)

    # -------------------- Métodos auxiliares --------------------
    def capturar_saida(self, funcao, *args, **kwargs):
        """Executa uma função e captura tudo o que ela imprime no console."""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            resultado = funcao(*args, **kwargs)
        saida = f.getvalue()
        return resultado, saida

    def mostrar_mensagem(self, titulo, mensagem, erro=False):
        """Exibe uma messagebox (erro ou informação)."""
        if erro:
            messagebox.showerror(titulo, mensagem)
        else:
            messagebox.showinfo(titulo, mensagem)

    def obter_cpf(self, mensagem="CPF do titular:"):
        """Janela simples para digitar CPF."""
        return self._obter_entrada("CPF", mensagem)

    def obter_valor(self, mensagem="Valor (R$):"):
        """Janela simples para digitar valor numérico."""
        valor_str = self._obter_entrada("Valor", mensagem)
        if valor_str is None:
            return None
        try:
            # Aceita vírgula ou ponto
            valor = float(valor_str.replace(",", "."))
            return valor
        except ValueError:
            self.mostrar_mensagem("Erro", "Valor inválido. Use números (ex: 150.75).", erro=True)
            return None

    def _obter_entrada(self, titulo, rotulo):
        """Janela genérica com campo de entrada."""
        dialog = tk.Toplevel(self.root)
        dialog.title(titulo)
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        dialog.grab_set()  # modal

        ttk.Label(dialog, text=rotulo).pack(pady=10)
        entry = ttk.Entry(dialog, width=30)
        entry.pack(pady=5)
        entry.focus()

        resultado = None

        def ok():
            nonlocal resultado
            resultado = entry.get().strip()
            dialog.destroy()

        def cancelar():
            dialog.destroy()

        frame_botoes = ttk.Frame(dialog)
        frame_botoes.pack(pady=15)
        ttk.Button(frame_botoes, text="OK", width=10, command=ok).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botoes, text="Cancelar", width=10, command=cancelar).pack(side=tk.LEFT, padx=5)

        self.root.wait_window(dialog)
        return resultado

    # -------------------- Operações --------------------
    def criar_conta_ui(self):
        cpf = self.obter_cpf("CPF (apenas números ou com formatação):")
        if not cpf:
            return
        nome = self._obter_entrada("Criar Conta", "Nome completo do titular:")
        if not nome:
            return

        resultado, saida = self.capturar_saida(self.banco.criar_conta, cpf, nome)
        if resultado is not None:
            self.mostrar_mensagem("Sucesso", f"Conta criada com sucesso!\nCPF: {cpf}\nTitular: {nome}")
        else:
            # A mensagem de erro já está na 'saida' (ex: "Já existe uma conta...")
            self.mostrar_mensagem("Erro", saida if saida else "Falha ao criar conta.", erro=True)

    def depositar_ui(self):
        cpf = self.obter_cpf("CPF da conta para depósito:")
        if not cpf:
            return
        valor = self.obter_valor("Valor a depositar (R$):")
        if valor is None:
            return

        _, saida = self.capturar_saida(self.banco.depositar, cpf, valor)
        # Como depositar retorna bool, a mensagem de sucesso/erro está em saida
        if "✅" in saida or "Depósito efetuado" in saida:
            self.mostrar_mensagem("Depósito", saida)
        else:
            self.mostrar_mensagem("Erro", saida if saida else "Falha no depósito.", erro=True)

    def sacar_ui(self):
        cpf = self.obter_cpf("CPF da conta para saque:")
        if not cpf:
            return
        valor = self.obter_valor("Valor a sacar (R$):")
        if valor is None:
            return

        _, saida = self.capturar_saida(self.banco.sacar, cpf, valor)
        if "✅" in saida or "Saque efetuado" in saida:
            self.mostrar_mensagem("Saque", saida)
        else:
            self.mostrar_mensagem("Erro", saida if saida else "Falha no saque.", erro=True)

    def transferir_ui(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Transferência")
        dialog.geometry("400x320")
        dialog.resizable(False, False)
        dialog.grab_set()

        # CPF origem
        ttk.Label(dialog, text="CPF da conta de ORIGEM:").pack(pady=(10,0))
        cpf_origem_entry = ttk.Entry(dialog, width=30)
        cpf_origem_entry.pack(pady=5)

        # CPF destino
        ttk.Label(dialog, text="CPF da conta de DESTINO:").pack(pady=(10,0))
        cpf_destino_entry = ttk.Entry(dialog, width=30)
        cpf_destino_entry.pack(pady=5)

        # Valor
        ttk.Label(dialog, text="Valor (R$):").pack(pady=(10,0))
        valor_entry = ttk.Entry(dialog, width=30)
        valor_entry.pack(pady=5)

        # Modalidade (nova)
        ttk.Label(dialog, text="Modalidade:").pack(pady=(10,0))
        modalidade_var = tk.StringVar()
        modalidade_combo = ttk.Combobox(dialog, textvariable=modalidade_var, values=["Pix", "TED", "DOC"], width=27)
        modalidade_combo.pack(pady=5)
        modalidade_combo.set("Pix")   # valor padrão

        def transferir():
            cpf_origem = cpf_origem_entry.get().strip()
            cpf_destino = cpf_destino_entry.get().strip()
            valor_str = valor_entry.get().strip()
            modalidade = modalidade_var.get().strip()

            if not cpf_origem or not cpf_destino or not valor_str or not modalidade:
                messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
                return
            try:
                valor = float(valor_str.replace(",", "."))
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido.")
                return

            # Chama o método transferir com a modalidade
            _, saida = self.capturar_saida(self.banco.transferir, cpf_origem, cpf_destino, valor, modalidade)
            if "sucesso" in saida.lower() or "✅" in saida:
                messagebox.showinfo("Transferência", saida)
                dialog.destroy()
            else:
                messagebox.showerror("Erro", saida if saida else "Falha na transferência.")

        botoes_frame = tk.Frame(dialog)
        botoes_frame.pack(pady=20)

        tk.Button(botoes_frame, text="Transferir", width=12, command=transferir).pack(side=tk.LEFT, padx=5)
        tk.Button(botoes_frame, text="Cancelar", width=12, command=dialog.destroy).pack(side=tk.LEFT, padx=5)
    def saldo_ui(self):
        cpf = self.obter_cpf("CPF da conta para consultar saldo:")
        if not cpf:
            return
        # o método exibir_saldo apenas imprime, capturamos a saída
        _, saida = self.capturar_saida(self.banco.exibir_saldo, cpf)
        if "Conta não encontrada" in saida or not saida.strip():
            self.mostrar_mensagem("Erro", saida if saida else "Conta não encontrada.", erro=True)
        else:
            self.mostrar_mensagem("Saldo", saida)

    def historico_ui(self):
        cpf = self.obter_cpf("CPF da conta para ver histórico:")
        if not cpf:
            return
        _, saida = self.capturar_saida(self.banco.ver_historico, cpf)
        if "Conta não encontrada" in saida or not saida.strip():
            self.mostrar_mensagem("Erro", saida if saida else "Conta não encontrada.", erro=True)
        else:
            # xibir em uma janela com barra de rolagem
            self.mostrar_texto_longo("Histórico de Movimentações", saida)

    def listar_contas_ui(self):
        _, saida = self.capturar_saida(self.banco.listar_contas)
        if "Nenhuma conta cadastrada" in saida or not saida.strip():
            self.mostrar_mensagem("Lista de Contas", saida if saida else "Nenhuma conta encontrada.")
        else:
            self.mostrar_texto_longo("Contas Cadastradas", saida)

    def mostrar_texto_longo(self, titulo, texto):
        """mostra uma janela com texto e barra de rolagem."""
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("500x400")

        frame = ttk.Frame(janela)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        text_widget = tk.Text(frame, wrap=tk.WORD, font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget.insert(tk.END, texto)
        text_widget.configure(state=tk.DISABLED)  # somente leitura

        btn_fechar = ttk.Button(janela, text="Fechar", command=janela.destroy)
        btn_fechar.pack(pady=10)

    def sair(self):
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.root.destroy()


# ponto de entrada
def main():
    root = tk.Tk()
    app = BancoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()