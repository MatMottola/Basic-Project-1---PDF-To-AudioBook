# PDF to AudioBook 🎧

Conversor de PDFs em audiolivros via linha de comando, desenvolvido em Python.
Selecione qualquer arquivo PDF e ouça o conteúdo em voz sintetizada,
com suporte a interrupção instantânea via teclado e leitura página a página.

## Funcionalidades

- Seleção de arquivo PDF por interface gráfica (Tkinter)
- Conversão de texto em voz com pyttsx3 (offline, sem API externa)
- Leitura página a página com detecção de páginas vazias
- Interrupção instantânea pressionando ESC — sem travar o programa
- Execução em threads separadas: leitura e monitoramento de teclado
  rodam em paralelo sem bloquear um ao outro
- Tratamento de arquivos inválidos ou vazios

## Como usar

```bash
pip install pyttsx3 PyPDF2 keyboard
python pdf_to_audiobook.py
```

1. Uma janela de seleção de arquivo será aberta
2. Selecione o PDF desejado
3. A leitura começa automaticamente
4. Pressione **ESC** a qualquer momento para interromper

## Tecnologias

- Python 3.x
- `pyttsx3` — síntese de voz offline
- `PyPDF2` — extração de texto de PDFs
- `tkinter` — interface gráfica para seleção de arquivo
- `threading` — execução paralela de leitura e controle
- `keyboard` — captura de input do teclado em tempo real

## Decisões técnicas

- **Multithreading:** a escuta do ESC roda em thread daemon separada,
  garantindo que o programa responda ao comando de parada sem
  interromper o fluxo principal de leitura
- **Síntese offline:** pyttsx3 não depende de conexão ou API externa,
  tornando o uso viável em qualquer ambiente
- **os._exit(0):** encerramento forçado ao final para evitar
  travamento de threads residuais do pyttsx3

