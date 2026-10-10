# Manual do Criador — Pokemon UltraRed v1.0

Fork: https://github.com/thaynansusyt-jpg/Pokemon-UltraRed

## O que o kit entrega
- Uma primeira mudanca real: `STANDARD_IV` muda de 10 para 15 em `src/config.h`.
- O script `tools/starter_check.py`, que confere arquivos e configuracoes.
- Um workflow no GitHub Actions que executa o verificador sem precisar de computador.

**Atencao:** o teste NAO produz uma ROM jogavel ou um patch. A CFRU precisa de um fluxo separado de compilacao e aplicacao a uma copia legal do jogo-base. Nunca suba ROMs comerciais ao repositorio.

## Instalacao segura
1. Abra a branch `starter-kit-v1` no seu fork.
2. Revise os commits e, se estiver tudo certo, mescle o pull request com a branch `master`.
3. Abra a aba **Actions**; habilite GitHub Actions se solicitado.
4. Selecione **UltraRed - Primeiro Teste (sem ROM)**.
5. Toque em **Run workflow** (apos a mesclagem), execute na master e abra o resultado.
6. Se estiver verde, confira o resumo e o artifact `ultrared-primeiro-teste`.

*Observacao:* a execucao manual `workflow_dispatch` costuma exigir que o workflow ja exista na branch padrao. Antes de mesclar, a execucao automatica de push na branch tambem pode aparecer no Actions.

## Exercício rapido no celular
1. Entre em `src/config.h` e encontre `#define STANDARD_IV 15`.
2. Toque no lapis e altere **15** para **20**.
3. Salve com **Commit changes**.
4. Execute o workflow e procure `STANDARD_IV = 20` no relatorio.

**O que o codigo significa?** `#define` define uma configuracao do pre-processador C; `STANDARD_IV` e o nome, e o numero e o valor. O script valida se o numero esta entre 0 e 31. Uma configuracao alterada nao aparece no jogo ate a base real ser compilada/aplicada.

## Entendendo o resultado
- Verde / **APROVADO**: estrutura, sintaxe Python e configuracoes verificadas passaram.
- Vermelho / **FALHOU**: abra o log e leia o primeiro erro.
- Workflow ausente: confira a branch, a mesclagem e se Actions esta ativo.
- Se o navegador celular ocultar opcoes, use **Site para computador**.

## Caminho para o jogo real
1. Validar o starter.
2. Configurar as ferramentas de compilacao ARM, Python e utilitarios de imagem/som exigidos pela CFRU.
3. Fazer um teste de compilacao isolado do motor, sem distribuir ROM de terceiros.
4. Construir e testar uma ROM apenas sobre uma copia compativel obtida de forma legitima.
5. Distribuir patches e documentar creditos/permissoes, nunca ROM comercial.

## Regras do projeto
- Commits pequenos, uma ideia de cada vez.
- Mantenha backups e anote bugs.
- Nao compartilhe senhas, tokens ou codigos de autenticacao.
- Se for compartilhar tela, confirme se o recurso existe no seu modo de chamada. Quando indisponivel, use capturas de tela; eu nao enxergo sua tela automaticamente.

## Proxima aula
Interpretar o primeiro resultado e mapear, com calma, a compilacao real da CFRU.

Fonte: https://github.com/Skeli789/Complete-Fire-Red-Upgrade
