# Site ProPodium Events & Hospitality — como instalar

## O que tem nesta pasta
- `index.html`, `about.html`, `services.html`, `events.html`, `partners.html`, `contact.html`: as páginas principais.
- `events/`: as páginas de cada categoria de eventos (`motorsport.html`, `sports.html`, `festivals.html`, `business.html`, `government.html`) e a de eventos passados (`past-events.html`).
- `assets/`: estilo (css), script do menu e do formulário (js) e as imagens da marca (img).
- `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`: ícones do navegador e do celular.
- `robots.txt`, `sitemap.xml`, `site.webmanifest`: arquivos para o Google e para celulares.

É um site estático: só HTML e CSS, sem banco de dados e sem instalação de programas.

## 1. Antes de publicar: troque os dados de contato
Os campos de contato estão marcados com dois textos provisórios:
- `EMAIL_AQUI` → seu e-mail de contato
- `TELEFONE_AQUI` → seu telefone

Eles aparecem em todas as páginas (rodapé e página Contact) e em `assets/js/main.js`.
Os e-mails dos eventos (por exemplo `f1austin@propodiumevents.com`) e o `leo@propodiumevents.com` vieram do PDF de textos: confira se essas caixas existem antes de publicar.
No VS Code ou no Notepad++, use "Substituir em arquivos" (Ctrl+Shift+H) na pasta inteira.

## 2. Fotos
As "Media Suggestion" do PDF aparecem como quadros "Photo placeholder" com a descrição da foto.
Quando tiver as fotos, troque cada quadro por uma imagem (`<img src="assets/img/nome-da-foto.jpg" alt="descrição">`). Use só fotos com direito de uso e sem marcas de terceiros.

## 3. Ver no seu computador
Abra a pasta e dê dois cliques em `index.html`.

## 4. Publicar (só quando você decidir)
Qualquer hospedagem de site estático serve. Opções comuns:
- **Netlify** ou **Cloudflare Pages**: arraste a pasta para o painel e o site sobe em minutos.
- **Hostinger, GoDaddy etc.**: envie os arquivos para a pasta `public_html` pelo gerenciador de arquivos.

Depois aponte o domínio para a hospedagem escolhida, seguindo as instruções dela.
As páginas também abrem sem o `.html` (por exemplo `/events/motorsport`) na maioria das hospedagens, como Netlify e Cloudflare Pages.

## 5. Domínio
O sitemap, o robots e as tags de SEO usam `https://www.propodiumevents.com`.
Se o domínio final for outro, substitua `www.propodiumevents.com` em todos os arquivos.

## 6. Formulário de contato
O botão "Send request" abre o programa de e-mail do visitante com a mensagem pronta para o seu e-mail.
Se quiser receber direto no e-mail sem depender disso, dá para ligar o formulário a um serviço como Formspree ou Netlify Forms.

## Importante
Nada foi publicado, nenhum domínio foi comprado e nenhum DNS foi alterado. Isso só acontece com o seu "sim".
