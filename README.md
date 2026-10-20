# ONOFF Links

Pagina link-in-bio per l'Instagram di ONOFF (@onoff.zone). Riproduce la griglia dei post: ogni riquadro apre il progetto (Projects) o l'articolo (Mag) corrispondente su onoff.zone, versione italiana. In cima ci sono i link a sito, progetti, mag e contatti.

## Come si aggiorna

Tutto il contenuto sta in `posts.json`:

- `links`: i pulsanti in cima (etichetta + url)
- `posts`: i riquadri della griglia, dal più recente al più vecchio
- `skipped`: post Instagram esclusi di proposito (nessun progetto o articolo dedicato), così non vengono riproposti

Per aggiungere un post, inserisci un nuovo oggetto in cima a `posts`:

```json
{
  "id": "CODICE_DEL_POST",
  "date": "2026-10-19",
  "permalink": "https://www.instagram.com/onoff.zone/p/CODICE_DEL_POST/",
  "title": "Nome del progetto",
  "url": "https://onoff.zone/it/projects/slug-progetto",
  "image": "assets/posts/CODICE_DEL_POST.jpg",
  "source_image": "URL della prima immagine del post su Instagram"
}
```

Al push su `main`, la GitHub Action `Publish link page`:

1. scarica in `assets/posts/` le copertine che mancano (i link delle immagini Instagram scadono dopo qualche settimana, quindi vengono salvate subito nel repo)
2. pubblica il sito su GitHub Pages

## Struttura

- `index.html`: pagina (stile onoff.zone: nero, bianco, Figtree, nav a pillola)
- `posts.json`: dati
- `assets/logo.svg`: logo ONOFF
- `assets/posts/`: copertine dei post
- `scripts/fetch_images.py`: download copertine
- `.github/workflows/deploy.yml`: pubblicazione
