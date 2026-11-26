# Site Pro Podium Events & Hospitality — como instalar

## O que tem nesta pasta
- `index.html`, `about.html`, `services.html`, `events.html`, `partners.html`, `contact.html`: as páginas principais.
- `events/`: as páginas de cada categoria de eventos (`motorsport.html`, `sports.html`, `festivals.html`, `business.html`, `government.html`).
- `assets/`: estilo (css), script do menu e dos formulários (js) e as imagens da marca (img).
- `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`: ícones do navegador e do celular.
- `robots.txt`, `sitemap.xml`, `site.webmanifest`: arquivos para o Google e para celulares.

É um site estático: só HTML e CSS, sem banco de dados e sem instalação de programas.

## 1. Contato
O contato do site já está preenchido: `info@propodiumevents.com` e `(737) 202-7261`.
Os e-mails dos eventos (por exemplo `f1austin@propodiumevents.com`) e o `leo@propodiumevents.com` nas páginas de categoria vieram do PDF de textos: confira se essas caixas existem antes de publicar.

## 2. Reviews
- O botão "Leave a review" abre o formulário (Name, Company / Role, Event, Rating, Your review e a caixa de autorização).
- Ao enviar, o programa de e-mail do visitante abre com o review pronto para `info@propodiumevents.com`, e aparece a mensagem "Thank you! Your review will appear on our site once approved."
- Nada vai ao ar sozinho. Para publicar um review aprovado, abra `source/content.py` no repositório propodium-site do GitHub, adicione o review na lista `REVIEWS` (estrelas, texto, nome, cargo e evento) e gere o site de novo com `python3 source/build.py`. Enquanto a lista estiver vazia, a lista de reviews fica escondida.
- Publique somente reviews reais, de quem marcou a caixa de autorização.

## 3. Fotos
As "Media Suggestion" do PDF aparecem como quadros "Photo placeholder" com a descrição da foto.
Quando tiver as fotos, troque cada quadro por uma imagem (`<img src="assets/img/nome-da-foto.jpg" alt="descrição">`). Use só fotos com direito de uso e sem marcas de terceiros.

## 4. Ver no seu computador
Abra a pasta e dê dois cliques em `index.html`.

## 5. Publicar (só quando você decidir)
Qualquer hospedagem de site estático serve. Opções comuns:
- **Netlify** ou **Cloudflare Pages**: arraste a pasta para o painel e o site sobe em minutos.
- **Hostinger, GoDaddy etc.**: envie os arquivos para a pasta `public_html` pelo gerenciador de arquivos.

Depois aponte o domínio `propodiumevents.com` para a hospedagem escolhida, seguindo as instruções dela.
As páginas também abrem sem o `.html` (por exemplo `/events/motorsport`) na maioria das hospedagens, como Netlify e Cloudflare Pages.

## 6. Domínio
O sitemap, o robots e as tags de SEO usam `https://www.propodiumevents.com`.
Se o domínio final for outro, substitua `www.propodiumevents.com` em todos os arquivos.

## 7. Formulários
Os botões "Send request" e "Submit review" abrem o programa de e-mail do visitante com a mensagem pronta para `info@propodiumevents.com`.
Se quiser receber direto no e-mail sem depender disso, dá para ligar os formulários a um serviço como Formspree ou Netlify Forms.

## Antes de publicar (do seu PDF)
- Confirmar que todos os eventos da lista foram realmente atendidos pela Pro Podium.
- Pedir autorização antes de exibir nomes de clientes ou parceiros.

## Importante
Nada foi publicado no domínio próprio e nenhum DNS foi alterado. Isso só acontece com o seu "sim".
