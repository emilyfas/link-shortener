# Encurtador de Links
Um encurtador de URLs simples e elegante feito com Flask, permitindo transformar links longos em URLs curtas, ideais para compartilhamento. O projeto inclui uma interface moderna com suporte a temas claro/escuro, além de funcionalidades úteis como expiração automática dos links após 7 dias.

## 📸 Demonstração

![Demonstração troca de tema](static/images/ezgif-15b5357eb86f3f.gif)

Demonstração

## Funcionalidades
**1.** Encurta links longos

**2.** Links expiram automaticamente após 7 dias

**3.** Alternância entre modo claro e escuro

**4.** Redirecionamento automático de URLs curtas

**5.** Validação de links

**6.** Interface estilizada com TailwindCSS

**7.** Armazenamento usando SQLite

## Estrutura do Projeto

```

link-shortener/
│
├── .venv/                  # Ambiente virtual (não versionado)
├── instance/
│   └── database.db         # Banco de dados SQLite
│
├── models/
│   └── models.py           # Modelo de dados para os links
│
├── static/
│   ├── images/             # Imagens estáticas (logo, ícone, banner)
│   ├── scripts/
│   │   └── script.js       # Script JS (tema escuro/claro)
│   └── styles/
│       └── style.css       # Estilos personalizados
│
├── templates/
│   ├── base.html           # Template base com navbar e footer
│   ├── index.html          # Página principal
│   ├── about.html          # Página "Sobre o Projeto"
│   ├── contact.html        # Página de contato
│   ├── link_expired.html   # Página de link expirado
│   └── 404.html            # Página de erro 404
│
├── app.py                 # Arquivo principal da aplicação Flask
├── extensions.py          # Inicialização do SQLAlchemy
├── requirements.txt       # Dependências do projeto
└── LICENSE                # Licença MIT

```

# Como funciona






