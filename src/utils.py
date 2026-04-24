# src/utils.py
def normalizar_cpf(cpf: str) -> str:
    """Remove pontos, traços e espaços de um CPF."""
    if not cpf:
        return ""
    return ''.join(filter(str.isdigit, cpf))