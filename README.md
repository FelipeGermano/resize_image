# Editor de Imagens com Interface Gráfica

Este é um projeto em Python que permite redimensionar uma imagem, adicionar margens e desenhar uma linha ao redor da margem por meio de uma interface gráfica. Ele foi desenvolvido utilizando as bibliotecas `tkinter` para a interface e `Pillow` para manipulação de imagens.

## Funcionalidades
- Selecionar uma imagem de entrada nos formatos JPG ou PNG.
- Definir a largura e altura desejadas para a imagem.
- Adicionar uma margem ao redor da imagem.
- Desenhar uma linha preta ao longo da borda da margem.
- Salvar a imagem editada em um local especificado pelo usuário.

## Requisitos
- Python 3.7 ou superior.
- Bibliotecas necessárias:
  - `Pillow`
  - `tkinter` (nativo do Python)

## Instalação
1. Clone este repositório ou baixe os arquivos.
2. Certifique-se de que as bibliotecas necessárias estão instaladas:
   ```bash
   pip install pillow
   ```

## Como usar
1. Execute o script principal:
   ```bash
   python editor_de_imagens.py
   ```
2. Na janela que abrir:
   - Selecione uma imagem de entrada clicando em "Selecionar".
   - Insira a largura e altura desejadas para a imagem.
   - Defina o tamanho da margem em pixels.
   - Escolha o local e o nome do arquivo de saída clicando em "Selecionar".
   - Clique em "Executar" para processar a imagem.
3. A imagem processada será salva no local especificado.

## Geração de Executável
Para facilitar a distribuição, você pode gerar um arquivo executável usando `pyinstaller`:

1. Instale o `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Gere o executável:
   ```bash
   pyinstaller --onefile --noconsole editor_de_imagens.py
   ```
3. O executável será criado na pasta `dist`.

## Exemplo de Uso
### Entrada:
- Uma imagem JPG ou PNG.
- Largura: 800 pixels.
- Altura: 600 pixels.
- Margem: 50 pixels.

### Saída:
- Uma imagem redimensionada para 800x600 pixels com uma margem branca de 50 pixels e uma borda preta ao longo da margem.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas na página de issues.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

